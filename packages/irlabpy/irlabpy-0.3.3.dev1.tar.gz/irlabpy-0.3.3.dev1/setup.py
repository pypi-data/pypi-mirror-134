# !/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup
import os


def _process_requirements():
    packages = open('requirements.txt').read().strip().split('\n')
    requires = []
    for pkg in packages:
        if pkg.startswith('git+ssh'):
            return_code = os.system('pip install {}'.format(pkg))
            assert return_code == 0, 'error, status_code is: {}, exit!'.format(return_code)
        else:
            requires.append(pkg)
    return requires


setup(
    name='irlabpy',
    version='0.3.3.dev1',
    author='chenghao',
    author_email='xuguiqiang.xuguiqi@antgroup.com',
    url='https://code.alipay.com/neo/irlab.git',
    packages=['irlabpy', 'irlabpy.dev', 'irlabpy.ops', 'irlabpy.data_model', 'irlabpy.decorators', 'irlabpy.feature_engineering','irlabpy.pontus', 'irlabpy.irlabLogger', 'irlabpy.cache'],
    long_description='this is irlabpy python sdk',
    include_package_data=True,
    package_data={'': ['*.ini'], },
    install_requires=_process_requirements()
)
