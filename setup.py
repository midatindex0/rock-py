from setuptools import setup

VERSION = "1.0.0"

setup(
    name="rock",
    version=VERSION,
    author="midnigth",
    packages=["rock"],
    install_requires=["aiohttp", "requests"],
)
