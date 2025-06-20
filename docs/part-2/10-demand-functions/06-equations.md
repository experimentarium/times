# Equations

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
