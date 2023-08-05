# coding=gbk
from distutils.core import setup

setup(
    name='nxqtest_module', # 对外我们模块的名字
    version='1.0', # 版本号
    description='这是第一个对外发布的模块，测试哦', #描述
    author='niexiaoqiang', # 作者
    author_email='niexiaoqiang03@sina.com',
    py_modules=['nxqtest_module.demo1','nxqtest_module.demo2'] # 要发布的模块
)