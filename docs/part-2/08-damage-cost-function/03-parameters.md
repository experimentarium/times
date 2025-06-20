(b-switches-and-parameters)=
# Switches and Parameters

## Activating the Damage Cost Functions

Like all other aspects of TIMES, the user describes the Damage Cost Functions by means of a Set and the Parameters and Switches described in this chapter.

As discussed in Section {numref}`%s <b-mathematical-formulations>`, the TIMES Damage Cost Function facility permits the assessment of environmental externalities by means of two approaches to determine the impact or cost of damages arising from emissions: ex-post calculation and internalized damage costs. The second approach can be further divided into the non-linear and linear formulations, and therefore the following three approaches are available in Standard TIMES:

1. The environmental damages are computed ex-post, without feedback into the optimization process;
2. The environmental damages are a linearized part of the objective function and therefore taken into account in the optimization process;
3. The environmental damages are a non-linear part of the objective function and therefore taken into account in the optimization process.

The user can control whether or not the damage costs are activated in the objective function by means of the switch `$SET DAMAGE LP`/`NLP`/`NO`. This switch is provided by the data handling system according to how the user wishes the option to be included:

```
$SET DAMAGE LP
$SET DAMAGE NLP
$SET DAMAGE NO
```

The setting `$SET DAMAGE LP` is the default, and activates the linearized formulation of damage costs, with the costs included in the objective function. The setting `$SET DAMAGE NLP` activates the non-linear damage cost option, with the costs included in the objective function. The setting `$SET DAMAGE NO` causes the damage costs only to be computed ex-post, without feedback into the optimization process.

Note that owing to the non-linear nature of the modified objective function that endogenizes the damages, the NLP damage option requires non-linear solution methods that can lead to much larger resource utilization compared to LP models. In addition, the options with an augmented objective function cannot be currently activated with the non-linear TIMES-MACRO model variant. However, the linear option LP can be used together with the decomposed MACRO_MSA option.

## Input parameters

All the parameters for describing damage functions are available in the VEDA-FE shell, where they may be specified. All parameters have a prefix \'DAM\_\' in the GAMS code of the model generator. The parameters are discussed in more detail below:
1. The parameter **DAM_COST** is used to specify the marginal damage cost at the reference level of emissions. The parameter has a year index, which can be utilized also for turning damage accounting on/off for an emission in a period (by specifying an EPS value for the cost). **DAM_COST** is interpolated/extrapolated by default, but unlike other cost parameters, the interpolation is sparse, and the costs are assumed to be constant within each period.
2. The parameter **DAM_BQTY** is used to specify the reference level of emissions. If not specified or set to zero, the marginal damage costs will be assumed constant, and no emission steps are used.
3. The parameter **DAM_ELAST** is used to specify the elasticity of marginal damage costs to emissions in the lower and upper direction. If specified in one direction only, the elasticity is assumed in both directions. If neither is specified, the marginal damage costs will be constant in both directions.
4. The parameter **DAM_STEP** can be used for specifying the number of emission steps below and above the reference level of emissions. The last step above the reference level will always have an infinite bound. If the number of steps is not provided in either direction, but the elasticity is, one step is assumed in that direction. If a non-zero **DAM_STEP**(r,c,\'N\') is specified, the damage costs for commodity **c** in region **r** are not included in the objective. If the NLP formulation is used (DAMAGE=NLP), all **DAM_STEP** parameters will be ignored.
5. The parameter **DAM_VOC** can be used for specifying the variation in emissions covered by the emission steps, both in the lower an upper direction. The variation in the lower direction should be less than or equal to the reference level of emissions. If the lower variation is smaller than **DAM_BQTY**, the damage costs are zero for emissions below the difference. The lower variance can thus be used for defining a threshold level for the damage costs. If **DAM_VOC** is not specified in the lower direction, it is assumed to be equal to **DAM_BQTY**. If **DAM_VOC** is not specified in the upper direction, the emission step size in the upper direction is assumed to be equal to that in the lower direction. The limtype 'N' can be used for defining step sizes in proportion to the reference level. If the NLP formulation is used (DAMAGE\=\=NLP), any **DAM_VOC** parameters specified in the upper direction will be ignored.  However, even in the NLP formulation the lower **DAM_VOC** can be used for defining a threshold emission level for the costs.

The input parameters are listed in {numref}`dam-input-parameters`. 

```{list-table} Input parameters for the TIMES Damage Cost Functions.
:name: dam-input-parameters
:header-rows: 1

* - Input parameter(Indexes)[^48]
  - Related parameters[^49]
  - Units / Ranges & Default values & Default inter-/extrapolation[^50]
  - Instances[^51] (Required / Omit / Special conditions)
  - Description
  - Affected equations or variables[^52] |
* - DAM_COST (r,datayear,c,cur)
  - DAM_BQTY, DAM_ELAST, DAM_STEP, DAM_VOC
  - TIMES cost unit
  <br>[0,INF); default value: none
  <br>Default i/e[^53]: standard
  - Required for each commodity for which damage costs are to be accounted.
  - Marginal damage cost of emission c at reference emission level.
  - EQ_OBJDAM
* - DAM_BQTY (r,c)
  - See above
  - TIMES emission unit
  <br>[0,INF); default value: 0
  - Only taken into account if DAM_COST has been specified
  - Reference level of emissions c
  - EQ_DAMAGE
  <br>EQ_OBJDAM
* - DAM_ELAST (r,c,bd)
  - See above
  - Dimensionless
  <br>[0,INF); default value: 0
  - Only taken into account if DAM_COST has been specified
  - Elasticity of marginal damage cost to emissions on the lower and upper side of the reference level
  - EQ_OBJDAM
* - DAM_STEP(r,c,bd)
  - See above
  - Dimensionless
  <br>[0,INF), integer; default value: 0
  - Only taken into account if DAM_COST is specified. Non-zero \'N\' value excludes costs from the objective.
  - Number of emission steps for the linearized cost function in the lower/upper direction. Can also be used for excluding the costs from the objective.
  - EQ_DAMAGE
  <br>EQ_OBJDAM
* - DAM_VOC(r,c,lim)
  - See above
  - TIMES emission unit
  <br>(0,INF); ≤ DAM_BQTY; default value: DAM_BQTY
  - Only taken into account if DAM_COST has been specified
  - Variation in emissions covered by the emission steps in the lower/upper direction. A threshold emission level can be defined with bd=\'LO\', and proportional variation can be defined with lim=\'N\'.
  - EQ_DAMAGE
  <br>EQ_OBJDAM
```

## Reporting parameters

There is only one reporting parameter specifically related to the Damage Cost functions. The parameter represents the undiscounted damage costs by region, period and emission commodity. The parameter has two flavours; the first one is for standard TIMES and the second one for stochastic TIMES:

- **CST_DAM(r,t,c)**: Annual damage costs from emission **c** in region **r**,
- **SCST_DAM(w,r,t,c)**: Annual damage costs from emission **c** in region **r** and stochastic scenario **w**.

However, in addition the standard reporting parameters REG_WOBJ, and REG_ACOST are augmented with damage costs results, using the label \'DAM\'/\'DAM-EXT\' to distinguish damage costs from other cost components.

These parameters are included in the .vdd files that describe the parameters to be transferred to VEDA-BE under standard TIMES and stochastic TIMES. Therefore, the corresponding result parameter is always available in VEDA-BE whenever Damage Cost functions have been defined, even with the setting DAMAGE=NO.

The damage costs are always reported by using the accurate non-linear expressions, even if the linearized formulation is chosen for the augmented objective function.

```{list-table} Reporting parameters for the TIMES Damage cost functions.
:name: dam-reporting-parameters
:header-rows: 1

* - Parameter
  - Description
* - CST_DAM (r,t,c)
  - Damage costs by region, period and emission(standard TIMES)
* - SCST_DAM (w,r,t,c)
  - Damage costs by region, period and emission (stochastic TIMES)
```

[^48]: The first row contains the parameter name, the second row contains in brackets the index domain over which the parameter is defined.

[^49]: This column mentions related input parameters or sets being used in the context of the headword parameter.

[^50]: This column lists the unit of the parameter, the possible range of its numeric value \[in square brackets\] and the inter-/extrapolation rules that apply.

[^51]: An indication of circumstances for which the parameter is to be provided or omitted.

[^52]: Equations or variables that are directly affected by the parameter.

[^53]: Abbreviation i/e = inter-/extrapolation
