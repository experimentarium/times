# Variables

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

## VAR_CCAP(r,t,p)

**Description:** The cumulative investment in capacity for an ETL technology.

**Purpose and** This variable tracks the cumulative investment in capacity for an ETL

**Occurrence:** technology which then determines, along with the progress ratio, how much the investment cost is to be adjusted for the learning gains.

This variable is generated for each ETL technology in all time periods beginning from the period that the technology is first available. It appears in the cumulative capacity definition constraint (EQ_CUINV) that defines it as the initial cumulative capacity (CCAP0) plus investments in new capacity (VAR_NCAP) made up to and including the current period. It also appears in the cumulative capacity interpolation constraint (EQ_CC). This constraint equates VAR_CCAP(r,t,p) to the sum over k of the variables VAR_LAMBD(r,t,p,k) used to represent the cumulative investment in capacity lying in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.

**Units:** PJ/a, Gw, or Bvkm/a, or any other unit defined by the analyst to represent technology capacity.

**Bounds:** This variable is not directly bounded. It may be indirectly bounded by specifying a bound (NCAP_BND) on the level of investment in new capacity (VAR_NCAP).

## VAR_CCOST(r,t,p)

**Description:** The cumulative cost of investment in capacity for an ETL technology.

**Purpose and** This variable defines the interpolated cumulative cost of investment in

**Occurrence:** capacity in terms of the continuous variables VAR_LAMBD and the binary variables VAR_DELTA, and the internal model parameters ALPH and BETA. ALPH and BETA represent the intercepts on the vertical axis and the slopes, respectively, of the line segments in the piecewise linear approximation of the cumulative cost curve.

This variable is generated for each ETL technology in all time periods beginning from the period that the technology is first available. It appears in the cumulative cost interpolation equation (EQ_COS) that defines it. It also appears in the equations EQ_IC1 and EQ_IC2 that define the VAR_IC variables that represent the portions of the cumulative cost of investment in capacity that are incurred in period t.

**Units:** Million 2000 US\$, or any other unit in which costs are tracked.

**Bounds:** None.

## VAR_DELTA(r,t,p,k)

**Description:** *Binary* variable (takes the value 0 or 1) used for an ETL technology to indicate in which interval of the piecewise linear approximation of the cumulative cost curve the cumulative investment in capacity (VAR_CCAP) lies.

**Purpose and** To indicate which step on the learning curve a technology achieves. A

**Occurrence:** value of 1 for this variable for interval k, and zero values for intervals ≠ k, imply that the cumulative investment in capacity (VAR_CCAP) lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.

This binary variable, along with the associated continuous variable VAR_LAMBD, are generated for each ETL technology in all time periods beginning from the period that the technology is first available, and for each interval in the piecewise linear approximation. It appears in the constraint EQ_DEL, whose purpose is to ensure that, for each ETL technology in each period, it has a value of 1 for exactly one interval k (with zero values for intervals ≠ k); and in the cumulative cost interpolation constraint (MR_COS). It also appears in the pair of constraints EQ_LA1 and EQ_LA2, whose purpose is to ensure that VAR_LAMBD, if positive for interval k, is between the two break points on the horizontal axis for interval k in the piecewise linear approximation. (See below under "Purpose and Occurrence" for the variable VAR_LAMBD.)

Finally, this binary variable appears in two constraints EQ_EXPE1 and EQ_EXPE2, whose purpose is to reduce the domain of feasibility of the binary variables and thereby improve solution time for the Mixed Integer Program (MIP).

**Units:** None. This is a binary variable that takes the value 0 or 1.

**Bounds:** This binary variable is not directly bounded.

## VAR_IC(r,t,p)

**Description:** The portion of the cumulative cost of investment in capacity for an ETL technology (VAR_CCOST) that is incurred in period t.

**Purpose and** This variable represents the portion of the cumulative cost of investment

**Occurrence:** in capacity for an ETL technology that is incurred in period t, and so is subject to the same discounting in the investment cost part of the objective function (EQ_OBJINV) that applies to other period t investment costs.

This variable is calculated as the difference between the cumulative costs of investment in capacity for period t and t-1, and is generated for each ETL technology in all time periods beginning from the period that the technology is first available. Apart from its appearance in the objective function, this variable appears in the constraints EQ_IC1 and EQ_IC2 that define it in the first period that the technology is available, and in subsequent periods, respectively. It also appears in the salvage of investments constraint (EQ_OBJSALV), which calculates the amount to be credited back to the objective function for learning capacity remaining past the modeling horizon.

**Units:** Million 2000 US\$, or any other unit in which costs are tracked.

**Bounds:** None.

## VAR_LAMBD(r,t,p,k)

**Description:** *Continuous* variable used for an ETL technology to represent the portion of cumulative investment in capacity (VAR_CCAP) that lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve.

**Purpose and** A positive value for this variable for interval k, and zero values for

**Occurrence:** intervals ≠ k, imply that the cumulative investment in capacity (VAR_CCAP) lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve. This continuous variable, along with the associated binary variable VAR_DELTA, are generated for each ETL technology in all time periods beginning from the period that the technology is first available (START), and for each interval in the piecewise linear approximation.

> Since this variable represents the portion of the cumulative investment in capacity (VAR_CCAP) that lies in the k^th^ interval of the piecewise linear approximation of the cumulative cost curve, the value of EQ_LAMBD -- if positive -- is required to be between CCAPK(k-1,p) and CCAP(k,p), where the internal model parameters CCAPK are the break points on the horizontal axis in the piecewise linear approximation of the cumulative cost curve. A zero value for VAR_LAMBD is also allowed. These requirements on the value of VAR_LAMBD are imposed via the pair of constraints EQ_LA1 and EQ_LA2, in which the value for VAR_LAMBD is subject to lower and upper bounds of CCAPK(k-1,p) \* VAR_DELTA and CCAP(k,p) \* VAR_DELTA respectively, where VAR_DELTA = VAR_DELTA(r,t,p,k) is the binary variable associated with VAR_LAMBD = VAR_LAMBD(r,t,p,k).

This variable also appears in the cumulative capacity interpolation constraint (EQ_CC), and the cumulative cost interpolation constraint (EQ_COS).

**Units:** PJ/a, Gw, or Bvkm/a, or any other unit defined by the analyst to represent technology capacity.

**Bounds:** The pair of constraints EQ_LA1 and EQ_LA2 that are discussed above have the effect of either bounding VAR_LAMBD between CCAPK(k-1,p) and CCAP(k,p), or forcing VAR_LAMBD to be zero.
