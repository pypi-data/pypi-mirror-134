#! python
# @Time    : 21/09/23 上午 10:35
# @Author  : azzhu 
# @FileName: model_torch.py
# @Software: PyCharm
import pickle

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn


class Conv(nn.Module):
    clsname = 'conv2d'

    def __init__(self, in_c, out_c, kers=3, padding=1, act=True, name=None):
        super().__init__()
        if kers == 2: padding = 0  # kers=2时特殊处理
        self.conv = nn.Conv2d(in_c, out_c, kers, padding=padding)
        # self.conv = nn.Conv2d(in_c, out_c, kers, padding=padding, padding_mode='reflect')
        self.act = act
        self.kers = kers
        self.name = name

    def forward(self, x):
        if self.kers == 2:
            x = F.pad(x, (0, 1, 0, 1), mode="constant", value=0)
            # x = F.pad(x, (1, 0, 1, 0), mode="constant", value=0)  # 改变padding位置对结果影响较大，变的有点模糊
            # x = F.pad(x, (0, 1, 0, 1), mode="reflect") # 改变padding模式对结果影响较小，肉眼没发现区别
        x = self.conv(x)
        if self.act:
            x = nn.LeakyReLU(negative_slope=0.2)(x)  # 改变斜度对结果影响比较大
        return x


class Residual_unit_bottleneck_old(nn.Module):
    '''
    使用nn.DataParallel来并行加速推理的时候会报错（很奇怪的错误，完全不知道从哪下手debug）。
    因为这里不能有__new__方法，不知道为啥，反正去掉就不报错了。
    但是去掉之后就不能初始化权重了，所以得想想办法。
    '''

    clsname = 'Residual_unit_bottleneck'
    clsnumb = -1

    def __new__(cls, ch, *args, **kwargs):
        cls.clsnumb += 1
        instance = super(Residual_unit_bottleneck, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, ch, *args, **kwargs):
        super().__init__()
        self.index = self.clsnumb * 3
        self.act = nn.LeakyReLU(negative_slope=0.2)
        self.conv1 = nn.Conv2d(ch, 64, kernel_size=1)
        self.bn1 = nn.BatchNorm2d(64, eps=1e-3)  # 改变eps对结果影响非常大，1e-5:变的有点类似二值图了;1e-2:非常模糊
        self.conv2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64, eps=1e-3)
        self.conv3 = nn.Conv2d(64, ch, kernel_size=1)
        self.bn3 = nn.BatchNorm2d(ch, eps=1e-3)

    def forward(self, input):
        x = self.conv1(input)
        x = self.bn1(x)
        x = self.act(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = self.act(x)

        x = self.conv3(x)
        x = self.bn3(x)

        x = x + input
        x = self.act(x)
        return x


class Residual_unit_bottleneck(nn.Module):
    '''
    为了兼容DataParallel和DistributedDataParallel，去掉了__new__方法。
    思想：clsnumb不在自动分配，而是手动设置，虽然比较笨但是没办法。
    '''

    clsname = 'Residual_unit_bottleneck'

    def __init__(self, ch, clsnumb, *args, **kwargs):
        super().__init__()
        self.index = clsnumb * 3
        self.act = nn.LeakyReLU(negative_slope=0.2)
        self.conv1 = nn.Conv2d(ch, 64, kernel_size=1)
        self.bn1 = nn.BatchNorm2d(64, eps=1e-3)  # 改变eps对结果影响非常大，1e-5:变的有点类似二值图了;1e-2:非常模糊
        self.conv2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64, eps=1e-3)
        self.conv3 = nn.Conv2d(64, ch, kernel_size=1)
        self.bn3 = nn.BatchNorm2d(ch, eps=1e-3)

    def forward(self, input):
        x = self.conv1(input)
        x = self.bn1(x)
        x = self.act(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = self.act(x)

        x = self.conv3(x)
        x = self.bn3(x)

        x = x + input
        x = self.act(x)
        return x


class Unet_sr(nn.Module):
    '''
    因为推理模式下dropout无效，所以这里没有加入dropout层
    '''

    def __init__(self):
        super().__init__()
        # 非参数层
        self.pool = nn.MaxPool2d(2, 2)
        self.up = nn.Upsample(scale_factor=2, mode='nearest')
        self.tail_act = nn.Sigmoid()

        self.c1 = Conv(1, 64, name='c1')
        self.c2 = Residual_unit_bottleneck(64, clsnumb=0)
        self.c3 = Conv(64, 128, name='c3')
        self.c4 = Residual_unit_bottleneck(128, clsnumb=1)
        self.c5 = Conv(128, 256, name='c5')
        self.c6 = Residual_unit_bottleneck(256, clsnumb=2)
        self.c7 = Conv(256, 512, name='c7')
        self.c8 = Residual_unit_bottleneck(512, clsnumb=3)
        self.c9 = Conv(512, 1024, name='c9')
        self.c10 = Residual_unit_bottleneck(1024, clsnumb=4)

        self.uc1 = Conv(1024, 512, kers=2, name='uc1')
        self.c11 = Conv(1024, 512, name='c11')
        self.c12 = Residual_unit_bottleneck(512, clsnumb=5)
        self.uc2 = Conv(512, 256, kers=2, name='uc2')
        self.c13 = Conv(512, 256, name='c13')
        self.c14 = Residual_unit_bottleneck(256, clsnumb=6)
        self.uc3 = Conv(256, 128, kers=2, name='uc3')
        self.c15 = Conv(256, 128, name='c15')
        self.c16 = Residual_unit_bottleneck(128, clsnumb=7)
        self.uc4 = Conv(128, 64, kers=2, name='uc4')
        self.c17 = Conv(128, 64, name='c17')
        self.c18 = Residual_unit_bottleneck(64, clsnumb=8)

        self.c19 = Conv(64, 2, name='c19')
        self.tail = Conv(2, 1, kers=1, padding=0, act=False, name='prd')

    def forward(self, x):
        c1 = self.c1(x)
        c2 = self.c2(c1)
        p1 = self.pool(c2)
        c3 = self.c3(p1)
        c4 = self.c4(c3)
        p2 = self.pool(c4)
        c5 = self.c5(p2)
        c6 = self.c6(c5)
        p3 = self.pool(c6)
        c7 = self.c7(p3)
        c8 = self.c8(c7)
        p4 = self.pool(c8)
        c9 = self.c9(p4)
        c10 = self.c10(c9)

        u1 = self.up(c10)
        u1 = self.pad(u1, c8)
        uc1 = self.uc1(u1)
        mg1 = torch.cat((c8, uc1), dim=1)
        c11 = self.c11(mg1)
        c12 = self.c12(c11)
        u2 = self.up(c12)
        u2 = self.pad(u2, c6)
        uc2 = self.uc2(u2)
        mg2 = torch.cat((c6, uc2), dim=1)
        c13 = self.c13(mg2)
        c14 = self.c14(c13)
        u3 = self.up(c14)
        u3 = self.pad(u3, c4)
        uc3 = self.uc3(u3)
        mg3 = torch.cat((c4, uc3), dim=1)
        c15 = self.c15(mg3)
        c16 = self.c16(c15)
        u4 = self.up(c16)
        u4 = self.pad(u4, c2)
        uc4 = self.uc4(u4)
        mg4 = torch.cat((c2, uc4), dim=1)
        c17 = self.c17(mg4)
        c18 = self.c18(c17)

        c19 = self.c19(c18)
        prd = self.tail(c19)
        prd = self.tail_act(prd)
        return prd

    def pad(self, u, c):
        if u.shape[-1] != c.shape[-1]:
            u = F.pad(u, (0, 1, 0, 0), "reflect")
        if u.shape[-2] != c.shape[-2]:
            u = F.pad(u, (0, 0, 0, 1), "reflect")
        return u

    def __get_weight(self, name: str, not_as_param: bool = False):
        value = self.weights.get(name, None)
        if value is None:
            raise KeyError(f"can't find '{name}' in weights file!")
        if not_as_param:
            return torch.from_numpy(value)
        else:
            return nn.Parameter(torch.from_numpy(value))

    def __init_weigets_conv(self, attrname: str):
        v = getattr(self, attrname)
        weight = self.__get_weight(f'generator/{v.name}/kernel')
        bias = self.__get_weight(f'generator/{v.name}/bias')

        if v.conv.weight.shape != weight.shape or \
                v.conv.bias.shape != bias.shape:
            raise ValueError(f"'{v.name}': shape is not accordant!")
        v.conv.weight = weight
        v.conv.bias = bias
        setattr(self, attrname, v)

    def __init_weigets_rub(self, attrname: str):
        v = getattr(self, attrname)
        inds = np.arange(0, 3)
        inds += v.index
        for i in [0, 1, 2]:
            ind = inds[i]

            # bn层
            bn = getattr(v, f'bn{i + 1}')
            name_flag = f'batch_normalization_{ind}' if ind != 0 else 'batch_normalization'
            running_mean = self.__get_weight(f'generator/{name_flag}/moving_mean', not_as_param=True)
            running_var = self.__get_weight(f'generator/{name_flag}/moving_variance', not_as_param=True)
            weight = self.__get_weight(f'generator/{name_flag}/gamma')
            bias = self.__get_weight(f'generator/{name_flag}/beta')
            if bn.running_mean.shape != running_mean.shape or \
                    bn.running_var.shape != running_var.shape or \
                    bn.weight.shape != weight.shape or \
                    bn.bias.shape != bias.shape:
                raise ValueError(f"'{name_flag}': shape is not accordant!")
            bn.running_mean = running_mean
            bn.running_var = running_var
            bn.weight = weight
            bn.bias = bias
            setattr(v, f'bn{i + 1}', bn)

            # conv层
            conv = getattr(v, f'conv{i + 1}')
            name_flag = f'conv2d_{ind}' if ind != 0 else 'conv2d'
            weight = self.__get_weight(f'generator/{name_flag}/kernel')
            bias = self.__get_weight(f'generator/{name_flag}/bias')
            if conv.weight.shape != weight.shape or \
                    conv.bias.shape != bias.shape:
                raise ValueError(f"'{name_flag}': shape is not accordant!")
            conv.weight = weight
            conv.bias = bias
            setattr(v, f'conv{i + 1}', conv)

        setattr(self, attrname, v)

    def init_weights(self, weights_path: str):
        with open(weights_path, 'rb') as f:
            self.weights = pickle.load(f)
        ...
        attrs = [_ for _ in dir(self) if not _.startswith('_')]
        attrs = [_ for _ in attrs if hasattr(getattr(self, _), 'clsname')]
        attrs_con = [_ for _ in attrs if getattr(getattr(self, _), 'clsname') == 'conv2d']
        attrs_rub = [_ for _ in attrs if getattr(getattr(self, _), 'clsname') == 'Residual_unit_bottleneck']
        for attr in attrs_con:
            self.__init_weigets_conv(attr)
        for attr in attrs_rub:
            self.__init_weigets_rub(attr)
        ...


def _test_():
    model = Unet_sr()
    model.init_weights('data/pyweights.pkl')
    model.eval()
    x = torch.ones(1, 1, 533, 358)
    y = model(x)
    print(y.shape)


def eval():
    import cv2
    img = cv2.imread(r'D:\tempp\TMP_IMGS\sr_x.bmp', 0)
    x = img[None, None]
    x = x.astype(np.float32) / 255

    model = Unet_sr()
    model.init_weights('data/pyweights.pkl')
    model.eval()

    x = torch.from_numpy(x)
    y = model(x)
    y = y.detach().numpy()
    y = y[0, 0] * 255
    y = np.round(y).astype(np.uint8)
    cv2.imshow('', y)
    cv2.waitKeyEx()
    cv2.imwrite('d:/tempp/srr_1.bmp', y)


class No_gard:
    def _no_gard(self):
        self.eval()
        params = self.parameters()
        for p in params: p.requires_grad = False


class VGG16_feature(nn.Module, No_gard):
    def __init__(self):
        super().__init__()
        import torchvision.models as models
        vgg16 = models.vgg16(pretrained=True)
        layers = list(vgg16.features.children())
        self.feature = torch.nn.Sequential(*layers[:16])
        self.imgmean = [103.939, 116.779, 123.68]
        self._no_gard()

    def forward(self, x):
        '''
        :param x: range:[0,1] shape:[N,1,H,W]
        :return:
        '''
        x = x[:, 0] * 255.
        b = x - self.imgmean[0]
        g = x - self.imgmean[1]
        r = x - self.imgmean[2]
        x = torch.stack([b, g, r], dim=1)
        return self.feature(x)


class Perceptual_Loss(nn.Module, No_gard):
    def __init__(self):
        super().__init__()
        self.feature = VGG16_feature()
        self._no_gard()

    def forward(self, x, y):
        f_x = self.feature(x)
        f_y = self.feature(y)
        diff = torch.abs(f_x - f_y)
        loss = torch.mean(diff)
        return loss


if __name__ == '__main__':
    Device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    model = Unet_sr()
    namedparams = list(model.named_parameters())
    weights = torch.load('model.pth', map_location=torch.device(Device))
    keys = weights.keys()
    model.load_state_dict(weights)
    exit()

    import os, cv2
    import torch.distributed as dist
    from torch.nn.parallel import DistributedDataParallel as DDP

    os.environ["CUDA_VISIBLE_DEVICES"] = '6,7'
    print('~' * 50)
    Device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    print(f"Device: {Device}")
    print(torch.__version__)
    print(torch.version.cuda)
    print(torch.backends.cudnn.version())
    print('~' * 50)

    model = Unet_sr()
    # model.init_weights(cfg.model.weights_path)
    model.to(Device)
    if torch.cuda.device_count() > 1:
        print("Let's use", torch.cuda.device_count(), "GPUs!")
        # model = nn.DataParallel(model)
        dist.init_process_group(backend='nccl')
        model = DDP(model)

    model.eval()
    x = cv2.imread(r'D:\tempp\156897765535812900.bmp', 0)
    cv2.imshow('src', x)
    x = x[None, None].astype(np.float32) / 255.
    x = torch.from_numpy(x)
    # x = torch.rand([1, 1, 128, 128], dtype=torch.float32).to(Device)
    y = model(x).detach().numpy()
    y = y[0, 0] * 255
    y = np.round(y).astype(np.uint8)
    cv2.imshow('dst', y)
    cv2.waitKeyEx()
