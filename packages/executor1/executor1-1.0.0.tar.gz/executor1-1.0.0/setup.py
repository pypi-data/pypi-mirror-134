# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(path, 'README.MD'), encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    long_description = "The configuration file is automatically executed"
package = find_packages(exclude=['Download-bank-statement'], include=['main'])

setup(
    name="executor1",
    version="1.0.0",
    keywords=("uiautomation", "autoit", "python"),
    description="The configuration file is automatically executed",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.6.0",
    author="rejii",
    license='MIT',
    include_package_data=True,
    author_email="ljy@bczx365.com",
    packages=package,
    install_requires=['pyautoit', 'uiautomation'],
    url="http://gitlab.bczx365.com/rpa/UIA_Executor",
)
print(package)

