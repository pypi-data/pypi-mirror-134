from setuptools import setup, find_packages

__version__ = '0.0.1'

install_requires = [
    'numpy',
    'pandas',
    'tqdm'
]

setup(
    name='brewmaster',
    packages=find_packages(),
    version=__version__,
    description='A package trying to accelerate the pandas'
    'apply in a parallel manner.',
    author='Zhengkai Yang',
    install_requires=install_requires,
)
