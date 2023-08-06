from setuptools import setup, find_packages


setup(
    name='my_cool_module',
    version='0.1',
    license='MIT',
    author="Nathan",
    author_email='boomshaka08mc@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Boomshaka08/my_cool_module',
    keywords='test',
    install_requires=[],
)
