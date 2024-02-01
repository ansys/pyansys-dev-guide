
Style
=====

In the PyAnsys ecosystem, three key styles—packaging, coding, and documentation—
serve as foundational pillars to enhance the overall developer experience.

- Packaging style focuses on creating clear, open source APIs hosted on GitHub,allowing
  for reusable packages that can be updated independently of the Ansys release schedule.

- Coding style adheres to PEP 8 and aligns with the conventions of major data science libraries
  like NumPy, SciPy, and pandas, ensuring consistency and readability.

- Documentation style emphasizes the significance of well-documented APIs, 
  offering increased adoption, an improved on-boarding experiences, and streamlined code maintenance.

All PyAnsys libraries follow the Google developer documentation style guide, 
incorporating sentence case, active voice, and concise, clear sentences for 
cohesive and user-friendly documentation.


.. grid:: 3

    .. grid-item-card:: :octicon:`file-directory` Packaging
        :link: packaging/index
        :link-type: doc

        Best practices for distributing Python code.

    .. grid-item-card:: :octicon:`codespaces` Coding
        :link: coding-style/index
        :link-type: doc

        Best practices for writing Python code.

    .. grid-item-card:: :octicon:`pencil` Documentation
        :link: doc-style/index
        :link-type: doc

        Best practices for writing PyAnsys library documentation.

.. toctree::
   :hidden:
   :maxdepth: 2

   packaging/index
   coding-style/index
   doc-style/index