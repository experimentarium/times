(b-mathematical-formulations)=
# Mathematical formulation

We now describe the mathematical formulation used for the damage cost functions.

With respect to optimization, two distinct approaches to account for damage costs can be distinguished:

1. Environmental damages are computed ex-post, without feedback into the optimization process, and
2. Environmental damages are part of the objective function and therefore taken into account in the optimization process.

In both approaches, a number of assumptions are made:

- Emissions in each region may be assumed to cause damage only in the same region or, due to trans-boundary pollution, also in other regions; however, all damage costs are allocated to the polluters in the source region, in accordance with the Polluter Pays Principle, or Extended Polluter Responsibility;
- Damages in a given time period are linked to emissions in that same period only (damages are not delayed, nor are they cumulative); and
- Damages due to several pollutants are the sum of damages due to each pollutant (no cross impacts).

In a given time period, and for a given pollutant, the damage cost is modeled as follows:

$$DAM(EM) = \alpha \cdot EM^{\beta + 1}$$ (2-8-1)

where:

- EM is the emission in the current period;
- DAM is the damage cost in the current period;
- *β* ≥ 0 is the elasticity of marginal damage cost to amount of emissions; and
- *α* \> 0 is a calibrating parameter, which may be obtained from dose-response studies that allow the computation of the marginal damage cost per unit of emission at some reference level of emissions.

If we denote the marginal cost at the reference level $MC_{0}$, the following holds:

$$MC_{0} = \alpha \cdot (\beta + 1) \cdot EM_{0}^{\beta}$$ (2-8-2)

where $EM_0$ is the reference amount of emissions. Therefore expression {eq}`2-8-1` may be re-written as:

$$DAM(EM) = MC_{0} \cdot \frac{EM^{\beta + 1}}{(\beta + 1) \cdot EM_{0}^{\beta}}$$ (2-8-3)

The marginal damage cost is therefore given by the following expression:

$$MC(EM) = MC_{0} \cdot \frac{EM^{\beta}}{EM_{0}^{\beta}}$$ (2-8-4)

The approach to damage costs described in this section applies more particularly to local pollutants. Extension to global emissions such GHG emissions requires the use of a global TIMES model and a reinterpretation of the equations discussed above.

The modeling of damage costs via equation {eq}`2-8-3` introduces a non-linear term in the objective function if the ***β*** parameter is strictly larger than zero. This in turn requires that the model be solved via a Non-Linear Programming (NLP) algorithm rather than a LP algorithm. However, the resulting Non-Linear Program remains convex as long as the elasticity parameter is equal to or larger than zero. For additional details on convex programming, see Nemhauser et al (1989). If linearity is desired (for instance if problem instances are very large), we can approximate expression {eq}`2-8-3` by a sequence of linear segments with increasing slopes, and thus obtain a Linear Program.

The linearization can be done by choosing a suitable range of emissions, and dividing that range into *m* intervals below the reference level, and *n* intervals above the reference level. We also assume a middle interval centered at the reference emission level. To each interval corresponds one step variable *S*. Thus, we have for emissions:

$$EM = \sum_{i = 1}^{m}S_{i}^{lo} + S^{mid} + \sum_{i = 1}^{n}S_{i}^{up}$$ (2-8-5)

The damage cost can then be written as follows:

$$DAM(EM) = \sum_{i = 1}^{m}{MC_{i}^{lo} \cdot S_{i}^{lo}} + MC_{0} \cdot S^{mid} + \sum_{i = 1}^{n}{MC_{i}^{up} \cdot S_{i}^{up}}$$ (2-8-6)

where:

- $MC_{i}^{lo}$ and $MC_{i}^{up}$ are the approximate marginal costs at each step below and above the reference level as shown in {eq}`2-8-7` below; and
- $S_{i}^{lo}$, $S^{mid}$ and $S_{i}^{up}$ are the non-negative step variables for emissions. Apart from the final step, each step variable has an upper bound equal to the width of the interval. In this formulation we choose intervals of uniform width on each side of the reference level. However, the intervals below and above the reference level can have different sizes. The width of the middle interval is always the average of the widths below and above the reference level.

The approximate marginal costs at each step can be assumed to be the marginal costs at the center of each step. If all the steps intervals are of equal size, the marginal costs for the steps below the reference level are obtained by the following formula:

$$MC_{i}^{lo} = MC_{0} \cdot \left( \frac{(i - 0.5)}{(m + 0.5)} \right)^{\beta}$$ (2-8-7)

Formulas for the marginal costs of the other steps can be derived similarly.

The TIMES implementation basically follows the equations shown above. Both the non-linear and linearized approaches can be used. However, in order to provide some additional flexibility, the implementation supports also defining a threshold level of emissions, below which the damage costs are zero. This refinement can be taken into account in the balance equation {eq}`2-8-5` by adding one additional step variable having an upper bound equal to the threshold level, and by adjusting the widths of the other steps accordingly. The threshold level can also easily be taken into account in the formulas for the approximate marginal costs.

In addition, the implementation supports different elasticities and step sizes to be used below and above the reference level. See Section {numref}`%s <b-switches-and-parameters>` for more details.
