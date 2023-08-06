import setuptools

import versioneer

setuptools.setup(
    name="preheat_open",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Neogrid and contributors",
    author_email="analytics@neogrid.dk",
    description="Python wrapper for Neogrid Technologies' REST API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/neogrid-technologies-public/preheat-open-python",
    packages=["preheat_open"],
    install_requires=["dateutils", "requests", "pandas", "numpy", "networkx"],
    extras_require={
        "dev": [
            "setuptools>=42",
            "wheel",
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "Sphinx",
            "m2r2",
            "sphinx-autodoc-typehints",
            "sphinx-rtd-theme",
        ],
    },
)
