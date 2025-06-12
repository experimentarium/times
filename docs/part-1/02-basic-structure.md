# The basic structure of the core TIMES model

## The TIMES economy

The TIMES energy economy is made up of producers and consumers of *commodities* such as energy carriers, materials, energy services, and emissions. By default, TIMES assumes competitive markets for all commodities, unless the modeler voluntarily imposes regulatory or other constraints on some parts of the energy system, in which case the equilibrium is (partially) regulated. The result is a supply-demand equilibrium that maximizes the *net total surplus* (i.e. the sum of producers' and consumers' surpluses) as fully discussed in chapters 3 and 4. TIMES may however depart from perfectly competitive market assumptions by the introduction of user-defined explicit constraints, such as limits to technological penetration, constraints on emissions, exogenous oil price, etc. Market imperfections can also be introduced in the form of taxes, subsidies and hurdle rates.

While computing the equilibrium, a TIMES run configures the *energy system* of a *set of regions*, over a certain *time horizon,* in such a way as to *minimize the net total cost* (or equivalently *maximize the net total surplus*) of the system, while satisfying a number of *constraints*. TIMES is run in a dynamic manner, which is to say that all investment decisions are made in each period with full knowledge of future events. The model is said to have *perfect foresight*[^4] (or to be *clairvoyant*). The next subsection describes in detail the time dimension of the model.

## Time horizon

The time horizon is divided into a user-chosen number of time-periods, each period containing a (possibly different) number of years.

In the standard version of TIMES each year in a given period is considered identical, except for the cost objective function which differentiates between payments in each year of a period. For all other quantities (capacities, commodity flows, operating levels, etc.) any model input or output related to period ***t*** applies to each of the years in that period, with the exception of investment variables, which are usually made only once in a period[^5].

Another version of TIMES is available, in which the TIMES variables (capacities and flows) are defined at some year in the midst of each period (called milestone year), and are assumed to evolve linearly between the successive milestone years. This option emulates that of the EFOM model and is discussed in section 5.5.

The initial period is usually considered a past period, over which the model has no freedom, and for which the quantities of interest are all fixed by the user at their historical values. It is often advisable to choose an initial period consisting of a single year, in order to facilitate calibration to standard energy statistics. Calibration to the initial period is one of the more important tasks required when setting up a TIMES model. The main variables to be calibrated are: the capacities and operating levels of all technologies, as well as the extracted, exported, imported, produced, and consumed quantities for all energy carriers, and the emissions if modeled.

In TIMES, years preceding the first period also play a role. Although no explicit variables are defined for these years, data may be provided by the modeler on past investments. Note carefully that the specification of past investments influences not only the initial period's calibration, but also partially determines the model's behavior over several future periods, since the past investments provide residual capacity in several years within the modeling horizon proper.

In addition to time-periods (which may be of variable length), there are time divisions within a year, also called *time-slices,* which may be defined at will by the user (see {numref}`p1-timeslice-tree`). For instance, the user may want to define seasons, portions of the day/night, and/or weekdays/weekends. Time-slices are especially important whenever the mode and cost of production of an energy carrier at different times of the year are significantly different. This is the case for instance when the some energy commodity is expensive to store so that the matching of production and consumption of that commodity is itself an issue to be resolved by the model. The production technologies for the commodity may themselves have different characteristics depending on the time of year (e.g. wind turbines or run-of-the-river hydro plants). In such cases, the matching of supply and demand requires that the activities of the technologies producing and consuming the commodity be tracked for each time slice. Examples of commodities requiring time-slicing may include electricity, district heat, natural gas, industrial steam, and hydrogen.

An additional reason for defining sub yearly time slices is the requirement of an expensive infrastructure whose capacity should be sufficient to allow the peak demand for the commodity to be satisfied. Technologies that store a commodity in one time slice, at a cost, for discharge in another time slice, may also be defined and modeled.

The net result of these conditions is that the deployment in time of the various production technologies may be very different in different time slices, and furthermore that specific investment decisions will be taken to insure adequate reserve capacity at peak.

```{figure} ../assets/timeslice-tree-example.svg
:name: p1-timeslice-tree

Example of a time-slice tree.
```

## Decoupling of data and model horizon

In TIMES, special efforts have been made to decouple the specification of data from the definition of the time periods for which a model is run. Two TIMES features facilitate this decoupling.

First, the fact that investments made in past years are recognized by TIMES makes it much easier to modify the choice of the initial and subsequent periods without major revisions of the database.

Second, the specification of process and demand input data in TIMES is made by specifying the *calendar years* when the data apply, irrespective of how the model time periods have been defined. The model then takes care of interpolating and extrapolating the data for the *periods* chosen by the modeler for a particular model run. TIMES offers a particularly rich range of interpolation/extrapolation modes adapted to each type of data and freely overridden by the user. Section 3.1.1 of Part II discusses this feature.

These two features combine to make a change in the definition of periods quite easy and error-free. For instance, if a modeler decides to change the initial year from 2010 to 2015, and perhaps change the number and durations of all other periods as well, only one type of data change is needed, namely to define the investments made from 2011 to 2015 as past investments. All other data specifications need not be altered[^6]. This feature represents a great simplification of the modeler's work. In particular, it enables the user to define time periods that have varying lengths, without changing the input data.

## The components of a Reference Energy System (RES): processes, commodities, flows

The TIMES energy economy consists of three types of entities:
- *Technologies* (also called *processes*) are representations of physical plants, vehicles, or other devices that transform some commodities into other commodities. They may be primary sources of commodities (e.g. mining processes, import processes), or transformation activities such as conversion plants that produce electricity, energy-processing plants such as refineries, or end-use demand devices such as cars and heating systems, that transform energy into a demand service;
- *Commodities* consisting of energy carriers, energy services, materials, monetary flows, and emissions. A commodity is produced by one or more processes and/or consumed by other processes; and
- *Commodity flows* are the links between processes and commodities. A flow is of the same nature as a commodity but is attached to a particular process, and represents one input or one output of that process. For instance, electricity produced by wind turbine type A at period *p*, time-slice *s*, in region *r*, is a commodity flow.

### The RES

It is helpful to picture the relationships among these various entities using a network diagram, referred to as a *Reference Energy System* (RES). In a TIMES RES, processes are represented as boxes and commodities as vertical lines. Commodity flows are represented as links between process boxes and commodity lines.

{numref}`part-view-res` depicts a small portion of a hypothetical RES containing a single energy service demand, namely residential space heating. There are three end-use space heating technologies using the gas, electricity, and heating oil energy carriers (commodities), respectively. These energy carriers in turn are produced by other technologies, represented in the diagram by one gas plant, three electricity-generating plants (gas fired, coal fired, oil fired), and one oil refinery.

```{figure} assets/res-example.svg
:name: part-view-res
:align: center

Partial view of a Reference Energy System (links are oriented left to right).
```

To complete the production chain on the primary energy side, the diagram also represents an extraction source for natural gas, an extraction source for coal, and two sources of crude oil (one extracted domestically and then transported by pipeline, and the other one imported). This simple RES has a total of 13 commodities and 13 processes. Note that in the RES every time a commodity enters/leaves a process (via a particular flow) its name is changed (e.g., wet gas becomes dry gas, crude becomes pipeline crude). This simple rule enables the inter-connections between the processes to be properly maintained throughout the network.

To organize the RES, and inform the modeling system of the nature of its components, the various technologies, commodities, and flows may be classified into *sets*. Each set regroups components of a similar nature. The entities belonging to a set are referred to as *members, items* or *elements* of that set. The same item may appear in multiple technology or commodity sets. While the topology of the RES can be represented by a multi-dimensional network, which maps the flow of the commodities to and from the various technologies, the set membership conveys the nature of the individual components and is often most relevant to post-processing (reporting) rather than influencing the model structure itself. However, the TIMES commodities are still classified into several *Major Groups*. There are five such groups: energy carriers, materials, energy services, emissions, and monetary flows. The use of these groups is essential in the definition of some TIMES constraints, as discussed in chapter 5.

### Three classes of processes

We now give a brief overview of three classes of processes that need to be distinguished.

Processes are *general processes, storage processes*, and *inter-regional trading processes* (also called *inter-regional exchange processes*). The latter two classes need to be distinguished from general processes due to their special function requiring special rules and sometimes a different set of indices.

#### General processes

In TIMES most processes are endowed with essentially the same attributes (with the exceptions of storage and inter-regional exchange processes, see below), and unless the user decides otherwise (e.g. by providing values for some attributes and ignoring others), they have the same variables attached to them, and must obey similar constraints. Therefore, the differentiation between the various species of processes (or commodities) is made through data specification only, thus eliminating the need to define specialized membership sets, unless desired for processing results. Most of the TIMES features (e.g. sub-annual time-slice resolution, vintaging) are available for all processes and the modeler chooses the features being assigned to a particular process by specifying a corresponding indicator set (e.g. PRC_TSL, PRC_VINT).

A general process receives one or more commodity inputs (inflows) and produces one or more commodity outputs (outflows) in the same time-slice, period, and region.

As already mentioned, two classes of process do not follow these rules and deserve separate descriptions, namely *storage processes* and *inter-regional exchange processes*.

#### Storage processes (class STG)

This advanced feature of TIMES allows the modeller to represent very intricate storage activities from real life energy systems. Storage processes are used to store a commodity either between periods or between time-slices in the same period. A process $p$ is specified to be an ***inter-period storage (IPS) process*** for commodity $c$, or as ***general time-slice storage (TSS)***. A special case of time-slice storage is a so-called ***night-storage device (NST)*** where the commodity for charging and the one for discharging the storage are different.

An example of a night storage device is an electric heating technology that is charged during the night using electricity and produces heat during the day. Several time-slices may be specified as charging time-slices, the non-specified time-slices are assumed to be discharging time-slices. However, when the process is an end-use process that satisfies a service demand, the discharging occurs according to the load curve of the corresponding demand, and the charging is freely optimized by TIMES across time-slices. Such an exception for demand processes only exists if the demand is at the ANNUAL level. But if the demand is not ANNUAL, discharging can only occur in the non-charging time-slices.

An example of general time-slice storage is a pumped storage reservoir, where electricity is consumed during the night to store water in a reservoir, water which is then used to activate a turbine and produce electricity at a different time-slice.

An example of an inter-period storage process is a plant that accumulates organic refuse in order to produce methane some years later.

Besides the commodity being stored, other (auxiliary) commodity flows are also permitted and may be defined in relation to the stored commodity using the FLO_FUNC and/or the ACT_FLO parameters. The activity of a storage process is interpreted as the amount of the commodity being stored in the storage process. Accordingly the capacity of a storage process describes the maximum commodity amount that can be kept in storage.

#### Inter-regional exchange processes (class IRE)

Inter-regional exchange (IRE) processes are used for trading commodities between regions. Note that the name of the traded commodity is allowed to be different in both regions, depending on the chosen commodity names in both regions. There are two types of trade in TIMES, bi-lateral or multi-lateral.

Bi-lateral trade is the most detailed way to specify trade between regions. It takes place between specific pairs of regions. A pair of regions together with an exchange process and the direction of the commodity flow is first identified, and the model ensures that trade through the exchange process is balanced between these two regions (the amount is exported from region A to region B must be imported by region B from region A, possibly adjusted for transportation losses). If trade should occur only in one direction then only that direction is provided by the proper ordinal attribute. The process capacity and the process related costs (e.g. activity costs, investment costs) of the exchange process may be described individually for both regions by specifying the corresponding parameters in each region. This allows for instance the investment cost of a trade process to be shared between regions in user chosen proportions.

There are cases when it is not important to fully specify the pair of trading regions. An example is the trading of greenhouse gas (GHG) emission permits in a global market. In such cases, the *multi-lateral trade* option decreases the size of the model. Multi-lateral trade is based on the idea that a common marketplace exists for a traded commodity with several selling and several buying regions for the commodity (e.g. GHG emission permits). To model a marketplace the user must first identify (or create) one region that participates both in the production and consumption of the traded commodity. Then a single exchange process is used to link all regions with the marketplace region. Note however that some flexibility is lost when using multilateral trade. For instance, it is not possible to express transportation costs in a fully accurate manner, if such cost depends upon the precise pair of trading regions in a specific way.

## Data-driven model structure

It is useful to distinguish between a model's *structure* and a particular *instance* of its implementation. A model's structure exemplifies its fundamental approach for representing a problem --- it does not change from one implementation to the next. All TIMES models exploit an identical underlying structure. However, because TIMES is *data*[^7] *driven*, the *effective structure* of a particular instance of a model will vary according to the data inputs. This means that some of the TIMES features will not be activated if the corresponding data is not specified. For example, in a multi-region model one region may, as a matter of user data input, have undiscovered domestic oil reserves. Accordingly, TIMES automatically generates technologies and processes that account for the cost of discovery and field development. If, alternatively, user supplied data indicate that a region does not have undiscovered oil reserves no such technologies and processes would be included in the representation of that region's Reference Energy System (RES, see section 2.4). Due to this property TIMES may also be called a *model generator* that, based on the input information provided by the modeler, generates an instance of a model. In the following, if not stated otherwise, the word \'model\' is used with two meanings indifferently: the instance of a TIMES model or more generally the model generator TIMES.

Thus, the structure of a TIMES model is ultimately defined by variables and equations created from the union of the underlying TIMES equations and the data input provided by the user. This information collectively defines each TIMES regional model database, and therefore the resulting mathematical representation of the RES for each region. The database itself contains both qualitative and quantitative data.

The *qualitative data* includes, for example, the list of commodities, and the list of those technologies that the modeler feels are applicable (to each region) over a specified time horizon. This information may be further classified into subgroups, for example commodities may include energy carriers (themselves split by type \--e.g., fossil, nuclear, renewable, etc.), materials, emissions, energy services.

*Quantitative data*, in contrast, contains the technological and economic parameter assumptions specific to each technology, region, and time period. When constructing multi-region models it is often the case that a given technology is available for use in two or more regions; however, cost and performance assumptions may be quite different. The word ***attribute*** designates both qualitative and quantitative elements of the TIMES modeling system.

## A brief overview of the TIMES attributes

Due to the data driven nature of TIMES (see section 2.5), all TIMES constraints are activated and defined by specifying some attributes. Attributes are attached to processes, to commodities, to flows, or to special variables that have been created to define new TIMES features. Indeed, TIMES has many new attributes that were not available in earlier versions, corresponding to powerful new features that confer additional modeling flexibility. The complete list of attributes is fully described in section 3 of PART II, and we provide below only succinct comments on the types of attribute attached to each entity of the RES or to the RES as a whole. Additional attribute definitions may also be included in the chapters describing new features or variants of the TIMES generator.

Attributes may be *cardinal* (numbers) or *ordinal* (lists, sets). For example, some ordinal attributes are defined for processes to describe subsets of flows that are then used to construct specific flow constraints as described in section 5.4. PART II, section 2 shows the complete list of TIMES sets.

The cardinal attributes are usually called *parameters*. We give below a brief idea of the main types of parameters available in the TIMES model generator.

### Parameters attached to processes

TIMES process-oriented parameters fall into several general categories.

#### Technical parameters

*Technical parameters* include process efficiency, availability factor(s)[^8], commodity consumptions per unit of activity, shares of fuels per unit activity, technical life of the process, construction lead time, dismantling lead-time and duration, amounts of the commodities consumed (respectively released) by the construction (respectively dismantling) of one unit of the process, and contribution to the peak equations. The efficiency, availability factors, and commodity inputs and outputs of a process may be defined in several flexible ways depending on the desired process flexibility, on the time-slice resolution chosen for the process and on the time-slice resolution of the commodities involved. Certain parameters are only relevant to special processes, such as storage processes or processes that implement trade between regions.

(economic-and-policy-parameters)=
#### Economic and policy parameters

A second class of process parameters comprises *economic and policy parameters* that include a variety of costs attached to the investment, dismantling, maintenance, and operation of a process. The investment cost of the technology is incurred once at the time of acquisition; the fixed annual cost is incurred each year per unit of the capacity of the technology, as long as the technology is kept alive (even if it is not actively functioning); the annual variable cost is incurred per unit of the activity of the technology. In addition to costs, taxes and subsidies (on investment and/or on activity) may be defined in a very flexible manner. Other economic parameters are: the economic life of a process (the time during which the investment cost of a process is amortized, which may differ from the operational lifetime) and the process specific discount rate, also called *hurdle rate*. Both these parameters serve to calculate the annualized payments on the process investment cost, which enters the expression for the total cost of the run (section 5.2).

(processes-bounds)=
#### Bounds

Another class of parameter is used to define the right-hand-side of some constraint. Such a parameter represents a ***bound*** and its specification triggers the constraint on the quantity concerned. Most frequently used bounds are those imposed on period investment, capacity, or activity of a process. Newly defined bounds allow the user to impose limits on the annual or annualized payments at some period or set of consecutive years.

A special type of bounding consists in imposing upper or lower limits on the ***growth rate*** of technologies. The most frequently quantities thus bounded are investment, capacity and activity of a process, for which a simplified formulation has been devised.

The growth constraints belong to the class of ***dynamic bounds*** that involve multiple periods. Many other dynamic bounds may be defined by the user. ***Bounds on cumulative quantities*** are also very useful. The accumulation may be over the entire horizon or over some user defined set of consecutive years. The variables on which such bounds apply may quite varied, such as: process capacity, process investment, process activity, annual or annuity payments, etc.

All bounds may be of four types: lower (LO), upper (UP), equality (FX), or neutral (N). The latter case does not introduce any restriction on the optimization, and is used only to generate a new reporting quantity.

#### Other parameters

Features that were added to TIMES over the years require new parameters. For instance, the Climate Module of TIMES (chapter 7), the Lumpy Investment feature (chapter 10), and several others. These will be alluded to in the corresponding chapters of this Part I, and more completely described in section 2 and Appendices of Part II.

An advanced feature allows the user to define certain process parameters as *vintaged* (i.e. dependent upon the date of installation of new capacity). For instance, the investment cost and fuel efficiency of a specific type of automobile will depend on the model year[^9].

Finally, another advanced TIMES feature renders some parameters dependent *also on the age* of the technology. For instance, the annual maintenance cost of an automobile could be defined to remain constant for say 3 years and then increase in a specified manner each year after the third year.

### Parameters attached to commodities

This subsection concerns parameters attached to each commodity, irrespective of how the commodity is produced or consumed. The next subsection concerns commodity flows. Commodity-oriented parameters fall into the same categories as those attached to processes.

#### Technical parameters 

*Technical parameters* associated with commodities include overall efficiency (for instance the overall electric grid efficiency), and the time-slices over which that commodity is to be tracked. For demand commodities, in addition, the annual projected demand and load curves (if the commodity has a sub-annual time-slice resolution) can be specified.

#### Economic and policy parameters 

*Economic parameters* include additional costs, taxes, and subsidies on the overall or net production of a commodity. These cost elements are then added to all other (implicit) costs of that commodity. In the case of a demand service, additional parameters define the demand curve (i.e. the relationship between the quantity of demand and its price). These parameters are: the demand's own-price elasticity, the total allowed range of variation of the demand value, and the number of steps to use for the discrete approximation of the curve.

*Policy based parameters* include bounds (at each period or cumulative over user defined years) on the gross or net production of a commodity, or on the imports or exports of a commodity by a region.

(commodities-bounds)=
#### Bounds

In TIMES the net or the total production of each commodity may be explicitly represented by a variable, if needed for imposing a bound or a tax. A similar variety of bounding parameters exists for commodities as for processes.

### Parameters attached to commodity flows

A *commodity flow* (more simply, a *flow*) is an amount of a given commodity produced or consumed by a given process. Some processes have several flows entering or leaving them, perhaps of different types (fuels, materials, demands, or emissions). In TIMES, each flow has a variable attached to it, as well as several attributes (parameters or sets).

Flow related parameters confer enormous flexibility for modeling a large spectrum of conditions.

#### Technical parameters

*Technical parameters,* along with some set attributes, permit full control over the maximum and/or minimum share a given input or output flow may take within the same commodity group. For instance, a flexible turbine may accept oil and/or gas as input, and the modeler may use a parameter to limit the share of oil to, say, at most 40% of the total fuel input. Other parameters and sets define the amount of certain outflows in relation to certain inflows (e.g., efficiency, emission rate by fuel). For instance, in an oil refinery a parameter may be used to set the total amount of refined products equal to 92% of the total amount of crude oils (s) entering the refinery, or to calculate certain emissions as a fixed proportion of the amount of oil consumed. If a flow has a sub-annual time-slice resolution, a load curve can be specified for the flow. It is possible to define not only load curves for a flow, but also bounds on the share of a flow in a specific time-slice relative to the annual flow, e.g. the flow in the time-slice "Winter-Day" has to be at least 10 % of the total annual flow. Refer to section 5.4 describing TIMES constraints for details. Cumulative bounds on a process flow are also allowed.

#### Economic and policy parameters

*Economic or policy parameters* include delivery and other variable costs, taxes and subsidies attached to an individual process flow.

#### Bounds

Bounds may be defined for flows in similar variety that exists for commodities.

### Parameters attached to the entire RES

These parameters include currency conversion factors (in a multi-regional model), region-specific time-slice definitions, a region-specific general discount rate, and reference year for calculating the discounted total cost (objective function). In addition, certain switches are needed to control the activation of the data interpolation procedure as well as special model features to be used. The complete set of switches is described in Part III.

## Process and commodity classification

Although TIMES does not explicitly differentiate processes or commodities that belong to different portions of the RES (with the notable exceptions of storage and trading processes), there are three ways in which some differentiation does occur.

First, TIMES requires the definition of Primary Commodity Groups (*pcg*), i.e. subsets of commodities *of the same nature* entering or leaving a process. TIMES utilizes the pcg to define the activity of the process, and also its capacity. For instance, the *pcg* of an oil refinery is defined as the set of energy forms produced by the plant; and the activity of the refinery is thus simply the sum of all its energy outputs (excluding any outputs that are non energy).

Besides establishing the process activity and capacity, these groups are convenient aids for defining certain complex quantities related to process flows, as discussed in chapter 5 and in PART II, section 2.1.

Even though TIMES *does not require* that the user provide many set memberships, the TIMES reporting step does pass some set declarations to the VEDA-BE result-processing system[^10]to facilitate construction of results analysis tables. These include process subsets to distinguish demand devices, energy processes, material processes (by weight or volume), refineries, electric production plants, coupled heat and power plants, heating plants, storage technologies and distribution (link) technologies; and commodity subsets for energy, useful energy demands (split into six aggregate sub-sectors), environmental indicators, currencies, and materials.

Besides the definition of *pcg*\'s and that of VEDA reporting sets, there is a third instance of commodity or process differentiation which is not embedded in TIMES, but rests entirely on the modeler. A modeler may well want to choose process and commodity names in a judicious manner so as to more easily identify them when browsing through the input database or when examining results. As an example, the TIAM-World multi-regional TIMES model (Loulou, 2007) adopts a naming convention whereby the first three characters of a commodity's name denote the sector and the next three the fuel (e.g., light fuel oil used in the residential sector is denoted RESLFO). Similarly, process names are chosen so as to identify the sub-sector or end-use (first three characters), the main fuel used (next three), and the specific technology (last four). For instance, a standard (0001) residential water heater (RWH) using electricity (ELC) is named RWHELC0001. Naming conventions may thus play a critical role in allowing the easy identification of an element's position in the RES and thus facilitate the analysis and reporting of results.

Similarly, energy services may be labeled so that they are more easily recognized. For instance, the first letter may indicate the broad sector (e.g. 'T' for transport) and the second letter designate any homogenous sub-sectors (e.g. 'R' for road transport), the third character being free.

In the same fashion, fuels, materials, and emissions may be identified so as to immediately designate the sector and sub-sector where they are produced or consumed. To achieve this, some fuels have to change names when they change sectors. This is accomplished via processes whose primary role is to change the name of a fuel. In addition, such a process may serve as a bearer of sector wide parameters such as distribution cost, price markup, tax, that are specific to that sector and fuel. For instance, a tax may be levied on industrial distillate use but not on agricultural distillate use, even though the two commodities are physically identical.


[^4]: However, there are TIMES variants -- discussed in chapters 8 to 12, that depart significantly from these assumptions

[^5]: There are exceptional cases when an investment must be repeated more than once in a period, namely when the period is so long that it exceeds the technical life of the investment. These cases are described in detail in section 6.2.2 of PART II.

[^6]: However, if the horizon has been lengthened beyond the years already covered by the data, additional data for the new years at the end of the horizon must of course be provided.

[^7]: Data in this context refers to parameter assumptions, technology characteristics, projections of energy service demands, etc. It does not refer to historical data series.

[^8]: There are a variety of availability factors: annual or seasonal. Each may be specified as a maximum factor (the most frequent case), an exact factor, or even a minimum factor (in order to force some minimum utilization of the capacity of some equipment, as in a backup gas turbine for instance).

[^9]: Vintaging could also be introduced by defining a new technology for each vintage year, but this approach would be wasteful, as many parameters remain the same across all vintages.

[^10]: See Appendix A for the VEDA-FE, VEDA-BE, and ANSWER modeling and analysis systems, used to maintain and manage TIMES databases, conduct model runs, and organize results.
