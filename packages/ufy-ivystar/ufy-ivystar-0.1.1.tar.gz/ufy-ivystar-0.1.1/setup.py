# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2022/01/17 15:31:51
@Author  :   ufy
@Contact :   antarm@outlook.com
@Version :   v1.0
@Desc    :   None
'''

# here put the import lib
from setuptools import setup,find_packages

setup(
    name='ufy-ivystar',
    version='0.1.1',
    description='ivystar packages',
    author='ufy',
    author_email='antarm@outlook.com',
    url='',
    packages=find_packages('.'),
    install_requires =['ufy','numpy','matplotlib']
)