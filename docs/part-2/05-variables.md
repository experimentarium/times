# Variables

This chapter describes each variable name, definition, and role in the TIMES Linear Program. To facilitate identification of the variables when examining the model's source code, all variable names start with the prefix VAR\_. The value assigned to each variable indexed by some time period, represents the average value in that time period, but the case of VAR_NCAP(v) is an exception, since that variable represents a point-wise investment decided at time period **v**. VAR_NCAP is discussed in detail below.

{numref}`times-variables-by-category` is a list of TIMES variables by category, with brief description of each variable.

**Remarks on {numref}`times-variables-by-category`:**

- Many variables that are related to a process have two period indexes: **t** represents the current period, and **v** represents the vintage of a process, i.e. the period when the investment in that process was decided. For the VAR_NCAP variable, **t** is by definition equal to **v**. For other variables, **t** ≥ **v**, if the process is vintaged (**prc_vint**), i.e., the characteristics of the process depend on the vintage year. If the process is non-vintaged, the characteristics of the capacity of a process are not differentiated by its vintage structure, so that the vintage index is actually not needed for the variables of a non-vintaged process. In these cases, the vintage index **v** is by convention set equal to the period index **t**.
- In {numref}`times-variables-by-category`, the variables are listed according to five categories, depending on what TIMES entity they represent. In the rest of the chapter, the variables are listed and fully described in alphabetical order.
- {numref}`times-variables-by-category` does not list the variables used in the Climate Module, Damage Cost and ETL extensions of TIMES, which are fully documented in Appendices A, B, and C, respectively.
- In the Objective function category, also lists several parameters that stand for certain portions of the objective functions. These are not bona fide GAMS variables, but mostly serve as convenient placeholders for this documentation, and also as useful parameters that may be reported in the solution.

```{list-table} List of TIMES variables by category
:name: times-variables-by-category
:header-rows: 1

* - Category
  - Variable name
  - Brief description
  - DT\*
* - Region related
  - VAR_CUMCST
  - Cumulative amount of regional cost/tax/subsidy
  - ≥0
* - Process related
  - VAR_ACT
  - Annual activity of a process
  - ≥0
* - 
  - VAR_CAP
  - Current capacity of a process, all vintages together
  - ≥0
* - 
  - VAR_NCAP
  - Investment (new capacity) in a process
  - ≥0
* - 
  - VAR_DNCAP
  <br>VAR_SNCAP
  - Binary variable (VAR_DNCAP) and semi-continuous variable (VAR_SNCAP) used with the discrete investment option (see EQ_DSCNCAP)
  - ≥0
* - 
  - VAR_RCAP
  - Retired capacity of a process in a period by vintage
  - ≥0
* - 
  - VAR_SCAP
  - Cumulative retired capacity of a process in a period
  - ≥0
* - 
  - VAR_DRCAP
  - Binary variable for discrete capacity retirements
  - ≥0
* - 
  - VAR_UPS
  - Started-up, shut-down, and off-line capacities
  - ≥0
* - 
  - VAR_UDP
  - Capacity unit dispatching load level variables
  - ≥0
* - Commodity related
  - VAR_BLND
  - Blending variable (for oil refining)
  - ≥0
* - 
  - VAR_COMNET
  - Net amount of a commodity
  - ≥0
* - 
  - VAR_COMPRD
  - Gross production of a commodity (COM_IE applied)
  - ≥0
* - 
  - VAR_CUMCOM
  - Cumulative gross/net production of commodity
  - ≥0
* - 
  - VAR_ELAST
  - Variables used to linearize elastic demand curves
  - ≥0
* - 
  - VAR_GRIDELC
  - Transfer of power between grid nodes and demand nodes in the add-on grid formulation
  - ≥0
* - 
  - VAR_COMAUX
  - Phase angles in the DC power flow formulation
  - ≥0
* - Flow (Process and Commodity) related
  - VAR_FLO
  - Flow of a commodity in or out of a process
  - ≥0
* - 
  - VAR_CUMFLO
  - Cumulative amount of process flow/activity
  - ≥0
* - 
  - VAR_IRE
  - Flow of a commodity in or out of an exchange process (trade variable)
  - ≥0
* - 
  - VAR_SIN/OUT
  - Flow of a commodity in or out of a storage process
  - ≥0
* - Objective function related
  - OBJZ
  - Variable representing the overall objective function (all regions together)
  - free
* - 
  - VAR_OBJ
  - Variable representing objective function by region and main type (OBJINV, OBJFIX, OBJVAR, OBJSAL)
  - ≥0
* - 
  - 
  - *The following 10 parameters are not true variables of the LP matrix*
  - 
* - 
  - OBJR
  - Parameter representing a regional component of the objective function.
  - 
* - 
  - INVCOST
  - Parameter representing the investments portion of a regional component of the objective function
  - 
* - 
  - INVTAXSUB
  - Parameter representing the taxes and subsidies attached to the investments portion of a regional component of the objective function
  - 
* - 
  - INVDECOM
  - Parameter representing the capital cost attached to the dismantling (decommissioning) portion of a regional component of the objective function
  - 
* - 
  - FIXCOST
  - Parameter representing the fixed annual costs portion of a regional component of the objective function
  - 
* - 
  - FIXTAXSUB
  - Parameter representing the taxes and subsidies attached to fixed annual costs of a regional component of the objective function
  - 
* - 
  - VARCOST
  - Parameter representing the variable annual cost portion of a regional component of the objective function
  - 
* - 
  - VARTAXSUB
  - Parameter representing the variable taxes and subsidies of a regional component of the objective function
  - 
* - 
  - ELASTCOST
  - Variable representing the demand loss portion of a regional component of the objective function
  - 
* - 
  - LATEREVENUES
  - Parameter representing the late revenue portion of a regional component of the objective function.
  - 
* - 
  - SALVAGE
  - Parameter representing the salvage value portion of a regional component of the objective function
  - 
* - User Constraint related[^38]
  - VAR_UC
  - Variable representing the LHS expression of a user constraint summing over regions (**uc_r_sum**), periods (**uc_t_sum**) and timeslices (**uc_ts_sum**).
  - free
* - 
  - VAR_UCR
  - Variable representing the LHS expression of a user constraint summing over periods (**uc_t_sum**) and timeslices (**uc_ts_sum**) and being generated for the regions specified in **uc_r_each**.
  - free
* - 
  - VAR_UCT
  - Variable representing the LHS expression of a user constraint summing over regions (**uc_r_sum**) and timeslices (**uc_ts_sum**) and being generated for the periods specified in **uc_t_each**.
  - free
* - 
  - VAR_UCRT
  - Variable representing the LHS expression of a user constraint summing over timeslices (**uc_ts_sum**) and being generated for the regions specified in **uc_r_each** and periods in **uc_t_each**.
  - free
* - 
  - VAR_UCTS
  - Variable representing the LHS expression of a user constraint summing over regions (**uc_r_sum**) and being generated for the periods specified in **uc_t_each** and timeslices in **uc_ts_each**.
  - free
* - 
  - VAR_UCRTS
  - Variable representing the LHS expression of a user constraint summing over periods being generated for the regions specified in **uc_r_each**, the periods in **uc_t_each** and timeslices in **uc_ts_each**.
  - free
* - Miscellaneous
  - 
  - 
  - 
* - Load levels
  - VAR_RLD
  - Power load levels by user-defined supply category. Used in the residual load and ABS extensions.
  - ≥0
```

> \* DT = Default Type of variable: either ≥0 or free

**<ins>Notation for indexes</ins>**: The following indexes are used in the remainder of this chapter:

**r, r'** = region; **v** = vintage; **t, t'** = time period; **y** = year; **p** = process; **c, c'** = commodity; **s**, **s'** = timeslice; **ie** = import or export; ***l*** = sense of a constraint (≥, =, or ≤). In addition, some indexes (**u; ble; opr; j; uc_n**) are used for specific variables only and are defined in their context.

## $VAR\_ACT(r,v,t,p,s)$

> **Definition:** the overall activity of a process. VAR_ACT is defined by the EQ_ACTFLO equation either as the sum of outflows or as the sum of inflows of a particular (user selected) group of commodities, adequately normalized. If the process is not vintaged, the vintage index **v** is by convention set equal to the period index **t**.
>
> **Role:** reports the activity of a process and implicitly defines how the capacity is measured, since the activity is bounded by the available capacity in the constraint EQ(*l*)\_CAPACT, e.g. if the activity of a coal power plant is defined over its electricity output, the capacity is measured in terms of the output commodity, e.g. $MW_{electric}$. Similarly, if the activity variable represents the input flow of coal, the capacity of the coal plant is measured in terms of the input commodity, e.g. $MW_{coal}$.
>
> **Bounds:** Can be directly bounded by ACT_BND
>
> **User constraints:** Can be directly referred to by UC_ACT

## $VAR\_BLND(r,ble,opr)$

> **Definition:** amount of the blending stock **opr** in energy, volume or weight units needed for the production of the blending product **ble** in oil refinery modeling.
>
> **Role:** used for specifying constraints on quality of the various refined petroleum products.
>
> **Bounds:** Cannot be bounded.
>
> **User constraints:** Cannot be referred to in user constraints.

## $VAR\_CAP(r,t,p)$

> **Definition:** the installed capacity in place in any given year **t**, of all vintages of a process determined by the equation EQ(*l*)\_CPT. The variable is equal to the sum of all previously made investments in new capacity, plus any remaining residual capacity installed before the modeling horizon, that has not yet reached the end of its technical lifetime, and minus any capacity that has been retired early.
>
> **Role:** Its main purpose is to allow the total capacity of a process to be bounded. The variable is only created when

- capacity bounds (CAP_BND) for the total capacity installed are specified. In case only one lower or one upper capacity bound is specified, the variable is not generated, but the bound is directly used in the EQ(l)\_CPT constraint.
- the capacity variable is needed in a user constraint, or
- the process is a learning technology (**teg**) in case that endogenous technological learning is used.

> **Bounds:** Can be directly bounded by CAP_BND
>
> **User constraints:** Can be directly referred to by UC_CAP

## $VAR\_COMNET(r,t,c,s)$

> **Definition:** the net amount of a commodity at period **t**, timeslice **s**. It is equal to the difference between amount procured (produced plus imported) minus amount disposed (consumed plus
> exported).
>
> **Role:** The variable is only created if a bound is imposed, or a cost is explicitly associated with the net level of a commodity.
>
> **Bounds:** Can be directly bounded by COM_BNDNET
>
> **User constraints:** Can be directly referred to by UC_COMNET

## $VAR\_COMPRD(r,t,c,s)$

> **Definition:** the amount of commodity **c** procured at time period **t**, timeslice **s**, after applying the commodity efficiency COM_IE.
>
> **Role:** this variable is only created if a bound is imposed on total production of a commodity, or a cost is explicitly associated with production level of a commodity. The variable is defined through the equation EQE_COMPRD.
>
> **Bounds:** Can be directly bounded by COM_BNDPRD
>
> **User constraints:** Can be directly referred to by UC_COMPRD

## $VAR\_CUMCOM(r,c,type,y1,y2)$

> **Definition:** the cumulative amount of commodity **c** produced in region **r** between years **y1** and **y2**, over all timeslices. The **type** indicator (PRD/NET) distinguishes between gross and net production.
>
> **Role:** this variable is only created if a bound is imposed on cumulative gross/net production of a commodity. The variable is defined through the equations EQ_CUMPRD and EQ_CUMNET.
>
> **Bounds:** Can be directly bounded by COM_CUMNET/ COM_CUMPRD
>
> **User constraints:** Can be directly referred to by UC_CUMCOM

## $VAR\_CUMCST(r, y1,y2,costagg,cur)$

> **Definition:** the cumulative amount of costs/taxes/subsidies according to the aggregation **costagg** in region **r** between years **y1** and **y2**, over all timeslices. The available cost aggregations are identified by the pre-defined members of the fixed index set **costagg**.
>
> **Role:** this variable is only created if a bound is imposed on the cumulative amount of regional costs, taxes, and/or subsidies. The variable is defined through the equation EQ_BNDCST.
>
> **Bounds:** Can be directly bounded by REG_CUMCST
>
> **User constraints:** Cannot be referred to in user constraints

## $VAR\_CUMFLO(r,p,c,y1,y2)$

> **Definition:** the cumulative amount of flow in commodity **c** by process **p** in region **r** between years **y1** and **y2**, over all timeslices. With the commodity name **c=**\'ACT\' (reserved system label), the variable represents the cumulative amount of process activity.
>
> **Role:** this variable is only created if a bound is imposed on the cumulative amount of process flow or activity. The variable is defined through the equation EQ_CUMFLO.
>
> **Bounds:** Can be directly bounded by FLO_CUM / ACT_CUM
>
> **User constraints:** Can be directly referred to by UC_CUMFLO/UC_CUMACT

## $VAR\_DNCAP(r,t,p,u)$ / $VAR\_SNCAP(r,t,p)$

> **Definition:** VAR_DNCAP is only used for processes selected by the user as being discrete, i.e. for which the new capacity in period **t** may only be equal to one of a set of discrete sizes, specified by the user. For such processes, VAR_DNCAP is a binary decision variable equal to 1 if the investment is equal to size **'u'** and 0 otherwise. Thanks to an additional constraint, only one of the various potential sizes allowed for the investment at period **t** is indeed allowed.
>
> VAR_SNCAP is only used for processes selected by the user as having semi-continuous amounts of new capacity, i.e. for which new capacity in period **t** may only be zero or between positive lower and upper bounds specified by the user.
>
> **Role:** useful to mathematically express the fact that investment in process **p** at period **t** may only be done in discrete or semi-continuous sizes. See equation EQ_DSCNCAP in Chapter 6.
>
> **Bounds:** Direct bounding not available, indirectly by NCAP_BND
>
> **User constraints:** Not available

## $VAR\_DRCAP(r,v,t,p,j)$

> **Definition:** this variable is used only for processes selected by the user as having discrete early capacity retirements, i.e. for which the retirement at period **t** may only be a multiple of a block size, specified by the user. For such processes, VAR_DRCAP is an integer decision variable equal to the number of blocks retired.
>
> **Role:** needed for mathematically expressing the fact that early retirement in capacity of process **p** at period **t** may only be done in discrete amounts. See equation EQ_DSCRET in Chapter 6.
>
> **Bounds:** Direct bounding not available, indirectly by RCAP_BND
>
> **User constraints:** Not available

## $VAR\_ELAST(r,t,c,s,j,l)$

> **Definition:** these variables are defined whenever a demand is declared to be price elastic. These variables are indexed by **j**, where **j** runs over the number of steps used for discretizing the demand curve of commodity **c** (**c** = energy service only). The $j^{th}$ variable stands for the portion of the demand that lies within discretization interval **j**, on side ***l*** (***l*** indicates either increase or decrease of demand w.r.t. the reference case demand). Each ELAST variable is bounded upward via virtual equation EQ_BNDELAS.
>
> **Role:** Each elastic demand is expressed as the sum of these variables. In the objective function, these variables are used to bear the cost of demand losses as explained in Part I, Chapter 4.
>
> **Bounds:** Direct bounding not available, indirectly by COM_VOC/COM_STEP
>
> **User constraints:** Not available

## $VAR\_FLO(r,v,t,p,c,s)$

> **Definition**: these variables stand for the individual commodity flows in and out of a process. If the process is not vintaged, the vintage index **v** is by convention set equal to the period index **t**.
>
> **Role**: The flow variables are the fundamental quantities defining the detailed operation of a process. They are used to define the activity of a process (VAR_ACT) in a user chosen manner. They are also essential for expressing various constraints that balance the flows of a commodity, or that control the flexibility of processes.
>
> **Bounds:** Can be directly bounded by FLO_BND
>
> **User constraints:** Can be directly referred to by UC_FLO

## $VAR\_IRE(r,v,t,p,c,s,ie)$

> **Definition: t**he inter-regional exchange variable (i=IMPort, e=EXPort) that tracks import (**ie**=i) or export (**ie**=e) of a commodity between region **r** and other regions. The region(s) **r'** trading with **r** is (are) not specified via this variable, but rather via the process(es) **p** through which the import/export is accomplished. The topology set **top_ire(r,c,r',c',p)** of an exchange process indicates the (single) region **r'** with which region **r** is trading commodity **c** (which may have a different name **c'** in region **r')**. Each trade process may trade more than one commodity. Otherwise, VAR_IRE operates in a manner similar to VAR_FLO for conventional processes. An option exists for trading with an external region that is not modeled explicitly (exogenous trading). If the process is not vintaged, the vintage index **v** is by convention set equal to the period index **t**.
>
> **Role:** the role of an IRE variable is to embody the amount of a commodity in or out of a trading process.
>
> **Bounds:** Can be bounded by IRE_BND (directly for bilateral trade)
>
> **User constraints:** Can be directly referred to by UC_IRE

## $VAR\_NCAP(r,v,p)$

> **Definition:** the amount of new capacity (or what has traditionally been called "investment" in new capacity, or capacity build-up) at period **v**. As will be explained in Section 6.2.2, VAR_NCAP represents the total investment in technology **p** at period **v** only when ILED+TLIFE ≥ D(v), where D(v) is the period length. And, as discussed further in that Section, when ILED+TLIFE \< D(v), the model assumes that the investment is repeated as many times as necessary within the period so that the life of the last repetition is beyond the end of period **v**. In this case VAR_NCAP represents the capacity level of the single investments. {numref}`repeated-investment-same-period` illustrates a case where the investment is made twice in period **v** (and some capacity still remains after period **v**). The average capacity in period **v** resulting from the investment VAR_NCAP(v) is less than VAR_NCAP(v), due to the delay ILED (it is equal to VAR_NCAP(v)\* D(v)/TLIFE). The average capacity in period **v+1** due to VAR_NCAP(v) is also less than VAR_NCAP(v) because the end of life of the second round of investment occurs before the end of period **v+1**. These adjustments are made in every equation involving VAR_NCAP by the internal parameter COEF_CPT.

 ```{figure} assets/repeated-investment-example.svg
:name: repeated-investment-same-period
:align: center

Example of a repeated investment in same period.
```

> **Role:** The new capacity (i.e. investment) variables are fundamental in defining the investment decisions, and many other quantities derived from it (for instance process capacities). They play a key role in the model structure and intervene in the majority of constraints. They are notably used in equations that define the conservation of capacity and those that tie the activity of a process to its capacity. The omnipresence of VAR_NACP is in part due to the fact that the VAR_CAP variable is not always defined in TIMES, by design. Note that residual capacity, or capacity in place prior to the initial model year, is handled as a constant in place of VAR_NCAP given by the input parameter NCAP_PASTI(y), which describes the investment made prior to the first period in the pastyear **y**.
>
> **Bounds:** Can be directly bounded by NCAP_BND
>
> **User constraints:** Can be directly referred to by UC_NCAP

## $OBJZ(y_0)$ and related variables

> **Definition:** equal to the objective function of the TIMES LP, i.e. the total cost of all regions, discounted to year $y_0$.
>
> **Role:** this is the quantity that is minimized by the TIMES optimizer.
>
> **Remark:** The next 10 'variables' do not directly correspond to GAMS variables. They are used in the documentation (especially Section 6.2) as convenient intermediate placeholders that capture certain portions of the cost objective function. The reader is invited to look at Section 6.2 for detailed explanations on how these various costs enter the composition of the objective function. Most of these 'variables' are defined as reporting parameters that are made available to the VEDA-BE results analyser, as shown in Section 3.3.

### $VAR\_OBJR(r, y_0)$

> **Definition:** equal to the sum of the various pieces of the total cost of region **r** discounted to year $y_0$.
>
> **Role:** this is not a true variable in the GAMS code. It is used only as a convenient placeholder for writing the corresponding portion of the objective function in this documentation. It may also be reported in VEDA-BE.

### $INVCOST(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region **r**, that corresponds to investments.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $INVTAXSUB(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region **r**, that corresponds to investment taxes and subsidies.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $INVDECOM(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region **r**, that corresponds to capital costs linked to decommissioning of a process.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $FIXCOST(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region ***r*,** that corresponds to fixed annual costs.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $FIXTAXSUB(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region ***r*,** that corresponds to taxes and subsidies attached to fixed annual costs.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $VARCOST(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region ***r*,** that corresponds to variable annual costs.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $VARTAXSUB(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region ***r*,** that corresponds to variable annual taxes and subsidies.
>
> **Role:** it is used mainly as a convenient place holder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $ELASTCOST(r,y)$

> **Definition:** equal to the portion of the cost objective for year **y**, region ***r*,** that corresponds to the cost incurred when demands are reduced due to their price elasticity.
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

### $LATEREVENUES(r,$y)

> **Definition:** equal to the portion of the cost objective for year **y**, region ***r***, that corresponds to certain late revenues from the recycling of materials from dismantled processes that occur after the end-of-horizon.
>
> **Role:** this is not a true variable in the GAMS code. It is used only as a convenient placeholder for writing the corresponding portion of the objective function in this documentation. It may also be reported in VEDA-BE as a convenient replacement for the sum of the components of the total cost.

### $SALVAGE(r,y_0)$

> **Definition:** equal to the portion of the cost objective for region *r*, that corresponds to the salvage value of investments and other one-time costs. It is discounted to some base year $y_0$
>
> **Role:** it is used mainly as a convenient placeholder for writing the corresponding portion of the objective function. It may also be reported in VEDA-BE.

## $VAR\_RCAP(r,v,t,p)$

> **Definition:** this variable is used only for processes selected by the user as having early capacity retirements. For such processes, VAR_RCAP represents the amount of capacity of vintage **v** retired in period **t**.
>
> **Role:** introduced for supporting bounds on the amount of retired capacity of process **p** and vintage **v** in period **t**.
>
> **Bounds:** Can be directly bounded by RCAP_BND
>
> **User constraints:** Not available

## $VAR\_SCAP(r,v,t,p)$

> **Definition:** this variable is used only for processes selected by the user as having early capacity retirements. For such processes, VAR_SCAP represents the cumulative amount of capacity of vintage **v** retired in periods **tt** ≤ **t**.
>
> **Role:** needed in several TIMES equations for adjusting the overall available capacity of process **p** at period **t** according to the amount of capacity already retired.
>
> **Bounds:** Not directly available; indirectly by RCAP_BND / CAP_BND
>
> **User constraints:** Not available

## $VAR\_SIN/SOUT(r,v,t,p,c,s)$

> **Definition:** flow entering/leaving at period **t** a storage process **p**, storing commodity **c**. The process may be vintaged. If the process is not vintaged, the vintage index **v** is by convention set equal to the period index **t**. For storages between timeslices (**prc_stgtss**) and night-storage devices (**prc_nsttss**) the timeslice index s of the storage flows is determined by the timeslice resolution of the storage (e.g. DAYNITE for a day storage). For a storage operating between periods (**prc_stgips**), the storage flows are always on an annual level and hence the timeslice **s** is then always set to ANNUAL.
>
> **Role:** to store some commodity so that it may be used in a time slice or period different from the one in which it was procured; enters the expressions for the storage constraints.
>
> **Bounds:** Can be directly bounded by STGIN_BND/ STGOUT_BND
>
> **User constraints:** Not directly available; indirectly by using auxiliary storage flows

## $VAR\_UPS(r,v,t,p,s,l)$

> **Definition:** amount of off-line capacity (l=\'N\'), started-up capacity (l=\'UP\'), shut-down capacity (l=\'LO\'), or efficiency losses due to partial loads (l=\'FX\') in period **t** process **p** vintage index **v**.
>
> **Role:** used for modeling capacity dispatching, start-up costs as well as partial load efficiencies, but only when requested so by the user.
>
> **Bounds:** Not available
>
> **User constraints:** Not directly available; in timeslice-dynamic constraints on-line capacity can be referred by UC_CAP, using the ONLINE modifier for CAP

## $VAR\_UDP(r,v,t,p,s,l)$

> **Definition:** amount of on-line capacity by cycling/continuously (l=\'N\'/\'FX\'), or load change due to ramping (l=\'UP\'/\'LO\') in period **t** process **p** vintage index **v**.
>
> **Role:** used for modeling capacity dispatching, start-up costs as well as ramping costs, but only when requested so by the user.
>
> **Bounds:** Not available
>
> **User constraints:** Not directly available

## Variables used in User Constraints

The remaining TIMES variables are all attached to user constraints. User constraints are quite flexible, and may involve any of the usual TIMES variables. Two variants of formulating user constraints exist. In the first case a LHS expression, containing expressions involving the different TIMES variables, are bounded by a RHS constant (given by the input parameter UC_RHS(R)(T)(S)). In the second case, the constant on the RHS is replaced by a variable. The bound UC_RHS(R)(T)(S) is then applied to this variable. In the latter case, the user constraints are always generated as strict equalities, while in the first case the equation sign of the user constraint is determined by the bound type.

- Case 1 (RHS constants): \<LHS expression\> ≤/=/≥ UC_RHS(R)(T)(S)
- Case 2 (UC variables): \<LHS expression\> = VAR_UC(R)(T)(S)

These user constraint variables are in fact redundant, but quite useful in providing streamlined expressions constraints (see Chapter 6), and allow for reporting the slack level of each UC. Moreover, in the case of range constraints, they will reduce model size and the amount of input data. By setting the dollar control parameter VAR_UC to YES in the run-file, the variable based formulation is activated (second case). By default, the formulation without user constraint variables will be used, and only the marginals of the equations are reported.

Non-binding user constraints (introduced for reporting purposes) can only be defined when the user constraint variables are used (i.e. VAR_UC == YES).

Each of the listed variables is related to a specific class of user constraint depending on whether the user constraint is created for each period, region, or time slice or only a subset of these indices. In addition, some user constraints are defined for pair of successive time periods (dynamic user constraint or growth constraint). Each variable has at least one index (representing the user constraint **uc_n** for which this variable is defined), and may have up to three additional indexes among **r**, **t**, and **s**.

### $VAR\_UC(uc\_n)$

Variable representing the LHS expression of the user constraint EQE_UC(uc_n) summing over regions (**uc_r_sum**), periods (**uc_t_sum**) and timeslices (**uc_ts_sum**).

### $VAR\_UCR(uc\_n,r)$

Variable representing the LHS expression of the user constraint EQE_UCR(r,uc_n) summing over periods (**uc_t_sum**) and timeslices (**uc_ts_sum**) and being generated for the regions specified in **uc_r_each**.

### $VAR\_UCT(uc\_n,t)$

Variable representing the LHS expression of the user constraint EQE_UCT(uc_n,t) and the combined LHS--RHS expression of the user constraint EQE_UCSU(uc_n,t), summing over regions (**uc_r_sum**) and timeslices (**uc_ts_sum**) and being generated for the periods specified in **uc_t_each/uc_t_succ**.

### $VAR\_UCRT(uc\_n,r,t)$

Variable representing the LHS expression of the user constraint EQE_UCRT(r,uc_n,t) and the combined LHS--RHS expression of the user constraint EQE_UCRSU(r,uc_n,t), summing over timeslices (**uc_ts_sum**) and being generated for the regions specified in **uc_r_each** and periods in **uc_t_each/uc_t_succ**.

### $VAR\_UCTS(uc\_n,t,s)$

Variable representing the LHS expression of the user constraint EQE_UCTS(uc_n,t,s) and the combined LHS--RHS expression of the user constraint EQE_UCSUS(uc_n,t,s), summing over regions (**uc_r_sum**) and being generated for the periods specified in **uc_t_each/uc_t_succ** and timeslices in **uc_ts_each**.

### $VAR\_UCRTS(uc\_n,r,t,s)$

Variable representing the LHS expression of the user constraint EQE_UCRTS(r,uc_n,t,s) and the combined LHS--RHS expression of the user constraint EQE_UCRSUS(r,uc_n,t,s), being generated for the regions speci­fied in **uc_r_each**, the periods in **uc_t_each/uc_t_succ** and the timeslices in **uc_ts_each**.
