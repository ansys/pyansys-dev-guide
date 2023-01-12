.. code:: toml

    [build-system]
    requires = ["poetry-core>=1.0.0"]
    build-backend = "poetry.core.masonry.api"
    
    [tool.poetry]
    # Check https://python-poetry.org/docs/pyproject/ for all available sections
    name = "Py<Product> <Library>"
    version = "<version>"
    description = "A Python wrapper for <Product> <Library>"
    license = "MIT"
    authors = ["ANSYS, Inc. <pyansys.support@ansys.com>"]
    maintainers = ["PyAnsys developers <pyansys.maintainers@ansys.com>"]
    readme = "README.rst"
    repository = "https://github.com/pyansys/py<product>-<library>"
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    packages = [
        { include = "ansys", from = "src" },
    ]
    
    [tool.poetry.dependencies]
    python = ">=3.<minor>"
    importlib-metadata = {version = "^4.0", python = "<3.8"}
