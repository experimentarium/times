# Introduction to the TIMES model

## A brief summary

TIMES (an acronym for The Integrated MARKAL-EFOM[^1] System) is an economic model generator for local, national, multi-regional, or global energy systems, which provides a technology-rich basis for representing energy dynamics over a multi-period time horizon. It is usually applied to the analysis of the entire energy sector, but may also be applied to study single sectors such as the electricity and district heat sector.

Estimates of end-use energy service demands (e.g., car road travel; residential lighting; steam heat requirements in the paper industry; etc.) are provided by the user for each region to drive the reference scenario. In addition, the user provides estimates of the existing stocks of energy related equipment in all sectors, and the characteristics of available future technologies, as well as present and future sources of primary energy supply and their potentials.

Using these as inputs, the TIMES model aims to supply energy services at minimum global cost (more accurately at minimum loss of total surplus) by simultaneously making decisions on equipment investment and operation; primary energy supply; and energy trade for each region. For example, if there is an increase in residential lighting energy service relative to the reference scenario (perhaps due to a decline in the cost of residential lighting, or due to a different assumption on GDP growth), either existing generation equipment must be used more intensively or new -- possibly more efficient -- equipment must be installed. The choice by the model of the generation equipment (type and fuel) is based on the analysis of the characteristics of alternative generation technologies, on the economics of the energy supply, and on environmental criteria. TIMES is thus a vertically integrated model of the entire extended energy system.

The scope of the model extends beyond purely energy-oriented issues, to the representation of environmental emissions, and perhaps materials, related to the energy system. In addition, the model is suited to the analysis of energy-environmental policies, which may be represented with accuracy thanks to the explicitness of the representation of technologies and fuels in all sectors.

In TIMES -- like in its MARKAL forebear -- the quantities and prices of the various commodities are in equilibrium, i.e. their prices and quantities in each time period are such that the suppliers produce exactly the quantities demanded by the consumers. This equilibrium has the property that the total economic surplus is maximized.

## Driving a TIMES model via scenarios

The TIMES model is particularly suited to the *exploration* of possible energy futures based on contrasted *scenarios*. Given the long horizons that are usually simulated with TIMES, the scenario approach is really the only choice (whereas for the shorter term, econometric methods may provide useful projections). Scenarios, unlike forecasts, do not pre-suppose knowledge of the main drivers of the energy system. Instead, a scenario consists of a set of *coherent assumptions* about the future trajectories of these drivers, leading to a coherent organization of the system under study. A scenario builder must therefore carefully test the scenario assumptions for internal coherence, via a credible *storyline*.

In TIMES, a complete scenario consists of four types of inputs: energy service demand curves, primary resource supply curves, a policy setting, and the descriptions of a complete set of technologies. We now present a few comments on each of these four components.

### The Demand component of a TIMES scenario

In the case of the TIMES model, demand drivers (population, GDP, households, etc.) are obtained externally, via other models or from accepted other sources. As one example, several global instances of TIMES (e.g. Loulou, 2007) use the GEM-E3[^2] to generate a set of *coherent* (national and sectoral) output growth rates in the various regions. Note that GEM-E3 or GEMINI-E3 themselves use other drivers as inputs, in order to derive GDP trajectories. These drivers consist of measures of technological progress, population, degree of market competitiveness, and a few other (perhaps qualitative) assumptions. For population and household projections, TIMES instances use the same exogenous sources (IPCC, Nakicenovic 2000, Moomaw and Moreira, 2001). Other approaches may be used to derive TIMES drivers, whether via models or other means.

For the global versions of TIMES, the main drivers are: Population, GDP, GDP per capita, number of households, and sectoral outputs. For sectoral TIMES models, the demand drivers may be different depending on the system boundaries.

Once the drivers for a TIMES model are determined and quantified the construction of the reference demand scenario requires computing a set of energy service demands over the horizon. This is done by choosing elasticities of demands to their respective drivers, in each region, using the following general formula:

$$Demand = Driver^{Elasticity}$$

As mentioned above, the demands are user provided for the reference scenario only. When the model is run for alternate scenarios (for instance for an emission constrained case, or for a set of alternate technological assumptions), it is likely that the demands will be affected. TIMES has the capability of estimating the response of the demands to the changing conditions of an alternate scenario. To do this, the model requires still another set of inputs, namely the assumed elasticities of the demands to their own prices. TIMES is then able to endogenously adjust the demands to the alternate cases without exogenous intervention. In fact, the TIMES model is driven not by demands but by *demand curves*.

To summarize: the TIMES demand scenario components consist of a set of assumptions on the drivers (GDP, population, households, outputs) and on the elasticities of the demands to the drivers and to their own prices.

### The Supply component of a TIMES scenario

The second constituent of a scenario is a set of *supply curves* for primary energy and material resources. Multi-stepped supply curves are easily modeled in TIMES, each step representing a certain potential of the resource available at a particular cost. In some cases, the potential may be expressed as a cumulative potential over the model horizon (e.g. reserves of gas, crude oil, etc.), as a cumulative potential over the resource base (e.g. available areas for wind converters differentiated by velocities, available farmland for biocrops, roof areas for PV installations) and in others as an annual potential (e.g. maximum extraction rates, or for renewable resources the available wind, biomass, or hydro potentials). Note that the supply component also includes the identification of trading possibilities, where the amounts and prices of the traded commodities are determined endogenously (optionally within user imposed limits).

### The Policy component of a TIMES scenario

Insofar as some policies impact on the energy system, they become an integral part of the scenario definition. For instance, a reference scenario may perfectly ignore emissions of various pollutants, while alternate policy scenarios may enforce emission restrictions, or emission taxes, etc. The detailed technological nature of TIMES allows the simulation of a wide variety of both micro measures (e.g. technology portfolios, or targeted subsidies to groups of technologies), and broader policy targets (such as general carbon tax, or permit trading system on air contaminants). A simpler example might be a nuclear policy that limits the future capacity of nuclear plants. Another example might be the imposition of fuel taxes, or of targeted capital subsidies, etc.

### The Techno-economic component of a TIMES scenario

The fourth and last constituent of a scenario is the set of technical and economic parameters assumed for the transformation of primary resources into energy services. In TIMES, these techno-economic parameters are described in the form of *technologies* (or processes) that transform some commodities into others (fuels, materials, energy services, emissions). In TIMES, some technologies may be user imposed and others may simply be available for the model to choose from. The quality of a TIMES model rests on a rich, well developed set of technologies, both current and future, for the model to choose from. The emphasis put on the technological database is one of the main distinguishing factors of the class of Bottom-up models, to which TIMES belongs. Other classes of models will tend to emphasize other aspects of the system (e.g. interactions with the rest of the economy) and treat the technical system in a more succinct manner via aggregate production functions.

*Remark:* Two scenarios may differ in some or all of their components. For instance, the same demand scenario may very well lead to multiple scenarios by varying the primary resource potentials and/or technologies and/or policies, insofar as the alternative scenario assumptions do not alter the basic demand inputs (drivers and elasticities). The scenario builder must always be careful about the overall coherence of the various assumptions made on the four components of a scenario.

## Selected scenario types

The purpose of this section is to show how certain policies may be simulated in a TIMES model. The enormous flexibility of TIMES, especially at the technology level, allows the representation of almost any policy, be it at the national, sector, or subsector level.

**Policy 1: Carbon tax**

A tax is levied on emissions of CO<sub>2</sub> at point of source.

This policy is easily represented in TIMES a) making sure that all technologies that emit CO<sub>2</sub> have an emission coefficient, and then defining a tax on these emissions :ref:`(see 2.6.1.2) <part-1/02-basic-structure:economic and policy parameters>`. The policy may indicate that the tax be levied upstream for some end-use sectors (e.g. automobiles), in which case the emission coefficient is defined at the oil refinery level rather than at the level of individual car types.

**Policy 2: Cap-and-trade on CO<sub>2</sub>**

An upper limit on CO<sub>2</sub> emissions is imposed at the national level (alternatively, separate upper limits are imposed at the sector level). If the model is multi-country, trade of emission permits is allowed between countries (and/or between sectors). The trade may also be upper bounded by a maximum percentage of the actual emissions, thus representing a form of the subsidiarity principle.

This type of policy is simulated by defining upper bounds on emissions, a straightforward feature in TIMES (sections2.6.1.3 and 2.6.2.3). By defining total sector emissions as a new commodity, the sector-restricted cap is just as easily implemented. The trade of national emissions makes use of the standard trade variables of TIMES (section 5.2).

**Policy 3: Portfolio standard**

A sector is submitted to a lower limit on its efficiency. For instance, the electricity subsector using fossil fuels must have an overall efficiency of 50%[^3]. A similar example is an overall lower limit on the efficiency of light road vehicles.

This type of policy requires the definition of a new constraint that expresses that the ratio of electricity produced (via fossil fueled plants) over the amount of fuel used be more than 0.5. TIMES allows the modeller to define such new constraints via the user constraints (section 5.4.9).

**Policy 4: Subsidies for some classes of technologies**

The representation of this policy requires defining a capital subsidy for every new capacity of a class of technologies. This is quite straightforward in TIMES using the subsidy parameters (section 2.6.1.2.)

A more elaborate form of the subsidy might be to first levy an emission tax, and then use the proceeds of the tax to subsidize low-emitting and non-emitting technologies. Such a compound policy requires several sequential runs of TIMES, the first run establishing the proceeds of the carbon tax, followed by subsequent runs that distribute the proceeds among the targeted technologies. Several passes of these two runs may well be required in order to balance exactly the proceeds of the tax and the use of them as subsidies.

**Assessing the robustness of policies**

An important aspect of any policy is whether it will stay effective under various conditions. Examples of such conditions are oil prices, climate parameters, availability of certain resources, key technology costs or efficiency, etc. A policy that remains effective under a range of values for such conditions, is said to be ***robust***. In TIMES, robustness may be assessed using a variety of features, ranging from sensitivity analysis (chapter 6) to Stochastic Programming (chapter 8).


[^1]: MARKAL (MARket ALlocation model, Fishbone et al, 1981, 1983, Berger et al. 1992) and EFOM (Van Voort et al, 1984) are two bottom-up energy models that inspired the structure of TIMES.

[^2]: European Commission, *The GEM-E3 Model*, *General Equilibrium Model for Economy, Energy and Environment*, <https://ec.europa.eu/jrc/en/gem-e3/model>.

[^3]: This standard may also be imposed on the entire electricity generation sector, in which case renewable electricity plants are assumed to have zero energy input.
