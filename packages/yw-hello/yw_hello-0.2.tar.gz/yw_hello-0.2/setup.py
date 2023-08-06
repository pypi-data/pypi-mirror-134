from setuptools import setup, find_packages


setup(
    name='yw_hello',
    version='0.2',
    license='MIT',
    author="Suchin Ravi",
    author_email='suchin.ravi@wonksknow.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/wonksknowsuchin/yw_hello',
    keywords='Youngwonks Hello',
    install_requires=[],
)