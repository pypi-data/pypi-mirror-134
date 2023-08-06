from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="excelop",
    version="0.1.1",
    author="vcbe",  # 作者名字
    author_email="945193029@qq.com",
    description="simple Excel Operation",
    license="MIT",
    url="https://github.com/VCBE123/excelop.git",  # github地址或其他地址
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'openpyxl>=3.0.7'  # 所需要包的版本号
    ],
    zip_safe=True,
)
