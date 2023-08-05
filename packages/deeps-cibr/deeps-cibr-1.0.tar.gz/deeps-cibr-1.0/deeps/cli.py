#! python
# @Time    : 22/01/10 下午 03:48
# @Author  : azzhu 
# @FileName: cli.py
# @Software: PyCharm
import sys
from pathlib import Path
import yaml
from deeps.main import run_pytorch


def deeps_():
    args = sys.argv
    cfg_p = Path(args[1])
    with open(cfg_p, 'r', encoding='utf-8') as f:
        cfg = yaml.safe_load(f)
    run_pytorch(cfg)
    ...


if __name__ == '__main__':
    deeps_()
    ...
