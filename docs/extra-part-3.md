---
title: |
  **Energy Technology Systems Analysis Programme**

  []{#OLE_LINK19 .anchor}

  [http://www.iea-etsap.org/web/Documentation.asp]{.underline}
---

Documentation for the TIMES Model

PART III

July 2016\
(Last update: January 2023)

Authors:

Gary Goldstein

Amit Kanudia

Antti Lehtilä

Uwe Remme

Evelyn Wright

**General Introduction** **to the TIMES Documentation**

This documentation is composed of five Parts.

**[Part I]{.underline}** provides a general description of the TIMES paradigm, with emphasis on the model's general structure and its economic significance. Part I also includes a simplified mathematical formulation of TIMES, a chapter comparing it to the MARKAL model, pointing to similarities and differences, and chapters describing new model options.

**[Part II]{.underline}** constitutes a comprehensive reference manual intended for the technically minded modeler or programmer looking for an in-depth understanding of the complete model details, in particular the relationship between the input data and the model mathematics, or contemplating making changes to the model's equations. Part II includes a full description of the sets, attributes, variables, and equations of the TIMES model.

**[Part III]{.underline}** describes the organization of the TIMES modeling environment and the GAMS control statements required to run the TIMES model. GAMS is a modeling language that translates a TIMES database into the Linear Programming matrix, and then submits this LP to an optimizer and generates the result files. Part III describes how the routines comprising the TIMES source code guide the model through compilation, execution, solve, and reporting; the files produced by the run process and their use; and the various switches that control the execution of the TIMES code according to the model instance, formulation options, and run options selected by the user. It also includes a section on identifying and resolving errors that may occur during the run process.

**[Part IV]{.underline}** provides a step-by-step introduction to building a TIMES model in the VEDA model management software. It first offers an orientation to the basic features of VEDA, including software layout, data files and tables, and model management features. It then describes in detail twelve Demo models (available for download from the ETSAP website) that progressively introduce VEDA-TIMES principles and modeling techniques. It also provides a guide to results processing, including how to create and view results tables, and to create and modify user-defined sets.


PART III: THE OPERATION OF THE TIMES CODE