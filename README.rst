



PyAnsys Package Basic Structure
-------------------------------

ansys/<product>/<service>/my_module.py
ansys/<product>/<service>/my_other_module.py
ansys/<product>/<service>/__init__.py
README.rst
LICENSE (use Ansys license file in this repo)
setup.py
requirements.txt
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
.github/workflows/ci.yml

This contains a `README.rst` containing
 - How to install...


Unit Testing
 - <you know the drill>
 - Will probably require your application/server to be packaged in a
   way that lets you consume it from public infrastructure.

Workflows
 - Test CI online
 - Deploy package automagically

Setup File
 - Defines what the "package is"

 <Setup File>


Python Modules
 - Non-proprietary source.
 - Exposes server functionality pythonically.


Documentation Directory `doc`
 - Use `pyansys-sphinx-theme <https://sphinxdocs.pyansys.com/>`_
