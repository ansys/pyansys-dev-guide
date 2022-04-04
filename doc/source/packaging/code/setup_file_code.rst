.. code:: python

    """Installation file for ansys-mapdl-core."""
    
    from setuptools import find_namespace_packages, setup
    
    setup(
        name="ansys-<product>-<library>",
        packages=find_namespace_packages(where="src", include="ansys*"),
        package_dir={"": "src"},
        version="<version>",
        description="<Short description of the package>",
        long_description=open("README.rst").read(),
        license="MIT",
        author="ANSYS, Inc.",
        author_email="pyansys.support@ansys.com",
        maintainer="PyAnsys developers",
        maintainer_email="pyansys.maintainers@ansys.com",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        url="<https://github.com/pyansys/py<product>-<library>",
        python_requires=">=3.<minor>",
        install_requires=["importlib-metadata >=4.0"],
    )
