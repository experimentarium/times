# Damage Cost Functions

## Introduction

This Appendix contains the documentation on the Damage Cost Function extensions for the TIMES model. The chapter contains 6 sections: section 2 contains the mathematical formulation, section 3 describes the parameters for the Damage Cost Functions, and section 4 gives two examples. Finally, section 5 describes the variables and section 6 describes the equations.

The Damage Cost Function option of TIMES is intended for modelers who wish to evaluate the environmental externalities caused by an energy system. For instance, emissions of toxic or environmentally harmful pollutants from the energy system create social costs linked to impacts of the pollution on human health and the environment. In another example, in global studies of GHG emissions, it may be of interest to evaluate the impact of GHG emissions on concentrations and ultimately on damages created by climate change induced by increased concentration of GHGs.

Until recently, in most studies involving bottom-up models, emission externalities have been modeled in one of two ways: either by introducing an emission tax, or by imposing emission caps. In the first case, the tax is (ideally) supposed to represent the external cost created by one unit of emission. However, using a tax assumes that the cost is a linear function of emissions. In the second approach, it is assumed that such a cost is unknown but that exogenous studies (or regulations, treaties, etc.) have defined a level of acceptable emissions that should not be exceeded. However, using this approach is akin to making the implicit assumption that emissions in excess of the cap have an infinite external cost. Both of these approaches have merit and have been successfully applied to many energy system model studies.

It is however possible to extend these two approaches by introducing an option to better model the cost of damages created by emissions. The damage function option discussed in this document extends the concept of an emission tax by modeling more accurately the assumed cost of damages due to emissions of a pollutant.

## Mathematical formulation

We now describe the mathematical formulation used for the damage cost functions.

With respect to optimization, two distinct approaches to account for damage costs can be distinguished:

1. Environmental damages are computed ex-post, without feedback into the optimization process, and
2. Environmental damages are part of the objective function and therefore taken into account in the optimization process.

In both approaches, a number of assumptions are made:

- Emissions in each region may be assumed to cause damage only in the same region or, due to trans-boundary pollution, also in other regions; however, all damage costs are allocated to the polluters in the source region, in accordance with the Polluter Pays Principle, or Extended Polluter Responsibility; 
- Damages in a given time period are linked to emissions in that same period only (damages are not delayed, nor are they cumulative); and 
- Damages due to several pollutants are the sum of damages due to each pollutant (no cross impacts).

In a given time period, and for a given pollutant, the damage cost is modeled as follows:

$$DAM(EM) = \alpha \cdot EM^{\beta + 1}$$ (1)

where:

- EM is the emission in the current period;
- DAM is the damage cost in the current period;
- *β* ≥ 0 is the elasticity of marginal damage cost to amount of emissions; and
- *α* \> 0 is a calibrating parameter, which may be obtained from dose-response studies that allow the computation of the marginal damage cost per unit of emission at some reference level of emissions.

If we denote the marginal cost at the reference level $MC_{0}$, the following holds:

$$MC_{0} = \alpha \cdot (\beta + 1) \cdot EM_{0}^{\beta}$$ (2)

where EM_ 0 is the reference amount of emissions. Therefore expression (1) may be re-written as:

$$DAM(EM) = MC_{0} \cdot \frac{EM^{\beta + 1}}{(\beta + 1) \cdot EM_{0}^{\beta}}$$ (3)

The marginal damage cost is therefore given by the following expression:

$$MC(EM) = MC_{0} \cdot \frac{EM^{\beta}}{EM_{0}^{\beta}}$$ (4)

The approach to damage costs described in this section applies more particularly to local pollutants. Extension to global emissions such GHG emissions requires the use of a global TIMES model and a reinterpretation of the equations discussed above.

The modeling of damage costs via equation (3) introduces a non-linear term in the objective function if the ***β*** parameter is strictly larger than zero. This in turn requires that the model be solved via a Non-Linear Programming (NLP) algorithm rather than a LP algorithm. However, the resulting Non-Linear Program remains convex as long as the elasticity parameter is equal to or larger than zero. For additional details on convex programming, see Nemhauser et al (1989). If linearity is desired (for instance if problem instances are very large), we can approximate expression (3) by a sequence of linear segments with increasing slopes, and thus obtain a Linear Program.

The linearization can be done by choosing a suitable range of emissions, and dividing that range into *m* intervals below the reference level, and *n* intervals above the reference level. We also assume a middle interval centered at the reference emission level. To each interval corresponds one step variable *S*. Thus, we have for emissions:

$$EM = \sum_{i = 1}^{m}S_{i}^{lo} + S^{mid} + \sum_{i = 1}^{n}S_{i}^{up}$$ (5)

The damage cost can then be written as follows:

$$DAM(EM) = \sum_{i = 1}^{m}{MC_{i}^{lo} \cdot S_{i}^{lo}} + MC_{0} \cdot S^{mid} + \sum_{i = 1}^{n}{MC_{i}^{up} \cdot S_{i}^{up}}$$ (6)

where:

- $MC_{i}^{lo}\text{and}MC_{i}^{up}$are the approximate marginal costs at each step below and above the reference level as shown in (105) below; and 
- $S_{i}^{lo},S^{mid}\text{and}S_{i}^{up}$are the non-negative step variables for emissions. Apart from the final step, each step variable has an upper bound equal to the width of the interval. In this formulation we choose intervals of uniform width on each side of the reference level. However, the intervals below and above the reference level can have different sizes. The width of the middle interval is always the average of the widths below and above the reference level.

The approximate marginal costs at each step can be assumed to be the marginal costs at the center of each step. If all the steps intervals are of equal size, the marginal costs for the steps below the reference level are obtained by the following formula:

$$MC_{i}^{lo} = MC_{0} \cdot \left( \frac{(i - 0.5)}{(m + 0.5)} \right)^{\beta}$$ (7)

Formulas for the marginal costs of the other steps can be derived similarly.

The TIMES implementation basically follows the equations shown above. Both the non-linear and linearized approaches can be used. However, in order to provide some additional flexibility, the implementation supports also defining a threshold level of emissions, below which the damage costs are zero. This refinement can be taken into account in the balance equation (5) by adding one additional step variable having an upper bound equal to the threshold level, and by adjusting the widths of the other steps accordingly. The threshold level can also easily be taken into account in the formulas for the approximate marginal costs.

In addition, the implementation supports different elasticities and step sizes to be used below and above the reference level. See Section 3 for more details.

## Switches and Parameters

### Activating the Damage Cost Functions

Like all other aspects of TIMES, the user describes the Damage Cost Functions by means of a Set and the Parameters and Switches described in this chapter.

As discussed in Section 2, the TIMES Damage Cost Function facility permits the assessment of environmental externalities by means of two approaches to determine the impact or cost of damages arising from emissions: ex-post calculation and internalized damage costs. The second approach can be further divided into the non-linear and linear formulations, and therefore the following three approaches are available in Standard TIMES:

1. The environmental damages are computed ex-post, without feedback into the optimization process;
2. The environmental damages are a linearized part of the objective function and therefore taken into account in the optimization process;
3. The environmental damages are a non-linear part of the objective function and therefore taken into account in the optimization process.

The user can control whether or not the damage costs are activated in the objective function by means of the switch \$SET DAMAGE LP/NLP/NO. This switch is provided by the data handling system according to how the user wishes the option to be included:

> \$SET DAMAGE LP
>
> \$SET DAMAGE NLP
>
> \$SET DAMAGE NO

The setting \$SET DAMAGE LP is the default, and activates the linearized formulation of damage costs, with the costs included in the objective function. The setting \$SET DAMAGE NLP activates the non-linear damage cost option, with the costs included in the objective function. The setting \$SET DAMAGE NO causes the damage costs only to be computed ex-post, without feedback into the optimization process.

Note that owing to the non-linear nature of the modified objective function that endogenizes the damages, the NLP damage option requires non-linear solution methods that can lead to much larger resource utilization compared to LP models. In addition, the options with an augmented objective function cannot be currently activated with the non-linear TIMES-MACRO model variant. However, the linear option LP can be used together with the decomposed MACRO_MSA option.

### Input parameters

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
* - DAM_VOC(r,c,bd)
  - See above
  - TIMES emission unit
  <br>(0,INF); ≤ DAM_BQTY; default value: DAM_BQTY
  - Only taken into account if DAM_COST has been specified
  - Variation in emissions covered by the emission steps in the lower/upper direction. A threshold emission level can be defined with bd=\'LO\', and proportional variation can be defined with lim=\'N\'.
  - EQ_DAMAGE
  <br>EQ_OBJDAM
```

### Reporting parameters

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

## Examples

Assume that we wish to define linearized damage costs for the emission commodity \'EM\' so that the cost function has the following properties:

- The reference level of emissions is 80 units;
- The marginal cost at the reference level are 10 cost units per emission unit;
- The cost elasticity is 1 in the lower direction, and 0.7 in the upper direction;

The damage function can be specified with the following parameters:

PARAMETER DAM_COST / REG.2000.EM.CUR 10 /;

PARAMETER DAM_BQTY / REG.EM 80 /;

PARAMETER DAM_ELAST / REG.EM.LO 1, REG.EM.UP 0.7 /;

 ```{figure} assets/linearized-damage-function.svg
:name: example-linearized-function-111
:align: center

Example of a linearized damage function with 1+1+1 steps (1 lower step, 1 middle step, 1 upper step).
```

As we did not specify the number of steps, but we did specify the elasticities in both directions, the number of steps is assumed to be 1 in both directions. The resulting damage cost function is illustrated in {numref}`example-linearized-function-111`. Because the damage function has a very coarse representation, the total costs have notable deviations from the accurate non-linear function. Note that the step size has been automatically determined to be **DAM_BQTY/(DAM_STEP+0.5)** = 80/1.5. However, the last step has no upper bound.

Assume next that we would like to refine the damage function by the following specifications:

- We want to have 5 steps below the reference, and 3 steps above it;
- The threshold level of damage costs is 20 units of emissions;
- The steps above the reference level should cover 100 units of emissions.

The damage function can be specified with the following parameters

PARAMETER DAM_COST / REG.2000.EM.CUR 10 /;

PARAMETER DAM_BQTY / REG.EM 80 /;

PARAMETER DAM_ELAST / REG.EM.LO 1, REG.EM.UP 0.7 /;

PARAMETER DAM_STEP / REG.EM.LO 5, REG.EM.UP 3 /;

PARAMETER DAM_VOC / REG.EM.LO 60, REG.EM.UP 100 /;

The resulting damage cost function is illustrated in {numref}`example-linearized-function-1513`. The cost function follows now very closely the accurate non-linear function. Note that the step sizes derived from the VOC specifications are 10 units for the lower steps, 20 for the middle step, and 30 units for the upper steps. However, the last step of course has no upper bound.

 ```{figure} assets/linearized-damage-function-2.svg
:name: example-linearized-function-1513
:align: center
Example of a linearized damage function with 1+5+1+3 steps (one zero cost step, 5 lower steps, one middle step, 3 upper steps).
```

## Variables

There are only two sets of new variables in the damage cost formulation, VAR_DAM and VAR_OBJDAM, which are shown below in {numref}`dam-variables`. The variables VAR_DAM represent the steps in the emissions in each period. In the linearized formulation, there are DAM_STEP(\...,\'LO\') number of step variables on the lower side and DAM_STEP(\...\'UP\') number of step variables on the higher side of emissions. In addition, one step variable of type \'FX\' corresponds to the middle step that includes the reference level of emissions, and an optional additional step variable of type \'FX\' corresponds to the zero-damage fraction of emissions, as defined by the difference between DAM_BQTY(..) and DAM_VOC(\...,\'LO\').

The variables VAR_OBJDAM represent the total discounted damage costs by region. The undiscounted costs in each period described in Section 2 are discounted and summed over all periods and emissions in each region. As emissions are in TIMES assumed to be constant within each period, damage costs are likewise assumed to be constant within each period.

```{list-table} Model variables specific to the Damage Cost Functions.
:name: dam-variables
:header-rows: 1

* - Variable (Indexes)
  - Variable Description
* - VAR_DAM (r,t,c,bd,j)
  - The emission step variable for the damage function of commodity **c** in region **r**, for each step **j** in each direction **bd**.
* - VAR_OBJ (r,\'OBJDAM\',cur)
  - The variable is equal to the sum of the total discounted damage costs in each region **r** with currency **cur**.
```

### VAR_DAMAGE(r,t,c,bd,j)

**Description:** The amount of emission indicator **c** at cost step **j** in direction **bd**, in period **t**.

**Purpose:** This variable tracks the amount of an emission indicator by cost step and period, in both the lower and upper direction from the reference level.

**Occurrence:** The variable is generated for emission indicator that has damage costs specified, whenever the damage cost functions are included in the objective function.

**Units:** Units of the emission commodity **c**.

**Bounds:** This variable cannot be directly bounded by the user.

### VAR_OBJ(r,\'OBJDAM\',cur)

**Description:** The total present value of damage costs by region.

**Purpose:** This variable is included in the objective function in order to include damage costs in the objective when requested by the user.

**Occurrence:** This variable is generated for each region when damage cost functions are included in the objective function

**Units:** Currency units used for damage functions.

**Bounds:** This variable cannot be directly bounded by the user.

## Equations

There are two blocks of equations generated for damage cost functions, whenever they are included in the objective function. The two equations related to the damage functions are listed and briefly described below in {numref}`dam-constraints`. The equations include the balance of stepped emissions, the objective component for damage costs, and the augmented total objective function.

In addition, the standard TIMES objective function, **EQ_OBJ**, is augmented by the present value of the damage costs, as defined by the equation EQ_OBJDAM.

We now give the formulations of these constraints.

:::{admonition} Reminder
The Damage Cost Functions are activated at run time from the data handling system, which in turn sets the switch $SET DAMAGE LP/NLP/NO.
:::

```{list-table} Constraints specific to damage costs (in the GAMS file eqdamage.mod).
:name: dam-constraints
:header-rows: 1

* - Constraints (Indexes)
  - Constraint Description
* - EQ_DAMAGE (r,t,c)
  - The balance equation between the stepped emission variables and the total emissions in each period.
* - EQ_OBJDAM (r,cur) 
  - The total discounted damage costs by region, which will be added as a component to the objective function.
```

### EQ_DAMAGE(r,t,c)

**Description:** Allocates the total amount of emission indicator in period **t** to cost steps.

**Purpose:** This constraint allocates the total amount of emission indicator c to the cost steps of the linearized / non-linear damage cost functions in each period ***t***.

> This equation is generated in each time period for all emission indicators considered.

**Units:** Units of the emission commodity **c**.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Remarks**:

- The damage costs can be defined either on the net production (VAR_COMNET) or the gross production (VAR_COMPRD) of the commodity c. By default the damage costs are applied to the NET amount, unless $DAM_ELAST_{ r,c,\'N\'}$ is also specified. $DAM_ELAST_{r,c,\'N\'}$ defines a multiplier for the Base prices to be added to the damage cost function, when it is to be applied to the gross production.
- The internal parameter $DAM_COEF_{r,t,c,s}$ is set to the base prices, if $DAM_ELAST_{r,c,\'N\'}$ is specified, and otherwise to 1.

**Equation:**

$$EQ\_ DAMAGE_{r,t,c} \ni \left( \mathbf{rt}\mathbf{c}_{r,t,c} \land \exists(cur):DAM\_ COST_{r,t,c,cur} \right)$$

$${\sum_{(jj,bd) \in \mathbf{dam}\_\mathbf{nu}\mathbf{m}_{r,c,jj,bd}}^{}{\sum_{j \leq jj}^{}{VAR\_ DAM_{r,t,c,bd,j}}}
} \\ \\ {\left\{ = \right\}
} \\ \\ {\sum_{\mathbf{com}\_\mathbf{t}\mathbf{s}_{\mathbf{r},\mathbf{c},\mathbf{ts}}}^{}\left( \begin{aligned}
 & DAM\_ COEF_{r,t,c,ts} \times \\
 & \left( \begin{aligned}
 & VAR\_ COMNET_{r,t,c,ts}if\mspace{6mu} DAM\_ ELAST_{r,c,'N'}\mspace{6mu} not\mspace{6mu} given \\
 & VAR\_ COMPRD_{r,t,c,ts}otherwise
\end{aligned} \right)
\end{aligned} \right)}$$

### EQ_OBJDAM(r,cur)

**Description:** Computes the present value of all damage costs by region and currency.

**Purpose:** Defines the variable VAR_OBJ(r,\'OBJDAM\',cur), which represents the total present value of all damage costs in region r, having currency cur. This variable is included in the TIMES objective function.

**Units:** Currency units.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Remarks:**

- The internal parameter $DAM_SIZE_{r,c,bd}$ represents the sizes of cost steps of the dlinearized damage cost function, for both directions (bd=LO/UP) and for the middle step (bd=FX), as described above in Section 2.

**Equation:**

$$EQ\_ OBJDAM_{r,cur} \ni \left( \mathbf{rdcu}\mathbf{r}_{\mathbf{r},\mathbf{cur}} \right)$$

**Case A: Linearized functions**

$${\sum_{(t,c) \in \left\{ \mathbf{rt}\mathbf{c}_{\mathbf{r},\mathbf{t},\mathbf{c}}|(DAM\_ COST_{r,t,} > 0) \right\}}^{}{DAM\_ COST_{r,t,c,cur} \times OBJ\_ PVT_{r,t,cur}} \times 
} \\ \\ {\left\lbrack \begin{aligned}
 & \sum_{\begin{matrix}
jj \in \mathbf{dam}\_\mathbf{nu}\mathbf{m}_{r,c,jj,'LO'} \\
j \leq jj
\end{matrix}}^{}{\left( \begin{aligned}
 & \frac{VAR\_ DAM_{r,t,c,'LO',j}}{DAM\_ BQT{Y_{r,c}}^{DAM\_ ELAST_{r,c,'LO'}}} \times \\
 & \left( \begin{aligned}
 & DAM\_ BQTY_{r,c} - DAM\_ VOC_{r,c,'LO'} + \\
 & DAM\_ SIZE_{r,c,'LO'} \times (j - 0.5)
\end{aligned} \right)^{DAM\_ ELAST_{r,c,'LO'}}
\end{aligned} \right) +} \\
 & VAR\_ DAM_{r,t,c,'FX',1} \\
 & \sum_{\begin{matrix}
jj \in \mathbf{dam}\_\mathbf{nu}\mathbf{m}_{r,c,jj,'UP'} \\
j \leq ORD(jj)
\end{matrix}}^{}\left( \begin{aligned}
 & \frac{VAR\_ DAM_{r,t,c,'UP',j}}{DAM\_ BQT{Y_{r,c}}^{DAM\_ ELAST_{r,c,'UP'}}} \times \\
 & \left( \begin{aligned}
 & DAM\_ BQTY_{r,c} + \frac{DAM\_ SIZE_{r,c,'FX'}}{2} + \\
 & DAM\_ SIZE_{r,c,'UP'} \times (j - 0.5)
\end{aligned} \right)^{DAM\_ ELAST_{r,c,'UP'}}
\end{aligned} \right)
\end{aligned} \right\rbrack
} \\ \\ {\left\{ = \right\}
} \\ \\ {VAR\_ OBJ_{r,'OBJDAM',cur}}$$

**\
Case B: Non-linear functions**

$${\sum_{(t,c) \in \left\{ \mathbf{rt}\mathbf{c}_{\mathbf{r},\mathbf{t},\mathbf{c}}|(DAM\_ COST_{r,t,} > 0) \right\}}^{}{DAM\_ COST_{r,t,c,cur} \times OBJ\_ PVT_{r,t,cur}} \times 
} \\ \\ {\left\lbrack \begin{aligned}
 & \\
 & \frac{\left( \begin{aligned}
 & \left( \begin{aligned}
 & VAR\_ DAM_{r,t,c,'LO',j} + \\
 & DAM\_ BQTY_{r,c} - DAM\_ VOC_{r,c,'LO'}
\end{aligned} \right)^{\left( DAM\_ ELAST_{r,c,'LO'} + 1 \right)} - \\
 & \left( DAM\_ BQTY_{r,c} - DAM\_ VOC_{r,c,'LO'} \right)^{\left( DAM\_ ELAST_{r,c,'LO'} + 1 \right)}
\end{aligned} \right)}{DAM\_ BQT{Y_{r,c}}^{DAM\_ ELAST_{r,c,'LO'}} \times \left( DAM\_ ELAST_{r,c,'LO'} + 1 \right)} + \\
 & \\
 & \frac{\left( \begin{aligned}
 & \left( VAR\_ DAM_{r,t,c,'UP',j} + DAM\_ BQTY_{r,c} \right)^{\left( DAM\_ ELAST_{r,c,'UP'} + 1 \right)} - \\
 & \left( DAM\_ BQTY_{r,c} \right)^{\left( DAM\_ ELAST_{r,c,'UP'} + 1 \right)}
\end{aligned} \right)}{DAM\_ BQT{Y_{r,c}}^{DAM\_ ELAST_{r,c,'UP'}} \times \left( DAM\_ ELAST_{r,c,'UP'} + 1 \right)}
\end{aligned} \right\rbrack
} \\ \\ {\left\{ = \right\}
} \\ \\ {VAR\_ OBJ_{r,'OBJDAM',cur}}$$

## References

Goldstein, G., Noble, K. & Van Regemorter, D. 2001. *Adaptation to MARKAL for including environmental damages*. MARKAL User Information Note.

Loulou, R., Goldstein, G. & Noble, K. 2004. *Documentation for the MARKAL Family of Models.* October 2004*.* <http://www.iea-etsap.org/web/Documentation.asp>

Loulou, R., Remme, U., Kanudia, A., Lehtilä, A. & Goldstein, G. 2005. *Documentation for the TIMES Model*. Energy Technology Systems Ananlysis Programme (ETSAP), April 2005. <http://www.iea-etsap.org/web/Documentation.asp>

Nemhauser, G.L., Rinnooy Kan, A.H.G. & Todd, M.J. (eds.) 1989. Handbooks in Operations Research and Management Science, Vol I: Optimization. North-Holland.


[^48]: The first row contains the parameter name, the second row contains in brackets the index domain over which the parameter is defined.

[^49]: This column mentions related input parameters or sets being used in the context of the headword parameter.

[^50]: This column lists the unit of the parameter, the possible range of its numeric value \[in square brackets\] and the inter-/extrapolation rules that apply.

[^51]: An indication of circumstances for which the parameter is to be provided or omitted.

[^52]: Equations or variables that are directly affected by the parameter.

[^53]: Abbreviation i/e = inter-/extrapolation
