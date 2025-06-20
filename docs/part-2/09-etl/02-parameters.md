# Sets, Switches and Parameters

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

[^42]: Parameters that occur in the ETL-specific equations but that also occur in non-ETL equations (e.g., TCH_LIFE) are not listed in this table.