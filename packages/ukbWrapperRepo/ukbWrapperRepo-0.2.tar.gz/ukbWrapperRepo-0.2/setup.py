import setuptools
setuptools.setup(name='ukbWrapperRepo',
version='0.2',
description='UKB Dataset Access Wrapper',
url='https://github.com/tighu20/ukbWrapperRepo',
author='Tigmanshu Chaudhary',
install_requires=['pandas','numpy','pandas_plink','datalad'],
author_email='tic48@pitt.edu',
packages=setuptools.find_packages(),
zip_safe=False)
