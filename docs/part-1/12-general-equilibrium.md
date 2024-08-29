# General equilibrium extensions

## Preamble

In order to achieve a general (as opposed to partial) equilibrium, the energy system described in TIMES must be linked to a representation of the rest of the economy. The idea of hard-linking an energy model with the economy while still keeping the resulting model as an optimization program, dates back to the ETA-MACRO model (Manne, 1977), where both the energy system and the rest of the economy were succinctly represented by a small number of equations. This approach differs from the one taken by the so-called Computable General Equilibrium (CGE), models (Johanssen 1960, Rutherford 1992), where the calculation of the equilibrium relies on the resolution of simultaneous non-linear equations. In CGE\'s, the use of (non-linear, non-convex) equation solvers limits the size of the problem and thus the level of detail in the energy system description. This computational difficulty is somewhat (but not completely) alleviated when the computation relies on a single non-linear optimization program. Note however that MACRO is a much simplified representation of the economy as a single producing sector and no government sector, thus precluding the endogenous representation of taxes, subsidies, multi-sector interactions, etc. Therefore, the idea of a linked TIMES-MACRO model is not to replace the CGE\'s but rather to create an energy model where the feedbacks from the economy goes beyond the endogenization of demands (which TIMES does) to include the endogenization of capital.

Some years after ETA-MACRO, MARKAL-MACRO (Manne-Wene, 1992) was obtained by replacing the simplified ETA energy sub-model by the much more detailed MARKAL, giving rise to a large optimization model where most, but not all equations were linear. The MERGE model (Manne et al., 1995) is a multi-region version of ETA-MACRO with much more detail on the energy side --although not as much as in MARKAL-MACRO. The TIMES-MACRO model (Remme-Blesl, 2006) is based on exactly the same approach as MARKAL-MACRO. Both MARKAL-MACRO and TIMES-MACRO were essentially single-region models, until the multi-region version of TIMES-MACRO (named TIMES-MACRO-MSA, Kypreos-Lettila, 2013) was devised as an extension that accommodates multiple regions.

In this chapter, we describe the single region and the multi-region versions of TIMES-MACRO, focusing on the concepts and mathematical representation, whereas the implementation details are left to Part II of the TIMES documentation and to technical notes.

## The single-region TIMES-MACRO model

As was already discussed in chapter 4, the main physical link between a TIMES model and the rest of the economy occurs at the level of the consumption of energy by the end-use sectors. There are however other links, such as capital and labor, which are common to the energy system and the rest of the economy. {numref}`energy-labor-monetary-flows` shows the articulation of the three links in TIMES-MACRO. Energy flows from TIMES to MACRO, whereas money flows in the reverse direction. Labor would also flow from MACRO to TIMES, but here a simplification is used, namely that the representation of labor is purely exogenous in both sub-models. Thus, TIMES-MACRO is not suitable for analyzing the impact of policies on labor, or on taxation, etc.

```{figure} assets/times-macro-flows.svg
:name: energy-labor-monetary-flows
:align: center

Energy, Labor, and Monetary flows between TIMES and MACRO.
```

We now turn to the mathematical description of the above, starting with the MACRO portion of the hybrid model.

### Formulation of the MACRO model
We start our description of the hybrid model by stating the MACRO equations {eq}`12-1` -- {eq}`12-6`[^39]:

$$Max \quad \sum_{t = 1}^{T - 1}{dfact_{t}} \times \ln(C_{t}) + \frac{dfact_{T - 1} \times dfactcur{r_{T - 1}}^{\frac{d_{T - 1} + d_{T}}{2}}}{1 - dfactcur{r_{T}}^{\frac{d_{T - 1} + d_{T}}{2}}} \times \ln(C_{T})$$ (12-1)

$$Y_{t} = C_{t} + INV_{t} + EC_{t}$$ (12-2)

$$Y_{t} = \left( akl \times K_{r}^{kpvs \times \rho} \times l_{t}^{(1 - kpvs)\rho} + \sum_{dm}^{}{b_{dm} \times DEM\_M_{t,dm}^{\rho}} \right)^{\frac{1}{\rho}}$$ (12-3)

$$l_{1} = 1\mspace{6mu}\mspace{6mu}\quad\text{and      }l_{t + 1} = l_{t} \times \left( 1 + growv_{t} \right)^{\frac{d_{t} + d_{t + 1}}{2}}$$ (12-4)

$$K_{t + 1} = tsrv_{t} \times K_{t} + \frac{1}{2}\left( d_{t} \times tsrv \times INV_{t} + d_{t + 1} \times INV_{t + 1} \right)$$ (12-5)

$$K_{T} \times \left( growv_{T} + depr \right) \leq INV_{T}$$ (12-6)

with the model **variables**:

> $C_{t}$: annual consumption in period $t$,
> 
> $DEM\_ M_{t,dm}$: annual energy demand in MACRO for commodity $dm$ in period $t$,
> 
> $Y_{t}$: annual production in period $t$,
> 
> $INV_{t}$: annual investments in period $t$,
> 
> $EC_{t}$: annual energy costs in period $t$,
> 
> $K_{t}$: total capital in period $t$

and the **exogenous parameters**:

> $akl$: production function constant,
> 
> $b_{dm}$: demand coefficient,
> 
> $d_{t}$: duration of period $t$ in years,
> 
> $depr$: depreciation rate,
> 
> $dfact_{t}$: utility discount factor,
> 
> $dfactcurr_{t}$: annual discount rate,
> 
> $growv_{t}$: growth rate in period $t$,
> 
> $kpvs$ capital value share,
> 
> $l_{t}$: annual labor index in period $t$,
> 
> $\rho$: substitution constant,
> 
> $T$: period index of the last period,
> 
> $tsrv_{t}$: capital survival factor between two periods.

The objective function {eq}`12-1` of the MACRO model is the maximization of the summation of discounted utility at each period. The utility is defined as the logarithm of consumption $C_{t}$ of the households. A logarithmic utility function embodies a decreasing marginal utility property (Manne, 1977). Note that the discount factor $dfact_{t}$ for period t must take into account both the length of the period and the time elapsed between the period\'s start and the base year. Note also that the discount factor of the last period has a larger impact since it is assumed to apply to the infinite time horizon after the last model period (alternatively, the user may decide to limit the number of years in the last term, in those cases where it is deemed important to confer less weight to the indefinite future).

The national accounting equation {eq}`12-2` simply states that national production $Y_t$ must cover national consumption $C_t$ , plus investments $INV_t$, plus energy costs $EC_t$.

The production function {eq}`12-3` represents the entire economy. It is a nested, constant elasticity of substitution (CES) function with the three input factors capital, labor and energy. The production input factors labor $l_{t}$ and capital $K_{t}$ form an aggregate, in which both can be substituted by each other represented via a Cobb-Douglas function. Then, the aggregate of the energy services and the aggregate of capital and labor can substitute each other. Note that labor is not endogenous in MACRO, but is specified exogenously by the user provided a labor growth rate $growv_{t}$.

The energy in term in {eq}`12-3` is a weighted sum of end-use demands in all sectors $dm$ of the economy, $DEM\_M_{t,dm}$, raised to the power $\rho$. We defer the definition of these quantities until the next subsection.

The lower the value of the elasticity of substitution the closer is the linkage between economic growth and increase in energy demand. For homogenous production functions with constant returns to scale[^40] the substitution constant $\rho$ in {eq}`12-3` is directly linked with the user-defined elasticity of substitution $\sigma$ by the expression $\rho = 1 - \frac{1}{\sigma}$.

The capital value share $kpvs$ describes the share of capital in the sum of all production factors and must be specified by the user. The parameter $akl$ is the level constant of the production function. The parameters $akl$ and $b_{dm}$ of the production are determined based on the results from a TIMES model run without the MACRO module.

The capital dynamics equation {eq}`12-5` describes the capital stock in the current period $K_{t + 1}$ based on the capital stock in the previous period and on investments made in the current and the previous period. Depreciation leads to a reduction of the capital. This effect is taken into account by the capital survival factor$tsrv_{t}$, which describes the share of the capital or investment in period $t$ that still exists in period $t+1$. It is derived from the depreciation rate $depr$ using the following expression:

$$tsrv_{t} = (1 - depr)^{\frac{\left( d_{t + 1} + d_{t} \right)}{2}}$$ (12-7)

Expression {eq}`12-7` calculates the capital survival factor for a period of years beginning with the end of the middle year $m_{t}$ and ending with the end of the year $m_{t + 1}$. The duration between these two middle years equals the duration $\frac{d_{t + 1} + d_{t}}{2}$. Then, a mean investment in period $t$ is calculated by weighting the investments in $t$ and $t+1$ with the respective period duration: $\frac{1}{2}\left( d_{t} \times tsrv \times INV_{t} + d_{t + 1} \times INV_{t + 1} \right)$.

For the first period it is assumed that the capital stock grows with the labor growth rate of the first period$growv_{0}$. Thus, the investment has to cover this growth rate plus the depreciation of capital. Since the initial capital stock is given and the depreciation and growth rates are exogenous, the investment in the first period can be calculated beforehand:

$$INV_{0} = K_{0} \times \left( depr + growv_{0} \right)$$ (12-8)

Since the model horizon is finite, one has to ensure that the capital stock is not fully exhausted (which would maximize the utility in the model horizon). Therefore a terminal condition {eq}`12-6` is added, which guarantees that after the end of the model horizon a capital stock for the following generations exists. It is assumed that the capital stock beyond the end of horizon grows with the labor growth rate $growv_{T}$. This is coherent with the last term of the utility function.

### Linking MACRO with TIMES

TIMES is represented via the following condensed LP

$Min\ \sum_{t}^{}{dfact}_{t} \times {COST\_T_{t}}_{}(x)$

s.t. $E \times x = DEM\_T_{dm,t}$ (A)

$A \times x = b$ (B)

where
- $x$ is the vector of TIMES variables
- ${COST\_ T_{t}}_{}(x)$ is the annual undiscounted cost TIMES expression
- $dfact_t$ is the discount factor for period $t$
- equations (A) express the satisfaction of demands in TIMES (and thus defines the $DEM\_T_{dm,t}$ variables), and
- equations (B) is the set of all other TIMES constraints

MACRO and TIMES are hard linked via two sets of variables: the energy variables $DEM\_T_{dm,t}$, and the period energy costs $COST\_T_t$.

The aggregate energy input into MACRO (see equation {eq}`12-3`), is slightly different from the TIMES variables defined above. In the linked model, each term $DEM\_M$ is obtained by further applying a factor $aeeifac_{t,dm}$ as shown in equation {eq}`12-9`.

$$DEM\_T_{t,dm} = aeeifac_{t,dm} \times DEM\_M_{t,dm}$$ (12-9)

Indeed, the energy demand in the TIMES model can be lower than the energy requirement of the MACRO model due to demand reductions, which are caused by autonomous energy efficiency improvements and come in addition to those captured in the energy sector of the TIMES model. The autonomous energy efficiency improvement factor $aeeifac_{t,dm}$ is determined in a calibration procedure described in technical note "Documentation of the TIMES-MACRO model", which also discusses the weighing coefficients $b_{dm}$.

The other link consists in accounting for the monetary flow $EC_{t}$, equal to the expenditures made in the energy sector. Precisely, $EC_{t}$is equal to the annual *undiscounted* energy system cost of the TIMES model, $COST\_ T_{t}$, (as used in the TIMES objective function), augmented with an additional term as shown in equation {eq}`12-10`:

$$COST\_T_{t} + \frac{1}{2}qfac\sum_{p}^{}{\frac{cstinv_{t,p}}{\exp f_{t} \times capfy_{p}} \times XCAP_{t,p}^{2}} = EC_{t}$$ (12-10)

with

> $XCAP_{t,p}$: portion of the capacity expansion for technology $p$ in period $t$ that is penalized. Constraint {eq}`12-11` below states that it is the portion exceeding a predefined tolerable expansion rate$\ exp f_{t}$,
> 
> $EC_{t}$: costs for the production factor energy in the MACRO model,
> 
> $qfac$: trigger to activate penalty term (0 for turning-off penalty, 1 for using penalty term),
> 
> $cstinv_{t,p}$: specific annualized investment costs of technology $p$ in period $t$,
> 
> $capfy_{p}$: maximum level of capacity for technology $p$,
> 
> $\exp f_{t}$: tolerable expansion between two periods.

Just like in the pure MACRO model, the quadratic penalty term added on the left hand side of equation {eq}`12-10` serves to slow down the penetration of technologies. This term plays a somewhat similar role as the growth constraints do in the stand-alone TIMES model. The variable $XCAP_{t,p}$ is the amount of capacity exceeding a predefined expansion level expressed by the expansion factor $\exp f_{t}$ and is determined by the following equation:

$$VAR\_CAP_{t + 1,p} \leq \left( 1 + expf_{t} \right) \times VAR\_CAP_{t,p} + XCAP_{t + 1,p}$$ (12-11)

with:

$VAR\_CAP_{t,p}$: total installed capacity of technology $p$ in period $t$.

As long as the total installed capacity in period $t+1$ is below $\left( 1 + expf_{t} \right) \cdot CAP_{t,p}$ no penalty costs are applied. For the capacity amount $XCAP_{t + 1,p}$ exceeding this tolerated capacity level penalty costs are added to the regular costs of the TIMES model in Equation {eq}`12-10`.

The quadratic term in equation {eq}`12-10` introduces a large number of nonlinear terms (one for each technology and period) that may constitute a considerable computational burden for large models. These constraints are therefore replaced in the current implementation of TIMES, by linear piece-wise approximations in a way quite similar to what was done to linearize the surplus in chapter 4.

### A brief comment

In spite of the linearization of the penalty terms in equation {eq}`12-10`, TIMES-Macro still contains non-linearities: its objective function is a concave function, a good property when maximizing, but there are $T$ nonlinear, non convex constraints as per equation {eq}`12-3` that introduce a non trivial computational obstacle to large size instances of the model.

Although not discussed here, the calibration of the TIMES-MACRO model is an exceedingly important task, since the model must agree with the initial state of the economy in the dimensions of labor, capital, and the links between the energy sector and the economy at large. Fuller details on calibration are provided in the above-mentioned technical note.

Overall, the experience with TIMES-MACRO has been good, with sizable model instances solved in reasonable time. But the modeler would benefit from carefully weighing the limitation of model size imposed by the non-linear nature of TIMES-MACRO, against the advantage of using a (single sector) general equilibrium model.

## The multi-regional TIMES-MACRO model (MSA)

In this section, we only sketch the generalization of TIMES-MACRO to a multi-regional setting. Full details, including the important calibration step and other implementation issues, appear in technical note "TIMES-Macro: Decomposition into Hard-Linked LP and NLP Problems".

### Theoretical background

In a multi-regional setting, inter-regional trade introduces an important new complication in the calculation of the equilibrium[^41]. Indeed, the fact that the utility function used in the MACRO module is highly non linear also means that the global utility is not equal to the sum of the national utilities. Also, it would be impractical and conceptually wrong to define a single consumption function for the entire set of regions, since the calibration of the model may only be done using national statistics, and furthermore, there may be large differences in the parameters of each region\'s production function, etc.

It follows from the above that it is not possible to use a single optimization step to calculate the global equilibrium. Instead, one must resort to more elaborate approaches in order to compute what is termed a Pareto-optimal solution to the equilibrium problem, i.e. a solution where the utility of any region may not be improved without deteriorating the utility of some other region(s).

Such a situation has been studied in the economics literature, starting with the seminal paper by Negishi (1960) that established the existence of equilibria that are Pareto-optimal in the Welfare functions. Manne (1999) applied the theory to the MACRO model, and Rutherford (1992) proposed a decomposition algorithm that makes the equilibrium computation more tractable. The Rutherford algorithm is used in the TIMES-MACRO model. An interesting review of the applications of Negishi theory to integrated assessment models appeared in Stanton (2010).

### A sketch of the algorithm to solve TIMES-MACRO-MSA

Rutherford\'s procedure is an iterative decomposition algorithm. Each iteration has two steps. The first step optimizes a large TIMES LP and the second step optimizes a stand-alone *reduced* non-linear program which is an alteration of MACRO, and is named MACRO-MSA. These two steps are repeated until convergence occurs.

Because the two steps must be solved repeatedly, the iterative procedure is computationally demanding; furthermore, it is established that the speed of convergence is dependent upon the number of trade variables that link the regions. For this and other reasons, the trade between regions is limited to a single commodity, namely a *numéraire*, expressed in monetary units. The numéraire $NT_{r,t}$ affects the national account equation {eq}`12-2` of each region, as follows:

$$Y_{r,t} = C_{r,t} + INV_{r,t} + EC_{r,t} + NTX_{r,t}$$

and is subject to the conservation constraint: $\sum_{r}^{}{NTX_{r,t}\  = \text{0 }}\forall\ \{ t\}$, which insures that trade is globally balanced.

<ins>First step</ins>: at each iteration, the first step is the resolution of TIMES using non-elastic demands provided by the previous solution of the non-linear program (except at iteration 1, where demands are either exogenously provided or generated by TIMES[^42]).

<ins>Second step</ins>: once the TIMES solution is obtained, it is used to form a quadratic expression representing an approximation of the aggregate energy cost, to be used in MACRO-MSA. Defining this approximation is the crux of Rutherford decomposition idea. It replaces the entire TIMES model, thus greatly simplifying the resolution of Step 2. The global objective function of MACRO-MSA is a weighted sum (over all regions) of the regional MACRO welfare functions, where the weights are the Negishi weights for each region. The thus modified global objective function is maximized. Then, a convergence criterion is checked. If convergence is not observed, the new demands are fed into TIMES and a new iteration is started. The Negishi weights are also updated at each iteration, leading to a new version of the objective, until the algorithm converges to the Pareto-optimal equilibrium.

The adaptation of Rutherford algorithm to TIMES-MACRO was formalized by Kypreos (2006) and implemented by Kypreos and Lettila as the above-mentioned technical note.


[^39]: The concrete implementation in the TIMES-MACRO model differs in some points, e.g. the consumption variable in the utility function is substituted by equations {eq}`12-2` and {eq}`12-3`.

[^40]: A production function is called homogenous of degree $r$, if multiplying all production factors by a constant scalar leads $\lambda$ to an increase of the function by $\lambda^r$. If $r = 1$, the production function is called linearly homogenous and leads to constant returns to scale.

[^41]: Of course, if no trade between the regions is assumed, the global equilibrium amounts to a series of independent national equilibria, which may be calculated by the single region TIMES-MACRO.

[^42]: It may be desirable, although not required to use non-zero demand elasticities at the very first iteration.
