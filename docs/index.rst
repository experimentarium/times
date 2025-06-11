.. TIMES - The Integrated MARKAL-EFOM System documentation master file, created by
   sphinx-quickstart on Fri Jun 16 10:59:54 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TIMES - The Integrated MARKAL-EFOM System's documentation!
=====================================================================

This documentation is composed of four Parts.

**[Part I]** provides a general description of the TIMES paradigm, with emphasis on the model's general structure and its economic significance. Part I also includes a simplified mathematical formulation of TIMES, a chapter comparing it to the MARKAL model, pointing to similarities and differences, and chapters describing new model options.

**[Part II]** constitutes a comprehensive reference manual intended for the technically minded modeler or programmer looking for an in-depth understanding of the complete model details, in particular the relationship between the input data and the model mathematics, or contemplating making changes to the model's equations. Part II includes a full description of the sets, attributes, variables, and equations of the TIMES model.

**[Part III]** describes the organization of the TIMES modeling environment and the GAMS control statements required to run the TIMES model. GAMS is a modeling language that translates a TIMES database into the Linear Programming matrix, and then submits this LP to an optimizer and generates the result files. Part III describes how the routines comprising the TIMES source code guide the model through compilation, execution, solve, and reporting; the files produced by the run process and their use; and the various switches that control the execution of the TIMES code according to the model instance, formulation options, and run options selected by the user. It also includes a section on identifying and resolving errors that may occur during the run process.

**[Part IV]** provides a step-by-step introduction to building a TIMES model in the VEDA2.0 user interface for model management and results analysis. It first offers an orientation to the basic features of VEDA2.0, including software layout, data files and tables, and model management features, both for handling the input and examining the results. It then describes in detail twelve Demo models (available for download from the ETSAP website) that progressively introduce VEDA-TIMES principles and modeling techniques.

.. toctree::
   :numbered:
   :maxdepth: 2
   :titlesonly:
   
   part-1/index
   part-2/index
   part-3/index
   part-4/index



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
