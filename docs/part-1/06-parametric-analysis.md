(parametric-analysis-with-times)=
# Parametric analysis with TIMES

Dealing with uncertainty in modeling is a complex endeavour that may be accomplished via a number of (sometimes widely different) approaches. In the case of TIMES, two different features are available: ***Stochastic Programming*** (treated in chapter 8) and ***parametric analysis***, also known as ***sensitivity analysis***, which is the subject of this chapter. In sensitivity analysis, the values of some important exogenous assumptions are varied, and a series of model runs is performed over a discrete set of combinations of these assumptions. Sensitivity analysis is often combined with ***tradeoff analysis***, where the tradeoff relation between several objectives is analyzed.

The uncertain attributes are similar to the corresponding standard TIMES attributes, but they may now have different values according to the different ***states-of-the-world*** (SOW), just as in the case of stochastic programming. The difference between the two approaches is that sensitivity analysis solves a sequence of instances, each assuming different values of the uncertain parameters, whereas stochastic programming solves a single instance that encompasses all potential values of the uncertain parameters simultaneously.

In TIMES, sensitivity analysis and tradeoff analysis facility are implemented using the same setup and some of the attributes of the stochastic mode of TIMES, since both approaches, although conceptually different, use the same state of the world construct.

Here are a few possible set-ups for sensitivity and tradeoff analyses in TIMES, all of which are supported by the model generator:

A.  Single phase sensitivity analysis over the set of SOWs. Each run corresponds to a set of values for the uncertain parameters. The runs are mutually independent. This is the most straightforward approach;

B.  Two-phase tradeoff analysis, where the model is first run using a user-defined objective function, and then the TIMES objective function is used in phase 2, while the solution from the first phase is used for defining additional constraints in a series of model runs in the second phase.

C.  Multiphase tradeoff analysis over N phases, which is a generalization of the two-phase case.

Analyzing tradeoffs between the standard objective function and some other possible objectives (for which the market is not able to give a price) was not possible in an effective way with earlier versions of TIMES.

(two-phase-tradeoff-analysis)=
## Two-phase tradeoff analysis

In the ***first phase*** of the TIMES two-phase tradeoff analysis facility, the objective function is user defined as a weighted sum of any number of components, each component being a user constraint\'s left-hand-side. All UC\'s must be of the global type, (i.e. aggregated over regions and periods). Optionally, each of the component UCs may also be constrained by upper/lower bounds. The components are defined by the user, via the specification of non-zero weight coefficients for the UC\'s to be included in the objective. The original objective function (total discounted costs) is automatically pre-defined as a non-constraining user constraint with the name $OBJZ$, and can therefore always be directly used as one of the component UCs, if desired.

Consequently, the first phase can be considered as representing a Utility Tradeoff Model, which can also be used as a stand-alone option. If used in a stand-alone manner, it constitutes a case of multi-criterion decision making (see e.g. Weistroffer, 2005). The resulting objective function to be minimized can be written as follows:

$$\min \ obj1 = \sum_{uc \in UC\_ GLB}^{}{W(uc) \times LHS(uc)}$$

where:

> $W(uc)$ = weight of objective component $uc$ in Phase 1
>
> $LHS(uc)$ = LHS expression of user constraint $uc$ according to its definition
>
> $UC\_GLB$ = the set of all global UC constraints (including $OBJZ$)

In the ***second phase*** of the TIMES two-phase tradeoff analysis facility the objective function is always the ***original objective function*** in TIMES, i.e. the total discounted system cost (this ensures that the second phase solution produce an economically meaningful set of values for the dual variables.)

In addition, in the second phase the user can specify bounds on fractional deviations in the LHS values of any or all user constraints, in comparison to the optimal LHS values obtained in the first phase. Such deviation bounds can be set for both global and non-global constraints, and for both non-constraining and constrained UCs (however, any original absolute bounds are overridden by the deviation bounds). The ***objective function used in Phase 1*** is also available as an additional pre-defined UC, named $OBJ1$, so that one can set either deviation bounds or absolute bounds on that as well, if desired. In addition, both the total and regional original objective functions can be referred to by using the predefined UC name $OBJZ$ in the deviation bound parameters.

The objective function to be minimized in the second phase, and the additional bounds on the LHS values of UCs, can be written as follows:

$${\min objz = LHS('OBJZ')}{\left. \ \begin{matrix} LHS(uc) \leq (1 + maxdev(uc)) \times LHS^{*}(uc) \\ LHS(uc) \geq (1 - maxdev(uc)) \times LHS^{*}(uc) \end{matrix} \right\}\begin{matrix} \text{for each }uc\text{ for which } \\ maxdev(uc)\text{ has been specified} \end{matrix}}$$

where:

> $LHS('OBJZ')$ = the standard objective function (discounted total system costs)
>
> $LHS(uc)$ = LHS expression of user constraint $uc$ according to its definition
>
> $LHS(uc)$ = optimal LHS value of user constraint $uc$ in Phase 1
>
> $maxdev(uc)$ = user-specified fraction defining the maximum proportional deviation in the value of $LHS(uc)$ compared to the solution in Phase 1

Remarks:
1. Use of the two-phase tradeoff analysis facility requires that a weight has been defined for at least one objective component in the first phase.
2. If no deviation bounds are specified, the second phase will be omitted.
3. Automatic discounting of any commodity or flow-based UC component is possible by using a new UC_ATTR option 'PERDISC' which could be applied e.g. to the user-defined objective components in Phase 1.
4. The two-phase tradeoff analysis can be carried over a set of distinct cases, each identified by a unique SOW index.

(multiphase-tradeoff-analysis)=
## Multiphase tradeoff analysis

The multiphase tradeoff analysis is otherwise similar to the two-phase analysis, but in this case the objective function can be defined in the same way as in the Phase 1 described above also in all subsequent phases. The different objective functions in each phase are distinguished by using an additional phase index (the SOW index). Deviation bounds can be specified in each phase, such that they will be in force over all subsequent phases (any user constraints), or only in some of the succeeding phases (any user constraints excluding $OBJ1$). The deviation bounds defined on any of the user-defined objectives $OBJ1$ will thus always be preserved over all subsequent phases.

**Remark**: Although the multiphase tradeoff analysis allows the use of any user-defined objective functions in each phase, it is highly recommended that the original objec­tive function be used in the last phase, so that the economic meaning is maintained in the final solution.

The procedure was presented in a very general form, in order to let the user exert her ingenuity at will. Typical simple examples of using the feature may be useful.

<ins>Example 1</ins>: Trade-off between cost and risk.

First, a special UC (call it RISK) is defined that expresses a **global risk** measure. The successive phases consist in minimizing the following parameterized objective:

$$Min\ OBJZ + \alpha \times RISK$$

where α is a user chosen coefficient that may be varied within a range to explore an entire trade-off curve such as illustrated in {numref}`trade-off-risk-cost`, where the vertical axis represents the values of the cost objective function, and the horizontal axis the risk measure.

```{figure} assets/risk-cost-trade-off.svg
:name: trade-off-risk-cost
:align: center

Trade-off between Risk and Cost.
```

$OBJZ^*$ is the lowest value for $OBJZ$, corresponding to a relatively large value $R_0$ for RISK, i.e. when $α = 0.$ As $α$ increases, RISK decreases and $OBJZ$ increases. In this example, 4 alternate values of $α$ were chosen until the value of $OBJZ$ becomes very large, at point ($R_4$, $OBJZ_4$). This would correspond to very large value for α, i.e. a point where RISK is minimized.

An example of such an analysis is fully developed in Kanudia et al (2013), where a risk index is constructed to capture an indicator of energy security for the European Union. A complex (but linear) risk measure was developed to evaluate the risk for a large number of alternative channels of energy imports into the EU, and the trade-off between risk and overall cost was explored.

<ins>Example 2</ins>: exploring the opportunity cost of the nuclear option

At phase 1, the original $OBJZ$ is minimized with the habitual TIMES constraints. This results in an optimal cost $OBJZ^*$. At phase 2, the objective function is equal to the total nuclear capacity over the entire horizon and over all regions, and a new constraint is added as follows:

$$OBJZ \leq (1 + \alpha) \times {OBJZ}^{*}$$

The α parameter may be varied to explore the entire trade-off curve. A last phase may also be added at the end, with OBJZ as objective function, and a user selected value for the maximum level of nuclear capacity.
