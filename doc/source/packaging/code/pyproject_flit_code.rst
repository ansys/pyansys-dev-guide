.. code:: toml

    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"
    
    [project]
    # Check https://flit.readthedocs.io/en/latest/pyproject_toml.html for all available sections
    name = "Py<Product> <Library>"
    version = "<version>"
    description = "A Python wrapper for Ansys <Product> <Library>"
    readme = "README.rst"
    requires-python = ">=3.<minor>"
    license = {file = "LICENSE"}
    authors = [
        {name = "ANSYS, Inc.", email = "pyansys.support@ansys.com"},
    ]
    maintainers = [
        {name = "PyAnsys developers", email = "pyansys.maintainers@ansys.com"},
    ]
    
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    dependencies = [
        "importlib-metadata >=4.0",
    ]
    
    [tool.flit.module]
    name = "ansys.<product>.<library>"
    
    [project.urls]
    Source = "https://github.com/pyansys/py<product>-<library>"
