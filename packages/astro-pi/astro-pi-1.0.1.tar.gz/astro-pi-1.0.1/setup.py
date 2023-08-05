import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="astro-pi",
    version="1.0.1",
    author="Dave Honess",
    author_email="dave@raspberrypi.org",
    description="Python API for Astro Pi (Sense HAT) for the Raspberry Pi",
    license="BSD",
    keywords=[
        "raspberrypi",
        "astro pi",
        "astro pi hat",
        "sense hat",
    ],
    url="https://github.com/astro-pi/astro-pi-hat",
    packages=find_packages(),
    package_data={
        "txt": ['astro_pi_text.txt'],
        "png": ['astro_pi_text.png']
    },
    include_package_data=True,
    install_requires=[
        "pillow",
        "numpy"
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: BSD License",
    ],
)
