
Style
=====

In the PyAnsys ecosystem, three key styles contribute to an 
enhanced developer experience:

- **Packaging style**: Focuses on creating clear, GitHub-hosted open source APIs, allowing
  for reusable packages that can be updated independently of the Ansys release schedule.
- **Coding style**: Ensures that code adheres to `PEP 8`_ and aligns with the conventions of
  major data science packages like `NumPy`_, `SciPy`_, and `pandas`_ for consistency and readability.
- **Documentation style**: Emphasizes the significance of cohesive and user-friendly
  content and well-documented APIs to improve the on-boarding experience and increase library adoption.
  All PyAnsys libraries follow the `Google developer documentation style guide
  <https://developers.google.com/style/>`_, which includes using sentence-case titles, active voice,
  present tense, and clear, concise sentences.

.. grid:: 3

    .. grid-item-card:: :octicon:`file-directory` Packaging style
        :link: packaging/index
        :link-type: doc

        Best practices for distributing Python code.

    .. grid-item-card:: :octicon:`codespaces` Coding style
        :link: coding-style/index
        :link-type: doc

        Best practices for writing Python code.

    .. grid-item-card:: :octicon:`pencil` Documentation style
        :link: doc-style/index
        :link-type: doc

        Best practices for writing PyAnsys library documentation.

.. toctree::
   :hidden:
   :maxdepth: 2

   packaging/index
   coding-style/index
   doc-style/index