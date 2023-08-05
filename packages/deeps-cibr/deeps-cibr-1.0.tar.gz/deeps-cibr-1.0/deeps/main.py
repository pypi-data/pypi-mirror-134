#! python
# @Time    : 21/08/09 下午 03:46
# @Author  : azzhu 
# @FileName: main.py
# @Software: PyCharm
import itertools
import time
from pathlib import Path
from threading import Thread

import copy
import cv2
import numpy as np
import torch
from torch import nn
from types import GeneratorType

from deeps.model_torch import Unet_sr
from deeps.utils import Pbar, download_weights

'''
运行方式：
module load cuda/10.0
module load cudnn/7.4.2
srun -p q_ai -c 2 -w ai01 --gres=gpu:1 /GPFS/zhangli_lab_permanent/zhuqingjie/env/py3_tf2/bin/python main.py
'''


# os.environ["CUDA_VISIBLE_DEVICES"] = '1,2,3,4,5,6,7'


# 异步装饰器
def _async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def sub(g: np.ndarray, r: np.ndarray) -> np.ndarray:
    '''
    两张图像按照一定规则相减，规则：
    if g>=r:
        g-r
    else:
        0

    并不一定非得是一张2D图像，3D也可以
    :param g:   绿色通道
    :param r:   红色通道
    :return:
    '''
    g = g.astype(np.float32)
    r = r.astype(np.float32)
    res = g - r
    res = np.clip(res, 0, None)
    return res


def load_files(cfg) -> list:
    data_dir = cfg['path']
    ranges = cfg['ranges']

    files = []
    if cfg['sub']:
        sub_dim = cfg['sub_dim']
        sub_range = ranges.pop(sub_dim)
        if cfg['sub_reverse']:
            sub0, sub1 = sub_range[1], sub_range[0]
        else:
            sub0, sub1 = sub_range[0], sub_range[1]

        for ids in itertools.product(*[range(r[0], r[1] + 1) for r in ranges]):
            ids = list(ids)
            ids.insert(sub_dim, sub0)
            p1 = Path(data_dir, cfg['file_name_fmt'].format(*ids))
            ids[sub_dim] = sub1
            p2 = Path(data_dir, cfg['file_name_fmt'].format(*ids))
            files.append([p1, p2])
    else:
        for ids in itertools.product(*[range(r[0], r[1] + 1) for r in ranges]):
            files.append(Path(data_dir, cfg['file_name_fmt'].format(*ids)))

    return files


class Data():
    def __init__(self, all_files: list, batchsize: int, sub: bool):
        '''
            每次返回一个batchsize的数据
            :param all_files:
            :return:
            '''
        self.all_files = all_files
        self.batch_size = batchsize

        self.had_gen_batch = False
        self.batch_data = None
        if sub:
            self.get_data_loader = self.get_data_loader1
        else:
            self.get_data_loader = self.get_data_loader2
        self.__get_batch_fn()

    # 有减法操作
    def get_data_loader1(self) -> GeneratorType:
        res = []
        filenames = []  # 只保存了其中一个通道的filename，就绿色吧
        for gp, rp in self.all_files:
            g = cv2.imread(str(gp), cv2.IMREAD_UNCHANGED)
            # g = np.zeros([100, 100])
            if g is None:
                raise FileNotFoundError(f'FileNotFound: {gp}')
            r = cv2.imread(str(rp), cv2.IMREAD_UNCHANGED)
            # r = np.zeros([100, 100])
            if r is None:
                raise FileNotFoundError(f'FileNotFound: {rp}')
            dif = sub(g=g, r=r)
            res.append(dif)
            filenames.append(gp)
            if len(res) == self.batch_size:
                ret = np.array(res)
                res.clear()
                yield ret, filenames
                filenames.clear()
        # 遍历完若有剩余，说明不够batchsize，剩余的这里再一并返回
        if len(res) != 0:
            yield np.array(res), filenames

    # 无减法操作
    def get_data_loader2(self) -> GeneratorType:
        res = []
        filenames = []
        for p in self.all_files:
            img = cv2.imread(str(p), cv2.IMREAD_UNCHANGED)
            if img is None:
                raise FileNotFoundError(f'FileNotFound: {p}')
            res.append(img)
            filenames.append(p)
            if len(res) == self.batch_size:
                ret = np.array(res)
                res.clear()
                yield ret, filenames
                filenames.clear()
        # 遍历完若有剩余，说明不够batchsize，剩余的这里再一并返回
        if len(res) != 0:
            yield np.array(res), filenames

    @_async
    def __get_batch_fn(self):
        if not hasattr(self, 'data_loader'):
            self.data_loader = self.get_data_loader()
        try:
            batch = next(self.data_loader)
        except:
            batch = None
        self.batch_data = batch
        self.had_gen_batch = True

    def get_batch(self):
        while True:
            if self.had_gen_batch:
                ret = copy.deepcopy(self.batch_data)
                self.had_gen_batch = False
                self.__get_batch_fn()
                return ret
            time.sleep(0.02)

    def __len__(self):
        a, b = divmod(len(self.all_files), self.batch_size)
        return a if b == 0 else a + 1


class Merge_and_save_img:
    def __init__(self, saved_dir, imageisbig, bism=None):
        self.had_merge_and_save = True
        self.saved_dir = saved_dir
        self.bism = bism
        self.imageisbig = imageisbig

    @_async
    def __merge_and_save_img(self, res, fn):
        if self.imageisbig:
            res = self.bism.merge(res)

        res = res[:, 0] * 255
        res = np.round(res).astype(np.uint8)
        for dst, f in zip(res, fn):
            saved_fn = Path(self.saved_dir, f'{f.stem}_dst.tif')
            cv2.imwrite(str(saved_fn), dst)
        self.had_merge_and_save = True

    def do(self, res, fn):
        while True:
            if not self.had_merge_and_save:  # 上次的数据还没保存完
                time.sleep(0.1)
                continue
            self.had_merge_and_save = False
            self.__merge_and_save_img(res, fn)
            break


def run_pytorch(cfg):
    print('~' * 50)
    Device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    print(f"Device: {Device}")
    print('~' * 50)

    files = load_files(cfg)
    batchsize = int(torch.cuda.device_count() * cfg['batch_size']) \
        if torch.cuda.device_count() > 0 else cfg['batch_size']
    data = Data(files, batchsize, cfg['sub'])
    data_len = len(data)
    pbar = Pbar(total=data_len)
    saved_dir = cfg['path_dst']
    Path(saved_dir).mkdir(exist_ok=True)

    # download weights
    weights_path = Path(__file__).parent / 'weights.pkl'
    if not weights_path.exists():
        download_weights(weights_path)

    model = Unet_sr()
    model.init_weights(weights_path)
    model.to(Device)

    # 加入过卡支持
    if torch.cuda.device_count() > 1:
        print("Let's use", torch.cuda.device_count(), "GPUs!")
        model = nn.DataParallel(model)

    model.eval()

    dep = cfg['image_depth']
    if dep == 8:
        imgmaxvalue = 255.
    else:
        imgmaxvalue = cfg['norm_maxv']

    bism = Batch_imgs_split_merge()
    masi = Merge_and_save_img(saved_dir=saved_dir, imageisbig=cfg['imageisbig'], bism=bism)

    while True:
        ret = data.get_batch()
        if ret is None: break
        batch_imgs, fn = ret
        imgs = batch_imgs[:, None]
        imgs = imgs.astype(np.float32) / imgmaxvalue
        imgs = np.clip(imgs, 0, 1)

        if cfg['imageisbig']:
            splitimgs = bism.split(imgs)
            splitres = []
            for rowimgs in splitimgs:
                rowres = []
                for img in rowimgs:
                    x = torch.from_numpy(img).to(Device)
                    y = model(x)
                    y = y.cpu().detach().numpy()
                    rowres.append(y)
                splitres.append(rowres)
            masi.do(splitres, fn)
        else:
            imgs = torch.from_numpy(imgs).to(Device)
            res = model(imgs).cpu().detach().numpy()
            masi.do(res, fn)

        pbar.update()
    pbar.close()


class Batch_imgs_split_merge():
    def __init__(self, size=256, overlap=10, dtype=np.float32):
        self.s = size
        self.o = overlap

        self.wa = np.linspace(1, 0, 2 * overlap).reshape(1, -1).astype(dtype)
        self.wb = 1 - self.wa

    def split(self, imgs):
        s, o = self.s, self.o
        h, w = imgs.shape[2:]
        hps = [i * s for i in range(h // s - 1)]
        wps = [i * s for i in range(w // s - 1)]

        def get_start_and_end(i, ps, l):
            '''
            考虑完overlap、边界等信息后的图像起始点
            '''
            if i == 0:
                start = ps[i]
                end = ps[i] + s + o
            elif i == len(ps) - 1:
                start = ps[i] - o
                end = l
            else:
                start = ps[i] - o
                end = ps[i] + s + o
            return start, end

        simgs = []
        for i in range(len(hps)):
            h_start, h_end = get_start_and_end(i, hps, h)
            wimgs = []
            for j in range(len(wps)):
                w_start, w_end = get_start_and_end(j, wps, w)
                wimgs.append(imgs[:, :, h_start:h_end, w_start:w_end])
            simgs.append(wimgs)

        return simgs

    def merge(self, simgs):
        s, o = self.s, self.o

        def merge_a_row_or_col(imgs, axis):
            def merge_two_imgs(a, b):
                a0 = a[:, :, :, :-2 * o] if axis == 'w' else a[:, :, :-2 * o]
                b0 = b[:, :, :, 2 * o:] if axis == 'w' else b[:, :, 2 * o:]
                ap = a[:, :, :, -2 * o:] if axis == 'w' else a[:, :, -2 * o:]
                bp = b[:, :, :, :2 * o] if axis == 'w' else b[:, :, :2 * o]
                wa = self.wa[None, None] if axis == 'w' else self.wa[None, :, :, None]
                wb = self.wb[None, None] if axis == 'w' else self.wb[None, :, :, None]
                ab = ap * wa + bp * wb
                dst = np.concatenate([a0, ab, b0], axis=-1) if axis == 'w' else np.concatenate([a0, ab, b0], axis=-2)
                return dst

            res = imgs[0]
            for img in imgs[1:]:
                res = merge_two_imgs(res, img)
            return res

        dsts = []
        for imgs in simgs:
            dsts.append(merge_a_row_or_col(imgs, 'w'))
        dst = merge_a_row_or_col(dsts, 'h')
        return dst


# todo
'''
更新相减的方式，可以设置谁减谁
'''

if __name__ == '__main__':
    '''
    1,原代码用时：time_used:8.507475833098093 mins
    2,DataParallel方式耗时：5.185853377978007 mins
    3,DistributedDataParallel方式耗时：5.09063835144043 mins
    4,再加上异步：
    '''

    t1 = time.time()
    run_pytorch()
    t2 = time.time()
    print(f'time_used:{(t2 - t1) / 60} mins')
    exit()
