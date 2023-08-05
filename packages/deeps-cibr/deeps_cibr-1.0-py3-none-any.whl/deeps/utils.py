#! python
# @Time    : 21/12/29 上午 09:32
# @Author  : azzhu 
# @FileName: utils.py
# @Software: PyCharm
import time
from multiprocessing import Process

import requests


class Pbar():
    '''
    自己实现一个进度条，使用方法类似tqdm。
    特点：
    不会出现一直换行问题，只保留一行更新。
    格式：
    【完成百分比 进度条 当前任务/总共任务 [总耗时<剩余时间，速度]】
    '''

    def __init__(self, total, pbar_len=50, pbar_value='|', pbar_blank='-'):
        self.total = total
        self.pbar_len = pbar_len
        self.pbar_value = pbar_value
        self.pbar_blank = pbar_blank
        self.now = 0
        self.time = time.time()
        self.start_time = time.time()
        self.close_flag = False

    def update(self, nb=1, set=False, set_value=None):
        if set:
            self.now = set_value
        else:
            self.now += nb
        percent = int(round(self.now / self.total * 100))  # 百分比数值
        pbar_now = round(self.pbar_len * percent / 100)  # 进度条当前长度
        if pbar_now > self.pbar_len: pbar_now = self.pbar_len  # 允许now>total，但是不允许pbar_now>pbar_len
        blank_len = self.pbar_len - pbar_now
        time_used = time.time() - self.time  # 当前更新耗时
        eps = 1e-4  # 一个比较小的值，加在被除数上，防止除零
        speed = nb / (time_used + eps)  # 速度
        total_time_used = time.time() - self.start_time  # 总耗时
        total_time_used_min, total_time_used_sec = divmod(total_time_used, 60)
        total_time_used = f'{int(total_time_used_min):0>2d}:{int(total_time_used_sec):0>2d}'
        remaining_it = self.total - self.now if self.total - self.now >= 0 else 0  # 剩余任务
        remaining_time = remaining_it / speed  # 剩余时间
        remaining_time_min, remaining_time_sec = divmod(remaining_time, 60)
        remaining_time = f'{int(remaining_time_min):0>2d}:{int(remaining_time_sec):0>2d}'
        pbar = f'{percent:>3d}%|{self.pbar_value * pbar_now}{self.pbar_blank * blank_len}| ' \
               f'{self.now}/{self.total} [{total_time_used}<{remaining_time}, {speed:.2f}it/s]'
        print(f'\r{pbar}', end='')
        self.time = time.time()

    def close(self, reset_done=True):
        if self.close_flag: return  # 防止多次执行close时会打印多行
        if reset_done:  # 把状态条重置为完成
            self.update(set=True, set_value=self.total)
        print()  # 把光标移到下一行
        self.close_flag = True


class Wait():
    '''
    等待模块。
    跟Pbar类似，Pbar需要更新，需要知道当前进度，这个不需要，只展示了一个等待的动画。
    需要处理的代码块放到with里面即可，注意，该代码块里面最好就不要再有任何print了。

    usage:
    with Wait():
        time.sleep(10)
    '''

    def __init__(self, info=None):
        if info:
            print(f'{info}.../', end='', flush=True)
        else:
            print('.../', end='', flush=True)

    def __enter__(self):
        self.p = Process(target=self.print_fn, args=())
        self.p.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.p.terminate()
        print('\bDone')

    def print_fn(self):
        while True:
            time.sleep(0.3)
            print('\b\\', end='', flush=True)
            time.sleep(0.3)
            print('\b/', end='', flush=True)


class WaitTime():
    '''
    优雅地计算with代码块内的执行耗时。
    '''

    def __init__(self):
        self._time_used = None
        self._time_used_list = []

    def __enter__(self):
        self._start_time_point = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._time_used = time.time() - self._start_time_point
        self._time_used_list.append(self._time_used)

    def clear(self):
        self._time_used_list = []

    @property
    def time_used(self):
        return self._time_used

    @property
    def time_used_list(self):
        return self._time_used_list


def get_time() -> str:
    tm = time.localtime(time.time())
    ret = f'{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday} {tm.tm_hour:0>2d}:{tm.tm_min:0>2d}:{tm.tm_sec:0>2d}'
    return ret


def print_tolog(s, end='\n', file='log.log'):
    with open(file, 'a') as f:
        f.write(f'{s}{end}')


def download_weights(filename):
    page_url = 'http://119.90.33.35:3557/sharing/xVgrvNL0T'
    data_url = 'http://119.90.33.35:3557/fsdownload/xVgrvNL0T/pyweights.pkl'
    page = requests.get(page_url)
    f = requests.get(data_url, cookies=page.cookies)
    with open(filename, 'wb') as file:
        file.write(f.content)


if __name__ == '__main__':
    download_weights(r'C:\Users\33041\Desktop\weights.pkl')
