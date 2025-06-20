# Equations

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

## EQ_CC(r,t,p)

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

Sum over all intervals $k$ (in the piecewise linear approximation of the cumulative cost curve) of the _continuous_ variables VAR_LAMBD in the current period $t$.

$$\sum_k {VAR\_LAMBD_{r,t,p,k}}$$

## EQ_CLU(r,t,p)

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

## EQ_COS(r,t,p)

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

## EQ_CUINV(r,t,p)

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

## EQ_DEL(r,t,p)

**Description:** The constraint for an ETL technology that ensures that in each time period there is exactly one interval k for which the *binary* variable VAR_DELTA(r,t,p,k) has value 1 (with zero values for intervals ≠ k).

**Purpose and Occurrence:** To ensure that only one of the *binary* variable VAR_DELTA(r,t,p,k) has value 1 for each technology. This constraint, in combination with other ETL constraints, is fundamental to ensuring the validity of the piecewise linear approximation of the cumulative cost curve. This equation is generated in each time period for which the ETL technology is available.

**Units:** None.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be 1 in a feasible solution.

*Dual variable:* The dual variables of mixed integer problems have limited usefulness, as already mentioned.

**Equation**

$$EQ\_DEL_{r,t,p}\forall[(p \in teg) \land ((r,t,p) \in rtp)]$$

Sum over all intervals $k$ (in the piecewise linear approximation of the cumulative cost curve) of the _binary_ variables VAR_DELTA in the current period $t$.

$$\{ = \} \space 1$$

## EQ_EXPE1(r,t,p,k)

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

## EQ_EXPE2(r,t,p,k)

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

## EQ_IC1(r,t,p)

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

## EQ_IC2(r,t,p)

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

## EQ_LA1(r,t,p,k)

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

## EQ_LA2(r,t,p,k)

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

## EQ_MRCLU(r,t,p)

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

## EQ_OBJSAL(r,cur)

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

## EQ_OBJINV(r,cur) 

*- see EQ_OBJINV in section 5.2.2 for a general description without ETL*

**Description:** Regional investment cost part of objective function adjusted to include the endogenously determined investment cost (VAR_IC) for new investments in learning technologies.

**Purpose and Occurrence:** The objective function part calculating the investment costs is changed (for learning technologies only) by replacing the traditional calculation of discounted cost of investments in new capacity with that of the endogenously determined value. This equation is generated for each region where the learning investment costs occur in each time period beginning from the period, for which the ETL technology is available.

**Equation**

$$EQ\_OBJINV_{r,cur}$$

All the basic objective function terms for investment costs (section 5.2.2)

$$...$$

The calculated investments costs associated with the ETL technologies.

$$+ \sum_{t, p \in teg} [DISC_{r,t,p} \times VAR\_IC_{r,t,p}]$$
