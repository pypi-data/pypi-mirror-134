from setuptools import setup, find_packages


setup(
    name='yw_hello',
    version='0.1',
    license='MIT',
    author="Suchin Ravi",
    author_email='suchin.ravi@wonksknow.com',
    packages=find_packages('yw_hello'),
    package_dir={'': 'yw_hello'},
    url='https://github.com/wonksknowsuchin/yw_hello',
    keywords='Youngwonks Hello',
    install_requires=[],
)