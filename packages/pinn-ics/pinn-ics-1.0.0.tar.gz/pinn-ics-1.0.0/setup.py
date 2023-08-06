from setuptools import find_packages, setup


NAME = 'pinn-ics'
VERSION = '1.0.0'
DESCRIPTION = 'Solving physics problems by using Deep Learning'
LONG_DESCRIPTION = ''
AUTHOR = 'threezinedine'


classifiers = [
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3 :: Only"
]


setup(
    name='pinn-ics',
    version='1.0.0',
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author_emal='threezinedine@gmail.com',
    packages=find_packages(),
    requires=['tensorflow', 'numpy'],
    keywords=['python', 'scientist', "equation solver"],
    classifiers=classifiers
)
