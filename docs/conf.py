# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TIMES - The Integrated MARKAL-EFOM System'
copyright = '2023, IEA-ETSAP'
author = 'IEA-ETSAP'
release = '4.7.2'

rst_prolog = """.. note::
    This documentation was migrated to **Read the Docs** from the original PDF version to improve accessibility, searchability, and version control.
    The migration was performed by `Olexandr Balyk <https://github.com/olejandro>`_ and `ESMIA Consultants <https://esmia.ca/en>`_.
    The original version of the Documentation can be found in an `ETSAP repository on GitHub <https://github.com/etsap-TIMES/TIMES_Documentation>`_.
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
numfig = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# -- Options for MyST-Parser -------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html

myst_enable_extensions = ["dollarmath", "colon_fence"]
