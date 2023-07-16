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


------------

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
