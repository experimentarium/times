# PART II: REFERENCE MANUAL

The purpose of the Reference Manual is to lay out the full details of
the TIMES model, including data specification, internal data structures,
and mathematical formulation of the model's Linear Program (LP)
formulation, as well as the Mixed Integer Programming (MIP) formulations
required by some of its options. As such, it provides the TIMES
modeller/programmer with sufficiently detailed information to fully
understand the nature and purpose of the data components, model
equations and variables. A solid understanding of the material in this
Manual is a necessary prerequisite for anyone considering making
programming changes in the TIMES source code.

The Reference Manual is organized as follows:

Chapter 1 Basic notation and conventions: lays the groundwork for
understanding the rest of the material in the Reference Manual;

Chapter 2 Sets: explains the meaning and role of various sets that
identify how the model components are grouped according to their nature
(e.g. demand devices, power plants, energy carriers, etc.) in a TIMES
model;

Chapter 3 Parameters: elaborates the details related to the
user-provided numerical data, as well as the internally constructed data
structures, used by the model generator (and report writer) to derive
the coefficients of the LP matrix (and prepare the results for
analysis);

Chapter 4 Usage notes on special types of processes: Gives additional
information about using input sets and parameters for the modelling of
special types of processes: CHP, inter-regional exchange, and storage
processes;

Chapter 5 Variables: defines each variable that may appear in the
matrix, both explaining its nature and indicating how it fits into the
matrix structure;

Chapter 6 Equations: states each equation in the model, both explaining
its role and providing its explicit mathematical formulation. Includes
user constraints that may be employed by modellers to formulate
additional linear constraints, which are not part of the generic
constraint set of TIMES.

Appendix A The Climate Module;

Appendix B The Damage Cost Functions;

Appendix C The Endogenous Technological Learning capability;

Appendix D TIMES Demand Functions.
	
	
```{toctree}
---
titlesonly:
glob:
---
*
```