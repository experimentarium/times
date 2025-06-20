(part-2-intro)=
# Introduction

## Basic notation and conventions

To assist the reader, the following conventions are employed consistently throughout this chapter:

- Sets, and their associated index names, are in lower and bold case, e.g., **com** is the set of all commodities;
- Literals, explicitly defined in the code, are in upper case within single quotes (note that in conformity with the GAMS syntax, single quotes must, in fact, be apostrophes), e.g., \'UP\' for upper bound;
- Parameters, and scalars (constants, i.e., un-indexed parameters) are in upper case, e.g., $NCAP\_AF$ for the availability factor of a technology;
- Variables are in upper case with a prefix of $VAR\_$, e.g., $VAR\_ACT$ corresponds to the activity level of a technology.
- Equations are in upper case with a prefix of $EQ\_$ or $EQ(l)\_$ with the placeholder ($l$) denoting the equation type ($l=E$ for a strict equality, $l=L$ for an inequality with the left hand side term being smaller than or equal to the right hand side term and $l=G$ for an inequality with the left hand side term being greater than or equal to the right hand side term), e.g., $EQ\_PTRANS$ is the process transformation equation (strict equality), and $EQG\_COMBAL$ is the commodity balance constraint of type $G$ (inequality).

## GAMS modelling language and TIMES implementation

TIMES consists of generic variables and equations constructed from the specification of sets and parameter values depicting an energy system for each distinct region in a model. To construct a TIMES model, a preprocessor first translates all data defined by the modeller into special internal data structures representing the coefficients of the TIMES matrix applied to each variable of {numref}`Chapter %s <variables>` for each equation of {numref}`Chapter %s <equations>` in which the variable may appear. This step is called Matrix Generation. Once the model is solved (optimised) a Report Writer assembles the results of the run for analysis by the modeller. The matrix generation, report writer, and control files are written in GAMS[^1] (the General Algebraic Modelling System), a powerful high-level language specifically designed to facilitate the process of building large-scale optimisation models. GAMS accomplishes this by relying heavily on the concepts of sets, compound indexed parameters, dynamic looping and conditional controls, variables and equations. Thus there is very a strong synergy between the philosophy of GAMS and the overall concept of the RES specification embodied in TIMES, making GAMS very well suited to the TIMES paradigm.

Furthermore, by nature of its underlying design philosophy, the GAMS code is very similar to the mathematical description of the equations provided in {numref}`Chapter %s <equations>`. Thus, the approach taken to implement a TIMES model is to "massage" the input data by means of a (rather complex) preprocessor that handles the necessary exceptions that need to be taken into consideration to properly construct the matrix coefficients in a form ready to be applied to the appropriate variables in the respective equations. GAMS also integrates seamlessly with a wide range of commercially available optimisers that are charged with the task of solving the actual TIMES linear (LP) or mixed integer (MIP) problems that represent the desired model. This step is called the Solve or Optimisation step. CPLEX or XPRESS are the optimisers most often employed to solve the TIMES LP and MIP formulations.

The standard TIMES formulation has optional features, such as lumpy investments and endogenous technology learning. The organization and layout of the TIMES code, along with how it is processed by GAMS during a model run, is discussed in detail in [PART III](project:/part-3/index.md). In addition, a modeller experienced in GAMS programming and the details of the TIMES implementation could define additional equation modules or report routine modules based on this organization, which allows the linkage of these modules to the standard TIMES code in a flexible way. However, any thoughts of modifying the core TIMES code should be discussed and coordinated with ETSAP.

To build, run, and analyse a TIMES model, several software tools have been developed in the past or are currently under development, so that the modeller does not need to provide the input information needed to build a TIMES model directly in GAMS. These tools are the model interfaces VEDA-FE and ANSWER-TIMES, as well as the reporting and analysing tool VEDA-BE.

[^1]: *GAMS A User's Guide*, A. Brooke, D. Kendrick, A. Meeraus, R. Raman, GAMS Development Corporation, December 1998.
