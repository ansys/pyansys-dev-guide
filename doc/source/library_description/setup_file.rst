Setup File
##########
The setup file for a PyAnsys library package, ``setup.py``, should contain 
these elements:

- Name (such as ``ansys-mapdl-core``)
- Packages (such as ``ansys.mapdl.core``)
- Short description
- Long description in a ``README.md`` or ``README.rst`` file
- `Single-sourced package version <https://packaging.python.org/guides/single-sourcing-package-version/>`_
- Author of ``"ANSYS, Inc."``
- Maintainer's name and email
- Dependency requirements
- Applicable classifiers

The ``ansys-<product/service>-<feature>`` would have at the minimum
the following within its ``setup.py``.

.. code:: python

   """Setup file for ansys-<product/service>-<feature>"""
   import codecs
   import os
   from io import open as io_open
   from setuptools import setup

   THIS_PATH = os.path.abspath(os.path.dirname(__file__))
   __version__ = None
   version_file = os.path.join(THIS_PATH, 'ansys', '<product/service>',
                               '<feature>', '_version.py')
   with io_open(version_file, mode='r') as fd:
       exec(fd.read())

   setup(
       name='ansys-<product/service>-<feature>',
       packages=['ansys.<product/service>.<feature>'],
       version=__version__,
       description='Short description',
       long_description=open('README.rst').read(),
       long_description_content_type='text/x-rst',
       url='https://github.com/pyansys/pyansys-package-example/',
       license='MIT',
       author='ANSYS, Inc.',
       maintainer='First Last',
       maintainer_email='first.last@ansys.com',
       install_requires=['grpcio>=1.30.0'],
       python_requires='>=3.5',
       classifiers=[
           'Development Status :: 4 - Beta',
           'Programming Language :: Python :: 3',
           'License :: OSI Approved :: MIT License',
           'Operating System :: OS Independent',
       ],
   )
