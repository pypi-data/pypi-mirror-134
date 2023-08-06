from setuptools import find_packages, setup

with open("requirements.txt",'r+') as f:
    lines = f.readlines()

requirements = [str(x).strip() for x in lines]

setup(
    version='0.0.2',
    name='rltrade_pypbo',
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=requirements,
    keywords="Reinforcement Learning",
    url="https://github.com/esvhd/pypbo",
    description="probability for overfitting",
    long_description="probability for overfitting",
)
