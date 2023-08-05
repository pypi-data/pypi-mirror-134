#! python
# @Time    : 22/01/10 上午 10:42
# @Author  : azzhu 
# @FileName: setup.py.py
# @Software: PyCharm
import setuptools
import deeps

''' 
国内源找不到该包(或者说更新不及时)，一定要使用官方源安装：
pip install -i https://pypi.org/simple/ deeps-cibr
pip install --upgrade -i https://pypi.org/simple/ deeps-cibr
🀙🀚🀛🀜🀝🀞🀟🀠🀡🀢🀣
'''

with open('requirements.txt') as f:
    req = [line.strip() for line in f.readlines() if line.strip()]

# with open("README.md", "r", encoding='utf-8') as fh:
#     long_description = fh.read()

setuptools.setup(
    name="deeps-cibr",
    version=deeps.__version__,
    author="azzhu",
    author_email="zhu.qingjie@qq.com",
    description="A deeps inference module.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/azzhu/deeps",
    install_requires=req,
    license='MIT',
    packages=setuptools.find_packages(),
    # package_data={
    #     'easyFlyTracker': ['fonts/*.ttf'],
    # },
    # project_urls={
    #     "Source Code": "https://github.com/azzhu/EasyFlyTracker",
    #     "Bug Tracker": "https://github.com/azzhu/EasyFlyTracker/issues",
    #     # "Documentation": "",  # 待补充修改
    # },
    entry_points={
        'console_scripts': [
            'deeps=deeps.cli:deeps_',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
