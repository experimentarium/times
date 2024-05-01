# The Stochastic Programming extension

## Preamble to chapters 8 to 11

Recall that the core TIMES paradigm described in chapters 3, 4, and 5 makes several basic assumptions:
- Linearity of the equations and objective function
- Perfect foresight of all agents over the entire horizon
- Competitive markets (i.e. no market power by any agent)

If any or all of these assumptions are violated, the properties of the resulting equilibrium are no longer entirely valid. In the following four chapters, we present four variants of the TIMES paradigm that depart from the core model. Each of these variants (extensions) departs from one or more assumptions above, as follows:
- Stochastic Programming TIMES extension: departs from the perfect foresight assumption and instead assumes that certain key model parameters are random. This extension requires the use of stochastic programming rather than the usual deterministic linear programming algorithm;
- Limited horizon TIMES extension: departs from the perfect foresight assumption and replaces it by an assumption of limited (in time) foresight. This extension requires the use of sequential linear programming rather than a single global linear optimization;
- Lumpy investments extension: departs from the linearity assumption and replaces it by the assumption that certain investments may only be made in discrete units rather than in infinitely divisible quantities. This extension requires the use of mixed integer programming (MIP) instead of Linear programming;
- The endogenous technological learning (ETL) extension: departs from the linearity assumption for the cost of technologies and replaces it by an assumption that the costs of some technologies are decreasing functions of the cumulative amounts of the technologies, i.e. a learning curve is assumed. This entails that some parts of the objective function are non-linear and non-convex, and requires the use of MIP.

<ins>Remark</ins>: None of these four extensions departs from the competitive market assumption. It is *also* possible to simulate certain types of non-competitive behavior using TIMES. For instance, it has been possible to simulate the behavior of the OPEC oil cartel by assuming that OPEC imposes an upper limit on its oil production in order to increase its long term profit (Loulou et al, 2007). Such uses of TIMES are not embodied in new extensions. Rather, they are left to the ingenuity of the user.

## Stochastic Programming concepts and formulation

Stochastic Programming is a method for making optimal decisions under risk. The risk consists of facing uncertainty regarding the values of some (or all) of the LP parameters (cost coefficients, matrix coefficients, RHSs). Each uncertain parameter is considered to be a random variable, usually with a discrete, known probability distribution. The objective function thus becomes also a random variable and a criterion must be chosen in order to make the optimization possible. Such a criterion may be expected cost, expected utility, etc., as mentioned by Kanudia and Loulou (1998). Technical note "TIMES-Stochastic" provides a more complete description of the TIMES implementation

Uncertainty on a given parameter is said to be resolved, either fully or partially, at the *resolution time*, i.e. the time at which the actual value of the parameter is revealed. Different parameters may have different times of resolution. Both the resolution times and the probability distributions of the parameters may be represented on an event tree, such as the one of {numref}`stochastic-TIMES-tree`, depicting a typical energy/environmental situation. In {numref}`stochastic-TIMES-tree`, two parameters are uncertain: mitigation level, and demand growth rate. The first may have only two values (High and Low), and becomes known in 2010. The second also may have two values (High and Low) and becomes known in 2020. The probabilities of the outcomes are shown along the branches. This example assumes that present time is 2000. This example is said to have three stages (i.e. two resolution times). The simplest non-trivial event tree has only two stages (a single resolution time). Each pathway along the event tree, representing a different realization of the uncertain parameters is referred to as a state-of-the-world (SOW).

The **key observation** is that prior to resolution time, the decision maker (and hence the model) does not know the eventual values of the uncertain parameters, but still has to take decisions. On the contrary, after resolution, the decision maker knows with certainty the outcome of some event(s) and his subsequent decisions will be different depending on which outcome has occurred.

For the example shown in {numref}`stochastic-TIMES-tree`, in 2000 and 2010 there can be only one set of decisions, whereas in 2020 there will be two sets of decisions, contingent on which of the mitigation outcomes (High or Low) has occurred, and in 2030, 2040, 2050 and 2060, there will be four sets of contingent decisions.

```{figure} assets/image23.png
:name: stochastic-TIMES-tree
:align: center
Event Tree for a three-stage stochastic TIMES Example.
```

This remark leads directly to the following general multi-period, multi-stage stochastic program in Equations 8-1 to 8-3 below. The formulation described here is based on Dantzig (1963, Wets (1989), or Kanudia and Loulou (1999), and uses the expected cost criterion. Note that this is a LP, but its size is much larger than that of the deterministic TIMES model.

**Minimize**

  -------------------------------------------------------------------------------------------- -------------
  $$Z = \sum_{t \in T}^{}{}\sum_{s \in S(t)}^{}{}C(t,s) \times X(t,s) \times p(t,s)(8 - 1)$$   

  -------------------------------------------------------------------------------------------- -------------

**Subject to:**

  ----------------------------------------------------------------------------------- -----------
  $$A(t,s) \times X(t,s) \geq b(t,s)\forall s \in S(T),t \in T$$                      (8-2)

  $$\sum_{t \in T}^{}{D(t,g(t,s)) \times X(t,g(t,s))} \geq e(s)\forall s \in S(T)$$   (8-3)
  ----------------------------------------------------------------------------------- -----------

where

> $t$ = time period
>
> $T$ = set of time periods
>
> $s$ = state index
>
> $S(t)$ = set of state indices for time period $t$;

For {numref}`stochastic-TIMES-tree`, we have: S(2000) = 1; S(2010) = 1; S(2020) = 1,2;
S(2030) = 1,2,3,4;\
S(2040) = 1,2,3,4; S(2050) = 1,2,3,4; S(2060) = 1,2,3,4;

> $S(T)$ = set of state indices at the last stage (the set of *scenarios*). Set $S(T)$ is homeomorphic to the set of paths from period 1 to last period, in the event tree.
>
> $g(t,s)$ = a unique mapping from $\left\{ (t,s)|s \in S(T) \right\}$ to $S(t)$, according to the event tree. $g(t,s)$ is the state at period $t$ corresponding to scenario $s$.
>
> $X(t,s)$ = the column vector of decision variables in period $t$, under state $s$
>
> $C(t,s)$ = the cost row vector
>
> $p(t,s)$ = event probabilities
>
> $A(t,s)$ = the LP sub-matrix of single period constraints, in time period $t$, under state $s$
>
> $b(t,s)$ = the right hand side column vector (single period constraints) in time period $t$, under state $s$
>
> $D(t,s)$ = the LP sub-matrix of multi-period constraints under state $s$
>
> $e(s)$ = the right hand side column vector (multi-period > constraints) under scenario $s$

**Alternate formulation**: The above formulation makes it a somewhat difficult to retrieve the strategies attached to the various scenarios. Moreover, the actual writing of the cumulative constraints (8-3) is a bit delicate. An alternate (but equivalent) formulation consists in defining one scenario per path from initial to terminal period, and to define distinct variables *X(t,s)* for each scenario and each time period. For instance, in this alternate formulation of the example, there would be four variables *X(t,s)* at every period t, (whereas there was only one variable X(2000,1) in the previous formulation).

**Minimize**

  -------------------------------------------------------------------------------------------- -------------
  $$Z = \sum_{t \in T}^{}{}\sum_{s \in S(t)}^{}{}C(t,s) \times X(t,s) \times p(t,s)$$ (8-1)

  -------------------------------------------------------------------------------------------- -------------

**Subject to:**

  ----------------------------------------------------------------------------------- -----------
  $$A(t,s) \times X(t,s) \geq b(t,s) \forall t, for all s$$ (8-2)        

  $$\sum_{t \in T}^{}{D(t,s) \times X(t,s)} \geq e(s) \forall t, \forall s$$ (8-3)                                          
  ----------------------------------------------------------------------------------- -----------

Of course, in this approach we need to add equality constraints to express the fact that some scenarios are identical at some periods. In the example of {numref}`stochastic-TIMES-tree`, we would have:

X(2000,1)=X(2000,2)=X(2000,3)=X(2000,4),

X(2010,1)=X(2010,2)=X(2010,3)=X(2010,4),

X(2020,1)=X(2020,2),

X(2020,3)=X(2020,4).

Although this formulation is less parsimonious in terms of additional variables and constraints, many of these extra variables and constraints are in fact eliminated by the pre-processor of most optimizers. The main advantage of this new formulation is the ease of producing outputs organized by scenario.

In the current implementation of stochastic TIMES, the first approach has been used (Equations 8-1 to 8-3). The results are however reported for all scenarios in the same way as in the second approach.

In addition, in TIMES there is also an experimental variant for the modeling of recurring uncertainties with stochastic programming, described in Appendix A of technical note "TIMES-Stochastic".

## Alternative criteria for the objective function

The preceding description of stochastic programming assumes that the policy maker accepts the expected cost as his optimizing criterion. This is equivalent to saying that he is risk neutral. In many situations, the assumption of risk neutrality is only an approximation of the true utility function of a decision maker.

Two alternative candidates for the objective function are:
- Expected utility criterion with linearized risk aversion
- Minimax Regret criterion (Raiffa,1968, applied in Loulou and Kanudia, 1999)

### Expected utility criterion with risk aversion

The first alternative has been implemented into the stochastic version of TIMES. This provides a feature for taking into account that a decision maker may be risk averse, by defining a new utility function to replace the expected cost.

The approach is based on the classical E-V model (an abbreviation for Expected Value-Variance). In the E-V approach, it is assumed that the variance of the cost is an acceptable measure of the risk attached to a strategy in the presence of uncertainty. The variance of the cost of a given strategy $k$ is computed as follows:

$$Var(C_{k}) = \sum_{j}^{}{p_{j} \times (Cost_{j\left| k \right.\ } - EC_{k})^{2}}$$

where $Cost_{j|k}$ is the cost when strategy $k$ is followed and the $j^{th}$ state of nature prevails, and $EC_k$ is the expected cost of strategy $k$, defined as usual by:

$$EC_{k} = \sum_{j}^{}{p_{j} \times Cost_{j\left| k \right.\ }}$$

An E-V approach would thus replace the expected cost criterion by the following utility function to minimize:

$$U = EC + \lambda \times \sqrt{Var(C)}$$

where $λ>0$ is a measure of the risk aversion of the decision maker. For $λ=0$, the usual expected cost criterion is obtained. Larger values of $λ$ indicate increasing risk aversion.

Taking risk aversion into account by this formulation would lead to a non-linear, non-convex model, with all its ensuing computational restrictions. These would impose serious limitations on model size.

### Utility function with linearized risk aversion

To avoid non-linearities, it is possible to replace the semi-variance by the upper-absolute-deviation, defined by:

$$UpAbsDev(Cost_{k}) = \sum_{j}^{}{p_{j} \times \left\{ Cost_{j\left| k \right.\ } - EC_{k} \right\}^{+}}$$

where $y= {x}^+$ is defined by the following two *linear* constraints: $y ≥ x$ , and $y ≥ 0$, and the utility is now written via the following *linear* expression:

$$U = EC + \lambda \times UpsAbsDev(C)$$

This is the expected utility formulation implemented into the TIMES model generator.

## Solving approaches

General multi-stage stochastic programming problems of the type described above can be solved by standard deterministic algorithms by solving the deterministic equivalent of the stochastic model. This is the most straightforward approach, which may be applied to all problem instances. However, the resulting deterministic problem may become very large and thus difficult to solve, especially if integer variables are introduced, but also in the case of linear models with a large number of stochastic scenarios.

Two-stage stochastic programming problems can also be solved efficiently by using a Benders decomposition algorithm (Wets, 1989). Therefore, the classical decomposition approach to solving large multi-stage stochastic linear programs has been nested Benders decomposition. However, a multi-stage stochastic program with integer variables does not, in general, allow a nested Benders decomposition. Consequently, more complex decompositions approaches are needed in the general case (e.g. Dantzig-Wolfe decomposition with dynamic column generation, or stochastic decomposition methods).

The current version of the TIMES implementation for stochastic programming is solely based on directly solving the equivalent deterministic problem. As this may lead to very large problem instances, stochastic TIMES models are in practice limited to a relatively small number of branches of the event tree (SOW\'s).

## Economic interpretation

The introduction of uncertainty alters the economic interpretation of the TIMES solution. Over the last two decades, economic modeling paradigms have evolved to a class of equilibria called Dynamic Stochastic General Equilibria (DSGE, see references Chen and Crucuni, 2012; de Walque et al., 2005; Smets et al., 2007). In the case of Stochastic TIMES, we are in the presence of a Dynamic Stochastic Partial Equilibria (DSPE), with a much less developed literature. The complete characterization of a DSPE is beyond the scope of this documentation, but it is useful to note some of its properties, which derive from the theory of Linear Programming, as follows: 
- During the first stage (i.e. before resolution of any uncertainties), the meaning of the primal solution is identical to that of a deterministic TIMES run, i.e. of a set of optimal decisions, whereas the meaning of the shadow prices is that of *expected prices*(resp. expected marginal utility changes) of the various commodities. This is so because the shadow price is the marginal change in objective function when a commodity\'s balance is marginally altered, and the objective function is an expected cost (resp. an expected utility function).
- During subsequent stages, the primal values of any given branch of the event tree represent the optimal decisions *conditional on the corresponding outcome being true*, and the shadow prices are the *expected*[^35] *prices* of the commodities also conditional on the corresponding outcome being true.

------------

[^35]: The expected prices become deterministic prices if the stage is the last one, so that there is no uncertainty remaining at or after the current period.
