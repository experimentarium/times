# Core TIMES Model: A simplified description of the Optimization Program (variables, objective, constraints)

This chapter contains a simplified formulation of the core TIMES Linear Program.

Mathematically, a TIMES instance is a Linear Program, as was mentioned in the previous chapter. A Linear Program (LP for short) consists in the minimization or maximization of an *objective function* (defined as a linear mathematical expression of *decision variables)*, subject to linear *constraints,* also called *equations*[^26].

Very large instances of Linear Programs involving sometimes millions of constraints and variables may be formulated using modern modeling languages such as [GAMS](http://www.gams.com), and solved via powerful Linear Programming *optimizers*[^27]. The Linear Program described in this chapter is much simplified, since it ignores many exceptions and complexities that are not essential to a basic understanding of the principles of the model. Chapter 14 gives additional details on general Linear Programming concepts. The full details of the parameters, variables, objective function, and constraints of TIMES are given in Part II of this documentation (sections 3, 5, and 6).

A linear optimization problem formulation consists of three types of entities:
- *the decision variables:* i.e. the unknowns, or endogenous quantities, to be determined by the optimization;
- *the objective function*: expressing the criterion to be minimized or maximized; and;
- *the constraints*: equations or inequalities involving the decision variables that must be satisfied by the optimal solution.

## Indices

The model data structures (sets and parameters), variables and equations use the following indices:

> $r$: indicates the region
>
> $t$ or $v$: time period; $t$ corresponds to the current period, and $v$ is used to indicate the vintage year of an investment. When a process is not vintaged then $v = t$.
>
> $p$: process (technology)
>
> $s$: time-slice; this index is relevant only for user-designated commodities and processes that are tracked at finer than annual level (e.g. electricity, low-temperature heat, and perhaps natural gas, etc.). Time-slice defaults to "ANNUAL", indicating that a commodity is tracked only annually.
>
> $c$: commodity (energy, material, emission, demand).

## Decision variables

The decision variables represent the *choices* to be made by the model, i.e. the *unknowns*. All TIMES variables are prefixed with the three letters VAR followed by an underscore.

**Important remark**: There are two possible choices concerning the very *meaning* of some decision variables, namely those variables that represent yearly flows or process activities. In the original TIMES formulation, the activity of a process during some period $t$ is considered to be constant in all years constituting the period. This is illustrated in panel M.a of {numref}`process-act-original-TIMES-linear-variant`). In the alternative option the activity variable is considered to represent the value *in a milestone year* of each period, and the values at all other years is linearly interpolated between the consecutive milestone year values, as illustrated in panel M.b). A milestone year is chosen close to the middle of a period. This second option is similar to that of the EFOM and the MESSAGE models. The user is free to choose either option. The constraints and objective function presented below apply to the first option (constant value of activity variables within a period). Appropriate changes in constraints and objective function are made for the alternative option, as explained in section 5.5, and more completely in Part II, section 6.

The main kinds of decision variables in a TIMES model are:

$VAR\_NCAP(r,v,p)$: new capacity addition (investment) for technology $p$, in period $v$ and region $r$. For all technologies the $v$ value corresponds to the vintage of the process, i.e. year in which it is invested in. For vintaged technologies (declared as such by the user) the vintage ($v$) information is reflected in other process variables, discussed below. Typical units are PJ/year for most energy technologies, Million tonnes per year (for steel, aluminum, and paper industries), Billion vehicle-kilometers per year (B-vkm/year) or million cars for road vehicles, and GW for electricity equipment (1GW=31.536 PJ/year), etc.

```{figure} assets/image15.png
:name: process-act-original-TIMES-linear-variant
:align: center
Process activity in the original TIMES formulation (top) and Linear variant (bottom)
```

$VAR\_RCAP(r,v,t,p)$: Amount of capacity that is newly retired at period $t$. The new retirements will reduce the available capacity of vintage $v$ in period $t$ and in all successive periods $t_i > t$ by the value of the variable. This new feature was not available in early versions of TIMES. Note carefully that the feature must be activated by a special switch in order to become effective. Note also that additional a new advanced feature allows the user to specify that capacity retirement may only occur in lump amounts that are either equal to the entire remaining capacity or equal to a multiple of some user defined block. Consult the separate technical note *TIMES Early Retirement of Capacity* for details.

$VAR\_DRCAP(r,v,t,p,j)$: Binary variables used in formulating the special early retirement equations. Two variables may be defined, one when retirement must be for the entire remaining capacity ($j=1$), another when retirement must be a multiple of some block defined by the user via parameter $RCAP\_BLK$ ($j=2$).

$VAR\_SCAP(r,v,t,p)$: Total amount of capacity that has been retired at period $t$ and periods preceding $t$ (see above $VAR\_RCAP$ paragraph).

$CAP(r,v,t,p)$: installed capacity of process $p$, in region $r$ and period $t$, optionally with vintage $v$. It represents the total capacity available at period $t$, considering the residual capacity at the beginning of the modeling horizon and adding to it new investments made prior to and including period $t$ that have not reached their technical lifetime, and subtracting retired capacity. Typical units: same as investments. The $CAP$ quantity, although convenient for formulation and reporting purposes, is in fact *not explicitly defined in the model*, but is derived from the $VAR\_NCAP$ variables and from data on past investments, process lifetimes, and any retirements.

$VAR\_CAP(r,t,p)$: total installed capacity of technology $p$, in region $r$ and period $t$, all vintages together. The $VAR\_CAP$ variables are only defined when some bounds or user-constraints are specified for them. They do not enter any other equation.

<ins>Remark</ins>: The lumpy investment option. There is a TIMES feature that allows the user to impose that new additions to capacity may only be done in predefined blocks. This feature may be useful for technologies that are implementable only in discrete sizes such as a nuclear plant, or a large hydroelectric project. The user should however be aware that using this option voids some of the economic properties of the equilibrium. This feature is described in Chapter 10 of this part of the documentation.

$VAR\_ACT(r,v,t,p,s)$: activity level of technology $p$, in region $r$ and period $t$ (optionally vintage $v$ and time-slice $s$). Typical units: PJ for all energy technologies. The $s$ index is relevant only for processes that produce or consume commodities specifically declared as time-sliced. Moreover, it is the process that determines which time slices prevail. By default, only annual activity is tracked.

$VAR\_FLO(r,v,t,p,c,s)$: the quantity of commodity $c$ consumed or produced by process $p$, in region $r$ and period $t$ (optionally with vintage $v$ and time-slice $s$). Typical units: PJ for all energy technologies. The $VAR\_FLO$ variables confer considerable flexibility to the processes modeled in TIMES, as they allow the user to define flexible processes for which input and/or output flows are not rigidly linked to the process activity.

$VAR\_SIN(r,v,t,p,c,s)/VAR\_SOUT(r,v,t,p,c,s)$: the quantity of commodity $c$ stored or discharged by storage process $p$, in time-slice $s$, period $t$ (optionally with vintage $v$), and region $r$.

$VAR\_IRE(r,v,t,p,c,s,exp)$ and $VAR\_IRE(r,v,t,p,c,s,imp)$[^28]: quantity of commodity $c$ (PJ per year) sold ($exp$) or purchased ($imp$) by region $r$ through export (resp. import) process $p$ in period $t$ optionally in time-slice $s$). Note that the topology defined for the exchange process $p$ specifies the traded commodity $c$, the region $r$, and the regions $r'$ with which region $r$ is trading commodity $c$. In the case of bi-lateral trading, if it is desired that region $r$ should trade with several other regions, each such trade requires the definition of a separate bi-lateral exchange process. Note that it is also possible to define multi-lateral trading relationships between region $r$ and several other regions $r'$ by defining one of the regions as the common market for trade in commodity $c$. In this case, the commodity is 'put on the market' and may be bought by any other region participating in the market. This approach is convenient for global commodities such as emission permits or crude oil. Finally, exogenous trading may also be modeled by specifying the $r'$ region as an external region. Exogenous trading is required for models that are not global, since exchanges with non-modeled regions cannot be considered endogenous.

$VAR\_DEM(r,t,d)$: demand for end-use energy service $d$ in region $r$ and period $t$. It is a true variable, even though in the reference scenario, this variable is fixed by the user. In alternate scenarios however, $VAR\_DEM(r,t,d)$ may differ from the reference case demand due to the responsiveness of demands to their own prices (based on each service demand's own-price elasticity). Note that in this simplified formulation, we do not show the variables used to decompose $DEM(r,t,d)$ into a sum of step-wise quantities, as was presented in chapter 4.

*Other variables:* Several options that have been added to TIMES over the successive versions require the definition of additional variables. They are alluded to in the sections describing the new options, and described more precisely in Part II, and in additional technical notes. Also, TIMES has a number of commodity related variables that are not strictly needed but are convenient for reporting purposes and/or for applying certain bounds to them. Examples of such variables are: the total amount produced of a commodity ($VAR\_COMPRD$), or the total amount consumed of a commodity ($VAR\_COMCON$).

*<ins>Important remark</ins>*: It is useful to know that many variables (for instance the above two accounting variables, but also the flow variables described earlier) add only a moderate computational burden to the optimization process, thanks to the use of a *reduction algorithm* to detect and eliminate redundant variables and constraints before solving the LP. These variables and constraints are later reinstated in the solution file for reporting purposes.

## TIMES objective function: discounted total system cost

### The costs accounted for in the objective function

The Surplus Maximization objective is first transformed into an equivalent Cost Minimization objective by taking the negative of the surplus, and calling this value the *total system cost*. This practice is in part inspired from historical custom from the days of the fixed demand MARKAL model. The TIMES objective is therefore to minimize the total \'cost\' of the system, properly augmented by the 'cost' of lost demand. All cost elements are appropriately discounted to a user-selected year.

In TIMES, the cost elements are defined at a finer level than the period. While the TIMES constraints and variables are linked to a *period*, the components of the system cost are expressed for each *year* of the horizon (and even for some years outside the horizon). This choice is meant to provide a smoother, more realistic rendition of the stream of cost payments in the energy system, as discussed below. Each year, the total cost includes the following elements:

- *Capital Costs* incurred for *investing* into and/or *dismantling* processes.
- Fixed and variable annual *Operation and Maintenance (O&M) Costs, and other annual costs occurring during the dismantling of technologies.
- Costs incurred for *exogenous imports* and for domestic resource *extraction* and *production*. An exogenous import is one that imported from a non-specified entity, i.e. not from another modeled region. Exogenous imports are not relevant in global TIMES instances.
- Revenues from exogenous *export.* An exogenous export is one that is exported to a non-specified entity, i.e. not to another modeled region. Exogenous exports are irrelevant in global TIMES instances. Exogenous export earnings are revenues and appear with a negative sign in the cost expressions.
- *Delivery* costs for commodities consumed by the processes. These costs are attached to commodity flows.
- *Taxes* and *subsidies* associated with commodity flows and process activities or investments. A tax is not a cost *per se*. However, since the tax is intended to influence the optimization, it is considered as an integral part of the objective function. It is however reported separately from regular costs. Similarly for subsidies.
- *Revenues from recuperation of embedded commodities,* accrued when a process's dismantling releases some valuable commodities.
- *Damage costs* (if defined) due to emissions of certain pollutants. Several assumptions are made: the damage costs in region $r$ result from emissions in $r$ and possibly in other regions; damage cost is imputed to the emitting region (polluter pays); emissions in period $t$ entail damages in period $t$ only; the damage cost from several types of emission is assumed to be the sum of the costs from each emission type (no cross-effect); and the damage function linking cost DAM to emissions EM is a power function of the form:

$$DAM(EM) = MC_{0} \times \frac{EM^{\beta + 1}}{(\beta + 1) \times EM_{0}^{\beta}}$$

> Where $\beta$ is non-negative (i.e. marginal damage costs are non decreasing). Hence, the damage cost function is linear ($\beta = 0$) or non linear but convex ($\beta > 0$). Therefore, the same linearization procedure that was used for the surplus may be applied here in order to linearize the damage cost[^29]. Appendix B of Part II and Technical note \"TIMES Damage\", explain how to declare the various parameters required to define the damage functions, to specify the linearization parameters, and to define the switches used to control the optimization. It should be noted that global emissions such as GHG\'s should not be treated via this feature but rather should make use of the Climate Module option described in chapter 7.

- *Salvage value* of processes and embedded commodities at the end of the planning horizon. This revenue appears with a negative sign in the cost expressions. It should also be stressed that the calculation of the salvage value at the end of the planning horizon is very complex and that the original TIMES expressions accounting for it contained some biases (over- or under-estimations of the salvage values in some cases). These biases have been corrected in the present version of TIMES as explained in sections 5.3.4 and 5.5.
- *Welfare loss* resulting from reduced end-use demands. Chapter 4 has presented the mathematical derivation of this quantity.

### Cash flow tracking

As already mentioned, in TIMES, special care is taken to precisely track the cash flows related to process investments and dismantling in each year of the horizon. Such tracking is made complex by several factors:
- First, TIMES recognizes that there may be a lead-time (ILED) between the beginning and the end of the construction of some large processes, thus spreading the investment installments over several years. A recent TIMES feature allows the definition of a negative lead-time, with the meaning that the construction of the technology starts before the year the investment decision is made (this is useful for properly accounting for interest during construction, and is especially needed when using the time-stepped version of TIMES described in chapter 9.)
- Second, TIMES also recognizes that for some other processes (e.g. new cars), the investment in new capacity occurs *progressively* over the years constituting the time period (whose length is denoted by $D(t)$), rather than in one lumped amount.
- Third, there is the possibility that a certain investment decision made at period $t$ will have to be repeated more than once during that same period. (This will occur if the period is long compared to the process technical life.)
- Fourth, TIMES recognizes that there may be dismantling capital costs at the end-of-life of some processes (e.g. a nuclear plant), and that these costs, while attached to the investment variable indexed by period $t$, are actually incurred much later.
- Finally, TIMES permits the payment of any capital cost to be spread over an *economic life (ELIFE)* that is different from the *technical life (TLIFE)* of the process. Furthermore it may be annualized at a different rate than the overall discount rate.

To illustrate the above complexities, we present a diagram taken from Part II that pictures the yearly investments and yearly outlays of capital in one particular instance where there is no lead time and no dismantling of the technology, and the technical life of the technology does not exceed the period length. There are 4 distinct such instances, discussed in detail in section 6.2 of Part II.

```{figure} assets/image16.png
:name: year-inv-tracking-case
:align: center
Illustration of yearly investments and payments for one of four investment tracking cases.
```

### Aggregating the various costs

The above considerations, while adding precision and realism to the cost profile, also introduce complex mathematical expressions into the objective function. In this simplified formulation, we do not provide much detail on these complex expressions, which are fully described in section 6.2 of Part II. We limit our description to giving general indications on the cost elements comprising the objective function, as follows:
- The capital costs (investment and dismantling) are first transformed into streams of annual payments, computed for each year of the horizon (and beyond, in the case of dismantling costs and recycling revenues), along the lines presented above.
- A *salvage value* of all investments still active at the end of the horizon (EOH) is calculated as a lump sum revenue which is subtracted from the other costs and assumed to be accrued in the (single) year following the EOH.[^30]It is then discounted to the user selected reference year.
- The other costs listed above, which are all annual costs, are added to the annualized capital cost payments, to form the $ANNCOST$ quantity below.

TIMES then computes for each region a total net present value of the stream of annual costs, discounted to a user selected reference year. These regional discounted costs are then aggregated into a single total cost, which constitutes the objective function to be minimized by the model in its equilibrium computation.

$$NPV = \sum_{r = 1}^{R}{}\sum_{y \in YEARS}^{}{(1 + d_{r,y})^{REFYR - y} \times ANNCOST(r,y)}$$

where:
> $NPV$ is the net present value of the total cost for all regions (the TIMES objective function);
>
> $ANNCOST(r,y)$ is the total annual cost in region $r$ and year $y$;
>
> $d_{r,y}$ is the general discount rate;
>
> $REFYR$ is the reference year for discounting;
>
> $YEARS$ is the set of years for which there are costs, including all years in the horizon, plus past years (before the initial period) if costs have been defined for past investments, plus a number of years after EOH where some investment and dismantling costs are still being incurred, as well as the Salvage Value; and
>
> $R$ is the set of regions in the area of study.

As already mentioned, the exact computation of $ANNCOST$ is quite complex and is postponed until section 6.2 of PART II

### Variants for the objective function

There are some cases where the standard formulation described above leads to small distortions in the cost accounting between capacity-related costs and the corresponding activity-related costs. This occurs even without discounting but may be increased by discounting. These distortions may occur at the end of the model horizon, either due to excessive or deficient salvage value.

In addition to these cost accounting problems at the end of horizon, the investment spreads used in the standard formulation can also lead to other cost distortions, regardless of discounting. In very long periods, the investment spreads are divided into $D_t$ successive steps, each amounting to $1/D_t$ of the total capacity to be invested in the period. Recall that the full capacity must be in place by the milestone year, in order to allow activity to be constant over the period. For example, if the period length $D_t$ is 20 years, the investments start already 19 years before the milestone year, and can thus start *even before the previous milestone year. If the investment costs are changing over time, it is clear that in such cases the costs will not be accounted in a realistic way, because the investment cost data is taken from the start year of each investment step.*

Similarly, in short periods the investment costs are spread over only a few years, and if the previous period is much longer, this can leave a considerable gap in the investment years between successive periods. Here again, if the investment costs are changing over time, this would lead to a distortion in the cost accounting.

Unfortunately, it is a well-known fact that the original choice of defining milestone years at or near the middle of each period limits the choice of milestone years, and furthermore tends to induce periods that may be very unequal in length, thus exacerbating the anomalies mentioned above. Such variability in period length can increase the cost distortions under discounting due to the larger differences in the timing of the available capacity (as defined by the investments) and the assumed constant activity levels in each period in the original definition of TIMES variables.

These were remedied by making changes in parts of the **OBJ** cost representation. Four options are now available, three of which apply to the original definition of TIMES variables, the fourth one applying to the alternate definition of TIMES variables. The fourth option (named **LIN**) is discussed separately in section 5.5, since it concerns not only the objective function but also several constraints.

The three options are as follows:
- The original OBJ with minor changes made to it, activated via the **OBLONG** switch.
- The modified objective function (**MOD**). The **MOD** formulation adds only a few modifications to the standard formulation:
	- The model periods are defined in a different way; and
	- The investment spreads in the investment Cases 1a and 1b (see section 6.2 of Part II for a list of all cases) are defined slightly differently.
- The **ALT** formulation includes all the modifications made in the MOD formulation. In addition, it includes the following further modifications that eliminate basically all of the remaining problems in the standard formulation:
	- The investment spreads in the investment Case 1b are defined slightly differently;
	- The capacity transfer coefficients for newly installed capacities are defined slightly differently, so that the effective lifetime of technologies is calculated taking into account discounting;
	- Variable costs are adjusted to be in sync with the available capacity.

It has been observed that these three options yield results that have practically the same degree of accuracy and reliability. There is however an advantage to the MOD and ALT options, as the milestone years need no longer be at the middle of a period.

Additional details and comments are provided on all three options in technical note "TIMES Objective Variants".

<ins>Conclusion on the variants</ins>: The multiplicity of options may confuse the modeler. Extensive experience with their use has shown that the distortions discussed above remain quite small. In practice, old TIMES users seem to stick to the classical OBJ with the OBLONG switch. And, as mentioned above, using MOD allows the further flexibility of freely choosing milestone years. Finally, using the LIN option (described in section 5.5) is a more serious decision, since it implies a different meaning for the TIMES variables; some modelers are more comfortable with this choice, which has also implications for the reporting of results.

## Constraints

While minimizing total discounted cost, the TIMES model must satisfy a large number of constraints (the so-called *equations* of the model) which express the physical and logical relationships that must be satisfied in order to properly depict the associated energy system. TIMES constraints are of several kinds. Here we list and briefly discuss the main types of constraints. A full, mathematically more precise description is given in Part II. If any constraint is not satisfied, the model is said to be *infeasible*, a condition caused by a data error or an over-specification of some requirement.

In the descriptions of the equations that follow, the equation and variable names (and their indexes) are in ***bold italic*** type, and the parameters (and their indexes), corresponding to the input data, are in regular *italic* typeset. Furthermore, some parameter indexes have been omitted in order to provide a streamlined presentation.

### Capacity transfer (conservation of investments)

Investing in a particular technology increases its installed capacity for the duration of the physical life of the technology. At the end of that life, the total capacity for this technology is decreased by the same amount. When computing the available capacity in some time period, the model takes into account the capacity resulting from all investments up to that period, some of which may have been made prior to the initial period but are still in operating condition (embodied by the residual capacity of the technology), and others that have been decided by the model at, or after, the initial period, up to and including the period in question.

The total available capacity for each technology *p,* in region *r*, in period *t* (all vintages),is equal to the sum of investments made by the model in past and current periods, and whose physical life has not yet ended, plus capacity in place prior to the modeling horizon that is still available. The exact formulation of this constraint is made quite complex by the fact that TIMES accepts variable time periods, and therefore the end of life of an investment may well fall in the middle of a future time period. We ignore here these complexities and provide a streamlined version of this constraint. Full details are shown in section 6.3.18 of Part II.

#### $EQ\_CPT(r,t,p)$ -- Capacity transfer

$$VAR\_CAPT(r,t,p) = \sum_{t' \in \{t-t'< LIFE(r,t',p)\}} VAR\_NCAP(r,t',p) + RESID(r,t,p)$$ (5-1)
>
> where $RESID(r,t,p)$ is the (exogenously provided) capacity of technology $p$ due to investments that were made prior to the initial model period and still exist in region $r$ at time $t$.

### Definition of process activity variables

Since TIMES recognizes activity variables as well as flow variables, it is necessary to relate these two types of variables. This is done by introducing a constraint that equates an overall activity variable, $VAR\_ACT(r,v,t,p,s)$, with the appropriate set of flow variables, $VAR\_FLO(r,v,t,p,c,s)$, properly weighted. This is accomplished by first identifying the group of commodities that defines the activity (and thereby the capacity as well) of the process. In a simple process, one consuming a single commodity and producing a single commodity, the modeler simply chooses one of these two flows to define the activity, and thereby the process normalization (input or output). In more complex processes, with several commodities (perhaps of different types) as inputs and/or outputs, the definition of the activity variable requires first to choose the *primary commodity group (pcg)* that will serve as the activity-defining group. For instance, the *pcg* may be the group of energy carriers, or the group of materials of a given type, or the group of GHG emissions, etc. The modeler then identifies whether the activity is defined via inputs or via outputs that belong to the selected *pcg*. Conceptually, this leads to the following relationship:

#### $EQ\_ACTFLO(r,v,t,p,s)$ -- Activity definition

$$VAR\_ACT(r,v,t,p,s) = \sum_{c \in pcg} VAR\_FLO(r,v,t,p,c,s) / ACTFLO(r,v p,c)$$ (5-2)

> where $ACTFLO(r,v,p,c)$ is a conversion factor (often equal to 1) from the activity of the process to the flow of a particular commodity.

### Use of capacity

In each time period the model may use some or all of the installed capacity according to the Availability Factor (AF) of that technology. Note that the model may decide to use *less* than the available capacity during certain time-slices, or even throughout one or more whole periods, if such a decision contributes to minimizing the overall cost. Optionally, there is a provision for the modeler to force specific technologies to use their capacity to their full potential.

For each technology $p$, period $t$, vintage $v$, region $r$, and time-slice $s$, the activity of the technology may not exceed its available capacity, as specified by a user defined availability factor.

#### $EQ\_CAPACT (r,v,t,p,s)$ -- Use of capacity

$$VAR\_ACT(r,v,t,p,s) ≤ or = AF(r,v,t,p,s) \times PRC\_CAPACT(r,p)) \times FR(r,s) \times VAR\_CAP(r,v,t,p)$$ (5-3)

> Here $PRC\_CAPACT(r,p)$ is the conversion factor between units of capacity and activity (often equal to 1, except for power plants). The $FR(r,s)$ parameter is equal to the (fractional) duration of time-slices. The availability factor ***AF*** also serves to indicate the nature of the constraint as an inequality or an equality. In the latter case the capacity is forced to be fully utilized. Note that the ***CAP(r,v,t,p)*** "variable" is not explicitly defined in TIMES. Instead it is replaced in (5-3) by a fraction (less than or equal to 1) of the investment variable $VAR\_NCAP(r,v,p)$[^31] sum of past investments that are still operating, as in equation (5-1).

**<ins>Example</ins>**: a coal fired power plant's activity in any time-slice is bounded above by 80% of its capacity, i.e. $VAR\_ACT(r,v,t,p,s) ≤ 0.8 \times 31.536 \times CAP(r,v,t,p)$, where $PRC\_CAPACT(r,p) = 31.536$ is the conversion factor between the units of the capacity variable (GW) and the activity-based capacity unit (PJ/a) The activity-based capacity unit is obtained from the activity unit(PJ) by division by a denominator of one year.

The $s$ index of the $AF$ coefficient in equation (5-3) indicates that the user may specify time-sliced dependency on the availability of the installed capacity of some technologies, if desirable. This is especially needed when the operation of the equipment depends on the availability of a resource that cannot be stored, such as wind and sun, or that can be only partially stored, such as water in a reservoir. In other cases, the user may provide an $AF$ factor that does not depend on $s$, which is then applied to the entire year. The operation profile of a technology within a year, if the technology has a sub-annual process resolution, is determined by the optimization routine. The number of $EQ\_CAPACT$ constraints is at least equal to the number of time-slices in which the equipment operates. For technologies with only an annual characterization the number of constraints is reduced to one per period (where $s$="ANNUAL").

### Commodity balance equation

In each time period, the production by a region plus imports from other regions of each commodity must balance the amount consumed in the region or exported to other regions. In TIMES, the sense of each balance constraint (**≥** or **=**) is user controlled, via a special parameter attached to each commodity. However, the constraint defaults to an equality in the case of materials (i.e. the quantity produced and imported is *exactly* equal to that consumed and exported), and to an inequality in the case of energy carriers, emissions and demands (thus allowing some surplus production). For those commodities for which time-slices have been defined, the balance constraint must be satisfied in each time-slice.

The balance constraint is very complex, due to the many terms involving production or consumption of a commodity. We present a much simplified version below, to simply indicate the basic meaning of this equation.

For each commodity $c$, time period $t$ (vintage $v$), region $r$, and time-slice $s$ (if necessary or "ANNUAL" if not), this constraint requires that the disposition of each commodity balances its procurement. The disposition includes consumption in the region plus exports; the procurement includes production in the region plus imports.

#### $EQ\_COMBAL(r,t,c,s)$ -- Commodity balance

$$\sum_{p,c \in TOP(r,p,c,out)} VAR\_FLO(r,v,t,p,c,s) + VAR\_SOUT(r,v,t,p,c,s) \times STG\_EFF(r,v,p) + \sum_{p,c \in RPC\_IRE(r,p,c,imp)} VAR\_IRE(r,t,p,c,s,imp) + \sum_{p} Release(r,t,p,c) \times VAR\_NCAP(r,t,p,c) ≥ or = \sum_{p,c \in TOP(r,p,c,in)} VAR\_FLO(r,v,t,p,c,s) + VAR\_SIN(r,v,t,p,c,s) + \sum_{p,c \in RPC\_IRE(r,p,c,exp)} VAR\_IRE(r,t,p,c,s,exp) + \sum_{p} Sink(r,t,p,c) \times VAR\_NCAP(r,t,p,c) + FR(c,s) \times VAR\_DEM(c,t)$$
> (5-4)
> 
> where:
>
> The constraint is ≥ for energy forms and = for materials and emissions (unless these defaults are overridden by the user, see Part II).
> 
> $TOP(r,p,c,in/out)$ identifies that there is an input/output flow of commodity $c$ into/from process $p$ in region $r$;
> 
> $RPC\_IRE(r,p,c,imp/exp)$ identifies that there is an import/export flow into/from region $r$ of commodity $c$ via process $p$;
> 
> $STG\_EFF(r,v,p)$ is the efficiency of storage process $p$;
> 
> $COM\_IE(r,t,c)$ is the infrastructure efficiency of commodity $c$;
> 
> $Release(r,t,p,c)$ is the amount of commodity $c$ recuperated per unit of capacity of process $p$ dismantled (useful to represent some materials or fuels that are recuperated while dismantling a facility);
> 
> $Sink(r,t,p,c)$ is the quantity of commodity $c$ required per unit of new capacity of process $p$ (useful to represent some materials or fuels consumed for the construction of a facility);
> 
> $FR(s)$ is the fraction of the year covered by time-slice $s$ (equal to 1 for non- time-sliced commodities).

**<ins>Example</ins>**: Gasoline consumed by vehicles plus gasoline exported to other regions must not exceed gasoline produced from refineries plus gasoline imported from other regions.

### Defining flow relationships in a process

A process with one or more (perhaps heterogeneous) commodity flows is essentially defined by one or more input and output flow variables. In the absence of relationships between these flows, the process would be completely undetermined, i.e. its outputs would be independent from its inputs. We therefore need one or more constraints stating in a most general case that the ratio of the sum of some of its output flows to the sum of some of its input flows is equal to a constant. In the case of a single commodity in, and a single commodity out of a process, this equation defines the traditional efficiency of the process. With several commodities, this constraint may leave some freedom to individual output (or input) flows, as long as their sum is in fixed proportion to the sum of input (or output) flows. An important rule for this constraint is that *each sum must be taken over commodities of the same type* (i.e. in the same group, say: energy carriers, or emissions, etc.). In TIMES, for each process the modeler identifies the input commodity group $cg1$, and the output commodity group $cg2$, and chooses a value for the efficiency ratio, named $FLO\_FUNC(p,cg1,cg2)$. The following equation embodies this:

#### $EQ\_PTRANS(r,v,t,p,cg1,cg2,s)$ -- Efficiency definition

$$\sum_{c \in cg2} VAR\_FLO(r,v,t,p,c,s) = FLO\_FUNC(r,v,cg1,cg2,s) \times \sum_{c \in cg1} COEFF(r,v,p,cg1,c,cg2,s) \times VAR_FLO(r,v,t,p,c,s)$$ (5-5)

> where $COEFF(r,v,p,cg1,c,cg2,s)$ takes into account the harmonization of different time-slice resolution of the flow variables, which have been omitted here for simplicity, as well as commodity-dependent transformation efficiencies.

### Limiting flow shares in flexible processes

When either of the commodity groups $cg1$ or $cg2$ contains more than one element, the previous constraint allows a lot of freedom on the values of flows. The process is therefore quite flexible. The flow share constraint is intended to limit the flexibility, by constraining the share of each flow within its own group. For instance, a refinery output might consist of three refined products: $c_1$ is light, $c_2$ is medium, and $c_3$ is heavy distillate. If losses are 9% of the input, then the user must specify $FLO\_FUNC = 0.91$ to define the overall efficiency. The user may then want to limit the flexibility of the slate of outputs by means of three $FLO\_SHAR(c_i)$ coefficients, say 0.4, 0.5, 0.6, resulting in three flow share constraints as follows (ignoring some indices for clarity):

> $VAR\_FLO(c_1) ≤ 0.4 \times (VAR\_FLO(c_1) + VAR\_FLO(c_2) + VAR\_FLO(c_3))$, so that $c_1$ is at most 40% of the total output,
>
> $VAR\_FLO(c_2) ≤ 0.5 \times (VAR\_FLO(c_1) + VAR\_FLO(c_2) + VAR\_FLO(c_3))$, so that $c_2$ is at most 50% of the total output,
>
> $VAR\_FLO(c_3) ≤ 0.6 \times (VAR\_FLO(c_1) + VAR\_FLO(c_2) + VAR\_FLO(c_3))$, so that $c_3$ is at most 60% of the total output.

The general form of this constraint is:

$EQ\_INSHR(c,cg,p,r,t,s)$ and $EQ\_OUTSHR(c,cg,p,r,t,s)$

$$VAR\_FLO(c) ≤,≥,= FLO\_SHAR(c) \times \sum_{c' \in cg} VAR\_FLO(c')$$ (5-6)

> The commodity group $cg$ may be on the input or output side of the process.

A recent modification of TIMES simplifies the above constraints by allowing the use of the $VAR\_ACT$ variable instead of the sum of $VAR\_FLO$ variables in equation (5-6) or in similar ones. This simplification is triggered when the user defines the new attribute $ACT\_FLO$, which is a coefficient linking a flow to the activity of a process. Furthermore, commodity $c$ appearing in left-hand-side of the constraint may even be a flow that is not part of the $cg$ group.

<ins>Warning</ins>: It is quite possible (and regrettable) to over specify flow related equations such as (5-6), especially when the constraint is an equality. Such an over specification leads to an infeasible LP. A new feature of TIMES consists in deleting some of the flow constraints in order to re-establish feasibility, in which case a warning message is issued.

### Peaking reserve constraint (time-sliced commodities only)

This constraint imposes that the total capacity of all processes producing a commodity at each time period and in each region must exceed the average demand in the time-slice where peaking occurs by a certain percentage. This percentage is the Peak Reserve Factor, $COM_PKRSV(r,t,c,s)$, and is chosen to insure against several contingencies, such as: possible commodity shortfall due to uncertainty regarding its supply (e.g. water availability in a reservoir); unplanned equipment down time; and random peak demand that exceeds the average demand during the time-slice when the peak occurs. This constraint is therefore akin to a safety margin to protect against random events not explicitly represented in the model. In a typical cold country the peaking time-slice for electricity (or natural gas) will be Winter-Day, and the total electric plant generating capacity (or gas supply plant) must exceed the Winter-Day demand load by a certain percentage. In a warm country the peaking time-slice may be Summer-Day for electricity (due to heavy air conditioning demand). The user keeps full control regarding which time-slices have a peaking equation.

For each time period $t$ and for region $r$, there must be enough installed capacity to exceed the required capacity in the season with largest demand for commodity $c$ by a safety factor $E$ called the *peak reserve factor*.

#### $EQ\_PEAK(r,t,c,s)$ -- Commodity peak requirement

$$\sum_{p,c=pcg} PRC\_CAPACT(r,p) \times Peak(r,v,p,c,s) \times FR(s) \times VAR\_CAP(r,v,t,p) \times VAR\_ACTFLO(r,v,p,c) + \sum_{p,c≠pcg} CAP\_PKCNT(r,v,p,c,s) \times VAR\_FLO(r,v,t,p,c,s) + VAR\_IRE(r,t,p,c,s,i) ≥ (1+ COM\_PKRSV(r,t,c,s))(\sum_{p,c} VAR\_FLO(r,v,t,p,c,s) + VAR\_IRE(r,t,p,c,s,e))$$

where:

> $COM_PKRSV(r,t,c,s)$ is the region-specific reserve coefficient for commodity $c$ in time-slice $s$, which allows for unexpected down time of equipment, for demand at peak, and for uncertain resource availability, and
>
> $NCAP_PKCNT(r,v,p,c,s)$ specifies the fraction of technology $p$'s capacity in a region $r$ for a period $t$ and commodity $c$ (electricity or heat only) that is allowed to contribute to the peak load in slice $s$; many types of supply processes are predictably available during the peak and thus have a peak coefficient equal to 1, whereas others (such as wind turbines or solar plants in the case of electricity) are attributed a peak coefficient less than 1, since they are on average only fractionally available at peak (e.g., a wind turbine typically has a peak coefficient of .25 or .3, whereas a hydroelectric plant, a gas plant, or a nuclear plant typically has a peak coefficient equal to 1).
>
> For simplicity it has been assumed in (5-7) that the time-slice resolution of the peaking commodity and the time-slice resolution of the commodity flows (FLO, TRADE) are the same. In practice, this is not the case and additional conversion factors or summation operations are necessary to match different time-slice levels.

*Remark*: to establish the peak capacity, two cases must be distinguished in constraint ***EQ_PEAK***.
- For production processes where the peaking commodity is the only commodity in the primary commodity group (denoted $c=pcg$), the capacity of the process may be assumed to contribute to the peak.
- For processes where the peaking commodity is not the only member of the pcg, there are several commodities included in the pcg. Therefore, the capacity as such cannot be used in the equation. In this case, the actual production is taken into account in the contribution to the peak, instead of the capacity. For example, in the case of CHP only the production of electricity contributes to the peak electricity supply, not the entire capacity of the plant, because the activity of the process consists of both electricity and heat generation in either fixed or flexible proportions, and, depending on the modeler\'s choice, the capacity may represent either the electric power of the turbine in condensing or back-pressure mode, or the sum of power and heat capacities in back-pressure mode. There is therefore a slight inconsistency between these two cases, since in the first case, a technology may contribute to the peak requirement without producing any energy, whereas this is impossible in the second case.

Note also that in the peak equation (5-7), it is assumed that imports of the commodity are contributing to the peak of the importing region (thus, exports are implicitly considered to be of the *firm power* type).

### Constraints on commodities

In TIMES variables are optionally attached to various quantities related to commodities, such as total quantity produced. Therefore it is quite easy to put constraints on these quantities, by simply bounding the commodity variables in each period. It is also possible to impose cumulative bounds on commodities over more than one period, a particularly useful feature for cumulatively bounding emissions or modeling reserves of fossil fuels. By introducing suitable naming conventions for emissions the user may constrain emissions from specific sectors. Furthermore, the user may also impose global emission constraints that apply to several regions taken together, by allowing emissions to be traded across regions. Alternatively or concurrently a tax or penalty may be applied to each produced (or consumed) unit of a commodity (energy form, emission), via specific parameters.

A specific type of constraint may be defined to limit the share of process (p) in the total production of commodity (c). The constraint indicates that the flow of commodity (c) from/to process (p) is bounded by a given fraction of the total production of commodity (c). In the present implementation, the same given fraction is applied to all time­ slices.

### User constraints

In addition to the standard TIMES constraints discussed above, the user may create a wide variety of so-called User Constraints (UC\'s), whose coefficients follow certain rules. Thanks to recent enhancements of the TIMES code, user defined constraints may involve virtually any TIMES variable. For example, there may a user-defined constraint limiting investment in new nuclear capacity (regardless of the type of reactor), or dictating that a certain percentage of new electricity generation capacity must be powered by a portfolio of renewable energy sources. User constraints may be employed across time periods, for example to model options for retrofitting existing processes or extending their technical lives. A frequent use of UC\'s involves cumulative quantities (over time) of commodities, flows, or process capacities or activities. Recent TIMES code changes make the definition of the right-hand-sides of such UC\'s fairly independent of the horizon chosen for the scenario, and thus make it unnecessary to redefine the RHS\'s when the horizon is changed.

In order to facilitate the creation of a new user constraint, TIMES provides a *template* for indicating a) the set of variables involved in the constraint, and b) the user-defined coefficients needed in the constraint.

The details of how to build different types of UC are included in section 6.4 of Part II of the documentation.

### Growth constraints

These are special cases of UC\'s that are frequently used to maintain the growth (or the decay) of the capacity of a process within certain bounds, thus avoiding excessive abrupt investment in new capacity. Such bounding of the growth is often justified by the reality of real life constraints on technological adoption and evolution. The user is however advised to exert caution on the choice of the maximum rates of technological change, the risk being to restrict it too much and thus \"railroad\" the model.

Typically, a growth constraint is of the following generic form (ignoring several indices for clarity:

$VAR\_CAP(t+1) \leq (1+ GROWTH^{M(t+1)- M(t)}).VAR\_CAP(t) + K$ (5-8)

The $GROWTH$ coefficient is defined as a new attribute of the technology, and represents the maximum annual growth allowed for the capacity. The quantity $M(t+1)-M(t)$ is the number of years between the milestones of periods $t$ and $t+1$. The constant $K$ is useful whenever the technology has no capacity initially, in order to allow capacity to build over time (if $K$ were absent and initial capacity is zero, the technology would never acquire any capacity)

Note that the sign of the constraint may also be of the \"larger than or equal to\" type to express a maximum rate of abandonment, in which case the \"+\" sign is replaced by a \"--\" sign in the right-hand-side of the constraint. Equality is also allowed, but must be used only exceptionally in order to avoid railroading of the model.

### Early retirement of capacity

With this new TIMES feature the user may allow the model to retire some technologies before the end of their technical lives. The retirement may be continuous or discrete. In the former case, the model may retire any amount of the remaining capacity (if any) at each period. In the latter case, the retirement may be effected by the model either in a single block (i.e. the remaining capacity is completely retired) or in multiples of a user chosen block. Please refer to chapter 10 of this document *The lumpy investment option*, for additional discussion of the mathematical formulation of MIP problems.

This feature requires the definition of three new constraints, as listed and briefly described in table 5.1, as well as the alteration of many existing constraints and the objective function, as described in table 5.2 Part II and the special separate note *TIMES Early Retirement of Capacity* provide additional detail.

The user is advised to use the discrete early retirement feature sparingly, as it implies the use of mixed integer programming optimizer, rather than the computationally much more efficient linear programming optimizer. The user should also be aware that using the discrete option voids some of the economic properties of the equilibrium, as discussed in section 10.3.

+--------------------------+-------------------------------------------+
| **New Equation**         | **Description**                           |
+==========================+===========================================+
| EQ_DSCRET(r,v,t,p)       | Discrete retirement equation for process  |
|                          | **p** and vintage **v** in region **r**   |
|                          | and period **t**.                         |
|                          |                                           |
|                          | Plays an analogous role to equation       |
|                          | EQ_DSCNCAP in the Discrete Capacity       |
|                          | Investment Extension.                     |
+--------------------------+-------------------------------------------+
| EQ_CUMRET(r,v,t,p)       | Cumulative retirement equation for        |
|                          | process **p** and vintage **v** in region |
|                          | **r** and period **t**.                   |
+--------------------------+-------------------------------------------+
| EQL_SCAP(r,t,p,ips)      | Maximum salvage capacity constraint for   |
|                          | process **p** in region **r** and period  |
|                          | **t**, defined for **ips** = N (unless    |
|                          | NCAP_OLIFE is specified).                 |
+--------------------------+-------------------------------------------+

*Table 5.1. The new constraints required to implement early retirement of capacity*

+---------------+----------------------+-------------------------------+
| **Existing    | **Equation           | **Purpose of Modification**   |
| Equation**    | Description**        |                               |
+===============+======================+===============================+
| EQ_OBJFIX     | Fixed cost component | To credit back the fixed      |
|               | of objective         | costs of the capacity that is |
|               | function             | retired early                 |
+---------------+----------------------+-------------------------------+
| EQ_OBJVAR     | Variable cost        | To reflect the effect of      |
|               | component of         | capacity that is retired      |
|               | objective function   | early in the costs of         |
|               |                      | capacity-related flows        |
+---------------+----------------------+-------------------------------+
| EQ_OBJSALV    | Salvage cost         | To subtract the salvage value |
|               | component of         | (if any) of capacity that is  |
|               | objective function   | retired early                 |
+---------------+----------------------+-------------------------------+
| E             | Capacity transfer    | To reflect the effect of      |
| Q(**l**)\_CPT | equation             | capacity that is retired      |
|               |                      | early                         |
| for **l** =   |                      |                               |
| L, E, G       |                      |                               |
+---------------+----------------------+-------------------------------+
| EQ(*          | Capacity utilization | To reflect the effect of      |
| *l**)\_CAPACT | equation             | capacity that is retired      |
|               |                      | early                         |
| for **l** =   |                      |                               |
| L, E, G       |                      |                               |
+---------------+----------------------+-------------------------------+
| EQ(*          | Commodity based      | To reflect the effect of      |
| *l**)\_CAFLAC | availability         | capacity that is retired      |
|               | constraint           | early                         |
| for **l** =   |                      |                               |
| L, E          |                      |                               |
+---------------+----------------------+-------------------------------+
| EQ(**         | Commodity balance    | To reflect the effect of      |
| l**)\_COMBAL\ | equation             | capacity that is retired      |
| for **l** =   |                      | early in capacity-related     |
| G, E          |                      | flows                         |
+---------------+----------------------+-------------------------------+
| EQ_PEAK       | Commodity peaking    | To subtract the peak          |
|               | constraint           | contribution of capacity that |
|               |                      | is retired early              |
+---------------+----------------------+-------------------------------+
| EQ(           | The FLO component of | To reflect the effect of      |
| **l**)\_UC\*\ | all user constraints | capacity that is retired      |
| for **l** =   |                      | early in capacity-related     |
| L, E, G       |                      | flows                         |
+---------------+----------------------+-------------------------------+
| EQ(*          | Market share of flow | To reflect the effect of      |
| *l**)\_MRKCON | in the consumption   | capacity that is retired      |
|               | of a commodity       | early in capacity-related     |
| for **l** =   |                      | flows                         |
| L, E, G       |                      |                               |
+---------------+----------------------+-------------------------------+
| EQ(*          | Market share of flow | To reflect the effect of      |
| *l**)\_MRKPRD | in the production of | capacity that is retired      |
|               | a commodity          | early in capacity-related     |
| for **l** =   |                      | flows                         |
| L, E, G       |                      |                               |
+---------------+----------------------+-------------------------------+

*Table 5.2. List of existing constraints that are affected by the early retirement option.*

### Electricity grid modeling

The electricity sector plays a central role in any energy model, and particularly so in TIMES. The electricity commodity has features that present particular challenges for its representation, in that it is difficult to store, and requires a network infrastructure to be transported and delivered. The considerable development of new renewable electricity generation technologies adds to the complexity, inasmuch as the technical requirements of integrating interruptible generation facilities (such as wind turbines and solar plants) to a set of traditional plants, must be satisfied for the integration to be feasible. Such considerations become even more relevant in large regions or countries, where the distances between potential generation areas and consumption areas are quite large.

Such considerations have led to the introduction of an optional grid modeling feature into the TIMES model\'s equations. A grid consists in a network of nodes linked by arcs (or branches). Each node may represent a well-defined geographic area that is deemed distinct from other areas of the region, either because of its generation potential (e.g. a windy area suitable for wind farms) and/or because of a concentration of points of consumption of electricity (e.g. a populated area separated from other populated areas or from generation areas.)

The purpose of this section is to indicate the broad principles and characteristics of the grid representation feature in TIMES. The modeler wishing to implement the feature is urged to read to the detailed Technical Note "TIMES Grid modeling feature", which contains the complete mathematical derivations of the equations, and their implementation in TIMES. What follows is a much streamlined version outlining only the main approach and ignoring the many details of the mathematical equations.

#### A much simplified sketch of the grid constraints

The traditional way to represent the nodes and arcs of a grid is shown in {numref}`grid-connection-nodes`, where each node is shown as a horizontal segment, and the nodes are connected via bi-directional arcs.

```{figure} assets/image17.png
:name: grid-connection-nodes
:align: center
Connection of a grid node with other nodes.
```
The basic energy conservation equation of a grid is as follows:

$G_{i} - L_{i} = \sum_{j = 1}^{M} P_{i,j}$ *for each i=1,2,\...,M*

where:

> $M$ the number of nodes connected with node $i$
> 
> $G_{i}$ active power injected into node $i$ by generators
> 
> $L_{i}$ active power withdrawn from node $i$ by consumer loads
> 
> $P_{i,j}$ branch flow from node $i$ to node $j$

As mentioned above, these constraints are then modified so as to include important technical requirements on the electrical properties (reactance and phase angle) of each line. Suffice it to say here that the resulting new equations remain linear in the flow and other variables.

#### Integrating grid equations into TIMES

It should be clear that the variables $G_{i}$ and $L_{i}$ must be tightly related to the rest of the TIMES variables that concern the electricity commodities. In fact, the modeler must first decide on an allocation of the set of generation technologies into $M$ subsets, each subset being attached to a node of the grid. Similarly, the set of all technologies that consume electricity must also be partitioned into $M$ subsets, each attached to a node. These two partitions are effected via new parameters specifying the fractions of each generation type to be allocated to each grid node, and similarly for the fractions of each technology consuming electricity to be allocated to grid each node. This indeed amounts to a partial regionalization of the model concerning the electricity sector. Thus, variables $G_{i}$ and $L_{i}$ are defined in relation to the existing TIMES variables.

Of course, the introduction of the grid requires modifying the electricity balance equations and peak equations, via the introduction of the net total flow variables the set of grid nodes. The electricity balance equations are modified for each time slice defined for electricity.

Finally, additional a security constraint is added in the case of a multi-regional model, expressing that the total net export or import of electricity from region $r$ does not exceed a certain (user-defined) fraction of the capacity of the portion of the grid linking region $r$ to other regions.

#### Costs

New costs attached to the grid are also modeled, and form a new component of the objective function for the region. For this, a new cost coefficient is defined and attached to each node of the grid. TIMES multiplies this cost coefficient by the proper new grid variables and discounts the expression in order to form the new OBJ component.

### Reporting \"constraints\"

These are not constraints proper but expressions representing certain quantities useful for reporting, after the run is completed. They have no impact on the optimization. We have already mentioned $CAP(r,v,t,p)$, which represents the capacity of a process by vintage.

One sophisticated expression reports the *levelized cost* (LC) of a process. A process\'s LC is a life cycle quantity that aggregates all costs attached to a process, whether explicit or implicit. It is a useful quantity for ranking processes. However, such a ranking is dependent upon a particular model run, and may vary from run to run. This is so because several implicit costs attached to a process such as the cost of fuels used or produced, and perhaps the cost of emissions, are run dependent.

The general expression for the levelized cost of a process is as follows:

$LEC = \frac{\sum_{t = 1}^{n}{\frac{IC_{t}}{(1 + r)^{t - 1}} + \frac{OC_{t} + VC_{t} + \sum_{i}^{}{FC_{i,t} + FD_{i,t}} + \sum_{j}^{}{ED_{j,t}}}{(1 + r)^{t - 0.5}} -}\frac{\sum_{k}^{}{BD_{k,t}}}{(1 + r)^{t - 0.5}}}{\sum_{t = 1}^{n}\frac{\sum_{m}^{}{MO_{m,t}}}{(1 + r)^{t - 0.5}}}$
(5-9)

where

> $r$ discount rate (e.g. 5%)
> 
> $IC_{t}$ investment expenditure in (the beginning of) year $t$
> 
> $OC_{t}$ fixed operating expenditure in year $t$
> 
> $VC_{t}$ variable operating expenditure in year $t$
> 
> $FC_{i,t}$ fuel-specific operating expenditure for fuel $i$ in year $t$
> 
> $FD_{i,t}$ fuel-specific acquisition expenditure for fuel $i$ in year $t$
> 
> $ED_{j,t}$ emission-specific allowance expenditure for emission $j$ in year $t$ (optional)
> 
> $BD_{k,t}$ revenues from commodity $k$ produced by the process in year $t$ (optional)
> 
> $MO_{m,t}$ output of main product $m$ in year $t$, i.e. a member of the $pcg$

Comments:

Each cost element listed above is obtained by multiplying a unit cost by the value of the corresponding variable indicated in the run results.

The unit values of the first four costs are simply equal the process input data, i.e. the unit investment cost, the fixed unit O&M cost, the unit variable operating cost, and the unit delivery cost. The last three costs are the shadow prices of the commodities concerned, endogenously obtained as the dual solution of the current model run.

Note also that the user may choose to ignore the last two costs or to include them. Furthermore, concerning the last cost (which is indeed a revenue), the user may decide to ignore the revenue from the main commodities produced by the process and retain only the revenues from the by-products. The choice is specified via the parameter RPT_OPT('NCAP','1'). Technical note \"Levelized costs-TIMES\" provides details on the parameter values.

## The \'Linear\' variant of TIMES

This alternate TIMES formulation (called the LIN variant) assumes a different meaning for the activity and flow variables of TIMES. More precisely, instead of assuming that flows and activities are constant in all years within the same period, the variant assumes that the flow and activity variables apply to only one milestone year within each period. The variables\' values at other years of a period are interpolated between successive milestone years\' values. See section 5.2 for a figure depicting the two alternate definitions.

Choosing the LIN formulation affects the variable costs in the objective function as well as all dynamic constraints involving activities or flows. Note also that the LIN variant avoids the cost distortions mentioned in section 5.3.1.

Significant modifications in the LIN formulation concern the variable cost accounting, since the latter are no longer constant in all years of any given period, but evolve linearly between successive milestone years. The objective function components for all variable costs have been modified accordingly.

The following further modifications are done in the LIN formulation:
- The cumulative constraints on commodity production (EQ(l)\_CUMNET and EQ(l)\_CUMPRD) are modified to include linear interpolation of the commodity variables involved;
- The cumulative constraints on commodity and flow taxes and subsidies (EQ(l)\_CUMCST) are modified to include linear interpolation of the commodity and flow variables involved;
- The dynamic equations of the Climate module are modified to include linear interpolation of the variables involved;
- The inter-period storage equations are modified to include linear interpolation of the flow variables involved;
- The cumulative user constraints for activities and flows are also modified in a similar manner.
- Note that in the LIN formulation the activity of ***inter-period storage*** equations is measured at the milestone year (in the standard formulation it is measured at the end of each period). In addition, new EQ_STGIPS equations are added to ensure that the storage level remains non-negative at the end of each period. (Without these additional constraints, the linear interpolation of storage could lead to a negative storage level if the period contains more than a single year.)


------------

[^26]: This rather improper term includes equality as well as inequality
    relationships between mathematical expressions.

[^27]: For more information on optimizers see Brooke et al., 1998

[^28]: IRE stands for Inter-Regional Exchange

[^29]: Alternatively, one may use a convex programming code to solve the
    entire TIMES LP.

[^30]: The salvage value is thus the only cost element that remains
    lumped in the TIMES objective function. All other costs are
    annualized.

[^31]: That fraction is equal to 1 if the technical life of the
    investment made in period ***v*** fully covers period ***t***. It is
    less than 1 (perhaps 0) otherwise.
