from setuptools import find_packages
from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='ntcpy',
    version='1.0.0',
    description='A Python port of ntcjs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vrumger/ntcpy',
    author='Avrumy',
    author_email='contact@lungers.com',
    license='MIT',
    packages=find_packages(),
)
