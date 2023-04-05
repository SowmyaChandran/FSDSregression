from setuptools import find_packages,setup
from typing import List

remove_last_line='-e .'


def get_requirements(filename):
    req=[]
    with open(filename) as f:
        req=f.readlines()
        req= [i.replace("\n","") for i in req]
        if remove_last_line in req:
            req.remove(remove_last_line)
    return req




setup(
    name='RegessorProject',
    version='0.0.1',
    author='sowmya',
    install_requires=get_requirements('requirements.txt'),
    package=find_packages()
)