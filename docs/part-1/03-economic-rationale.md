(economic-rationale-of-the-times)=
# Economic rationale of the TIMES modeling approach

This chapter provides a detailed economic interpretation of TIMES and other partial equilibrium models based on maximizing total surplus. Partial equilibrium models have one common feature -- they simultaneously configure the production and consumption of commodities (i.e. fuels, materials, and energy services) and their prices. The price of producing a commodity affects the demand for that commodity, while at the same time the demand affects the commodity's price. A market is said to have reached an equilibrium at prices *p\** and quantities *q\** when no consumer wishes to purchase less than *q\** and no producer wishes to produce more than *q\** at price *p\**. Both *p\** and *q\** are vectors whose dimension is equal to the number of different commodities being modeled. As will be explained below, when all markets are in equilibrium the total economic surplus is maximized.

The concept of total surplus maximization extends the direct cost minimization approach upon which earlier bottom-up energy system models were based. These simpler models had fixed energy service demands, and thus were limited to minimizing the cost of supplying these demands. In contrast, the TIMES demands for energy services are themselves elastic to their own prices, thus allowing the model to compute a *bona fide* supply-demand equilibrium. This feature is a fundamental step toward capturing the main feedback from the economy to the energy system.

Section {numref}`%s <brief-classification-of-energy-models>` provides a brief review of different types of energy models. Section {numref}`%s <core-times-paradigm>` discusses the economic rationale of the TIMES model with emphasis on the features that distinguish TIMES from other bottom-up models (such as the early incarnations of MARKAL, see Fishbone and Abilock, 1981 and Berger et al., 1992, though MARKAL has since been extended beyond these early versions). Section 3.3 describes the details of how price elastic demands are modeled in TIMES, and section 3.4 provides additional discussion of the economic properties of the model.

(brief-classification-of-energy-models)=
## A brief classification of energy models

Many energy models are in current use around the world, each designed to emphasize a particular facet of interest. Differences include: economic rationale, level of disaggregation of the variables, time horizon over which decisions are made (which is closely related to the type of decisions, i.e., only operational planning or also investment decisions), and geographic scope. One of the most significant differentiating features among energy models is the degree of detail with which commodities and technologies are represented, which will guide our classification of models into two major classes, as explained in the following very streamlined classification.

### 'Top-down' models

At one end of the spectrum are aggregated *General Equilibrium* (GE) models. In these each sector is represented by a production function designed to simulate the potential substitutions between the main factors of production (also highly aggregated into a few variables such as: energy, capital, and labor) in the production of each sector's output. In this model category are found a number of models of national or global energy systems. These models are usually called "top-down", because they represent an entire economy via a relatively small number of aggregate variables and equations. In these models, production function parameters are calculated for each sector such that inputs and outputs reproduce a single base historical year.[^11] In policy runs, the mix of inputs[^12] required to produce one unit of a sector's output is allowed to vary according to user-selected elasticities of substitution. Sectoral production functions most typically have the following general form:

$X_{s} = A_{0}\left( B_{K} \cdot K_{s}^{\rho} + B_{L} \cdot L_{S}^{\rho} + B_{E} \cdot E_{S}^{\rho} \right)^{1/\rho}$ (3-1)

where 

> $X_{S}$ is the output of sector $S$,
> 
> $K_{S}$, $L_{S}$, and $E_{S}$ are the inputs of capital, labor and energy needed to produce one unit of output in sector $S$,
> 
> $\rho$ is the elasticity of substitution parameter,
> 
> $A_{0}$ and the $B$ 's are scaling coefficients.

The choice of *ρ* determines the ease or difficulty with which one production factor may be substituted for another: the smaller $\rho$ is (but still greater than or equal to 1), the easier it is to substitute the factors to produce the same amount of output from sector $S$. Also note that the degree of factor substitutability does not vary among the factors of production --- the ease with which capital can be substituted for labor is equal to the ease with which capital can be substituted for energy, while maintaining the same level of output. GE models may also use alternate forms of production function (3-1), but retain the basic idea of an explicit substitutability of production factors.

### 'Bottom-up' models

At the other end of the spectrum are the very detailed, *technology explicit* models that focus primarily on the energy sector of an economy. In these models, each important energy-using technology is identified by a detailed description of its inputs, outputs, unit costs, and several other technical and economic characteristics. In these so-called 'bottom-up' models, a sector is constituted by a (usually large) number of logically arranged technologies, linked together by their inputs and outputs (*commodities*, which may be energy forms or carriers, materials, emissions and/or demand services). Some bottom-up models compute a partial equilibrium via maximization of the total net (consumer and producer) surplus, while others simulate other types of behavior by economic agents, as will be discussed below. In bottom-up models, one unit of sectoral output (e.g., a billion vehicle kilometers, one billion tonnes transported by heavy trucks or one petajoule of residential cooling service) is produced using a mix of individual technologies' outputs. Thus the production function of a sector is *implicitly* constructed, rather than explicitly specified as in more aggregated models. Such implicit production functions may be quite complex, depending on the complexity of the reference energy system of each sector (sub-RES).

### Hybrid approaches

While the above dichotomy applied fairly well to earlier models, these distinctions now tend to be somewhat blurred by advances in both categories of model. In the case of aggregate top-down models, several general equilibrium models now include a fair amount of fuel and technology disaggregation in the key energy producing sectors (for instance: electricity production, oil and gas supply). This is the case with MERGE[^13] and SGM[^14], among others.

In the other direction, the more advanced bottom-up models are 'reaching up' to capture some of the effects of the entire economy on the energy system. The TIMES model has end-use demands (including demands for industrial output) that are sensitive to their own prices, and thus captures the impact of rising energy prices on economic output and *vice versa*. Recent incarnations of technology-rich models (including TIMES) are multi-regional, and thus are able to consider the impacts of energy-related decisions on trade. It is worth noting that while the multi-regional top-down models have always represented trade, they have done so with a very limited set of traded commodities -- typically one or two, whereas there may be quite a number of traded energy forms and materials in multi-regional bottom-up models.

MARKAL-MACRO (Manne and Wene, 1992) and TIMES-MACRO (Kypreos and Lehtila, 2013) are hybrid models combining the technological detail of MARKAL with a succinct representation of the macro-economy consisting of a single producing sector in a single region. Because of its succinct single-sector production function, MARKAL-MACRO is able to compute a general equilibrium in a single optimization step. More recently, TIMES_MACRO-MSA (section {numref}`%s <the-single-region-times-macro-model>`) is based on the computation of a multi-regional global equilibrium, but requires an iterative process to do so. MESSAGE (Messner and Strubegger, 1995) links a bottom-up model based on the EFOM paradigm with a macro module, and computes a global, multi-regional equilibrium iteratively. The NEMS (US EIA, 2000) model is another example of a full linkage between several technology rich modules of the various energy subsectors and a set of macro-economic equations, and requires iterative resolution methods.

In spite of these advances in both classes of models, there remain important differences. Specifically:
- Top-down models encompass macroeconomic variables beyond the energy sector proper, such as wages, consumption, and interest rates, and
- Bottom-up models have a rich representation of the variety of technologies (existing and/or future) available to meet energy needs, and, they often have the capability to track a much wider variety of traded commodities. They are also more adapted to the representation of micro policies targeting specific technologies or commodities.

The top-down vs. bottom-up approach is not the only relevant difference among energy models. Among top-down models, the so-called Computable General Equilibrium models (CGE) described above differ markedly from the *macro econometric models*. The latter do not compute equilibrium solutions, but rather simulate the flows of capital and other monetized quantities between sectors (see, e.g., Meade, 1996 on the LIFT model). They use econometrically derived input-output coefficients to compute the impacts of these flows on the main sectoral indicators, including economic output (GDP) and other variables (labor, investments). The sector variables are then aggregated into national indicators of consumption, interest rate, GDP, labor, and wages.

Among technology explicit models also, two main classes are usually distinguished: the first class is that of the partial equilibrium models such as MARKAL, MESSAGE, and TIMES, that use optimization techniques to compute a least cost (or maximum surplus) path for the energy system. The second class is that of *simulation* models, where the emphasis is on representing a system not governed purely by financial costs and profits. In these simulation models (e.g., CIMS, Jaccard et al. 2003), investment decisions taken by a representative agent (firm or consumer) are only partially based on profit maximization, and technologies may capture a share of the market even though their life-cycle cost may be higher than that of other technologies. Simulation models use market-sharing formulas that preclude the easy computation of equilibrium -- at least not in a single pass. The SAGE (US EIA, 2002) incarnation of the MARKAL model possesses a market sharing mechanism that allows it to reproduce certain behavioral characteristics of observed markets.

(core-times-paradigm)=
## The core TIMES paradigm

In the rest of this chapter, we present the properties of the **core TIMES** paradigm. As will be seen in chapters {numref}`%s <stochastic-programming-extension>` to {numref}`%s <general-equilibrium-extensions>`, some of these properties are not applicable to several important TIMES variants. The reader should keep this caveat in mind when contemplating the use of some features that are described in these 5 chapters.

Since certain portions of this and the next sections require an understanding of the concepts and terminology of Linear Programming, the reader requiring a brush-up on this topic may first read [Appendix B](appendix-b-linear-programming), and then, if needed, some standard textbook on LP, such as Hillier and Lieberman (2009), Chvàtal (1983), or Schrijver (1986). The application of Linear Programming to microeconomic theory is covered in two historically important references, Gale (1960 and 11th edition 1989), and in Dorfman, Samuelson, and Solow (1958, and 1987 reprint).

A brief description of the core TIMES model generator would express that it is:
- *Technologically explicit, integrated*;
- *Multi-regional*; and
- *Partial equilibrium* (with *price elastic* demands for energy services) in *competitive markets* with *perfect foresight*. It will be seen that such an equilibrium entails *marginal value pricing* of all commodities.

We now proceed to flesh out each of these properties.

### A technologically explicit integrated model

As already presented in chapter {numref}`%s <the-basic-structure-of-the-core>` (and described in much more detail in Part II, section {numref}`%s <parameters>`), each technology is described in TIMES by a number of technical and economic parameters. Thus each technology is explicitly identified (given a unique name) and distinguished from all others in the model. A mature TIMES model may include several thousand technologies in all sectors of the energy system (energy procurement, conversion, processing, transmission, and end-uses) in each region. Thus TIMES is not only technologically explicit, it is technology rich and it is integrated as well. Furthermore, the number of technologies and their relative topology may be changed at will, purely via data input specification, without the user ever having to modify the model's equations. The model is thus to a large extent *data driven*.

### Multi-regional

Some existing TIMES models comprise several dozen regional modules, or more. The number of regions in a model is limited only by the difficulty of solving LP's of very large size. The individual regional modules are linked by energy and material trading variables, and by emission permit trading variables, if desired. The linking variables transform the set of regional modules into a *single* multi-regional (possibly global) energy model, where actions taken in one region may affect all other regions. This feature is essential when global as well as regional energy and emission policies are being simulated. Thus a multi-regional TIMES model is geographically integrated.

### Partial equilibrium

The core version of TIMES computes a partial equilibrium on energy markets. This means that the model computes both the *flows* of energy forms and materials as well as their *prices*, in such a way that, at the prices computed by the model, the suppliers of energy produce exactly the amounts that the consumers are willing to buy. This equilibrium feature is present at every stage of the energy system: primary energy forms, secondary energy forms, and energy services[^15]. A supply-demand equilibrium model has as its economic rationale the maximization of the total surplus, defined as the sum of all suppliers' and consumers' surpluses. The mathematical method used to maximize the surplus must be adapted to the particular mathematical properties of the model. In TIMES, these properties are as follows:
- Outputs of a technology are linear functions of its inputs (subsection {numref}`%s <partial-equilibrium-linearity>`)[^16];
- Total economic surplus is maximized over the entire horizon ({numref}`%s <maximization-of-total-surplus>`); and
- Energy markets are competitive, with perfect foresight ({numref}`%s <competitive-energy-markets-with-perfect-foresight>`)[^17].

As a result of these assumptions the following additional properties hold:
- The market price of each commodity is equal to its marginal value in the overall system ({numref}`%s <marginal-value-pricing>`); and
- Each economic agent maximizes its own profit or utility ({numref}`%s <profit-maximization-the-invisible-hand>`).

(partial-equilibrium-linearity)=
#### Linearity

A linear input-to-output relationship first means that each technology represented may be implemented at any capacity, from zero to some upper limit, without economies or diseconomies of scale. In a real economy, a given technology is usually available in discrete sizes, rather than on a continuum. In particular, for some real life technologies, there may be a minimum size below which the technology may not be implemented (or else at a prohibitive cost), as for instance a nuclear power plant, or a hydroelectric project. In such cases, because TIMES assumes that all technologies may be implemented in any size, it may happen that the model's solution shows some technology's capacity at an unrealistically small size. It should however be noted that in most applications, such a situation is relatively infrequent and often innocuous, since the scope of application is at the country or region's level, and thus large enough so that small capacities are unlikely to occur.

On the other hand, there may be situations where plant size matters, for instance when the region being modeled is very small. In such cases, it is possible to enforce a rule by which certain capacities are allowed only in multiples of a given size (e.g., build or not a gas pipeline), by introducing *integer variables*. This option, referred to as lumpy investment (LI), is available in TIMES and is discussed in chapter {numref}`%s <the-lumpy-investment-extension>`. This approach should, however, be used sparingly because it may greatly increase solution time.

It is the linearity property that allows the TIMES equilibrium to be computed using Linear Programming techniques. In the case where economies of scale or some other non-convex relationship is important to the problem being investigated, the optimization program would no longer be linear or even convex. We shall examine such cases in chapters {numref}`%s <using-times-with-limited-foresight>` to {numref}`%s <general-equilibrium-extensions>`.

We must now mention a common misconception regarding linearity: the fact that TIMES equations are linear *does not mean that production functions behave in a linear fashion; far from it*. Indeed, the TIMES production functions are usually highly non-linear (although convex), consisting of a stepped sequence of linear functions. As a simple example, a supply of some resource is almost always represented as a sequence of segments, each with rising (but constant within an interval) unit cost. The modeler defines the 'width' of each interval so that the resulting supply curve may simulate any non-linear convex function. In brief, diseconomies of scale are easily represented in linear models.

(maximization-of-total-surplus)=
#### Maximization of total surplus: Price equals marginal value

The *total surplus* of an economy is the sum of the suppliers' and the consumers' surpluses. The term *supplier* designates any economic agent that produces (and/or sells) one or more commodities i.e., in TIMES, an energy form, a material, an emission permit, and/or an energy service. A *consumer* is a buyer of one or more commodities. In TIMES, the suppliers of a commodity are technologies that procure a given commodity, and the consumers of a commodity are technologies or service segments that consume a given commodity. Some (indeed most) technologies are both suppliers and consumers. Therefore, for each commodity the RES defines a complex set of suppliers and consumers.

It is customary in microeconomics to represent the set of suppliers of a commodity by their *inverse production function*, that plots the marginal production cost of the commodity (vertical axis) as a function of the quantity supplied (horizontal axis). In TIMES, as in other linear optimization models, the supply curve of a commodity, with the exception of end-use demands, is entirely determined endogenously by the model. It is a standard result of Linear Programming theory that the inverse supply function is step-wise constant and increasing in each factor (see {numref}`eq-supply-demand-endogenous` and {numref}`eq-fixed-energy-service` for the case of a single commodity[^18]). Each horizontal step of the inverse supply function indicates that the commodity is produced by a certain technology or set of technologies in a strictly linear fashion. As the quantity produced increases, one or more resources in the mix (either a technological potential or some resource's availability) is exhausted, and therefore the system must start using a different (more expensive) technology or set of technologies in order to produce additional units of the commodity, albeit at higher unit cost. Thus, each change in production mix generates one step of the staircase production function with a value higher than the preceding step. The width of any particular step depends upon the technological potential and/or resource availability associated with the set of technologies represented by that step.

```{figure} assets/supply-demand-equilibrium.svg
:name: eq-supply-demand-endogenous
:align: center

Equilibrium in the case of an energy form: the model implicitly constructs both the supply and the demand curves (note that the equilibrium is multiple in this configuration).
```

In a similar manner, each TIMES model instance defines a series of inverse demand functions. In the case of demands, two cases are distinguished. First, if the commodity in question is an energy carrier whose production and consumption are endogenous to the model, then its demand function is *implicitly* constructed within TIMES, and is a step-wise constant, decreasing function of the quantity demanded, as illustrated in {numref}`eq-supply-demand-endogenous` for a single commodity. If on the other hand the commodity is a demand for an energy service, then its demand curve is *defined by the user* via the specification of the own-price elasticity of that demand, and the curve is in this instance a smoothly decreasing curve as illustrated in {numref}`eq-demand-curve`[^19]. In both cases, the supply-demand equilibrium is at the intersection of the supply function and the demand function, and corresponds to an equilibrium quantity $Q_E$ and an equilibrium price $P_E$[^20]. At price $P_E$, suppliers are willing to supply the quantity $Q_E$ and consumers are willing to buy exactly that same quantity $Q_E$. Of course, the TIMES equilibrium concerns a large number of commodities simultaneously, and thus the equilibrium is a multi-dimensional analog of the above, where $Q_E$ and $P_E$ are now vectors rather than scalars.

As already mentioned, the demand curves of most TIMES commodities (i.e. energy carriers, materials, emission permits) are implicitly constructed endogenously as an integral part of the solution of the LP. For each commodity that is an energy service, the user *explicitly* defines the demand *function* by specifying its own price elasticity. In TIMES, each energy service demand is assumed to have a constant own price elasticity function of the form (see {numref}`eq-demand-curve`):

$$DM/DM_{0} = (P/P_{0})^{E}$$ (3-2)

Where $\{DM_0,P_0\}$ is a reference pair of demand and price values for that energy service over the forecast horizon, and $E$ is the (negative) own price elasticity of that energy service demand, as specified by the user (note that although not obvious from the notation, this price elasticity may vary over time). The pair $\{DM_0,P_0\}$ is obtained by solving TIMES for a reference scenario. More precisely, $DM_0$ is the demand projection estimated by the user in the reference scenario (usually based upon explicitly defined relationships to economic and demographic drivers), and $P_0$ is the shadow price of that energy service demand in the dual solution of the reference case scenario. The precise manner in which the demand functions are discretized and incorporated in the TIMES objective function is explained in chapter {numref}`%s <core-times-model-mathematics>`.

Using {numref}`eq-supply-demand-endogenous` as an example, the definition of the suppliers' surplus corresponding to a certain point S on the inverse supply curve is the difference between the total revenue and the total cost of supplying a commodity, i.e. the gross profit. In {numref}`eq-supply-demand-endogenous`, the surplus is thus the area between the horizontal segment SS' and the inverse supply curve. Similarly, the consumers' surplus for a point C on the inverse demand curve, is defined as the area between line segment CC' and the inverse demand curve. This area is a consumer's analog to a producer's profit; more precisely it is the cumulative opportunity gain of all consumers who purchase the commodity at a price lower than the price they would have been willing to pay. Thus, for a given quantity $Q$, the total surplus (suppliers' plus consumers') is simply the area between the two inverse curves situated at the left of $Q$. It should be clear from {numref}`eq-supply-demand-endogenous` that the total surplus is maximized when $Q$ is exactly equal to the equilibrium quantity $Q_E$. Therefore, we may state (in the single commodity case) the following Equivalence Principle:

> *"The supply-demand equilibrium is reached when the total surplus is maximized."*

This is a remarkably useful result, as it leads to a method for computing the equilibrium, as will be see in much detail in Chapter {numref}`%s <core-times-model-mathematics>`.

In the multi-dimensional case, the proof of the above statement is less obvious, and requires a certain qualifying property (called the integrability property) to hold (Samuelson, 1952, Takayama and Judge, 1972). One sufficient condition for the integrability property to be satisfied is realized when the cross-price elasticities of any two energy forms are equal, viz.

$$\partial P_{j}/\partial Q_{i} = \partial P_{i}/\partial Q_{j} \quad \text{for all } i,j$$

In the case of commodities that are end-use energy services, these conditions are trivially satisfied in TIMES because we have assumed zero cross price elasticities. In the case of an endogenous energy carrier, where the demand curve is implicitly derived, it is also easy to show that the integrability property is always satisfied[^21]. Thus the equivalence principle is valid in all cases.

In summary, the equivalence principle guarantees that the TIMES supply-demand equilibrium maximizes total surplus. The total surplus concept has long been a mainstay of social welfare economics because it takes into account both the surpluses of consumers and of producers.[^22]

```{figure} assets/energy-service-elastic-demand.svg
:name: eq-demand-curve
:align: center

Equilibrium in the case of an energy service: the user explicitly provides the demand curve, usually using a simple functional form (see text for details).
```

*Remark:* In older versions of MARKAL, and in several other least-cost bottom-up models, energy service demands are exogenously specified by the modeler, and only the cost of supplying these energy services is minimized. Such a case is illustrated in {numref}`eq-fixed-energy-service` where the "inverse demand curve" is a vertical line. The objective of such models was simply the minimization of the total cost of meeting exogenously specified levels of energy service.

```{figure} assets/energy-service-inelastic-demand.svg
:name: eq-fixed-energy-service
:align: center

Equilibrium when an energy service demand is fixed.
```

(competitive-energy-markets-with-perfect-foresight)=
#### Competitive energy markets with perfect foresight

Competitive energy markets are characterized by perfect information and atomic economic agents, which together preclude any of them from exercising market power. That is, neither the level at which any individual producer supplies, nor the level any individual consumer acquires, affects the equilibrium market price (because there are many other buyers and sellers to replace them). It is a standard result of microeconomic theory that the assumption of competitive markets entails that the market price of a commodity is equal to its marginal value in the economy (Samuelson, 1952). This is of course also verified in the TIMES economy, as discussed in the next subsection.

Of course, real world energy markets are not always competitive. For instance, an electric utility company may be a (regulated) monopoly within an entire country, or a cartel of oil producing countries may have market power on oil markets. There are ways around these so-called "market imperfections". For instance, concerning the monopolistic utility, a socially desirable approach would be to first use the assumption of marginal cost pricing, so as to determine a socially optimal plan for the monopoly, and then to have the regulatory agency enforce such a plan, including the principle of marginal cost pricing. The case of the oil producers' cartel is less simple, since there is no global regulatory agency to ensure that oil producers act in a socially optimal fashion. There are however ways to use equilibrium models such as TIMES in order to faithfully represent the market power of certain economic agents, as exemplified in (Loulou et al., 2007).

In the core version of TIMES, the perfect information assumption extends to the entire planning horizon, so that each agent has perfect foresight, i.e. complete knowledge of the market's parameters, present and future. Hence, the equilibrium is computed by maximizing total surplus in one pass for the entire set of periods. Such a farsighted equilibrium is also called an *inter-temporal dynamic equilibrium*.

Note that there are at least two ways in which the perfect foresight assumption may be voided: in one variant, agents are assumed to have foresight over a limited portion of the horizon, say one or a few periods. Such an assumption of limited foresight is embodied in the TIMES feature discussed in chapter {numref}`%s <using-times-with-limited-foresight>`, as well as in the SAGE variant of MARKAL (US EIA, 2002). In another variant, foresight is assumed to be imperfect, meaning that agents may only *probabilistically* know certain key future events. This assumption is at the basis of the TIMES Stochastic Programming option, discussed in chapter {numref}`%s <stochastic-programming-extension>`.

(marginal-value-pricing)=
### Marginal value pricing

We have seen in the preceding subsections that the TIMES equilibrium occurs at the intersection of the inverse supply and inverse demand curves. It follows that the equilibrium prices are equal to the marginal system values of the various commodities. From a different angle, the duality theory of Linear Programming (chapter {numref}`%s <appendix-b-linear-programming>`) indicates that for each constraint of the TIMES linear program there is a *dual variable.* This dual variable (when an optimal solution is reached) is also called the constraint's *shadow price*[^23]*,* and is equal to the marginal change of the objective function per unit increase of the constraint's right-hand-side. For instance, the shadow price of the balance constraint of a commodity (whether it be an energy form, material, a service demand, or an emission) represents the competitive market price of the commodity.

The fact that the price of a commodity is equal to its marginal value is an important feature of competitive markets. Duality theory does not necessarily indicate that the marginal value of a commodity is equal to the marginal cost of *producing* that commodity. For instance, in the equilibrium shown in {numref}`eq-price-different-marginal-cost` the price does not correspond to *any* marginal supply cost, since it is situated at a discontinuity of the inverse supply curve. In this case, the price is precisely determined by demand rather than by supply, and the term *marginal cost pricing* (so often used in the context of optimizing models) is *sensu stricto* incorrect. The term *marginal value pricing* is a more appropriate term to use.

It is important to reiterate that marginal value pricing *does not imply that suppliers have zero profit*. Profit is exactly equal to the suppliers' surplus, and is generally positive. Only the last few units produced may have zero profit, if, and when, their production cost equals the equilibrium price.

In TIMES the shadow prices of commodities play a very important diagnostic role. If some shadow price is clearly out of line (i.e. if it seems much too small or too large compared to the anticipated market prices), this indicates that the model's database may contain some errors. The examination of shadow prices is just as important as the analysis of the quantities produced and consumed of each commodity and of the technological investments.

```{figure} assets/intermediate-equilibrium-price.svg
:name: eq-price-different-marginal-cost
:align: center

Case where the equilibrium price is not equal to any marginal supply cost.
```

(profit-maximization-the-invisible-hand)=
### Profit maximization: the Invisible Hand

An interesting property may be derived from the assumptions of competitiveness. While the avowed objective of the TIMES model is to maximize the overall surplus, it is also true that each economic agent in TIMES maximizes its own surplus. This property is akin to the famous 'invisible hand' property of competitive markets, and may be established rigorously by the following theorem that we state in an informal manner:

> *<ins>Theorem:</ins> Let (p\*,q\*) be a pair of equilibrium vectors that maximize total surplus. If we now replace the original TIMES linear program by one where all commodity prices are <ins>fixed</ins> at value p\*, and we let each agent maximize its own surplus, the vector of optimal quantities produced or purchased by the agents also maximizes the total surplus*[^24]*.*

This property is important inasmuch as it provides an alternative justification for the class of equilibria based on the maximization of total surplus. It is now possible to shift the model's rationale from a global, societal one (total surplus maximization), to a local, decentralized one (individual utility maximization). Of course, the equivalence suggested by the theorem is valid only insofar as the marginal value pricing mechanism is strictly enforced --- that is, neither an individual producer nor an individual consumer may affect market prices --- both are price takers. Clearly, some markets are not competitive in the sense the term has been used here. For example, the behavior of a few oil producers has a dramatic impact on world oil prices, which then depart from their marginal system value. Market power[^25] may also exist in cases where a few consumers dominate a market.


[^11]: These models assume that the relationships (as defined by the form of the production functions as well as the calculated parameters) between sector level inputs and outputs are in equilibrium in the base year.

[^12]: Most models use inputs such as labor, energy, and capital, but other input factors may conceivably be added, such as arable land, water, or even technical know-how. Similarly, labor may be further subdivided into several categories.

[^13]: Model for Evaluating Regional and Global Effects (Manne et al., 1995)

[^14]: Second Generation Model (Edmonds et al., 1991)

[^15]: It has been argued, based on strong experimental evidence, that the change in demands for energy services indeed captures the main economic impact of energy system policies on the economy at large (Loulou and Kanudia, 2000)

[^16]: This property does not hold in three TIMES extensions presented in Chapters {numref}`%s <the-lumpy-investment-extension>`-{numref}`%s <general-equilibrium-extensions>`.

[^17]: These two properties do not hold in the time-stepped extension of TIMES (chapter {numref}`%s <using-times-with-limited-foresight>`) and in Stochastic TIMES (Chapter {numref}`%s <stochastic-programming-extension>`.)

[^18]: This is so because in Linear Programming the shadow price of a constraint remains constant over a certain interval, and then changes abruptly, giving rise to a stepwise constant functional shape.

[^19]: This smooth curve will be discretized later for computational purposes, and thus become a staircase function, as described in section 4.2

[^20]: As may be seen in {numref}`eq-supply-demand-endogenous`, the equilibrium is not necessarily unique. In the case shown, any point on the vertical segment containing the equilibrium is also an equilibrium, with the same quantity $Q_E$ but a different price. In other situations, the multiple equilibria may have a single price but multiple quantities.

[^21]: This results from the fact that in TIMES each price $P_i$ is the shadow price of a balance constraint (see section 5.4.4), and may thus be (loosely) expressed as the derivative of the objective function $F$ with respect to the right-hand-side of a balance constraint, i.e. $\partial F/\partial Q_i$. When that price is further differentiated with respect to another quantity $Q_j$, one gets $\partial^2 F/(\partial Q_i \cdot \partial Q_j)$, which, under mild conditions is always equal to $\partial^2 F/(\partial Q_j \cdot \partial Q_i)$, as desired.

[^22]: See e.g. Samuelson and Nordhaus (1977)

[^23]: The term *shadow price* is often used in the mathematical economics literature, whenever the price is derived from the marginal value of a commodity. The qualifier 'shadow' is used to distinguish the competitive market price from the price observed in the real world, which may be different, as is the case in regulated industries or in sectors where either consumers or producers exercise market power, or again when other market imperfections exist. When the equilibrium is computed using LP optimization, as is the case for TIMES, the shadow price of each commodity is computed as the dual variable of that commodity's balance constraint, see chapter {numref}`%s <appendix-b-linear-programming>`

[^24]: However, the resulting Linear Program has multiple optimal solutions. Therefore, although *q*\* is an optimal solution, it is not necessarily the one found when the modified LP is solved.

[^25]: An agent has market power if its decisions, all other things being equal, have an impact on the market price. Monopolies and oligopolies are example of markets where one or several agents have market power.
