# -*- coding:utf-8 -*-
from setuptools import setup

# 第三方依赖
requires = [
    'py_ios_device'
]
setup(
    name="iOS_tools",
    version="1.0.2",
    author="crystal",
    author_email="zhuhuiping@shizhuang-inc.com",
    description="iOS tools",
    packages=["iOS_tools"],
    python_requires=">=3.7",
    install_requires=requires,  # 第三方库依赖
    long_description_content_type="text/x-rst",
    entry_points={
        'console_scripts':{
            'iosdevice=iOS_tools.main:cli'
        }
    },
)