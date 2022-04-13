from setuptools import setup, find_packages

setup(
    name='My_Package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Daniel-Motsoeneng/My_Package',
    author='Daniel Motsoeneng',
    author_email='dgmotsoeneng@gmail.com' 
)