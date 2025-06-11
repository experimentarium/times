# TIMES Demand Functions

## Introduction

As discussed in Chapters 3 and 4 of Part I, in TIMES the standard Demand Function formulation includes only sensitive of the demands to their own prices, modeled through a linearized formulation of the price elasticities. Until TIMES v4.0, only the linearized own-price elasticity formulation was available in the common code. In MARKAL, the corresponding non-linear formulation was also available (see Loulou & al. 2004), and it was therefore subsequently made available in TIMES v4.1 and above, as the first natural generalization of the original demand functions.

When substitution possibilities are to be modeled, demand functions involving Constant Elasticity of Substitution (CES) aggregates are very commonly used in economic models integrating engineering and bio-physical properties. Hence, the possibility to use CES-based demand functions were considered desirable also in TIMES. The non-linear option implemented for modeling CES aggregates is based on the old sketches that were found in the MARKAL GAMS code (but were not active in the code), designed by Dr. Denise Van Regemorter and implemented by Gary Goldstein. Just like under the own-price elasticity option, the calibration of the CES functions is based on the demand projections and the corresponding shadow prices from the solution of a Baseline TIMES run. When defining CES functions, the substitution elasticity between the demands within each CES aggregate is given as an input. The aggregate outputs of the CES functions may then be considered as the final useful demands, with the standard exogenous Baseline projections and own-price elasticities provided for the aggregate demands.

A linearization of the CES demand function formulation has also been implemented, and is available in three different variants. In the lienearized formulation, the CES demand functions can be also subsequently nested further into higher-level CES functions.

All the generalizations presented in this Appendix have been implemented in TIMES v4.1.0. For now, the implementation should be still considered experimental, and therefore any feedback, comments and suggestions from TIMES users concerning the formulation and implementation are welcome.

In this Appendix we provide the input attributes and modeling details associated with the generalized Demand Functions in TIMES. As mentioned above, the implementation of the Demand Functions in TIMES is based on the corresponding formulations originally designed for the MARKAL model generator. The next three sections of the Appendix will address the Sets, Parameters, Variables, and Equations related to the Demand Function options, including the special volume-preserving CES option where the aggre­gate volume of the components of the combined demand remains equal to the (optionally weighted) sum of the component demands also under any substitution taking place.

## Mathematical formulation

For the own-price elasticities, we have the following relations (see Part I, Chapter 4), where $U_{i}$ is the term in the objective function associated with the utility change due to the demand variation of demand *i*:

$$DM_{i}/D{M_{i}}^{0} = (p_{i}/p_{i}^{0})^{E_{i}}$$ (2-10-1)

$$p_{i} = p_{i}^{0} \cdot (DM_{i}/D{M_{i}}^{0})^{1/E_{i}}$$ (2-10-2)

$$U_{i} = \sum_{t}^{}\left( \frac{p_{i}^{0}(t)}{(1 + 1/E_{i})} \cdot \left\lbrack DM_{i}^{0}(t) \right\rbrack^{- 1/E_{i}} \bullet DM_{i}(t)^{1 + 1/E_{i}} \right)$$ (2-10-3)

Consider then a utility function of the general CES form:

$$U_{k} = \left( \sum_{i}^{}{\alpha_{i}^{\frac{1}{\sigma}}x_{i}^{\frac{\sigma - 1}{\sigma}}} \right)^{\frac{\sigma}{\sigma - 1}}$$ (2-10-4)

where:

- $U_{k}$ is the total aggregate utility of demand *k*
- $x_{i}$ is the demand for commodity *i* (component of the aggregate demand)
- $α_{i}$ is a share parameter (the sum of which over *i* needs not be equal to 1)
- $σ$ is the elasticity of substitution (0 \< *σ* \< ∞)

The demand functions for $x_{i}$ can be derived from the utility function in terms of prices, and can be given by the formulas:

$$x_{i} = \frac{\alpha_{i}m}{p_{i}^{\sigma}}\left( \sum_{i}^{}{\alpha_{i}p_{i}^{1 - \sigma}} \right)^{- 1} = \frac{\alpha_{i}m}{p_{u}}\left( \frac{p_{u}}{p_{i}} \right)^{\sigma}$$ (2-10-5)

where *m* is the income level, and $p_{u}$ is the aggregate price, or unit cost, of the utility, can be given in terms of the individual prices $p{i}$ of the demands *i*:

$$p_{u} = \left( \sum_{i}^{}{\alpha_{i}p_{i}^{1 - \sigma}} \right)^{\frac{1}{1 - \sigma}}$$ (10-2-6)

The share parameters $α_{i}$ can be derived from the expenditure shares, as shown in Eq. {eq}`2-10-7` below. In the objective function, the utility change can then be calculated by the expression shown in Eq. {eq}`2-10-9` below.

$$\alpha_{i}^{k} = \frac{agg_{i}^{k}(t) \cdot DM_{i}^{0}(t)}{DM_{k}^{0}(t)} \cdot \left( \frac{p_{i}^{0}(t)}{agg_{i}^{k}(t) \cdot p_{u_{k}}^{0}(t)} \right)^{\sigma}$$ (2-10-7)

$$\beta_{k} = \left( \frac{p_{u_{k}}^{0}(t)}{1 + \frac{1}{E_{k}}} \right) \cdot \left( DM_{k}^{0}(t) \right)^{\frac{- 1}{E_{k}}}$$ (2-10-8)

$$U_{k} = \sum_{t}^{}\left( \beta_{k}(t) \cdot \left( \left( \left( \sum_{i}^{}{\left( \alpha_{i}^{k}(t) \right)^{\frac{1}{\sigma_{k}}} \cdot \left( agg_{i}^{k}(t) \cdot DM_{i}^{k}(t) \right)^{\frac{\sigma_{k} - 1}{\sigma_{k}}}} \right)^{\frac{\sigma_{k}}{\sigma_{k} - 1}} \right)^{1 + \frac{1}{E_{k}}} - \left( DM_{k}^{0}(t) \right)^{1 + \frac{1}{E_{k}}} \right) \right)$$ (2-10-9)

In the above, the coefficients $agg_{i}$ are represent user-defined aggregation coefficients for defining the aggregation from the component demands to the aggregate demands. The constant term corresponding to the Baseline value is subtracted in order to reproduce the value of the Baseline objective function when no variation occurs from the Baseline demands. The non-linear formulation of the elastic demand functions implemented in TIMES follows these expressions.

The corresponding linearized formulations are based on piece-wise linear functions which approximate the integrals over the inverse demand curves, as explained in Part I, Chapter 4. The method described there has been generalized to linearize also the somewhat more complex CES demand functions, allowing also for nested CES functions. Each demand having own-price or substitution elasticities requires the definition of as many variables as there are steps in the discrete representation of the demand curve (both upward and downward), for each period and region. Each such variable has an upper bound, and in the CES formulation they are included in an additional balance equation. However, otherwise the step variables are not involved in other new constraints. Therefore, the linear program is augmented by a number of variables, but does not have any notable number of more constraints than the initial inelastic LP. For partial equilibrium models, volume-preserving demand functions may, however, be preferred over standard CES formulations, and therefore an option for using a simple volume-preserving variant of the CES linearization has been also implemented.

The resulting linearization has been verified to work well over a large range of demand elasticities and price changes, and indeed also with nested CES functions. Cobb-Douglas functions (*σ* = 1) are also supported. Using the same linearization approach, even the simple Macro general equilibrium model, which is integrated in TIMES-Macro and includes Cobb-Douglas function nested into a CES production function, might be in principle linearized into an LP problem.

It is also important to note again here that, instead of maximizing the net total surplus, TIMES minimizes its negative (plus a constant). For this and other reasons, it is inappropriate to pay too much attention to the meaning of the *absolute* objective function values. Rather, examining the difference between the objective function values of two scenarios is a far more useful exercise. That difference is of course, the negative of the difference between the net total surpluses of the two scenario runs.

## Sets, Switches and Parameters

### Switches

Besides the basic data parameters described in {numref}`dem-input-parameters` below, the user controls whether the linear or non-linear formulation is activated by means of the switches shown in {numref}`dem-switches`. These switches are provided by the data handling system when the user indicates that the option is to be included in a run.

```{list-table} Switches
:name: dem-switches
:header-rows: 1

* - Switch
  - Parameter Description
* - \$SET TIMESED NO
  - Causes the Base Prices to be saved to a GDX file, for subsequent use in a policy analysis run based on any of the elastic demand options.
* - \$SET TIMESED YES
  - Activates any of LP formulations used for Demand Functions (exact formulations depending on input data)
* - \$SET MICRO YES
  - Activates any of NLP or mixed LP/NLP formulations used for Demand Functions (exact formulations depending on input data)
```

### Sets and Parameters

Like all other aspects of TIMES the user describes the demand functions for the energy system model by means of a Set and the Parameters and Switches described in this chapter. {numref}`dem-input-parameters` below describes the User Input Parameters associated with defining the TIMES demand functions.

```{list-table} Input parameters specific to demand functions.
:name: dem-input-parameters
:header-rows: 1

* - Parameter (Indexes)
  - Units & defaults
  - Parameter Description
* - COM_PROJ (r,y,c)
  - Commodity unit;
  <br>[0,∞)
  <br>default value:none
  <br>Default i/e: STD
  - Exogenous reference (Baseline) demand projection of commodity **c** in region **r** and year **y**.
  <br>In inelastic runs (Baseline runs, and any other model runs with non-elastic demands) the demands are met at the levels of the exogenous projections defined by COM_PROJ, usually exactly, but under certain circumstances some of them may also end up at a higher level than the projection.
* - COM_AGG (r,y,c,com)
  - Commodity units
  <br>[open];
  <br>default value:none
  <br>Default i/e: STD
  - Defines an aggregation of component demand **c** into an aggregate demand **com** in region **r** and year (period) **y**.
  <br>Defining COM_AGG between the component demands and the aggregate demand is required for modeling substitution elasticities.
  <br>If defined zero (e.g. by specifying IE=2), the values will be auto-generated according to the price ratios; defining the COM_AGG values zero is required for using the proper CES functions.
* - COM_VOC (r,y,c,bd)
  - Dimensionless;
  <br>[0,∞);
  <br>default value:none
  <br>Default i/e: STD
  - Defines the maximum demand variation in the lower / upper direction (**bd**=LO/UP) for demand **c** in region **r** and year **y**. The value gives the maximum deviation in proportion to the Baseline demand. Different values may be provided for each direction, thus demand elasticity curves may be asymmetric.
* - COM_STEP (r,c,bd)
  - Integer
  <br>[1,∞);
  <br>default value:none
  - Number of steps to use for the approximation of demand variation in the lower / upper direction (**bd**=LO/UP), and the associated change in producer/consumer surplus, for commodity **c** in region **r**, when using the elastic demand formulations. The shortcut **bd**=FX may be used for defining the same number of steps in both directions.
* - COM_ELAST (r,y,c,s,bd)
  - Dimensionless;
  <br>[open]
  <br>default value:none
  <br>Default i/e: STD
  - Elasticity of demand for commodity ***c***, indicating the following:
  <br>For own-price elasticities: how much the demand rises/falls in response to a unit change in the marginal cost of meeting a demand that is elastic.
  <br>For substitution elasticities: responsiveness of the ratio in which the component demands are used to the ratio of the prices of those demands
  <br>Defines elasticities for demand ***c*** in region ***r*** and year ***y***, timeslice ***s***
  <br>***lim*** = LO/UP : defines the own-price elasticity in the lower / upper direction in the linear formulation
  <br>***lim*** = FX (s=ANNUAL): defines own-price elasticities in the non-linear formulation; can also be used in the linear formulation for defining the own-price elasticities for the aggregate demands, optionally also for defining component-differentiated susbstution elasticities
  <br>***lim*** = N (s=ANNUAL): defines the substitution elasticity for component demands of the demand aggregation represented by commodity ***c***; positive values signify the standard variant, negative values signify the volume-preserving variant formulation
```

**Important remarks:**

- *COM_PROJ* should be explicitly defined by the user only for the component demands, and never for the aggregate demands.
- As mentioned in {numref}`dem-input-parameters`, the substitution elasticities can be defined by specifying *COM_ELAST*(r,t,com,ANNUAL,\'N\') for the aggregate demands. However, \'FX\' elasticities for the *component demands* can be optionally specified for defining component-differentiated substitution elasticities. Nonetheless, even when doing so, *COM_ELAST*(r,t,com, ANNUAL,\'N\') always defines the minimum substitution elasticity among the component demands of ***com***.
- Note that the aggregate demands are always at the ANNUAL level only, and thus only ANNUAL level own-price demand elasticities are supported for the demand aggregates.
- When using the non-linear formulation, demand substitution is supported only at the ANNUAL level for the component demands of the CES aggregates. The demand variations will thus be proportionally the same for all timeslices.
- Multi-level nested CES demand aggregations are also fully supported both in the non-linear and in the linearized case.
- Recursive CES demand aggregations are not supported, neither in the non-linear nor in the linearized case.
- The Cobb-Douglas case ($σ_{k}=1$) is also supported, but in the non-linear formulation it is handled by setting $σ_{k}$ very close to unity.

## Examples

Assume that we wish to define a non-linear CES demand function for the aggregate demand TLPKM (passenger land travel), having the following component demands:

- TRT -- passenger car travel
- TRB -- passenger bus travel
- TRW -- passenger two-wheeler travel
- TTP -- passenger rail travel

The demand function can be set up with the following input parameters (where **r** stands for regions, **t** for milestone years, and \'**0**\' for interpolation option placeholder):

```{list-table} Non-linear CES demand function example.
:name: dem-nl-ces-example
:header-rows: 1

* - Parameters
  - Description
* - COM_AGG(r,\'0\',\'TRT\',\'TLPKM\') = 2;
  - Aggregation of TRT into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRB\',\'TLPKM\') = 2;
  - Aggregation of TRB into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRW\',\'TLPKM\') = 2;
  - Aggregation of TRW into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TTP\',\'TLPKM\') = 2;
  - Aggregation of TTP into TPASS with price ratios
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'FX\')=0.35;
  - Own-price elasticity of aggregate demand
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'N\')=1.2;
  - Elasticity of substitution between components
* - COM_VOC(r,t,\'TLPKM\',\'UP\')=1;
  - Max. upper variance of aggregate demand
```

Assume now that we wish to define the same demand function but with the linear formulation for the CES function. The demand function can be set up with the following input parameters (where **r** stands for regions, **t** for milestone years, and **bd** for the inequality bound types (\'LO\', \'UP\')):

```{list-table} Linear CES demand function example.
:name: dem-linear-ces-example
:header-rows: 1

* - Parameters
  - Description
* - COM_AGG(r,\'0\',\'TRT\',\'TLPKM\') = 2;
  - Aggregation of TRT into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRB\',\'TLPKM\') = 2;
  - Aggregation of TRB into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRW\',\'TLPKM\') = 2;
  - Aggregation of TRW into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TTP\',\'TLPKM\') = 2;
  - Aggregation of TTP into TPASS with price ratios
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'FX\')=0.35;
  - Own-price elasticity of aggregate demand
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'N\')=1.2;
  - Elasticity of substitution between components
* - COM_STEP(r,\'TRT\',\'FX\')=100;
  - Number of steps for TRT in both directions
* - COM_STEP(r,\'TRB\',\'FX\')=100;
  - Number of steps for TRB in both directions
* - COM_STEP(r,\'TRW\',\'FX\')=100;
  - Number of steps for TRW in both directions
* - COM_STEP(r,\'TTP\',\'FX\')=100;
  - Number of steps for TTP in both directions
* - COM_STEP(r,\'TLPKM\',\'LO\')=120;
  - Number of steps for TLPKM in lower direction
* - COM_STEP(r,\'TLPKM\',\'UP\')=80;
  - Number of steps for TLPKM in upper direction
* - COM_VOC(r,t,\'TRT\',bd)=0.8;
  - Max. variance of TRT, given in both directions
* - COM_VOC(r,t,\'TRB\',bd)=0.8;
  - Max. variance of TRB, given in both directions
* - COM_VOC(r,t,\'TRW\',bd)=0.8;
  - Max. variance of TRW, given in both directions
* - COM_VOC(r,t,\'TTP\',bd)=0.8;
  - Max. variance of TTP, given in both directions
* - COM_VOC(r,t,\'TLPKM\',\'LO\')=0.5;
  - Max. lower variance of aggregate demand
* - COM_VOC(r,t,\'TLPKM\',\'UP\')=0.3;
  - Max. upper variance of aggregate demand
```

Note that using \'FX\' as a shortcut for bd={\'LO\',\'UP\'} in *COM_STEP* is only supported in TIMES v4.4.0 and above, and that *COM_VOC* does not have any such shortcut.

## Variables

The variables that are used to model the Demand Functions in TIMES are presented in {numref}`dem-variables` below. The primary role of the variables and equations used to model the functions is to control the standard TIMES variable and the associated dynamic cost of these.

```{list-table} Model variables employed in demand functions.
:name: dem-variables
:header-rows: 1

* - Variable (Indexes)
  - Variable Description
* - VAR_COMPRD (r,t,c,s)
  - Variable used for tracking the Gross production of a commodity **c** in region **r**, period **t**, and timeslice **s**.
* - VAR_DEM (r,t,c)
  - Variable used for the enodenous (elastic) demand for commodity **c** in region **r**, and period **t**, when the demand function is non-linear.
* - VAR_ELAST (r,t,c,s,bd)
  - Step variables used to linearize elastic demand curves for demand **c** in region **r**, period **t**, and timeslice **s**. The index **bd**=LO corresponds to the direction of decreasing the demand, while **bd**=UP denotes the direction for demand increase.
* - VAR_OBJELS (r,bd,cur)
  - Variable used for accounting the total discounted endogenous losses (**bd**=LO) or gains (**bd**=UP) in the utility of region **r** in currency **cur** through the demand variations of all elastic demands.
```

### VAR_COMPRD(r,t,c,s)

**Description:** The amount of demand commodity **c** procured at time period **t**, timeslice **s**.

**Purpose and** This variable tracks the total amount of demand commodity produced.

**Occurrence:** This variable is normally only created if a bound is imposed on total production of the demand commodity, or a cost is explicitly associated with the production level of the demand. However, when defining CES demand functions, the variable is always created both for the component demand and for the aggregate demand. The variable is defined through the equations EQE_COMPRD and/or EQ(l)\_COMBAL.

**Units:** PJ, Bvkm, or any other unit defined by the analyst to represent the quantity of the demand.

**Bounds:** This variable is non-negative. It is by default not otherwise directly bounded. It can be directly bounded by the COM_BNDPRD attribute. It may be indirectly bounded by specifying a user constraint referring to it by UC_COMPRD.

### VAR_DEM

**Description:** The total amount of demand for commodity **c** in time period **t**.

**Purpose:** This variable is used for tracking the endogenous amount of demand for commodity **c** in the non-linear formulation of elastic demands.

**Occurrence:** This variable is not created in the LP formulation. It is only created in the non-linear formulation of demand functions based on own-price and/or substitution elasticities (as well as in the Macro formulation). It is generated for each demand with a non-linear own-price elasticity function, and for all demands associated with a non-linear CES demand function.

**Units:** PJ, Bvkm, or any other unit in which demands are tracked.

**Bounds:** This variable is non-negative and is not bounded upwards.

### VAR_ELAST (r,t,c,s,j,bd)

**Description:** Variables used to linearize elastic demand curves by step-wise variations.

**Purpose:** To indicate how far the demand variation extends on the elasticity curve, by step.

**Occurrence:** Each elastic demand is expressed as the sum of these variables. In the objective function, these variables are used to bear the cost of demand losses and revenues of demand gains as explained in Part I, Chapter 4.

These variables are defined whenever a demand is declared to be price elastic, either to its own price or through cross-elastic substitution. These variables are indexed by j, where j runs over the number of steps used for discretizing the demand curve of demand commodity c. The jth variable stands for the portion of the demand that lies within discretization interval **j**, on side **bd** (**bd** indicates either increase or decrease of demand w.r.t. the reference case demand). In the objective function, these variables are used to represent the utility change caused by demand losses or gains, as explained in Part I, Chapter 4.

**Units:** Demand units: PJ, Bvkm, or any other unit in which the demand is tracked.

**Bounds:** This variable is non-negative. Each ELAST variable is bounded upward via virtual equation EQ_BNDELAS, of in the case of a CES function, via the equation EQL_COMCES.

### VAR_OBJELS (r,bd,cur)

**Description:** Variables used to linearize elastic demand curves by step-wise variations.

**Purpose:** To indicate how far the demand variation extends on the elasticity curve.

**Occurrence:** The utility change caused by all demand losses and gains as explained in Part I, Chapter 4.

These variables are defined whenever any of the elastic demand formulations is used. These variables are indexed by **bd** (**bd** indicates either increase or decrease of demand w.r.t. the reference case demand). These variables are included in the objective function, to represent the total utility changes caused by demand losses or gains, as explained in Part I, Chapter 4.

**Units:** Demand units: PJ, Bvkm, or any other unit in which the demand is tracked.

**Bounds:** This variable is non-negative.

## Equations

The equations that are used to model the demand functions in TIMES are presented in {numref}`dem-constraints` below. The primary role of the variables and equations used to model Demand Functions is to control the standard TIMES demand variables VAR_DEM and the associated losses or gains in consumer\'s utility in the regional demand utility part of the objective function (EQ_OBJELS).

:::{admonition} Reminder

The elastic demand function formulations are activated at run time from the data handling system. The linear formulation is activated by the switch `$SET TIMESED YES` and the non-linear formulation by the switch `$SET MICRO YES`.
:::

```{list-table} Model constraints specific to demand functions
:name: dem-constraints
:header-rows: 1

* - Constraints (Indexes)
  - Constraint Description
  - GAMS Ref
* - EQG_COMBAL (r,t,c,s)
  - The commodity balance constraint associated with the demand function of commodity c, as an inequality. The constraint requires that the total production of the demand commodity is greater than or equal to the endogenous elastic demand. This constraint is normally generated for all demands modeled with own-price elasticities.
  - EQCOMBAL.mod
* - EQE_COMBAL (r,t,c,s)
  - The commodity balance constraint associated with the demand function of commodity c, as a strict equality. This constraint is automatically generated for the component demands of all CES demand functions, i.e. demands modeled with substitution elasticities.
  - EQCOMBAL.mod
* - EQE_COMPRD (r,t,c,s)
  - This equation is a strict equality and is generated in two forms for the demands included in demand functions:
  <br>1. Defining equation for the commodity production of commodity c. This constraint is automatically generated for all the component demands of CES demand functions.
  <br>2. Balance equation for the total variation of the component demands of the aggregate demands of CES demand functions. This constraint is automatically generated for all the aggregate demands of CES demand functions.
  - EQCOMBAL.mod
* - EQL_COMCES (r, t,com,c,s)
  - The constraint bounding the step variables of a demand commodity **c** included as a component in the CES function of demand aggregate **com**. The constraint is generated for each of the component demands whenever the aggregate demand of a CES function has been modeled with an own-price elasticity (otherwise variable bounds are sufficient).
  - EQOBJELS.mod
* - EQ_OBJELS (r,bd,cur)
  - The calculation of the endogenous losses or gains in utility through the demand variations of all elastic demands are discounted and summed together into the VAR_OBJELS variable representing the regional elastic demand cost part of the objective function, which is subsequently included in the total objective function (EQ_OBJ).
  - EQOBJELS.mod
```
