# Variables

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

## VAR_COMPRD(r,t,c,s)

**Description:** The amount of demand commodity **c** procured at time period **t**, timeslice **s**.

**Purpose and** This variable tracks the total amount of demand commodity produced.

**Occurrence:** This variable is normally only created if a bound is imposed on total production of the demand commodity, or a cost is explicitly associated with the production level of the demand. However, when defining CES demand functions, the variable is always created both for the component demand and for the aggregate demand. The variable is defined through the equations EQE_COMPRD and/or EQ(l)\_COMBAL.

**Units:** PJ, Bvkm, or any other unit defined by the analyst to represent the quantity of the demand.

**Bounds:** This variable is non-negative. It is by default not otherwise directly bounded. It can be directly bounded by the COM_BNDPRD attribute. It may be indirectly bounded by specifying a user constraint referring to it by UC_COMPRD.

## VAR_DEM

**Description:** The total amount of demand for commodity **c** in time period **t**.

**Purpose:** This variable is used for tracking the endogenous amount of demand for commodity **c** in the non-linear formulation of elastic demands.

**Occurrence:** This variable is not created in the LP formulation. It is only created in the non-linear formulation of demand functions based on own-price and/or substitution elasticities (as well as in the Macro formulation). It is generated for each demand with a non-linear own-price elasticity function, and for all demands associated with a non-linear CES demand function.

**Units:** PJ, Bvkm, or any other unit in which demands are tracked.

**Bounds:** This variable is non-negative and is not bounded upwards.

## VAR_ELAST (r,t,c,s,j,bd)

**Description:** Variables used to linearize elastic demand curves by step-wise variations.

**Purpose:** To indicate how far the demand variation extends on the elasticity curve, by step.

**Occurrence:** Each elastic demand is expressed as the sum of these variables. In the objective function, these variables are used to bear the cost of demand losses and revenues of demand gains as explained in Part I, Chapter 4.

These variables are defined whenever a demand is declared to be price elastic, either to its own price or through cross-elastic substitution. These variables are indexed by j, where j runs over the number of steps used for discretizing the demand curve of demand commodity c. The jth variable stands for the portion of the demand that lies within discretization interval **j**, on side **bd** (**bd** indicates either increase or decrease of demand w.r.t. the reference case demand). In the objective function, these variables are used to represent the utility change caused by demand losses or gains, as explained in Part I, Chapter 4.

**Units:** Demand units: PJ, Bvkm, or any other unit in which the demand is tracked.

**Bounds:** This variable is non-negative. Each ELAST variable is bounded upward via virtual equation EQ_BNDELAS, of in the case of a CES function, via the equation EQL_COMCES.

## VAR_OBJELS (r,bd,cur)

**Description:** Variables used to linearize elastic demand curves by step-wise variations.

**Purpose:** To indicate how far the demand variation extends on the elasticity curve.

**Occurrence:** The utility change caused by all demand losses and gains as explained in Part I, Chapter 4.

These variables are defined whenever any of the elastic demand formulations is used. These variables are indexed by **bd** (**bd** indicates either increase or decrease of demand w.r.t. the reference case demand). These variables are included in the objective function, to represent the total utility changes caused by demand losses or gains, as explained in Part I, Chapter 4.

**Units:** Demand units: PJ, Bvkm, or any other unit in which the demand is tracked.

**Bounds:** This variable is non-negative.
