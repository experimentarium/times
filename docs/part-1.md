---
title: |
  **Energy Technology Systems Analysis Programme**

  []{#OLE_LINK19 .anchor}

  [http://www.iea-etsap.org/web/Documentation.asp]{.underline}
---

Documentation for the TIMES Model

PART I

July 2016

(Last update: February 2021)

**Author:** Richard Loulou

**Co-authors:** Gary Goldstein

Amit Kanudia

Antti Lettila

Uwe Remme

**Reviewers:** Evelyn Wright

George Giannakidis

Ken Noble

**General Introduction** **to the TIMES Documentation**

This documentation is composed of four Parts.

> **[Part I]{.underline}** provides a general description of the TIMES
> paradigm, with emphasis on the model's general structure and its
> economic significance. Part I also includes a simplified mathematical
> formulation of TIMES, a chapter comparing it to the MARKAL model,
> pointing to similarities and differences, and chapters describing new
> model options.
>
> **[Part II]{.underline}** constitutes a comprehensive reference manual
> intended for the technically minded modeler or programmer looking for
> an in-depth understanding of the complete model details, in particular
> the relationship between the input data and the model mathematics, or
> contemplating making changes to the model's equations. Part II
> includes a full description of the sets, attributes, variables, and
> equations of the TIMES model.
>
> **[Part III]{.underline}** describes the organization of the TIMES
> modeling environment and the GAMS control statements required to run
> the TIMES model. GAMS is a modeling language that translates a TIMES
> database into the Linear Programming matrix, and then submits this LP
> to an optimizer and generates the result files. Part III describes how
> the routines comprising the TIMES source code guide the model through
> compilation, execution, solve, and reporting; the files produced by
> the run process and their use; and the various switches that control
> the execution of the TIMES code according to the model instance,
> formulation options, and run options selected by the user. It also
> includes a section on identifying and resolving errors that may occur
> during the run process.
>
> **[Part IV]{.underline}** provides a step-by-step introduction to
> building a TIMES model in the VEDA2.0 user interface for model
> management and results analysis. It first offers an orientation to the
> basic features of VEDA2.0, including software layout, data files and
> tables, and model management features, both for handling the input and
> examining the results. It then describes in detail twelve Demo models
> (available for download from the ETSAP website) that progressively
> introduce VEDA-TIMES principles and modeling techniques.

PART I: TIMES CONCEPTS AND THEORY

**TABLE OF CONTENTS FOR PART I**

Organization of PART I [8](#organization-of-part-i)

1 Introduction to the TIMES model [9](#introduction-to-the-times-model)

1.1 A brief summary [9](#a-brief-summary)

1.2 Driving a TIMES model via scenarios
[10](#driving-a-times-model-via-scenarios)

1.2.1 The Demand component of a TIMES scenario
[10](#the-demand-component-of-a-times-scenario)

1.2.2 The Supply component of a TIMES scenario
[11](#the-supply-component-of-a-times-scenario)

1.2.3 The Policy component of a TIMES scenario
[12](#the-policy-component-of-a-times-scenario)

1.2.4 The Techno-economic component of a TIMES scenario
[12](#the-techno-economic-component-of-a-times-scenario)

1.3 Selected scenario types [13](#selected-scenario-types)

2 The basic structure of the core TIMES model
[15](#the-basic-structure-of-the-core-times-model)

2.1 The TIMES economy [15](#the-times-economy)

2.2 Time horizon [15](#time-horizon)

2.3 Decoupling of data and model horizon
[17](#decoupling-of-data-and-model-horizon)

2.4 The components of a Reference Energy System (RES): processes,
commodities, flows [18](#_Toc323917580)

2.4.1 The RES [19](#the-res)

2.4.2 Three classes of processes [20](#three-classes-of-processes)

2.5 Data-driven model structure [22](#data-driven-model-structure)

2.6 A brief overview of the TIMES attributes
[24](#a-brief-overview-of-the-times-attributes)

2.6.1 Parameters attached to processes
[24](#parameters-attached-to-processes)

2.6.2 Parameters attached to commodities
[26](#parameters-attached-to-commodities)

2.6.3 Parameters attached to commodity flows
[27](#parameters-attached-to-commodity-flows)

2.6.4 Parameters attached to the entire RES
[28](#parameters-attached-to-the-entire-res)

2.7 Process and commodity classification
[28](#process-and-commodity-classification)

3 Economic rationale of the TIMES modeling approach
[31](#economic-rationale-of-the-times-modeling-approach)

3.1. A brief classification of energy models
[31](#a-brief-classification-of-energy-models)

3.1.1 'Top-down' models [32](#top-down-models)

3.1.2 'Bottom-up' models [33](#bottom-up-models)

3.1.3 Hybrid approaches [33](#hybrid-approaches)

3.2 The core TIMES paradigm [35](#the-core-times-paradigm)

3.2.1 A technologically explicit integrated model
[36](#a-technologically-explicit-integrated-model)

3.2.2 Multi-regional [36](#multi-regional)

3.2.3 Partial equilibrium [36](#partial-equilibrium)

3.2.4 Marginal value pricing [44](#marginal-value-pricing)

3.2.5 Profit maximization: the Invisible Hand
[46](#profit-maximization-the-invisible-hand)

4 Core TIMES model: Mathematics of the computation of the supply-demand
equilibrium
[47](#core-times-model-mathematics-of-the-computation-of-the-supply-demand-equilibrium)

4.1 Theoretical considerations: the Equivalence Theorem
[47](#theoretical-considerations-the-equivalence-theorem)

4.2 Mathematics of the TIMES equilibrium
[48](#mathematics-of-the-times-equilibrium)

4.2.1 Defining demand functions [48](#defining-demand-functions)

4.2.2 Formulating the TIMES equilibrium
[48](#formulating-the-times-equilibrium)

4.2.3 Linearization of the Mathematical Program
[49](#linearization-of-the-mathematical-program)

4.2.4 Calibration of the demand functions
[51](#calibration-of-the-demand-functions)

4.2.5 Computational considerations [51](#computational-considerations)

4.2.6 Interpreting TIMES costs, surplus, and prices
[52](#interpreting-times-costs-surplus-and-prices)

5 Core TIMES Model: A simplified description of the Optimization Program
(variables, objective, constraints)
[53](#core-times-model-a-simplified-description-of-the-optimization-program-variables-objective-constraints)

5.1 Indices [53](#indices)

5.2 Decision variables [54](#decision-variables)

5.3 TIMES objective function: discounted total system cost
[58](#times-objective-function-discounted-total-system-cost)

5.3.1 The costs accounted for in the objective function
[58](#the-costs-accounted-for-in-the-objective-function)

5.3.2 Cash flow tracking [60](#cash-flow-tracking)

5.3.3 Aggregating the various costs [61](#aggregating-the-various-costs)

5.3.4 Variants for the objective function
[62](#variants-for-the-objective-function)

5.4 Constraints [64](#constraints)

5.4.1 Capacity transfer (conservation of investments)
[65](#capacity-transfer-conservation-of-investments)

5.4.2 Definition of process activity variables [66](#_Toc323917620)

5.4.3 Use of capacity [66](#use-of-capacity)

5.4.4 Commodity balance equation [67](#commodity-balance-equation)

5.4.5 Defining flow relationships in a process
[69](#defining-flow-relationships-in-a-process)

5.4.6 Limiting flow shares in flexible processes
[70](#limiting-flow-shares-in-flexible-processes)

5.4.7 Peaking reserve constraint (time-sliced commodities only)
[71](#peaking-reserve-constraint-time-sliced-commodities-only)

5.4.8 Constraints on commodities [73](#constraints-on-commodities)

5.4.9 User constraints [74](#user-constraints)

5.4.10 Growth constraints [74](#growth-constraints)

5.4.11 Early retirement of capacity [75](#early-retirement-of-capacity)

5.4.12 Electricity grid modeling [76](#electricity-grid-modeling)

5.4.13 Reporting \"constraints\" [79](#reporting-constraints)

5.5 The \'Linear\' variant of TIMES [80](#the-linear-variant-of-times)

6 Parametric analysis with TIMES [82](#parametric-analysis-with-times)

6.1 Two-phase tradeoff analysis [83](#two-phase-tradeoff-analysis)

6.2 Multiphase tradeoff analysis [84](#multiphase-tradeoff-analysis)

7 The TIMES Climate Module [87](#the-times-climate-module)

7.1 Concentrations (accumulation of CO2, CH4, N2O)
[88](#concentrations-accumulation-of-co2-ch4-n2o)

7.2 Radiative forcing [89](#radiative-forcing)

7.3 Linear approximations of the three forcings
[91](#linear-approximations-of-the-three-forcings)

7.4 Temperature increase [92](#temperature-increase)

8 The Stochastic Programming extension
[94](#the-stochastic-programming-extension)

8.1 Preamble to chapters 8 to 11 [94](#preamble-to-chapters-8-to-11)

8.2 Stochastic Programming concepts and formulation
[95](#stochastic-programming-concepts-and-formulation)

8.3 Alternative criteria for the objective function
[98](#alternative-criteria-for-the-objective-function)

8.3.1 Expected utility criterion with risk aversion
[99](#expected-utility-criterion-with-risk-aversion)

8.3.2 Utility function with linearized risk aversion
[99](#utility-function-with-linearized-risk-aversion)

8.4 Solving approaches [100](#solving-approaches)

8.5 Economic interpretation [100](#economic-interpretation)

9 Using TIMES with limited foresight (time-stepped)
[102](#using-times-with-limited-foresight-time-stepped)

9.1 The FIXBOH feature [102](#the-fixboh-feature)

9.2 The time-stepped option (TIMESTEP)
[103](#the-time-stepped-option-timestep)

10 The Lumpy Investment extension [105](#the-lumpy-investment-extension)

10.1 Formulation and solution of the Mixed Integer Linear Program
[106](#formulation-and-solution-of-the-mixed-integer-linear-program)

10.2 Discrete early retirement of capacity
[107](#discrete-early-retirement-of-capacity)

10.3 Important remark on the MIP dual solution (shadow prices)
[107](#important-remark-on-the-mip-dual-solution-shadow-prices)

11 The Endogenous Technological Learning extension
[109](#the-endogenous-technological-learning-extension)

11.1 The basic ETL challenge [109](#the-basic-etl-challenge)

11.2 The TIMES formulation of ETL [110](#the-times-formulation-of-etl)

11.2.1 The cumulative investment cost
[110](#the-cumulative-investment-cost)

11.2.2 Calculation of break points and segment lengths
[113](#calculation-of-break-points-and-segment-lengths)

11.2.3 New variables [113](#new-variables)

11.2.4 New constraints [114](#new-constraints)

11.2.5 Objective function terms [115](#objective-function-terms)

11.2.6 Additional (optional) constraints
[115](#additional-optional-constraints)

11.3 Clustered learning [115](#clustered-learning)

11.4 Learning in a multiregional TIMES model
[116](#learning-in-a-multiregional-times-model)

11.5 Endogenous vs. exogenous learning: a discussion
[117](#endogenous-vs.-exogenous-learning-a-discussion)

12 General equilibrium extensions [120](#general-equilibrium-extensions)

12.1 Preamble [120](#preamble)

12.2 The single-region TIMES-MACRO model
[121](#the-single-region-times-macro-model)

12.2.1 Formulation of the MACRO model
[122](#formulation-of-the-macro-model)

12.2.2 Linking MACRO with TIMES [125](#linking-macro-with-times)

12.2.3 A brief comment [127](#a-brief-comment)

12.3 The multi-regional TIMES-MACRO model (MSA)
[127](#the-multi-regional-times-macro-model-msa)

12.3.1 Theoretical background [127](#theoretical-background)

12.3.2 A sketch of the algorithm to solve TIMES-MACRO-MSA
[128](#a-sketch-of-the-algorithm-to-solve-times-macro-msa)

13 Appendix A: History and comparison of MARKAL and TIMES
[130](#appendix-a-history-and-comparison-of-markal-and-times)

13.1 A brief history of TIMES and MARKAL
[130](#a-brief-history-of-times-and-markal)

13.2 A comparison of the TIMES and MARKAL models
[134](#a-comparison-of-the-times-and-markal-models)

13.2.1 Similarities [134](#similarities)

13.2.2 TIMES features not in MARKAL [134](#times-features-not-in-markal)

14 Appendix B: Linear Programming complements
[139](#appendix-b-linear-programming-complements)

14.1 A brief primer on Linear Programming and Duality Theory
[139](#a-brief-primer-on-linear-programming-and-duality-theory)

14.1.1 Basic definitions [139](#basic-definitions)

14.1.2 Duality Theory [140](#duality-theory)

14.2 Sensitivity analysis and the economic interpretation of dual
variables
[141](#sensitivity-analysis-and-the-economic-interpretation-of-dual-variables)

14.2.1 Economic interpretation of the dual variables
[141](#economic-interpretation-of-the-dual-variables)

14.2.2 Reduced surplus and reduced cost
[142](#reduced-surplus-and-reduced-cost)

15 References [144](#references)

# Organization of PART I {#organization-of-part-i .unnumbered}

Part I comprises five divisions, each containing a number of chapters:

-   Chapters 1 and 2 provide a general overview of the representation in
    TIMES of the Reference Energy System (RES) of a typical region or
    country, focusing on its basic elements, namely technologies and
    commodities.

-   Chapters 3 to 7 describe the core TIMES model generator, i.e. the
    dynamic partial equilibrium version with perfect foresight: Chapter
    3 discusses the economic rationale of the model, and Chapter 4
    describes in more detail than chapter 3 the elastic demand feature
    and other economic and mathematical properties of the TIMES
    equilibrium. Chapter 5 presents a streamlined representation of the
    Linear Program used by TIMES to compute the equilibrium. Chapter 6
    describes a new TIMES feature for conducting systematic sensitivity
    analyses. Chapter 7 describes the Climate Module of TIMES.

-   Chapters 8 to 11 contain descriptions of 4 extensions or variants
    that, if used, depart from the assumptions of the core model in a
    way that alters the nature of the equilibrium: Chapter 8 covers the
    stochastic programming variant, which no longer assumes perfect
    foresight, but rather imperfect foresight; Chapter 9 describes the
    myopic use of TIMES, which violates the perfect foresight property
    and replaces it with limited foresight; Chapter 10 describes the
    lumpy investment variant where some decisions are discrete rather
    than continuous, and thus violate the convexity property; Chapter 11
    describes the endogenous technology learning extension, also
    involving non-convex elements.

-   Chapter 12 is devoted to two extensions that make TIMES into a
    General Equilibrium model, namely ES-MACRO and TIMES-MERGE-MACRO.

-   Chapters 13 and 14 constitute appendices that may be of interest to
    readers at any point in their use of the rest of the text. Chapter
    13 provides a brief history and comparison of TIMES and MARKAL, the
    modeling framework that preceded TIMES. Chapter 14 provides a short
    review of the theoretical foundation of Linear Programming and the
    interpretation of the dual solution of a linear program.

# Introduction to the TIMES model

## A brief summary

TIMES (an acronym for The Integrated MARKAL-EFOM[^1] System) is an
economic model generator for local, national, multi-regional, or global
energy systems, which provides a technology-rich basis for representing
energy dynamics over a multi-period time horizon. It is usually applied
to the analysis of the entire energy sector, but may also be applied to
study single sectors such as the electricity and district heat sector.

Estimates of end-use energy service demands (e.g., car road travel;
residential lighting; steam heat requirements in the paper industry;
etc.) are provided by the user for each region to drive the reference
scenario. In addition, the user provides estimates of the existing
stocks of energy related equipment in all sectors, and the
characteristics of available future technologies, as well as present and
future sources of primary energy supply and their potentials.

Using these as inputs, the TIMES model aims to supply energy services at
minimum global cost (more accurately at minimum loss of total surplus)
by simultaneously making decisions on equipment investment and
operation; primary energy supply; and energy trade for each region. For
example, if there is an increase in residential lighting energy service
relative to the reference scenario (perhaps due to a decline in the cost
of residential lighting, or due to a different assumption on GDP
growth), either existing generation equipment must be used more
intensively or new -- possibly more efficient -- equipment must be
installed. The choice by the model of the generation equipment (type and
fuel) is based on the analysis of the characteristics of alternative
generation technologies, on the economics of the energy supply, and on
environmental criteria. TIMES is thus a vertically integrated model of
the entire extended energy system.

The scope of the model extends beyond purely energy-oriented issues, to
the representation of environmental emissions, and perhaps materials,
related to the energy system. In addition, the model is suited to the
analysis of energy-environmental policies, which may be represented with
accuracy thanks to the explicitness of the representation of
technologies and fuels in all sectors.

In TIMES -- like in its MARKAL forebear -- the quantities and prices of
the various commodities are in equilibrium, i.e. their prices and
quantities in each time period are such that the suppliers produce
exactly the quantities demanded by the consumers. This equilibrium has
the property that the total economic surplus is maximized.

## Driving a TIMES model via scenarios

The TIMES model is particularly suited to the *exploration* of possible
energy futures based on contrasted *scenarios*. Given the long horizons
that are usually simulated with TIMES, the scenario approach is really
the only choice (whereas for the shorter term, econometric methods may
provide useful projections). Scenarios, unlike forecasts, do not
pre-suppose knowledge of the main drivers of the energy system. Instead,
a scenario consists of a set of *coherent assumptions* about the future
trajectories of these drivers, leading to a coherent organization of the
system under study. A scenario builder must therefore carefully test the
scenario assumptions for internal coherence, via a credible *storyline*.

In TIMES, a complete scenario consists of four types of inputs: energy
service demand curves, primary resource supply curves, a policy setting,
and the descriptions of a complete set of technologies. We now present a
few comments on each of these four components.

### The Demand component of a TIMES scenario

In the case of the TIMES model, demand drivers (population, GDP,
households, etc.) are obtained externally, via other models or from
accepted other sources. As one example, several global instances of
TIMES (e.g. Loulou, 2007) use the GEM-E3[^2] to generate a set of
*coherent* (national and sectoral) output growth rates in the various
regions. Note that GEM-E3 or GEMINI-E3 themselves use other drivers as
inputs, in order to derive GDP trajectories. These drivers consist of
measures of technological progress, population, degree of market
competitiveness, and a few other (perhaps qualitative) assumptions. For
population and household projections, TIMES instances use the same
exogenous sources (IPCC, Nakicenovic 2000, Moomaw and Moreira, 2001).
Other approaches may be used to derive TIMES drivers, whether via models
or other means.

For the global versions of TIMES, the main drivers are: Population, GDP,
GDP per capita, number of households, and sectoral outputs. For sectoral
TIMES models, the demand drivers may be different depending on the
system boundaries.

Once the drivers for a TIMES model are determined and quantified the
construction of the reference demand scenario requires computing a set
of energy service demands over the horizon. This is done by choosing
elasticities of demands to their respective drivers, in each region,
using the following general formula:

$$Demand = Driver^{Elasticity}$$

As mentioned above, the demands are user provided for the reference
scenario only. When the model is run for alternate scenarios (for
instance for an emission constrained case, or for a set of alternate
technological assumptions), it is likely that the demands will be
affected. TIMES has the capability of estimating the response of the
demands to the changing conditions of an alternate scenario. To do this,
the model requires still another set of inputs, namely the assumed
elasticities of the demands to their own prices. TIMES is then able to
endogenously adjust the demands to the alternate cases without exogenous
intervention. In fact, the TIMES model is driven not by demands but by
*demand curves*.

To summarize: the TIMES demand scenario components consist of a set of
assumptions on the drivers (GDP, population, households, outputs) and on
the elasticities of the demands to the drivers and to their own prices.

### The Supply component of a TIMES scenario

The second constituent of a scenario is a set of *supply curves* for
primary energy and material resources. Multi-stepped supply curves are
easily modeled in TIMES, each step representing a certain potential of
the resource available at a particular cost. In some cases, the
potential may be expressed as a cumulative potential over the model
horizon (e.g. reserves of gas, crude oil, etc.), as a cumulative
potential over the resource base (e.g. available areas for wind
converters differentiated by velocities, available farmland for
biocrops, roof areas for PV installations) and in others as an annual
potential (e.g. maximum extraction rates, or for renewable resources the
available wind, biomass, or hydro potentials). Note that the supply
component also includes the identification of trading possibilities,
where the amounts and prices of the traded commodities are determined
endogenously (optionally within user imposed limits).

### The Policy component of a TIMES scenario

Insofar as some policies impact on the energy system, they become an
integral part of the scenario definition. For instance, a reference
scenario may perfectly ignore emissions of various pollutants, while
alternate policy scenarios may enforce emission restrictions, or
emission taxes, etc. The detailed technological nature of TIMES allows
the simulation of a wide variety of both micro measures (e.g. technology
portfolios, or targeted subsidies to groups of technologies), and
broader policy targets (such as general carbon tax, or permit trading
system on air contaminants). A simpler example might be a nuclear policy
that limits the future capacity of nuclear plants. Another example might
be the imposition of fuel taxes, or of targeted capital subsidies, etc.

### The Techno-economic component of a TIMES scenario

The fourth and last constituent of a scenario is the set of technical
and economic parameters assumed for the transformation of primary
resources into energy services. In TIMES, these techno-economic
parameters are described in the form of *technologies* (or processes)
that transform some commodities into others (fuels, materials, energy
services, emissions). In TIMES, some technologies may be user imposed
and others may simply be available for the model to choose from. The
quality of a TIMES model rests on a rich, well developed set of
technologies, both current and future, for the model to choose from. The
emphasis put on the technological database is one of the main
distinguishing factors of the class of Bottom-up models, to which TIMES
belongs. Other classes of models will tend to emphasize other aspects of
the system (e.g. interactions with the rest of the economy) and treat
the technical system in a more succinct manner via aggregate production
functions.

*Remark:* Two scenarios may differ in some or all of their components.
For instance, the same demand scenario may very well lead to multiple
scenarios by varying the primary resource potentials and/or technologies
and/or policies, insofar as the alternative scenario assumptions do not
alter the basic demand inputs (drivers and elasticities). The scenario
builder must always be careful about the overall coherence of the
various assumptions made on the four components of a scenario.

## Selected scenario types

The purpose of this section is to show how certain policies may be
simulated in a TIMES model. The enormous flexibility of TIMES,
especially at the technology level, allows the representation of almost
any policy, be it at the national, sector, or subsector level.

**Policy 1: Carbon tax**

A tax is levied on emissions of CO2 at point of source.

This policy is easily represented in TIMES a) making sure that all
technologies that emit CO2 have an emission coefficient, and then
defining a tax on these emissions (see 2.6.1.2). The policy may indicate
that the tax be levied upstream for some end-use sectors (e.g.
automobiles), in which case the emission coefficient is defined at the
oil refinery level rather than at the level of individual car types.

**Policy 2: Cap-and-trade on CO2**

An upper limit on CO2 emissions is imposed at the national level
(alternatively, separate upper limits are imposed at the sector level).
If the model is multi-country, trade of emission permits is allowed
between countries (and/or between sectors). The trade may also be upper
bounded by a maximum percentage of the actual emissions, thus
representing a form of the subsidiarity principle.

This type of policy is simulated by defining upper bounds on emissions,
a straightforward feature in TIMES (sections2.6.1.3 and 2.6.2.3). By
defining total sector emissions as a new commodity, the
sector-restricted cap is just as easily implemented. The trade of
national emissions makes use of the standard trade variables of TIMES
(section 5.2).

**Policy 3: Portfolio standard**

A sector is submitted to a lower limit on its efficiency. For instance,
the electricity subsector using fossil fuels must have an overall
efficiency of 50%[^3]. A similar example is an overall lower limit on
the efficiency of light road vehicles.

This type of policy requires the definition of a new constraint that
expresses that the ratio of electricity produced (via fossil fueled
plants) over the amount of fuel used be more than 0.5. TIMES allows the
modeller to define such new constraints via the user constraints
(section 5.4.9).

**Policy 4: Subsidies for some classes of technologies**

The representation of this policy requires defining a capital subsidy
for every new capacity of a class of technologies. This is quite
straightforward in TIMES using the subsidy parameters (section 2.6.1.2.)

A more elaborate form of the subsidy might be to first levy an emission
tax, and then use the proceeds of the tax to subsidize low-emitting and
non-emitting technologies. Such a compound policy requires several
sequential runs of TIMES, the first run establishing the proceeds of the
carbon tax, followed by subsequent runs that distribute the proceeds
among the targeted technologies. Several passes of these two runs may
well be required in order to balance exactly the proceeds of the tax and
the use of them as subsidies.

**Assessing the robustness of policies**

An important aspect of any policy is whether it will stay effective
under various conditions. Examples of such conditions are oil prices,
climate parameters, availability of certain resources, key technology
costs or efficiency, etc. A policy that remains effective under a range
of values for such conditions, is said to be ***robust***. In TIMES,
robustness may be assessed using a variety of features, ranging from
sensitivity analysis (chapter 6) to Stochastic Programming (chapter 8).

#  The basic structure of the core TIMES model

## The TIMES economy

The TIMES energy economy is made up of producers and consumers of
*commodities* such as energy carriers, materials, energy services, and
emissions. By default, TIMES assumes competitive markets for all
commodities, unless the modeler voluntarily imposes regulatory or other
constraints on some parts of the energy system, in which case the
equilibrium is (partially) regulated. The result is a supply-demand
equilibrium that maximizes the *net total surplus* (i.e. the sum of
producers' and consumers' surpluses) as fully discussed in chapters 3
and 4. TIMES may however depart from perfectly competitive market
assumptions by the introduction of user-defined explicit constraints,
such as limits to technological penetration, constraints on emissions,
exogenous oil price, etc. Market imper­fections can also be introduced in
the form of taxes, subsidies and hurdle rates.

While computing the equilibrium, a TIMES run configures the *energy
system* of a *set of regions*, over a certain *time horizon,* in such a
way as to *minimize the net total cost* (or equivalently *maximize the
net total surplus*) of the system, while satisfying a number of
*constraints*. TIMES is run in a dynamic manner, which is to say that
all investment decisions are made in each period with full knowledge of
future events. The model is said to have *perfect foresight*[^4] (or to
be *clairvoyant*). The next subsection describes in detail the time
dimension of the model.

## Time horizon

The time horizon is divided into a user-chosen number of time-periods,
each period containing a (possibly different) number of years.

In the standard version of TIMES each year in a given period is
considered identical, except for the cost objective function which
differentiates between payments in each year of a period. For all other
quantities (capacities, commodity flows, operating levels, etc.) any
model input or output related to period ***t*** applies to each of the
years in that period, with the exception of investment variables, which
are usually made only once in a period[^5].

Another version of TIMES is available, in which the TIMES variables
(capacities and flows) are defined at some year in the midst of each
period (called milestone year), and are assumed to evolve linearly
between the successive milestone years. This option emulates that of the
EFOM model and is discussed in section 5.5.

The initial period is usually considered a past period, over which the
model has no freedom, and for which the quantities of interest are all
fixed by the user at their historical values. It is often advisable to
choose an initial period consisting of a single year, in order to
facilitate calibration to standard energy statistics. Calibration to the
initial period is one of the more important tasks required when setting
up a TIMES model. The main variables to be calibrated are: the
capacities and operating levels of all technologies, as well as the
extracted, exported, imported, produced, and consumed quantities for all
energy carriers, and the emissions if modeled.

In TIMES, years preceding the first period also play a role. Although no
explicit variables are defined for these years, data may be provided by
the modeler on past investments. Note carefully that the specification
of past investments influences not only the initial period's
calibration, but also partially determines the model's behavior over
several future periods, since the past investments provide residual
capacity in several years within the modeling horizon proper.

In addition to time-periods (which may be of variable length), there are
time divisions within a year, also called *time-slices,* which may be
defined at will by the user (see Figure 2.1). For instance, the user may
want to define seasons, portions of the day/night, and/or
weekdays/weekends. Time-slices are especially important whenever the
mode and cost of production of an energy carrier at different times of
the year are significantly different. This is the case for instance when
the some energy commodity is expensive to store so that the matching of
production and consumption of that commodity is itself an issue to be
resolved by the model. The production technologies for the commodity may
themselves have different characteristics depending on the time of year
(e.g. wind turbines or run-of-the-river hydro plants). In such cases,
the matching of supply and demand requires that the activities of the
technologies producing and consuming the commodity be tracked for each
time slice. Examples of commodities requiring time-slicing may include
electricity, district heat, natural gas, industrial steam, and hydrogen.

An additional reason for defining sub yearly time slices is the
requirement of an expensive infrastructure whose capacity should be
sufficient to allow the peak demand for the commodity to be satisfied.
Technologies that store a commodity in one time slice, at a cost, for
discharge in another time slice, may also be defined and modeled.

The net result of these conditions is that the deployment in time of the
various production technologies may be very different in different time
slices, and furthermore that specific investment decisions will be taken
to insure adequate reserve capacity at peak.

![timeslice_tree](media/image1.wmf){width="5.483665791776028in"
height="3.2058344269466317in"}

*Figure 2.1: Example of a time-slice tree*

## Decoupling of data and model horizon

In TIMES, special efforts have been made to decouple the specification
of data from the definition of the time periods for which a model is
run. Two TIMES features facilitate this decoupling.

First, the fact that investments made in past years are recognized by
TIMES makes it much easier to modify the choice of the initial and
subsequent periods without major revisions of the database.

Second, the specification of process and demand input data in TIMES is
made by specifying the *calendar years* when the data apply,
irrespective of how the model time periods have been defined. The model
then takes care of interpolating and extrapolating the data for the
*periods* chosen by the modeler for a particular model run. TIMES offers
a particularly rich range of interpolation/extrapolation modes adapted
to each type of data and freely overridden by the user. Section 3.1.1of
Part II discusses this feature.

These two features combine to make a change in the definition of periods
quite easy and error-free. For instance, if a modeler decides to change
the initial year from 2010 to 2015, and perhaps change the number and
durations of all other periods as well, only one type of data change is
needed, namely to define the investments made from 2011 to 2015 as past
investments. All other data specifications need not be altered[^6]. This
feature represents a great simplification of the modeler's work. In
particular, it enables the user to define time periods that have varying
lengths, without changing the input data.

## The components of a Reference Energy System (RES): processes, commodities, flows

The TIMES energy economy consists of three types of entities:

-   *Technologies* (also called *processes*) are representations of
    physical plants, vehicles, or other devices that transform some
    commodities into other commodities. They may be primary sources of
    commodities (e.g. mining processes, import processes), or
    transformation activities such as conversion plants that produce
    electricity, energy-processing plants such as refineries, or end-use
    demand devices such as cars and heating systems, that transform
    energy into a demand service;

-   *Commodities* consisting of energy carriers, energy services,
    materials, monetary flows, and emissions. A commodity is produced by
    one or more processes and/or consumed by other processes; and

-   *Commodity flows* are the links between processes and commodities. A
    flow is of the same nature as a commodity but is attached to a
    particular process, and represents one input or one output of that
    process. For instance, electricity produced by wind turbine type A
    at period *p*, time-slice *s*, in region *r*, is a commodity flow.

### The RES

It is helpful to picture the relationships among these various entities
using a network diagram, referred to as a *Reference Energy System*
(RES). In a TIMES RES, processes are represented as boxes and
commodities as vertical lines. Commodity flows are represented as links
between process boxes and commodity lines.

Figure 2.2 depicts a small portion of a hypothetical RES containing a
single energy service demand, namely residential space heating. There
are three end-use space heating technologies using the gas, electricity,
and heating oil energy carriers (commodities), respectively. These
energy carriers in turn are produced by other technologies, represented
in the diagram by one gas plant, three electricity-generating plants
(gas fired, coal fired, oil fired), and one oil refinery.

![](media/image2.wmf){width="5.996527777777778in"
height="4.4215277777777775in"}

*Figure 2.2. Partial view of a Reference Energy System (links are
oriented left to right)*

To complete the production chain on the primary energy side, the diagram
also represents an extraction source for natural gas, an extraction
source for coal, and two sources of crude oil (one extracted
domestically and then transported by pipeline, and the other one
imported). This simple RES has a total of 13 commodities and 13
processes. Note that in the RES every time a commodity enters/leaves a
process (via a particular flow) its name is changed (e.g., wet gas
becomes dry gas, crude becomes pipeline crude). This simple rule enables
the inter-connections between the processes to be properly maintained
throughout the network.

To organize the RES, and inform the modeling system of the nature of its
components, the various technologies, commodities, and flows may be
classified into *sets*. Each set regroups components of a similar
nature. The entities belonging to a set are referred to as *members,
items* or *elements* of that set. The same item may appear in multiple
technology or commodity sets. While the topology of the RES can be
represented by a multi-dimensional network, which maps the flow of the
commodities to and from the various technologies, the set membership
conveys the nature of the individual components and is often most
relevant to post-processing (reporting) rather than influencing the
model structure itself. However, the TIMES commodities are still
classified into several *Major Groups*. There are five such groups:
energy carriers, materials, energy services, emissions, and monetary
flows. The use of these groups is essential in the definition of some
TIMES constraints, as discussed in chapter 5.

### Three classes of processes

We now give a brief overview of three classes of processes that need to
be distinguished:

Processes are *general processes, storage processe*s, and
*inter-regional trading processes* (also called *inter-regional exchange
processes*). The latter two classes need to be distinguished from
general processes due to their special function requiring special rules
and sometimes a different set of indices.

#### General processes

In TIMES most processes are endowed with essentially the same attributes
(with the exceptions of storage and inter-regional exchange processes,
see below), and unless the user decides otherwise (e.g. by providing
values for some attributes and ignoring others), they have the same
variables attached to them, and must obey similar constraints.
Therefore, the differentiation between the various species of processes
(or commodities) is made through data specification only, thus
eliminating the need to define specialized membership sets, unless
desired for processing results. Most of the TIMES features (e.g.
sub-annual time-slice resolution, vintaging) are available for all
processes and the modeler chooses the features being assigned to a
particular process by specifying a corresponding indicator set (e.g.
PRC_TSL, PRC_VINT).

A general process receives one or more commodity inputs (inflows) and
produces one or more commodity outputs (outflows) in the same
time-slice, period, and region.

As already mentioned, two classes of process do not follow these rules
and deserve separate descriptions, namely *storage processes* and
i*nter-regional exchange processes*.

#### Storage processes (class STG)

This advanced feature of TIMES allows the modeller to represent very
intricate storage activities from real life energy systems. Storage
processes are used to store a commodity either between periods or
between time-slices in the same period. A process ***p*** is specified
to be an ***inter-period storage (IPS) process*** for commodity ***c,***
or as ***general time-slice storage (TSS)***. A special case of
time-slice storage is a so-called ***night-storage device (NST)*** where
the commodity for charging and the one for discharging the storage are
different.

An example of a night storage device is an electric heating technology
that is charged during the night using electricity and produces heat
during the day. Several time-slices may be specified as charging
time-slices, the non-specified time-slices are assumed to be discharging
time-slices. However, when the process is an end-use process that
satisfies a service demand, the discharging occurs according to the load
curve of the corresponding demand, and the charging is freely optimized
by TIMES across time-slices. Such an exception for demand processes only
exists if the demand is at the ANNUAL level. But if the demand is not
ANNUAL, discharging can only occur in the non-charging time-slices.

An example of general time-slice storage is a pumped storage reservoir,
where electricity is consumed during the night to store water in a
reservoir, water which is then used to activate a turbine and produce
electricity at a different time-slice.

An example of an inter-period storage process is a plant that
accumulates organic refuse in order to produce methane some years later.

Besides the commodity being stored, other (auxiliary) commodity flows
are also permitted and may be defined in relation to the stored
commodity using the FLO_FUNC and/or the ACT_FLO parameters. The activity
of a storage process is interpreted as the amount of the commodity being
stored in the storage process. Accordingly the capacity of a storage
process describes the maximum commodity amount that can be kept in
storage.

#### Inter-regional exchange processes (class IRE)

Inter-regional exchange (IRE) processes are used for trading commodities
between regions. Note that the name of the traded commodity is allowed
to be different in both regions, depending on the chosen commodity names
in both regions. There are two types of trade in TIMES, bi-lateral or
multi-lateral.

Bi-lateral trade is the most detailed way to specify trade between
regions. It takes place between specific pairs of regions. A pair of
regions together with an exchange process and the direction of the
commodity flow is first identified, and the model ensures that trade
through the exchange process is balanced between these two regions (the
amount is exported from region A to region B must be imported by region
B from region A, possibly adjusted for trans­portation losses). If trade
should occur only in one direction then only that direction is provided
by the proper ordinal attribute. The process capacity and the process
related costs (e.g. activity costs, investment costs) of the exchange
process may be described individually for both regions by specifying the
corresponding parameters in each region. This allows for instance the
investment cost of a trade process to be shared between regions in user
chosen proportions.

There are cases when it is not important to fully specify the pair of
trading regions. An example is the trading of greenhouse gas (GHG)
emission permits in a global market. In such cases, the *multi-lateral
trade* option decreases the size of the model. Multi-lateral trade is
based on the idea that a common marketplace exists for a traded
commodity with several selling and several buying regions for the
commodity (e.g. GHG emission permits). To model a marketplace the user
must first identify (or create) one region that participates both in the
production and consumption of the traded commodity. Then a single
exchange process is used to link all regions with the marketplace
region. Note however that some flexibility is lost when using
multilateral trade. For instance, it is not possible to express
transportation costs in a fully accurate manner, if such cost depends
upon the precise pair of trading regions in a specific way.

## Data-driven model structure

It is useful to distinguish between a model's *structure* and a
particular *instance* of its implementation. A model's structure
exemplifies its fundamental approach for representing a problem---it
does not change from one implementation to the next. All TIMES models
exploit an identical underlying structure. However, because TIMES is
*data*[^7] *driven*, the *effective structure* of a particular instance
of a model will vary according to the data inputs. This means that some
of the TIMES features will not be activated if the corresponding data is
not specified. For example, in a multi-region model one region may, as a
matter of user data input, have undiscovered domestic oil reserves.
Accordingly, TIMES automatically generates technologies and processes
that account for the cost of discovery and field development. If,
alternatively, user supplied data indicate that a region does not have
undiscovered oil reserves no such technologies and processes would be
included in the representation of that region's Reference Energy System
(RES, see section 2.4). Due to this property TIMES may also be called a
*model generator* that, based on the input information provided by the
modeler, generates an instance of a model. In the following, if not
stated otherwise, the word \'model\' is used with two meanings
indifferently: the instance of a TIMES model or more generally the model
generator TIMES.

Thus, the structure of a TIMES model is ultimately defined by variables
and equations created from the union of the underlying TIMES equations
and the data input provided by the user. This information collectively
defines each TIMES regional model database, and therefore the resulting
mathematical representation of the RES for each region. The database
itself contains both qualitative and quantitative data.

The *qualitative data* includes, for example, the list of commodities,
and the list of those technologies that the modeler feels are applicable
(to each region) over a specified time horizon. This information may be
further classified into subgroups, for example commodities may include
energy carriers (themselves split by type \--e.g., fossil, nuclear,
renewable, etc.), materials, emissions, energy services.

*Quantitative data*, in contrast, contains the technological and
economic parameter assumptions specific to each technology, region, and
time period. When constructing multi-region models it is often the case
that a given technology is available for use in two or more regions;
however, cost and performance assumptions may be quite different. The
word ***attribute*** designates both qualitative and quantitative
elements of the TIMES modeling system.

## A brief overview of the TIMES attributes

Due to the data driven nature of TIMES (see section 2.5), all TIMES
constraints are activated and defined by specifying some attributes.
Attributes are attached to processes, to commodities, to flows, or to
special variables that have been created to define new TIMES features.
Indeed, TIMES has many new attributes that were not available in earlier
versions, corresponding to powerful new features that confer additional
modeling flexibility. The complete list of attributes is fully described
in section 3 of PART II, and we provide below only succinct comments on
the types of attribute attached to each entity of the RES or to the RES
as a whole. Additional attribute definitions may also be included in the
chapters describing new features or variants of the TIMES generator.

Attributes may be *cardinal* (numbers) or *ordinal* (lists, sets). For
example, some ordinal attributes are defined for processes to describe
subsets of flows that are then used to construct specific flow
constraints as described in section 5.4. PART II, section 2 shows the
complete list of TIMES sets.

The cardinal attributes are usually called *parameters*. We give below a
brief idea of the main types of parameters available in the TIMES model
generator.

### Parameters attached to processes

TIMES process-oriented parameters fall into several general categories.

#### Technical parameters

*Technical parameters* include process efficiency, availability
factor(s)[^8], commodity consumptions per unit of activity, shares of
fuels per unit activity, technical life of the process, construction
lead time, dismantling lead-time and duration, amounts of the
commodities consumed (respectively released) by the construction
(respectively dismantling) of one unit of the process, and contribution
to the peak equations. The efficiency, availability factors, and
commodity inputs and outputs of a process may be defined in several
flexible ways depending on the desired process flexibility, on the
time-slice resolution chosen for the process and on the time-slice
resolution of the commodities involved. Certain parameters are only
relevant to special processes, such as storage processes or processes
that implement trade between regions.

#### Economic and policy parameters

A second class of process parameters comprises *economic and policy
parameters* that include a variety of costs attached to the investment,
dismantling, maintenance, and operation of a process. The investment
cost of the technology is incurred once at the time of acquisition; the
fixed annual cost is incurred each year per unit of the capacity of the
technology, as long as the technology is kept alive (even if it is not
actively functioning); the annual variable cost is incurred per unit of
the activity of the technology. In addition to costs, taxes and
subsidies (on investment and/or on activity) may be defined in a very
flexible manner. Other economic parameters are: the economic life of a
process (the time during which the investment cost of a process is
amortized, which may differ from the operational lifetime) and the
process specific discount rate, also called *hurdle rate*. Both these
parameters serve to calculate the annualized payments on the process
investment cost, which enters the expression for the total cost of the
run (section 5.2).

#### Bounds

Another class of parameter is used to define the right-hand-side of some
constraint. Such a parameter represents a ***bound*** and its
specification triggers the constraint on the quantity concerned. Most
frequently used bounds are those imposed on period investment, capacity,
or activity of a process. Newly defined bounds allow the user to impose
limits on the annual or annualized payments at some period or set of
consecutive years.

A special type of bounding consists in imposing upper or lower limits on
the ***growth rate*** of technologies. The most frequently quantities
thus bounded are investment, capacity and activity of a process, for
which a simplified formulation has been devised.

The growth constraints belong to the class of ***dynamic bounds*** that
involve multiple periods. Many other dynamic bounds may be defined by
the user. ***Bounds on cumulative quantities*** are also very useful.
The accumulation may be over the entire horizon or over some user
defined set of consecutive years. The variables on which such bounds
apply may quite varied, such as: process capacity, process investment,
process activity, annual or annuity payments, etc.

All bounds may be of four types: lower (LO), upper (UP), equality (FX),
or neutral (N). The latter case does not introduce any restriction on
the optimization, and is used only to generate a new reporting quantity.

#### Other parameters

Features that were added to TIMES over the years require new parameters.
For instance, the Climate Module of TIMES (chapter 7), the Lumpy
Investment feature (chapter 10), and several others. These will be
alluded to in the corresponding chapters of this Part I, and more
completely described in section 2 and Appendices of Part II.

An advanced feature allows the user to define certain process parameters
as *vintaged* (i.e. dependent upon the date of installation of new
capacity). For instance, the investment cost and fuel efficiency of a
specific type of automobile will depend on the model year[^9].

Finally, another advanced TIMES feature renders some parameters
dependent *also on the age* of the technology. For instance, the annual
maintenance cost of an automobile could be defined to remain constant
for say 3 years and then increase in a specified manner each year after
the third year.

### Parameters attached to commodities

This subsection concerns parameters attached to each commodity,
irrespective of how the commodity is produced or consumed. The next
subsection concerns commodity flows. Commodity-oriented parameters fall
into the same categories as those attached to processes.

#### Technical parameters 

*Technical parameters* associated with commodities include overall
efficiency (for instance the overall electric grid efficiency), and the
time-slices over which that commodity is to be tracked. For demand
commodities, in addition, the annual projected demand and load curves
(if the commodity has a sub-annual time-slice resolution) can be
specified.

#### Economic and policy parameters 

*Economic parameters* include additional costs, taxes, and subsidies on
the overall or net production of a commodity. These cost elements are
then added to all other (implicit) costs of that commodity. In the case
of a demand service, additional parameters define the demand curve (i.e.
the relationship between the quantity of demand and its price). These
parameters are: the demand's own-price elasticity, the total allowed
range of variation of the demand value, and the number of steps to use
for the discrete approximation of the curve.

*Policy based parameters* include bounds (at each period or cumulative
over user defined years) on the gross or net production of a commodity,
or on the imports or exports of a commodity by a region.

#### Bounds

In TIMES the net or the total production of each commodity may be
explicitly represented by a variable, if needed for imposing a bound or
a tax. A similar variety of bounding parameters exists for commodities
as for processes.

### Parameters attached to commodity flows

A *commodity flow* (more simply, a *flow*) is an amount of a given
commodity produced or consumed by a given process. Some processes have
several flows entering or leaving them, perhaps of different types
(fuels, materials, demands, or emissions). In TIMES, each flow has a
variable attached to it, as well as several attributes (parameters or
sets).

Flow related parameters confer enormous flexibility for modeling a large
spectrum of conditions.

#### Technical parameters

*Technical parameters,* along with some set attributes, permit full
control over the maximum and/or minimum share a given input or output
flow may take within the same commodity group. For instance, a flexible
turbine may accept oil and/or gas as input, and the modeler may use a
parameter to limit the share of oil to, say, at most 40% of the total
fuel input. Other parameters and sets define the amount of certain
outflows in relation to certain inflows (e.g., efficiency, emission rate
by fuel). For instance, in an oil refinery a parameter may be used to
set the total amount of refined products equal to 92% of the total
amount of crude oils (s) entering the refinery, or to calculate certain
emissions as a fixed proportion of the amount of oil consumed. If a flow
has a sub-annual time-slice resolution, a load curve can be specified
for the flow. It is possible to define not only load curves for a flow,
but also bounds on the share of a flow in a specific time-slice relative
to the annual flow, e.g. the flow in the time-slice "Winter-Day" has to
be at least 10 % of the total annual flow. Refer to section 5.4
describing TIMES constraints for details. Cumulative bounds on a process
flow are also allowed.

#### Economic and policy parameters

*Economic or policy parameters* include delivery and other variable
costs, taxes and subsidies attached to an individual process flow.

#### Bounds

Bounds may be defined for flows in similar variety that exists for
commodities.

### Parameters attached to the entire RES

These parameters include currency conversion factors (in a
multi-regional model), region-specific time-slice definitions, a
region-specific general discount rate, and reference year for
calculating the discounted total cost (objective function). In addition,
certain switches are needed to control the activation of the data
interpolation procedure as well as special model features to be used.
The complete set of switches is described in Part III.

## Process and commodity classification

Although TIMES does not explicitly differentiate processes or
commodities that belong to different portions of the RES (with the
notable exceptions of storage and trading processes), there are three
ways in which some differentiation does occur.

First, TIMES requires the definition of Primary Commodity Groups
(*pcg*), i.e. subsets of commodities *of the same nature* entering or
leaving a process. TIMES utilizes the pcg to define the activity of the
process, and also its capacity. For instance, the *pcg* of an oil
refinery is defined as the set of energy forms produced by the plant;
and the activity of the refinery is thus simply the sum of all its
energy outputs (excluding any outputs that are non energy).

Besides establishing the process activity and capacity, these groups are
convenient aids for defining certain complex quantities related to
process flows, as discussed in chapter 5 and in PART II, section 2.1.

Even though TIMES *does not require* that the user provide many set
memberships, the TIMES reporting step does pass some set declarations to
the VEDA-BE result-processing system[^10]to facilitate construction of
results analysis tables. These include process subsets to distinguish
demand devices, energy processes, material processes (by weight or
volume), refineries, electric production plants, coupled heat and power
plants, heating plants, storage technologies and distribution (link)
technologies; and commodity subsets for energy, useful energy demands
(split into six aggregate sub-sectors), environmental indicators,
currencies, and materials.

Besides the definition of *pcg*\'s and that of VEDA reporting sets,
there is a third instance of commodity or process differentiation which
is not embedded in TIMES, but rests entirely on the modeler. A modeler
may well want to choose process and commodity names in a judicious
manner so as to more easily identify them when browsing through the
input database or when examining results. As an example, the TIAM-World
multi-regional TIMES model (Loulou, 2007) adopts a naming convention
whereby the first three characters of a commodity's name denote the
sector and the next three the fuel (e.g., light fuel oil used in the
residential sector is denoted RESLFO). Similarly, process names are
chosen so as to identify the sub-sector or end-use (first three
characters), the main fuel used (next three), and the specific
technology (last four). For instance, a standard (0001) residential
water heater (RWH) using electricity (ELC) is named RWHELC0001. Naming
conventions may thus play a critical role in allowing the easy
identification of an element's position in the RES and thus facilitate
the analysis and reporting of results.

Similarly, energy services may be labeled so that they are more easily
recognized. For instance, the first letter may indicate the broad sector
(e.g. 'T' for transport) and the second letter designate any homogenous
sub-sectors (e.g. 'R' for road transport), the third character being
free.

In the same fashion, fuels, materials, and emissions may be identified
so as to immediately designate the sector and sub-sector where they are
produced or consumed. To achieve this, some fuels have to change names
when they change sectors. This is accomp­lished via processes whose
primary role is to change the name of a fuel. In addition, such a
process may serve as a bearer of sector wide parameters such as
distribution cost, price markup, tax, that are specific to that sector
and fuel. For instance, a tax may be levied on industrial distillate use
but not on agricultural distillate use, even though the two commodities
are physically identical.

# Economic rationale of the TIMES modeling approach

This chapter provides a detailed economic interpretation of TIMES and
other partial equilibrium models based on maximizing total surplus.
Partial equilibrium models have one common feature -- they
simultaneously configure the production and consumption of commodities
(i.e. fuels, materials, and energy services) and their prices. The price
of producing a commodity affects the demand for that commodity, while at
the same time the demand affects the commodity's price. A market is said
to have reached an equilibrium at prices *p\** and quantities *q\** when
no consumer wishes to purchase less than *q\** and no producer wishes to
produce more than *q\** at price *p\**. Both *p\** and *q\** are vectors
whose dimension is equal to the number of different commodities being
modeled. As will be explained below, when all markets are in equilibrium
the total economic surplus is maximized.

The concept of total surplus maximization extends the direct cost
minimization approach upon which earlier bottom-up energy system models
were based. These simpler models had fixed energy service demands, and
thus were limited to minimizing the cost of supplying these demands. In
contrast, the TIMES demands for energy services are themselves elastic
to their own prices, thus allowing the model to compute a *bona fide*
supply-demand equilibrium. This feature is a fundamental step toward
capturing the main feedback from the economy to the energy system.

Section 3.1 provides a brief review of different types of energy models.
Section 3.2 discusses the economic rationale of the TIMES model with
emphasis on the features that distinguish TIMES from other bottom-up
models (such as the early incarnations of MARKAL, see Fishbone and
Abilock, 1981 and Berger et al., 1992, though MARKAL has since been
extended beyond these early versions). Section 3.3 describes the details
of how price elastic demands are modeled in TIMES, and section 3.4
provides additional discussion of the economic properties of the model.

## A brief classification of energy models

Many energy models are in current use around the world, each designed to
emphasize a particular facet of interest. Differences include: economic
rationale, level of disaggregation of the variables, time horizon over
which decisions are made (which is closely related to the type of
decisions, i.e., only operational planning or also investment
decisions), and geographic scope. One of the most significant
differentiating features among energy models is the degree of detail
with which commodities and technologies are represented, which will
guide our classification of models into two major classes, as explained
in the following very streamlined classification.

### 'Top-down' models

At one end of the spectrum are aggregated *General Equilibrium* (GE)
models. In these each sector is represented by a production function
designed to simulate the potential substitutions between the main
factors of production (also highly aggregated into a few variables such
as: energy, capital, and labor) in the production of each sector's
output. In this model category are found a number of models of national
or global energy systems. These models are usually called "top-down",
because they represent an entire economy via a relatively small number
of aggregate variables and equations. In these models, production
function parameters are calculated for each sector such that inputs and
outputs reproduce a single base historical year.[^11] In policy runs,
the mix of inputs[^12] required to produce one unit of a sector's output
is allowed to vary according to user-selected elasticities of
substitution. Sectoral production functions most typically have the
following general form:

$X_{s} = A_{0}\left( B_{K} \cdot K_{s}^{\rho} + B_{L} \cdot L_{S}^{\rho} + B_{E} \cdot E_{S}^{\rho} \right)^{1/\rho}$
(3-1)

where ***X~S\ ~***is the output of sector *S,*

> ***K~S~**, **L~S~**, and **E~S~*** are the inputs of capital, labor
> and energy needed to
>
> produce one unit of output in sector *S,*
>
> ***ρ*** is the elasticity of substitution parameter,
>
> ***A~0~*** and the ***B***'s are scaling coefficients.

The choice of *ρ* determines the ease or difficulty with which one
production factor may be substituted for another: the smaller *ρ* is
(but still greater than or equal to 1), the easier it is to substitute
the factors to produce the same amount of output from sector *S*. Also
note that the degree of factor substitutability does not vary among the
factors of production --- the ease with which capital can be substituted
for labor is equal to the ease with which capital can be substituted for
energy, while maintaining the same level of output. GE models may also
use alternate forms of production function (3-1), but retain the basic
idea of an explicit substitutability of production factors.

### 'Bottom-up' models

At the other end of the spectrum are the very detailed, *technology
explicit* models that focus primarily on the energy sector of an
economy. In these models, each important energy-using technology is
identified by a detailed description of its inputs, outputs, unit costs,
and several other technical and economic characteristics. In these
so-called 'bottom-up' models, a sector is constituted by a (usually
large) number of logically arranged technologies, linked together by
their inputs and outputs (*commodities*, which may be energy forms or
carriers, materials, emissions and/or demand services). Some bottom-up
models compute a partial equilibrium via maximization of the total net
(consumer and producer) surplus, while others simulate other types of
behavior by economic agents, as will be discussed below. In bottom-up
models, one unit of sectoral output (e.g., a billion vehicle kilometers,
one billion tonnes transported by heavy trucks or one petajoule of
residential cooling service) is produced using a mix of individual
technologies' outputs. Thus the production function of a sector is
*implicitly* constructed, rather than explicitly specified as in more
aggregated models. Such implicit production functions may be quite
complex, depending on the complexity of the reference energy system of
each sector (sub-RES).

### Hybrid approaches

While the above dichotomy applied fairly well to earlier models, these
distinctions now tend to be somewhat blurred by advances in both
categories of model. In the case of aggregate top-down models, several
general equilibrium models now include a fair amount of fuel and
technology disaggregation in the key energy producing sectors (for
instance: electricity production, oil and gas supply). This is the case
with MERGE[^13] and SGM[^14], among others.

In the other direction, the more advanced bottom-up models are 'reaching
up' to capture some of the effects of the entire economy on the energy
system. The TIMES model has end-use demands (including demands for
industrial output) that are sensitive to their own prices, and thus
captures the impact of rising energy prices on economic output and *vice
versa*. Recent incarnations of technology-rich models (including TIMES)
are multi-regional, and thus are able to consider the impacts of
energy-related decisions on trade. It is worth noting that while the
multi-regional top-down models have always represented trade, they have
done so with a very limited set of traded commodities -- typically one
or two, whereas there may be quite a number of traded energy forms and
materials in multi-regional bottom-up models.

MARKAL-MACRO (Manne and Wene, 1992) and TIMES-MACRO (Kypreos and
Lehtila, 2013) are hybrid models combining the technological detail of
MARKAL with a succinct representation of the macro-economy consisting of
a single producing sector in a single region. Because of its succinct
single-sector production function, MARKAL-MACRO is able to compute a
general equilibrium in a single optimization step. More recently,
TIMES_MACRO-MSA (section 12.2) is based on the computation of a
multi-regional global equilibrium, but requires an iterative process to
do so. MESSAGE (Messner and Strubegger, 1995) links a bottom-up model
based on the EFOM paradigm with a macro module, and computes a global,
multi-regional equilibrium iteratively. The NEMS (US EIA, 2000) model is
another example of a full linkage between several technology rich
modules of the various energy subsectors and a set of macro-economic
equations, and requires iterative resolution methods.

In spite of these advances in both classes of models, there remain
important differences. Specifically:

-   Top-down models encompass macroeconomic variables beyond the energy
    sector proper, such as wages, consumption, and interest rates, and

-   Bottom-up models have a rich representation of the variety of
    technologies (existing and/or future) available to meet energy
    needs, and, they often have the capability to track a much wider
    variety of traded commodities. They are also more adapted to the
    representation of micro policies targeting specific technologies or
    commodities.

The top-down vs. bottom-up approach is not the only relevant difference
among energy models. Among top-down models, the so-called Computable
General Equilibrium models (CGE) described above differ markedly from
the *macro econometric models*. The latter do not compute equilibrium
solutions, but rather simulate the flows of capital and other monetized
quantities between sectors (see, e.g., Meade, 1996 on the LIFT model).
They use econometrically derived input-output coefficients to compute
the impacts of these flows on the main sectoral indicators, including
economic output (GDP) and other variables (labor, investments). The
sector variables are then aggregated into national indicators of
consumption, interest rate, GDP, labor, and wages.

Among technology explicit models also, two main classes are usually
distinguished: the first class is that of the partial equilibrium models
such as MARKAL, MESSAGE, and TIMES, that use optimization techniques to
compute a least cost (or maximum surplus) path for the energy system.
The second class is that of *simulation* models, where the emphasis is
on representing a system not governed purely by financial costs and
profits. In these simulation models (e.g., CIMS, Jaccard et al. 2003),
investment decisions taken by a representative agent (firm or consumer)
are only partially based on profit maximization, and technologies may
capture a share of the market even though their life-cycle cost may be
higher than that of other technologies. Simulation models use
market-sharing formulas that preclude the easy computation of
equilibrium -- at least not in a single pass. The SAGE (US EIA, 2002)
incarnation of the MARKAL model possesses a market sharing mechanism
that allows it to reproduce certain behavioral characteristics of
observed markets.

## The core TIMES paradigm

In the rest of this chapter, we present the properties of the **core
TIMES** paradigm. As will be seen in chapters8 to 12, some of these
properties are not applicable to several important TIMES variants. The
reader should keep this caveat in mind when contemplating the use of
some features that are described in these 5 chapters.

Since certain portions of this and the next sections require an
understanding of the concepts and terminology of Linear Programming, the
reader requiring a brush-up on this topic may first read Appendix B, and
then, if needed, some standard textbook on LP, such as Hillier and
Lieberman (2009), Chvàtal (1983), or Schrijver (1986). The application
of Linear Programming to microeconomic theory is covered in two
historically important references, Gale (1960 and 11th edition 1989),
and in Dorfman, Samuelson, and Solow (1958, and 1987 reprint).

A brief description of the core TIMES model generator would express that
it is:

-   *Technologically explicit, integrated*;

-   *Multi-regional*; and

-   *Partial equilibrium* (with *price elastic* demands for energy
    services) in *competitive markets* with *perfect foresight*. It will
    be seen that such an equilibrium entails *marginal value pricing* of
    all commodities.

We now proceed to flesh out each of these properties.

### A technologically explicit integrated model

As already presented in chapter 2 (and described in much more detail in
Part II, section 3), each technology is described in TIMES by a number
of technical and economic parameters. Thus each technology is explicitly
identified (given a unique name) and distinguished from all others in
the model. A mature TIMES model may include several thousand
technologies in all sectors of the energy system (energy procurement,
conversion, processing, transmission, and end-uses) in each region. Thus
TIMES is not only technologically explicit, it is technology rich and it
is integrated as well. Furthermore, the number of technologies and their
relative topology may be changed at will, purely via data input
specification, without the user ever having to modify the model's
equations. The model is thus to a large extent *data driven*.

### Multi-regional

Some existing TIMES models comprise several dozen regional modules, or
more. The number of regions in a model is limited only by the difficulty
of solving LP's of very large size. The individual regional modules are
linked by energy and material trading variables, and by emission permit
trading variables, if desired. The linking variables transform the set
of regional modules into a *single* multi-regional (possibly global)
energy model, where actions taken in one region may affect all other
regions. This feature is essential when global as well as regional
energy and emission policies are being simulated. Thus a multi-regional
TIMES model is geographically integrated.

### Partial equilibrium

The core version of TIMES computes a partial equilibrium on energy
markets. This means that the model computes both the *flows* of energy
forms and materials as well as their *prices*, in such a way that, at
the prices computed by the model, the suppliers of energy produce
exactly the amounts that the consumers are willing to buy. This
equilibrium feature is present at every stage of the energy system:
primary energy forms, secondary energy forms, and energy services[^15].
A supply-demand equilibrium model has as its economic rationale the
maximization of the total surplus, defined as the sum of all suppliers'
and consumers' surpluses. The mathematical method used to maximize the
surplus must be adapted to the particular mathematical properties of the
model. In TIMES, these properties are as follows:

-   Outputs of a technology are linear functions of its inputs
    (subsection 3.2.3.1)[^16];

-   Total economic surplus is maximized over the entire horizon
    (3.2.3.2); and

-   Energy markets are competitive, with perfect foresight
    (3.2.3.3)[^17].

As a result of these assumptions the following additional properties
hold:

-   The market price of each commodity is equal to its marginal value in
    the overall system (3.2.4); and

```{=html}
<!-- -->
```
-   Each economic agent maximizes its own profit or utility (3.2.5).

#### Linearity

A linear input-to-output relationship first means that each technology
represented may be implemented at any capacity, from zero to some upper
limit, without economies or dis­economies of scale. In a real economy, a
given technology is usually available in discrete sizes, rather than on
a continuum. In particular, for some real life technologies, there may
be a minimum size below which the technology may not be implemented (or
else at a prohibitive cost), as for instance a nuclear power plant, or a
hydroelectric project. In such cases, because TIMES assumes that all
technologies may be implemented in any size, it may happen that the
model's solution shows some technology's capacity at an unrealistically
small size. It should however be noted that in most applications, such a
situation is relatively infrequent and often innocuous, since the scope
of application is at the country or region's level, and thus large
enough so that small capacities are unlikely to occur.

On the other hand, there may be situations where plant size matters, for
instance when the region being modeled is very small. In such cases, it
is possible to enforce a rule by which certain capacities are allowed
only in multiples of a given size (e.g., build or not a gas pipeline),
by introducing *integer variables*. This option, referred to as lumpy
investment (LI), is available in TIMES and is discussed in chapter 10.
This approach should, however, be used sparingly because it may greatly
increase solution time.

It is the linearity property that allows the TIMES equilibrium to be
computed using Linear Programming techniques. In the case where
economies of scale or some other non-convex relationship is important to
the problem being investigated, the optimization program would no longer
be linear or even convex. We shall examine such cases in chapters 9 to
12.

We must now mention a common misconception regarding linearity: the fact
that TIMES equations are linear *does not mean that production functions
behave in a linear fashion; far from it*. Indeed, the TIMES production
functions are usually highly non-linear (although convex), consisting of
a stepped sequence of linear functions. As a simple example, a supply of
some resource is almost always represented as a sequence of segments,
each with rising (but constant within an interval) unit cost. The
modeler defines the 'width' of each interval so that the resulting
supply curve may simulate any non-linear convex function. In brief,
dis­economies of scale are easily represented in linear models.

#### Maximization of total surplus: Price equals marginal value

The *total surplus* of an economy is the sum of the suppliers' and the
consumers' surpluses. The term *supplier* designates any economic agent
that produces (and/or sells) one or more commodities i.e., in TIMES, an
energy form, a material, an emission permit, and/or an energy service. A
*consumer* is a buyer of one or more commodities. In TIMES, the
suppliers of a commodity are technologies that procure a given
commodity, and the consumers of a commodity are technologies or service
segments that consume a given commodity. Some (indeed most) technologies
are both suppliers and consumers. Therefore, for each commodity the RES
defines a complex set of suppliers and consumers.

It is customary in microeconomics to represent the set of suppliers of a
commodity by their *inverse production function*, that plots the
marginal production cost of the commodity (vertical axis) as a function
of the quantity supplied (horizontal axis). In TIMES, as in other linear
optimization models, the supply curve of a commodity, with the exception
of end-use demands, is entirely determined endogenously by the model. It
is a standard result of Linear Programming theory that the inverse
supply function is step-wise constant and increasing in each factor (see
Figures 3.1 and 3.3 for the case of a single commodity[^18]). Each
horizontal step of the inverse supply function indicates that the
commodity is produced by a certain technology or set of technologies in
a strictly linear fashion. As the quantity produced increases, one or
more resources in the mix (either a technological potential or some
resource's availability) is exhausted, and therefore the system must
start using a different (more expensive) technology or set of
technologies in order to produce additional units of the commodity,
albeit at higher unit cost. Thus, each change in production mix
generates one step of the staircase production function with a value
higher than the preceding step. The width of any particular step depends
upon the technological potential and/or resource availability associated
with the set of technologies represented by that step.

![](media/image3.wmf)*Figure 3.1. Equilibrium in the case of an energy
form: the model implicitly constructs both the supply and the demand
curves (note that the equilibrium is multiple in this configuration)*

In a similar manner, each TIMES model instance defines a series of
inverse demand functions. In the case of demands, two cases are
distinguished. First, if the commodity in question is an energy carrier
whose production and consumption are endogenous to the model, then its
demand function is *implicitly* constructed within TIMES, and is a
step-wise constant, decreasing function of the quantity demanded, as
illustrated in Figure 3.1 for a single commodity. If on the other hand
the commodity is a demand for an energy service, then its demand curve
is *defined by the user* via the specification of the own-price
elasticity of that demand, and the curve is in this instance a smoothly
decreasing curve as illustrated in Figure 3.2[^19]. In both cases, the
supply-demand equilibrium is at the intersection of the supply function
and the demand function, and corresponds to an equilibrium quantity Q~E~
and an equilibrium price P~E~[^20]. At price P~E~, suppliers are willing
to supply the quantity Q~E~ and consumers are willing to buy exactly
that same quantity Q~E.~ Of course, the TIMES equilibrium concerns a
large number of commodities simultaneously, and thus the equilibrium is
a multi-dimensional analog of the above, where Q~E~ and P~E~ are now
vectors rather than scalars.

As already mentioned, the demand curves of most TIMES commodities (i.e.
energy carriers, materials, emission permits) are implicitly constructed
endogenously as an integral part of the solution of the LP. For each
commodity that is an energy service, the user *explicitly* defines the
demand *function* by specifying its own price elasticity. In TIMES, each
energy service demand is assumed to have a constant own price elasticity
function of the form (see Figure 3.2):

DM/DM~0~ = (P/P~0~)^E^ (3-2)

Where {*DM~0~ ,P~0~*} is a reference pair of demand and price values for
that energy service over the forecast horizon, and *E* is the (negative)
own price elasticity of that energy service demand, as specified by the
user (note that although not obvious from the notation, this price
elasticity may vary over time). The pair {*DM~0~, P~0~*} is obtained by
solving TIMES for a reference scenario. More precisely, *DM~0~*is the
demand projection estimated by the user in the reference scenario
(usually based upon explicitly defined relationships to economic and
demographic drivers), and P~0~ is the shadow price of that energy
service demand in the dual solution of the reference case scenario. The
precise manner in which the demand functions are discretized and
incorporated in the TIMES objective function is explained in chapter 4.

Using Figure 3.1 as an example, the definition of the suppliers' surplus
corresponding to a certain point S on the inverse supply curve is the
difference between the total revenue and the total cost of supplying a
commodity, i.e. the gross profit. In Figure 3.1, the surplus is thus the
area between the horizontal segment SS' and the inverse supply curve.
Similarly, the consumers' surplus for a point C on the inverse demand
curve, is defined as the area between line segment CC' and the inverse
demand curve. This area is a consumer's analog to a producer's profit;
more precisely it is the cumulative opportunity gain of all consumers
who purchase the commodity at a price lower than the price they would
have been willing to pay. Thus, for a given quantity Q, the total
surplus (suppliers' plus consumers') is simply the area between the two
inverse curves situated at the left of Q. It should be clear from Figure
3.1 that the total surplus is maximized when Q is exactly equal to the
equilibrium quantity Q~E~. Therefore, we may state (in the single
commodity case) the following Equivalence Principle:

> *"The supply-demand equilibrium is reached when the total surplus is
> maximized."*

This is a remarkably useful result, as it leads to a method for
computing the equilibrium, as will be see in much detail in Chapter 4.

In the multi-dimensional case, the proof of the above statement is less
obvious, and requires a certain qualifying property (called the
integrability property) to hold (Samuelson, 1952, Takayama and Judge,
1972). One sufficient condition for the integrability property to be
satisfied is realized when the cross-price elasticities of any two
energy forms are equal, viz.

$$\partial P_{j}/\partial Q_{i} = \partial P_{i}/\partial Q_{j}\text{for} ⥂ ⥂ \text{all}i,j$$

In the case of commodities that are end-use energy services, these
conditions are trivially satisfied in TIMES because we have assumed zero
cross price elasticities. In the case of an endogenous energy carrier,
where the demand curve is implicitly derived, it is also easy to show
that the integrability property is always satisfied[^21]. Thus the
equivalence principle is valid in all cases.

In summary, the equivalence principle guarantees that the TIMES
supply-demand equilibrium maximizes total surplus. The total surplus
concept has long been a mainstay of social welfare economics because it
takes into account both the surpluses of consumers and of
producers.[^22]

![](media/image7.wmf)*Figure 3.2. Equilibrium in the case of an energy
service: the user explicitly provides the demand curve, usually using a
simple functional form (see text for details)*

*Remark:* In older versions of MARKAL, and in several other least-cost
bottom-up models, energy service demands are exogenously specified by
the modeler, and only the cost of supplying these energy services is
minimized. Such a case is illustrated in Figure 3.3 where the "inverse
demand curve" is a vertical line. The objective of such models was
simply the minimization of the total cost of meeting exogenously
specified levels of energy service.

![](media/image8.wmf)*Figure 3.3. Equilibrium when an energy service
demand is fixed*

#### Competitive energy markets with perfect foresight

Competitive energy markets are characterized by perfect information and
atomic economic agents, which together preclude any of them from
exercising market power. That is, neither the level at which any
individual producer supplies, nor the level any individual consumer
acquires, affects the equilibrium market price (because there are many
other buyers and sellers to replace them). It is a standard result of
microeconomic theory that the assumption of competitive markets entails
that the market price of a commodity is equal to its marginal value in
the economy (Samuelson, 1952). This is of course also verified in the
TIMES economy, as discussed in the next subsection.

Of course, real world energy markets are not always competitive. For
instance, an electric utility company may be a (regulated) monopoly
within an entire country, or a cartel of oil producing countries may
have market power on oil markets. There are ways around these so-called
"market imperfections". For instance, concerning the monopolistic
utility, a socially desirable approach would be to first use the
assumption of marginal cost pricing, so as to determine a socially
optimal plan for the monopoly, and then to have the regulatory agency
enforce such a plan, including the principle of marginal cost pricing.
The case of the oil producers' cartel is less simple, since there is no
global regulatory agency to ensure that oil producers act in a socially
optimal fashion. There are however ways to use equilibrium models such
as TIMES in order to faithfully represent the market power of certain
economic agents, as exemplified in (Loulou et al., 2007).

In the core version of TIMES, the perfect information assumption extends
to the entire planning horizon, so that each agent has perfect
foresight, i.e. complete knowledge of the market's parameters, present
and future. Hence, the equilibrium is computed by maximizing total
surplus in one pass for the entire set of periods. Such a farsighted
equilibrium is also called an *inter-temporal dynamic equilibrium*.

Note that there are at least two ways in which the perfect foresight
assumption may be voided: in one variant, agents are assumed to have
foresight over a limited portion of the horizon, say one or a few
periods. Such an assumption of limited foresight is embodied in the
TIMES feature discussed in chapter 9, as well as in the SAGE variant of
MARKAL (US EIA, 2002). In another variant, foresight is assumed to be
imperfect, meaning that agents may only *probabilistically* know certain
key future events. This assumption is at the basis of the TIMES
Stochastic Programming option, discussed in chapter 8.

### Marginal value pricing

We have seen in the preceding subsections that the TIMES equilibrium
occurs at the intersection of the inverse supply and inverse demand
curves. It follows that the equilibrium prices are equal to the marginal
system values of the various commodities. From a different angle, the
duality theory of Linear Programming (chapter 14) indicates that for
each constraint of the TIMES linear program there is a *dual variable.*
This dual variable (when an optimal solution is reached) is also called
the constraint's *shadow price*[^23]*,* and is equal to the marginal
change of the objective function per unit increase of the constraint's
right-hand-side. For instance, the shadow price of the balance
constraint of a commodity (whether it be an energy form, material, a
service demand, or an emission) represents the competitive market price
of the commodity.

The fact that the price of a commodity is equal to its marginal value is
an important feature of competitive markets. Duality theory does not
necessarily indicate that the marginal value of a commodity is equal to
the marginal cost of *producing* that commodity. For instance, in the
equilibrium shown in Figure 3.4 the price does not correspond to *any*
marginal supply cost, since it is situated at a discontinuity of the
inverse supply curve. In this case, the price is precisely determined by
demand rather than by supply, and the term *marginal cost pricing* (so
often used in the context of optimizing models) is *sensu stricto*
incorrect. The term *marginal value pricing* is a more appropriate term
to use.

It is important to reiterate that marginal value pricing *does not imply
that suppliers have zero profit*. Profit is exactly equal to the
suppliers' surplus, and is generally positive. Only the last few units
produced may have zero profit, if, and when, their production cost
equals the equilibrium price.

In TIMES the shadow prices of commodities play a very important
diagnostic role. If some shadow price is clearly out of line (i.e. if it
seems much too small or too large compared to the anticipated market
prices), this indicates that the model's database may contain some
errors. The examination of shadow prices is just as important as the
analysis of the quantities produced and consumed of each commodity and
of the technological investments. ![](media/image9.wmf)

*Figure 3.4. Case where the equilibrium price is not equal to any
marginal supply cost.*

### Profit maximization: the Invisible Hand

An interesting property may be derived from the assumptions of
competitiveness. While the avowed objective of the TIMES model is to
maximize the overall surplus, it is also true that each economic agent
in TIMES maximizes its own surplus. This property is akin to the famous
'invisible hand' property of competitive markets, and may be established
rigorously by the following theorem that we state in an informal manner:

> *[Theorem]{.underline}: Let (p\*,q\*) be a pair of equilibrium vectors
> that maximize total surplus. If we now replace the original TIMES
> linear program by one where all commodity prices are
> [fixed]{.underline} at value p\*, and we let each agent maximize its
> own surplus, the vector of optimal quantities produced or purchased by
> the agents also maximizes the total surplus*[^24]*.*

This property is important inasmuch as it provides an alternative
justification for the class of equilibria based on the maximization of
total surplus. It is now possible to shift the model's rationale from a
global, societal one (total surplus maximization), to a local,
decentralized one (individual utility maximization). Of course, the
equivalence suggested by the theorem is valid only insofar as the
marginal value pricing mechanism is strictly enforced---that is, neither
an individual producer nor an individual consumer may affect market
prices---both are price takers. Clearly, some markets are not
competitive in the sense the term has been used here. For example, the
behavior of a few oil producers has a dramatic impact on world oil
prices, which then depart from their marginal system value. Market
power[^25] may also exist in cases where a few consumers dominate a
market.

# Core TIMES model: Mathematics of the computation of the supply-demand equilibrium

In the preceding chapter, we have seen that TIMES does more than
minimize the cost of supplying energy services. Instead, it computes a
supply-demand equilibrium where both the energy supplies and the energy
service demands are endogenously determined by the model. The
equilibrium is driven by the user-defined specification of demand
functions, which determine how each energy service demand varies as a
function of the current market price of that energy service. The TIMES
code assumes that each demand has constant own-price elasticity in a
given time period, and that cross price elasticities are zero. We have
also seen that economic theory establishes that the equilibrium thus
computed corresponds to the maximization of the net total surplus,
defined as the sum of the suppliers' and consumers' surpluses. We have
argued in section 3.2 that the total net surplus has often been
considered a valid metric of societal welfare in microeconomic
literature, and this fact confers strong validity to the equilibrium
computed by TIMES. Thus although TIMES falls short of computing a
general equilibrium, it does capture a major element of the feedback
effects not previously accounted for in bottom-up energy models.

In this chapter we provide the details on how the equilibrium is
transformed into an optimization problem and solved accordingly.

Historically, the approach was first used in the Project Independence
Energy System (PIES, see Hogan, 1975), although in the context of
demands for final energy rather than for energy services as in TIMES or
MARKAL. It was then proposed for MARKAL model by Tosato (1980) and
Altdorfer (1982), and later made available as a standard MARKAL option
by Loulou and Lavigne (1995). The TIMES implementation is identical to
the MARKAL one.

## Theoretical considerations: the Equivalence Theorem

The computational method is based on the equivalence theorem presented
in chapter 3, which we restate here:

*\"A supply/demand economic equilibrium is reached when the sum of the
producers and the consumers surpluses is maximized\"*

Figure 3.2 of Chapter 3 provides a graphical illustration of this
theorem in a case where only one commodity is considered.

## Mathematics of the TIMES equilibrium

### Defining demand functions

From chapter 3, we have the following demand function for each demand
category ***i***

$$
{DM_{i}/D{M_{i}}^{0} = (p_{i}/p_{i}^{0})^{E_{i}}(4 - 1)}$$

Or its inverse:

$$p_{i} = p_{i}^{0} \cdot (DM_{i}/D{M_{i}}^{0})^{1/E_{i}}$$

where the superscript '0' indicates the reference case, and the
elasticity ***E~i\ ~***is negative. Note also that the elasticity may
have two different values, one for upward changes in demand, the other
for downward changes.

### Formulating the TIMES equilibrium

With inelastic demands (i.e. pure cost minimization), the TIMES model
may be written as the following Linear Program:

$Min\ c \bullet X$ (4 -- 2)

$s.t\ \sum_{k}^{}{{VAR_{ACT}}_{k,j}(t) \geq {DM}_{i}(t)\ \ \ \ \ i = 1,2,\ldots.,I;t = 1,..,T}$
(4 -- 3)

$and\ \ \ B\  \bullet X\  \geq b$ (4 -- 4)

where ***X*** is the vector of all TIMES variables and ***I*** is the
number of demand categories. In words:

-   (4-2) expresses the total discounted cost to be minimized. See
    chapter 5 for details on the list of TIMES variables ***X***, and on
    the cost vector ***c.***

-   (4-3) is the set of demand satisfaction constraints (where the
    ***VAR_ACT*** variables are the activity levels of end-use
    technologies, and the ***DM*** right-hand-sides are the exogenous
    demands to satisfy).

-   (4-4) is the set of all other TIMES constraints, which need not be
    explicated here, and are presented in chapter 5.

When demand are elastic, TIMES must compute a supply/demand equilibrium
of the optimization problem (4-2) through (4-4), where the demand side
adjusts to changes in prices, and the prevailing demand prices are the
marginal costs of the demand categories (i.e. *p~i~* is the marginal
cost of producing demand *DM~i~*). *A priori* this seems to be a
difficult task, because the demand prices are computed as part of the
dual solution to that optimization problem. The Equivalence Theorem,
however, states that the equilibrium is reached as the solution of the
following mathematical program, where the objective is to maximize the
net total surplus:

![](media/image10.emf)

where ***X*** is the vector of all TIMES variables, (4-5) expresses the
total net surplus, and ***DM(t )***is now a vector of *variables* in
(4-6), rather than fixed demands. The integral in (4-5) is easily
computed, yielding the following maximization program:

![](media/image11.emf)

We are almost there, but not quite, since the
***\[DM~i~(t)\]^-1/Ei\ ^***are non linear expressions and thus not
directly usable in an L.P.

### Linearization of the Mathematical Program

The Mathematical Program embodied in (4-5)', (4-6)' and (4-7)' has a
non-linear objective function. Because the latter is separable (i.e.
does not include cross terms) and concave in the *DM~i\ ~*variables,
each of its terms is easily linearized by piece-wise linear functions
which approximate the integrals in (4-5). This is the same as saying
that the inverse demand curves are approximated by staircase functions,
as illustrated in figure 4.1. By so doing, the resulting optimization
problem becomes linear again. The linearization proceeds as follows.

a)  For each demand category ***i***, and each time period ***t***, the
    user selects a range ***R(t)~i~***, i.e. the distance between some
    values ***DM~i~(t)*~min~** and ***DM~i~(t)*~max~*. ***The user
    estimates that the demand value ***DM~i~(t)*** will always remain
    within such a range, even after adjustment for price effects (for
    instance the range could be equal to the reference demand
    ***DM^o^~i~(t)*** plus or minus 50%).

b)  Select a grid that divides each range into a number *n* of equal
    width intervals. Let ß~i~(t) be the resulting common width of the
    grid*, **ß~i~(t)= R~i~(t)/n*****.** See Figure 4.1 for a sketch of
    the non-linear expression and of its step-wise constant
    approximation. The number of steps, *n*, should be chosen so that
    the step-wise constant approximation remains close to the exact
    value of the function.

c)  For each demand segment ***DM~i~(t)*** define *n* step-variables
    (one per grid interval), denoted *s~1,i~(t), s~2,i~ (t), ...,
    s~n,i~(t)*. Each *s* variable is bounded below by 0 and above by
    *ß~i~(t)*. One may now replace in equations (4-5)' and (4-6)' each
    ***DM~i~(t)*** variable by the sum of the *n*-step variables, and
    each non-linear term in the objective function by a weighted sum of
    the *n* step-variables, as follows:

> ![](media/image12.emf)
>
> and

![](media/image13.emf)

The ***A~j,i,t~*** term is equal to the value of the inverse demand
function of the ***j^th\ ^***demand at the mid-point of the ***i^th^***
interval. The resulting Mathematical Program is now fully linearized.

Since the ***A~j,i,t~*** terms have decreasing values (due to the
concavity of the curve), the optimization will always make sure that the
***s~j,I\ ~***variables are increased consecutively and in the correct
order, thus respecting the step-wise constant approximation described
above.

*Remark:* Instead of maximizing the linearized objective function, TIMES
minimizes its negative, which then has the dimension of a cost. The
portion of that cost representing the negative of the consumer surplus
is akin to a *welfare loss.*

![](media/image14.wmf)*Figure 4.1. Step-wise constant approximation of
the non-linear terms in the objective function*

### Calibration of the demand functions

Besides selecting elasticities for the various demand categories, the
user must evaluate each constant *K~i~(t)*. To do so, we have seen that
one needs to know one point on each demand function in each time
period,*{ p^0^~i~(t),DM^0^~i~(t) }*. To determine such a point, we
perform a single preliminary run of the inelastic TIMES model (with
exogenous *DM^0^~i~(t)*), and use the resulting shadow prices
*p^0^~i~(t)* for all demand constraints, in all time periods for each
region.

### Computational considerations

Each demand segment that is elastic to its own price requires the
definition of as many variables as there are steps in the discrete
representation of the demand curve (both upward and down if desired),
for each period and region. Each such variable has an upper bound, but
is otherwise involved in no new constraint. Therefore, the linear
program is augmented by a number of variables, but does not have more
constraints than the initial inelastic LP (with the exception of the
upper bounds). It is well known that with modern LP codes the number of
variables has little or no impact on computational time in Linear
Programming, whether the variables are upper bounded or not. Therefore,
the inclusion in TIMES of elastic demands has a very minor impact on
computational time or on the tractability of the resulting LP. This is
an important observation in view of the very large LP's that result from
representing multi-regional and global models in TIMES.

### Interpreting TIMES costs, surplus, and prices

It is important to note that, instead of maximizing the net total
surplus, TIMES minimizes its negative (plus a constant), obtained by
changing the signs in expression (4-5). For this and other reasons, it
is inappropriate to pay too much attention to the meaning of the
*absolute* objective function values. Rather, examining the difference
between the objective function values of two scenarios is a far more
useful exercise. That difference is of course, the negative of the
difference between the net total surpluses of the two scenario runs.

Note again that the popular interpretation of shadow prices as the
*marginal costs* of model constraints is inaccurate. Rather, the shadow
price of a constraint is, by definition, the incremental value of the
objective function per unit of that constraint's right hand side (RHS).
The interpretation is that of an amount of *surplus loss* per unit of
the constraint's RHS. The difference is subtle but nevertheless
important. For instance, the shadow price of the electricity balance
constraint is not necessarily the marginal cost of producing
electricity. Indeed, when the RHS of the balanced constraint is
increased by one unit, one of two things may occur: either the system
*produces* one more unit of electricity, or else the system *consumes*
one unit less of electricity (perhaps by choosing more efficient end-use
devices or by reducing an electricity-intensive energy service, etc.) It
is therefore correct to speak of shadow prices as the marginal *system
value* of a resource, rather than the marginal *cost* of procuring that
resource.

#  Core TIMES Model: A simplified description of the Optimization Program (variables, objective, constraints)

This chapter contains a simplified formulation of the core TIMES Linear
Program.

Mathematically, a TIMES instance is a Linear Program, as was mentioned
in the previous chapter. A Linear Program (LP for short) consists in the
minimization or maximization of an *objective function* (defined as a
linear mathematical expression of *decision variables)*, subject to
linear *constraints,* also called *equations*[^26].

Very large instances of Linear Programs involving sometimes millions of
constraints and variables may be formulated using modern modeling
languages such as GAMS (<http://www.gams.com/help/index.jsp>), and
solved via powerful Linear Programming *optimizers*[^27]. The Linear
Program described in this chapter is much simplified, since it ignores
many exceptions and complexities that are not essential to a basic
understanding of the principles of the model. Chapter 14 gives
additional details on general Linear Programming concepts. The full
details of the parameters, variables, objective function, and
constraints of TIMES are given in Part II of this documentation
(sections 3, 5, and 6).

A linear optimization problem formulation consists of three types of
entities:

-   *the decision variables:* i.e. the unknowns, or endogenous
    quantities, to be determined by the optimization;

-   *the objective function*: expressing the criterion to be minimized
    or maximized; and;

-   *the constraints*: equations or inequalities involving the decision
    variables that must be satisfied by the optimal solution.

## Indices

The model data structures (sets and parameters), variables and equations
use the following indices:

***r:*** indicates the region

***t or v:*** time period; ***t*** corresponds to the current period,
and ***v*** is used to indicate the

> vintage year of an investment. When a process is not vintaged then
> ***v*** = ***t***.

***p:*** process (technology)

***s:*** time-slice; this index is relevant only for user-designated
commodities and

> processes that are tracked at finer than annual level (e.g.
> electricity, low-
>
> temperature heat, and perhaps natural gas, etc.). Time-slice defaults
> to "ANNUAL", indicating that a commodity is tracked only annually.

***c:*** commodity (energy, material, emission, demand).

## Decision variables

The decision variables represent the *choices* to be made by the model,
i.e. the *unknowns*. All TIMES variables are prefixed with the three
letters VAR followed by an underscore.

**Important remark**: There are two possible choices concerning the very
*meaning* of some decision variables, namely those variables that
represent yearly flows or process activities. In the original TIMES
formulation, the activity of a process during some period ***t*** is
considered to be constant in all years constituting the period. This is
illustrated in panel M.a of Figure 5.1).In the alternative option the
activity variable is considered to represent the value *in a milestone
year* of each period, and the values at all other years is linearly
interpolated between the consecutive milestone year values, as
illustrated in panel M.b). A milestone year is chosen close to the
middle of a period. This second option is similar to that of the EFOM
and the MESSAGE models. The user is free to choose either option. The
constraints and objective function presented below apply to the first
option (constant value of activity variables within a period).
Appropriate changes in constraints and objective function are made for
the alternative option, as explained in section 5.5, and more completely
in Part II, section 6.

The main kinds of decision variables in a TIMES model are:

***VAR_NCAP(r,v,p)*:** new capacity addition (investment) for technology
***p***, in period ***v*** and region ***r***. For all technologies the
***v*** value corresponds to the vintage of the process*,* i.e. year in
which it is invested in. For vintaged technologies (declared as such by
the user) the vintage (***v*)** information is reflected in other
process variables, discussed below. Typical units are PJ/year for most
energy technologies, Million tonnes per year (for steel, aluminum, and
paper industries), Billion vehicle-kilometers per year (B-vkm/year) or
million cars for road vehicles, and GW for electricity equipment
(1GW=31.536 PJ/year), etc.

![](media/image15.wmf){width="6.0in" height="4.498988407699038in"}

*Figure 5.1.Process activity in the original TIMES formulation (top) and
Linear variant (bottom)*

***VAR_RCAP(r,v,t,p):*** Amount of capacity that is newly retired at
period ***t***. The new retirements will reduce the available capacity
of vintage ***v*** in period ***t*** and in all successive periods
***t~i~\> t*** by the value of the variable. This new feature was not
available in early versions of TIMES. Note carefully that the feature
must be activated by a special switch in order to become effective. Note
also that additional a new advanced feature allows the user to specify
that capacity retirement may only occur in lump amounts that are either
equal to the entire remaining capacity or equal to a multiple of some
user defined block. Consult the separate technical note *TIMES Early
Retirement of Capacity* for details.

***VAR_DRCAP(r,v,t,p,j):*** Binary variables used in formulating the
special early retirement equations. Two variables may be defined, one
when retirement must be for the entire remaining capacity **(j=1**),
another when retirement must be a multiple of some block defined by the
user via parameter RCAP_BLK **(j=2**).

***VAR_SCAP(r,v,t,p):***Total amount of capacity that has been retired
at period ***t*** and periods preceding ***t*** (see above
***VAR_RCAP***paragraph).

***CAP(r,v,t,p):*** installed capacity of process ***p***, in region
***r*** and period ***t,*** optionally with vintage ***v.*** It
represents the total capacity available at period ***t***, considering
the residual capacity at the beginning of the modeling horizon and
adding to it new investments made prior to and including period ***t***
that have not reached their technical lifetime, and subtracting retired
capacity. Typical units: same as investments. The ***CAP*** quantity,
although convenient for formulation and reporting purposes, is in fact
*not explicitly defined in the model*, but is derived from the
***VAR_NCAP*** variables and from data on past investments, process
lifetimes, and any retirements.

***VAR_CAP(r,t,p):*** total installed capacity of technology ***p***, in
region ***r*** andperiod ***t***, all vintages together. The
***VAR_CAP*** variables are only defined when some bounds or
user-constraints are specified for them. They do not enter any other
equation.

[Remark]{.underline}: The lumpy investment option. There is a TIMES
feature that allows the user to impose that new additions to capacity
may only be done in predefined blocks. This feature may be useful for
technologies that are implementable only in discrete sizes such as a
nuclear plant, or a large hydroelectric project. The user should however
be aware that using this option voids some of the economic properties of
the equilibrium. This feature is described in Chapter 10 of this part of
the documentation.

***VAR_ACT(r,v,t,p,s):*** activity level of technology ***p***, in
region ***r*** and period ***t*** (optionally vintage ***v*** and
time-slice ***s***)***.*** Typical units: PJ for all energy
technologies. The ***s*** index is relevant only for processes that
produce or consume commodities specifically declared as time-sliced.
Moreover, it is the process that determines which time slices prevail.
By default, only annual activity is tracked.

***VAR_FLO(r,v,t,p,c,s):*** the quantity of commodity ***c*** consumed
or produced by process ***p***, in region ***r*** and period ***t***
(optionally with vintage ***v*** and time-slice ***s***). Typical units:
PJ for all energy technologies. The ***VAR_FLO*** variables confer
considerable flexibility to the processes modeled in TIMES, as they
allow the user to define flexible processes for which input and/or
output flows are not rigidly linked to the process activity.

***VAR_SIN(r,v,t,p,c,s)/VAR_SOUT(r,v,t,p,c,s):*** the quantity of
commodity ***c*** stored or discharged by storage process ***p,*** in
time-slice ***s***, period ***t*** (optionally with vintage ***v)***,
and region ***r***.

***VAR_IRE(r,v,t,p,c,s,exp) and VAR_IRE(r,v,t,p,c,s,imp)***[^28]***:***
quantity of commodity ***c*** (PJ per year) sold (***exp***) or
purchased (***imp***) by region ***r*** through export (resp. import)
process ***p*** in period ***t***(optionally in time-slice ***s***).
Note that the topology defined for the exchange process ***p***
specifies the traded commodity ***c***, the region ***r***, and the
regions ***r'*** with which region ***r*** is trading commodity ***c***.
In the case of bi-lateral trading, if it is desired that region ***r***
should trade with several other regions, each such trade requires the
definition of a separate bi-lateral exchange process. Note that it is
also possible to define multi-lateral trading relationships between
region ***r*** and several other regions ***r'*** by defining one of the
regions as the common market for trade in commodity ***c***. In this
case, the commodity is 'put on the market' and may be bought by any
other region participating in the market. This approach is convenient
for global commodities such as emission permits or crude oil. Finally,
exogenous trading may also be modeled by specifying the ***r'*** region
as an external region. Exogenous trading is required for models that are
not global, since exchanges with non-modeled regions cannot be
considered endogenous.

***VAR_DEM(r,t,d):*** demand for end-use energy service ***d*** in
region ***r*** and period ***t.*** It is a true variable, even though in
the reference scenario, this variable is fixed by the user. In alternate
scenarios however, ***VAR_DEM(r,t,d)*** may differ from the reference
case demand due to the responsiveness of demands to their own prices
(based on each service demand's own-price elasticity). Note that in this
simplified formulation, we do not show the variables used to decompose
***DEM(r,t,d)*** into a sum of step-wise quantities, as was presented in
chapter 4.

***Other variables:*** Several options that have been added to TIMES
over the successive versions require the definition of additional
variables. They are alluded to in the sections describing the new
options, and described more precisely in Part II, and in additional
technical notes. Also, TIMES has a number of commodity related variables
that are not strictly needed but are convenient for reporting purposes
and/or for applying certain bounds to them. Examples of such variables
are: the total amount produced of a commodity (***VAR_COMPRD***), or the
total amount consumed of a commodity (***VAR_COMCON***).

**[Important remark]{.underline}**: It is useful to know that many
variables (for instance the above two accounting variables, but also the
flow variables described earlier) add only a moderate computational
burden to the optimization process, thanks to the use of a *reduction
algorithm* to detect and eliminate redundant variables and constraints
before solving the LP. These variables and constraints are later
reinstated in the solution file for reporting purposes.

## TIMES objective function: discounted total system cost

### The costs accounted for in the objective function

The Surplus Maximization objective is first transformed into an
equivalent Cost Minimization objective by taking the negative of the
surplus, and calling this value the *total system cost*. This practice
is in part inspired from historical custom from the days of the fixed
demand MARKAL model. The TIMES objective is therefore to minimize the
total \'cost\' of the system, properly augmented by the 'cost' of lost
demand. All cost elements are appropriately discounted to a
user-selected year.

In TIMES, the cost elements are defined at a finer level than the
period. While the TIMES constraints and variables are linked to a
*period*, the components of the system cost are expressed for each
*year* of the horizon (and even for some years outside the horizon).
This choice is meant to provide a smoother, more realistic rendition of
the stream of cost payments in the energy system, as discussed below.
Each year, the total cost includes the following elements:

-   *Capital Costs* incurred for *investing* into and/or *dismantling*
    processes*.*

-   Fixed and variable annual *Operation and Maintenance (O&M) Costs,*
    and other annual costs occurring during the dismantling of
    technologies.

-   Costs incurred for *exogenous imports* and for domestic resource
    *extraction* and *production*. An exogenous import is one that
    imported from a non-specified entity, i.e. not from another modeled
    region. Exogenous imports are not relevant in global TIMES
    instances.

-   Revenues from exogenous *export.* An exogenous export is one that is
    exported to a non-specified entity, i.e. not to another modeled
    region. Exogenous exports are irrelevant in global TIMES instances.
    Exogenous export earnings are revenues and appear with a negative
    sign in the cost expressions.

-   *Delivery* costs for commodities consumed by the processes. These
    costs are attached to commodity flows.

-   *Taxes* and *subsidies* associated with commodity flows and process
    activities or investments. A tax is not a cost *per se*. However,
    since the tax is intended to influence the optimization, it is
    considered as an integral part of the objective function. It is
    however reported separately from regular costs. Similarly for
    subsidies.

-   *Revenues from recuperation of embedded commodities,* accrued when a
    process's dismantling releases some valuable commodities.

-   *Damage costs* (if defined) due to emissions of certain pollutants.
    Several assumptions are made: the damage costs in region ***r***
    result from emissions in ***r*** and possibly in other regions;
    damage cost is imputed to the emitting region (polluter pays);
    emissions in period ***t*** entail damages in period ***t*** only;
    the damage cost from several types of emission is assumed to be the
    sum of the costs from each emission type (no cross-effect); and the
    damage function linking cost DAM to emissions EM is a power function
    of the form:

$$DAM(EM) = MC_{0} \cdot \frac{EM^{\beta + 1}}{(\beta + 1) \cdot EM_{0}^{\beta}}$$

> Where β is non-negative (i.e. marginal damage costs are non
> decreasing). Hence, the damage cost function is linear (β=0) or non
> linear but convex (β \>0). Therefore, the same linearization procedure
> that was used for the surplus may be applied here in order to
> linearize the damage cost[^29]. Appendix B of Part II and Technical
> note \"TIMES Damage\", explain how to declare the various parameters
> required to define the damage functions, to specify the linearization
> parameters, and to define the switches used to control the
> optimization. It should be noted that global emissions such as GHG\'s
> should not be treated via this feature but rather should make use of
> the Climate Module option described in chapter 7.

-   ***Salvage value*** of processes and embedded commodities at the end
    of the planning horizon. This revenue appears with a negative sign
    in the cost expressions. It should also be stressed that the
    calculation of the salvage value at the end of the planning horizon
    is very complex and that the original TIMES expressions accounting
    for it contained some biases (over- or under-estimations of the
    salvage values in some cases). These biases have been corrected in
    the present version of TIMES as explained in sections 5.3.4 and 5.5.

-   *Welfare loss* resulting from reduced end-use demands. Chapter 4has
    presented the mathematical derivation of this quantity.

### Cash flow tracking

As already mentioned, in TIMES, special care is taken to precisely track
the cash flows related to process investments and dismantling in each
year of the horizon. Such tracking is made complex by several factors:

-   First, TIMES recognizes that there may be a lead-time (ILED) between
    the beginning and the end of the construction of some large
    processes, thus spreading the investment installments over several
    years. A recent TIMES feature allows the definition of a negative
    lead-time, with the meaning that the construction of the technology
    starts before the year the investment decision is made (this is
    useful for properly accounting for interest during construction, and
    is especially needed when using the time-stepped version of TIMES
    described in chapter 9.)

-   Second, TIMES also recognizes that for some other processes (e.g.
    new cars), the investment in new capacity occurs *progressivel*y
    over the years constituting the time period (whose length is denoted
    by D(t)), rather than in one lumped amount.

-   Third, there is the possibility that a certain investment decision
    made at period ***t*** will have to be repeated more than once
    during that same period. (This will occur if the period is long
    compared to the process technical life.)

-   Fourth, TIMES recognizes that there may be dismantling capital costs
    at the end-of-life of some processes (e.g. a nuclear plant), and
    that these costs, while attached to the investment variable indexed
    by period ***t***, are actually incurred much later.

-   Finally, TIMES permits the payment of any capital cost to be spread
    over an *economic life (ELIFE)* that is different from the
    *technical life (TLIFE)* of the process. Furthermore it may be
    annualized at a different rate than the overall discount rate.

To illustrate the above complexities, we present a diagram taken from
Part II that pictures the yearly investments and yearly outlays of
capital in one particular instance where there is no lead time and no
dismantling of the technology, and the technical life of the technology
does not exceed the period length. There are 4 distinct such instances,
discussed in detail in section 6.2 of Part II.

![](media/image16.emf){width="5.973185695538057in"
height="3.891053149606299in"}

*Figure 5.2. Illustration of yearly investments and payments for one of
four investment tracking cases*

### Aggregating the various costs

The above considerations, while adding precision and realism to the cost
profile, also introduce complex mathematical expressions into the
objective function. In this simplified formulation, we do not provide
much detail on these complex expressions, which are fully described in
section 6.2 of Part II. We limit our description to giving general
indications on the cost elements comprising the objective function, as
follows:

-   The capital costs (investment and dismantling) are first transformed
    into streams of annual payments, computed for each year of the
    horizon (and beyond, in the case of dismantling costs and recycling
    revenues), along the lines presented above.

-   A *salvage value* of all investments still active at the end of the
    horizon (EOH) is calculated as a lump sum revenue which is
    subtracted from the other costs and assumed to be accrued in the
    (single) year following the EOH.[^30]It is then discounted to the
    user selected reference year.

-   The other costs listed above, which are all annual costs, are added
    to the annualized capital cost payments, to form the ***ANNCOST***
    quantity below.

TIMES then computes for each region a total net present value of the
stream of annual costs, discounted to a user selected reference year.
These regional discounted costs are then aggregated into a single total
cost, which constitutes the objective function to be minimized by the
model in its equilibrium computation.

$$NPV = \sum_{r = 1}^{R}{}\sum_{y \in YEARS}^{}{(1 + d_{r,y})^{REFYR - y} \bullet ANNCOST(r,y)}$$

> where:
>
> ***NPV*** is the net present value of the total cost for all regions
> (the TIMES objective function);
>
> ***ANNCOST(r,y)*** is the total annual cost in region ***r*** and year
> ***y***;
>
> ***d~r,y\ ~***is the general discount rate;
>
> ***REFYR*** is the reference year for discounting;
>
> ***YEARS*** is the set of years for which there are costs, including
> all years in the horizon, plus past years (before the initial period)
> if costs have been defined for past investments, plus a number of
> years after EOH where some investment and dismantling costs are still
> being incurred, as well as the Salvage Value; and
>
> ***R*** is the set of regions in the area of study.

As already mentioned, the exact computation of ***ANNCOST*** is quite
complex and is postponed until section 6.2 of PART II

### Variants for the objective function

There are some cases where the standard formulation described above
leads to small distortions in the cost accounting between
capacity-related costs and the corresponding activity-related costs.
This occurs even without discounting but may be increased by
discounting. These distortions may occur at the end of the model
horizon, either due to excessive or deficient salvage value.

In addition to these cost accounting problems at the end of horizon, the
investment spreads used in the standard formulation can also lead to
other cost distortions, regardless of discounting. In very long periods,
the investment spreads are divided into D~t~ successive steps, each
amounting to 1/D~t~ of the total capacity to be invested in the period.
Recall that the full capacity must be in place by the milestone year, in
order to allow activity to be constant over the period. For example, if
the period length D~t~ is 20 years, the investments start already 19
years before the milestone year, and can thus start *even before the
previous milestone year*. *If the investment costs are changing over
time, it is clear that in such cases the costs will not be accounted in
a realistic way, because the investment cost data is taken from the
start year of each investment step.*

Similarly, in short periods the investment costs are spread over only a
few years, and if the previous period is much longer, this can leave a
considerable gap in the investment years between successive periods.
Here again, if the investment costs are changing over time, this would
lead to a distortion in the cost accounting.

Unfortunately, it is a well-known fact that the original choice of
defining milestone years at or near the middle of each period limits the
choice of milestone years, and furthermore tends to induce periods that
may be very unequal in length, thus exacerbating the anomalies mentioned
above. Such variability in period length can increase the cost
distortions under discounting due to the larger differences in the
timing of the available capacity (as defined by the investments) and the
assumed constant activity levels in each period in the original
definition of TIMES variables.

These were remedied by making changes in parts of the **OBJ** cost
representation. Four options are now available, three of which apply to
the original definition of TIMES variables, the fourth one applying to
the alternate definition of TIMES variables. The fourth option (named
**LIN**) is discussed separately in section 5.5, since it concerns not
only the objective function but also several constraints.

The three options are as follows:

-   The original OBJ with minor changes made to it, activated via the
    **OBLONG** switch.

-   The modified objective function (**MOD**). The **MOD** formulation
    adds only a few modifications to the standard formulation:

```{=html}
<!-- -->
```
-   The model periods are defined in a different way; and

-   The investment spreads in the investment Cases 1a and 1b (see
    section 6.2 of Part II for a list of all cases) are defined slightly
    differently.

```{=html}
<!-- -->
```
-   The **ALT** formulation includes all the modifications made in the
    MOD formulation. In addition, it includes the following further
    modifications that eliminate basically all of the remaining problems
    in the standard formulation:

```{=html}
<!-- -->
```
-   The investment spreads in the investment Case 1b are defined
    slightly differently;

-   The capacity transfer coefficients for newly installed capacities
    are defined slightly differently, so that the effective lifetime of
    technologies is calculated taking into account discounting;

-   Variable costs are adjusted to be in sync with the available
    capacity.

It has been observed that these three options yield results that have
practically the same degree of accuracy and reliability. There is
however an advantage to the MOD and ALT options, as the milestone years
need no longer be at the middle of a period.

Additional details and comments are provided on all three options in
technical note \"TIMES Objective Variants\"\
\
[Conclusion on the variants]{.underline}: The multiplicity of options
may confuse the modeler. Extensive experience with their use has shown
that the distortions discussed above remain quite small. In practice,
old TIMES users seem to stick to the classical OBJ with the OBLONG
switch. And, as mentioned above, using MOD allows the further
flexibility of freely choosing milestone years. Finally, using the LIN
option (described in section 5.5) is a more serious decision, since it
implies a different meaning for the TIMES variables; some modelers are
more comfortable with this choice, which has also implications for the
reporting of results.

## Constraints

While minimizing total discounted cost, the TIMES model must satisfy a
large number of constraints (the so-called *equations* of the model)
which express the physical and logical relationships that must be
satisfied in order to properly depict the associated energy system.
TIMES constraints are of several kinds. Here we list and briefly discuss
the main types of constraints. A full, mathematically more precise
description is given in Part II. If any constraint is not satisfied, the
model is said to be *infeasible*, a condition caused by a data error or
an over-specification of some requirement.

In the descriptions of the equations that follow, the equation and
variable names (and their indexes) are in ***bold italic*** type, and
the parameters (and their indexes), corresponding to the input data, are
in regular *italic* typeset. Furthermore, some parameter indexes have
been omitted in order to provide a streamlined presentation.

### Capacity transfer (conservation of investments)

Investing in a particular technology increases its installed capacity
for the duration of the physical life of the technology. At the end of
that life, the total capacity for this technology is decreased by the
same amount. When computing the available capacity in some time period,
the model takes into account the capacity resulting from all investments
up to that period, some of which may have been made prior to the initial
period but are still in operating condition (embodied by the residual
capacity of the technology), and others that have been decided by the
model at, or after, the initial period, up to and including the period
in question.

The total available capacity for each technology *p,* in region *r*, in
period *t* (all vintages),is equal to the sum of investments made by the
model in past and current periods, and whose physical life has not yet
ended, plus capacity in place prior to the modeling horizon that is
still available. The exact formulation of this constraint is made quite
complex by the fact that TIMES accepts variable time periods, and
therefore the end of life of an investment may well fall in the middle
of a future time period. We ignore here these complexities and provide a
streamlined version of this constraint. Full details are shown in
section 6.3.18 of Part II.

#### **EQ_CPT(r,t,p)** - Capacity transfer {#eq_cptrtp---capacity-transfer .unnumbered}

> ***VAR_CAPT(r,t,p)*** = ***Sum**{over all periods t' preceding or
> equal to t such that* *t-t'\<LIFE(r,t',p) of **VAR_NCAP(r,t',p)**}*
> **+** *RESID(r,t,p)* **(5-1)**
>
> where *RESID(r,t,p)* is the (exogenously provided) capacity of
> technology *p* due to investments that were made prior to the initial
> model period and still exist in region *r* at time *t*.

### Definition of process activity variables

Since TIMES recognizes activity variables as well as flow variables, it
is necessary to relate these two types of variables. This is done by
introducing a constraint that equates an overall activity variable,
***VAR_ACT(r,v,t,p,s)***, with the appropriate set of flow variables,
***VAR_FLO(r,v,t,p,c,s)***, properly weighted. This is accomplished by
first identifying the group of commodities that defines the activity
(and thereby the capacity as well) of the process. In a simple process,
one consuming a single commodity and producing a single commodity, the
modeler simply chooses one of these two flows to define the activity,
and thereby the process normalization (input or output). In more complex
processes, with several commodities (perhaps of different types) as
inputs and/or outputs, the definition of the activity variable requires
first to choose the *primary commodity group (pcg)* that will serve as
the activity-defining group. For instance, the *pcg* may be the group of
energy carriers, or the group of materials of a given type, or the group
of GHG emissions, etc. The modeler then identifies whether the activity
is defined via inputs or via outputs that belong to the selected *pcg*.
Conceptually, this leads to the following relationship:

***EQ_ACTFLO(r,v,t,p,s)** --* Activity definition

***VAR_ACT(r,v,t,p,s)*** = **SUM{***c in pcg of
**VAR***\_***FLO(r,v,t,p,c,s) /** ACTFLO(r,v p,c)***}**

**(5-2)**

> where *ACTFLO(r,v,p,c)* is a conversion factor (often equal to 1) from
> the activity of the process to the flow of a particular commodity.

### Use of capacity

In each time period the model may use some or all of the installed
capacity according to the Availability Factor (AF) of that technology.
Note that the model may decide to use *less* than the available capacity
during certain time-slices, or even throughout one or more whole
periods, if such a decision contributes to minimizing the overall cost.
Optionally, there is a provision for the modeler to force specific
technologies to use their capacity to their full potential.

For each technology *p*, period *t*, vintage *v*, region *r*, and
time-slice *s*, the activity of the technology may not exceed its
available capacity, as specified by a user defined availability factor.

#### **EQ_CAPACT (r,v,t,p,s)** - Use of capacity {#eq_capact-rvtps---use-of-capacity .unnumbered}

***VAR_ACT (r,v,t,p,s) ≤ or =***

*AF(r,v,t,p,s)\* PRC_CAPACT(r,p))\*FR(r,s**)\*VAR_CAP(r,v,t,p)***

**(5-3)**

Here *PRC_CAPACT(r,p)* is the conversion factor between units of
capacity and activity (often equal to 1, except for power plants). The
*FR(r,s)*parameter is equal to the (fractional) duration of time-slice
s. The availability factor *AF* also serves to indicate the nature of
the constraint as an inequality or an equality. In the latter case the
capacity is forced to be fully utilized. Note that the
***CAP(r,v,t,p)***\"variable\" is not explicitly defined in TIMES.
Instead it is replaced in (5-3) by a fraction (less than or equal to 1)
of the investment variable ***VAR_NCAP(r,v,p)***[^31] sum of past
investments that are still operating, as in equation (5-1).

***[Example]{.underline}*:** *a coal fired power plant's activity in any
time-slice is bounded above by 80% of its capacity, i.e. **VAR**\_**ACT
(r,v,t,p,s) ≤**0.8\*31.536 **\* CAP(r,v,t,p),** where PRC_CAPACT(r,p) =
31.536 is the conversion factor between the units of the capacity
variable (GW) and the activity-based capacity unit (PJ/a) The
activity-based capacity unit is obtained from the activity unit(PJ) by
division by a denominator of one year.*

The *s* index of the *AF* coefficient in equation (5-3) indicates that
the user may specify time-sliced dependency on the availability of the
installed capacity of some technologies, if desirable. This is
especially needed when the operation of the equipment depends on the
availability of a resource that cannot be stored, such as wind and sun,
or that can be only partially stored, such as water in a reservoir. In
other cases, the user may provide an *AF* factor that does not depend on
*s*, which is then applied to the entire year. The operation profile of
a technology within a year, if the technology has a sub-annual process
resolution, is determined by the optimization routine. The number of
***EQ_CAPACT*** constraints is at least equal to the number of
time-slices in which the equipment operates. For technologies with only
an annual characterization the number of constraints is reduced to one
per period (where *s="ANNUAL"*).

### Commodity balance equation

In each time period, the production by a region plus imports from other
regions of each commodity must balance the amount consumed in the region
or exported to other regions. In TIMES, the sense of each balance
constraint (**≥** or **=**) is user controlled, via a special parameter
attached to each commodity. However, the constraint defaults to an
equality in the case of materials (i.e. the quantity produced and
imported is *exactly* equal to that consumed and exported), and to an
inequality in the case of energy carriers, emissions and demands (thus
allowing some surplus production). For those commodities for which
time-slices have been defined, the balance constraint must be satisfied
in each time-slice.

The balance constraint is very complex, due to the many terms involving
production or consumption of a commodity. We present a much simplified
version below, to simply indicate the basic meaning of this equation.

For each commodity ***c,*** time period ***t (***vintage ***v)***,
region ***r***, and time-slice ***s*** (if necessary or "ANNUAL" if
not), this constraint requires that the disposition of each commodity
balances its procurement. The disposition includes consumption in the
region plus exports; the procurement includes production in the region
plus imports.

#### EQ_COMBAL(r,t,c,s) - Commodity balance {#eq_combalrtcs---commodity-balance .unnumbered}

> ***\[ Sum** {over all **p,c ∈**TOP(r,p,c,"out" )of:*
> **\[*VAR*\_*FLO(r,v,t,p,c,s) +
> VAR_SOUT(r,v,t,p,c,s)\*****STG_EFF(r,v,p)***\] *} +***
>
> ***Sum** {over all **p,c ∈**RPC_IRE(r,p,c,"imp") of
> :**VAR_IRE(r,t,p,c,s,"imp")**}*+
>
> ***Sum** {over all **p** of:
> Release(r,t,p,c)\***VAR_NCAP(r,t,p,c)**}**\] \*** COM_IE(r,t,c,s)*
>
> ***≥ or =* (5-4)**
>
> ***Sum** {over all **p,c ∈ TOP(r,p,c,"in")** of:
> **VAR_FLO(r,v,t,p,c,s) + VAR_SIN(r,v,t,p,c,s)**} **+ ***
>
> ***Sum {**over all **p,c∈ RPC_IRE(r,p,c,"exp")**} of:*
>
> ***VAR_IRE(r,t,p,c,s,'exp") +***
>
> ***Sum** {over all **p** of: Sink(r,t,p,c)\***VAR_NCAP(r,t,p,c)**} +*
>
> *FR(c,s) \***VAR_DEM(c,t)***
>
> where:
>
> The constraint is ≥ for energy forms and = for materials and emissions
> (unless these defaults are overridden by the user, see Part II).
>
> *TOP(r,p,c,"in/out")* identifies that there is an input/output flow of
> commodity c into/from process *p* in region *r;*
>
> *RPC_IRE(r,p,c,"imp/exp*") identifies that there is an import/export
> flow into/from region *r* of commodity *c* via process *p;*
>
> *STG_EFF(r,v,p) is the efficiency of storage process p;*
>
> *COM_IE(r,t,c) is the infrastructure efficiency of commodity c;*
>
> *Release(r,t,p,c)* is the amount of commodity ***c*** recuperated per
> unit of capacity of process ***p*** dismantled (useful to represent
> some materials or fuels that are recuperated while dismantling a
> facility);
>
> *Sink(r,t,p,c)* is the quantity of commodity ***c*** required per unit
> of new capacity of process ***p*** (useful to represent some materials
> or fuels consumed for the construction of a facility);
>
> *FR(s)* is the fraction of the year covered by time-slice ***s***
> (equal to 1 for non- time-sliced commodities)*.*

*[**Example**:]{.underline} Gasoline consumed by vehicles plus gasoline
exported to other regions must not exceed gasoline produced from
refineries plus gasoline imported from other regions.*

### Defining flow relationships in a process

A process with one or more (perhaps heterogeneous) commodity flows is
essentially defined by one or more input and output flow variables. In
the absence of relationships between these flows, the process would be
completely undetermined, i.e. its outputs would be independent from its
inputs. We therefore need one or more constraints stating in a most
general case that the ratio of the sum of some of its output flows to
the sum of some of its input flows is equal to a constant. In the case
of a single commodity in, and a single commodity out of a process, this
equation defines the traditional efficiency of the process. With several
commodities, this constraint may leave some freedom to individual output
(or input) flows, as long as their sum is in fixed proportion to the sum
of input (or output) flows. An important rule for this constraint is
that *each sum must be taken over commodities of the same type* (i.e. in
the same group, say: energy carriers, or emissions, etc.). In TIMES, for
each process the modeler identifies the input commodity group *cg*1*,*
and the output commodity group *cg*2, and chooses a value for the
efficiency ratio, named *FLO_FUNC(p,cg1,cg2).* The following equation
embodies this:

***EQ_PTRANS(r,v,t,p,cg1,cg2,s)** --*Efficiency definition

***SUM**{c in cg2 of : **VAR_FLO(r,v,t,p,c,s )**}=*

> *FLO_FUNC(r,v,cg1,cg2,s) \* **SUM**{c within cg1 of:
> COEFF(r,v,p,cg1,c,cg2,s)\***VAR_FLO(r,v,t,p,c,s)**}* **(5-5)**
>
> where *COEFF(r,v,p,cg1,c,cg2,s)* takes into account the harmonization
> of different time-slice resolution of the flow variables, which have
> been omitted here for simplicity, as well as commodity-dependent
> transformation efficiencies.

### Limiting flow shares in flexible processes

When either of the commodity groups*cg*1 or *cg*2 contains more than one
element, the previous constraint allows a lot of freedom on the values
of flows. The process is therefore quite flexible. The flow share
constraint is intended to limit the flexibility, by constraining the
share of each flow within its own group. For instance, a refinery output
might consist of three refined products: *c1*=light, *c2*=medium, and
*c3*=heavy distillate. If losses are 9% of the input, then the user must
specify *FLO_FUNC* = 0.91 to define the overall efficiency. The user may
then want to limit the flexibility of the slate of outputs by means of
three *FLO_SHAR(ci) coefficients, say 0.4, 0.5, 0.6,* resulting in three
flow share constraints as follows (ignoring some indices for clarity):

> *VAR_FLO(c1) ≤ 0.4\*\[VAR_FLO(c1) + VAR_FLO(c2) + VAR_FLO(c3)\],* so
> that *c*1 is at most 40% of the total output,
>
> *VAR_FLO(c2) ≤ 0.5\*\[VAR_FLO(c1) + VAR_FLO(c2) + VAR_FLO(c3)\],* so
> that *c*2 is at most 50% of the total output,
>
> *VAR_FLO(c3) ≤ 0.6\*\[VAR_FLO(c1) + VAR_FLO(c2) + VAR_FLO(c3)\],* so
> that *c*3 is at most 60% of the total output,

The general form of this constraint is:

*EQ_INSHR(c,cg,p,r,t,s)* and *EQ_OUTSHR(c,cg,p,r,t,s)*

***VAR_FLO(c)**≤**,≥**, =*

*FLO_SHAR(c) \* Sum {over all c' in cg of: **VAR_FLO(c')** }* **(5-6)**

The commodity group *cg* may be on the input or output side of the
process.

A recent modification of TIMES simplifies the above constraints by
allowing the use of the ***VAR_ACT*** variable instead of the sum of
***VAR_FLO*** variables in equation (5-6) or in similar ones. This
simplification is triggered when the user defines the new attribute
ACT_FLO, which is a coefficient linking a flow to the activity of a
process. Furthermore, commodity ***c*** appearing in left-hand-side of
the constraint may even be a flow that is not part of the ***cg***
group.

[Warning]{.underline}: It is quite possible (and regrettable) to over
specify flow related equations such as (5-6), especially when the
constraint is an equality. Such an over specification leads to an
infeasible LP. A new feature of TIMES consists in deleting some of the
flow constraints in order to re-establish feasibility, in which case a
warning message is issued.

### Peaking reserve constraint (time-sliced commodities only)

This constraint imposes that the total capacity of all processes
producing a commodity at each time period and in each region must exceed
the average demand in the time-slice where peaking occurs by a certain
percentage. This percentage is the Peak Reserve Factor,
*COM_PKRSV(r,t,c,s)*, and is chosen to insure against several
contingencies, such as: possible commodity shortfall due to uncertainty
regarding its supply (e.g. water availability in a reservoir); unplanned
equipment down time; and random peak demand that exceeds the average
demand during the time-slice when the peak occurs. This constraint is
therefore akin to a safety margin to protect against random events not
explicitly represented in the model. In a typical cold country the
peaking time-slice for electricity (or natural gas) will be Winter-Day,
and the total electric plant generating capacity (or gas supply plant)
must exceed the Winter-Day demand load by a certain percentage. In a
warm country the peaking time-slice may be Summer-Day for electricity
(due to heavy air conditioning demand). The user keeps full control
regarding which time-slices have a peaking equation.

For each time period ***t*** and for region ***r***, there must be
enough installed capacity to exceed the required capacity in the season
with largest demand for commodity ***c*** by a safety factor *E* called
the *peak reserve factor*.

#### **EQ_PEAK(r,t,c,s)** - Commodity peak requirement {#eq_peakrtcs---commodity-peak-requirement .unnumbered}

> ***Sum** {over all **p** producing **c with c=pcg** of
> PRC_CAPACT(r,p)* **\*** *Peak(r,v,p,c,s)* **\*** *FR(s)*
> **\**VAR_CAP(r,v,t,p) \* VAR_ACTFLO(r,v,p,c)*** *} **+ ***
>
> ***Sum** {over all **p** producing **c** with **c***≠***pcg** of*
>
> *NCAP_PKCNT(r,v,p,c,s)* **\**VAR_FLO(r,v,t,p,c,s****)}
> +**VAR_IRE(r,t,p,c,s,i**)*
>
> ***≥* (5-7)**
>
> *\[1+ COM_PKRSV(r,t,c,s)\]* \* *\[ **Sum** {over all **p consuming c**
> of **VAR_FLO(r,v,t,p,c,s) +VAR_IRE(r,t,p,c,s,e)**} \]*
>
> where:
>
> *COM_PKRSV(r,t,c,s)* is the region-specific reserve coefficient for
> commodity *c* in time-slice *s*, which allows for unexpected down time
> of equipment, for demand at peak, and for uncertain resource
> availability, and
>
> *NCAP_PKCNT(r,v,p,c,s)* specifies the fraction of technology *p*'s
> capacity in a region *r* for a period *t* and commodity *c*
> (electricity or heat only) that is allowed to contribute to the peak
> load in slice *s***;** many types of supply processes are predictably
> available during the peak and thus have a peak coefficient equal to 1,
> whereas others (such as wind turbines or solar plants in the case of
> electricity) are attributed a peak coefficient less than 1, since they
> are on average only fractionally available at peak (e.g., a wind
> turbine typically has a peak coefficient of .25 or .3, whereas a
> hydroelectric plant, a gas plant, or a nuclear plant typically has a
> peak coefficient equal to 1).
>
> For simplicity it has been assumed in (5-7) that the time-slice
> resolution of the peaking commodity and the time-slice resolution of
> the commodity flows (FLO, TRADE) are the same. In practice, this is
> not the case and additional conversion factors or summation operations
> are necessary to match different time-slice levels.
>
> *Remark*: to establish the peak capacity, two cases must be
> distinguished in constraint *EQ_PEAK*.
>
>   -- For production processes where the peaking commodity is the only
> commodity in the primary commodity group (denoted c=pcg), the capacity
> of the process may be assumed to contribute to the peak.\
>   -- For processes where the peaking commodity is not the only member
> of the pcg, there are several commodities included in the pcg.
> Therefore, the capacity as such cannot be used in the equation. In
> this case, the actual production is taken into account in the
> contribution to the peak, instead of the capacity. For example, in the
> case of CHP only the production of electricity contributes to the peak
> electricity supply, not the entire capacity of the plant, because the
> activity of the process consists of both electricity and heat
> generation in either fixed or flexible proportions, and, depending on
> the modeler\'s choice, the capacity may represent either the electric
> power of the turbine in condensing or back-pressure mode, or the sum
> of power and heat capacities in back-pressure mode. There is therefore
> a slight inconsistency between these two cases, since in the first
> case, a technology may contribute to the peak requirement without
> producing any energy, whereas this is impossible in the second case.

Note also that in the peak equation (5-7), it is assumed that imports of
the commodity are contributing to the peak of the importing region
(thus, exports are implicitly considered to be of the *firm power*
type).

### Constraints on commodities

In TIMES variables are optionally attached to various quantities related
to commodities, such as total quantity produced. Therefore it is quite
easy to put constraints on these quantities, by simply bounding the
commodity variables in each period. It is also possible to impose
cumulative bounds on commodities over more than one period, a
particularly useful feature for cumulatively bounding emissions or
modeling reserves of fossil fuels. By introducing suitable naming
conventions for emissions the user may constrain emissions from specific
sectors. Furthermore, the user may also impose global emission
constraints that apply to several regions taken together, by allowing
emissions to be traded across regions. Alternatively or concurrently a
tax or penalty may be applied to each produced (or consumed) unit of a
commodity (energy form, emission), via specific parameters.

A specific type of constraint may be defined to limit the share of
process (p) in the total production of commodity (c). The constraint
indicates that the flow of commodity (c) from/to process (p) is bounded
by a given fraction of the total production of commodity (c). In the
present implementation, the same given fraction is applied to all time­
slices.

### User constraints

In addition to the standard TIMES constraints discussed above, the user
may create a wide variety of so-called User Constraints (UC\'s), whose
coefficients follow certain rules. Thanks to recent enhancements of the
TIMES code, user defined constraints may involve virtually any TIMES
variable. For example, there may a user-defined constraint limiting
investment in new nuclear capacity (regardless of the type of reactor),
or dictating that a certain percentage of new electricity generation
capacity must be powered by a portfolio of renewable energy sources.
User constraints may be employed across time periods, for example to
model options for retrofitting existing processes or extending their
technical lives. A frequent use of UC\'s involves cumulative quantities
(over time) of commodities, flows, or process capacities or activities.
Recent TIMES code changes make the definition of the right-hand-sides of
such UC\'s fairly independent of the horizon chosen for the scenario,
and thus make it unnecessary to redefine the RHS\'s when the horizon is
changed.

In order to facilitate the creation of a new user constraint, TIMES
provides a *template* for indicating a) the set of variables involved in
the constraint, and b) the user-defined coefficients needed in the
constraint.

The details of how to build different types of UC are included in
section 6.4 of Part II of the documentation.

### Growth constraints

These are special cases of UC\'s that are frequently used to maintain
the growth (or the decay) of the capacity of a process within certain
bounds, thus avoiding excessive abrupt investment in new capacity. Such
bounding of the growth is often justified by the reality of real life
constraints on technological adoption and evolution. The user is however
advised to exert caution on the choice of the maximum rates of
technological change, the risk being to restrict it too much and thus
\"railroad\" the model.

Typically, a growth constraint is of the following generic form
(ignoring several indices for clarity:

$\mathbf{VAR}\_\mathbf{CAP}(\mathbf{t} + \mathbf{1}) \leq \left( \mathbf{1} + \mathbf{GROWTH}^{\mathbf{M}\left( \mathbf{t} + \mathbf{1} \right) - \mathbf{M}\left( \mathbf{t} \right)} \right) \times \mathbf{VAR}\_\mathbf{CAP}(\mathbf{t}) + \mathbf{K}$
(5-8)

The GROWTH coefficient is defined as a new attribute of the technology,
and represents the maximum annual growth allowed for the capacity. The
quantity M(t+1)-M(t) is the number of years between the milestones of
periods t and t+1. The constant K is useful whenever the technology has
no capacity initially, in order to allow capacity to build over time (if
K were absent and initial capacity is zero, the technology would never
acquire any capacity)

Note that the sign of the constraint may also be of the \"larger than or
equal to\" type to express a maximum rate of abandonment, in which case
the \"+\" sign is replaced by a \"--\" sign in the right-hand-side of
the constraint. Equality is also allowed, but must be used only
exceptionally in order to avoid railroading of the model.

### Early retirement of capacity

With this new TIMES feature the user may allow the model to retire some
technologies before the end of their technical lives. The retirement may
be continuous or discrete. In the former case, the model may retire any
amount of the remaining capacity (if any) at each period. In the latter
case, the retirement may be effected by the model either in a single
block (i.e. the remaining capacity is completely retired) or in
multiples of a user chosen block. Please refer to chapter 10 of this
document *The lumpy investment option*, for additional discussion of the
mathematical formulation of MIP problems.

This feature requires the definition of three new constraints, as listed
and briefly described in table 5.1, as well as the alteration of many
existing constraints and the objective function, as described in table
5.2 Part II and the special separate note *TIMES Early Retirement of
Capacity* provide additional detail.

The user is advised to use the discrete early retirement feature
sparingly, as it implies the use of mixed integer programming optimizer,
rather than the computationally much more efficient linear programming
optimizer. The user should also be aware that using the discrete option
voids some of the economic properties of the equilibrium, as discussed
in section 10.3.

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

*Table 5.1. The new constraints required to implement early retirement
of capacity*

+--------------+----------------------+-------------------------------+
| **Existing   | **Equation           | **Purpose of Modification**   |
| Equation**   | Description**        |                               |
+==============+======================+===============================+
| EQ_OBJFIX    | Fixed cost component | To credit back the fixed      |
|              | of objective         | costs of the capacity that is |
|              | function             | retired early                 |
+--------------+----------------------+-------------------------------+
| EQ_OBJVAR    | Variable cost        | To reflect the effect of      |
|              | component of         | capacity that is retired      |
|              | objective function   | early in the costs of         |
|              |                      | capacity-related flows        |
+--------------+----------------------+-------------------------------+
| EQ_OBJSALV   | Salvage cost         | To subtract the salvage value |
|              | component of         | (if any) of capacity that is  |
|              | objective function   | retired early                 |
+--------------+----------------------+-------------------------------+
| EQ           | Capacity transfer    | To reflect the effect of      |
| (**l**)\_CPT | equation             | capacity that is retired      |
|              |                      | early                         |
| for **l** =  |                      |                               |
| L, E, G      |                      |                               |
+--------------+----------------------+-------------------------------+
| EQ(**        | Capacity utilization | To reflect the effect of      |
| l**)\_CAPACT | equation             | capacity that is retired      |
|              |                      | early                         |
| for **l** =  |                      |                               |
| L, E, G      |                      |                               |
+--------------+----------------------+-------------------------------+
| EQ(**        | Commodity based      | To reflect the effect of      |
| l**)\_CAFLAC | availability         | capacity that is retired      |
|              | constraint           | early                         |
| for **l** =  |                      |                               |
| L, E         |                      |                               |
+--------------+----------------------+-------------------------------+
| EQ(**l       | Commodity balance    | To reflect the effect of      |
| **)\_COMBAL\ | equation             | capacity that is retired      |
| for **l** =  |                      | early in capacity-related     |
| G, E         |                      | flows                         |
+--------------+----------------------+-------------------------------+
| EQ_PEAK      | Commodity peaking    | To subtract the peak          |
|              | constraint           | contribution of capacity that |
|              |                      | is retired early              |
+--------------+----------------------+-------------------------------+
| EQ(*         | The FLO component of | To reflect the effect of      |
| *l**)\_UC\*\ | all user constraints | capacity that is retired      |
| for **l** =  |                      | early in capacity-related     |
| L, E, G      |                      | flows                         |
+--------------+----------------------+-------------------------------+
| EQ(**        | Market share of flow | To reflect the effect of      |
| l**)\_MRKCON | in the consumption   | capacity that is retired      |
|              | of a commodity       | early in capacity-related     |
| for **l** =  |                      | flows                         |
| L, E, G      |                      |                               |
+--------------+----------------------+-------------------------------+
| EQ(**        | Market share of flow | To reflect the effect of      |
| l**)\_MRKPRD | in the production of | capacity that is retired      |
|              | a commodity          | early in capacity-related     |
| for **l** =  |                      | flows                         |
| L, E, G      |                      |                               |
+--------------+----------------------+-------------------------------+

*Table 5.2. List of existing constraints that are affected by the early
retirement option.*

### Electricity grid modeling

The electricity sector plays a central role in any energy model, and
particularly so in TIMES. The electricity commodity has features that
present particular challenges for its representation, in that it is
difficult to store, and requires a network infrastructure to be
transported and delivered. The considerable development of new renewable
electricity generation technologies adds to the complexity, inasmuch as
the technical requirements of integrating interruptible generation
facilities (such as wind turbines and solar plants) to a set of
traditional plants, must be satisfied for the integration to be
feasible. Such considerations become even more relevant in large regions
or countries, where the distances between potential generation areas and
consumption areas are quite large.

Such considerations have led to the introduction of an optional grid
modeling feature into the TIMES model\'s equations. A grid consists in a
network of nodes linked by arcs (or branches). Each node may represent a
well-defined geographic area that is deemed distinct from other areas of
the region, either because of its generation potential (e.g. a windy
area suitable for wind farms) and/or because of a concentration of
points of consumption of electricity (e.g. a populated area separated
from other populated areas or from generation areas.)

The purpose of this section is to indicate the broad principles and
characteristics of the grid representation feature in TIMES. The modeler
wishing to implement the feature is urged to read to the detailed
Technical Note "TIMES Grid modeling feature", which contains the
complete mathematical derivations of the equations, and their
implementation in TIMES. What follows is a much streamlined version
outlining only the main approach and ignoring the many details of the
mathematical equations.

#### A much simplified sketch of the grid constraints

The traditional way to represent the nodes and arcs of a grid is shown
in figure 5.3, where each node is shown as a horizontal segment, and the
nodes are connected via bi-directional arcs.

![](media/image17.png){width="3.875in" height="2.220883639545057in"}

*Figure 5.3. Connection of a grid node with other nodes*

The basic energy conservation equation of a grid is as follows:

$G_{i} - L_{i} = \sum_{j = 1}^{M}P_{i,j}$*for each i=1,2,\...,M*

where:

> M = the number of nodes connected with node *i*
>
> *G~i~ =* active power injected into node *i* by generators
>
> *L~i~ =* active power withdrawn from node *i* by consumer loads
>
> *P~ij~ =* branch flow from node *i* to node *j*

As mentioned above, these constraints are then modified so as to include
important technical requirements on the electrical properties (reactance
and phase angle) of each line. Suffice it to say here that the resulting
new equations remain linear in the flow and other variables.

#### Integrating grid equations into TIMES

It should be clear that the variables *G~i~* and *L~i\ ~*must be tightly
related to the rest of the TIMES variables that concern the electricity
commodities. In fact, the modeler must first decide on an allocation of
the set of generation technologies into *M* subsets, each subset being
attached to a node of the grid. Similarly, the set of all technologies
that consume electricity must also be partitioned into *M* subsets, each
attached to a node. These two partitions are effected via new parameters
specifying the fractions of each generation type to be allocated to each
grid node, and similarly for the fractions of each technology consuming
electricity to be allocated to grid each node. This indeed amounts to a
partial regionalization of the model concerning the electricity sector.
Thus, variables *G~i~* and *L~i\ ~* are defined in relation to the
existing TIMES variables.

Of course, the introduction of the grid requires modifying the
electricity balance equations and peak equations, via the introduction
of the net total flow variables the set of grid nodes. The electricity
balance equations are modified for each time slice defined for
electricity.

Finally, additional a security constraint is added in the case of a
multi-regional model, expressing that the total net export or import of
electricity from region ***r*** does not exceed a certain (user-defined)
fraction of the capacity of the portion of the grid linking region
***r*** to other regions.

#### Costs

New costs attached to the grid are also modeled, and form a new
component of the objective function for the region. For this, a new cost
coefficient is defined and attached to each node of the grid. TIMES
multiplies this cost coefficient by the proper new grid variables and
discounts the expression in order to form the new OBJ component.

### Reporting \"constraints\"

These are not constraints proper but expressions representing certain
quantities useful for reporting, after the run is completed. They have
no impact on the optimization. We have already mentioned
***CAP(r,v,t,p)***, which represents the capacity of a process by
vintage.

One sophisticated expression reports the *levelized cost* (LC) of a
process. A process\'s LC is a life cycle quantity that aggregates all
costs attached to a process, whether explicit or implicit. It is a
useful quantity for ranking processes. However, such a ranking is
dependent upon a particular model run, and may vary from run to run.
This is so because several implicit costs attached to a process such as
the cost of fuels used or produced, and perhaps the cost of emissions,
are run dependent.

The general expression for the levelized cost of a process is as
follows:

$LEC = \frac{\sum_{t = 1}^{n}{\frac{IC_{t}}{(1 + r)^{t - 1}} + \frac{OC_{t} + VC_{t} + \sum_{i}^{}{FC_{i,t} + FD_{i,t}} + \sum_{j}^{}{ED_{j,t}}}{(1 + r)^{t - 0.5}} -}\frac{\sum_{k}^{}{BD_{k,t}}}{(1 + r)^{t - 0.5}}}{\sum_{t = 1}^{n}\frac{\sum_{m}^{}{MO_{m,t}}}{(1 + r)^{t - 0.5}}}$
(5-9)

where

-   *r* = discount rate (e.g. 5%)

-   *IC~t~* = investment expenditure in (the beginning of) year *t*

-   *OC~t~* = fixed operating expenditure in year *t*

-   *VC~t~* = variable operating expenditure in year *t*

-   *FC~it~* = fuel-specific operating expenditure for fuel *i* in year
    *t*

-   *FD~it~* = fuel-specific acquisition expenditure for fuel *i* in
    year *t*

-   *ED~jt~* = emission-specific allowance expenditure for emission *j*
    in year *t* (optional)

-   *BD~kt~* = revenues from commodity *k* produced by the process in
    year *t* (optional;)

-   *MO~mt~* = output of main product *m* in year *t*, i.e. a member of
    the *pcg*

Comments:

Each cost element listed above is obtained by multiplying a unit cost by
the value of the corresponding variable indicated in the run results.

The unit values of the first four costs are simply equal the process
input data, i.e. the unit investment cost, the fixed unit O&M cost, the
unit variable operating cost, and the unit delivery cost. The last three
costs are the shadow prices of the commodities concerned, endogenously
obtained as the dual solution of the current model run.

Note also that the user may choose to ignore the last two costs or to
include them. Furthermore, concerning the last cost (which is indeed a
revenue), the user may decide to ignore the revenue from the main
commodities produced by the process and retain only the revenues from
the by-products. The choice is specified via the parameter
RPT_OPT('NCAP','1'). Technical note \"Levelized costs-TIMES\" provides
details on the parameter values.

## The \'Linear\' variant of TIMES

This alternate TIMES formulation (called the LIN variant) assumes a
different meaning for the activity and flow variables of TIMES. More
precisely, instead of assuming that flows and activities are constant in
all years within the same period, the variant assumes that the flow and
activity variables apply to only one milestone year within each period.
The variables\' values at other years of a period are interpolated
between successive milestone years\' values. See section 5.2 for a
figure depicting the two alternate definitions.

Choosing the LIN formulation affects the variable costs in the objective
function as well as all dynamic constraints involving activities or
flows. Note also that the LIN variant avoids the cost distortions
mentioned in section 5.3.1.

Significant modifications in the LIN formulation concern the variable
cost accounting, since the latter are no longer constant in all years of
any given period, but evolve linearly between successive milestone
years. The objective function components for all variable costs have
been modified accordingly.

The following further modifications are done in the LIN formulation:

-   The cumulative constraints on commodity production (EQ(l)\_CUMNET
    and EQ(l)\_CUMPRD) are modified to include linear interpolation of
    the commodity variables involved;

-   The cumulative constraints on commodity and flow taxes and subsidies
    (EQ(l)\_CUMCST) are modified to include linear interpolation of the
    commodity and flow variables involved;

-   The dynamic equations of the Climate module are modified to include
    linear interpolation of the variables involved;

-   The inter-period storage equations are modified to include linear
    interpolation of the flow variables involved;

-   The cumulative user constraints for activities and flows are also
    modified in a similar manner.

-   Note that in the LIN formulation the activity of ***inter-period
    storage*** equations is measured at the milestone year (in the
    standard formulation it is measured at the end of each period). In
    addition, new EQ_STGIPS equations are added to ensure that the
    storage level remains non-negative at the end of each period.
    (Without these additional constraints, the linear interpolation of
    storage could lead to a negative storage level if the period
    contains more than a single year.)

# Parametric analysis with TIMES

Dealing with uncertainty in modeling is a complex endeavour that may be
accomplished via a number of (sometimes widely different) approaches. In
the case of TIMES, two different features are available: ***Stochastic
Programming*** (treated in chapter 8) and ***parametric analysis***,
also known as ***sensitivity analysis***, which is the subject of this
chapter. In sensitivity analysis, the values of some important exogenous
assumptions are varied, and a series of model runs is performed over a
discrete set of combinations of these assumptions. Sensitivity analysis
is often combined with ***tradeoff analysis***, where the tradeoff
relation between several objectives is analyzed.

The uncertain attributes are similar to the corresponding standard TIMES
attributes, but they may now have different values according to the
different ***states-of-the-world*** (SOW), just as in the case of
stochastic prog­ramming. The difference between the two approaches is
that sensitivity analysis solves a sequence of instances, each assuming
different values of the uncertain parameters, whereas stochastic
programming solves a single instance that encompasses all potential
values of the uncertain parameters simultaneously.

In TIMES, sensitivity analysis and tradeoff analysis facility are
implemented using the same setup and some of the attributes of the
stochastic mode of TIMES, since both approaches, although conceptually
different, use the same state of the world construct.

Here are a few possible set-ups for sensitivity and tradeoff analyses in
TIMES, all of which are supported by the model generator:

A.  Single phase sensitivity analysis over the set of SOWs. Each run
    corresponds to a set of values for the uncertain parameters. The
    runs are mutually independent. This is the most straightforward
    approach;

B.  Two-phase tradeoff analysis, where the model is first run using a
    user-defined objective function, and then the TIMES objective
    function is used in phase 2, while the solution from the first phase
    is used for defining additional constraints in a series of model
    runs in the second phase.

C.  Multiphase tradeoff analysis over N phases, which is a
    generalization of the two-phase case.

Analyzing tradeoffs between the standard objective function and some
other possible objectives (for which the market is not able to give a
price) was not possible in an effective way with earlier versions of
TIMES.

## Two-phase tradeoff analysis

In the ***first phase*** of the TIMES two-phase tradeoff analysis
facility, the objective function is user defined as a weighted sum of
any number of components, each component being a user constraint\'s
left-hand-side. All UC\'s must be of the global type, (i.e. aggregated
over regions and periods). Optionally, each of the component UCs may
also be constrained by upper/lower bounds. The components are defined by
the user, via the specification of non-zero weight coefficients for the
UC\'s to be included in the objective. The original objective function
(total discounted costs) is auto­matically pre-defined as a
non-constraining user constraint with the name '***OBJZ***', and can
therefore always be directly used as one of the component UCs, if
desired.

Consequently, the first phase can be considered as representing a
Utility Tradeoff Model, which can also be used as a stand-alone option.
If used in a stand-alone manner, it constitutes a case of
multi-criterion decision making (see e.g. Weistroffer, 2005). The
resulting objective function to be minimized can be written as follows:

$$\min obj1 = \sum_{uc \in UC\_ GLB}^{}{W(uc) \bullet LHS(uc)}$$

where:

*W(uc)* = weight of objective component *uc* in Phase 1

*LHS(uc)* = LHS expression of user constraint *uc* according to its
definition

*UC_GLB* = the set of all global UC constraints (including '***OBJZ***')

In the ***second phase*** of the TIMES two-phase tradeoff analysis
facility the objective function is always the ***original objective
function*** in TIMES, i.e. the total discounted system cost (this
ensures that the second phase solution produce an economically
meaningful set of values for the dual variables.)

In addition, in the second phase the user can specify bounds on
fractional deviations in the LHS values of any or all user constraints,
in compa­rison to the optimal LHS values obtained in the first phase.
Such deviation bounds can be set for both global and non-global
constraints, and for both non-constrai­ning and constrained UCs (however,
any original absolute bounds are overridden by the deviation bounds).
The ***objective function used in Phase 1*** is also available as an
additional pre-defined UC, named '***OBJ1***', so that one can set
either deviation bounds or absolute bounds on that as well, if desired.
In addition, both the total and regional original objective functions
can be referred to by using the pre­defined UC name '***OBJZ***' in the
deviation bound parameters.

The objective function to be minimized in the second phase, and the
addi­tional bounds on the LHS values of UCs, can be written as follows:

$${	\min objz = 	LHS('OBJZ')
}{\left. \ \begin{matrix}
LHS(uc) \leq (1 + maxdev(uc)) \bullet LHS^{*}(uc) \\
LHS(uc) \geq (1 - maxdev(uc)) \bullet LHS^{*}(uc)
\end{matrix} \right\}\begin{matrix}
\text{for each }uc\text{ for which } \\
maxdev(uc)\text{ has been specified}
\end{matrix}}$$

where:

> *LHS('OBJZ')* = the standard objective function (discounted total
> system costs)
>
> *LHS(uc)* = LHS expression of user constraint *uc* according to its
> definition
>
> *LHS\*(uc)* = optimal LHS value of user constraint *uc* in Phase 1
>
> *maxdev(uc)* = user-specified fraction defining the maximum
> proportional
>
> deviation in the value of LHS(uc) compared to the solution in Phase 1

Remarks:

1.  Use of the two-phase tradeoff analysis facility requires that a
    weight has been defined for at least one objective component in the
    first phase.

2.  If no deviation bounds are specified, the second phase will be
    omitted.

3.  Automatic discounting of any commodity or flow-based UC component is
    possible by using a new UC_ATTR option 'PERDISC' which could be
    applied e.g. to the user-defined objective components in Phase 1.

4.  The two-phase tradeoff analysis can be carried over a set of
    distinct cases, each identified by a unique SOW index.

## Multiphase tradeoff analysis

The multiphase tradeoff analysis is otherwise similar to the two-phase
analysis, but in this case the objective function can be defined in the
same way as in the Phase 1 described above also in all subsequent
phases. The different objective functions in each phase are
distinguished by using an additional phase index (the SOW index).
Deviation bounds can be specified in each phase, such that they will be
in force over all subsequent phases (any user constraints), or only in
some of the succeeding phases (any user constraints excluding OBJ1). The
deviation bounds defined on any of the user-defined objectives OBJ1 will
thus always be preserved over all subsequent phases.

**Remark**: Although the multiphase tradeoff analysis allows the use of
any user-defined objective functions in each phase, it is highly
recommended that the original objec­tive function be used in the last
phase, so that the economic meaning is maintained in the final solution.

The procedure was presented in a very general form, in order to let the
user exert her ingenuity at will. Typical simple examples of using the
feature may be useful.

[Example 1]{.underline}: trade-off between cost and risk.

First, a special UC (call it RISK) is defined that expresses a **global
risk** measure. The successive phases consist in minimizing the
following parameterized objective:

$$Min\ OBJZ + \ \alpha \bullet RISK$$

where α is a user chosen coefficient that may be varied within a range
to explore an entire trade-off curve such as illustrated in figure 6.1,
where the vertical axis represents the values of the cost objective
function, and the horizontal axis the risk measure.

![](media/image18.emf)

*Figure 6.1. Trade-off between Risk and Cost*

OBJZ\* is the lowest value for OBJZ, corresponding to a relatively large
value R~0~ for RISK, i.e. when α = 0. As α increases, RISK decreases and
OBJZ increases. In this example, 4 alternate values of α were chosen
until the value of OBJZ becomes very large, at point (R~4~,OBJZ~4~).
This would correspond to very large value for α, i.e. a point where RISK
is minimized.

An example of such an analysis is fully developed in Kanudia et al
(2013), where a risk index is constructed to capture an indicator of
energy security for the European Union. A complex (but linear) risk
measure was developed to evaluate the risk for a large number of
alternative channels of energy imports into the EU, and the trade-off
between risk and overall cost was explored.

[Example 2]{.underline}: exploring the opportunity cost of the nuclear
option

At phase 1, the original *OBJZ* is minimized with the habitual TIMES
constraints. This results in an optimal cost *OBJZ\*.* At phase 2, the
objective function is equal to the total nuclear capacity over the
entire horizon and over all regions, and a new constraint is added as
follows:

$$OBJZ\  \leq (1 + \alpha) \bullet {OBJZ}^{*}$$

The α parameter may be varied to explore the entire trade-off curve. A
last phase may also be added at the end, with OBJZ as objective
function, and a user selected value for the maximum level of nuclear
capacity.

# The TIMES Climate Module

This chapter provides a detailed description of the theoretical approach
taken to model changes in atmospheric greenhouse gas concentrations,
radiative forcing, and global mean temperatures in the TIMES Climate
Module. Appendix A of Part II contains a full description of the
implementation of the Climate Module in TIMES, including parameters,
variables, and equations, as represented in the TIMES code.

The Climate Module starts from global emissions of CO2, CH4, and N2O, as
generated by the TIMES global model, and proceeds to compute
successively:

-   the changes in CO2, CH4, and N2O concentrations via three separate
    sets of equations;

-   the total change (over pre-industrial times) in atmospheric
    radiative forcing resulting from the three gases plus an exogenously
    specified additional forcing resulting from other causes (other
    anthropogenic and/or natural causes, as defined by the user), and

-   the temperature changes (over pre-industrial times) in two
    reservoirs (surface and deep ocean).

The climate equations used to perform these calculations were adapted
from Nordhaus and Boyer (1999), who proposed a three reservoir model for
the CO2 cycle only[^32]. This leads to linear recursive equations for
calculating CO2 concentrations in each reservoir. The temperature
equations use a two-reservoir model leading also to linear equations.
The forcing equation is the one used in most climate models, and is
non-linear.

In TIMES, we have modeled separately the life cycles of two other GHG's
besides CO2, namely methane and nitrous oxide. These linear equations
give results that are good approximations of those obtained from more
complex climate models (Drouet et al., 2004; Nordhaus and Boyer, 1999).

The non-linear radiative forcing equation used in virtually all climate
models was replaced in TIMES by a linear approximation whose values
closely approach the exact ones as long as the useful range is carefully
selected. This was done in order to keep the entire model linear, and
therefore to allow the user to set constraints on forcing and on
temperature as well as on concentrations and on emissions.

The temperature equations have been kept as in Nordhaus and Boyer.

We now describe the mathematical equations used at each of the three
steps of the climate module.

## Concentrations (accumulation of CO2, CH4, N2O[^33])

a\) CO2 accumulation is represented as the linear three-reservoir model
below: the atmosphere, the quickly mixing upper ocean + biosphere, and
the deep ocean. CO2 flows in both directions between adjacent
reservoirs. The 3-reservoir model is represented by the following 3
equations when the step of the recursion is equal to one year:

M~atm~ (y) = E(y) + (1 -- φ~atm-up~) M~atm~ (y-1) +φ~up-atm~ M~up~ (y-1)
(7-1)

M~up~ (y) = (1 --φ~up-atm~ -- φ~up-lo~) M~up~ (y-1) + φ~atm-up~ M~atm~
(y-1) + φ~lo-up~ M~lo~ (y-1) (7-2)

M~lo~ (y) = (1-- φ~lo-up~) M~lo~ (y-1) + φ~up-lo~ M~up~ (y-1) (7-3)

with

-   M~atm~(y), M~up~(y), M~lo~(y): Concentration (expressed in mass
    > units) of CO~2~ in atmosphere, in a quickly mixing reservoir
    > representing the upper level of the ocean and the biosphere, and
    > in deep oceans (GtC), respectively, in year y (GtC)

-   E(y) = CO~2~ emissions in year y (GtC)

-   φ~ij~, transport rate from reservoir i to reservoir j (i, j = atm,
    > up, lo) from year y-1 to y

b\) CH4 accumulation is represented by a so-called single-box model in
which the atmospheric methane concentration obeys the following
equations assuming a constant annual decay rate of the anthropogenic
concentrations $\Phi_{CH4}$ (whereas the natural concentration is
assumed in equilibrium):

$$CH4_{atm}(y) = (1 - \Phi_{CH4}) \cdot CH4_{atm}(y - 1) + EA_{CH4}(y)(7 - 4)$$

$$CH4_{up}(y) = CH4_{up}(y - 1)(7 - 5)$$

${CH4}_{tot}(y) = {CH4}_{atm}(y) + {CH4}_{up}(y)$ (7 - 6)

where

-   *CH4~atm~ ,, CH4~up~ ,CH4~tot~, ,* and *EA~CH4~* are respectively:
    the anthropogenic atmospheric concentration, the natural atmospheric
    concentration[^34], the total atmospheric concentration (all three
    expressed in Mt), and the anthropogenic emission of CH4 (expressed
    in Mt/yr). The anthropogenic emissions *EA~CH4~* are generated
    within the model and enter the dynamic equation (7-4) in order to
    derive the anthropogenic concentration. Note that the natural
    concentration *CH4~up~*is constant at all times. (See initial values
    for these and other parameters in Part II, Appendix A.)

-   *CH4~tot\ ~*is then reported and used in the forcing equations. All
    quantities are indexed by year.

-   $1 - \Phi_{CH4}$is the one-year retention rate of CH4 in the
    atmosphere.

-   *d~CH4~ =2.84* (the density of *CH4,* expressed in *Mt/ppbv*) is
    then used to convert concentration in Mt into ppbv for reporting
    purposes.

c\) N2O accumulation is also represented by a single-box model in a
manner entirely similar to CH4, although with different parameter
values. The corresponding equations are as follows:

![](media/image19.emf)

## Radiative forcing

We assume, as is routinely done in atmospheric science, that the
atmospheric radiative forcings caused by the various gases are additive
(IPCC, 2007). Thus:

![](media/image20.emf)

We now explain these four terms.

a\) The relationship between CO2 accumulation and increased radiative
forcing, *∆F~CO2~(y)*, is derived from empirical measurements and
climate models (IPCC 2001 and 2007).

  -----------------------------------------------------------------------
  ∆F~CO2~(y) = γ \* ![](media/image21.emf)
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

where:

-   M~0~ (i.e.CO2ATM_PRE_IND) is the pre-industrial (circa 1750)
    reference atmospheric concentration of CO2 = 596.4 GtC

-   γ is the radiative forcing sensitivity to atmospheric CO~2~
    concentration doubling = 3.7 W/m^2^

b\) The radiative forcing due to atmospheric CH4 is given by the
following expression (IPCC 2007), where the subscript tot has been
omitted

$$\mathbf{\Delta}\mathbf{F}_{\mathbf{CH4}}\mathbf{(y) = 0.036}\mathbf{\cdot}\left( \sqrt{\mathbf{CH}\mathbf{4}_{\mathbf{y}}}\mathbf{-}\sqrt{\mathbf{CH}\mathbf{4}_{\mathbf{0}}} \right)\mathbf{-}\left\lbrack \mathbf{f(CH}\mathbf{4}_{\mathbf{y}}\mathbf{,N2}\mathbf{O}_{\mathbf{0}}\mathbf{)}\mathbf{-}\mathbf{f(CH}\mathbf{4}_{\mathbf{0}}\mathbf{,N2}\mathbf{O}_{\mathbf{0}}\mathbf{)} \right\rbrack\mathbf{(7}\mathbf{-}\mathbf{8)}$$

c\) The radiative forcing due to atmospheric N2O is given by the
following expression (IPCC, 2007)

$$\mathbf{\Delta}\mathbf{F}_{\mathbf{N2O}}\mathbf{(y) = 0.12}\mathbf{\cdot}\left( \sqrt{\mathbf{N2}\mathbf{O}_{\mathbf{y}}}\mathbf{-}\sqrt{\mathbf{N2}\mathbf{O}_{\mathbf{0}}} \right)\mathbf{-}\left\lbrack \mathbf{f(CH}\mathbf{4}_{\mathbf{0}}\mathbf{,N2}\mathbf{O}_{\mathbf{y}}\mathbf{)}\mathbf{-}\mathbf{f(CH}\mathbf{4}_{\mathbf{0}}\mathbf{,N2}\mathbf{O}_{\mathbf{0}}\mathbf{)} \right\rbrack\mathbf{(7}\mathbf{-}\mathbf{9)}$$

where:

$$\mathbf{f(x,y) = 0.47}\mathbf{\cdot}\mathbf{\ln}\left\lbrack \mathbf{1 + 2.01}\mathbf{\cdot}\mathbf{1}\mathbf{0}^{\mathbf{-}\mathbf{5}}\mathbf{\cdot}\mathbf{(xy}\mathbf{)}^{\mathbf{0.75}}\mathbf{+ 5.31}\mathbf{\cdot}\mathbf{1}\mathbf{0}^{\mathbf{-}\mathbf{15}}\mathbf{\cdot}\mathbf{x(xy}\mathbf{)}^{\mathbf{1.52}} \right\rbrack\mathbf{(7}\mathbf{-}\mathbf{10)}$$

Note that the f(x,y) function, which quantifies the cross-effects on
forcing of the presence in the atmosphere of both gases (CH4 and N2O),
is not quite symmetrical in the two gases. As usual, the 0 subscript
indicates the pre-industrial times (1750).

d\) EXOFOR(y) is the increase in total radiative forcing at period t
relative to pre-industrial level due to GHG's that are not represented
explicitly in the model. Units = W/m^2^. In Nordhaus and Boyer (1999),
only emissions of CO2 were explicitly modeled, and therefore EXOFOR(y)
accounted for all other GHG's. In TIMES, N~2~O and CH~4~ are fully
accounted for, but some other substances are not (e.g. CFC's, aerosols,
ozone, volcanic activity, etc.). Therefore, the values for EXOFOR(y)
will differ from those in Nordhaus and Boyer (1999). It is the modeler's
responsibility to include in the calculation of EXOFOR(y) the forcing
from only those gases and other causes that are not modeled. The careful
modeler may also want to adapt the EXOFOR trajectory to particular
scenarios. This has been done using alternative trajectories for EXOFOR
provided by other models, as was done in a multi-model, multi-scenario
study conducted at the Energy Modeling Forum (Clarke et al., 2009)

The parameterization of the three forcing equations (7-8, 7-9, and 7-10)
is not controversial and relies on the results reported by Working Group
I of the IPCC. IPCC (2001, Table 6.2, p.358) provides a value of 3.7 for
γ, smaller than the one used by Nordhaus and Boyer (γ = 4.1). We have
adopted this lower value of 3.7 W/m^2^ as default in TIMES. Users are
free to experiment with other values of the γ parameter. The same
reference provides the entire expressions for all three forcing
equations.

## Linear approximations of the three forcings

In TIMES, each of the three forcing expressions is replaced by a linear
approximation, in order to preserve linearity of the entire model. All
three forcing expressions are concave functions. Therefore, two linear
approximations are obvious candidates. The first one is an approximation
from below, consisting of the chord of the graph between two selected
end-points. The second one has the same slope as the chord and is
tangent to the graph, thus approximating the function from above. The
final approximation is the arithmetic average of the two approximations.
These linear expressions are easily derived once a range of interest is
defined by the user.

As an example, we derive below the linear approximation for the CO2
forcing expression. The other approximations are obtained in a similar
manner.

***Linear approximation for the CO2 forcing expression*** (see technical
note "TIMES Climate Module" for similar approximations of the other two
forcings):

First, an interval of interest for the concentration M must be selected
by the user. The interval should be wide enough to accommodate the
anticipated values of the concentrations, but not so wide as to make the
approximation inaccurate. We denote the interval (M~1~,M~2~).

Next, the linear forcing equation is taken as the half sum of two linear
expressions, which respectively underestimate and overestimate the exact
forcing value. The underestimate consists of the chord of the
logarithmic curve, whereas the overestimate consists of the tangent to
the logarithmic curve that is parallel to the chord. These two estimates
are illustrated in Figure 7.1, where the interval (M~1~,M~2~) is from
375 ppm to 550 ppm.

By denoting the pre-industrial concentration level as *M~0~*, the
general formulas for the two estimates are as follows:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Overestimate:*     $$F_{1}(M) = \frac{\gamma}{\ln 2} \cdot \left\lbrack \ln(\frac{\gamma}{slope \cdot \ln(2) \cdot M_{0}}) - 1 \right\rbrack + slope \cdot M$$   
  ------------------- --------------------------------------------------------------------------------------------------------------------------------------------- ----
  *Underestimate:*    $$F_{2}(M) = \gamma \cdot \ln(M_{1}/M_{0})/\ln 2 + slope \cdot (M - M_{1})$$                                                                  

                                                                                                                                                                    

  where:              $$slope = \gamma \cdot \frac{\ln(M_{2}/M_{1})/\ln 2}{(M_{2} - M_{1})}$$                                                                       
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Final approximation*: $F_{3}(M) = \frac{F_{1}(M) + F_{2}(M)}{2}$

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

## Temperature increase

In the TIMES Climate Module as in many other integrated models, climate
change is represented by the global mean surface temperature. The idea
behind the two-reservoir model is that a higher radiative forcing warms
the atmospheric layer, which then quickly warms the upper ocean. In this
model, the atmosphere and upper ocean form a single layer, which slowly
warms the second layer consisting of the deep ocean.

ΔT~up~(y) = ΔT~up~(y-1) +σ~1~{F(y) --λΔT~up~(y-1) -- σ~2~ \[ΔT~up~(y-1)
-- ΔT~low~(y-1)\]} (7-11)

ΔT~low~(y) = ΔT~low~(y-1) + σ~3~\[ΔT~up~(y-1) -- ΔT~low~ (y-1)\] (7-12)

with

-   ΔT~up~ = globally averaged surface temperature increase above
    > pre-industrial level,

![](media/image22.emf){width="5.25in" height="4.4847222222222225in"}

*Figure 7.1. Illustration of the linearization of the CO2 radiative
forcing function*

-   ΔT~low~= deep-ocean temperature increase above pre-industrial level,

-   σ~1~= 1-year speed of adjustment parameter for atmospheric
    > temperature (also known as the lag parameter),

-   σ~2~= coefficient of heat loss from atmosphere to deep oceans,

-   σ~3~ = 1-year coefficient of heat gain by deep oceans,

-   λ= feedback parameter (climatic retroaction). It is customary to
    > write λ as λ =γ/C~s~, C~s~ being the climate sensitivity
    > parameter, defined as the change in equilibrium atmospheric
    > temperature induced by a doubling of CO~2~ concentration. In
    > contrast with most other parameters, the value of C~s~ is highly
    > uncertain, with a possible range of values from 1^o^C to 10^o^C.
    > This parameter is therefore a prime candidate for sensitivity
    > analysis, or for treatment by probabilistic methods such as
    > stochastic programming.

For more details on the implementation of the Climate Module in TIMES,
including parameters, variables, and equations, as represented in the
TIMES code, see Appendix A of Part II.

# The Stochastic Programming extension

## Preamble to chapters 8 to 11

Recall that the core TIMES paradigm described in chapters 3, 4, and 5
makes several basic assumptions:

-   Linearity of the equations and objective function

-   Perfect foresight of all agents over the entire horizon

-   Competitive markets (i.e. no market power by any agent)

If any or all of these assumptions are violated, the properties of the
resulting equilibrium are no longer entirely valid. In the following
four chapters, we present four variants of the TIMES paradigm that
depart from the core model. Each of these variants (extensions) departs
from one or more assumptions above, as follows:

-   Stochastic Programming TIMES extension: departs from the perfect
    foresight assumption and instead assumes that certain key model
    parameters are random. This extension requires the use of stochastic
    programming rather than the usual deterministic linear programming
    algorithm;

-   Limited horizon TIMES extension: departs from the perfect foresight
    assumption and replaces it by an assumption of limited (in time)
    foresight. This extension requires the use of sequential linear
    programming rather than a single global linear optimization;

-   Lumpy investments extension: departs from the linearity assumption
    and replaces it by the assumption that certain investments may only
    be made in discrete units rather than in infinitely divisible
    quantities. This extension requires the use of mixed integer
    programming (MIP) instead of Linear programming;

-   The endogenous technological learning (ETL) extension: departs from
    the linearity assumption for the cost of technologies and replaces
    it by an assumption that the costs of some technologies are
    decreasing functions of the cumulative amounts of the technologies,
    i.e. a learning curve is assumed. This entails that some parts of
    the objective function are non-linear and non-convex, and requires
    the use of MIP.

[Remark]{.underline}: None of these four extensions departs from the
competitive market assumption. It is *also* possible to simulate certain
types of non-competitive behavior using TIMES. For instance, it has been
possible to simulate the behavior of the OPEC oil cartel by assuming
that OPEC imposes an upper limit on its oil production in order to
increase its long term profit (Loulou et al, 2007). Such uses of TIMES
are not embodied in new extensions. Rather, they are left to the
ingenuity of the user.

## Stochastic Programming concepts and formulation

Stochastic Programming is a method for making optimal decisions under
risk. The risk consists of facing uncertainty regarding the values of
some (or all) of the LP parameters (cost coefficients, matrix
coefficients, RHSs). Each uncertain parameter is considered to be a
random variable, usually with a discrete, known probability
distribution. The objective function thus becomes also a random variable
and a criterion must be chosen in order to make the optimization
possible. Such a criterion may be expected cost, expected utility, etc.,
as mentioned by Kanudia and Loulou (1998). Technical note
"TIMES-Stochastic" provides a more complete description of the TIMES
implementation

Uncertainty on a given parameter is said to be resolved, either fully or
partially, at the *resolution time*, i.e. the time at which the actual
value of the parameter is revealed. Different parameters may have
different times of resolution. Both the resolution times and the
probability distributions of the parameters may be represented on an
event tree, such as the one of figure 8.1, depicting a typical
energy/environmental situation. In figure 8.1, two parameters are
uncertain: mitigation level, and demand growth rate. The first may have
only two values (High and Low), and becomes known in 2010. The second
also may have two values (High and Low) and becomes known in 2020. The
probabilities of the outcomes are shown along the branches. This example
assumes that present time is 2000. This example is said to have three
stages (i.e. two resolution times). The simplest non-trivial event tree
has only two stages (a single resolution time). Each pathway along the
event tree, representing a different realization of the uncertain
parameters is referred to as a state-of-the-world (SOW).

The **key observation** is that prior to resolution time, the decision
maker (and hence the model) does not know the eventual values of the
uncertain parameters, but still has to take decisions. On the contrary,
after resolution, the decision maker knows with certainty the outcome of
some event(s) and his subsequent decisions will be different depending
on which outcome has occurred.

For the example shown in figure 8.1, in 2000 and 2010 there can be only
one set of decisions, whereas in 2020 there will be two sets of
decisions, contingent on which of the mitigation outcomes (High or Low)
has occurred, and in 2030, 2040, 2050 and 2060, there will be four sets
of contingent decisions.

![](media/image23.emf){width="5.825694444444444in"
height="4.302777777777778in"}

*Figure*

* 8.**1. Event Tree for a three-stage stochastic TIMES Example.*

This remark leads directly to the following general multi-period,
multi-stage stochastic program in Equations 8-1 to 8-3 below. The
formulation described here is based on Dantzig (1963, Wets (1989), or
Kanudia and Loulou (1999), and uses the expected cost criterion. Note
that this is a LP, but its size is much larger than that of the
deterministic TIMES model.

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

> *t =* time period
>
> *T =* set of time periods
>
> *s =* state index
>
> *S(t) =* set of state indices for time period t;

For Figure 8.1, we have: S(2000) = 1; S(2010) = 1; S(2020) = 1,2;
S(2030) = 1,2,3,4;\
S(2040) = 1,2,3,4; S(2050) = 1,2,3,4; S(2060) = 1,2,3,4;

> *S*(*T*) = set of state indices at the last stage (the set of
> *scenarios*). Set *S(T)* is homeomorphic to the set of paths from
> period 1 to last period, in the event tree.
>
> *g*(*t,s*) = a unique mapping from $\left\{ (t,s)|s \in S(T) \right\}$
> to *S*(*t*), according to the event tree. *g(t,s)* is the state at
> period *t* corresponding to scenario *s*.
>
> *X*(*t,s*) = the column vector of decision variables in period t,
> under state s
>
> *C*(*t,s*) = the cost row vector
>
> *p*(*t,s*) = event probabilities
>
> *A*(*t,s*) = the LP sub-matrix of single period constraints, in time
> period t, under state s
>
> *b*(*t,s*) = the right hand side column vector (single period
> constraints) in time period t, under state s
>
> *D*(*t,s*) = the LP sub-matrix of multi-period constraints under state
> s
>
> *e*(*s*) = the right hand side column vector (multi-period
> constraints) under scenario s

**Alternate formulation**: The above formulation makes it a somewhat
difficult to retrieve the strategies attached to the various scenarios.
Moreover, the actual writing of the cumulative constraints (8-3) is a
bit delicate. An alternate (but equivalent) formulation consists in
defining one scenario per path from initial to terminal period, and to
define distinct variables *X(t,s)* for each scenario and each time
period. For instance, in this alternate formulation of the example,
there would be four variables *X(t,s)* at every period t, (whereas there
was only one variable X(2000,1) in the previous formulation).

+------------------------------------------------------------------+---+
| **Minimize**                                                     |   |
|                                                                  |   |
| $$Z = \sum_{t \in T}^{}{}\s                                      |   |
| um_{s \in S(t)}^{}{}C(t,s) \times X(t,s) \times p(t,s)(8 - 1)'$$ |   |
+------------------------------------------------------------------+---+

**Subject to:**

  ----------------------------------------------------------------- -----
  $A(t,s) \times X(t,s) \geq b(t,s)$ *all t, all* s (8---2)'        

  $\sum_{t \in T}^{}{D(t,s) \times X(t,s)} \geq e(s)$ *all t, all*  
  s (8---3)'                                                        
  ----------------------------------------------------------------- -----

Of course, in this approach we need to add equality constraints to
express the fact that some scenarios are identical at some periods. In
the example of Figure 8.1, we would have:

X(2000,1)=X(2000,2)=X(2000,3)=X(2000,4),

X(2010,1)=X(2010,2)=X(2010,3)=X(2010,4),

X(2020,1)=X(2020,2),

X(2020,3)=X(2020,4).

Although this formulation is less parsimonious in terms of additional
variables and constraints, many of these extra variables and constraints
are in fact eliminated by the pre-processor of most optimizers. The main
advantage of this new formulation is the ease of producing outputs
organized by scenario.

In the current implementation of stochastic TIMES, the first approach
has been used (Equations 8-1 to 8-3). The results are however reported
for all scenarios in the same way as in the second approach.

In addition, in TIMES there is also an experimental variant for the
modeling of recurring uncertainties with stochastic programming,
described in Appendix A of technical note "TIMES-Stochastic".

## Alternative criteria for the objective function

The preceding description of stochastic programming assumes that the
policy maker accepts the expected cost as his optimizing criterion. This
is equivalent to saying that he is risk neutral. In many situations, the
assumption of risk neutrality is only an approxi­mation of the true
utility function of a decision maker.

Two alternative candidates for the objective function are:

-   Expected utility criterion with linearized risk aversion

-   Minimax Regret criterion (Raiffa,1968, applied in Loulou and
    Kanudia, 1999)

### Expected utility criterion with risk aversion

The first alternative has been implemented into the stochastic version
of TIMES. This provides a feature for taking into account that a
decision maker may be risk averse, by defining a new utility function to
replace the expected cost.

The approach is based on the classical E-V model (an abbreviation for
Expected Value-Variance). In the E-V approach, it is assumed that the
variance of the cost is an acceptable measure of the risk attached to a
strategy in the presence of uncertainty. The variance of the cost of a
given strategy k is computed as follows:

$$Var(C_{k}) = \sum_{j}^{}{p_{j} \bullet (Cost_{j\left| k \right.\ } - EC_{k})^{2}}$$

where ***Cost~j\|k~*** is the cost when strategy ***k*** is followed and
the ***j^th^*** state of nature prevails, and ***EC ~k~*** is the
expected cost of strategy ***k,*** defined as usual by:

$$EC_{k} = \sum_{j}^{}{p_{j} \bullet Cost_{j\left| k \right.\ }}$$

An E-V approach would thus replace the expected cost criterion by the
following utility function to minimize:

$$U = EC + \lambda \cdot \sqrt{Var(C)}$$

where λ\>0 is a measure of the risk aversion of the decision maker. For
λ=0, the usual expected cost criterion is obtained. Larger values of
**λ** indicate increasing risk aversion.

Taking risk aversion into account by this formulation would lead to a
non-linear, non-convex model, with all its ensuing computational
restrictions. These would impose serious limitations on model size.

### Utility function with linearized risk aversion

To avoid non-linearities, it is possible to replace the semi-variance by
the upper-absolute-deviation, defined by:

$$UpAbsDev(Cost_{k}) = \sum_{j}^{}{p_{j} \bullet \left\{ Cost_{j\left| k \right.\ } - EC_{k} \right\}^{+}}$$

where ***y= {x}^+^*** is defined by the following two *linear*
constraints: ***y ≥ x*** , and ***y ≥ 0,*** and the utility is now
written via the following *linear* expression:

$$U = EC + \lambda \cdot UpsAbsDev(C)$$

This is the expected utility formulation implemented into the TIMES
model generator.

## Solving approaches

General multi-stage stochastic programming problems of the type
described above can be solved by standard deterministic algorithms by
solving the deterministic equivalent of the stochastic model. This is
the most straightforward approach, which may be applied to all problem
instances. However, the resulting deterministic problem may become very
large and thus difficult to solve, especially if integer vari­ables are
introduced, but also in the case of linear models with a large number of
stochastic scenarios.

Two-stage stochastic programming problems can also be solved efficiently
by using a Benders de­composition algorithm (Wets, 1989). Therefore, the
classical decompo­sition approach to solving large multi-stage stochastic
linear programs has been nested Benders decomposition. However, a
multi-stage stochastic program with integer vari­ables does not, in
general, allow a nested Benders decomposition. Consequently, more
complex decompositions approaches are needed in the general case (e.g.
Dantzig-Wolfe decomposition with dynamic column generation, or
stochastic decomposition methods).

The current version of the TIMES implementation for stochastic
programming is solely based on directly solving the equivalent
deterministic problem. As this may lead to very large problem instances,
stochastic TIMES models are in practice limited to a relatively small
number of branches of the event tree (SOW\'s).

## Economic interpretation

The introduction of uncertainty alters the economic interpretation of
the TIMES solution. Over the last two decades, economic modeling
paradigms have evolved to a class of equilibria called Dynamic
Stochastic General Equilibria (DSGE, see references Chen and Crucuni,
2012; de Walque et al., 2005; Smets et al., 2007). In the case of
Stochastic TIMES, we are in the presence of a Dynamic Stochastic Partial
Equilibria (DSPE), with a much less developed literature. The complete
characterization of a DSPE is beyond the scope of this documentation,
but it is useful to note some of its properties, which derive from the
theory of Linear Programming, as follows:

-   During the first stage (i.e. before resolution of any
    uncertainties), the meaning of the primal solution is identical to
    that of a deterministic TIMES run, i.e. of a set of optimal
    decisions, whereas the meaning of the shadow prices is that of
    *expected prices*(resp. expected marginal utility changes) of the
    various commodities. This is so because the shadow price is the
    marginal change in objective function when a commodity\'s balance is
    marginally altered, and the objective function is an expected cost
    (resp. an expected utility function).

-   During subsequent stages, the primal values of any given branch of
    the event tree represent the optimal decisions *conditional on the
    corresponding outcome being true*, and the shadow prices are the
    *expected*[^35] *prices* of the commodities also conditional on the
    corresponding outcome being true.

# Using TIMES with limited foresight (time-stepped)

It may be useful to simulate market conditions where all agents take
decisions with only a limited foresight of a few years or decades,
rather than the very long term. By so doing, a modeler may attempt to
simulate \"real-world\" decision making conditions, rather than socially
optimal ones. Both objectives are valid provided the modeler is well
aware of each approach\'s characteristics.

Be that as it may, it is possible to use TIMES in a series of
time-stepped runs, each with an optimizing horizon shorter than the
whole horizon. The option that enables this mode is named FIXBOH, which
freezes the solution over some user chosen years, while letting the
model optimize over later years. The FIXBOH feature has several
applications and is first described below before a full description of
the time-stepped procedure.

## The FIXBOH feature

This feature requires that an initial run be made first, and then FIXBOH
sets fixed bounds for a subsequent run according to the solution values
from the initial run up to the last milestone year less than or equal to
the year specified by the FIXBOH control parameter. For instance, the
initial run may be a reference case, which is run from 2010 to 2100, and
the FIXBOH value might be set at 2015, in which case a subsequent run
would have exactly the same solution values as the reference case up to
2015. This is an extremely convenient feature to use in most situations.

As a generalization to the basic scheme described above, the user can
also request fixing to the previous solution different sets of fixed
years accor­ding to region.

**[Example:]{.underline}** Assume that you would like to analyze the
15-region ETSAP TIAM model with some shocks after the year 2030, and you
are interested in differences in the model solution only in regions that
have notable gas or LNG trade with the EU. Therefore, you would like to
fix the regions AUS, CAN, CHI, IND, JPN, MEX, ODA and SKO completely to
the previous solution, and all other regions to the previous solution up
to 2030.

## The time-stepped option (TIMESTEP)

The purpose of the TIMESTEP option is to run the model in a stepwise
manner with limited foresight. The TIMESTEP control variable specifies
the number of years that should be optimized in each solution step. The
total model horizon will be solved by a series of successive steps, so
that in each step the periods to be optimized are advanced further in
the future, and all periods before them are fixed to the solution of the
previous step (using the FIXBOH feature). It is important that any two
successive steps have one or more overlapping period(s), in order to
insure overall continuity of the decisions between the two steps (in the
absence of the overlap, decisions taken at step ***n*** would have no
initial conditions and would be totally disconnected from step ***n-1***
decisions.)

Figure 9.1 illustrates the step-wise solution approach with a horizon of
8 periods and 6 successive optimization steps. Each step has a 2 period
sub-horizon, and there is also an overlap of one period between a step
and the next. More explicitly: at step 2, all period 2 variables are
frozen at the values indicated in the solution of step 1, and period 3
is free to be optimized. At step 3, period 3 variables are frozen and
period 4 is optimized, etc.

![](media/image24.wmf){width="5.674305555555556in"
height="2.765277777777778in"}

*Figure 9.1. Sequence of optimized periods in the stepped TIMES solution
approach.*

*Each run includes also the fixed solution of all earlier periods.*

The amount of overlapping years between successive steps is by default
half of the active step length (the value of TIMESTEP), but it can be
controlled by the user.

[Important remark]{.underline}: as mentioned above, the user chooses the
lengths of the sub-horizons and the length of the overlaps, *both
expressed in years*. Because the time periods used in the model may be
variable and may not always exactly match with the step-length and
overlap, the actual active step-lengths and overlaps may differ somewhat
from the values specified by the user. At each step the model generator
uses a heuristic that tries to make a best match between the remaining
available periods and the prescribed step length. However, at each step
it is imperative that at least one of the previously solved periods must
be fixed, and at least one remaining new period is taken into the active
optimization in the current step.

# The Lumpy Investment extension

In some cases, the linearity property of the TIMES model may become a
drawback for the accurate modeling of certain investment decisions.
Consider for example a TIMES model for a relatively small community such
as a city. For such a scope the *granularity* of some investments may
have to be taken into account. For instance, the size of an electricity
generation plant proposed by the model would have to conform to an
implementable minimum size (it would make no sense to decide to
construct a 50 MW nuclear plant). Another example for multi-region
modeling might be whether or not to build cross-region electric grid(s)
or gas pipeline(s) in discrete size increments. Processes subject to
investments of only specific size increments are described as "lumpy"
investments.

For other types of investments, size does not matter: for instance the
model may decide to purchase 10,950.52 electric cars, which is easily
rounded to 10,950 without any serious inconvenience, especially since
this number is an annual figure. The situation is similar for a number
of residential or commercial heating devices; or for the capacity of
wind turbines; or of industrial boilers; in short, for any technologies
with relatively small minimum feasible sizes. Such technologies would
not be candidates for treatment as "lumpy" investments.

This chapter describes the basic concept and mathematics of lumpy
investment option, whereas the implementation details are available in
Part II, section 6.3.24. We simply note here that this option, while
introducing new variables and constraints, does not affect existing
TIMES constraints.

It is the user's responsibility to decide whether or not certain
technologies should respect the minimum size constraint, weighing the
pros and cons of so doing. This chapter explains how the TIMES LP is
transformed into a Mixed Integer Program (MIP) to accommodate minimum or
multiple size constraints, and states the consequences of so doing on
computational time and on the interpretation of duality results.

The lumpy investment option available in TIMES is slightly more general
than the one described above. It insures that investment in technology
***k*** is equal to one of a finite number ***N*** of pre-determined
sizes: ***0, S~1~(t), S~2~(t), ...,S~N~(t).*** This is useful when
several typical plant sizes are feasible in the real world. As implied
by the notation, these discrete sizes may be different at different time
periods. Note that by choosing the ***N*** sizes as the successive
multiples of a fixed number ***S***, it is possible to invest (perhaps
many times) in a technology with fixed standard size.

Imposing such a constraint on an investment is unfortunately impossible
to formulate using standard LP constraints and variables. It requires
the introduction of *integer variables* into the formulation. The
optimization problem resulting from the introduction of integer
variables into a Linear Program is called a Mixed Integer Program (MIP).

## Formulation and solution of the Mixed Integer Linear Program

Typically, the modeling of a lumpy investment involves Integer
Variables, i.e. variables whose values may only be non-negative integers
(0, 1, 2, ...). The mathematical formulation is as follows:

$${VAR\_ NCAP(p,t) = \sum_{i = 1}^{N}{S_{i}(p,t) \times}Z_{i}(p,t)each ⥂ t = 1,..,T
}{with
}
{Z_{i}(p,t) = 0or1
}
{and
}
{\sum_{i = 1}^{N}Z_{i}(p,t) \leq 1}$$

The second and third constraints taken together imply that at most one
of the ***Z*** variables is equal to 1 and all others are equal to zero.
Therefore, the first constraint now means that ***NCAP*** is equal to
one of the preset sizes or is equal to 0, which is the desired result.

Although the formulation of lumpy investments *looks* simple, it has a
profound effect on the resulting optimization program. Indeed, MIP
problems are notoriously more difficult to solve than LPs, and in fact
many of the properties of linear programs discussed in the preceding
chapters do not hold for MIPs, including duality theory, complementary
slackness, etc. Note that the constraint that *Z(p,t)* should be 0 or 1
departs from the *divisibility* property of linear programs. This means
that the *feasibility domain* of integer variables (and therefore of
some investment variables) is no longer contiguous, thus making it
vastly more difficult to apply purely algebraic methods to solve MIP's.
In fact, practically all MIP solution algorithms make use (at least to
some degree) of partial enumerative schemes, which tend to be time
consuming and less reliable[^36] than the algebraic methods used in LP.

The reader interested in more technical details on the solution of LPs
and of MIPs is referred to references (Hillier and Lieberman, 1990,
Nemhauser et al. 1989). In the next section we shall be content to state
one important remark on the interpretation of the dual results from MIP
optimization.

## Discrete early retirement of capacity

The discrete retirement of capacity that was briefly mentioned in
section 5.4.11 requires a treatment quite similar to that of discrete
addition to capacity presented here. The complete mathematical
formulation mimics that presented above, and is fully described in Part
II, section 6.3.26, of the TIMES documentation.

## Important remark on the MIP dual solution (shadow prices)

Using MIP rather than LP has an important impact on the interpretation
of the TIMES shadow prices. Once the optimal MIP solution has been
found, it is customary for MIP solvers to fix all integer variables at
their optimal (integer) values, and to perform an additional iteration
of the LP algorithm, so as to obtain the dual solution (i.e. the shadow
prices of all constraints). However, the interpretation of these prices
is different from that of a pure LP. Consider for instance the shadow
price of the natural gas balance constraint: in a pure LP, this value
represents the price of natural gas. In MIP, this value represents the
price of gas *conditional on having fixed the lumpy investments at their
optimal integer values.* What does this mean? We shall attempt an
explanation via one example: suppose that one lumpy investment was the
investment in a gas pipeline; then, *the gas shadow price will not
include the investment cost of the pipeline, since that investment was
fixed when the dual solution was computed*.

In conclusion, when using MIP, only the primal solution is fully
reliable. In spite of this major caveat, modeling lumpy investments may
be of paramount importance in some instances, and may thus justify the
extra computing time and the partial loss of dual information.

# The Endogenous Technological Learning extension

In a long-term dynamic model such as TIMES the characteristics of many
of the future technologies are almost inevitably changing over the
sequence of future periods due to *technological learning*.

In some cases it is possible to forecast such changes in characteristics
as a function of time, and thus to define a time-series of values for
each parameter (e.g. unit investment cost, or efficiency). In such
cases, technological learning is *exogenous* since it depends only on
time elapsed and may thus be established outside the model.

In other cases there is evidence that the pace at which some
technological parameters change is dependent on the *experience*
acquired with this technology. Such experience is not solely a function
of time elapsed, but typically depends on the cumulative investment
(often global) in the technology. In such a situation, technological
learning is *endogenous*, since the future values of the parameters are
no longer a function of time elapsed alone, but depend on the cumulative
investment decisions taken by the model (which are unknown). In other
words, the evolution of technological parameters may no longer be
established outside the model, since it depends on the model's results.

Endogenous technological learning (ETL) is also named
*Learning-By-Doing* (LBD) by some authors.

Whereas exogenous technological learning does not require any additional
modeling, ETL presents a tough challenge in terms of modeling ingenuity
and of solution time. In TIMES, there is a provision to represent the
effects of endogenous learning on the unit investment cost of
technologies. Other parameters (such as efficiency) are not treated, at
this time.

## The basic ETL challenge

Empirical studies of unit investment costs of several technologies have
been undertaken in several countries. Many of these studies find an
empirical relationship between the unit investment cost of a technology
at time ***t***, ***INVCOST~t~***, and the cumulative investment in that
technology up to time ***t***,
$C_{t} = \sum_{j = - 1}^{t}{VAR\_ NCAP_{j}}$.

A typical relationship between unit investment cost and cumulative
investments is of the form:

$$INVCOST_{t} = a \cdot C_{t}^{- b}(11 - 1)$$

where

-   *INVCOST*[^37] is the unit cost of creating one unit of the
    technology, which is no longer a constant, but evolves as more units
    of the technology are produced;

-   ***a*** is the value of I*NVCOST* for the first unit of the
    technology (when ***C~t~*** is equal to 1) and;

-   ***b*** is the learning index, representing the speed of
    learning[^38].

As experience builds up, the unit investment cost decreases, potentially
rendering investments in the technology more attractive. It should be
clear that near-sighted investors will not be able to detect the
advantage of investing early in learning technologies, since they will
only observe the high initial investment cost and, being near-sighted,
will not anticipate the future drop in investment cost resulting from
early investments. In other words, tapping the full potential of
technological learning requires far-sighted agents who accept making
initially non-profitable investments in order to later benefit from the
investment cost reduction.

With regard to actual implementation, simply using (11-1) as the
objective function coefficient of ***VAR_NCAP~t~*** will yield a
non-linear, non-convex expression. Therefore, the resulting mathematical
optimization is no longer linear, and requires special techniques for
its solution. In TIMES, a Mixed Integer Programming (MIP) formulation is
used, that we now describe.

## The TIMES formulation of ETL

### The cumulative investment cost

We follow the basic approach described in Barreto, 2001.

The first step of the formulation is to express the total investment
cost, i.e. the quantity that should appear in the objective function.
The cumulative investment cost ***TC~t~*** of a learning technology in
period ***t***is obtained by integrating expression (11-1):

$$TC_{t} = \int_{0}^{C_{t}}{a \cdot y^{- b}*dy} = \frac{a}{1 - b} \cdot {C_{t}}^{- b + 1}(11 - 2)$$

***TC~t~*** is a concave function of ***C~t~***, with a shape as shown
in figure 11.1

![](media/image26.wmf)

*Figure 11.1. Example of a cumulative learning curve*

With the Mixed Integer Programming approach implemented in TIMES, the
cumulative learning curve is approximated by linear segments, and binary
variables are used to represent some logical conditions. Figure 11.2
shows a possible piecewise linear approximation of the curve of Figure
11.1. The choice of the number of steps and of their respective lengths
is carefully made so as to provide a good approximation of the smooth
cumulative learning curve. In particular, the steps must be smaller for
small values than for larger values, since the curvature of the curve
diminishes as total investment increases. The formulation of the ETL
variables and constraints proceeds as follows (we omit the period,
region, and technology indexes for notational clarity):

1.  The user specifies the set of learning technologies;

2.  For each learning technology, the user provides:

    a.  The progress ratio ***pr*** (from which the learning index
        ***b*** may be inferred)

    b.  One initial point on the learning curve, denoted ***(C~0~ ,
        TC~0~ )***

    c.  The maximum allowed cumulative investment ***C~max\ ~***(from
        which the maximum total investment cost ***TC~max~*** may be
        inferred)

    d.  The number ***N*** of segments for approximating the cumulative
        learning curve over the ***(C~0~***, ***C~max~)*** interval.

> Note that each of these parameters, including ***N,*** may be
> different for different technologies.

3.  The model automatically selects appropriate values for the ***N***
    step lengths, and then proceeds to generate the required new
    variables and constraints, and the new objective function
    coefficients for each learning technology. The detailed formulae are
    shown and briefly commented on below.

![](media/image27.wmf)

*Figure 11.2. Example of a 4-segment approximation of the cumulative
cost curve*

### Calculation of break points and segment lengths

The successive interval lengths on the vertical axis are chosen to be in
geometric progression, each interval being twice as wide as the
preceding one. In this fashion, the intervals near the low values of the
curve are smaller so as to better approximate the curve in its high
curvature zone. Let ***{TC~i-1~ , TC~i~}*** be the ***i^th^*** interval
on the vertical axis, for ***i = 1, ..., N-1***. Then:

$$TC_{i} = TC_{i - 1} + 2^{i - N - 1}(T{Co^{N}}_{\max}$$

Note that ***TC~max\ ~*** is equal to ***TC~N~***.

The break points on the horizontal axis are obtained by plugging the
***TC~i~*** 's into expression (11-2), yielding:

$$C_{i} = \left( \frac{(1 - b)}{a}\left( TC_{i} \right) \right)^{\frac{1}{1 - b}},i = 1,2,...,N$$

### New variables

Once intervals are chosen, standard approaches are available to
represent a concave function by means of integer (0-1) variables. We
describe the approach used in TIMES.

First, we define *N* continuous variables ***x~i~***, *i= 1,...,N*. Each
***x~i~*** represents the portion of cumulative investments lying in the
***i^th^*** interval. Therefore, the following holds:

![](media/image28.emf)

We now define ***N*** integer (0-1) variables ***z~i~*** that serve as
indicators of whether or not the value of ***C*** lies in the
***i^th\ ^***interval. We may now write the expression for ***TC***, as
follows:

![](media/image29.emf)

where ***b~i~*** is the slope of the ***i^th^*** line segment, and
***a~i~*** is the value of the intercept of that segment with the
vertical axis, as shown in figure 11.3. The precise expressions for
***a~i~*** and ***b~i~*** are:

$${b_{i} = \frac{TC_{i} - TC_{i - 1}}{C_{i} - C_{i - 1}}i = 1,2,...,N
}{11 - 5
}$$$a_{i} = TC_{i - 1} - b_{i} \cdot C_{i - 1}i = 1,2,...,N$
![](media/image30.wmf)*Figure 11.3. The i^th^ segment of the step-wise
approximation*

### New constraints

For (11-4) to be valid we must make sure that exactly one ***z~i\ ~***is
equal to 1, and the others equal to 0. This is done (recalling that the
***z~i~*** variables are 0-1) via:

$$\sum_{i = 1}^{N}{z_{i} ⥂ ⥂ = ⥂ ⥂ ⥂ ⥂ 1}$$

We also need to make sure that each ***x~i\ ~***lies within the *i^th^*
interval whenever ***z~i~*** is equal to 1 and is equal to 0 otherwise.
This is done via two constraints:

$$C_{i - 1} \cdot z_{i} \leq x_{i} \leq C_{i} \cdot z_{i}$$

### Objective function terms

Re-establishing the period index, we see that the objective function
term at period ***t***, for a learning technology is thus equal to
***TC~t\ ~***- ***TC~t-1~***, which needs to be discounted like all
other investment costs.

### Additional (optional) constraints

Solving integer programming problems is facilitated if the domain of
feasibility of the integer variables is reduced. This may be done via
additional constraints that are not strictly needed but that are
guaranteed to hold. In our application we know that experience (i.e.
cumulative investment) is always increasing as time goes on. Therefore,
if the cumulative investment in period t lies in segment i, it is
certain that it will not lie in segments *i-1, i-2, .., 1* in time
period *t+1*. This leads to two new constraints (re-establishing the
period index ***t*** for the ***z*** variables):

![](media/image31.emf)

Summarizing the above formulation, we observe that each learning
technology requires the introduction of ***N\*T*** integer (0-1)
variables. For example, if the model has 10 periods and a 5-segment
approximation is selected, 50 integer (0-1) variables are created for
that learning technology, assuming that the technology is available in
the first period of the model. Thus, the formulation may become very
onerous in terms of solution time, if many learning technologies are
envisioned, and if the model is of large size to begin with. In section
11.5 we provide some comments on ETL, as well as a word of warning.

## Clustered learning

An interesting variation of ETL is also available in TIMES, namely the
case where several technologies use the same key technology (or
component), itself subject to learning. For instance, table 11.1 lists
11 technologies using the key Gas Turbine technology. As experience
builds up for gas the turbine, each of the 11 technologies in the
cluster benefits. The phenomenon of clustered learning is modeled in
TIMES via the following modification of the formulation of the previous
section.

Let ***k*** designate the key technology and let ***l* = 1, 2, ...,*L***
designate the set of clustered technologies attached to ***k***. The
approach consists of three steps:

i)  Step 1: designate ***k*** as a learning technology, and write for it
    the formulation of the previous section;

ii) Step 2: subtract from each *INVCOST**~l\ ~***the initial investment
    cost of technology ***k*** (this will avoid double counting the
    investment cost of ***k***);

iii) Step 3: add the following constraint to the model, in each time
     period. This ensures that learning on ***k*** spreads to all
     members of its cluster:

$$VAR\_ NCAP_{k} - \sum_{l = 1}^{L}{VAR\_ NCAP_{l} = 0}$$

*Table 11.1: Cluster of gas turbine technologies*

*(from A. Sebregts and K. Smekens, unpublished report, 2002)*

  -----------------------------------------------------------------------
  Description

  Integrated Coal gasification power plant

  Integrated Coal Gasification Fuel Cell plant

  Gas turbine peaking plant

  Existing gas Combined Cycle power plant

  New gas Combined Cycle power plant

  Combined cycle Fuel Cell power plant

  Existing gas turbine CHP plant

  Existing Combined Cycle CHP plant

  Biomass gasification: small industrial cog.

  Biomass gasification: Combined Cycle power plant

  Biomass gasification: ISTIG+reheat
  -----------------------------------------------------------------------

## Learning in a multiregional TIMES model

Technological learning may be acquired via global or local experience,
depending on the technology considered. There are examples of
technologies that were developed and perfected in certain regions of the
world, but have tended to remain regional, never fully spreading
globally. Examples are found in land management, irrigation, and in
household heating and cooking devices. Other technologies are truly
global in the sense that the same (or close to the same) technology
becomes rather rapidly commercially available globally. In the latter
case, global experience benefits users of the technology worldwide.
Learning is said to *spillover* globally. Examples are found in large
electricity plants, in steel production, wind turbines, and many other
sectors.

The first and obvious implication of these observations is that the
appropriate model scope must be used to study either type of technology
learning. The formulation described in the previous sections is adequate
in two cases: a) learning in a single region model, and b) regional
learning in a multiregional model. It does *not* directly apply to
*global learning* in a multiregional global model, where the cumulative
investment variable must represent the sum of all cumulative investments
in all regions together. We now describe an approach to global learning
that may be implemented in TIMES, using only standard TIMES entities.

The first step in modeling multiregional ETL is to create one additional
region, region 0, which will play the role of the Manufacturing Region.
This region's RES consists only of the set of (global) learning
technologies (LT's). Each such LT has the following specifications:

a)  The LT has no commodity input.

b)  The LT has only one output, a new commodity ***c*** representing the
    'learning'. This output is precisely equal to the investment level
    in the LT in each period.

c)  Commodity ***c*** may be exported to all other regions.

Finally, in each 'real' region, the LT is represented with all its
attributes *except the investment cost NCAP_COST.* Furthermore, the
construction of one unit of the LT requires an input of one unit of the
learning commodity ***c*** (using the *NCAP_ICOM* parameter see chapter
3 of PART II). This ensures that the sum of all investments in the LT in
the real regions is exactly equal to the investment in the LT in region
0, as desired.

## Endogenous vs. exogenous learning: a discussion

In this section, we formulate a few comments and warnings that may be
useful to potential users of the ETL feature.

We start by stating a very important caveat to the ETL formulation
described in the previous sections: if a model is run with such a
formulation, it is very likely that the model will select some
technologies, and *will invest massively at some early period* in these
technologies unless it is prevented from doing so by additional
constraints. Why this is likely to happen may be qualitatively explained
by the fact that once a learning technology is selected for investing,
two opposing forces are at play in deciding the optimal timing of the
investments. On the one hand, the discounting provides an incentive for
postponing investments. On the other hand, investing early allows the
unit investment cost to drop immediately, and thus allows much cheaper
investments in the learning technologies in the current and all future
periods. Given the considerable cost reduction that is usually induced
by learning, the first factor (discounting) is highly unlikely to
predominate, and hence the model will tend to invest massively and early
in such technologies, or not at all. Of course, what we mean by
"massively" depends on the other constraints of the problem (such as the
extent to which the commodity produced by the learning technology is in
demand, the presence of existing technologies that compete with the
learning technology, etc.). However, there is a clear danger that we may
observe unrealistically large investments in some learning technologies.

ETL modelers are well aware of this phenomenon, and they use additional
constraints to control the penetration trajectory of learning
technologies. These constraints may take the form of upper bounds on the
capacity of or the investment in the learning technologies in each time
period, reflecting what is considered by the user to be realistic
penetrations. These upper bounds play a determining role in the solution
of the problem, and it is most often observed that the capacity of a
learning technology is either equal to 0 or to the upper bound. This
last observation indicates that the selection of upper bounds (or
capacity/investment growth rates) by the modeler is the predominant
factor in controlling the penetration of successful learning
technologies.

In view of the preceding discussion, a fundamental question arises: is
it worthwhile for the modeler to go to the trouble of modeling
e*ndogenous* learning (with all the attendant computational burdens)
when the results are to a large extent conditioned by *exogenous* upper
bounds? We do not have a clear and unambiguous answer to this question;
that is left for each modeler to evaluate.

However, given the above caveat, a possible alternative to ETL would
consist in using exogenous learning trajectories. To do so, the same
sequence of 'realistic' upper bounds on capacity would be selected by
the modeler, and the values of the unit investment costs (INVCOST) would
be externally computed by plugging these upper bounds into the learning
formula (11-1). This approach makes use of the same exogenous upper
bounds as the ETL approach, but avoids the MIP computational burden of
ETL. Of course, the running of exogenous learning scenarios is not
entirely foolproof, since there is no absolute guarantee that the
capacity of a learning technology will turn out to be exactly equal to
its exogenous upper bound. If that were not the case, a modified
scenario would have to be run, with upper bounds adjusted downward. This
trial-and-error approach may seem inelegant, but it should be remembered
that it (or some other heuristic approach) might prove to be necessary
in those cases where the number of learning technologies and the model
size are both large (thus making the rigorous ETL formulation
computationally intractable).

# General equilibrium extensions

## Preamble

In order to achieve a general (as opposed to partial) equilibrium, the
energy system described in TIMES must be linked to a representation of
the rest of the economy. The idea of hard-linking an energy model with
the economy while still keeping the resulting model as an optimization
program, dates back to the ETA-MACRO model (Manne, 1977), where both the
energy system and the rest of the economy were succinctly represented by
a small number of equations. This approach differs from the one taken by
the so-called Computable General Equilibrium (CGE), models (Johanssen
1960, Rutherford 1992), where the calculation of the equilibrium relies
on the resolution of simultaneous non-linear equations. In CGE\'s, the
use of (non-linear, non-convex) equation solvers limits the size of the
problem and thus the level of detail in the energy system description.
This computational difficulty is somewhat (but not completely)
alleviated when the computation relies on a single non-linear
optimization program. Note however that MACRO is a much simplified
representation of the economy as a single producing sector and no
government sector, thus precluding the endogenous representation of
taxes, subsidies, multi-sector interactions, etc. Therefore, the idea of
a linked TIMES-MACRO model is not to replace the CGE\'s but rather to
create an energy model where the feedbacks from the economy goes beyond
the endogenization of demands (which TIMES does) to include the
endogenization of capital.

Some years after ETA-MACRO, MARKAL-MACRO (Manne-Wene, 1992) was obtained
by replacing the simplified ETA energy sub-model by the much more
detailed MARKAL, giving rise to a large optimization model where most,
but not all equations were linear. The MERGE model (Manne et al., 1995)
is a multi-region version of ETA-MACRO with much more detail on the
energy side --although not as much as in MARKAL-MACRO. The TIMES-MACRO
model (Remme-Blesl, 2006) is based on exactly the same approach as
MARKAL-MACRO. Both MARKAL-MACRO and TIMES-MACRO were essentially
single-region models, until the multi-region version of TIMES-MACRO
(named TIMES-MACRO-MSA, Kypreos-Lettila, 2013) was devised as an
extension that accommodates multiple regions.

In this chapter, we describe the single region and the multi-region
versions of TIMES-MACRO, focusing on the concepts and mathematical
representation, whereas the implementation details are left to Part II
of the TIMES documentation and to technical notes.

## The single-region TIMES-MACRO model

As was already discussed in chapter 4, the main physical link between a
TIMES model and the rest of the economy occurs at the level of the
consumption of energy by the end-use sectors. There are however other
links, such as capital and labor, which are common to the energy system
and the rest of the economy. Figure 12.1 shows the articulation of the
three links in TIMES-MACRO. Energy flows from TIMES to MACRO, whereas
money flows in the reverse direction. Labor would also flow from MACRO
to TIMES, but here a simplification is used, namely that the
representation of labor is purely exogenous in both sub-models. Thus,
TIMES-MACRO is not suitable for analyzing the impact of policies on
labor, or on taxation, etc.

![](media/image32.wmf)

*Figure 12.1. Energy, Labor, and Monetary flows between TIMES and MACRO*

We now turn to the mathematical description of the above, starting with
the MACRO portion of the hybrid model.

### Formulation of the MACRO model

We start our description of the hybrid model by stating the MACRO
equations (12-1) -- (12-6)[^39]:

$Max\mspace{6mu}\mspace{6mu}\sum_{t = 1}^{T - 1}{dfact_{t}} \cdot \ln(C_{t}) + \frac{dfact_{T - 1} \cdot dfactcur{r_{T - 1}}^{\frac{d_{T - 1} + d_{T}}{2}}}{1 - dfactcur{r_{T}}^{\frac{d_{T - 1} + d_{T}}{2}}} \cdot \ln(C_{T})$
(12-1)

$Y_{t} = C_{t} + INV_{t} + EC_{t}$ (12-2)

$Y_{t} = \left( akl \cdot K_{r}^{kpvs \cdot \rho} \cdot l_{t}^{(1 - kpvs)\rho} + \sum_{dm}^{}{b_{dm} \cdot DEM\_ M_{t,dm}^{\rho}} \right)^{\frac{1}{\rho}}$
(12-3)

$l_{1} = 1\mspace{6mu}\mspace{6mu}\quad\text{and      }l_{t + 1} = l_{t} \cdot \left( 1 + growv_{t} \right)^{\frac{d_{t} + d_{t + 1}}{2}}$
(12-4)

$K_{t + 1} = tsrv_{t} \cdot K_{t} + \frac{1}{2}\left( d_{t} \cdot tsrv \cdot INV_{t} + d_{t + 1} \cdot INV_{t + 1} \right)$
(12-5)

$K_{T} \cdot \left( growv_{T} + depr \right) \leq INV_{T}$ (12-6)

with the model **variables**:

> $C_{t}$: annual consumption in period *t*,
>
> $DEM\_ M_{t,dm}$: annual energy demand in MACRO for commodity *dm* in
> period *t*,
>
> $Y_{t}$: annual production in period *t*,
>
> $INV_{t}$: annual investments in period *t*,
>
> $EC_{t}$: annual energy costs in period *t*,
>
> $K_{t}$: total capital in period *t*

and the **exogenous parameters**:

> $akl$: production function constant,
>
> $b_{dm}$: demand coefficient,
>
> $d_{t}$: duration of period *t* in years,
>
> $depr$: depreciation rate,
>
> $dfact_{t}$: utility discount factor,
>
> $dfactcurr_{t}$: annual discount rate,
>
> $growv_{t}$: growth rate in period *t*,
>
> $kpvs$ capital value share,
>
> $l_{t}$: annual labor index in period *t*,
>
> $\rho$: substitution constant,
>
> $T$: period index of the last period,
>
> $tsrv_{t}$: capital survival factor between two periods.

The objective function (12-1) of the MACRO model is the maximization of
the summation of discounted utility at each period. The utility is
defined as the logarithm of consumption $C_{t}$of the households. A
logarithmic utility function embodies a decreasing marginal utility
property (Manne, 1977). Note that the discount factor $dfact_{t}$for
period t must take into account both the length of the period and the
time elapsed between the period\'s start and the base year. Note also
that the discount factor of the last period has a larger impact since it
is assumed to apply to the infinite time horizon after the last model
period (alternatively, the user may decide to limit the number of years
in the last term, in those cases where it is deemed important to confer
less weight to the indefinite future).

The national accounting equation (12-2) simply states that national
production *Y~t~* must cover national consumption *C~t~* , plus
investments *INV~t~* , plus energy costs *EC~t~*.

The production function (12-3) represents the entire economy. It is a
nested, constant elasticity of substitution (CES) function with the
three input factors capital, labor and energy. The production input
factors labor $l_{t}$and capital $K_{t}$form an aggregate, in which both
can be substituted by each other represented via a Cobb-Douglas
function. Then, the aggregate of the energy services and the aggregate
of capital and labor can substitute each other. Note that labor is not
endogenous in MACRO,but is specified exogenously by the user provideda
labor growth rate$growv_{t}$.

The energy in term in (12-3) is a weighted sum of end-use demands in all
sectors *dm* of the economy, *DEM_M~t,dm~* , raised to the power *ρ.* We
defer the definition of these quantities until the next subsection.

The lower the value of the elasticity of substitution the closer is the
linkage between economic growth and increase in energy demand. For
homogenous production functions with constant returns to scale[^40] the
substitution constant $\rho$in (12-3) is directly linked with the
user-defined elasticity of substitution $\sigma$ by the
expression$\rho = 1 - \frac{1}{\sigma}$.

The capital value share $kpvs$ describes the share of capital in the sum
of all production factors and must be specified by the user. The
parameter $akl$ is the level constant of the production function. The
parameters $akl$ and $b_{dm}$ of the production are determined based on
the results from a TIMES model run without the MACRO module.

The capital dynamics equation (12-5) describes the capital stock in the
current period $K_{t + 1}$ based on the capital stock in the previous
period and on investments made in the current and the previous period.
Depreciation leads to a reduction of the capital. This effect is taken
into account by the capital survival factor$tsrv_{t}$, which describes
the share of the capital or investment in period *t* that still exists
in period *t+1*. It is derived from the depreciation rate $depr$ using
the following expression:

$tsrv_{t} = (1 - depr)^{\frac{\left( d_{t + 1} + d_{t} \right)}{2}}$
(12-7)

Expression (12-7) calculates the capital survival factor for a period of
years beginning with the end of the middle year $m_{t}$ and ending with
the end of the year $m_{t + 1}$. The duration between these two middle
years equals the duration $\frac{d_{t + 1} + d_{t}}{2}$. Then, a mean
investment in period *t* is calculated by weighting the investments in
*t* and *t+1* with the respective period duration:
$\frac{1}{2}\left( d_{t} \cdot tsrv \cdot INV_{t} + d_{t + 1} \cdot INV_{t + 1} \right)$.

For the first period it is assumed that the capital stock grows with the
labor growth rate of the first period$growv_{0}$. Thus, the investment
has to cover this growth rate plus the depreciation of capital. Since
the initial capital stock is given and the depreciation and growth rates
are exogenous, the investment in the first period can be calculated
beforehand:

$INV_{0} = K_{0} \cdot \left( depr + growv_{0} \right)$ (12-8)

Since the model horizon is finite, one has to ensure that the capital
stock is not fully exhausted (which would maximize the utility in the
model horizon.) Therefore a terminal condition (12-6) is added, which
guarantees that after the end of the model horizon a capital stock for
the following generations exists. It is assumed that the capital stock
beyond the end of horizon grows with the labor growth rate$growv_{T}$.
This is coherent with the last term of the utility function.

### Linking MACRO with TIMES

TIMES is represented via the following condensed LP

$$Min\ \sum_{t}^{}{dfact}_{t} \bullet {COST\_ T_{t}}_{}(x)$$

s.t. $E \bullet x = DEM\_ T_{dm,t}\ \ \ \ \ \ \ \ (A)$

$$A \bullet x = b\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (B)$$

where

-   *x* is the vector of TIMES variables

-   ${COST\_ T_{t}}_{}(x)$ is the annual undiscounted cost TIMES
    expression

-   *dfact~t~* is the discount factor for period *t*

-   equations *(A)* express the satisfaction of demands in TIMES (and
    thus defines the *DEM_T~dm,t\ ~*variables), and

-   equations *(B)* is the set of all other TIMES constraints

MACRO and TIMES are hard linked via two sets of variables: the energy
variables *DEM_T~dm,t~*, and the period energy costs *COST_T~t~*.

The aggregate energy input into MACRO (see equation (12-3)), is slightly
different from the TIMES variables defined above. In the linked model,
each term *DEM_M* is obtained by further applying a factor
$aeeifac_{t,dm}$ as shown in equation (12-9).

$DEM\_ T_{t,dm} = aeeifac_{t,dm} \cdot DEM\_ M_{t,dm}$ (12-9)

Indeed, the energy demand in the TIMES model can be lower than the
energy requirement of the MACRO model due to demand reductions, which
are caused by autonomous energy efficiency improvements and come in
addition to those captured in the energy sector of the TIMES model. The
autonomous energy efficiency improvement factor $aeeifac_{t,dm}$ is
determined in a calibration procedure described in technical note
"Documentation of the TIMES-MACRO model", which also discusses the
weighing coefficients$b_{dm}$.

The other link consists in accounting for the monetary flow$EC_{t}$,
equal to the expenditures made in the energy sector.
Precisely,$EC_{t}$is equal to the annual *undiscounted* energy system
cost of the TIMES model,$COST\_ T_{t}$, (as used in the TIMES objective
function), augmented with an additional term as shown in equation
(12-10):

$COST\_ T_{t} + \frac{1}{2}qfac\sum_{p}^{}{\frac{cstinv_{t,p}}{\exp f_{t} \cdot capfy_{p}} \cdot XCAP_{t,p}^{2}} = EC_{t}$
(12-10)

with

> $XCAP_{t,p}$: portion of the capacity expansion for technology *p* in
> period *t* that is penalized. Constraint (12-11) below states that it
> is the portion exceeding a predefined tolerable expansion
> rate$\exp f_{t}$,
>
> $EC_{t}$: costs for the production factor energy in the MACRO model,
>
> $qfac$: trigger to activate penalty term (0 for turning-off penalty, 1
> for using penalty term),
>
> $cstinv_{t,p}$: specific annualized investment costs of technology *p*
> in period *t*,
>
> $capfy_{p}$: maximum level of capacity for technology *p*,
>
> $\exp f_{t}$: tolerable expansion between two periods.

Just like in the pure MACRO model, the quadratic penalty term added on
the left hand side of Eqn. (11) serves to slow down the penetration of
technologies. This term plays a somewhat similar role as the growth
constraints do in the stand-alone TIMES model. The variable $XCAP_{t,p}$
is the amount of capacity exceeding a predefined expansion level
expressed by the expansion factor $\exp f_{t}$ and is determined by the
following equation:

$VAR\_ CAP_{t + 1,p} \leq \left( 1 + expf_{t} \right) \cdot VAR\_ CAP_{t,p} + XCAP_{t + 1,p}$
(12-11)

with:

$VAR\_ CAP_{t,p}$: total installed capacity of technology *p* in period
*t*.

As long as the total installed capacity in period *t+1* is below
$\left( 1 + expf_{t} \right) \cdot CAP_{t,p}$ no penalty costs are
applied. For the capacity amount $XCAP_{t + 1,p}$ exceeding this
tolerated capacity level penalty costs are added to the regular costs of
the TIMES model in Equation (12-10).

The quadratic term in Eqn. (11) introduces a large number of nonlinear
terms (one for each technology and period) that may constitute a
considerable computational burden for large models. These constraints
are therefore replaced in the current implementation of TIMES, by linear
piece-wise approximations in a way quite similar to what was done to
linearize the surplus in chapter 4.

### A brief comment

In spite of the linearization of the penalty terms in equation (12-10),
TIMES-Macro still contains non-linearities: its objective function is a
concave function, a good property when maximizing, but there are T
nonlinear, non convex constraints as per equation (12-3) that introduce
a non trivial computational obstacle to large size instances of the
model.

Although not discussed here, the calibration of the TIMES-MACRO model is
an exceedingly important task, since the model must agree with the
initial state of the economy in the dimensions of labor, capital, and
the links between the energy sector and the economy at large. Fuller
details on calibration are provided in the above-mentioned technical
note.

Overall, the experience with TIMES-MACRO has been good, with sizable
model instances solved in reasonable time. But the modeler would benefit
from carefully weighing the limitation of model size imposed by the
non-linear nature of TIMES-MACRO, against the advantage of using a
(single sector) general equilibrium model.

## The multi-regional TIMES-MACRO model (MSA)

In this section, we only sketch the generalization of TIMES-MACRO to a
multi-regional setting. Full details, including the important
calibration step and other implementation issues, appear in technical
note "TIMES-Macro: Decomposition into Hard-Linked LP and NLP Problems".

### Theoretical background

In a multi-regional setting, inter-regional trade introduces an
important new complication in the calculation of the equilibrium[^41].
Indeed, the fact that the utility function used in the MACRO module is
highly non linear also means that the global utility is not equal to the
sum of the national utilities. Also, it would be impractical and
conceptually wrong to define a single consumption function for the
entire set of regions, since the calibration of the model may only be
done using national statistics, and furthermore, there may be large
differences in the parameters of each region\'s production function,
etc.

It follows from the above that it is not possible to use a single
optimization step to calculate the global equilibrium. Instead, one must
resort to more elaborate approaches in order to compute what is termed a
Pareto-optimal solution to the equilibrium problem, i.e. a solution
where the utility of any region may not be improved without
deteriorating the utility of some other region(s).

Such a situation has been studied in the economics literature, starting
with the seminal paper by Negishi (1960) that established the existence
of equilibria that are Pareto-optimal in the Welfare functions. Manne
(1999) applied the theory to the MACRO model, and Rutherford (1992)
proposed a decomposition algorithm that makes the equilibrium
computation more tractable. The Rutherford algorithm is used in the
TIMES-MACRO model. An interesting review of the applications of Negishi
theory to integrated assessment models appeared in Stanton (2010).

### A sketch of the algorithm to solve TIMES-MACRO-MSA

Rutherford\'s procedure is an iterative decomposition algorithm. Each
iteration has two steps. The first step optimizes a large TIMES LP and
the second step optimizes a stand-alone *reduced* non-linear program
which is an alteration of MACRO, and is named MACRO-MSA. These two steps
are repeated until convergence occurs.

Because the two steps must be solved repeatedly, the iterative procedure
is computationally demanding; furthermore, it is established that the
speed of convergence is dependent upon the number of trade variables
that link the regions. For this and other reasons, the trade between
regions is limited to a single commodity, namely a *numéraire*,
expressed in monetary units. The numéraire ***NTX~r,t~*** affects the
national account equation (12-2) of each region, as follows:

$$Y_{r,t} = C_{r,t} + INV_{r,t} + EC_{r,t} + NTX_{r,t}$$

and is subject to the conservation constraint:
$\sum_{r}^{}{NTX_{r,t}\  = \text{0 }}	\forall\ \{ t\}$,

which insures that trade is globally balanced.

[First step:]{.underline} at each iteration, the first step is the
resolution of TIMES using non-elastic demands provided by the previous
solution of the non-linear program (except at iteration 1, where demands
are either exogenously provided or generated by TIMES[^42]).

[Second step:]{.underline} once the TIMES solution is obtained, it is
used to form a quadratic expression representing an approximation of the
aggregate energy cost, to be used in MACRO-MSA. Defining this
approximation is the crux of Rutherford decomposition idea. It replaces
the entire TIMES model, thus greatly simplifying the resolution of Step
2. The global objective function of MACRO-MSA is a weighted sum (over
all regions) of the regional MACRO welfare functions, where the weights
are the Negishi weights for each region. The thus modified global
objective function is maximized. Then, a convergence criterion is
checked. If convergence is not observed, the new demands are fed into
TIMES and a new iteration is started. The Negishi weights are also
updated at each iteration, leading to a new version of the objective,
until the algorithm converges to the Pareto-optimal equilibrium.

The adaptation of Rutherford algorithm to TIMES-MACRO was formalized by
Kypreos (2006) and implemented by Kypreos and Lettila as the
above-mentioned technical note.

# Appendix A: History and comparison of MARKAL and TIMES

## A brief history of TIMES[^43] and MARKAL

The TIMES ([T]{.underline}he [I]{.underline}ntegrated
[M]{.underline}arkal-[E]{.underline}fom[S]{.underline}ystem) and the
MARKAL ([MAR]{.underline}ket [AL]{.underline}location) models have a
common history beginning in the 1970\'s when a formal decision of the
International Energy Agency (IEA) led to the creation of a common tool
for analyzing energy systems, to be shared by the participating OECD
nations. MARKAL became a reality by the year 1980 and became a common
tool of the members of the Energy Technology Systems Analysis Programme
(ETSAP), an IEA Implementing Agreement (IA).

Development of the new modeling paradigm was undertaken over a period of
three years. First a team of national experts from more than sixteen
countries met numerous times to define the data requirements and
mathematics that were to underpin MARKAL. Then the actual coding and
testing of the model formulation proceeded on two parallel tracks. One
team at Brookhaven National Laboratory (BNL) embarked on the undertaking
employing OMNI[^44], a specialized programming language specifically
designed for optimization modeling, that was widely used for modeling
oil refinery operations. The second team at KFA Julich chose to use
Fortran to code the model. While both teams initially succeeded, changes
were quickly necessary that proved to be more manageable in the BNL OMNI
version of MARKAL than in the KFA Fortran version -- leading to the
decision to formally adopt only the BNL OMNI version for general use. A
full description of this initial incarnation of the model maybe be found
in the MARKAL User's Guide (Fishbone, 1983).

MARKAL was used intensively by ETSAP members throughout the two decades
after 1980 and beyond, undergoing many improvements. The initial
mainframe OMNI version of MARKAL was in use until 1990, when BNL ported
the model to the person computer that was just becoming a viable
alternative. At the same time, as part of this move of MARKAL to the PC,
the first model management system for MARKAL databases and model results
was developed at BNL which greatly facilitated working with MARKAL and
opened it up to a new class of users. This PC based shell, MUSS (MARKAL
User Support System, Goldstein, 1991), provided spreadsheet-like
browse/edit facilities for managing the input data, Reference Energy
System (RES) network diagramming to enable viewing the underlying
depiction of the energy system, scenario management and run submission,
and multi-case comparison graphics that collectively greatly facilitated
the ability to work effectively with MARKAL.

The next big step in the evolution of MARKAL/TIMES arose from the BNL
collaboration with Professor Alan Manne of Stanford University resulting
in the porting of MARKAL to the more flexible General Algebraic Modeling
System (GAMS), still used for TIMES today. The driving motivation for
this move to GAMS was to enable the creation of MARKAL-MACRO (see
chapter 12), a major model variant enhancement resulting in a General
Equilibrium version of the model. One drawback of MARKAL-MACRO is that
it was implemented as a non-linear programming (NLP) optimization model,
which limits its usability for large energy system models.

To overcome this shortcoming while embracing one of the main benefits
arising from MARKAL-MACRO, another major model enhancement was
implemented in 1995 from a proposal made in 1980 by Giancarlo Tosato
(1980), to allow end-use service demands to be price sensitive, thus
transforming MARKAL from a supply cost optimization model to a system
computing a supply demand partial equilibrium, named MARKAL-ED (Loulou
and Lavigne, 1996) while retaining its linear form. An alternative
formulation using non-linear programming, MARKAL-MICRO (Van Regemorter,
1998) was also implemented. Many other enhancements were made in the
late 1990\'s and early 2000\'s and are described in the second
comprehensive version of the MARKAL model documentation (Loulou et al.,
2004).

The development of ANSWER, the first Windows interface for MARKAL,
commenced at the Australian Bureau of Agricultural and Resource
Economics (ABARE) in Canberra in early 1996 with primary responsibility
taken by then ABARE staff member Ken Noble. By early 1998 the first
production version of ANSWER-MARKAL was in use, including by most ETSAP
Partners. In late 2003 Ken Noble retired from ABARE, established
Noble-Soft Systems and became the owner of the ANSWER-MARKAL software,
thereby ensuring its continuing development and support.

By the late 1990\'s, the need to gather all the existing MARKAL features
and to create many new ones was becoming pressing, and an international
group of ETSAP researchers was formed to create what became the TIMES
model generator. The main desired new features were as follows:

-   To allow time periods to be of unequal lengths, defined by the user;

-   To allow the user data to control the model structure;

-   To make data as independent as possible of the choice of the model
    periods (data decoupling), in particular to facilitate the
    recalibration of the model when the initial period is changed, but
    also to avoid having to redefine the data when period lengths are
    altered;

-   To formally define commodity flows as new variables (as in the EFOM
    model), thus making it easier to model certain complex processes;

-   To define vintaged processes that allow input data to change
    according to the investment year;

-   To enable the easy creation of flexible processes, a feature that
    was feasible with MARKAL only by creating multiple technologies;

-   To permit time-slices to be entirely flexible with a tiered
    hierarchy of year/season/week/time-of-day to permit much more robust
    modeling of the power sector;

-   To improve the representation and calculation of costs in the
    objective function;

-   To formally identify trade processes in order to facilitate the
    creation of multi-regional models;

-   To define storage processes that carry some commodities from one
    time-slice to another or from some period to another; and

-   To implement more dynamic and inter-temporal user-defined
    constraints.

Definition and development of TIMES began in late 1998, resulting in a
beta version in 1999, and the first production version in year 2000,
initially used by only a small number of ETSAP members. The transition
from MARKAL to TIMES was slower than anticipated, mainly because ETSAP
modellers already had mature MARKAL databases that required serious time
and effort to be converted into TIMES databases.

Furthermore there was a need for a TIMES specific model shell to manage
the new model. Two data handling shells were created during the 2000\'s
by two private developers closely associated with ETSAP and with partial
support from ETSAP: In the early 2000's, VEDA_FE (VErsatile Data
Analysis -Front End) (<http://www.kanors.com/Index.asp>) and in 2008,
ANSWER-TIMES (Noble-Soft Systems, 2009). Even before that, a back-end
version of VEDA (VEDA_BE, Kanudia <http://www.kanors.com/Index.asp>) had
been created to explore and exploit the results and create reports.

Following these developments, and as the merits of TIMES over MARKAL
became increasingly evident, TIMES became the preferred modeling tool
for most ETSAP members, old and new, as well as for energy system
modellers who were not formal ETSAP members, but were either associated
with ETSAP as partners in several outreach projects or on their own.

The first complete documentation of the TIMES model generator was
written in 2005 and made available on the ETSAP website
(<http://www.iea-etsap.org/web/index.asp>). It has since been replaced
by this documentation.

As the number of modellers increased and they gained experience with
TIMES, the model underwent many new additions and enhancements, and the
number of publications based on TIMES rose sharply. One development
started in 2000 and achieved by 2005 was the creation of the first world
multi-regional TIMES model (Loulou, 2007) and the simultaneous creation
of a Climate Module (chapter 7). Together, these two realizations
allowed ETSAP to participate in the Stanford Energy Modeling Forum (EMF,
<https://emf.stanford.edu/>) and conduct global climate change analyses
alongside other modellers who were mostly using general equilibrium
models. Following these developments, several ETSAP teams created
multiple versions of global TIMES models.

At the same time other major new features were implemented, some of them
found in MARKAL though often further advanced in TIMES, such as the
Endogenous Technological Learning feature (chapter 11), the lumpy
investment feature (chapter 10), both of which required the use of mixed
integer programming, and the multi-stage Stochastic Programming option
(chapter 8) allowing users to simulate uncertain scenarios. A
particularly challenging development was to enable the computation of
general equilibria in a multi-regional setting, since doing so required
a methodology beyond simple optimization (chapter 12).

Increasingly as TIMES benefitted from many enhancements and gained
prominence in the community of modellers, and while some features found
their way into the MARKAL model, in order to provide similar
capabilities to the large existing MARKAL user base, ETSAP decided that
there would be no further development of MARKAL though support would
continue to be provided to the existing users. By the early 2010\'s,
TIMES (and MARKAL) models were recognized as major contributors within
the community of energy and climate change researchers, and the number
of outreach projects increased tremendously. Today it is estimated that
MARKAL/TIMES has been introduced to well over 300 institutions in more
than 80 countries, and is generally considered the benchmark integrated
energy system optimization platform available for use around the world.

## A comparison of the TIMES and MARKAL models

This section contains a point-by-point comparison of highlights of the
TIMES and MARKAL models. It is of interest primarily to modelers already
familiar with MARKAL, and to provide a sense of the advancements
embodied in TIMES. The descriptions of the features given below are not
detailed, since they are repeated elsewhere in the documentation of both
models. Rather, the function of this section is to guide the reader, by
mentioning the features that are present or improved in one model that
are not found or only in a simplified form in the other.

### Similarities

The TIMES and the MARKAL models share the same basic modeling paradigm.
Both models are technology explicit, dynamic partial equilibrium models
of energy markets[^45]. In both cases the equilibrium is obtained by
maximizing the total surplus of consumers and suppliers via Linear
Programming, while minimizing total discounted energy system cost. Both
models are by default clairvoyant, that is, they optimize over the
entire modeling horizon, though partial look-ahead (or myopic) may also
be employed. The two models also share the multi-regional feature, which
allows the modeler to construct geographically integrated (even global)
instances, though in MARKAL there are no inter-regional exchange process
making the representation of trade (much) more cumbersome. These
fundamental features were described in Chapter 3 of this documentation,
and Section 1.3, PART I of the MARKAL documentation, and constitute the
backbone of the common paradigm. However, there are also significant
differences in the two models, which we now outline. These differences
do not affect the basic paradigm common to the two models, but rather
some of their technical features and properties.

### TIMES features not in MARKAL

#### Variable length time periods

MARKAL has fixed length time periods, whereas TIMES allows the user to
define period lengths in a completely flexible way. This is a major
model difference, which indeed required a complete re-definition of the
mathematics of most TIMES constraints and of the TIMES objective
function. The variable period length feature is very useful in two
instances: first if the user wishes to use a single year as initial
period (quite useful for calibration purposes), and second when the user
contemplates long horizons, where the first few periods may be described
in some detail by relatively short periods (say 5 years), while the
longer term may be regrouped into a few periods with long durations
(perhaps 20 or more years).

#### Data decoupling 

This somewhat misunderstood feature does not confer additional power to
TIMES, but it greatly simplifies the maintenance of the model database
and allows the user great flexibility in modifying the new definition of
the planning horizon. In TIMES all input data are specified by the user
independently from the definition of the time periods employed for a
particular model run. All time-dependent input data are specified by the
year in which the data applies. The model then takes care of matching
the data with the periods, wherever required. If necessary the data is
interpolated (or extrapolated) by the model preprocessor code to provide
data points at those time periods required for the current model run. In
addition, the user has control over the interpolation and extrapolation
of each time series.

The general rule of data decoupling applies also to past data: whereas
in MARKAL the user had to provide the residual capacity profiles for all
existing technologies in the initial period, and over the periods in
which the capacity remains available, in TIMES the user may provide
technical and cost data at those past years when the investments
actually took place, and the model takes care of calculating how much
capacity remains in the various modeling periods. Thus, past and future
data are treated essentially in the same manner in TIMES.

One instance when the data decoupling feature immensely simplifies model
management is when the user wishes to change the initial period, and/or
the lengths of the periods. In TIMES, there is essentially nothing to
do, except declaring the dates of the new periods. In MARKAL, such a
change represents a much larger effort requiring a substantive revision
of the database.

#### Flexible time slices and storage processes

In MARKAL, only two commodities have time-slices: electricity and low
temperature heat, with electricity having seasonal and day/night
time-slices, and heat having seasonal time-slices. In TIMES, any
commodity and process may have its own, user-chosen time-slices. These
flexible time-slices are segregated into three groups, seasonal (or
monthly), weekly (weekday vs. weekend), and daily (day/night or hourly),
where any level may be expanded (contracted) or omitted.

The flexible nature of the TIMES time-slices supports storage processes
that 'consume' commodities at one time-slice and release them at
another. MARKAL only supports night-to-day (electricity) storage.

Note that many TIMES parameters may be time-slice dependent (such as
availability factor (AF), basic efficiency (ACT_EFF), etc.

#### Process generality

In MARKAL processes in different RES sectors are endowed with different
(data and mathematical) properties. For instance, end-use processes do
not have activity variables (activity is then equated to capacity), and
resource processes have no investment variables. In TIMES, all processes
have the same basic features, which are activated or not solely via data
specification, with some additional special features relevant to trade
and storage processes.

#### Flexible processes

In MARKAL processes are by definition rigid, except for some specialized
processes which permit flexible output (such as limit refineries or
pass-out turbine CHPs), and thus outputs and inputs are in fixed
proportions with one another. In TIMES, the situation is reversed, and
each process starts by being entirely flexible, unless the user
specifies certain attributes to rigidly link inputs to outputs. This
feature permits better modeling of many real-life processes as a single
technology, where MARKAL may require several technologies (as well as
dummy commodities) to achieve the same result. A typical example is that
of a boiler that accepts any of 3 fuels as input, but whose efficiency
depends on the fuel used. In MARKAL, to model this situation requires
four processes (one per possible fuel plus one that carries the
investment cost and other parameters), plus one dummy fuel representing
the output of the three "blending" process. In TIMES one process is
sufficient, and no dummy fuel is required. Note also that TIMES has a
number of parameters that can limit the input share of each fuel,
whereas in MARKAL, imposing such limits requires that several user
constraints be defined.[^46]

#### Investment and dismantling lead-times and costs

New TIMES parameters allow the user to model the construction phase and
dismantling of facilities that have reached their end-of-life. These
are: lead times attached to the construction or to the dismantling of
facilities, capital costs for dismantling, and surveillance costs during
dismantling. Like in MARKAL, there is also the possibility to define
flows of commodities consumed at construction time, or released at
dismantling times, thus allowing the representation of life-cycle energy
and emission accounting.

#### Vintaged processes and age-dependent parameters

The variables associated with user declared vintaged processes employ
both the time period *p* and vintage period *v* (in which new
investments are made and associated input data is obtained). The user
indicates that a process is to be modeled as a vintaged process by using
a special vintage parameter. Note that in MARKAL vintaging is possible
only for end-use devices (for which there is no activity variable) and
only applies to the device efficiency (and investment cost, which is
always vintaged by definition for all technologies) or via the
definition of several replicas of a process, each replica being a
different vintage. In TIMES, the same process name is used for all
vintages of the same process.[^47]

In addition, some parameters may be specified to have different values
according to the age of the process. In the current version of TIMES,
these parameters include the availability factors, the in/out flow
ratios (equivalent to efficiencies), and the fixed cost parameters only.
Several other parameters could, in principle, be defined to be
age-dependent, but such extensions have not been implemented yet.

#### Commodity related variables

MARKAL has very few commodity related variables, namely exports/imports,
and emissions. TIMES has a large number of commodity-related variables
such as: total production, total consumption, but also (and most
importantly) specific variables representing the flows of commodities
entering or exiting each process. These variables provide the user with
many "handles" to define bounds and costs on commodity flows, and foster
easier setup of user constraints looking to impose shares across
technology groups (e.g., renewable electricity generation targets,
maximum share of demand that can be met by a (set of) devices).

#### More accurate and realistic depiction of investment cost payments

In MARKAL each investment is assumed to be paid in its entirety at the
beginning of thetime period in which it becomes available. In TIMES the
timing of investment payments is quite detailed. For large facilities
(e.g. a nuclear plant), capital is progressively laid out in yearly
increments over the facility's construction time, and furthermore, the
payment of each increment is made in installments spread over the
economic life (which may differ from the technical lifetime) of a
facility. For small processes (e.g. a car) the capacity expansion is
assumed to occur regularly each year rather than in one large lump, and
the payments are therefore also spread over time. Furthermore, when a
time period is quite long (i.e. longer that the life of the investment),
TIMES has an automatic mechanism to repeat the investment more than once
over the period. These features allow for a much smoother (and more
realistic) representation of the stream of capital outlays in TIMES than
in MARKAL.

Moreover, in TIMES all discount rates can be defined to be
time-dependent, whereas in MARKAL both the general and
technology-specific discount rates are constant over time.

#### Stochastic Programming

Both MARKAL and TIMES support stochastic programming (SP, Chapter 8) as
a means for examining uncertainty and formulating hedging strategies to
deal with same. In MARKAL only 2-stage SP was implemented, and thus the
resolution of the uncertainty could only occur at one particular time
period, whereas in TIMES uncertainty may be resolved progressively at
different successive periods (e.g., mitigation level at

one period and demand level at another).

#### Climate module

TIMES possesses a set of variables and equations that endogenize the
concentration of CO~2~, CH4, and N2O, and also calculate the radiative
forcing and global temperature changes resulting from GHG emissions and
accumulation here. This new feature is described in Chapter 7.

# Appendix B: Linear Programming complements

This section is not strictly needed for a basic understanding of the
TIMES model and may be skipped a first reading. However, it provides
additional insight into the microeconomics of the TIMES equilibrium. In
particular, it contains a review of the theoretical foundation of Linear
Programming and Duality Theory. This knowledge may help the user to
better understand the central role shadow prices and reduced costs play
in the economics of the TIMES model. More complete treatments of Linear
Programming and Duality Theory may be found in several standard
textbooks such as Chvátal (1983) or Hillier and Lieberman (1990 and
subsequent editions). Samuelson and Nordhaus (1977) contains a treatment
of micro-economics based on mathematical programming.

## A brief primer on Linear Programming and Duality Theory

### Basic definitions

In this subsection, the superscript *t* following a vector or matrix
represents the transpose of that vector or matrix. A Linear Program may
always be represented as the following *Primal Problem* in canonical
form:

> *Max c^t^x* (14-1)

s.t. Ax ≤ b (14-2)

> *x ≥ 0* (14-3)

where *x* is a vector of *decision variables*, *c^t^x* is a linear
function representing the *objective* to maximize, and *Ax ≤ b* is a set
of inequality *constraints*. Assume that the LP has a finite optimal
solution, *x\*.*

Then each decision variable, *x\* ~j~* falls into one of three
categories. *x^\*^ ~j~* may be:

-   equal to its lower bound (as defined in a constraint), or

-   equal to its upper bound, or

-   strictly between the two bounds.

In the last case, the variable *x\* ~j\ ~*is called *basic*. Otherwise
it is *non-basic*.

For each primal problem, there corresponds a *Dual problem* derived as
follows:

*Min b^t^ y* (14-4)

s.t. A^t^y ≥ c (14-5)

y ≥ 0 (14-6)

Note that the number of dual variables equals the number of constraints
in the primal problem. In fact, each dual variable *y~i~* may be
assigned to its corresponding primal constraint, which we represent as:
*A~i~x ≤ b~i~*, where *A~i\ ~*is the *i^th\ ^*row of matrix A*.*

### Duality Theory

Duality theory consists mainly of three theorems[^48]: weak duality,
strong duality, and complementary slackness.

*Weak Duality Theorem*

If *x* is any feasible solution to the primal problem and *y* is any
feasible solution to the dual, then the following inequality holds:

> *c^t^x≤ b^t^y* (14-7)

The weak duality theorem states that the value of a feasible dual
objective is never smaller than the value of a feasible primal
objective. The difference between the two is called the *duality gap*
for the pair of feasible primal and dual solutions *(x,y).*

*Strong duality theorem*

If the primal problem has a *finite, optimal* solution *x\**, then so
does the dual problem (*y\**), and both problems have the same optimal
objective value (their duality gap is zero):

c^t^x\* = b^t^y\* (14-8)

Note that the optimal values of the dual variables are also called the
*shadow prices* of the primal constraints.

*Complementary Slackness theorem*

At an optimal solution to an LP problem:

-   If *y\*~i~* is *\> 0* then the corresponding primal constraint is
    satisfied at equality (i.e. *A~i~x\*=b~i\ ~*and the *i^th^* primal
    constraint is called *tight*. Conversely, if the *i^th^* primal
    constraint is *slack* (not tight), then *y\*~i~* = *0,*

-   If *x\*~j~* is basic, then the corresponding dual constraint is
    satisfied at equality, (i.e. *A^t^~j~\*y =c~j~*, where *A^t^~j~* is
    the *j^th^* row of *A^t^*, i.e. the *j^th^* column of *A*.
    Conversely, if the *j^th^* dual constraint is slack, then
    *x\*~j\ ~*is equal to one of its bounds.

*Remark*: Note however that a primal constraint may have zero slack and
yet have a dual equal to 0. And, a primal variable may be non basic
(i.e. be equal to one of its bounds), and yet the corresponding dual
slack be still equal to 0. These situations are different cases of the
so-called degeneracy of the LP. They often occur when constraints are
over specified (a trivial case occurs if a constraint is repeated twice
in the LP)

## Sensitivity analysis and the economic interpretation of dual variables

It may be shown that if the *j^th^* RHS *b~j~* of the primal is changed
by an infinitesimal amount *d*, and if the primal LP is solved again,
then its new optimal objective value is equal to the old optimal value
plus the quantity *y~j~\**•*d*, where *y~j~\** is the optimal dual
variable value*.*

Loosely speaking[^49], one may say that the partial derivative of the
optimal primal objective function's value with respect to the RHS of the
i^th^ primal constraint is equal to the optimal shadow price of that
constraint.

### Economic interpretation of the dual variables

If the primal problem consists of maximizing the surplus (objective
function *c^t^x*), by choosing an activity vector *x*, subject to upper
limits on several resources (the *b* vector) then:

-   Each *a~ij\ ~*coefficient of the dual problem matrix, *A,* then
    represents the consumption of resource *b~j~* by activity *x~i~*;

-   The optimal dual variable value *y\*~j\ ~*is the unit price of
    resource *j,* and

-   The total optimal surplus derived from the optimal activity vector,
    *x\*,* is equal to the total value of all resources, *b,* priced at
    the optimal dual values *y\** (strong duality theorem).

Furthermore, each dual constraint *A^t^~j~\*y≥ c~j\ ~*has an important
economic interpretation. Based on the Complementary Slackness theorem,
if an LP solution *x\** is optimal, then for each *x\* ~j~* that is not
equal to its upper or lower bound (i.e. each basic variable *x\* ~j~*),
there corresponds a *tight* dual constraint *y\*A'~j~ = c~j~*, which
means that the revenue coefficient *c~j~* must be exactly equal to the
cost of purchasing the resources needed to produce one unit of *x
~j.\ ~*In economists' terms, *marginal cost equals marginal revenue, and
both are equal to the market price of **x\* ~j~***. If a variable is not
basic, then by definition it is equal to its lower bound or to its upper
bound. In both cases, the unit revenue *c~j~* need not be equal to the
cost of the required resources. The technology is then either
non-competitive (if it is at its lower bound) or it is super competitive
and makes a surplus (if it is at its upper bound).

*Example*: The optimal dual value attached to the balance constraint of
commodity *c* represents the change in objective function value
resulting from one additional unit of the commodity. This is precisely
the internal unit price of that commodity.

### Reduced surplus and reduced cost

In a maximization problem, the difference *y\*A'~j~ - c~j~* is called
the *reduced surplus* of technology *j*, and is available from the
solution of a TIMES problem. It is a useful indicator of the
competitiveness of a technology, as follows:

-   If *x\* ~j~* is at its lower bound, its unit revenue *c~j~* is
    *less* than the resource cost (i.e. its reduced surplus is
    positive). The technology is not competitive (and stays at its lower
    bound in the equilibrium);

-   If *x\* ~j~* is at its upper bound, revenue *c~j~* is *larger* than
    the cost of resources (i.e. its reduced surplus is negative). The
    technology is super competitive and produces a surplus; and

-   If *x\* ~j\ ~*is basic, its reduced surplus is equal to 0. The
    technology is competitive but does not produce a surplus.

We now restate the above summary in the case of a Linear Program that
minimizes cost subject to constraints:

*Min c^t^x*

s.t. Ax ≥ b

x ≥ 0

In a minimization problem (such as the usual formulation of TIMES), the
difference *c~j~ - y\*A'~j\ ~*is called the *reduced cost* of technology
*j.* The following holds:

-   If *x\* ~j~* is at its lower bound, its unit cost *c~j~* is *larger*
    than the value created (i.e. its reduced cost is positive). The
    technology is not competitive (and stays at its lower bound in the
    equilibrium);

-   if *x\* ~j~* is at its upper bound, its cost *c~j~* is *less* than
    the value created (i.e. its reduced cost is negative). The
    technology is super competitive and produces a profit; and

-   if *x\* ~j\ ~*is basic, its reduced cost is equal to 0. The
    technology is competitive but does not produce a profit

The reduced costs/surpluses may thus be used to rank all technologies,
*including those that are not selected by the model.*

# References

Altdorfer, F., (1981) , \"Introduction of price elasticities on energy
demand in MARKAL\", *Memorandum No 345, KFA*, Julich, July 1981.

Barreto, L. (2001), "Technological Learning in Energy Optimization
Models and the Deployment of Emerging Technologies", *Ph.D. Thesis No
14151, Swiss Federal Institute of Technology Zurich (ETHZ)*. Zurich,
Switzerland.

Berger, C., R. Dubois, A. Haurie, E. Lessard, R. Loulou, and J.-Ph.
Waaub (1992), \"Canadian MARKAL: an Advanced Linear Programming System
for Energy and Environment Modelling\", *INFOR*, Vol. 20, 114-125, 1992.

Birge, J. R., and Rosa, C. H. (1996), "Incorporating Investment
Uncertainty into Greenhouse Policy Models," *The Energy Journal*, 17/1,
79-90.

Brooke, A, D. Kendrick, A. Meeraus, and R. Raman, 1998, *The Solver
Manual of the GAMS: A USER\'S GUIDE*, December 1998.

Chen, K., M. Crucini (2012), \"Comparing General and Partial Equilibrium
Approaches to the Study of Real Business Cycles\", *Vanderbilt
University Research paper,* June 2012 (kan.chen@vanderbilt.edu,
<mario.crucini@vanderbilt.edu>)

Chvátal, V. (1983), *Linear Programming*, Freeman and Co, New-York, 1983

Clarke, L., J. Edmonds , V. Krey, R.Richels, S. Rose, M. Tavoni (2009),
"International climate policy architectures: Overview of the EMF 22
International Scenarios", *Energy Economics* **31**, S64--S81

Dantzig, G.B. (1963), *Linear programming and Extensions*, Princeton
University Press, Princeton, New-Jersey, 1963.

de Walque, G., F. Smets, and R. Wouters (2005), "An Estimated
Two-Country DSGE Model for the Euro Area and the US Economy," *Technical
Report*, European Central Bank, 2005.

Dorfman, R., P.A. Samuelson, and R.M. Solow (1987 reprint), *Linear
programming and Economic Analysis*, McGraw-Hill, New-York, 1958-1987.

Drouet L., Edwards N.R. and A. Haurie (2004), "Coupling Climate and
Economic Models in a Cost-Benefit Framework: A Convex Optimization
Approach". Environmental Modeling and Assessment.

Edmonds, J.A., H.M. Pitcher, D. Barns, R. Baron, and M.A. Wise (1991),
\"Modelling future greenhouse gas emissions: The second generation model
description\", in *Modelling global change*, L.R. Klein and Fu-Chen Lo
eds, United Nations University Press, Tokyo-New-York-Paris, 1991,
292-362.

European Commission, *The GEM-E3 Model*, *General Equilibrium Model for
Economy, Energy and Environment,*
<https://ec.europa.eu/jrc/en/gem-e3/model>.

Fankhauser, S. (1994), \"The social cost of GHG emissions: an expected
value approach\", *Energy Journal 15/2*, 157-184.

Fishbone L G, Giesen G, Hymmen H A, Stocks M, Vos H, Wilde, D, Zoelcher
R, Balzer C, and Abilock H. (1983), "Users Guide for MARKAL: A
Multi-period, Linear Programming Model for Energy Systems Analysis",
*BNL Upton, NY, and KFA, Julich, Germany*, BNL 51701.

Fishbone, L.G., and H. Abilock (1981), \"MARKAL, A Linear Programming
Model for Energy Systems Analysis: Technical Description of the BNL
Version\", *International Journal of Energy Research*, Vol. 5, 353-375.

Fragnière, E. and Haurie, A. (1996), \"MARKAL-Geneva: A Model to Assess
Energy-Environment Choices for a Swiss Canton\", in C. Carraro and A.
Haurie (eds.), *Operations Research and Environmental Management*,
Kluwer Academic Books.

Gale, D. (1989), *The Theory of Linear Economic Models*, McGraw-Hill,
New-York, 1960, 11^th^ edition Feb. 10 1989

Gerking. H., and Voss, A. (1986), "An Approach on How to Handle
Incomplete Foresight in Linear Programming Models*," International
Conference on Models and Uncertainty in the Energy Sector*, Risö
National Laboratory, Denmark, 11-12 February, 1986, p. 145.

G. Goldstein, G., 1991, "PC-MARKAL and the MARKAL User's Support System
(MUSS)", BNL 46319, April 1991

Gorenstin, B. G. et al. (1993), "Power System Expansion Planning Under
Uncertainty," *IEEE Transactions on Power Systems*, **8**, 1, pp
129-136.

Grubb, M., (1993), \"Policy Modelling for Climate Change: The Missing
Models,\" *Energy Policy*, 21, 3, pp 203-208.

Hillier, F. S, and G. L. Lieberman (1990), *Introduction to Operations
Research, Fifth Edition,* McGraw-Hill, New-York, 1990.

Hogan, W.W., (1975), \"Energy Policy Models for Project Independence\",
*Computers and Operations Research,* 2, 251-271.

IPCC, 1996, Climatic change (1995): The Science of Climate Change.
Intergovernmental Panel on Climate Change, Second Assessment Report,
Working Group I. Cambridge : Cambridge University Press. pp.572.

IPCC, 2001, *Climatic change 2001: The Scientific Basis,*
Intergovernmental Panel on Climate Change, Third Assessment Report,
Working Group I.

IPCC, 2007, *Climate Change, Fourth Assessment Report, WG III:
Mitigation*, B. Metz, O. Davidson, P. Bosch, R. Dave, L. Meyer, editors,
Cambridge : Cambridge.

Jaccard, M., J. Nyboer, C. Bataille, and B. Sadownik (2003). \"Modelling
the Cost of Climate Policy: Distinguishing between alternative cost
definitions and long-run cost dynamics*.\" Energy Journal* 24(1): 49-73.

Johansen, Leif (1960), *A Multi-Sectoral Study of Economic Growth,*
North-Holland (2nd enlarged edition 1974).

Kanudia, A., [R.
Gerboni](http://www.emeraldinsight.com/action/doSearch?ContribStored=Gerboni%2C+R), [R.
Loulou](http://www.emeraldinsight.com/action/doSearch?ContribStored=Loulou%2C+R), [M.
Gargiulo](http://www.emeraldinsight.com/action/doSearch?ContribStored=Gargiulo%2C+M), [M.
Labriet](http://www.emeraldinsight.com/action/doSearch?ContribStored=Labriet%2C+M), [E.
Lavagno](http://www.emeraldinsight.com/action/doSearch?ContribStored=Lavagno%2C+E), [R.
De
Miglio](http://www.emeraldinsight.com/action/doSearch?ContribStored=de+Miglio%2C+R),
[L.Schranz](http://www.emeraldinsight.com/action/doSearch?ContribStored=Schranz%2C+L), [G.
C.
Tosato](http://www.emeraldinsight.com/action/doSearch?ContribStored=Tosato%2C+G),
"[Modelling EU‐GCC energy systems and trade corridors: Long term
sustainable, clean and secure
scenarios](http://www.emeraldinsight.com/doi/full/10.1108/IJESM-01-2012-0007)*",
International Journal of Energy Management*, **7**, 2, 2013, 243 -- 268.

Kanudia, A., and R. Loulou, "Robust Responses to Climate Change via
Stochastic MARKAL: the case of Québec", *European Journal of Operations
Research*, vol. 106, pp. 15-30, 1998

Kunsch, P. L. and Teghem, J., Jr. (1987), \"Nuclear Fuel Cycle
Optimization Using Multi-Objective Stochastic Linear Programming,\"
*European Journal of Operations Research 31/2*, 240-249.

Kypreos, S. (2006), An Algorithm to Decompose the Global MARKAL-MACRO
(GMM) and TIMES Models, Internal document for ETSAP, Paul Scherrer
Institut.

Kypreos, S., and A. Lehtila, 2013, \"TIMES-Macro: Decomposition into
Hard-Linked\
LP and NLP Problems\", Technical note,
<http://www.etsap.org/documentation.asp>.

Larsson, T. and Wene, C.-O. (1993), \"Developing Strategies for Robust
Energy Systems. I: Methodology,\" *International Journal of Energy
Research 17*, 503-513.

Larsson, T. (1993), \"Developing Strategies for Robust Energy Systems.
II: Application to CO~2~ Risk Management,\" *International Journal of
Energy Research 17*, 505-535.

Loulou, R., and A. Kanudia (1999), "Minimax Regret Strategies for
Greenhouse Gas Abatement: Methodology and Application", *Operations
Research Letters,* 25, 219-230, 1999.

Loulou, R. and A. Kanudia (2000), "Using Advanced Technology-rich models
for Regional and Global Economic Analysis of GHG Mitigation", in
*Decision and Control: Essays in honor of Alain Haurie,* G. Zaccour ed.,
Kluwer Academic Publishers, Norwell, USA, pp.153-175, 2000. A condensed
version of this article was published electronically in the *Proceedings
of the International Energy Agency International conference on Climate
Change Modelling and Analysis*, held in Washington DC, June15-17, 1999.

Loulou, R., Goldstein, G. & Noble, K. (2004), Documentation for the
MARKAL Family of Models: Part II -- MARKAL-MACRO. October 2004.
<http://www.etsap.org/documentation.asp>

Loulou, R., and M. Labriet (2007), "ETSAP-TIAM: The TIMES Integrated
Assessment Model \--Part I: Model Structure", *Computational Management
Science special issue on Energy and Environment*, Vol. 5, No 1-2, pp.
7-40.

Loulou, R., M. Labriet, A. Haurie, A. Kanudia, 2007, "OPEC Oil Pricing
Strategies in a Climate Regime: a Two-Level Optimization Approach in an
Integrated Assessment Model", special report for the ERMITAGE Project,
European Commission.

Loulou, R., (2007), "ETSAP-TIAM: The TIMES Integrated Assessment Model
\--Part II: Mathematical Formulation", *Computational Management Science
special issue on Energy and Environment* , Vol. 5, No 1-2, pp. 41-66

Loulou, R., and Lavigne, D. (1996), "MARKAL Model with Elastic Demands:
Application to GHG Emission Control", in *Operations Research and
Environmental Engineering*, C. Carraro and A. Haurie eds., Kluwer
Academic Publishers, Dordrecht, Boston, London, 1996, pp. 201-220.

Manne, A. S., (1977), \"ETA-MACRO: A model of energy-economy
interactions\"*NASA STI/Recon Technical Report N 11/1977*; 78:26612,
Stanford Univ., CA.

Manne, A.S., (1999),"Greenhouse gas abatement: toward Pareto-optimality
in integrated assessment". In: Arrow KJ, Cottle RW, Eaves BC, Olkin I
(eds) *Education in a research university*. Springer, Dordrecht

Manne, A., Mendelsohn, R. and Richels, R. (1995), \"MERGE: a Model for
Evaluating Regional and Global Effects of GHG Reduction Policies\",
*Energy Policy* 23 (1), 17-34.

Manne, A.S., and Wene, C-O. (1992), \"MARKAL-MACRO: A Linked Model for
Energy-Economy Analysis\", *BNL-47161 report, Brookhaven National
Laboratory*, Upton, New-York, February 1992.

Meade, D. (1996) "LIFT User's Guide", Technical report, INFORUM, IERF,
College Park, Maryland (July 1996).

Messner, S. and Strubegger, M. (1995*), User's Guide for MESSAGE III*,
WP-95-69, IIASA, Luxembourg, Austria.

Moomaw, W.R. and J.R. Moreira (2001)," Technological and Economic
Potential of Greenhouse Greenhouse Gas Emissions Reduction". In *Climate
Change 2001: Mitigation*, edited by Metz, B., Davidson, O., Swart, R.
and J. Pan, Intergovernmental Panel on Climate Change (IPCC*), Third
Assessment Report*, Working Group III, p.167-299. Cambridge : Cambridge
University Press.

Nakicenovic, N. (ed.) (2000), Special Report on Emissions Scenarios. A
Special Report of Working III of the Intergovernmental Panel on Climate
Change.Cambridge : Cambridge University Press, p.599.

Negishi, T. (1960), \"Welfare eoconomics and existence of an equilibrium
for a competitive economy\", *Metroeconomic*a, [12, 
2-3, ](http://onlinelibrary.wiley.com/doi/10.1111/meca.1960.12.issue-2-3/issuetoc)pp.
92--97, June 1960.

Nemhauser, G.L., A.H.G. Rinnooy Kan, and M.J. Todd editors (1989),
*Handbooks in Operations Research and Management Science*, *Vol I:
Optimization*, North-Holland, 1989.

Noble-Soft Systems, 2009, "ANSWERv6-TIMES User Manual", March 2009

Nordhaus, W. (1993), \"Rolling the DICE: an optimal transition path for
controlling GHG\'s\", *Resources and Energy Economics 15/1*, 27‑50.

Nordhaus, W. D. and J. Boyer (1999), Roll the DICE Again: Economic
Models of Global Warming. Yale University, manuscript edition.

Papadimitriou, C.H., and K. Steiglitz (1982), *Combinatorial
Optimization \-- Algorithms and Complexity*, Prentice-Hall, New-Jersey,
1982.

Peck, S. C., and Teisberg,T. J. (1995), "Optimal CO2 Control Policy with
Stochastic Losses from Temperature Rise," *Climatic change*, 31/1,
19-34.

Raiffa, H. (1968), *Decision Analysis*, Addison-Wesley, Reading, Mass.,
1968

Remme, U. & Blesl, M. (2006), *Documentation of the TIMES-MACRO model*.
Energy Technology Systems Analysis Programme (ETSAP), February 2006.
<http://www.etsap.org/documentation.asp>

Rockafellar, R. T., (1970), *Convex Analysis*, Princeton University
Press, Princeton, New-Jersey, 1970

Rutherford, Thomas F. (1992), "Sequential Joint Maximization",
Discussion Papers in Economics -- 92-08; Boulder, University of
Colorado, September 1992.

Samuelson, P.A. (1952), \"Spatial Price Equilibrium and Linear
Programming\", *American Economic Review*, 42, 283-303, 1952.

Samuelson, P.A., and W. Nordhaus (1977), *Economics (17th edition)*,
John Wiley, 1977

Schrijver, A. (1986), *Theory of Linear and Integer Programming* , John
Wiley and Sons.

Smets, F. and R. Wouters (2007), "Shocks and Frictions in US Business
Cycles: a Bayesian DSGE Approach." *American Economic Review*
**97**(3):586--606.

Stanton E. (2010), \"Negishi welfare weights in integrated assessment
models: the mathematics of global inequality\", Climatic Change,
published first online December 16, 2010.

Takayama, T., and Judge G.G. (1971), *Spatial and Temporal Price and
Allocation Models*, North Holland, Amsterdam, 1971.

Tosato, G.C. (1980), \"Extreme Scenarios in MARKAL LP Model: use of
Demand Elasticity\", presented at the *5th Italian-Polish Symposium on
Applications of Systems Theory to Economics and Technology*, Torun, June
11-16 1980.

U.S. Energy Information Administration, 2000,
<http://pubsonline.informs.org/doi/pdf/10.1287/opre.49.1.14.11195>

U.S. Department of Energy/Energy Information Administration, US
Government (2000), \"The National Energy Modeling System: An overview
(2000)\", *DOE/EIA-0581*, Washington. DC, March 2000.

U.S. Energy Information Administration (2002), *System for the Analysis
of Global Energy Markets (SAGE)*, US Dept of Energy.

Van Regemorter, D., 1998, "Development of MARKAL Towards a Partial
Equilibrium Model", ETSAP, December 1998

Voort, E. van der, Donni, E., Thonet, C., Bois d\'Enghien, E., Dechamps,
C. & Guilmot, J.F. (1984), *Energy Supply Modelling Package EFOM-12C
Mark I, Mathematical description*. Louvain-la-Neuve, Cabay: Commission
of the European Communities, EUR-8896.

Weistroffer, H. R., Smith, C. H., and Narula, S. C., 2005, \"Multiple
criteria decision support software\", Ch 24 in: Figueira, J., Greco, S.,
and Ehrgott, M., eds, *Multiple Criteria Decision Analysis: State of the
Art Surveys Series*, Springer: New York, 2005

Wets, R. J. B. (1989), 'Stochastic Programming'. In: Nemhauser George
L., Rinnooy Kan, Alexander, H.G., Todd Michael J. (eds.) *Handbooks in
OR and MS Vol. 1*, Elsevier Science Publishers, Amsterdam.

Wigley, T.M.L., Solomon, M. and S.C.B. Raper(1994), *Model for the
Assessment of Greenhouse-Gas Induced Climate Change. Version 1.2.*
Climate Research Unit, University of East Anglia, UK.

[^1]: MARKAL (MARket ALlocation model, Fishbone et al, 1981, 1983,
    Berger et al. 1992) and EFOM (Van Voort et al, 1984) are two
    bottom-up energy models that inspired the structure of TIMES.

[^2]: European Commission, *The GEM-E3 Model*, *General Equilibrium
    Model for Economy, Energy and Environment,*
    <https://ec.europa.eu/jrc/en/gem-e3/model>.

[^3]: This standard may also be imposed on the entire electricity
    generation sector, in which case renewable electricity plants are
    assumed to have zero energy input.

[^4]: However, there are TIMES variants -- discussed in chapters 8 to
    12, that depart significantly from these assumptions

[^5]: There are exceptional cases when an investment must be repeated
    more than once in a period, namely when the period is so long that
    it exceeds the technical life of the investment. These cases are
    described in detail in section 6.2.2 of PART II.

[^6]: However, if the horizon has been lengthened beyond the years
    already covered by the data, additional data for the new years at
    the end of the horizon must of course be provided.

[^7]: Data in this context refers to parameter assumptions, technology
    characteristics, projections of energy service demands, etc. It does
    not refer to historical data series.

[^8]: There are a variety of availability factors: annual or seasonal.
    Each may be specified as a maximum factor (the most frequent case),
    an exact factor, or even a minimum factor (in order to force some
    minimum utilization of the capacity of some equipment, as in a
    backup gas turbine for instance).

[^9]: Vintaging could also be introduced by defining a new technology
    for each vintage year, but this approach would be wasteful, as many
    parameters remain the same across all vintages.

[^10]: See Appendix A for the VEDA-FE, VEDA-BE, and ANSWER modeling and
    analysis systems, used to maintain and manage TIMES databases,
    conduct model runs, and organize results.

[^11]: These models assume that the relationships (as defined by the
    form of the production functions as well as the calculated
    parameters) between sector level inputs and outputs are in
    equilibrium in the base year.

[^12]: Most models use inputs such as labor, energy, and capital, but
    other input factors may conceivably be added, such as arable land,
    water, or even technical know-how. Similarly, labor may be further
    subdivided into several categories.

[^13]: Model for Evaluating Regional and Global Effects (Manne et al.,
    1995)

[^14]: Second Generation Model (Edmonds et al., 1991)

[^15]: It has been argued, based on strong experimental evidence, that
    the change in demands for energy services indeed captures the main
    economic impact of energy system policies on the economy at large
    (Loulou and Kanudia, 2000)

[^16]: This property does not hold in three TIMES extensions presented
    in Chapters 10-12.

[^17]: These two properties do not hold in the time-stepped extension of
    TIMES (chapter 9) and in Stochastic TIMES (Chapter 8.)

[^18]: This is so because in Linear Programming the shadow price of a
    constraint remains constant over a certain interval, and then
    changes abruptly, giving rise to a stepwise constant functional
    shape.

[^19]: This smooth curve will be discretized later for computational
    purposes, and thus become a staircase function, as described in
    section 4.2

[^20]: As may be seen in figure 3.1, the equilibrium is not necessarily
    unique. In the case shown, any point on the vertical segment
    containing the equilibrium is also an equilibrium, with the same
    quantity Q~E~ but a different price. In other situations, the
    multiple equilibria may have a single price but multiple quantities.

[^21]: This results from the fact that in TIMES each price ***P~i~***is
    the shadow price of a balance constraint (see section 5.4.4), and
    may thus be (loosely) expressed as the derivative of the objective
    function ***F*** with respect to the right-hand-side of a balance
    constraint, i.e. ![](media/image4.wmf). When that price is further
    differentiated with respect to another quantity ***Q~j~***, one gets
    ![](media/image5.wmf), which, under mild conditions is always equal
    to ![](media/image6.wmf), as desired.

[^22]: See e.g. Samuelson and Nordhaus (1977)

[^23]: The term *shadow price* is often used in the mathematical
    economics literature, whenever the price is derived from the
    marginal value of a commodity. The qualifier 'shadow' is used to
    distinguish the competitive market price from the price observed in
    the real world, which may be different, as is the case in regulated
    industries or in sectors where either consumers or producers
    exercise market power, or again when other market imperfections
    exist. When the equilibrium is computed using LP optimization, as is
    the case for TIMES, the shadow price of each commodity is computed
    as the dual variable of that commodity's balance constraint, see
    chapter 14

[^24]: However, the resulting Linear Program has multiple optimal
    solutions. Therefore, although *q*\* is an optimal solution, it is
    not necessarily the one found when the modified LP is solved.

[^25]: An agent has market power if its decisions, all other things
    being equal, have an impact on the market price. Monopolies and
    oligopolies are example of markets where one or several agents have
    market power.

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

[^32]: Other important GHG's such as CH4 and N2O may either be expressed
    in CO2-equivalent, or a special exogenous forcing term may be added
    to CO2 forcing. The latter approach is not attractive as it keeps
    two major GHG's fully exogenous.

[^33]: In keeping with the literature, we have expressed all
    concentrations as masses in megatonnes.

[^34]: Note that the subscripts *atm* and *up*, which for the CO2
    equations referred to the atmosphere and upper reservoirs, have been
    reused for the CH4 and N2O equations to stand for anthropogenic and
    natural concentrations.

[^35]: The expected prices become deterministic prices if the stage is
    the last one, so that there is no uncertainty remaining at or after
    the current period.

[^36]: A TIMES LP program of a given size tends to have fairly constant
    solution time, even if the database is modified. In contrast, a
    TIMES MIP may show some erratic solution times. One may observe
    reasonable solution times (although significantly longer than LP
    solution times) for most instances, with an occasional *very* long
    solution time for some instances. This phenomenon is predicted by
    the theory of complexity as applied to MIP, see Papadimitriou and
    Stieglitz (1982).

[^37]: The notation in this chapter is sometimes different from the
    standard notation for parameters and variables, in order to conform
    to the more detailed technical note on the subject.

[^38]: It is usual to define, instead of ***b***, another parameter,
    ***pr*** called the *progress ratio*, which is related to ***b***
    via the following relationship:![](media/image25.wmf). Hence,
    ***1-pr*** is the cost reduction incurred when cumulative investment
    is doubled. Typical observed ***pr*** values are in a range of .75
    to .95.

[^39]: The concrete implementation in the TIMES-MACRO model differs in
    some points, e.g. the consumption variable in the utility function
    is substituted by equations (12-2) and (12-3).

[^40]: A production function is called homogenous of degree *r*, if
    multiplying all production factors by a constant scalar leads
    ![](media/image33.wmf)to an increase of the function
    by![](media/image34.wmf). If *r*= 1, the production function is
    called linearly homogenous and leads to constant returns to scale.

[^41]: Of course, if no trade between the regions is assumed, the global
    equilibrium amounts to a series of independent national equilibria,
    which may be calculated by the single region TIMES-MACRO.

[^42]: It may be desirable, although not required to use non-zero demand
    elasticities at the very first iteration.

[^43]: With the kind permission of Professor Stephen Hawking

[^44]: A product of Haverly Systems Incorporated,
    http://www.haverly.com/.

[^45]: But recall that some extensions depart from the classical
    equilibrium properties, see chapters 8-12.

[^46]: In the end the two models use equivalent mathematical expressions
    to represent a flexible process. However, TIMES reduces the user's
    effort to a minimum, while MARKAL requires the user to manually
    define the multiple processes, dummy fuels and user constraints.

[^47]: The representation of vintage as a separate index helps eliminate
    a common confusion that existed in MARKAL, namely the confusion of
    *vintage* with the *age* of a process. For instance, if the user
    defines in MARKAL an annual O&M cost for a car, equal to 10 in 2005
    and only 8 in 2010, the decrease would not only apply to cars
    purchased in 2010, but also to cars purchased in 2005 and earlier
    when they reach the 2010 period.

[^48]: Their proofs may be found in the textbooks on Linear Programming
    already referenced.

[^49]: Strictly speaking, the partial derivative may not exist for some
    values of the RHS, and may then be replaced by a directional
    derivative (see Rockafellar 1970).
