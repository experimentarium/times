# Endogenous Technological Learning (ETL)

## Introduction

As discussed in Chapter 11 of Part I, there are situations in which the rate at which a technology's unit investment cost changes over time is a function of cumulative investment in the technology. In these situations, technological learning is called endogenous.

Mixed Integer Programming (MIP) is employed in order to model Endogenous Technological Learning (ETL) in TIMES. As has already been noted in the case of Lumpy Investments, MIP problems are much more difficult to solve than standard LP problems, and so the ETL feature should be applied only where it is deemed necessary to model a limited number of technologies as candidates for Endogenous Technological Learning. This caution is especially required for large-scale TIMES instances. Another important caveat is that ETL is relevant when the modeling scope is broad e.g. when a large portion of (or perhaps the entire) world energy system is being modeled, since the technological learning phenomenon rests on global cumulative capacity of a technology, and not on the capacity implemented in a small portion of the world.

In this chapter we provide the data and modeling details associated with modeling Endogenous Technological Learning (ETL) in TIMES. The implementation of ETL in TIMES is based on the realization in the MARKAL model generator. The major part of the MARKAL code for ETL could be transferred to TIMES. Accordingly the description of ETL presented here follows the MARKAL documentation of ETL. To this end the next three sections will address the Sets, Parameters, Variables, and Equations related to the Endogenous Technological Learning option, including the special clustered learning ETL option where a component common to several technologies learns, thereby benefiting all the related (clustered) technologies.

## Sets, Switches and Parameters

Like all other aspects of TIMES the user describes the ETL components of the energy system by means of a Set and the Parameters and Switches described in this chapter. {numref}`etl-user-input-parameters` and {numref}`etl-internal-parameters` below describe the User Input Parameters, and the Matrix Coefficient and Internal Model Sets and Parameters, respectively, that are associated with the Endogenous Technological Learning option. Note that the special clustered learning ETL option requires one additional User Input Parameter (ETL-CLUSTER), and two additional Matrix Coefficient/Internal Model Parameters (CLUSTER and NTCHTEG).

Besides the basic data described in Table the user controls whether or not the ETL component is activated by means of the \$SET ETL 'YES' switch. This switch is provided by the data handling system when the user indicates that the ETL option is to be included in a run. This permits the easy exclusion of the feature if the user does not want to perform a MIP solve without having to remove the ETL data.

```{list-table} Definition of ETL user input parameters.
:name: etl-user-input-parameters
:header-rows: 1

* - Input Parameter (Indexes)
  - Alias / Internal Name
  - Related Parameters
  - Units/Range & Defaults
  - Instance (Requid/Omit/Special Conditions)
  - Description
* - CCAP0 (r,p)
  - TL_CCAP0
  - *PAT*
  <br>*CCOST0*
  - Units of capacity (e.g., GW, PJa).
  <br>\[open\]; no default.
  - Required, along with the other ETL input parameters, for each learning technology (TEG).
  - The initial cumulative capacity (starting point on the learning curve) for a (non-resource) technology that is modeled as one for which endogenous technology learning (ETL) applies. Learning only begins once this level of installed capacity is realized.
  <br>The CCAP0 parameter appears as the right-hand-side of the cumulative capacity definition constraint (EQ_CUINV).
  <br>Note that if the NCAP_PASTI parameter is specified for an ETL technology, then its value in the first period should match the value of CCAP0, otherwise an infeasibility will occur.
* - CCAPM (r,p)
  - TL_CCAPM
  - *CCOSTM*
  - Units of capacity (e.g., GW, PJa).
  <br>\[open\]; no default.
  - Required, along with the other ETL input parameters, for each learning technology (TEG).
  - The maximum cumulative capacity (ending point on the learning curve) for a (non-resource) technology that is modeled as one for which endogenous technology learning (ETL) applies.
  <br>The parameter CCAPM does not appear in any of the ETL constraints, but its value affects the values of a number of internal parameters that directly contribute to one or more of the ETL constraints.
* - TEG (p)
  - TEG
  - *ETL-CUMCAP0*
  <br>*ETL-CUMCAPMAX*
  <br>*ETL-INVCOST0*
  <br>*ETL-NUMSEG*
  <br>*ETL-PROGRATIO*
  - Indicator.
  <br>\[1\]; no default.
  - Required to identify the learning technologies.
  <br>For each TEG the other ETL input parameters are required.
  - An indicator (always 1) that a process is modeled as one for which endogenous technology learning (ETL) applies.
  <br>The set TEG controls the generation of the ETL constraints. Each of the ETL constraints is generated only for those technologies that are in set TEG.
* - SC0 (r,p)
  - TL_SC0
  - *PAT*
  - Base year monetary units per unit of capacity (e.g., 2000 M\$/GW or PJa).
  <br>\[open\]; no default.
  - Required, along with the other ETL input parameters, for each learning technology (TEG).
  - The investment cost corresponding to the starting point on the learning curve for a technology that is modeled as one for which endogenous technology learning (ETL) applies.
  <br>The parameter SC0 does not appear in any of the ETL constraints, but its value affects the values of a number of internal parameters that directly contribute to one or more of the ETL constraints.
* - SEG (r,p)
  - TL_SEG
  - *ALPH*
  <br>*BETA*
  <br>*CCAPK*
  <br>*CCOSTK*
  - Number of steps.
  <br>\[1-6\]; no default.
  - Required, along with the other ETL input parameters, for each learning technology (TEG).
  - The number of segments to be used in approximating the learning curve for a technology that is modeled as one for which endogenous technology learning (ETL) applies.
  <br>The SEG parameter appears in all of the ETL constraints that are related to piecewise linear approximation of the learning curve (EQ_CC, EQ_COS, EQ_EXPE1, EQ_EXPE2, EQ_LA1, EQ_LA2).
* - PRAT (r,p)
  - TL_PRAT
  - *CCAPK*
  <br>*CCOST0*
  <br>*CCOSTM*
  <br>*PAT*
  <br>*PBT*
  - Decimal fraction.
  <br>\[0-1\]; no default.
  - Required, along with the other ETL input parameters, for each learning technology (TEG).
  - The "progress ratio" for a technology that is modeled as one for which endogenous technology learning (ETL) applies. The progress ratio, which is referred to as the learning rate, is defined as the ratio of the change in unit investment cost each time cumulative investment in an ETL technology doubles. That is, if the initial unit investment cost is SC0 and the progress ratio is PRAT, then after cumulative investment is doubled the unit investment cost will be PRAT \* SC0.
  <br>The parameter PRAT does not appear in any of the ETL constraints, but its value affects the values of a number of internal parameters (ALPH, BETA, CCAPK, CCOST0) that directly contribute to one or more of the ETL constraints.
* - CLUSTER (r,p,p)
  - TL_CLUSTER
  <br>NCLUSTER
  - *TL_MRCLUST*
  - Decimal fraction.
  <br>\[0-1\]; no default.
  - Provided to model clustered endogenous technology learning.
  <br>Each of the learning parameters must also be specified for the key learning technology.
  - The "cluster mapping and coupling factor" for a technology that is modeled as a [clustered]{.underline} technology is associated with a [key]{.underline} learning technology to which endogenous technology learning (ETL) applies. Clustered technologies use the key ETL technology, and are subject to learning via the key technology.
  <br>The first index of the CLUSTER parameter is a [key]{.underline} learning technology.
  <br>The second index of the CLUSTER parameter is a [clustered]{.underline} technology that is associated with this [key]{.underline} learning technology.
  <br>In general there may be several [clustered]{.underline} technologies each of which is associated with the same [key]{.underline} learning technology, and hence there may be several instances of the CLUSTER parameter each of which has the same [key]{.underline} learning technology as its first index.
  <br>The numerical value of the CLUSTER parameter indicates the extent of coupling between the [clustered]{.underline} technology and the [key]{.underline} learning technology to which it is associated.
* - TL_MRCLUST (r,teg,reg,p)
  - 
  - *CLUSTER*
  - Decimal fraction.
  <br>\[0-1\]; no default.
  - See CLUSTER
  - The multi-region cluster mapping and coupling factor. Similar to CLUSTER, but may be used to map technologies p in multilple regions reg to key components teg in region r. See CLUSTER.
```

```{list-table} ETL-specific matrix coefficient and internal model parameters[^42]
:name: etl-internal-parameters
:header-rows: 1

* - Matrix Controls & Coefficients (indexes)
  - Type
  - Description & Calculations
* - ALPH (r,k,p)
  - I
  - ALPH are the intercepts on the vertical axis of the line segments in the piecewise linear approximation of the cumulative cost curve. They are calculated in COEF_ETL.ETL from the starting and ending points of the cumulative cost curve, its assumed form, the number of segments used in its piecewise linear approximation, and the choice of successive interval lengths on the vertical axis to be such that each interval is twice as wide as the preceding one. The parameter ALPH occurs in the ETL equation EQ_COS that defines the piecewise linear approximation to the cumulative cost curve.
* - BETA (r,k,p)
  - I
  - BETA are the slopes of the line segments in the piecewise linear approximation of the cumulative cost curve. They are calculated in COEF_ETL.ETL from the starting and ending points of the cumulative cost curve, its assumed form, the number of segments used in its piecewise linear approximation, and the choice of successive interval lengths on the vertical axis to be such that each interval is twice as wide as the preceding one. The parameter BETA occurs in the ETL equation EQ_COS that defines the piecewise linear approximation to the cumulative cost curve.
* - CCAP0 (r,p)
  - A
  - CCAP0 is the initial cumulative capacity (starting point on the learning curve). The parameter CCAP0 occurs in the ETL equation EQ_CUINV that defines cumulative capacity in each period.
* - CCAPK (k,p)
  - I
  - CCAPK are the break points on the horizontal axis in the piecewise linear approximation of the cumulative cost curve. They are calculated in COEF_ETL.ETL from the starting and ending points of the cumulative cost curve, its assumed form, the number of segments used in its piecewise linear approximation, and the choice of successive interval lengths on the vertical axis to be such that each interval is twice as wide as the preceding one. The parameter CCAPK occurs in the ETL equations EQ_LA1 and EQ_LA2 whose role is to ensure that variable R_LAMB(r,t,k,p) lies in the k^th^ interval, i.e., between CCAPK(r,k-1,p) and CCAPK(r,k,p), when its associated binary variable R_DELTA(r,t,k,p) = 1.
* - CCOST0 (r,p)
  - I
  - CCOST0 is the initial cumulative cost (starting point on the learning curve). It is calculated in COEF_ETL.ETL from the initial cumulative capacity (CCAP0) and corresponding initial investment cost (user input parameter SC0) and the progress ratio (user input parameter PRAT). The parameter CCOST0 occurs in the ETL equation EQ_IC1 that defines first period investment costs (prior to discounting).
* - SEG (r,p)
  - A
  - The user input parameter SEG is the number of segments in the cumulative cost curve. The parameter SEG occurs in all of those ETL equations that are related to the piecewise linear approximation of the cumulative cost curve.
* - TEG (p)
  - S
  - TEG is the set of technologies to which endogenous technology learning (ETL) applies. Each of the ETL equations has set TEG as an index.
* - CLUSTER (r,p,p)
  - I
  - The user input parameter CLUSTER (cluster mapping and coupling factor) is only relevant when modeling clustered endogenous technology learning. The parameter occurs in the special ETL cluster equation EQ_CLU that defines investment in new capacity (VAR_NCAP) in the key learning technology as the weighted sum of investments in new capacity of the clustered technologies that are attached to the key technology. (The weights used are the numeric values of the CLUSTER parameter.)
* - TL_MRCLUST (r,teg,reg,p)
  - I
  - The user input parameter TL_MRCLUST is only relevant when modeling clustered endogenous technology learning. The parameter occurs in the special ETL cluster equation EQ_MRCLU that defines investment in new capacity (VAR_NCAP) in the key learning technology as the weighted sum of investments in new capacity of the clustered technologies that are attached to the key technology.
* - NTCHTEG (r,p)
  - I
  - The parameter NTCHTEG is only relevant when modeling clustered endogenous technology learning. If TEG is an ETL technology, then NTCHTEG(R,TEG) is the number of clustered technologies that are attached to key technology TEG. NTCHTEG is calculated in COEF_ETL.ETL from the "cluster mapping and coupling factor" (CLUSTER). It occurs in the special ETL cluster equation EQ_CLU.
* - PBT (r,p)
  - 
  - The learning index PBT is an internal parameter calculated in COEF_ETL.ETL. It is derived from the progress ratio PRAT using the formula: PBT(r,p) = -log(PRAT(r,p))/log(2). PBT does not occur directly in the equations, but is used in the calculation of equation coefficients.
* - PAT (r,p)
  - 
  - The internal parameter PAT describes the specific investment costs of the first unit. It is derived in COEF_ETL.ETL using PBT, SC0 and CCAP0. PAT does not occur directly in the equations, but is used in the calculation of equation coefficients.
* - K
  - 
  - The set K has the members '1'-'6' and is used as indicator for the kink points of the piecewise linear approximation of the cumulative cost curve. The number of elements can be changed in the \*run file if desired.
* - WEIG (r,k,prc)
  - I
  - The internal parameter WEIG is calculated in COEF_ETL.ETL and is used as a factor in the calculation of the length of the intervals being used in the piecewise linear approximation of the cumulative cost curve. The interval lengths on the vertical axis are chosen in such a way that each interval is twice as wide as the preceding one.
```

## Variables

The variables that are used to model the Endogenous Technological Learning option in TIMES are presented in {numref}`etl-variables`. As is the case with the modeling of lumpy investments, the primary role of the variables and equations used to model ETL is to control the standard TIMES investment variable (VAR_NCAP) and the associated dynamic cost of these investments, so ETL is rather self-contained. That is the VAR_NCAP variable links the ETL decisions to the rest of the model, and the VAR_IC investment cost variable determines the associated contribution to the regional investment costs (VAR_OBJINV). Note that the special clustered learning ETL option does not require any additional variables, as compared with the modeling of endogenous technology learning when there are no clusters.

```{list-table} ETL-specific model variables.
:name: etl-variables
:header-rows: 1

* - Variable (Indexes)
  - Variable Description
* - VAR_CCAP (r,t,p)
  - The cumulative investment in capacity for an ETL technology. This variable represents the initial cumulative capacity (CCAP0) plus investments in new capacity made up to and including the current period. This variable differs from the total installed capacity for a technology (VAR_CAP) in that it includes all investments in new capacity made up to and including the current period, whereas the latter only includes investments that are still available (i.e. whose life has not expired yet).
* - VAR_CCOST (r,t,p)
  - The cumulative cost of investment in capacity for an ETL technology. The cumulative cost is interpolated from the piecewise linear approximation of the cumulative cost curve.
* - VAR_DELTA (r,t,p,k)
  - Binary variable (takes the value 0 or 1) used for an ETL technology to indicate in which interval of the piecewise linear approximation of the cumulative cost curve the cumulative investment in capacity (VAR_CCAP) lies. A value of 1 for this variable for exactly one interval k indicates that VAR_CCAP lies in the k^th^ interval.
* - VAR_IC (r,t,p)
  - The portion of the cumulative cost of investment in capacity for an ETL technology (VAR_CCOST) that is incurred in period t, and so subject to the same discounting that applies to other period t investment costs. This variable is calculated as the difference between the cumulative costs of investment in capacity for periods t and t-1, and enters the regional investment cost part of the objective function (EQ_OBJINV)
* - VAR_LAMBD (r,t,p,k)
  - Continuous variable used for an ETL technology to represent the portion of cumulative investment in capacity (VAR_CCAP) that lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve. For a given ETL technology and given time period, ETL model constraints involving this variable and the associated binary variable VAR_DELTA ensure that VAR_LAMBD is positive for exactly one interval k.
```

### VAR_CCAP(r,t,p)

**Description:** The cumulative investment in capacity for an ETL technology.

**Purpose and** This variable tracks the cumulative investment in capacity for an ETL

**Occurrence:** technology which then determines, along with the progress ratio, how much the investment cost is to be adjusted for the learning gains.

This variable is generated for each ETL technology in all time periods beginning from the period that the technology is first available. It appears in the cumulative capacity definition constraint (EQ_CUINV) that defines it as the initial cumulative capacity (CCAP0) plus investments in new capacity (VAR_NCAP) made up to and including the current period. It also appears in the cumulative capacity interpolation constraint (EQ_CC). This constraint equates VAR_CCAP(r,t,p) to the sum over k of the variables VAR_LAMBD(r,t,p,k) used to represent the cumulative investment in capacity lying in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.

**Units:** PJ/a, Gw, or Bvkm/a, or any other unit defined by the analyst to represent technology capacity.

**Bounds:** This variable is not directly bounded. It may be indirectly bounded by specifying a bound (NCAP_BND) on the level of investment in new capacity (VAR_NCAP).

### VAR_CCOST(r,t,p)

**Description:** The cumulative cost of investment in capacity for an ETL technology.

**Purpose and** This variable defines the interpolated cumulative cost of investment in

**Occurrence:** capacity in terms of the continuous variables VAR_LAMBD and the binary variables VAR_DELTA, and the internal model parameters ALPH and BETA. ALPH and BETA represent the intercepts on the vertical axis and the slopes, respectively, of the line segments in the piecewise linear approximation of the cumulative cost curve.

This variable is generated for each ETL technology in all time periods beginning from the period that the technology is first available. It appears in the cumulative cost interpolation equation (EQ_COS) that defines it. It also appears in the equations EQ_IC1 and EQ_IC2 that define the VAR_IC variables that represent the portions of the cumulative cost of investment in capacity that are incurred in period t.

**Units:** Million 2000 US\$, or any other unit in which costs are tracked.

**Bounds:** None.

### VAR_DELTA(r,t,p,k)

**Description:** *Binary* variable (takes the value 0 or 1) used for an ETL technology to indicate in which interval of the piecewise linear approximation of the cumulative cost curve the cumulative investment in capacity (VAR_CCAP) lies.

**Purpose and** To indicate which step on the learning curve a technology achieves. A

**Occurrence:** value of 1 for this variable for interval k, and zero values for intervals ≠ k, imply that the cumulative investment in capacity (VAR_CCAP) lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.

This binary variable, along with the associated continuous variable VAR_LAMBD, are generated for each ETL technology in all time periods beginning from the period that the technology is first available, and for each interval in the piecewise linear approximation. It appears in the constraint EQ_DEL, whose purpose is to ensure that, for each ETL technology in each period, it has a value of 1 for exactly one interval k (with zero values for intervals ≠ k); and in the cumulative cost interpolation constraint (MR_COS). It also appears in the pair of constraints EQ_LA1 and EQ_LA2, whose purpose is to ensure that VAR_LAMBD, if positive for interval k, is between the two break points on the horizontal axis for interval k in the piecewise linear approximation. (See below under "Purpose and Occurrence" for the variable VAR_LAMBD.)

Finally, this binary variable appears in two constraints EQ_EXPE1 and EQ_EXPE2, whose purpose is to reduce the domain of feasibility of the binary variables and thereby improve solution time for the Mixed Integer Program (MIP).

**Units:** None. This is a binary variable that takes the value 0 or 1.

**Bounds:** This binary variable is not directly bounded.

### VAR_IC(r,t,p)

**Description:** The portion of the cumulative cost of investment in capacity for an ETL technology (VAR_CCOST) that is incurred in period t.

**Purpose and** This variable represents the portion of the cumulative cost of investment

**Occurrence:** in capacity for an ETL technology that is incurred in period t, and so is subject to the same discounting in the investment cost part of the objective function (EQ_OBJINV) that applies to other period t investment costs.

This variable is calculated as the difference between the cumulative costs of investment in capacity for period t and t-1, and is generated for each ETL technology in all time periods beginning from the period that the technology is first available. Apart from its appearance in the objective function, this variable appears in the constraints EQ_IC1 and EQ_IC2 that define it in the first period that the technology is available, and in subsequent periods, respectively. It also appears in the salvage of investments constraint (EQ_OBJSALV), which calculates the amount to be credited back to the objective function for learning capacity remaining past the modeling horizon.

**Units:** Million 2000 US\$, or any other unit in which costs are tracked.

**Bounds:** None.

### VAR_LAMBD(r,t,p,k)

**Description:** *Continuous* variable used for an ETL technology to represent the portion of cumulative investment in capacity (VAR_CCAP) that lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.

**Purpose and** A positive value for this variable for interval k, and zero values for

**Occurrence:** intervals ≠ k, imply that the cumulative investment in capacity (VAR_CCAP) lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve. This continuous variable, along with the associated binary variable VAR_DELTA, are generated for each ETL technology in all time periods beginning from the period that the technology is first available (START), and for each interval in the piecewise linear approximation.

> Since this variable represents the portion of the cumulative investment in capacity (VAR_CCAP) that lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve, the value of EQ_LAMBD -- if positive -- is required to be between CCAPK(k-1,p) and CCAP(k,p), where the internal model parameters CCAPK are the break points on the horizontal axis in the piecewise linear approximation of the cumulative cost curve. A zero value for VAR_LAMBD is also allowed. These requirements on the value of VAR_LAMBD are imposed via the pair of constraints EQ_LA1 and EQ_LA2, in which the value for VAR_LAMBD is subject to lower and upper bounds of CCAPK(k-1,p) \* VAR_DELTA and CCAP(k,p) \* VAR_DELTA respectively, where VAR_DELTA = VAR_DELTA(r,t,p,k) is the binary variable associated with VAR_LAMBD = VAR_LAMBD(r,t,p,k).

This variable also appears in the cumulative capacity interpolation constraint (EQ_CC), and the cumulative cost interpolation constraint (EQ_COS).

**Units:** PJ/a, Gw, or Bvkm/a, or any other unit defined by the analyst to represent technology capacity.

**Bounds:** The pair of constraints EQ_LA1 and EQ_LA2 that are discussed above have the effect of either bounding VAR_LAMBD between CCAPK(k-1,p) and CCAP(k,p), or forcing VAR_LAMBD to be zero.

## Equations

The equations that are used to model the Endogenous Technological Learning option in TIMES are presented in {numref}`etl-constraints` below. Since the primary role of the variables and equations used to model ETL is to control the standard TIMES investment variable (VAR_NCAP) and the associated dynamic cost of these investments, ETL is rather self-contained. That is the VAR_NCAP variable links the ETL decisions to the rest of the model, and the VAR_IC investment cost variable determines the associated contribution to the regional investment cost part objective function (EQ_OBJINV). Note that the special clustered learning ETL option involves one additional equation (EQ_CLU), as compared with the modeling of endogenous technology learning where there are no clusters. IN BOX BELOW, ADD ANSWER or CHANGE TO \"system\"

```{list-table} Table C-4. ETL-specific model constraints
:name: etl-constraints
:header-rows: 1

* - Constraints (Indexes)
  - Constraint Description
  - GAMS Ref
* - EQ_CC (r,t,p)
  - The Cumulative Capacity Interpolation constraint for an ETL technology. This constraint defines the cumulative investment in capacity for a technology (VAR_CCAP) in a period as the sum over all intervals k of the continuous variables R_LAMBD(r,t,p,k) that represent cumulative investment in capacity as lying in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.
  - EQU_EXT.ETL
* - EQ_CLU (r,t,p)
  - Constraint that is generated only for the special clustered learning ETL option (CLUSTER). For a key learning ETL technology it defines investment in new capacity (VAR_NCAP) as the weighted sum of investments in new capacity of the associated clustered technologies.
  - EQU_EXT.ETL
* - EQ_COS (r,t,p)
  - The Cumulative Cost Interpolation constraint for an ETL technology. This constraint defines the interpolated cumulative cost of investment in capacity for a technology (VAR_CCOST) in a period in terms of the binary variables VAR_DELTA and the continuous variables VAR_LAMBD, and the internal model parameters ALPH and BETA.
  - EQU_EXT.ETL
* - EQ_CUINV (r,t,p)
  - The Cumulative Capacity Definition constraint for an ETL technology. Defines the cumulative investment in capacity for a technology in a period as the initial cumulative capacity (CCAP0) plus the sum of investments in new capacity (VAR_NCAP) made up to and including this period.
  - EQU_EXT.ETL
* - EQ_DEL (r,t,p)
  - The constraint for an ETL technology that ensures that in each period there is exactly one interval k for which the binary variable R_DELTA(r,t,p,k) has value 1 (with zero values for intervals ≠ k).
  - EQU_EXT.ETL
* - EQ_EXPE1 (r,t,p,k)
  - One of two constraints for an ETL technology to improve MIP solution time by reducing the domain of feasibility of the binary variables VAR_DELTA.
  - EQU_EXT.ETL
* - EQ_EXPE2 (r,t,p,k)
  - Second of two constraints for an ETL technology to improve MIP solution time by reducing the domain of feasibility of the binary variables VAR_DELTA.
  - EQU_EXT.ETL
* - EQ_IC1 (r,t,p)
  - The constraint for an ETL technology that defines the portion of the cumulative cost of investment in capacity (VAR_IC) that is incurred in the first period of the model horizon.
  - EQU_EXT.ETL
* - EQ_IC2 (r,t,p)
  - The constraint for an ETL technology that defines the portion of the cumulative cost of investment in capacity (VAR_IC) that is incurred in each period but the first one.
  - EQU_EXT.ETL
* - EQ_LA1 (r,t,p,k)
  - The constraint for an ETL technology that sets a lower bound on the continuous variable VAR_LAMBD(r,t,p,k).
  - EQU_EXT.ETL
* - EQ_LA2 (r,t,p,k)
  - The constraint for an ETL technology that sets an upper bound on the continuous variable VAR_LAMBD(r,t,p,k).
  - EQU_EXT.ETL
* - EQ_MRCLU\ (r,t,p)
  - Constraint that is generated only for the special clustered learning ETL option (TL_MRCLUST). For a key learning ETL technology it defines investment in new capacity (VAR_NCAP) as the weighted sum of investments in new capacity of the associated clustered technologies in multilple regions.
  - EQU_EXT.ETL
* - EQ_OBJSAL (r,cur)
  - For an ETL technology in periods appropriately close to the model horizon, part of the investment costs (VAR_IC) exceed the model horizon. This part of the investment cost is reflected in the calculation of the salvage value variable VAR_OBJSAL.
  - EQOBSALV.MOD
* - EQ_OBJINV (r,cur)
  - The endogenously calculated cost of investments for learning technologies (VAR_IC) needs to be discounted and included in the regional investment cost part of the objective function (EQ_OBJINV) in place of the traditional investment calculation using variable VAR_NCAP.
  - EQOBJINV.MOD
```

### EQ_CC(r,t,p)

**Description:** The Cumulative Capacity Interpolation constraint for an ETL technology.

**Purpose and Occurrence:** This constraint defines the cumulative investment in capacity for a technology in a period (VAR_CCAP) as the sum over all intervals $k$ of the *continuous* variables VAR_LAMBD(r,t,p,k) that represent cumulative investment in capacity as lying in the $k^{th}$ interval of the piecewise linear approximation of the cumulative cost curve. This constraint links the cumulative capacity investment variable (VAR_CCAP) to the variables VAR_LAMBD. In combination with other ETL constraints, it is fundamental to ensuring the validity of the piecewise linear approximation of the cumulative cost curve.

This equation is generated in each time period for which the ETL technology is available.

**Units:** Technology capacity units.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as discussed in Section 10.3 of PART I.

**Equation**

$$EQ\_CC_{r,t,p} \forall [(p \in teg) \land ((r,t,p) \in rtp)]$$

Cumulative investment in capacity in the current period.

$$VAR\_CCAP_{r,t,p}$$

$$\{ = \}$$

Sum over all intervals $k$ (in the piecewise linear approximation of the cumulative cost curve) of the *continuous* variables VAR_LAMBD in the current period $t$.

$$\sum_k {VAR\_LAMBD_{r,t,p,k}}$$

### EQ_CLU(r,t,p)

**Description:** For a <ins>key</ins> learning ETL technology it defines investment in new capacity (VAR_NCAP) as the weighted sum of investments in new capacity of the attached clustered technologies. The weights used are the numeric values of the CLUSTER parameter.

**Purpose and Occurrence:** Defines the relationship between investment in new capacity for a <ins>key</ins> learning technology learning ETL technology and investment in new capacity for the associated clustered technologies. This equation is generated in each time period for which the ETL technology is available. It is a <ins>key</ins> learning technology, that is, it has associated clustered technologies.

**Units:** Money units, e.g., million 2000 US\$, or any other unit in which costs are tracked.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variable (DVR_CLU) of this constraint in the MIP solution is of little interest.

**Remarks:** Activation of the special <ins>clustered</ins> learning ETL option occurs automatically if data is included for the CLUSTER parameter.

**Equation**

$$EQ\_ CLU_{r,t,p}\forall[(p \in teg) \land(NTCHTEG_{r,p} > 0) \land ((r,t,p) \in rtp)]$$

Investment in new capacity (for <u>key</u> learning technology $p \in teg$) in period $t$.

$$VAR\_ NCAP_{r,t,p}$$

$$\{ = \}$$

The weighted sum of the investments in new capacity in period $t$ of the clustered technologies $p'$ attached to the <u>key</u> learning technology $p \in teg$, and whose START period is less than or equal to $t$. The weights used are the numeric values of the CLUSTER parameter.

$$missing \ expression$$

### EQ_COS(r,t,p)

**Description:** The Cumulative Cost Interpolation constraint for an ETL technology.

**Purpose and Occurrence:** This constraint defines the interpolated cumulative cost of investment in
 capacity for a technology in a period (VAR_CCOST) in terms of the binary variables VAR_DELTA and the continuous variables VAR_LAMBD, and the internal model parameters ALPH and BETA, where ALPH and BETA represent the intercepts on the vertical axis and the slopes, respectively, of the line segments in the piecewise linear approximation of the cumulative cost curve. For a more precise definition, see "Equation" below. In combination with other ETL constraints, it is fundamental to ensuring the validity of the piecewise linear approximation of the cumulative cost curve. This equation is generated in each time for which the ETL technology is available.

**Units:** Money units, e.g., million 2000 US\$, or any other unit in which costs are tracked.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as discussed in Section 10.3 of PART I.

**Equation**

$$EQ\_ COS_{r,t,p}\forall\left[(p \in teg) \land \left( (r,t,p) \in rtp \right) \right]$$

Interpolated cumulative cost of investment in capacity in the current period.

$$VAR\_ CCOST_{r,t,p}$$
$$\{ = \}$$

Sum over all intervals $k$ (in the piecewise linear approximation of the cumulative cost curve) of $ALPH$ times the binary variable $VAR\_DELTA$ plus $BETA$ times the *continuous* variable $VAR\_LAMBD$, for the current period $t$, where $ALPH$ and $BETA$ represent the intercepts on the vertical axis and the slopes, respectively, of the $k^{th}$ interval.

$$\sum_k (ALPH_{k,p} \times VAR\_DELTA_{r,t,p,k} + BETA_{k,p} \times VAR\_LAMBD_{r,t,p,k})$$

### EQ_CUINV(r,t,p)

**Description:** The Cumulative Capacity Definition constraint for an ETL technology.

**Purpose and Occurrence:** This constraint defines the cumulative investment in capacity of a technology in a period (VAR_CCAP) as the initial cumulative capacity (CCAP0) plus the sum of investments in new capacity made up to and including this period. This equation is generated in each time period for which the ETL technology is available.

**Units:** Technology capacity units.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as mentioned above.

**Equation**

$$EQ\_CUINV_{r,t,p}\forall [(p \in teg) \land ((r,t,p) \in rtp)]$$

Cumulative investment in capacity in the current period.

$$VAR\_CCAP_{r,t,p}$$

$$\{ = \}$$

Cumulative investment in capacity at the start of the learning process.

$$CCAP0_{r,p}+$$

Sum of the investments made since the technology is first available.

$$\sum_{u \in rtp_{r,u,p} \land u \leq t} {VAR\_NCAP_{r,u,p}}$$

### EQ_DEL(r,t,p)

**Description:** The constraint for an ETL technology that ensures that in each time period there is exactly one interval k for which the *binary* variable VAR_DELTA(r,t,p,k) has value 1 (with zero values for intervals ≠ k).

**Purpose and Occurrence:** To ensure that only one of the *binary* variable VAR_DELTA(r,t,p,k) has value 1 for each technology. This constraint, in combination with other ETL constraints, is fundamental to ensuring the validity of the piecewise linear approximation of the cumulative cost curve. This equation is generated in each time period for which the ETL technology is available.

**Units:** None.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be 1 in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_DEL_{r,t,p}\forall[(p \in teg) \land ((r,t,p) \in rtp)]$$

Sum over all intervals $k$ (in the piecewise linear approximation of the cumulative cost curve) of the *binary* variables VAR_DELTA in the current period $t$.

$$\{ = \} \space 1$$

### EQ_EXPE1(r,t,p,k)

**Description:** One of two constraints for an ETL technology to improve MIP solution time by reducing the domain of feasibility of the binary variables VAR_DELTA.

**Purpose and Occurrence:** To improve MIP solution time this constraint takes advantage of the observation that cumulative investment is increasing with time, thus ensuring that if the cumulative investment in period t lies in segment $k$, then it will not lie in segments $k-1, k-2, ..., 1$ in period $t+1$. This equation is generated for each ETL technology in each time period, for which the technology is available, and excluding the final period (TLAST), and for each interval k in the piecewise linear approximation of the cumulative cost curve.

**Units:** None.

**Type:** *Binding.* The equation is a greater than or equal to (≥) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be greater than or equal to zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_EXPE1_{r,t,p,k} \forall [(p \in teg) \land ((r,t,p) \in rtp) \land (t < TLAST)]$$

Sum over intervals $j \leq k$ of binary variables VAR_DELTA(r,t,p,j), for the $k^{th}$ interval, in period $t$.

$$\sum_{j \leq k} (VAR\_DELTA_{r,t,p,j})$$

$$\{ \geq \}$$

Sum over intervals $j \leq k$ of binary variables VAR_DELTA(r,t,p,j), for the $k^{th}$ interval, in period $t+1$.

$$\sum_{j \leq k} (VAR\_DELTA_{r,t+1,p,j})$$

### EQ_EXPE2(r,t,p,k)

**Description:** Second of two constraints for an ETL technology to improve MIP solution time by reducing the domain of feasibility of the binary variables VAR_DELTA. Both constraints rely on the observation that cumulative investment is increasing as time goes on.

**Purpose and Occurrence:** To improve MIP solution times this constraint is derived from the observation that if cumulative investment in period t lies in segment k, then it must lie in segment $k$ or $k+1$ or $k+2$, etc. in period $t+1$.

This equation is generated for each ETL technology in each time period, for which the technology is available, and excluding the final period (TLAST), and for each interval k in the piecewise linear approximation of the cumulative cost curve.

**Units:** None.

**Type:** *Binding.* The equation is a less than or equal to (≤) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be less than or equal to zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_EXPE2_{r,t,p,k} \forall [(p \in teg) \land ((r,t,p) \in rtp) \land (t < TLAST)]$$

Sum over intervals $j \geq k$ of binary variables VAR_DELTA(r,t,p,j), for the $k^{th}$ interval, in period $t$.

$$\sum_{j \geq k} (VAR\_DELTA_{r,t,p,j})$$

$$\{ \leq \}$$

Sum over intervals $j \geq k$ of binary variables VAR_DELTA(r,t,p,j), for the $k^{th}$ interval, in period $t+1$.

$$\sum_{j \geq k} (VAR\_DELTA_{r,t+1,p,j})$$

### EQ_IC1(r,t,p)

**Description:** The constraint for an ETL technology that defines the portion of the cumulative cost of investment in capacity (VAR_IC) that is incurred in period $t$, where $t$ is the first period of model horizon.

**Purpose and Occurrence:** To determine the variable VAR_IC which represents the current investment cost incurred in the first period a learning technology is available according to the cumulative investments made in that period. VAR_IC then enters the regional investment cost part of the objective function (EQ_OBJINV) subject to the same discounting that applies to other period $t$ investment costs. This equation is generated for the first period of the model horizon.

**Units:** Money units, e.g., million 2000 US\$, or any other unit in which costs are tracked.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_IC1_{r,t,p} \forall (p \in teg) \land (t = MIYR\_V1)$$

The portion of the cumulative cost of investment in capacity that is incurred in period $t$, in this case the first period the technology is available.

$$VAR\_IC_{r,t,p}$$

$$\{ = \}$$

The cumulative cost of investment in new capacity in the first period $t$ ($t = MIYR\_V1$).

$$VAR\_CCOST_{r,t,p} -$$

The initial cumulative cost of investment in new capacity for a learning technology.

$$CCOST0_{}$$

### EQ_IC2(r,t,p)

**Description:** The constraint for an ETL technology that defines the portion of the cumulative cost of investment in capacity that is incurred in each period $t$ other than the first period.

**Purpose and Occurrence:** To determine the variable VAR_IC which represents the current investment cost incurred in period t according to the cumulative investments made thus far, where VAR_IC then enters the regional investment cost part of the objective function (EQ_OBJINV) subject to the same discounting that applies to other period t investment costs. This equation is generated in each time period other than the first period of the model horizon.

**Units:** Money units, e.g., million 2000 US\$, or any other unit in which costs are tracked.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_IC2_{r,t,p}\forall (p \in teg) \land (t > MIYR\_V1)$$

The portion of the cumulative cost of investment in capacity that is incurred in period $t$.

$$VAR\_IC_{r,t,p}$$

$$\{ = \}$$

The cumulative cost of investment in new capacity as of period $t$.

$$VAR\_CCOST_{r,t,p} -$$

The cumulative cost of investment in new capacity as of the previous period $t-1$.

$$VAR\_CCOST_{r,t-1,p}$$

### EQ_LA1(r,t,p,k)

**Description:** The constraint for an ETL technology that sets a lower bound on the continuous variable VAR_LAMBD(r,t,p,k).

**Purpose and Occurrence:** To set the lower bound for VAR_LAMBD(r,t,p,k) to CCAPK(r,k-1,p) \* VAR_DELTA, where CCAPK(r,k-1,p) is the left hand end of the $k^{th}$ interval and VAR_DELTA = VAR_DELTA(r,t,p,k) is the binary variable associated with VAR_LAMBD(r,t,p,k). If binary variable VAR_DELTA = 1, the effect is to set a lower bound on variable VAR_LAMBD(r,t,p,k) of CCAPK(r,k-1,p), whereas if VAR_DELTA = 0 the effect is to set a lower bound of 0. This constraint, in combination with other ETL constraints, is fundamental to ensuring the validity of the piecewise linear approximation of the cumulative cost curve.

This equation is generated in each time period, for which the ETL technology is available, and for each interval k in the piecewise linear approximation of the cumulative cost curve.

**Units:** Technology capacity units.

**Type:** *Binding.* The equation is a greater than or equal to (≥) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be greater than or equal to zero in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_LA1_{r,t,p,k}\forall [(p \in teg) \land ((r,t,p) \in rtp)]$$

Portion of the cumulative investment in capacity that lies in the $k^{th}$ interval (of the piecewise linear approximation of the cumulative cost curve), in the current period.

$$VAR\_LAMBD_{r,t,p,k}$$

$$\{ \geq \}$$

Left hand end of the $k^{th}$ interval (CCAPK(r,k-1,p)) times binary variable VAR_DELTA(r,t,p,k), in the current period.

$$CCAPK_{r,k - 1,p} \times VAR\_DELTA_{r,t,p,k}$$

### EQ_LA2(r,t,p,k)

**Description:** The constraint for an ETL technology that sets an upper bound on the continuous variable VAR_LAMBD(r,t,p,k).

**Purpose and Occurrence:** To set the upper bound of VAR_LAMBD(r,t,p,k) to CCAPK(r,k,p) \* VAR_DELTA, where CCAPK(r,k,p) is the right hand end of the $k^{th}$ interval and VAR_DELTA = VAR_DELTA(r,t,p,k) is the binary variable associated with VAR_LAMBD(r,t,p,k). If binary variable VAR_DELTA = 1, the effect is to set an upper bound on variable VAR_LAMBD(r,t,p,k) of CCAPK(r,k,p), whereas if VAR_DELTA = 0 the effect is to set an upper bound of 0. This constraint, in combination with other ETL constraints, is fundamental to ensuring the validity of the piecewise linear approximation of the cumulative cost curve.

This equation is generated in each time period, for which the ETL technology is available, and for each interval k in the piecewise linear approximation of the cumulative cost curve.

**Units:** Technology capacity units.

**Type:** *Binding.* The equation is a less than or equal to (≤) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be less than or equal to zero in a feasible solution.

*Dual variable:* The dual variable (DVR_LA2) of this constraint in the MIP solution is of little interest.

**Equation**

$$MR\_LA2_{r,t,p,k} \forall [(p \in teg) \land ((r,t,p) \in rtp)]$$

Portion of the cumulative investment in capacity that lies in the $k^{th}$ interval (of the piecewise linear approximation of the cumulative cost curve), in the current period.

$$VAR\_LAMBD_{r,t,p,k}$$

$$\{ \leq \}$$

Right hand end of the $k^{th}$ interval (CCAPK(r,k,p)) times binary variable R_DELTA(r,t,p,k), in the current period.

$$CCAPK_{r,k,p} \times VAR\_DELTA_{r,t,p,k}$$

### EQ_MRCLU(r,t,p)

**Description:** For a <ins>key</ins> learning ETL technology it defines investment in new capacity (VAR_NCAP) as the weighted sum of investments in new capacity of the attached clustered technologies in multiple regions. The weights used are the numeric values of the TL_MRCLUST parameter.

**Purpose and Occurrence:** Defines the relationship between investment in new capacity for a <ins>key</ins> learning ETL technology learning ETL technology and investment in new capacity for the associated clustered technologies. This equation is generated in each time period for which the ETL technology is available. It is a <ins>key</ins> learning technology, that is, it has associated clustered technologies, possibly in multiple regions.

**Units:** Money units, e.g., million 2010 US\$, or any other unit in which costs are tracked.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variable of this constraint in the MIP solution is of little interest.

**Remarks:** Activation of the special <ins>clustered</ins> learning ETL option occurs automatically if data is included for the TL_MRCLUST parameter.

**Equation**

$$EQ\_MRCLU_{r,t,p}\forall [(p \in teg) \land (TL\_RP\_KC_{r,p}) \land ((r,t,p) \in rtp)]$$

Investment in new capacity (for key learning technology $p \in teg$) in period $t$.

$$VAR\_NCAP_{r,t,p}$$

$$\{ = \}$$

The weighted sum of the investments in new capacity in period $t$ of the clustered technologies $p'$ attached to the <ins>key</ins> learning technology $p \in teg$, and whose START period is less than or equal to $t$. The weights used are the numeric values of the CLUSTER parameter.

$$\sum_{(reg,t,prc \in {rtp})} (TL\_MRCLUST_{reg,p,prc} \times VAR\_NCAP_{reg,t,prc})$$

### EQ_OBJSAL(r,cur)

**Description:** Regional salvage value part of objective function adjusted to include the salvage value of endogenously determined investments (VAR_IC) in learning technologies. A salvage value for a learning technology investment exists when the technical lifetime of the investment exceeds the model horizon.

**Purpose and Ocurrence:** The objective function part calculating the salvage value is changed (for learning technologies only) by replacing the traditional calculation of the salvage value of investments with one based on the investment costs of learning technologies (VAR_IC).

**Units:** Money units, e.g., million 2000 US\$, or any other unit in which costs are tracked.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Equation**

$$EQ\_OBJSAL_{r,cur}$$

All the basic objective function term for calculating the salvage value (section 5.2.8)

$$ ... $$

The calculated salvage value associated with the ETL technologies. The internally derived parameter coefficient OBJSIC describing the portion of the investment costs that has to be salvaged. It takes into account the discounting of the salvage value.

$$+ \sum_{t,p \in teg} [OBJSIC_{r,t,p} \times VAR\_IC_{r,t,p}]$$

### EQ_OBJINV(r,cur)

*- see EQ_OBJINV in section 5.2.2 for a general description without ETL*

**Description:** Regional investment cost part of objective function adjusted to include the endogenously determined investment cost (VAR_IC) for new investments in learning technologies.

**Purpose and Occurrence:** The objective function part calculating the investment costs is changed (for learning technologies only) by replacing the traditional calculation of discounted cost of investments in new capacity with that of the endogenously determined value. This equation is generated for each region where the learning investment costs occur in each time period beginning from the period, for which the ETL technology is available.

**Equation**

$$EQ\_OBJINV_{r,cur}$$

All the basic objective function terms for investment costs (section 5.2.2)

$$...$$

The calculated investments costs associated with the ETL technologies.

$$+ \sum_{t, p \in teg} [DISC_{r,t,p} \times VAR\_IC_{r,t,p}]$$
