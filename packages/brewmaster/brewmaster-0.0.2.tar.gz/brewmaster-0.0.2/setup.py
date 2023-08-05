from setuptools import setup

__version__ = '0.0.2'

install_requires = [
    'numpy',
    'pandas',
    'tqdm'
]

setup(
    name='brewmaster',
    packages=['brewmaster'],
    version=__version__,
    description='A package trying to accelerate the pandas'
    'apply in a parallel manner.',
    author='Zhengkai Yang',
    install_requires=install_requires,
)
