---
title: |
  **Energy Technology Systems Analysis Programme**

  []{#OLE_LINK19 .anchor}

  [http://www.iea-etsap.org/web/Documentation.asp]{.underline}
---

Documentation for the TIMES Model

PART IV: VEDA2.0

December 2020

Authors: G. Goldstein

> M. Gargiulo
>
> A. Kanudia

**General Introduction**

This documentation is composed of four Parts.

> **[Part I]{.underline}** provides a general description of the TIMES
> paradigm, with emphasis on the model's general structure and its
> economic significance. Part I also includes a simplified mathematical
> formulation of TIMES, a chapter comparing it to the MARKAL model,
> pointing to similarities and differences, and chapters describing new
> model options.
>
> **[Part II]{.underline}** constitutes a comprehensive reference manual
> intended for the technically minded modeler or programmer looking for
> an in-depth understanding of the complete model details, in particular
> the relationship between the input data and the model mathematics, or
> contemplating making changes to the model's equations. Part II
> includes a full description of the sets, attributes, variables, and
> equations of the TIMES model.
>
> **[Part III]{.underline}** describes the organization of the TIMES
> modeling environment and the GAMS control statements required to run
> the TIMES model. GAMS is a modeling language that translates a TIMES
> database into the Linear Programming matrix, and then submits this LP
> to an optimizer and generates the result files. Part III describes how
> the routines comprising the TIMES source code guide the model through
> compilation, execution, solve, and reporting; the files produced by
> the run process and their use; and the various switches that control
> the execution of the TIMES code according to the model instance,
> formulation options, and run options selected by the user. It also
> includes a section on identifying and resolving errors that may occur
> during the run process.
>
> **[Part IV]{.underline}** provides a step-by-step introduction to
> building a TIMES model in the VEDA2.0 user interface for model
> management and results analysis. It first offers an orientation to the
> basic features of VEDA2.0, including software layout, data files and
> tables, and model management features, both for handling the input and
> examining the results. It then describes in detail twelve Demo models
> (available for download from the ETSAP website) that progressively
> introduce VEDA-TIMES principles and modeling techniques.

PART IV: VEDA2.0[^1] Model Management System - Getting Started with the
VEDA-TIMES Demo Models

[^1]: Veda \[Sanskrit,=knowledge, cognate with English wit, from a root meaning know\], oldest scriptures of Hinduism and the most ancient religious texts in an Indo-European language. The authority of the Veda as stating the essential truths of Hinduism is still accepted to some extent by all Hindus. The Veda is the literature of the Aryans who invaded NW India c.1500 B.C. and pertains to the fire sacrifice that constituted their religion. The Vedic hymns were probably first compiled after a period of about 500 years during which the invaders assimilated various native religious ideas. The end of the Vedic period is about 500 B.C. Tradition ascribes the authorship of the hymns to inspired seer-poets (rishis). \[The Columbia Encyclopedia, 6th ed. New York: Columbia University Press, 2000. \]

