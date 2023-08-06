from setuptools import setup, find_packages


setup(
    name='yw_hello',
    version='0.6',
    license='MIT',
    author="Suchin Ravi",
    author_email='suchin.ravi@wonksknow.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://www.youngwonks.com/',
    keywords='Youngwonks Hello',
    install_requires=[],
)
