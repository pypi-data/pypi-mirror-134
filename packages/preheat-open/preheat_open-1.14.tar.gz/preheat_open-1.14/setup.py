import setuptools

import versioneer

setuptools.setup(
    name="preheat_open",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Neogrid et. al.",
    author_email="analytics@neogrid.dk",
    description="Open package consuming Neogrid REST API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
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
