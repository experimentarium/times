# Mathematical formulation

For the own-price elasticities, we have the following relations (see Part I, Chapter {numref}`%s <core-times-model-mathematics>`), where $U_{i}$ is the term in the objective function associated with the utility change due to the demand variation of demand *i*:

$$DM_{i}/D{M_{i}}^{0} = (p_{i}/p_{i}^{0})^{E_{i}}$$ (2-10-1)

$$p_{i} = p_{i}^{0} \cdot (DM_{i}/D{M_{i}}^{0})^{1/E_{i}}$$ (2-10-2)

$$U_{i} = \sum_{t}^{}\left( \frac{p_{i}^{0}(t)}{(1 + 1/E_{i})} \cdot \left\lbrack DM_{i}^{0}(t) \right\rbrack^{- 1/E_{i}} \bullet DM_{i}(t)^{1 + 1/E_{i}} \right)$$ (2-10-3)

Consider then a utility function of the general CES form:

$$U_{k} = \left( \sum_{i}^{}{\alpha_{i}^{\frac{1}{\sigma}}x_{i}^{\frac{\sigma - 1}{\sigma}}} \right)^{\frac{\sigma}{\sigma - 1}}$$ (2-10-4)

where:
- $U_{k}$ is the total aggregate utility of demand *k*
- $x_{i}$ is the demand for commodity *i* (component of the aggregate demand)
- $α_{i}$ is a share parameter (the sum of which over *i* needs not be equal to 1)
- $σ$ is the elasticity of substitution (0 \< *σ* \< ∞)

The demand functions for $x_{i}$ can be derived from the utility function in terms of prices, and can be given by the formulas:

$$x_{i} = \frac{\alpha_{i}m}{p_{i}^{\sigma}}\left( \sum_{i}^{}{\alpha_{i}p_{i}^{1 - \sigma}} \right)^{- 1} = \frac{\alpha_{i}m}{p_{u}}\left( \frac{p_{u}}{p_{i}} \right)^{\sigma}$$ (2-10-5)

where *m* is the income level, and $p_{u}$ is the aggregate price, or unit cost, of the utility, can be given in terms of the individual prices $p{i}$ of the demands *i*:

$$p_{u} = \left( \sum_{i}^{}{\alpha_{i}p_{i}^{1 - \sigma}} \right)^{\frac{1}{1 - \sigma}}$$ (10-2-6)

The share parameters $α_{i}$ can be derived from the expenditure shares, as shown in Eq. {eq}`2-10-7` below. In the objective function, the utility change can then be calculated by the expression shown in Eq. {eq}`2-10-9` below.

$$\alpha_{i}^{k} = \frac{agg_{i}^{k}(t) \cdot DM_{i}^{0}(t)}{DM_{k}^{0}(t)} \cdot \left( \frac{p_{i}^{0}(t)}{agg_{i}^{k}(t) \cdot p_{u_{k}}^{0}(t)} \right)^{\sigma}$$ (2-10-7)

$$\beta_{k} = \left( \frac{p_{u_{k}}^{0}(t)}{1 + \frac{1}{E_{k}}} \right) \cdot \left( DM_{k}^{0}(t) \right)^{\frac{- 1}{E_{k}}}$$ (2-10-8)

$$U_{k} = \sum_{t}^{}\left( \beta_{k}(t) \cdot \left( \left( \left( \sum_{i}^{}{\left( \alpha_{i}^{k}(t) \right)^{\frac{1}{\sigma_{k}}} \cdot \left( agg_{i}^{k}(t) \cdot DM_{i}^{k}(t) \right)^{\frac{\sigma_{k} - 1}{\sigma_{k}}}} \right)^{\frac{\sigma_{k}}{\sigma_{k} - 1}} \right)^{1 + \frac{1}{E_{k}}} - \left( DM_{k}^{0}(t) \right)^{1 + \frac{1}{E_{k}}} \right) \right)$$ (2-10-9)

In the above, the coefficients $agg_{i}$ are represent user-defined aggregation coefficients for defining the aggregation from the component demands to the aggregate demands. The constant term corresponding to the Baseline value is subtracted in order to reproduce the value of the Baseline objective function when no variation occurs from the Baseline demands. The non-linear formulation of the elastic demand functions implemented in TIMES follows these expressions.

The corresponding linearized formulations are based on piece-wise linear functions which approximate the integrals over the inverse demand curves, as explained in Part I, Chapter 4. The method described there has been generalized to linearize also the somewhat more complex CES demand functions, allowing also for nested CES functions. Each demand having own-price or substitution elasticities requires the definition of as many variables as there are steps in the discrete representation of the demand curve (both upward and downward), for each period and region. Each such variable has an upper bound, and in the CES formulation they are included in an additional balance equation. However, otherwise the step variables are not involved in other new constraints. Therefore, the linear program is augmented by a number of variables, but does not have any notable number of more constraints than the initial inelastic LP. For partial equilibrium models, volume-preserving demand functions may, however, be preferred over standard CES formulations, and therefore an option for using a simple volume-preserving variant of the CES linearization has been also implemented.

The resulting linearization has been verified to work well over a large range of demand elasticities and price changes, and indeed also with nested CES functions. Cobb-Douglas functions (*σ* = 1) are also supported. Using the same linearization approach, even the simple Macro general equilibrium model, which is integrated in TIMES-Macro and includes Cobb-Douglas function nested into a CES production function, might be in principle linearized into an LP problem.

It is also important to note again here that, instead of maximizing the net total surplus, TIMES minimizes its negative (plus a constant). For this and other reasons, it is inappropriate to pay too much attention to the meaning of the *absolute* objective function values. Rather, examining the difference between the objective function values of two scenarios is a far more useful exercise. That difference is of course, the negative of the difference between the net total surpluses of the two scenario runs.
