# TIMES Demand Functions

## Introduction

As discussed in Chapters 3 and 4 of Part I, in TIMES the standard Demand
Function formulation includes only sensitive of the demands to their own
prices, modeled through a linearized formulation of the price
elasticities. Until TIMES v4.0, only the linearized own-price elasticity
formulation was available in the common code. In MARKAL, the
corresponding non-linear formulation was also available (see Loulou &
al. 2004), and it was therefore subsequently made available in TIMES
v4.1 and above, as the first natural generalization of the original
demand functions.

When substitution possibilities are to be modeled, demand functions
involving Constant Elasticity of Substitution (CES) aggregates are very
commonly used in economic models integrating engineering and
bio-physical properties. Hence, the possibility to use CES-based demand
functions were considered desirable also in TIMES. The non-linear option
implemented for modeling CES aggregates is based on the old sketches
that were found in the MARKAL GAMS code (but were not active in the
code), designed by Dr. Denise Van Regemorter and implemented by Gary
Goldstein. Just like under the own-price elasticity option, the
calibration of the CES functions is based on the demand projections and
the corresponding shadow prices from the solution of a Baseline TIMES
run. When defining CES functions, the substitution elasticity between
the demands within each CES aggregate is given as an input. The
aggregate outputs of the CES functions may then be considered as the
final useful demands, with the standard exogenous Baseline projections
and own-price elasticities provided for the aggregate demands.

A linearization of the CES demand function formulation has also been
implemented, and is available in three different variants. In the
lienearized formulation, the CES demand functions can be also
subsequently nested further into higher-level CES functions.

All the generalizations presented in this Appendix have been implemented
in TIMES v4.1.0. For now, the implementation should be still considered
experimental, and therefore any feedback, comments and suggestions from
TIMES users concerning the formulation and implementation are welcome.

In this Appendix we provide the input attributes and modeling details
associated with the generalized Demand Functions in TIMES. As mentioned
above, the implementation of the Demand Functions in TIMES is based on
the corresponding formulations originally designed for the MARKAL model
generator. The next three sections of the Appendix will address the
Sets, Parameters, Variables, and Equations related to the Demand
Function options, including the special volume-preserving CES option
where the aggre­gate volume of the components of the combined demand
remains equal to the (optionally weighted) sum of the component demands
also under any substitution taking place.

## Mathematical formulation

For the own-price elasticities, we have the following relations (see
Part I, Chapter 4), where *U~i~* is the term in the objective function
associated with the utility change due to the demand variation of demand
*i*:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$DM_{i}/D{M_{i}}^{0} = (p_{i}/p_{i}^{0})^{E_{i}}$$                                                                                                                   \(1\)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------
  $$p_{i} = p_{i}^{0} \cdot (DM_{i}/D{M_{i}}^{0})^{1/E_{i}}$$                                                                                                           \(2\)

  $$U_{i} = \sum_{t}^{}\left( \frac{p_{i}^{0}(t)}{(1 + 1/E_{i})} \cdot \left\lbrack DM_{i}^{0}(t) \right\rbrack^{- 1/E_{i}} \bullet DM_{i}(t)^{1 + 1/E_{i}} \right)$$   \(3\)
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Consider then a utility function of the general CES form:

  --------------------------------------------------------------------------------------------------------------------------------------------
  $$U_{k} = \left( \sum_{i}^{}{\alpha_{i}^{\frac{1}{\sigma}}x_{i}^{\frac{\sigma - 1}{\sigma}}} \right)^{\frac{\sigma}{\sigma - 1}}$$   \(4\)
  ------------------------------------------------------------------------------------------------------------------------------------ -------

  --------------------------------------------------------------------------------------------------------------------------------------------

where:

-   *U~k~* is the total aggregate utility of demand *k*

-   *x~i~* is the demand for commodity *i* (component of the aggregate
    demand)

-   *α~i~* is a share parameter (the sum of which over *i* needs not be
    equal to 1)

-   *σ* is the elasticity of substitution (0 \< *σ* \< ∞)

The demand functions for *x~i~* can be derived from the utility function
in terms of prices, and can be given by the formulas:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$x_{i} = \frac{\alpha_{i}m}{p_{i}^{\sigma}}\left( \sum_{i}^{}{\alpha_{i}p_{i}^{1 - \sigma}} \right)^{- 1} = \frac{\alpha_{i}m}{p_{u}}\left( \frac{p_{u}}{p_{i}} \right)^{\sigma}$$   \(5\)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

where *m* is the income level, and *p~u~* is the aggregate price, or
unit cost, of the utility, can be given in terms of the individual
prices *p~i~* of the demands *i*:

  -----------------------------------------------------------------------------------------------------
  $$p_{u} = \left( \sum_{i}^{}{\alpha_{i}p_{i}^{1 - \sigma}} \right)^{\frac{1}{1 - \sigma}}$$   \(6\)
  --------------------------------------------------------------------------------------------- -------

  -----------------------------------------------------------------------------------------------------

The share parameters *α~i~* can be derived from the expenditure shares,
as shown in Eq. (7) below. In the objective function, the utility change
can then be calculated by the expression shown in Eq. (9) below.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$\alpha_{i}^{k} = \frac{agg_{i}^{k}(t) \cdot DM_{i}^{0}(t)}{DM_{k}^{0}(t)} \cdot \left( \frac{p_{i}^{0}(t)}{agg_{i}^{k}(t) \cdot p_{u_{k}}^{0}(t)} \right)^{\sigma}$$                                                                                                                                                                                                                  \(7\)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------
  $$\beta_{k} = \left( \frac{p_{u_{k}}^{0}(t)}{1 + \frac{1}{E_{k}}} \right) \cdot \left( DM_{k}^{0}(t) \right)^{\frac{- 1}{E_{k}}}$$                                                                                                                                                                                                                                                      \(8\)

  $$U_{k} = \sum_{t}^{}\left( \beta_{k}(t) \cdot \left( \left( \left( \sum_{i}^{}{\left( \alpha_{i}^{k}(t) \right)^{\frac{1}{\sigma_{k}}} \cdot \left( agg_{i}^{k}(t) \cdot DM_{i}^{k}(t) \right)^{\frac{\sigma_{k} - 1}{\sigma_{k}}}} \right)^{\frac{\sigma_{k}}{\sigma_{k} - 1}} \right)^{1 + \frac{1}{E_{k}}} - \left( DM_{k}^{0}(t) \right)^{1 + \frac{1}{E_{k}}} \right) \right)$$   \(9\)
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the above, the coefficients *agg~i~* are represent user-defined
aggregation coefficients for defining the aggregation from the component
demands to the aggregate demands. The constant term corresponding to the
Baseline value is subtracted in order to reproduce the value of the
Baseline objective function when no variation occurs from the Baseline
demands. The non-linear formulation of the elastic demand functions
implemented in TIMES follows these expressions.

The corresponding linearized formulations are based on piece-wise linear
functions which approximate the integrals over the inverse demand
curves, as explained in Part I, Chapter 4. The method described there
has been generalized to linearize also the somewhat more complex CES
demand functions, allowing also for nested CES functions. Each demand
having own-price or substitution elasticities requires the definition of
as many variables as there are steps in the discrete representation of
the demand curve (both upward and downward), for each period and region.
Each such variable has an upper bound, and in the CES formulation they
are included in an additional balance equation. However, otherwise the
step variables are not involved in other new constraints. Therefore, the
linear program is augmented by a number of variables, but does not have
any notable number of more constraints than the initial inelastic LP.
For partial equilibrium models, volume-preserving demand functions may,
however, be preferred over standard CES formulations, and therefore an
option for using a simple volume-preserving variant of the CES
linearization has been also implemented.

The resulting linearization has been verified to work well over a large
range of demand elasticities and price changes, and indeed also with
nested CES functions. Cobb-Douglas functions (*σ* = 1) are also
supported. Using the same linearization approach, even the simple Macro
general equilibrium model, which is integrated in TIMES-Macro and
includes Cobb-Douglas function nested into a CES production function,
might be in principle linearized into an LP problem.

It is also important to note again here that, instead of maximizing the
net total surplus, TIMES minimizes its negative (plus a constant). For
this and other reasons, it is inappropriate to pay too much attention to
the meaning of the *absolute* objective function values. Rather,
examining the difference between the objective function values of two
scenarios is a far more useful exercise. That difference is of course,
the negative of the difference between the net total surpluses of the
two scenario runs.

## Sets, Switches and Parameters

### Switches

Besides the basic data parameters described in Table D-2 below, the user
controls whether the linear or non-linear formulation is activated by
means of the switches shown in Table D-1. These switches are provided by
the data handling system when the user indicates that the option is to
be included in a run.

+--------------------+-------------------------------------------------+
| **Switch**         | **Parameter Description**                       |
+====================+=================================================+
| > \$SET TIMESED NO | Causes the Base Prices to be saved to a GDX     |
|                    | file, for subsequent use in a policy analysis   |
|                    | run based on any of the elastic demand options. |
+--------------------+-------------------------------------------------+
| > \$SET TIMESED    | Activates any of LP formulations used for       |
| > YES              | Demand Functions (exact formulations depending  |
|                    | on input data)                                  |
+--------------------+-------------------------------------------------+
| > \$SET MICRO YES  | Activates any of NLP or mixed LP/NLP            |
|                    | formulations used for Demand Functions (exact   |
|                    | formulations depending on input data)           |
+--------------------+-------------------------------------------------+

### Sets and Parameters

Like all other aspects of TIMES the user describes the demand functions
for the energy system model by means of a Set and the Parameters and
Switches described in this chapter. Table D-2 below describes the User
Input Parameters associated with defining the TIMES demand functions.

+---------+--------+---------------------------------------------------+
| **Pa    | *      | **Parameter Description**                         |
| rameter | *Units |                                                   |
| (Ind    | &      |                                                   |
| exes)** | defa   |                                                   |
|         | ults** |                                                   |
+=========+========+===================================================+
| > CO    | Com    | Exogenous reference (Baseline) demand projection  |
| M_PROJ\ | modity | of commodity **c** in region **r** and year       |
| >       | unit;\ | **y**.                                            |
| (r,y,c) | \      |                                                   |
|         | [0,∞)\ | In inelastic runs (Baseline runs, and any other   |
|         | d      | model runs with non-elastic demands) the demands  |
|         | efault | are met at the levels of the exogenous            |
|         | valu   | projections defined by COM_PROJ, usually exactly, |
|         | e:none | but under certain circumstances some of them may  |
|         |        | also end up at a higher level than the            |
|         | D      | projection.                                       |
|         | efault |                                                   |
|         | i/e:   |                                                   |
|         | STD    |                                                   |
+---------+--------+---------------------------------------------------+
| > C     | Com    | Defines an aggregation of component demand **c**  |
| OM_AGG\ | modity | into an aggregate demand **com** in region **r**  |
| > (r,y  | units  | and year (period) **y**.                          |
| ,c,com) |        |                                                   |
|         | \[o    | Defining COM_AGG between the component demands    |
|         | pen\]; | and the aggregate demand is required for modeling |
|         |        | substitution elasticities.                        |
|         | d      |                                                   |
|         | efault | If defined zero (e.g. by specifying IE=2), the    |
|         | valu   | values will be auto-generated according to the    |
|         | e:none | price ratios; defining the COM_AGG values zero is |
|         |        | required for using the proper CES functions.      |
|         | D      |                                                   |
|         | efault |                                                   |
|         | i/e:   |                                                   |
|         | STD    |                                                   |
+---------+--------+---------------------------------------------------+
| >       | Dim    | Defines the maximum demand variation in the lower |
| COM_VOC | ension | / upper direction (**bd**=LO/UP) for demand **c** |
| >       | -less; | in region **r** and year **y**. The value gives   |
| > (r,   |        | the maximum deviation in proportion to the        |
| y,c,bd) | \[     | Baseline demand.\                                 |
|         | 0,∞);\ | Different values may be provided for each         |
|         | d      | direction, thus demand elasticity curves may be   |
|         | efault | asymmetric.                                       |
|         | valu   |                                                   |
|         | e:none |                                                   |
|         |        |                                                   |
|         | D      |                                                   |
|         | efault |                                                   |
|         | i/e:   |                                                   |
|         | STD    |                                                   |
+---------+--------+---------------------------------------------------+
| > C     | I      | Number of steps to use for the approximation of   |
| OM_STEP | nteger | demand variation in the lower / upper direction   |
| >       |        | (**bd**=LO/UP), and the associated change in      |
| > (     | \[     | producer/consumer surplus, for commodity **c** in |
| r,c,bd) | 1,∞);\ | region **r**, when using the elastic demand       |
|         | d      | formulations. The shortcut **bd**=FX may be used  |
|         | efault | for defining the same number of steps in both     |
|         | valu   | directions.                                       |
|         | e:none |                                                   |
+---------+--------+---------------------------------------------------+
| > CO    | Dim    | Elasticity of demand for commodity ***c***,       |
| M_ELAST | ension | indicating the following:                         |
| >       | -less; |                                                   |
| > (r,y, | \[o    | -   For own-price elasticities: how much the      |
| c,s,bd) | pen\]\ |     > demand rises/falls in response to a unit    |
|         | d      |     > change in the marginal cost of meeting a    |
|         | efault |     > demand that is elastic.                     |
|         | valu   |                                                   |
|         | e:none | -   For substitution elasticities: responsiveness |
|         |        |     > of the ratio in which the component demands |
|         | D      |     > are used to the ratio of the prices of      |
|         | efault |     > those demands                               |
|         | i/e:   |                                                   |
|         | STD    | Defines elasticities for demand ***c*** in region |
|         |        | ***r*** and year ***y***, timeslice ***s***       |
|         |        |                                                   |
|         |        | -   ***lim*** = LO/UP :\                          |
|         |        |     > defines the own-price elasticity in the     |
|         |        |     > lower / upper direction in the linear       |
|         |        |     > formulation                                 |
|         |        |                                                   |
|         |        | -   ***lim*** = FX (s=ANNUAL):\                   |
|         |        |     > defines own-price elasticities in the       |
|         |        |     > non-linear formulation;\                    |
|         |        |     > can also be used in the linear formulation  |
|         |        |     > for defining the own-price elasticities for |
|         |        |     > the aggregate demands, optionally also for  |
|         |        |     > defining component-differentiated           |
|         |        |     > susbstution elasticities                    |
|         |        |                                                   |
|         |        | -   ***lim*** = N (s=ANNUAL):\                    |
|         |        |     > defines the substitution elasticity for     |
|         |        |     > component demands of the demand aggregation |
|         |        |     > represented by commodity ***c***; positive  |
|         |        |     > values signify the standard variant,        |
|         |        |     > negative values signify the                 |
|         |        |     > volume-preserving variant formulation       |
+---------+--------+---------------------------------------------------+

**Important remarks:**

-   *COM_PROJ* should be explicitly defined by the user only for the
    component demands, and never for the aggregate demands.

-   As mentioned in Table D-2, the substitution elasticities can be
    defined by specifying *COM_ELAST*(r,t,com,ANNUAL,\'N\') for the
    aggregate demands. However, \'FX\' elasticities for the *component
    demands* can be optionally specified for defining
    component-differentiated substitution elasticities. Nonetheless,
    even when doing so, *COM_ELAST*(r,t,com, ANNUAL,\'N\') always
    defines the minimum substitution elasticity among the component
    demands of ***com***.

-   Note that the aggregate demands are always at the ANNUAL level only,
    and thus only ANNUAL level own-price demand elasticities are
    supported for the demand aggregates.

-   When using the non-linear formulation, demand substitution is
    supported only at the ANNUAL level for the component demands of the
    CES aggregates. The demand variations will thus be proportionally
    the same for all timeslices.

-   Multi-level nested CES demand aggregations are also fully supported
    both in the non-linear and in the linearized case.

-   Recursive CES demand aggregations are not supported, neither in the
    non-linear nor in the linearized case.

-   The Cobb-Douglas case (*σ~k~*=1) is also supported, but in the
    non-linear formulation it is handled by setting *σ~k~* very close to
    unity.

## Examples

Assume that we wish to define a non-linear CES demand function for the
aggregate demand TLPKM (passenger land travel), having the following
component demands:

-   TRT -- passenger car travel

-   TRB -- passenger bus travel

-   TRW -- passenger two-wheeler travel

-   TTP -- passenger rail travel

The demand function can be set up with the following input parameters
(where **r** stands for regions, **t** for milestone years, and
\'**0**\' for interpolation option placeholder):

  ---------------------------------------------------------------------------------------
  **Parameters**                                     **Description**
  -------------------------------------------------- ------------------------------------
  COM_AGG(r,\'0\',\'TRT\',\'TLPKM\') = 2;            Aggregation of TRT into TPASS with
                                                     price ratios

  COM_AGG(r,\'0\',\'TRB\',\'TLPKM\') = 2;            Aggregation of TRB into TPASS with
                                                     price ratios

  COM_AGG(r,\'0\',\'TRW\',\'TLPKM\') = 2;            Aggregation of TRW into TPASS with
                                                     price ratios

  COM_AGG(r,\'0\',\'TTP\',\'TLPKM\') = 2;            Aggregation of TTP into TPASS with
                                                     price ratios

  COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'FX\')=0.35;   Own-price elasticity of aggregate
                                                     demand

  COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'N\')=1.2;     Elasticity of substitution between
                                                     components

  COM_VOC(r,t,\'TLPKM\',\'UP\')=1;                   Max. upper variance of aggregate
                                                     demand
  ---------------------------------------------------------------------------------------

Assume now that we wish to define the same demand function but with the
linear formulation for the CES function. The demand function can be set
up with the following input parameters (where **r** stands for regions,
**t** for milestone years, and **bd** for the inequality bound types
(\'LO\', \'UP\')):

  ---------------------------------------------------------------------------------------
  **Parameters**                                     **Description**
  -------------------------------------------------- ------------------------------------
  COM_AGG(r,\'0\',\'TRT\',\'TLPKM\') = 2;            Aggregation of TRT into TPASS with
                                                     price ratios

  COM_AGG(r,\'0\',\'TRB\',\'TLPKM\') = 2;            Aggregation of TRB into TPASS with
                                                     price ratios

  COM_AGG(r,\'0\',\'TRW\',\'TLPKM\') = 2;            Aggregation of TRW into TPASS with
                                                     price ratios

  COM_AGG(r,\'0\',\'TTP\',\'TLPKM\') = 2;            Aggregation of TTP into TPASS with
                                                     price ratios

  COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'FX\')=0.35;   Own-price elasticity of aggregate
                                                     demand

  COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'N\')=1.2;     Elasticity of substitution between
                                                     components

  COM_STEP(r,\'TRT\',\'FX\')=100;                    Number of steps for TRT in both
                                                     directions

  COM_STEP(r,\'TRB\',\'FX\')=100;                    Number of steps for TRB in both
                                                     directions

  COM_STEP(r,\'TRW\',\'FX\')=100;                    Number of steps for TRW in both
                                                     directions

  COM_STEP(r,\'TTP\',\'FX\')=100;                    Number of steps for TTP in both
                                                     directions

  COM_STEP(r,\'TLPKM\',\'LO\')=120;                  Number of steps for TLPKM in lower
                                                     direction

  COM_STEP(r,\'TLPKM\',\'UP\')=80;                   Number of steps for TLPKM in upper
                                                     direction

  COM_VOC(r,t,\'TRT\',bd)=0.8;                       Max. variance of TRT, given in both
                                                     directions

  COM_VOC(r,t,\'TRB\',bd)=0.8;                       Max. variance of TRB, given in both
                                                     directions

  COM_VOC(r,t,\'TRW\',bd)=0.8;                       Max. variance of TRW, given in both
                                                     directions

  COM_VOC(r,t,\'TTP\',bd)=0.8;                       Max. variance of TTP, given in both
                                                     directions

  COM_VOC(r,t,\'TLPKM\',\'LO\')=0.5;                 Max. lower variance of aggregate
                                                     demand

  COM_VOC(r,t,\'TLPKM\',\'UP\')=0.3;                 Max. upper variance of aggregate
                                                     demand
  ---------------------------------------------------------------------------------------

Note that using \'FX\' as a shortcut for bd={\'LO\',\'UP\'} in
*COM_STEP* is only supported in TIMES v4.4.0 and above, and that
*COM_VOC* does not have any such shortcut.

## Variables

The variables that are used to model the Demand Functions in TIMES are
presented in Table D-5 below. The primary role of the variables and
equations used to model the functions is to control the standard TIMES
variable and the associated dynamic cost of these.

+-------------+--------------------------------------------------------+
| **Variable  | **Variable Description**                               |
| (Indexes)** |                                                        |
+=============+========================================================+
| >           | Variable used for tracking the Gross production of a   |
|  VAR_COMPRD | commodity **c** in region **r**, period **t**, and     |
| >           | timeslice **s**.                                       |
| > (r,t,c,s) |                                                        |
+-------------+--------------------------------------------------------+
| > VAR_DEM   | Variable used for the enodenous (elastic) demand for   |
| >           | commodity **c** in region **r**, and period **t**,     |
| > (r,t,c)   | when the demand function is non-linear.                |
+-------------+--------------------------------------------------------+
| > VAR_ELAST | Step variables used to linearize elastic demand curves |
| >           | for demand **c** in region **r**, period **t**, and    |
| > (         | timeslice **s**. The index **bd**=LO corresponds to    |
| r,t,c,s,bd) | the direction of decreasing the demand, while          |
|             | **bd**=UP denotes the direction for demand increase.   |
+-------------+--------------------------------------------------------+
| >           | Variable used for accounting the total discounted      |
| VAR_OBJELS\ | endogenous losses (**bd**=LO) or gains (**bd**=UP) in  |
| >           | the utility of region **r** in currency **cur**        |
|  (r,bd,cur) | through the demand variations of all elastic demands.  |
+-------------+--------------------------------------------------------+

### VAR_COMPRD(r,t,c,s)

**Description:** The amount of demand commodity **c** procured at time
period **t**, timeslice **s**.

**Purpose and** This variable tracks the total amount of demand
commodity produced.

**Occurrence:** This variable is normally only created if a bound is
imposed on total production of the demand commodity, or a cost is
explicitly associated with the production level of the demand. However,
when defining CES demand functions, the variable is always created both
for the component demand and for the aggregate demand. The variable is
defined through the equations EQE_COMPRD and/or EQ(l)\_COMBAL.

**Units:** PJ, Bvkm, or any other unit defined by the analyst to
represent the quantity of the demand.

**Bounds:** This variable is non-negative. It is by default not
otherwise directly bounded. It can be directly bounded by the COM_BNDPRD
attribute. It may be indirectly bounded by specifying a user constraint
referring to it by UC_COMPRD.

### VAR_DEM

**Description:** The total amount of demand for commodity **c** in time
period **t**.

**Purpose:** This variable is used for tracking the endogenous amount of
demand for commodity **c** in the non-linear formulation of elastic
demands.

**Occurrence:** This variable is not created in the LP formulation. It
is only created in the non-linear formulation of demand functions based
on own-price and/or substitution elasticities (as well as in the Macro
formulation). It is generated for each demand with a non-linear
own-price elasticity function, and for all demands associated with a
non-linear CES demand function.

**Units:** PJ, Bvkm, or any other unit in which demands are tracked.

**Bounds:** This variable is non-negative and is not bounded upwards.

### VAR_ELAST (r,t,c,s,j,bd)

**Description:** Variables used to linearize elastic demand curves by
step-wise variations.

**Purpose:** To indicate how far the demand variation extends on the
elasticity curve, by step.

**Occurrence:** Each elastic demand is expressed as the sum of these
variables. In the objective function, these variables are used to bear
the cost of demand losses and revenues of demand gains as explained in
Part I, Chapter 4.

These variables are defined whenever a demand is declared to be price
elastic, either to its own price or through cross-elastic substitution.
These variables are indexed by j, where j runs over the number of steps
used for discretizing the demand curve of demand commodity c. The jth
variable stands for the portion of the demand that lies within
discretization interval **j**, on side **bd** (**bd** indicates either
increase or decrease of demand w.r.t. the reference case demand). In the
objective function, these variables are used to represent the utility
change caused by demand losses or gains, as explained in Part I, Chapter
4.

**Units:** Demand units: PJ, Bvkm, or any other unit in which the demand
is tracked.

**Bounds:** This variable is non-negative. Each ELAST variable is
bounded upward via virtual equation EQ_BNDELAS, of in the case of a CES
function, via the equation EQL_COMCES.

### VAR_OBJELS (r,bd,cur)

**Description:** Variables used to linearize elastic demand curves by
step-wise variations.

**Purpose:** To indicate how far the demand variation extends on the
elasticity curve.

**Occurrence:** The utility change caused by all demand losses and gains
as explained in Part I, Chapter 4.

These variables are defined whenever any of the elastic demand
formulations is used. These variables are indexed by **bd** (**bd**
indicates either increase or decrease of demand w.r.t. the reference
case demand). These variables are included in the objective function, to
represent the total utility changes caused by demand losses or gains, as
explained in Part I, Chapter 4.

**Units:** Demand units: PJ, Bvkm, or any other unit in which the demand
is tracked.

**Bounds:** This variable is non-negative.

## Equations

The equations that are used to model the demand functions in TIMES are
presented in Table D-6 below. The primary role of the variables and
equations used to model Demand Functions is to control the standard
TIMES demand variables VAR_DEM and the associated losses or gains in
consumer\'s utility in the regional demand utility part of the objective
function (EQ_OBJELS).

+------------+---------------------------------------------+-----------+
| **C        | **Constraint Description**                  | **GAMS    |
| onstraints |                                             | Ref**     |
| (          |                                             |           |
| Indexes)** |                                             |           |
+============+=============================================+===========+
| >          | The commodity balance constraint associated | EQC       |
| EQG_COMBAL | with the demand function of commodity c, as | OMBAL.mod |
| >          | an inequality. The constraint requires that |           |
| >          | the total production of the demand          |           |
|  (r,t,c,s) | commodity is greater than or equal to the   |           |
|            | endogenous elastic demand. This constraint  |           |
|            | is normally generated for all demands       |           |
|            | modeled with own-price elasticities.        |           |
+------------+---------------------------------------------+-----------+
| >          | The commodity balance constraint associated | EQC       |
| EQE_COMBAL | with the demand function of commodity c, as | OMBAL.mod |
| >          | a strict equality. This constraint is       |           |
| >          | automatically generated for the component   |           |
|  (r,t,c,s) | demands of all CES demand functions, i.e.   |           |
|            | demands modeled with substitution           |           |
|            | elasticities.                               |           |
+------------+---------------------------------------------+-----------+
| >          | This equation is a strict equality and is   | EQC       |
| EQE_COMPRD | generated in two forms for the demands      | OMBAL.mod |
| >          | included in demand functions:               |           |
| >          |                                             |           |
|  (r,t,c,s) | 1.  Defining equation for the commodity     |           |
|            |     production of commodity c. This         |           |
|            |     constraint is automatically generated   |           |
|            |     for all the component demands of CES    |           |
|            |     demand functions.                       |           |
|            |                                             |           |
|            | 2.  Balance equation for the total          |           |
|            |     variation of the component demands of   |           |
|            |     the aggregate demands of CES demand     |           |
|            |     functions. This constraint is           |           |
|            |     automatically generated for all the     |           |
|            |     aggregate demands of CES demand         |           |
|            |     functions.                              |           |
+------------+---------------------------------------------+-----------+
| >          | The constraint bounding the step variables  | EQO       |
| EQL_COMCES | of a demand commodity **c** included as a   | BJELS.mod |
| >          | component in the CES function of demand     |           |
| > (r,      | aggregate **com**. The constraint is        |           |
| t,com,c,s) | generated for each of the component demands |           |
|            | whenever the aggregate demand of a CES      |           |
|            | function has been modeled with an own-price |           |
|            | elasticity (otherwise variable bounds are   |           |
|            | sufficient).                                |           |
+------------+---------------------------------------------+-----------+
| >          | The calculation of the endogenous losses or | EQO       |
|  EQ_OBJELS | gains in utility through the demand         | BJELS.mod |
| >          | variations of all elastic demands are       |           |
| >          | discounted and summed together into the     |           |
| (r,bd,cur) | VAR_OBJELS variable representing the        |           |
|            | regional elastic demand cost part of the    |           |
|            | objective function, which is subsequently   |           |
|            | included in the total objective function    |           |
|            | (EQ_OBJ).                                   |           |
+------------+---------------------------------------------+-----------+

[^1]: *GAMS A User's Guide*, A. Brooke, D. Kendrick, A. Meeraus, R.
    Raman, GAMS Development Corporation, December 1998.

[^2]: The meaning and the role of internal and external regions is
    discussed in Section 2.2.

[^3]: See Section for a more in-depth treatment of commodity groups.

[^4]: This column contains the names of the indexes as used in this
    document.

[^5]: For programming reasons, alternative names (aliases) may exist for
    some indexes. This information is only relevant for those users who
    are interested in gaining an understanding of the underlying GAMS
    code.

[^6]: This column refers to possible related indexes, e.g. the index set
    **c** is a subset of the index set **cg**.

[^7]: VEDA/ANSWER compiles the complete list from the union of the
    commodities defined in each region.

[^8]: VEDA/ANSWER compiles the complete list from the union of the
    commodity groups defined in each region.

[^9]: VEDA/ANSWER compiles the complete list from the union of processes
    defined in each region.

[^10]: Important cases are the process type CHP, which activates the CHP
    attributes, storage process indicators (STG, STS, STK, NST), and
    material conversion process types PRW and PRV, which may affect the
    creation of the internal set **prc_spg** (see ).

[^11]: In this case the model may still decide to add additional new
    capacity, if this is economical and not inhibited by any investment
    bounds.

[^12]: The purpose of this table is to list those parameters whose year
    values are independent of the input **datayear**s associated with
    most of the regular parameters, and therefore need not be included
    in the set **datayear**. For example, a value for MULTI(j,\'2012\')
    would not require including 2012 in **datayear**s if 2012 were not
    relevant to the other input parameters.

[^13]: By setting G_YRFR(r,s)=0 one can exclude any individual
    timeslices from specific regions, even if only a global timeslice
    tree is defined for all regions (as it is the case when using
    VEDA-FE). In this way each region can employ a different subset of
    the global tree.

[^14]: Note however that some flexibility is lost when using
    multilateral trade. For instance, it is not possible to express
    transportation costs in a fully accurate manner, if such cost
    depends upon the precise pair of trading regions in a specific way.

[^15]: The first row contains the set name. If the set is a
    one-dimensional subset of another set, the second row contains the
    parent set in brackets. If the set is a multi-dimensional set, the
    second row contains the index domain in brackets.

[^16]: For programming reasons, alternative names (aliases) may exist
    for some indexes. This information is only relevant for those users
    who are interested in gaining an understanding of the underlying
    GAMS code.

[^17]: For multidimensional sets such as this one, two definitions are
    sometimes given, one as an indicator function or mapping, the other
    (in square brackets) as a set of n-tuples.

[^18]: Name of the internal set as used in this documentation and the
    GAMS code.

[^19]:
    > Index domain of the internal set is given in brackets (Note: the
    > symbols **y**, **y1**, **y2**, **k**, and **ll** all refer to
    > **year**).

[^20]:
    > The asterisk denotes in the modeling system GAMS a wildcard, so
    > that domain checking is disabled and any index may be used.

[^21]: The term *target timeslice level* or *target timeslice* is used
    in the following as synonym for the timeslice level or timeslices
    which are required by the model generators depending on the process
    or commodity timeslice resolution (**prc_tsl** and **com_tsl**
    respectively).

[^22]: Note that as an exception, for NCAP_AF direct inheritance and
    aggregation will be disabled if any values are specified at the
    process timeslice level. However, this may be circumvented by using
    NCAP_AFS for defining the values at process timeslices.

[^23]: The first row contains the parameter name, the second row
    contains in brackets the index domain over which the parameter is
    defined.

[^24]: This column gives references to related input parameters (in
    upper case) or sets (in lower case) being used in the context of
    this parameter as well as internal parameters/sets or result
    parameters being derived from the input parameter.

[^25]: This column lists the unit of the parameter, the possible range
    of its numeric value \[in square brackets\] and the
    inter-/extrapolation rules that apply.

[^26]: An indication of circumstances for which the parameter is to be
    provided or omitted, as well as description of
    inheritance/aggregation rules applied to parameters having the
    timeslice (**s)** index.

[^27]: Equations or variables that are directly affected by the
    parameter.

[^28]: Abbreviation i/e = inter-/extrapolation

[^29]: Standard aggregation not implemented for FLO_BND.

[^30]: The indexing of auxiliary consumption flows or emissions of
    inter-regional exchange processes is illustrated in the figure
    below.

    ![](media/image10.png){width="4.760416666666667in"
    height="1.40625in"}

[^31]: The first row contains the parameter name, the second row
    contains in brackets the index domain, for which the parameter is
    defined.

[^32]: GDX stands for GAMS Data Exchange. A GDX file is a binary file
    that stores the values of one or more GAMS symbols such as sets,
    parameters variables and equations. GDX files can be used to prepare
    data for a GAMS model, present results of a GAMS model, store
    results of the same model using different parameters etc. They do
    not store a model formulation or executable statements.

[^33]: The use of the **gdx2veda** tool together with the
    **times2veda.vdd** control file and the **VEDA-BE** software are
    described in Part V.

[^34]: First row: parameter name; second row (in brackets): the index
    domain, for which the parameter is defined.

[^35]: The activity remains constant over the iso-fuel line, but the
    electricity output varies when moving along it. Maximum electrical
    output is thus usually the most convenient quantity along this line
    for defining the basis of the process activity and capacity. This
    choice should then be consistently reflected in the input data (see
    Table 18).

[^36]: The indexing of auxiliary consumption flows or emissions of
    inter-regional exchange processes is illustrated in the figure
    below.

    ![](media/image10.png){width="4.760416666666667in"
    height="1.40625in"}

[^37]: The equation EQ(l)\_XBND may have an external regional as region
    index (bounding the import from one external regions to all other
    regions).

[^38]: In case the dollar control parameter VAR_UC is set to YES, the
    user constraints are always strict equalities (***l***=E) with the
    RHS constants replaced by the user constraint variables given in the
    table. The RHS bound parameter (UC_RHS(R)(T)(S)) are then applied to
    these user constraint related variables. See Section 5.20.

[^39]: The actual implementation of OBJ in the GAMS program is different
    from the one described in the documentation, since the annualizing
    of the various cost components is not performed in the GAMS code of
    the OBJ equation, but rather in the reporting section of the
    program, for improved code performance. However, despite the
    simplification, the GAMS code results in an objective function that
    is fully equivalent to the one in this documentation.

[^40]: This is the default definition adopted for *CRF*, corresponding
    to beginning-of-year discounting. For other discounting options, see
    Section .

[^41]: Ideally, it would be desirable that cases 1 be used only for
    those investments that have no lead time (and thus no interest
    during construction). However, if cases 1 are employed even for
    projects with significant IDC's, these should have their IDC
    included in the investment cost.

[^42]: Parameters that occur in the ETL-specific equations but that also
    occur in non-ETL equations (e.g., TCH_LIFE) are not listed in this
    table.

[^43]: GAMS moves all constants (e.g. past investments) on the RHS and
    the variables on the LHS of the equation. In the listing file the
    primal value of the equation can be found in the solution report
    under the LEVEL column. The RHS value is given under the column
    UPPER column in case of a \<= inequality and in the LOWER column for
    a \>= inequality. For an equality LOWER, LEVEL and UPPER value are
    the same.

[^44]: The primal value and the RHS constant of an equation can be found
    in the GAMS listing file in solution report part. The LEVEL value
    column corresponds to the primal value, the LOWER level value equals
    the RHS of a constraint of type \>= and the UPPER level value equals
    the RHS of a constraint of a type \<=.

[^45]: If the coefficient UC_ACT, UC_FLO, etc. is greater than one, it
    represents an annual growth rate, while a coefficient smaller than
    one describes an annual decay rate.

[^46]: There exists another well-known representation of CO~2~
    accumulation equations, using a five-box model.

[^47]: Note that the subscripts *atm* and *up*, which for the CO2
    equations referred to the atmosphere and upper reservoirs, have been
    reused for the CH4 and N2O equations to stand for anthropogenic and
    natural concentrations.

[^48]: The first row contains the parameter name, the second row
    contains in brackets the index domain over which the parameter is
    defined.

[^49]: This column gives references to related input parameters or sets
    being used in the context of this parameter as well as internal
    parameters/sets or result parameters being derived from the input
    parameter.

[^50]: This column lists the unit of the parameter, the possible range
    of its numeric value \[in square brackets\] and the
    inter-/extrapolation rules that apply.

[^51]: An indication of circumstances for which the parameter is to be
    provided or omitted.

[^52]: Equations or variables that are directly affected by the
    parameter.

[^53]: Abbreviation i/e = inter-/extrapolation
