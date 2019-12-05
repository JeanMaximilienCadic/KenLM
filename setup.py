from setuptools import setup
import setuptools
import os
from gnutools.utils import parent, listfiles
import numpy as np
from setuptools import Extension
def get_packages(root):
    """
    Get the list of packages availables in a root

    :param root: package root
    :return list:
    """
    root = os.path.realpath(root)
    proot = parent(root) + "/"
    py_files = [file.rsplit(proot)[1] for file in listfiles(root)]
    packages = list(np.unique([parent(file).replace("/", ".") for file in py_files]))
    # return list(np.unique([parent(file).replace("/", ".").split(".{name_root}.".format(name_root=name(root)))[1]
    #                        for file in py_files]))
    return packages

print(get_packages('/mnt/IYOProjects/IYO/kenlm-publish/kenlm'))

setup(
    name="kenlm",
    version="1.0",
    long_description="",
    include_package_data=True,
    url='https://9dw-lab.jp',
    license='9DWLab',
    author='jcadic',
    # python_requires='>=3.6' and '<3.7',
    packages=["kenlm", "kenlm.bin"],
    # setup_requires=setup_requires,
    #install_requires=install_requires,
    # extra_requires=setup_requires,
    # ext_modules=[Extension('kenlm.bin', ['kenlm/bin/lmplz'])],
    author_email='j.cadic@9dw-lab.jp',
    description='KenLM',
    # platforms="linux_debian_10_x86_64",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ]
)
