import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

base_dir = os.path.dirname(os.path.abspath(__file__))


def get_version(filename="seafoam/__init__.py"):
    with open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)


setup(
    name="seafoam",
    version=get_version(),
    description="Pelican theme, first used for Minchin.ca.",
    long_description="\n\n".join([open(os.path.join(base_dir, "README.rst")).read()]),
    long_description_content_type="text/x-rst",
    author="W. Minchin",
    author_email="w_minchin@hotmail.com",
    url="https://github.com/MinchinWeb/seafoam",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pelican",
        "minchin.pelican.plugins.image_process>=1.0.1, !=1.1.2",
        "pelican-jinja-filters>2.0.0",
        # requires asset plugin, bundle? -- https://github.com/getpelican/pelican-plugins/tree/master/assets
    ],
    extras_require={
        ":python_version < '3.4'": ["pathlib2"],
        "dev": [
            "minchin.releaser",
            "markdown",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Pelican",
        "Framework :: Pelican :: Themes",
    ],
    zip_safe=False,  # use wheels instead
)
