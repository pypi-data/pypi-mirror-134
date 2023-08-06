from setuptools import setup, find_packages


setup(
    name='various_utilities',
    version='0.1',
    license='MIT',
    author="Cristian Desivo",
    author_email='cdesivo92@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/crisdesivo/various_utilities',
    keywords='utilities',
    install_requires=[
      ],
)
