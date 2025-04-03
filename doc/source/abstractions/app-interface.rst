App interface
=============

Many Ansys apps are designed around user interaction within a
desktop GUI-based environment. Consequently, scripts are recorded
directly from user sessions and are in the context of manipulating the
desktop app. Instead, scripts should be written for an API 
that is structured around data represented as classes and methods.

PyAnsys seeks to make the API a "first class citizen" in regard to
interacting with an Ansys product by presenting the product as a
stateful data model. Consider the following comparison between using a
recorded script from AEDT versus using the PyAEDT library to create an
open region in the active editor:

+------------------------------------------------------+----------------------------------------------+
| Using a Recorded Script from AEDT (MS COM Methods)   | Using the `PyAEDT`_ Library                  |
+======================================================+==============================================+
| .. code:: python                                     | .. code:: python                             |
|                                                      |                                              |
|    import sys                                        |    from pyaedt import Hfss                   |
|    import pythoncom                                  |                                              |
|    import win32com.client                            |    hfss = Hfss()                             |
|                                                      |    hfss.create_open_region(frequency="1GHz") |
|    # initialize the desktop using pythoncom          |                                              |
|    Module = sys.modules['__main__']                  |                                              |
|    oDesktop = Module.oDesktop                        |                                              |
|    oProject = oDesktop.SetActiveProject("Project1")  |                                              |
|    oDesign = oProject.SetActiveDesign("HFSSDesign1") |                                              |
|    oEditor = oDesign.SetActiveEditor("3D Modeler")   |                                              |
|    oModule = oDesign.GetModule("BoundarySetup")      |                                              |
|                                                      |                                              |
|    # create an open region                           |                                              |
|    parm = [                                          |                                              |
|        "NAME:Settings",                              |                                              |
|        "OpFreq:=", "1GHz",                           |                                              |
|        "Boundary:=", "Radition",                     |                                              |
|        "ApplyInfiniteGP:=", False                    |                                              |
|    ]                                                 |                                              |
|    oModule.CreateOpenRegion(parm)                    |                                              |
+------------------------------------------------------+----------------------------------------------+

Besides length and readability, the biggest difference between the two
approaches is how the methods and attributes from the ``Hfss`` class
are encapsulated. For example, AEDT no longer needs to be
explicitly instantiated and is hidden as a protected attribute
``_desktop``. The connection to the app takes place
automatically when ``Hfss`` is instantiated, and the active AEDT 
project, editor, and module are automatically used to create the 
open region.

Furthermore, the ``create_open_region`` method within the ``Hfss`` 
class contains a full Python documentation string with keyword arguments,
clear ``numpydoc`` parameters and returns, and a basic example.
These are unavailable when directly using COM methods, preventing
the use of contextual help from within a Python IDE.

The source of the ``hfss.py`` method within `PyAEDT`_ follows. 
Note how calls to the COM object are all encapsulated 
within this method.

.. code:: python

    def create_open_region(
        self, frequency="1GHz", boundary="Radiation", apply_infinite_gp=False, gp_axis="-z"
    ):
        """Create an open region in the active editor.

        Parameters
        ----------
        frequency : str, optional
            Frequency with units. The  default is ``"1GHz"``.
        boundary : str, optional
            Type of the boundary. The default is ``"Radiation"``.
        apply_infinite_gp : bool, optional
            Whether to apply an infinite ground plane. The default is ``False``.
        gp_axis : str, optional
            The default is ``"-z"``.

        Returns
        -------
        bool
            ``True`` when successful, ``False`` when failed.

        Examples
        --------
        Create an open region in the active editor at 1 GHz.

        >>> hfss.create_open_region(frequency="1GHz")

        """
        vars = [
            "NAME:Settings",
            "OpFreq:=",
            frequency,
            "Boundary:=",
            boundary,
            "ApplyInfiniteGP:=",
            apply_infinite_gp,
        ]
        if apply_infinite_gp:
            vars.append("Direction:=")
            vars.append(gp_axis)

        self._omodelsetup.CreateOpenRegion(vars)
        return True

Here, the COM ``CreateOpenRegion`` method is abstracted, encapsulating
the model setup object. There's no reason why a user needs direct
access to ``_omodelsetup``, which is why it's protected in the
``Hfss`` class. Additionally, calling the method is simplified by
providing (and documenting) the defaults using keyword arguments and
placing them into the ``vars`` list, all while following the `Style
Guide for Python Code (PEP8)`_.
