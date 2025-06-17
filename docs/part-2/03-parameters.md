(parameters)=
# Parameters

While sets describe structural information of the energy system or qualitative characteristics of its entities (e.g. processes or commodities), parameters contain numerical information. Examples of parameters are the import price of an energy carrier or the investment cost of a technology. Most parameters are time-series where a value is provided (or interpolated) for each year ($datayear$). The TIMES model generator distinguishes between user input parameters and internal parameters. The former are provided by the modeller (usually by way of a data handling system or "shell" such a VEDA-FE or ANSWER-TIMES), while the latter are internally derived from the user input parameters, in combination with information given by sets, in order to calculate for example the cost coefficients in the objective function. This Chapter first covers the user input parameters in Section 3.1 and then describes the most important internal parameters as far as they are relevant for the basic understanding of the equations (Section 3.2). Section 3.3 presents the parameters used for reporting the results of a model run.

(user-input-parameters)=
## User input parameters

This section provides an overview of the user input parameters that are available in TIMES to describe the energy system. Before presenting the various parameters in detail in Section 3.1.3 two preprocessing algorithms applied to the user input data are presented, namely the inter-/extrapolation and the inheritance/aggregation routines. User input parameters that are time-dependent can be provided by the user for those years for which statistical information or future projections are available, and the inter-/extrapolation routine described in Section 3.1.1 used to adjust the input data to the years required for the model run. Timeslice dependent parameters do not have to be provided on the timelice level of a process, commodity or commodity flow. Instead the so-called inheritance/aggregation routine described in Section 3.1.2 assigns the input data from the user provided timeslice level to the appropriate timeslice level as necessary.

(inter-and-extrapolation-of-user)=
### Inter- and extrapolation of user input parameters

Time-dependent user input parameters are specified for specific years, the so-called *data years* ($datayear$). These data years do not have to coincide with the model years ($v$ or $modelyear$) needed for the current run. Reasons for differences between these two sets are for example that the period definition for the model has been altered after having provided the initial set of input data leading to different milestone years ($t$ or $milestoneyr$) or that data are only available for certain years that do not match the model years. In order to avoid burdening the user with the cumbersome adjustment of the input data to the model years, an inter-/extrapolation (I/E) routine is embedded in the TIMES model generator. The inter-/extrapolation routine distinguishes between a default inter-/extrapolation that is automatically applied to the input data and an enhanced user-controlled inter-/extrapolation that allows the user to specify an inter-/extrapolation rule for each time-series explicitly. Independent of the default or user-controlled I/E options, TIMES inter-/extrapolates (using the standard algorithm) all cost parameters in the objective function to the individual years of the model as part of calculating the annual cost details (see section 3.1.1.3 below).

The possibility of controlling interpolation on a time-series basis improves the independence between the years found in the primary database and the data actually used in the individual runs of a TIMES model. In this way the model is made more flexible with respect to running scenarios with arbitrary model years and period lengths, while using basically the very same input database.

#### Inter/extrapolation options

The TIMES interpolation/extrapolation facility provides both a default I/E method for all time-series parameters, and options for the user to control the interpolation and extrapolation of each individual time series ({numref}`ie-control-options`). The option 0 does not change the default behavior. The specific options that correspond to the default methods are 3 (the standard default) and 10 (alternative default method for bounds and RHS parameters).

Non-default interpolation/extrapolation can be requested for any parameter by providing an additional instance of the parameter with an indicator in the $YEAR$ index and a value corresponding to one of the integer-valued Option Codes (see {numref}`ie-control-options` and example below). This
control specification activates the interpolation/extrapolation rule for the time series, and is distinguished from actual time-series data by providing a special control label (\'**0**\') in the $YEAR$ index. The particular interpolation rule to apply is a function of the Option Code assigned to the control record for the parameter. Note that for log-linear interpolation the Option Code indicates the year from which the interpolation is switched from standard to log-linear mode. TIMES user shell(s) will provide mechanisms for imbedding the control label and setting the Option Code through easily understandable selections from a user-friendly drop-down list, making the specification simple and transparent to the user.

The enhanced interpolation/extrapolation facility provides the user with the following options to control the interpolation and extrapolation of each individual time series:
- Interpolation and extrapolation of data in the default way as predefined in TIMES. This option does not require any explicit action from the user.
- No interpolation or extrapolation of data (only valid for non-cost parameters).
- Interpolation between data points but no extrapolation (useful for many bounds). See option codes 1 and 11 in {numref}`ie-control-options` below.
- Interpolation between data points entered, and filling-in all points outside the interpolation window with the EPS (zero) value. This can useful for e.g. the RHS of equality-type user constraints, or bounds on future investment in a particular instance of a technology. See option codes 2 and 12 in {numref}`ie-control-options` below.
- Forced interpolation and extrapolation throughout the time horizon. Can be useful for parameters that are by default not interpolated. See option codes 3, 4, and 5 as well as 14 and 15 in {numref}`ie-control-options` below.
- Log-linear interpolation beyond a specified data year, and both forward and backward extrapolation outside the interpolation window. Log-linear interpolation is guided by relative coefficients of annual change instead of absolute data values.

```{list-table} Option codes for the control of time series data interpolation.
:name: ie-control-options
:header-rows: 1

* - Option code
  - Action
  - Applies to
* - 0 (or none)
  - Interpolation and extrapolation of data in the default way as predefined in TIMES (see below)
  - All
* - \<0
  - No interpolation or extrapolation of data (only valid for non-cost parameters).
  - All
* - 1
  - Interpolation between data points but no extrapolation.
  - All
* - 2
  - Interpolation between data points entered, and filling-in all points outside the interpolation window with the EPS value.
  - All
* - 3
  - Forced interpolation and both forward and backward extrapolation throughout the time horizon.
  - All
* - 4
  - Interpolation and backward extrapolation
  - All
* - 5
  - Interpolation and forward extrapolation
  - All
* - 10
  - Migrated interpolation/extrapolation within periods
  - Bounds, RHS
* - 11
  - Interpolation migrated at end-points, no extrapolation
  - Bounds, RHS
* - 12
  - Interpolation migrated at ends, extrapolation with EPS
  - Bounds, RHS
* - 14
  - Interpolation migrated at end, backward extrapolation
  - Bounds, RHS
* - 15
  - Interpolation migrated at start, forward extrapolation
  - Bounds, RHS
* - YEAR (≥1000)
  - Log-linear interpolation beyond the specified YEAR, and both forward and backward extrapolation outside the interpolation window.
  - All
```

Migration means that data points are interpolated and extrapolated within each period but not across periods. This method thus migrates any data point specified for other than $milestoneyr$ year to the corresponding $milestoneyr$ year within the period, so that it will be effective in that period.

Log-linear interpolation means that the values in the data series are interpreted as coefficients of annual change beyond a given $YEAR$. The $YEAR$ can be any year, including model years. The user only has to take care that the data values in the data series correspond to the interpretation given to them when using the log-linear option. For simplicity, however, the first data point is always interpreted as an absolute value, because log-linear interpolation requires at least one absolute data point to start with.

#### Default inter/extrapolation

The standard default method of inter-/extrapolation corresponds to the option 3, which interpolates linearly between data points, while it extrapolates the first/last data point constantly backward/forward. This method, full interpolation and extrapolation, is by default applied to most TIMES time series parameters. However, the parameters listed in {numref}`no-default-full-ie` are by default **NOT** inter/extrapolated in this way, but have a different default method.

(interpolation-of-cost-parameters)=
#### Interpolation of cost parameters

As a general rule, all cost parameters in TIMES are densely interpolated and extrapolated. This means that the parameters will have a value for every single year within the range of years they apply, and the changes in costs over years will thus be accurately taken into account in the objective function. The user can use the interpolation options 1--5 for even cost parameters. Whenever an option is specified for a cost parameter, it will be first sparsely interpolated/extrapolated according to the user option over the union of modelyear and datayear, and any remaining empty data points are filled with the EPS value. The EPS values will ensure that despite the subsequent dense interpolation the effect of user option will be preserved to the extent possible. However, one should note that due to dense interpolation, the effects of the user options will inevitably be smoothed.

#### Examples of using I/E options

**Example 1:**

Assume that we have three normal data points in a FLO_SHAR data series:

```
FLO_SHAR('REG','1995','PRC1','COAL','IN_PRC1','ANNUAL','UP') = 0.25;
FLO_SHAR('REG','2010','PRC1','COAL','IN_PRC1','ANNUAL','UP') = 0.12;
FLO_SHAR('REG','2020','PRC1','COAL','IN_PRC1','ANNUAL','UP') = 0.05;
```

$FLO\_SHAR$ is by default NOT interpolated or extrapolated in TIMES. To force interpolation/extrapolation of the $FLO\_SHAR$ parameter the following control option for this data series should be added:

```
FLO_SHAR('REG','0','PRC1','COAL','IN_PRC1','ANNUAL','UP') = 3;
```

```{list-table} Parameters not being fully inter/extrapolated by default
:name: no-default-full-ie
:header-rows: 1

* - Parameter
  - Justification
  - Default I/E
* - ACT_BND
  <br>CAP_BND
  <br>NCAP_BND
  <br>NCAP_DISC
  <br>FLO_FR
  <br>FLO_SHAR
  <br>STGIN_BND
  <br>STGOUT_BND
  <br>COM_BNDNET
  <br>COM_BNDPRD
  <br>COM_CUMNET
  <br>COM_CUMPRD
  <br>REG_BNDCST
  <br>RCAP_BND
  <br>IRE_BND
  <br>IRE_XBND
  - Bound may be intended at specific periods only.
  - 10 (migration)
* - PRC_MARK
  - Constraint may be intended at specific periods only
  - 11
* - PRC_RESID
  - Residual capacity usually intended to be only interpolated
  - 1\*
* - UC_RHST
  <br>UC_RHSRT
  <br>UC_RHSRTS
  - User constraint may be intended for specific periods only
  - 10 (migration)
* - NCAP_AFM
  <br>NCAP_FOMM
  <br>NCAP_FSUBM
  <br>NCAP_FTAXM
  - Interpolation meaningless for these parameters (parameter value is a discrete number indicating which MULTI curve should be used).
  - 10 (migration)
* - COM_ELASTX
  <br>FLO_FUNCX
  <br>NCAP_AFX
  <br>NCAP_FOMX
  <br>NCAP_FSUBX
  <br>NCAP_FTAXX
  - Interpolation meaningless for these parameters (parameter value is a discrete number indicating which SHAPE curve should be used).
  - 10 (migration)
* - NCAP_PASTI
  - Parameter describes past investment for a single vintage year.
  - none
* - NCAP_PASTY
  - Parameter describes number of years over which to distribute past investments.
  - none
* - CM_MAXC
  - Bound may be intended at specific years only
  - none
* - PEAKDA_BL
  - Blending parameters at the moment not interpolated
  - none
```

\* If only a single $PRC\_RESID$ value is specified, assumed to decay linearly over $NCAP\_TLIFE$ years

**Example 2:**

Assume that we define the following log-linear I/E option for a $FLO\_SHAR$ data series:

```
FLO_SHAR('REG','0','PRC1','COAL','IN_PRC1','ANNUAL','UP') = 2005;
```

This parameter specifies a log-linear control option with the value for the threshold YEAR of log-linear interpolation taken from 2005. The option specifies that all data points up to the year 2005 should be interpreted normally (as absolute data values), but all values beyond that year should be interpreted as coefficients of annual change. By using this interpretation, TIMES will then apply full interpolation and extrapolation to the whole data series. It is the responsibility of the user to ensure that the first data point and all data points up to (and including) the year 2005 represent absolute values of the parameter, and that all subsequent data points represent coefficients of annual change. Using the data of the example above, the first data point beyond 2005 is found for the year 2010, and it has the value of 0.12. The interpretation thus requires that the maximum flow share of COAL in the commodity group IN_PRC1 is actually meant to increase by as much as 12% per annum between the years 1995 and 2010, and by 5% per annum between 2010 and 2020.

#### Applicability

All the enhanced I/E options described above are available for all TIMES timeseries parameters, excluding $PRC\_RESID$ and $COM\_BPRICE$. $PRC\_RESID$ is always interpolated, as if option 1 were used, but is also extrapolated forwards over $TLIFE$ when either I/E option 5 or 15 is specified. $COM\_BPRICE$ is not interpolated at all, as it is obtained from the Baseline solution. Moreover, the I/E options are not applicable to the integer-valued parameters related to the $SHAPE$ and $MULTI$ tables, which are listed in {numref}`interpolation-not-applicable`.

```{list-table} Parameters which cannot be interpolated.
:name: interpolation-not-applicable
:header-rows: 1

* - Parameter
  - Comment
* - NCAP_AFM
  <br>NCAP_FOMM
  <br>NCAP_FSUBM
  <br>NCAP_FTAXM
  - Parameter value is a discrete numbers indicating which MULTI curve should be used, and not a time series datum.
* - COM_ELASTX
  <br>FLO_FUNCX
  <br>NCAP_AFX
  <br>NCAP_FOMX
  <br>NCAP_FSUBX
  <br>NCAP_FTAXX
  - Parameter value is a discrete number indicating which SHAPE curve should be used, and not a time series datum.
```

Nonetheless, a few options are supported also for the extrapolation of the $MULTI$ and $SHAPE$ index parameters, as shown in {numref}`e-option-codes-shape-multi`. The extrapolation can be done either only inside the data points provided by the user, or both inside and outside those data points. When using the inside data points option, the index specified for any $datayear$ is extrapolated to all model years ($v$) between that $datayear$ and the following $datayear$ for which the $SHAPE$ index is specified. The extrapolation options are available for all of the $SHAPE$ and $MULTI$ parameters listed in {numref}`interpolation-not-applicable`.

```{list-table} Option codes for the extrapolation of SHAPE/MULTI indexes.
:name: e-option-codes-shape-multi
:header-rows: 1

* - Option code
  - Action
* - <=0 (or none)
  - No extrapolation (default)
* - 1
  - Extrapolation between data points only
* - 2
  - Extrapolation between and outside data points
* - 4
  - Extrapolation between data points and backwards
* - 5
  - Extrapolation between data points and forwards
* - 11
  - Extrapolation between data points only, migration at ends
```

**Example:**

The user has specified the following two SHAPE indexes and a control option for extrapolation:

```
NCAP_AFX('REG', '0', 'PRC1') = 1;
NCAP_AFX('REG', '1995', 'PRC1') = 12;
NCAP_AFX('REG', '2010', 'PRC1') = 13;
``` 
 
 In this case, all model years ($v$) between 1995 and 2010 will get the shape index 12. No extrapolation is done for model years ($v$) beyond 2010 or before 1995.

(inheritance-and-aggregation-of)=
### Inheritance and aggregation of timesliced input parameters

As mentioned before, processes and commodities can be modelled in TIMES on different timeslice levels. Some of the input parameters that describe a process or a commodity are timeslice specific, i.e. they have to be provided by the user for specific timeslices, e.g. the availability factor $NCAP\_AF$ of a power plant operating on a \'DAYNITE\' timeslice level. During the process of developing a model, the timeslice resolution of some processes or even the entire model may be refined. One could imagine for example the situation that a user starts developing a model on an \'ANNUAL\' timeslice level and refines the model later by refining the timeslice definition of the processes and commodities. In order to avoid the need for all the timeslice related parameters to be re-entered again for the finer timeslices, TIMES supports inheritance and aggregation of parameter values along the timeslice tree.

Inheritance in this context means that input data being specified on a coarser timeslice level (higher up the tree) are inherited to a finer timeslice level (lower down the tree), whereas aggregation means that timeslice specific data are aggregated from a finer timeslice level (lower down the tree) to a coarser one (further up the tree). The inheritance feature may also be useful in some cases where the value of a parameter should be the same over all timeslices, since in this case it is sufficient to provide the parameter value for the \'ANNUAL\' timeslice which is then inherited to the required finer target timeslices.[^21]

```{list-table} Inheritance and aggregation rules.
:name: inheritance-and-aggregation-rules
:align: left

* - **Inheritance rules**
  - **Description**
* - Direct inheritance
  - A value on a coarser timeslice is inherited by target timeslices below (in the timeslice tree), without changing the numeric values.
* - Weighted inheritance
  - A value on a coarser timeslice is inherited by target timeslices below (in the timeslice tree) by weighting the input value with the ratio of the duration of the target timeslices to the duration of the coarser timeslice. Example: Parameter COM_FR.
* - No inheritance
  - Absolute bound parameters specified on a coarser timeslice level than the target timeslice level are not inherited. Instead a constraint summing over related variables on the finer timeslices is generated, e.g. an annual ACT_BND parameter specified for a process with a \'DAYNITE\' process timeslice level (prc_tsl) leads to a constraint (EQ_ACTBND) with the summation over the activity variables on the \'DAYNITE\' level as LHS term and with the bound as RHS term.
* - **Aggregation rules**
  - **Description**
* - Standard aggregation
  - The values specified on finer timeslices are aggregated to the target timeslice being a parent node in the timeslice tree by summing over the values on the finer timeslices.
* - Weighted aggregation
  - The values specified for finer timeslices are aggregated to the target timeslice being a parent node in the timeslice tree by summing over the weighted values on the finer timeslices. The ratios of the duration of the finer timeslices to the duration of the target timeslice serve as weighting factors.

```

The TIMES pre-processor supports different inheritance and aggregation rules, which depend on the type of attribute. The main characteristics of the different inheritance and aggregation rules are summarised in {numref}`inheritance-and-aggregation-rules`. The specific rules applied to each individual parameter are listed in the detailed reference further below.

The different aggregation rules are illustrated by examples in {numref}`inheritance-aggregation-rules-parameters`. It should be noted that if input data are specified on two timeslice levels different from the target level, then especially the weighted inheritance/aggregation method may lead to incorrect results. Therefore, at least for the parameters where weighted methods are applied, it is recommended to provide input data only for timeslices on one timeslice level. However, for parameters that are directly inherited, specifying values at multiple levels may sometimes be a convenient way to reduce the amount of values to be specified.[^22]

Bound parameters are in most cases not levelized by inheritance, only by aggregation. Exceptions to this rule are the relative type bound parameters $NCAP\_AF$ and $FLO\_SHAR$, which are inherited by the target timeslices. One should also notice that, due to levelization, fixed bounds that are either inherited or aggregated to the target timeslice level will always override any upper and lower bounds simultaneously specified.

```{figure} assets/inheritance-and-aggregation-rules.svg
:name: inheritance-aggregation-rules-parameters
:align: center

Inheritance and aggregation rules for timeslice specific parameters in TIMES.
```

(overview-of-user-input-parameters)=
### Overview of user input parameters

A list of all user input parameters (except for those specific to the TIMES-MACRO variants) is given in {numref}`user-input-parameters`. For the MACRO input parameters, the reader is advised to consult the separate documentation. In order to facilitate the recognition by the user of to which part of the model a parameter relates the following naming conventions apply to the prefixes of the parameters ({numref}`uip-naming-conventions`).

:::{table} Naming conventions for user input parameters.
:name: uip-naming-conventions

| Prefix      | Related model component        |
| ----------- | ------------------------------ |
| G\_         | Global characteristic          |
| ACT\_       | Activity of a process          |
| CAP\_       | Capacity of a process          |
| COM\_       | Commodity                      |
| FLO\_       | Process flow                   |
| IRE\_       | Inter-regional exchange        |
| NCAP\_      | New capacity of a process      |
| PRC\_       | Process                        |
| RCAP\_      | Retiring capacity of a process |
| REG\_ / R\_ | Region-specific characteristic |
| STG\_       | Storage process                |
| UC\_        | User constraint                |

:::

For brevity, the default interpolation/extrapolation method for each parameter is given by using the abbreviations listed in {numref}`ie-abbreviations`.

:::{table} Abbreviations for default I/E method in {numref}`user-input-parameters`.
:name: ie-abbreviations

| Abbreviation | Description                                   |
| ------------ | --------------------------------------------- |
| STD          | Standard full inter-/extrapolation (option 3) |
| MIG          | Migration (option 10)                         |
| \<number\>   | Option code for any other default method      |
| none         | No default inter-/extrapolation               |
| N/A          | Inter-/extrapolation not applicable           |
:::

```{list-table} User input parameters in TIMES
:name: user-input-parameters
:header-rows: 1

* - Input parameter (Indexes)[^23]
  - Related sets / parameters[^24]
  - Units / Ranges & Default values & Default inter-/extrapolation[^25]
  - Instances[^26] (Required / Omit / Special conditions)
  - Description
  - Affected equations or variables[^27]
* - ACT_BND
  <br>(r,datayear,p,s,bd)
  - 
  - Units of activity
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e[^28]: MIG
  - Since inter-/extrapolation default is MIG, the bound must be explicitly specified for each period, unless an inter-/extrapolation option is set.
  <br>If the bound is specified for a timeslice s above the process timeslice resolution (prc_tsl), the bound is applied to the sum of the activity variables according to the timeslice tree.
  <br>Standard aggregation.
  - Bound on the overall activity a process.
  - Activity limit constraint (EQ(l)\_ACTBND) when s is above prc_tsl.
  <br>Direct bound on activity variable (VAR_ACT) when at the prc_tsl level.
* - ACT_COST
  <br>(r,datayear,p,cur)
  - OBJ_ACOST, CST_ACTC, CST_PVP
  - Monetary unit per unit of activity
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - 
  - Variable costs associated with the activity of a process.
  - Applied to the activity variable (VAR_ACT) as a component of the objective function (EQ_OBJVAR).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - ACT_CSTPL
  <br>(r,datayear,p,cur)
  - ACT_MINLD, ACT_LOSPL
  - Monetary unit per unit of activity
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Used as an alternative or supplement to using ACT_LOSPL(r,y,p,\'FX\'). When used as an alternative, the fuel increase at the minimum operating level that should be included in the cost penalty must be embedded in the ACT_CSTPL coefficient.
  - Partial load cost penalty, defined as an additional cost per activity at the minimum operating level, corresponding to the efficiency loss at that load level.
  <br>Added as an extra term to variable costs in the objective and reporting.
  - Generates an additional term in EQ_OBJVAR for the increase in operating cost.
* - ACT_CSTRMP
  <br>(r,datayear,p,bd,cur)
  - ACT_UPS
  - Corrency unit per unit of capacity (change in load)
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can be used for standard processes in basic, advanced and discrete unit commitment extensions.
  <br>Can also be used for load-shifting processes for defining the cost of shifting loads per unit of demand load by one hour.
  - Defines ramp-up (L=UP) or ramp-down (L=LO) cost per unit of load change (in capacity units).
  <br>For **load-shifting** processes defines the cost of shifting one unit of load by one hour, forward (UP) or backward (LO).
  - Activates generation of EQ_ACTRMPC.
  <br>Generates an additional term in EQ_OBJVAR for the increase in operating cost.
* - ACT_CSTSD
  <br>(r,datayear,p,upt,bd,cur)
  - ACT_CSTUP, ACT_SDTIME, ACT_MAXNON
  - Currency units per unit of started-up capacity
  <br>\[0,∞);
  <br>Default value: none
  <br>Default i/e: STD
  - Activates the advanced unit commitment option.
  <br>In the case of the shut-down costs, only the tuple (upt, bd) = (HOT, LO) is a valid instance for this parameter.
  <br>Requires the parameter ACT_MAXNON to be defined as well.
  - Defines start-up (bd=UP) and shutdown costs (bd=LO) per unit of started-up capacity, differentiated by start-up type (upt).
  <br>The start-up type of a power plant depends on its non-operational time after shut-down, as defined by using ACT_MAXNON.
  - Generates an additional term in EQ_OBJVAR for the increase in operating cost.
* - ACT_CSTUP
  <br>(r,datayear,p,tslvl,cur)
  - ACT_MINLD, ACT_UPS
  - Monetary unit per unit of capacity
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - The tslvl level refers to the timeslice cycle for which the start-up cost is defined.
  <br>Only applicable when the min. stable operating level has been defined with ACT_MINLD.
  - Cost of process start-up per unit of started-up capacity.
  <br>Added as an extra term to variable costs in the objective and reporting.
  - Activates generation of EQL_ACTUPS eqs.
  <br>Generates an additional term in the variable operating costs included in EQ_OBJVAR.
* - ACT_CUM
  <br>(r,p,y1,y2,bd)
  - FLO_CUM
  - Activity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - The years y1 and y2 may be any years of the set allyear; where y1 may also be \'BOH\' for first year of first period and y2 may be \'EOH\' for last year of last period.
  - Bound on the cumulative amount of annual process activity between the years y1 and y2, within a region.
  - Generates an instance of the cumulative constraint (EQ_CUMFLO)
* - ACT_EFF
  <br>(r,datayear,p,cg,s)
  - 
  - Activity unit per flow unit
  <br>\[0,∞);
  <br>Default value: none
  <br>Default group efficiency =1 when values are specified only for individual commodities.
  <br>Default i/e: STD
  - The group cg may be a single commodity, group, or commodity type on the shadow side, or a single commodity in the PCG; cg=\'ACT\' refers to the default shadow group. If no group efficiency is defined, shadow group is assumed to be the commodity type. Individual commodity efficiencies are multiplied with the shadow group efficiency (default=1).
  <br>Levelized to the timeslice level of the flow variables in the shadow group.
  <br>Direct inheritance. Weighted aggregation.
  - Activity efficiency for process, i.e. amount of activity per unit of commodity flows in the group cg.
  <br>For more information on usage, see Section 6.3 for details about EQE_ACTEFF.
  - Generates instances of the activity efficiency constraint (EQE_ACTEFF)
* - ACT_FLO
  <br>(r,datayear,p,cg,s)
  - 
  - Flow unit per activity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Inherited/aggregated to the timeslice levels of the the process flow (cg=com) or the process activity (when cg=genuine group).
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Flow of commodities in cg in proportion to the process activity, in timeslice s.
  <br>Non-vintaged variant available for vintaged processes by using a negative FLO_FUNCX.
  - Establishes a transformation relationship (EQ_PTRANS) between the flows in the PCG and one or more input (or output) commodities.
* - ACT_LOSPL
  <br>(r,datayear,p,bd)
  - ACT_MINLD, ACT_CSTPL
  - Decimal fraction
  <br>\[0,∞);
  <br>default values:
  <br>FX: none
  <br>LO: default value is ACT_MINLD or 0.1
  <br>if that is not defined
  <br>UP: 0.6
  <br>Default i/e: STD
  - Endogenous partial load modeling can only be used for processes that have their efficiency modelled by the ACT_EFF parameter, which must be defined on the shadow side of the process.
  <br>For other processes, the ACT_CSTPL parameter can be used for modeling a cost penalty at partial loads.
  - Partial load efficiency parameters.
  <br>1\) (bd=\'FX\'): Proportional increase in specific fuel consumption at minimum operating level
  <br>2) (bd=\'LO\'):
  <br>Minimum operating level of partial load operation
  <br>3) (bd=\'UP\'):
  <br>Fraction of feasible load range above the minimum operating level, below which the efficiency losses are assumed to occur.
  - Generates instances of the partial load efficiency constraint EQ_ACTPL.
* - ACT_LOSSD
  <br>(r,datayear,p,upt,bd)
  - ACT_LOSPL, ACT_MINLD, ACT_SDTIME, ACT_EFF
  - Dimensionless
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can only be used when the advanced unit commitment option is used for the process (therefore, defining both ACT_CSTSD and ACT_MAXNON is required)
  <br>Requires also that ACT_EFF has been used for defining the process efficiency (on the shadow side of the process).
  - Used for modeling endogenous partial load efficiency losses during the start-up and shut-down phase.
  <br>- With bd=UP defines increase in specific fuel consumption at the start up load level defined by the ratio ACT_MINLD / ACT_SDTIME(upt,\'UP\') for start-up type upt;
  <br>- With bd=LO defines the increase in
  <br>specific fuel consumption at the start up load level defined by the ratio ACT_MINLD / ACT_SDTIME(\'HOT\', \'LO\').
  - Activates generation of EQ_SUDPLL
* - ACT_MAXNON
  <br>(r,datayear,p,upt)
  - ACT_CSTSD, ACT_SDTIME
  - hours
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can only be used when the advanced unit commitment option is used for the process (thus defining ACT_CSTSD is required)
  - Max. non-operational time before transition to next stand-by condition, by start-up type, in hours
  <br>- Defines the max. non-operational time before a subsequent start-up of type upt.
  - Activates generation of EQ_SUDUPT
* - ACT_MINLD
  <br>(r,datayear,p)
  - ACT_UPS, ACT_CSTUP, ACT_CSTPL, ACT_LOSPL
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can only be used for standard processes (not IRE or STG). Must be defined if ACT_CSTUP or ACT_TIME is specified.
  - Minimum stable operating level of a dispatchable process.
  - Generates instances of equations EQ_CAPLOAD and EQE_ACTUPS.
* - ACT_SDTIME
  <br>(r,datayear,p,upt,bd)
  - ACT_CSTSD, ACT_MAXNON
  - hours
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can only be used when ACT_CSTSD is specified for the process (advanced unit commitment option)
  <br>When specifying the duration of the shut-down phase, only the tuple (upt,bd)=(HOT,LO) is valid
  - Defines the duration of start-up (bd=UP) and shut-down (bd=LO) phases, by start-up type, in hours.
  - Activates generation of EQ_SUDTIME, and used also in the equations EQ_ACTPL, EQ_SDSLANT, EQ_SDMINON, EQ_SUDPLL
* - ACT_TIME
  <br>(r,datayear,p,lim)
  - ACT_MINLD, ACT_CSTUP, ACT_UPS, STG_SIFT
  - Hours
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can be used for standard processes when start-up costs have been modeled, using both ACT_MINLD and
  <br>ACT_CSTUP at the
  <br>DAYNITE/WEEKLY level.
  <br>The lim type \'FX\' is not supported for this use, and is ignored.
  <br>Can also be used for load-shifting storage processes, for defining the maximum delay/advance of load shift, or the time-window for load balancing (cf. Sect. 4.3.9).
  - 1\) Minimum online
  <br>(UP) / offline (LO)
  <br>hours of a process
  <br>with start-up costs
  <br>modeled (lim=LO/UP)
  <br>2\) Maximum number
  <br>of start-up cycles
  <br>within process timeslice cycles (lim=N).
  <br>3\) Maximum delay or advance of load shift (lim=UP/LO/FX) or load balancing time (lim=N) for a load-shifting storage.
  - Generates instances of EQL_ACTUPC.
  <br>For load-shifting storage processes, generates instances of EQ_SLSIFT.
* - ACT_UPS
  <br>(r,datayear,p,s,bd)
  - ACT_MINLD, ACT_CSTUP, ACT_CSTPL, ACT_LOSPL
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Inherited/aggregated to the timeslice levels of the process activity.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  <br>The ramp rates can only be specified with bd=LO/UP.
  - Maximum ramp-rate (down/up) of process activity as a fraction of nominal on-line capacity per hour.
  - Generates instances of equation EQ_ACTRAMP.
* - B
  <br>\(t)
  - M, D, E, COEF_CPT, rtp_vintyr
  - 
  - Required for each milestone year, but is auto-generated if not specified
  - Beginning year of period t.
  - 
* - BS_BNDPRS
  <br>(r,datayear,p,b,s,lim)
  - 
  - Unit: Capacity unit of the process
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Not levelized (inherited or aggregated), but applied only directly on the timeslice s specified.
  <br>See the ABS documentation for details
  - Absolute bound on the reserve provision **b** from process **p**.
  - EQ_BS27
* - BS_CAPACT
  <br>\(r\)
  - PRC_CAPACT
  - Flow unit / capacity unit;
  <br>(0,∞); default value: PRC_CAPACT
  <br>Default i/e: none
  - Applied also for the reporting of reserves in terms of power levels.
  <br>See the ABS documentation for details
  - Conversion factor from exogenous reserve demand from capacity to activity / commodity flow units
  - EQ_BS04
* - BS_DELTA
  <br>(r,datayear,b,s)
  - 
  - Unit: dimensionless
  <br>\[0,∞);
  <br>default value: 1
  <br>Default i/e: STD
  - Levelized to COM_TSL of **b**.
  <br>See the ABS documentation for details
  - Calibration parameters for probabilistic reserve demand **b**, in region **r**, and timeslice **s**.
  - EQ_BS03
* - BS_DEMDET
  <br>(r,datayear,rsp,b,s)
  - 
  - Unit for EXOGEN: capacity unit
  <br>Unit for WMAXSI: dimensionless (fraction of capacity)
  <br>Default value: none
  <br>Default i/e: STD
  - - rsp=\'EXOGEN\': Exogenous reserve demand for reserve **b**, in region **r**, timeslice **s**.
  <br>- rsp=\'WMAXSI\': Weight of the contribution of the largest system element in deterministic reserve demand **b**, in region **r**, timeslice **s**.
  <br>See the ABS documentation for details
  - Parameters for deterministic demands of reserves (rsp = EXOGEN or WMAXSI)
  - EQ_BS04
* - BS_DETWT
  <br>(r,datayear,b)
  - 
  - Unit: dimensionless
  <br>\[0,1\];
  <br>Default value: none
  <br>Default i/e: STD
  - See the ABS documentation for details.
  - Weight of the deterministic component in the formulation for endogenous requirements of reserve **b** in region **r**
  - EQ_BS03
* - BS_LAMBDA
  <br>(r,datayear,b)
  - BS_DELTA
  - Unit: dimensionless
  <br>(0,1\];
  <br>Default value: none
  <br>Default i/e: STD
  - Required. If not defined, then the demand for reserve **b** cannot be calculated.
  <br>See the ABS documentation for details.
  - Fudge factors for dependencies in the reserve requirements
  <br>calculated for reserve **b** in region **r**, in year datayear
  - EQ_BS03
* - BS_MAINT
  <br>(r,datayear,p,s)
  - 
  - Unit: hours
  <br>(if over 24 hours, continuous over whole season)
  <br>(0, ∞);
  <br>Default value: none
  <br>Default i/e: STD
  - Levelized to PRC_TSL.
  <br>If defined on DAYNITE or WEEKLY level, requires start-ups explicitly enabled on that level (using ACT_CSTUP/ACT_CSTSD).
  <br>See the ABS documentation for details.
  - For endogenous maintenance scheduling, defines minimum continuous maintenance time of process **p**, vintage **v**, timeslice **s**, in hours (**s** can be a process timeslice, or more usefully above it, to allow for optimized maintenance period)
  - EQ_BS27, EQ_BS28
* - BS_OMEGA
  <br>(r,datayear,b,s)
  - BS_DELTA, BS_LAMBDA
  - Unit: dimensionless
  <br>ω ϵ {1,2,3};
  <br>Default value: none
  <br>Default i/e: STD
  - Required for enabling reserve provision formulation.
  <br>Levelized to COM_TSL of **b**.
  <br>See the ABS documentation for details
  - Indicator denoting if the demand for reserve **b** is the weighted sum of the deterministic and probabilistic component (ω=2), the maximum of the two (ω=1), or their difference (ω=3)
  - EQ_BS03
* - BS_RMAX
  <br>(r,datayear,p,c,s)
  - 
  - Unit: dimensionless (fraction of capacity)
  <br>\[0, 1\];
  <br>Default value: none
  <br>Default i/e: STD
  - Required for enabling reserve provision from any non-storage processes.
  <br>Levelized to PRC_TSL.
  <br>See the ABS documentation for details
  - Maximum contribution of process **p**, vintage **v**, in timeslice **s** to the provision of reserve commodity **b**.
  - EQ_BS11, EQ_BS19
* - BS_RTYPE
  <br>(r,b)
  - 
  - Unit: dimensionless
  <br>{±1, ±2, ±3, ±4};
  <br>Default value: none
  <br>Default i/e: none
  - Required for enabling reserve provision calculations.
  <br>See the ABS documentation for details
  - Type of reserve commodity **b**, positive or negative ± 1--4:
  <br>±1 : FCR reserve
  <br>±2 : AFRR reserve
  <br>±3 : MFRR reserve
  <br>±4 : RR reserve
  - EQ_BS00, EQ_BS01, EQ_BS11, EQ_BS18, EQ_BS19, EQ_BS26
* - BS_SHARE
  <br>(r,datayear,b,grp,lim)
  - BS_OMEGA
  - Unit: dimensionless
  <br>\[0, 1\];
  <br>Default value: none
  <br>Default i/e: STD
  - The group **grp** can be defined by GR_GENMAP, or implicitly for any single process prc=grp.
  <br>See the ABS documentation for details
  - Maximum (bd=UP) or minimum (bd=LO) share of process group **grp** in the demand for reserve **b**, in region **r**, where demand is measured as defined by BS_OMEGA
  - EQ_BS01
* - BS_SIGMA
  <br>(r,datayear,b,grp,s)
  - 
  - Unit: dimensionless
  <br>(0, ∞);
  <br>Default value: none
  <br>Default i/e: STD
  - Levelized to finest ts-level.
  <br>See the ABS documentation for details
  - Standard deviation of forecast error for the imbalance source **grp**, in region **r**, timeslice **s**, used for calculating the demand for reserve **b**
  - EQ_BS03
* - BS_STIME
  <br>(r,p,b,bd)
  - 
  - Unit: hours
  <br>(0, ∞);
  <br>Default value: none
  <br>Default i/e: none
  - Required that \'UP\' ≥ \'LO\'.
  <br>See the ABS documentation for details
  - Defines the times for reserve provision from storage process **p** for reserve **b** in region **r** (in hours):
  <br>- bd=\'LO\': Time required to ramp up in order to provide reserve **b**
  <br>- bd=\'UP\': Duration of provision for reserve **b** including time to ramp up
  - EQ_BS22, EQ_BS23
* - CAP_BND
  <br>(r,datayear,p,bd)
  - PAR_CAPLO, PAR_CAPUP
  - Capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Since inter-/extrapolation is default is MIG, a bound must be specified for each period desired, if no explicit inter-/extrapolation option is given. Relaxed if upper bound less than existing non-retirable capacity.
  - Bound on investment in new capacity.
  - Imposes an indirect limit on the capacity transfer equation (EQ_CPT) by means of a direct bound on the capacity variable (VAR_CAP).
* - CM_CONST
  <br>(item)
  - 
  - Constant specific unit
  <br>\[open\];
  <br>default value: See Appendix
  <br>Default i/e: N/A
  - See Appendix on Climate Module for details.
  - Various climate module constants, e.g. phi and sigma values between reservoirs.
  - EQ_CLITOT, EQ_CLICONC, EQ_CLITEMP, EQ_CLIBEOH
* - CM_EXOFORC
  <br>(year)
  - 
  - Forcing unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Default values are provided. See Appendix on Climate Module for details.
  - Radiative forcing from exogenous sources
  - EQ_CLITOT
* - CM_GHGMAP
  <br>(r,c,cm_var)
  - 
  - Units of climate module emissions per units of regional emissions
  <br>\[0, ∞);
  <br>default value: none
  - The global emissions in the climate module (cm_var) are \'CO2-GtC\' (GtC), \'CH4-Mt\' (Mt) and \'N2O-Mt\' (Mt). See Appendix on Climate Module for details.
  - Mapping and conversion of regional GHG emissions to global emissions in the climate module
  - EQ_CLITOT
* - CM_HISTORY
  <br>(year,item)
  - 
  - Climate variable unit
  <br>\[0, ∞);
  <br>default value: none
  <br>Default i/e: STD
  - Default values are provided until 2010. See Appendix on Climate Module for details.
  - Calibration values for CO2 and forcing
  - EQ_CLITOT, EQ_CLICONC, EQ_CLITEMP, EQ_CLIBEOH
* - CM_LINFOR
  <br>(datayear,item,lim)
  - 
  - Forcing unit per concentration unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - With lim types LO/UP, CO2 forcing function can be automatically linearized between the concentration levels given. For CH4 and N2O, lim types FX/N must be used (N=concentration multiplier, FX=constant term). See Appendix on Climate Module for details.
  - Parameters of linearized forcing functions
  - EQ_CLITOT
* - CM_MAXC
  <br>(datayear,item)
  - 
  - Climate variable unit
  <br>\[0, ∞);
  <br>default value: none
  <br>Default i/e: none
  - Since no default inter-/extrapolation, bounds must be explicitly specified for each desired year, unless an explicit inter-/extrapolation option is set.
  <br>See Appendix on Climate Module for details.
  - Maximum level of climate variable
  - EQ_CLIMAX
* - COM_AGG
  <br>(r,dayayear,c1,c2)
  - 
  - Commodity units
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - When commodity lim_type is LO and commodity type is not DEM, VAR_COMNET of c1 is aggregated to c2;
  <br>When commodity lim_type is FX/N or commodity type is DEM, VAR_COMPRD of c1 is aggregated to c2.
  - Aggregation of commodity NET/PRD production to the production side of the balance of another commodity.
  - Adds a term in EQ(l)\_COMBAL and EQ(l)\_COMPRD.
* - COM_BNDNET
  <br>(r,datayear,c,s,bd)
  - rhs_combal, rcs_combal
  - Commodity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: MIG
  <br>Remark: All VAR_COMNET variables are by default non-negative, i.e. have lower bounds of zero
  - Since inter-/extrapolation default is MIG, a bound must be specified for each period desired, if no explicit inter-/extrapolation option is given.
  <br>If the bound is specified for a timeslice s above the commodity timeslice resolution (com_tsl), the bound is applied to the sum of the net commodity variables (VAR_COMNET) below it, according to the timeslice tree.
  <br>Standard aggregation.
  - Limit on the net amount of a commodity (variable
  <br>VAR_COMNET) within a region for a particular timeslice.
  - The balance constraint is set to an equality (EQE_COMBAL).
  <br>Either the finer timeslice variables are summed (EQ(l)\_BNDNET) or the bound applied direct to the commodity net variable(VAR_COMNET) when at the commodity level (com_tsl).
* - COM_BNDPRD
  <br>(r,datayear,c,s,bd)
  - rhs_comprd, rcs_comprd
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  <br>Remark: All VAR_COMPRD variables are by default non-negative, i.e. have lower bounds of zero
  - Since inter-/extrapolation default is MIG, a bound must be specified for each period desired, if no explicit inter-/extrapolation option is given.
  <br>If the bound is specified for a timeslice s being above the commodity timeslice resolution (com_tsl), the bound is applied to the sum of the commodity production variables (VAR_COMPRD) below it, according to the timeslice tree.
  <br>Standard aggregation.
  - Limit on the amount of a commodity produced (variable
  <br>VAR_COMPRD)
  <br>within a region for a particular timeslice.
  - The balance constraint is set to an equality (EQE_COMBAL).
  <br>Finer timeslice variables summed (EQ(l)\_BNDPRD).
  <br>or the bound is applied direct to the commodity production variable (VAR_COMPRD) when at the commodity level (com_tsl).
* - COM_BPRICE
  <br>(r,t,c,s,cur)
  - COM_ELAST, COM_STEP, COM_VOC
  - Monetary unit per commodity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: none
  - The control parameter \$SET TIMESED 'YES' to activate elastic demands must be set.
  - Base price of a demand commodity for the elastic demand formulation.
  - Controls the inclusion of the elastic demand variable (VAR_ELAST) in the commodity balance equation(EQ(l)\_COMBAL)
  <br>Applied to the elastic demand variable (VAR_ELAST) in the objective function (EQ_OBJELS).
* - COM_CSTNET
  <br>(r,datayear,c,s,cur)
  - OBJ_COMNT, CST_COMC, CST_PVC, rhs_combal, rcs_combal
  - Monetary unit per commodity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Cost on the net amount of a commodity within a region for a particular timeslice.
  - Forces the net commodity variable (VAR_COMNET) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Applied to said variable in the cost component of the objective function (EQ_OBJVAR).
* - COM_CSTPRD
  <br>(r,datayear,c,s,cur)
  - OBJ_COMPD, CST_COMC, CST_PVC, rhs_comprd, rcs_comprd
  - Monetary unit per commodity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Cost on the production of a commodity, within a region for a particular timeslice.
  - Forces the commodity production variable (VAR_COMPRD) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Applied to said variable in the cost component of the objective function (EQ_OBJVAR).
* - COM_CUMNET
  <br>(r,y1,y2,bd)
  - bohyear, eohyear, rhs_combal, rcs_combal, rtc_cumnet
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: not possible
  - The years y1 and y2 may be any years of the set allyear; where y1 may also be 'BOH' for first year of first period and y2 may be 'EOH' for last year of last period.
  - Bound on the cumulative net amount of a commodity between the years y1 and y2, within a region over timeslices.
  - Forces the net commodity variable (VAR_COMNET) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Generates the cumulative commodity constraint (EQ(l)\_CUMNET).
* - COM_CUMPRD
  <br>(r,y1,y2,bd)
  - bohyear, eohyear, rhs_comprd, rcs_comprd, rtc_cumprd
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: not possible
  - The years y1 and y2 may be any years of the set allyear; where y1 may also be 'BOH' for first year of first period and y2 may be 'EOH' for last year of last period.
  - Bound on the cumulative production of a commodity between the years y1 and y2 within a region over timeslices.
  - Forces the net commodity variable (VAR_COMPRD) to be included in the balance equation (EQE_COMBAL).
  <br>The cumulative constraint is generated (EQ(l)\_CUMPRD).
* - COM_ELAST
  <br>(r,datayear,c,s,lim)
  - COM_BPRICE, COM_STEP, COM_VOC, COM_AGG
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - The control parameter
  <br>\$SET TIMESED YES must be set to activate elastic demands.
  <br>An elasticity is required for each direction the demand is permitted to move.
  <br>The index lim = \'LO\' corresponds to demand decrease, while lim = \'UP\' denotes the direction for demand increase.
  <br>A different value may be provided for each direction, thus curves may be asymmetric.
  <br>Substitution elasticities can be defined with lim=\'N\', among a group of demands aggregated by COM_AGG.
  - Elasticity of demand indicating how much the demand rises/falls in response to a unit change in the marginal cost of meeting a demand that is elastic.
  <br>See also Appendix D for additional details on defining demand functions.
  - Controls the inclusion of the elastic demand variable (VAR_ELAST) in the commodity balance equation(EQ(l)\_COMBAL)
  <br>Applied to the elastic demand variable (VAR_ELAST) in the objective function costs (EQ_OBJELS).
* - COM_ELASTX
  <br>(r,datayear,c,bd)
  - COM_ELAST
  - Integer scalar
  <br>\[1,999\];
  <br>default value: none
  <br>Default extrapolation: MIG
  - Provided when shaping of elasticity based upon demand level is desired.
  <br>Note: Shape index 1 is reserved for constant 1.
  - Shape index for the elasticity of demand
  - Affects the demand elasticities applied in EQ_OBJELS
* - COM_FR
  <br>(r,datayear,c,s)
  - COM_PROJ, com_ts, com_tsl, RTCS_TSFR
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: timeslice duration (G_YRFR)
  <br>Default i/e: STD
  - Normally defined only for demand commodities (com_type = \'DEM\'), but can be applied to any commodity for defining load profiles.
  <br>Affects timeslice resolution at which a commodity is tracked (RTCS_TSFR), and thereby may affect when a process cannot operate (rtps_off).
  <br>Weighted inheritance.
  <br>Weighted aggregation.
  - Fraction of the annual demand (COM_PROJ) or commodity flow occurring in timeslice s; describes the shape of the load curve.
  - Applied to the annual demand (COM_PROJ) as the RHS of the balance equation (EQ(l)\_COMBAL).
  <br>Enters the peaking equation (EQ_PEAK), if a peaking commodity.
  <br>Applied to the bounds of elastic demand step variables (VAR_ELAST).
  <br>Applied via RTFCS_FR in all equations to flows having a timeslice level coarser than target level.
* - COM_IE
  <br>(r,datayear,c,s)
  - 
  - Decimal fraction
  <br>(0,∞);
  <br>default value: 1
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Infrastructure or transmission efficiency of a commodity.
  - Overall efficiency applied to the total production of a commodity in the commodity balance equation (EQ(l)\_COMBAL).
* - COM_MSHGV
  <br>(r,datayear,c)
  - NCAP_MSPRF
  - Unit: dimensionless
  <br>(0, ∞);
  <br>Default value: none
  <br>Default i/e: STD
  - Required for all markets modeled with the logit market sharing mechanism
  - In the logit market sharing mechanism, defines heterogeneity value for market **c** in region **r**, between the investment choices
  - EQ_MSNCAPB
* - COM_PKFLX
  <br>(r,datayear,c,s)
  - com_peak, com_pkts, COM_PKRSV, FLO_PKCOI
  - Scalar
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Difference between the average demand and the peak demand in timeslice s, expressed as fraction of the average demand.
  - Applied to the total consumption of a commodity to raise the capacity needed to satisfy the peaking constraint (EQ_PEAK).
* - COM_PKRSV
  <br>(r,datayear,c)
  - com_peak, com_pkts, COM_PKFLX, FLO_PKCOI
  - Scalar
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Requires that commodity c is also requested to have peaking constraints, by defining COM_PEAK or COM_PKTS
  - Peak reserve margin as fraction of peak demand, e.g. if COM_PKRSV = 0.2, the total installed capacity must exceed the peak load by 20%.
  - Applied to the total consumption of a commodity to raise the capacity needed to satisfy the peaking constraint (EQ_PEAK).
* - COM_PROJ
  <br>(r,datayear,c)
  - COM_FR
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - In standard usage, only applicable to demand commodities (com_type = 'DEM').
  <br>In advanced usage, may also be specified for other commodities for defining an exogenous demand.
  <br>Demand is allocated to sub-annual timeslices according to COM_FR.
  - Projected annual demand for a commodity.
  - Serves as the RHS (after COM_FR applied) of the commodity balance constraint (EQ(l)\_COMBAL).
  <br>Enters the peaking equation (EQ_PEAK), if a peaking commodity.
  <br>Applied when setting the upper bound of an elastic demand step (VAR_ELAST).
* - COM_STEP
  <br>(r,c,bd)
  - COM_BPRICE, COM_ELAST, COM_VOC, rcj
  - Integer number
  <br>\[1,∞);
  <br>default value: none
  - The control parameter \$SET TIMESED 'YES' must be set to activate elastic demands. The number of steps is required for each direction the demand is permitted to move.
  <br>The index bd=LO denotes the direction of demand decrease, bd=UP increase, and bd=FX is a shortcut for both. A different value may be provided for each direction, thus curves may be asymmetric.
  - Number of steps to use for the approximation of change of producer/consumer surplus when using the linearized elastic demand formulations.
  - Controls the instance of the elastic demand variable (VAR_ELAST) in:
  <br>the commodity balance equation (EQ(l)\_COMBAL);
  <br>setting of the step limit for the elastic demand variable (VAR_ELAST);
  <br>enters the objective function costs (EQ_OBJELS).
* - COM_SUBNET
  <br>(r,datayear,c,s,cur)
  - OBJ_COMNT, CST_COMX, CST_PVC, rhs_combal, rcs_combal
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Subsidy on the net amount of a commodity within a region for a particular timeslice.
  - Forces the net commodity variable (VAR_COMNET) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Applied (-) to said variable in the cost component of the objective function (EQ_OBJVAR).
* - COM_SUBPRD
  <br>(r,datayear,c,s,cur)
  - OBJ_COMPD, CST_COMX, CST_PVC, rhs_comprd, rcs_comprd
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Subsidy on the production of a commodity within a region for a particular timeslice.
  - Forces the commodity production variable (VAR_COMPRD) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Applied (-) to said variable in the cost component of the objective function (EQ_OBJVAR).
* - COM_TAXNET
  <br>(r,datayear,c,s,cur)
  - OBJ_COMNT, CST_COMX, CST_PVC, rhs_combal, rcs_combal
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Tax on the net amount of a commodity within a region for a particular timeslice.
  - Forces the net commodity variable (VAR_COMNET) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Applied to said variable in the cost component of the objective function (EQ_OBJVAR).
* - COM_TAXPRD
  <br>(r,datayear,c,s,cur)
  - OBJ_COMPD, CST_COMX, CST_PVC, rhs_comprd, rcs_comprd
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Tax on the production of a commodity within a region for a particular timeslice.
  - Forces the commodity production variable (VAR_COMPRD) to be included in the equality balance constraint (EQE_COMBAL).
  <br>Applied to said variable in the cost component of the objective function (EQ_OBJVAR).
* - COM_VOC
  <br>(r,datayear,c,bd)
  - COM_BPRICE, COM_STEP, COM_ELAST
  - Dimensionless
  <br>\[0,∞);
  <br>default: none
  <br>Default i/e: STD
  - The control parameter \$SET TIMESED 'YES' to activate elastic demands must be set.
  <br>A number is required for each direction the demand is permitted to move.
  <br>The index bd = LO corresponds to the direction of decreasing the demand, while bd = UP denotes the direction for demand increase.
  <br>A different value may be provided for each direction, thus curves may be asymmetric.
  - Possible variation of demand in both directions when using the elastic demand formulation.
  - Applied when setting the bound of an elastic demand step (VAR_ELAST).
  <br>Applied to the elasticity variable in the objective function costs (EQ_OBJELS).
* - DAM_BQTY
  <br>(r,c)
  - DAM_COST
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - Only effective when DAM_COST has been defined for commodity c.
  - Base quantity of emissions for damage cost accounting
  - EQ_DAMAGE, EQ_OBJDAM
* - DAM_COST
  <br>(r,datayear,c,cur)
  - DAM_BQTY
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Damage costs are by default endogenous (included in the objective).
  <br>To set them exogenous, use \$SET DAMAGE NO
  - Marginal damage cost of emissions at Base quantity.
  - EQ_DAMAGE, EQ_OBJDAM
* - DAM_ELAST
  <br>(r,c,lim)
  - DAM_COST, DAM_BQTY
  - Dimensionless
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - Only effective when DAM_COST has been defined for commodity c.
  - Elasticity of damage cost in the lower or upper direction from Base quantity.
  - EQ_OBJDAM
* - DAM_STEP
  <br>(r,c,lim)
  - DAM_COST, DAM_BQTY
  - Integer number
  <br>\[1,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - Only effective when DAM_COST has been defined for commodity c.
  - Number of steps for linearizing damage costs in the lower or upper direction from Base quantity.
  - EQ_DAMAGE, EQ_OBJDAM
* - DAM_VOC
  <br>(r,c,lim)
  - DAM_COST, DAM_BQTY
  - Decimal fraction
  <br>LO: \[0,1\]; UP: \[0,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - Only effective when DAM_COST is defined for c. Step sizes proportional to the Base quantity can be defined with lim=\'N\'.
  - Variance of emissions in the lower or upper direction from Base quantity as a fraction of Base quantity.
  - EQ_OBJDAM
* - E
  <br>(t)
  - B, D, M, COEF_CPT, rtp_vintyr
  - 
  - For each modelyear period
  - End year of period t, used in determining the length of each period
  - The amount of new investment (VAR_NCAP) carried over in the capacity transfer constraint (EQ(l)\_CPT).
  <br>Amount of investments (VAR_NCAP) remaining past the modelling horizon that needs to be credited back to the objective function (EQ_OBJINV).
* - FLO_BND
  <br>(r,datayear,p,cg,s,bd)
  - 
  - Commodity unit
  <br>\[0,∞);
  <br>default: none
  <br>Default i/e: MIG
  - If the bound is specified for a timeslice s being above the flow timeslice resolution (rtpcs_varf), the bound is applied to the sum of the flow variables (VAR_FLO) according to the timeslice tree, otherwise directly to the flow variable.
  <br>No aggregation.[^29]
  - Bound on the flow of a commodity or the sum of flows within a commodity group.
  - Flow activity limit constraint (EQ(l)\_FLOBND) when s is above rtpcs_varf
  <br>Direct bound on activity variable (VAR_FLO) when at the rtpcs_varf level.
* - FLO_COST
  <br>(r,datayear,p,c,s,cur)
  - OBJ_FCOST, CST_FLOC, CST_PVP
  - Monetary unit per commodity unit
  <br>\[open\];
  <br>default: none
  <br>Default i/e: STD
  - Direct inheritance
  <br>Weighted aggregation
  - Variable cost of a process associated with the production/ consumption of a commodity.
  - Applied to the flow variable (VAR_FLO) when entering the objective function (EQ_OBJVAR).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - FLO_CUM
  <br>(r,p,c,y1,y2,bd)
  - ACT_CUM
  - Flow unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - The years y1 and y2 may be any years of the set allyear; where y1 may also be \'BOH\' for first year of first period and y2 may be \'EOH\' for last year of last period.
  - Bound on the cumulative amount of annual process activity between the years y1 and y2, within a region.
  - Generates an instance of the cumulative constraint (EQ_CUMFLO)
* - FLO_DELIV
  <br>(r,datayear,p,c,s,cur)
  - OBJ_FDELV, CST_FLOC, CST_PVP
  - Monetary unit per commodity unit
  <br>\[open\];
  <br>default: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Cost of a delivering (consuming) a commodity to a process.
  - Applied to the flow variable (VAR_FLO) when entering the objective function (EQ_OBJVAR).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - FLO_EFF
  <br>(r,datayear,p,cg,c,s)
  - FLO_EMIS, PRC_ACTFLO
  - Commodity unit of c / commodity unit of cg
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Inherited/aggregated to the timeslice levels of the flow variables of the commodities in group cg. All parameters with the same process (p) and target commodity (c) are combined in the same transformation equation.
  <br>By using cg=\'ACT\', the attribute will be defined per unit of activity, by applying it on all PCG flows with the value divided by any user-defined PRC_ACTFLO.
  <br>FLO_EFF defined for an individual flow will override any value for a group.
  - Defines the amount of commodity flow of commodity (c) per unit of other process flow(s) or activity (cg).
  - Generates process transformation equation (EQ_PTRANS) between one or more input (or output) commodities and one output (or input) commodities.
* - FLO_EMIS
  <br>(r,datayear,p,cg,com,s)
  - FLO_EFF (alias)
  - Commodity unit of c / commodity unit of cg
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - See FLO_EFF.
  <br>If com is of type ENV and is not in the process topology, it is added to it as an output flow.
  - Defines the amount of emissions (c) per unit of process flow(s) or activity (cg).
  - See FLO_EFF.
* - FLO_FR
  <br>(r,datayear,p,c,s,bd)
  - 
  - Decimal fraction
  <br>\[0,1\] / \[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - FLO_FR may be specified as lower, upper or fixed bounds, in contrast to COM_FR.
  <br>Can be specified for any flow variable having a subannual timeslice resolution.
  <br>Weighted aggregation.
  <br>Direct inheritance, if defined at the ANNUAL level.
  - 1\) Bounds the flow of commodity (c) entering or leaving process (p) in a timeslice, in proportion to annual flow.
  <br>2\) If specified also at the ANNUAL level, bounds the flow **level** in proportion to the average level under the parent timeslice
  - A share equation (EQ(l)\_FLOFR) limiting the amount of commodity (c) is generated according to the bound type (bd = l indicator).
* - FLO_FUNC
  <br>(r,datayear,p,cg1,cg2,s)
  - FLO_SUM, FLO_FUNCX, COEF_PTRAN, rpc_ffunc, rpcg_ptran
  - Commodity unit of cg2/commodity unit of cg1
  <br>\[open\];
  <br>default value: see next column
  <br>Default i/e: STD
  - If for the same indexes the parameter FLO_SUM is specified but no FLO_FUNC, the FLO_FUNC is set to 1.
  <br>Important factor in determining the level at which a process operates in that the derived transformation parameter (COEF_PTRAN) is inherited/aggregated to the timeslice levels of the flow variables associated with the commodities in the group cg1.
  - A key parameter describing the basic operation of or within a process. Sets the ratio between the sum of flows in commodity group cg2 to the sum of flows in commodity group cg1, thereby defining the efficiency of producing cg2 from cg1 (subject to any FLO_SUM). cg1 and cg2 may be also single commodities.
  - Establishes the basic transformation relationship (EQ_PTRANS) between one or more input (or output) commodities and one or more output (or input) commodities.
  <br>Establishes the relationship between storage charging / discharging and a related commodity flow (VAR_FLO) in the auxiliary storage flow equation (EQ_STGAUX).
* - FLO_FUNCX
  <br>(r,datayear,p,cg1,cg2)
  - FLO_FUNC, FLO_SUM, COEF_PTRAN
  - Integer scalar
  <br>\[1,999\];
  <br>default value: none
  <br>Default extrapolation: MIG
  - Provided when shaping based upon age is desired.
  <br>Vintaged processes only
  <br>(or for NCAP_COM flows).
  <br>Note: Shape index 1 is reserved for constant 1.
  <br>ACT_EFF(cg): cg1=cg, cg2=\'ACT\'
  <br>ACT_FLO(cg): cg1=\'ACT\', cg2=cg
  <br>FLO_EMIS(cg,c): cg1=cg2=c
  <br>FLO_EFF(cg,c): cg1=cg2=c
  <br>FLO_FUNC(cg1,cg2): cgN=cgN
  <br>NCAP_COM(com): cg1=\'CAPFLO\', cg2=com
  - Age-based shaping curve (SHAPE) to be applied to the flow parameters (ACT_EFF/ACT_FLO/ FLO_FUNC/FLO_SUM/FLO_EMIS/FLO_EFF/ NCAP_COM)
  - Applied to the flow variable (VAR_FLO) in a transformation equation (EQ_PTRANS / EQE_ACTEFF) to account for changes in the transformation efficiency according to the age of each process vintage.
* - FLO_MARK
  <br>(r,datayear,p,c,bd)
  - PRC_MARK
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: none
  <br>Default i/e: STD
  - The same given fraction is applied to all timeslices of the commodity (this could be generalized to allow time-slice-specific fractions, if deemed useful).
  <br>If an ANNUAL level market-share is desired for a timesliced commodity, PRC_MARK can be used instead.
  - Process-wise market share in total commodity production.
  - The individual process flow variables (VAR_FLO, VAR_IN, VAR_STGIN/OUT) are constrained (EQ(l)\_FLOMRK) to a fraction of the total production of a commodity (VAR_COMPRD).
  <br>Forces the commodity production variable (VAR_COMPRD) to be included in the equality balance constraint (EQE_COMBAL).
* - FLO_PKCOI
  <br>(r,datayear,p,c,s)
  - COM_PKRSV, COM_PKFLX, com_peak, com_pkts
  - Scalar
  <br>\[open\];
  <br>default value: 1
  <br>Default i/e: STD
  - FLO_PKCOI is specified for individual processes p consuming the peak commodity c.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  <br>Used when the timeslices are not necessarily fine enough to pick up the actual peak within the peak timeslices.
  - Factor that permits attributing more (or less) demand to the peaking equation (EQ_PEAK) than the average demand calculated by the model, to handle the situation where peak usage is typically higher (or lower) due to coincidental (or non-coincidental) loads at the time of the peak demand.
  - Applied to the flow variable (VAR_FLO) to adjust the amount of a commodity consumed when considering the average demand contributing to the peaking constraint (EQ_PEAK).
* - FLO_SHAR
  <br>(r,datayear,p,c,cg,s,bd)
  - 
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: none
  <br>Default i/e: MIG over milestoneyears, STD over pastyears
  - Direct inheritance.
  <br>Weighted aggregation.
  <br>A common example of using FLO_SHAR is to specify the power-to-heat ratio of CHP plants in the backpressure point. For example, for a heat output of a CHP technology, the FLO_SHAR parameter would have the value CHPR/(1+CHPR), with CHPR being the heat-to-power ratio.
  - Share of flow commodity c based upon the sum of individual flows defined by the commodity group cg belonging to process p.
  - When the commodity is an input an EQ(l)\_INSHR equation is generated.
  <br>When the commodity is an output an EQ(l)\_OUTSHR equation is generated.
* - FLO_SUB
  <br>(r,datayear,p,c,s,cur)
  - OBJ_FSUB, CST_FLOX, CST_PVP
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Subsidy on a process flow.
  - Applied with a minus sign to the flow variable (VAR_FLO) when entering the objective function (EQ_OBJVAR).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - FLO_SUM
  <br>(r,datayear,p,cg1,c,cg2,s)
  - FLO_FUNC, FLO_FUNCX, COEF_PTRANS, fs_emis, rpc_emis, rpc_ffunc, rpcg_ptran
  - Commodity unit of cg2/commodity unit of c
  <br>\[open\];
  <br>default value: see next column
  <br>Default i/e: STD
  - If a FLO_SUM is specified and no corresponding FLO_FUNC, the FLO_FUNC is set to 1.
  <br>If FLO_FUNC is specified for a true commodity group cg1, and no FLO_SUM is specified for the commodities in cg1, these FLO_SUM are set to 1.
  <br>The derived parameter COEF_PTRANS is inherited/aggregated to the timeslice level of the flow variable of the commodity c.
  - Multiplier applied for commodity c of group cg1 corresponding to the flow rate based upon the sum of individual flows defined by the commodity group cg2 of process p. Most often used to define the emission rate, or to adjust the overall efficiency of a technology based upon fuel consumed.
  - The FLO_SUM multiplier is applied along with FLO_FUNC parameter in the transformation coefficient (COEF_PTRANS), which is applied to the flow variable (VAR_FLO) in the transformation equation (EQ_PTRANS).
* - FLO_TAX
  <br>(r,datayear,p,c,s,cur)
  - OBJ_FTAX, CST_FLOX, CST_PVP
  - Monetary unit per commodity unit
  <br>\[0,∞);
  <br>default: none
  <br>Default i/e: STD
  - Direct inheritance.
  <br>Weighted aggregation.
  - Tax on a process flow.
  - Applied to the flow variable (VAR_FLO) when entering the objective function (EQ_OBJVAR).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - G_CUREX
  <br>(cur1,cur2)
  - R_CUREX
  - Scalar
  <br>(0,∞)
  <br>Default value: none
  - The target currency cur2 must have a discount rate defined with G_DRATE.
  - Conversion factor from currency cur1 to currency cur2, with cur2 to be used in the objective function.
  - Affects cost coefficients in EQ_OBJ
* - G_CYCLE
  <br>(tslvl)
  - TS_CYCLE
  - Number of cycles
  <br>\[1,∞);
  <br>Default values:
  <br>- 1 for ANNUAL
  <br>- 1 for SEASON
  <br>- 52 for WEEKLY
  <br>- 365 for DAYNITE
  - Not recommended to be changed; use TS_CYCLE instead, whenever the timeslice cycles are different from the default, because changing G_CYCLE would change the meaning of storage availability factors.
  - Defines the total number of cycles on level tslvl, in a year.
  <br>Provides default values for TS_CYCLE (see entry for that).
  - Affects interpretation of availability factors for the storage level, whenever capacity represents the maximum nominal output level (EQ(l)\_CAPACT, EQL_CAPFLO).
* - G_DRATE
  <br>(r,allyear,cur)
  - OBJ_DISC, OBJ_DCEOH, NCAP_DRATE, COR_SALVI, COR_SALVD, COEF_PVT, VDA_DISC
  - Decimal fraction
  <br>(0,1\];
  <br>default value = none
  <br>Default i/e: STD
  - A value must be provided for each region. Interpolation is dense (all individual years included).
  - System-wide discount rate in region r for each time-period.
  - The discount rate is taken into consideration when constructing the objective function discounting multiplier (OBJ_DISC), which is applied in each components of the objective function (EQ_OBJVAR, EQ_OBJINV, EQ_OBJFIX, EQ_OBJSALV, EQ_OBJELS).
* - G_DYEAR
  - OBJ_DISC, COEF_PVT
  - Year
  <br>\[BOTIME,EOTIME\];
  <br>default value = M(MIYR_1), i.e. the first milestone year
  - 
  - Base year for discounting.
  - The year to which all costs are to be discounted is taken into consideration when constructing the objective function discounting multiplier (OBJ_DISC), which is applied in each of the components of the objective function (EQ_OBJVAR, EQ_OBJINV, EQ_OBJFIX, EQ_OBJSALV, EQ_OBJELS).
* - G_RFRIR
  <br>(r,allyear)
  - G_DRATE, NCAP_DRATE, COR_SALVI, COR_SALVD
  - Decimal fraction
  <br>(0,1\];
  <br>default value = none
  <br>Default i/e: STD
  - Optional parameter.
  <br>If value is not provided, G_DRATE is assumed as the risk-free rate.
  <br>By providing G_RFRIR, the technology-specific risk premiums can be kept unchanged over any sensitivity analyses with different G_DRATE values.
  - Risk-free real interest rate in region r for each time-period.
  <br>Provides the reference rate for NCAP_DRATE, such that the risk premium will be calculated against the risk-free rate.
  - The rate is taken into consideration when constructing the objective function coefficients for investment costs. EQ_OBJINV, EQ_OBJSALV
* - G_ILEDNO
  - NCAP_ILED
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: 0.1
  - Only provided when the costs associated with the lead-time for new capacity (NCAP_ILED) are not to be included in the objective function.
  <br>Not taken into account if the OBLONG switch or any alternative objective formulation is used.
  - If the ratio of lead-time (NCAP_ILED) to the period duration (D) is below this threshold then the lead-time consideration will be ignored in the objective function costs.
  - Prevents the investment costs associated with investment lead-times from energy the investment component of the objective function (EQ_OBJINV).
* - G_NOINTERP
  - All parameters that are normally subjected to interpolation / extrapolation
  - Binary indicator
  <br>\[0 or 1\];
  <br>default value = 0
  - Only provide when interpolation / extrapolation is to be turned off for all parameters.
  <br>Interpolation of cost parameters is always done.
  - Switch for generally turning-on (= 0 ) and turning-off (= 1 ) sparse inter- / extrapolation.
  - 
* - G_OFFTHD
  <br>(datayear)
  - PRC_NOFF, PRC_AOFF, PRC_FOFF, COM_OFF
  - Scalar
  <br>\[0,1\]
  <br>Default value: 0
  <br>Default i/e: 5
  - Setting G_OFFTHD=1 will make the \*\_OFF attributes effective only for periods fully included in the OFF range specified.
  - Threshold for considering an \*\_OFF attribute disabling a process/commodity variable in period.
  - Affects availability of VAR_NCAP, VAR_ACT, VAR_FLO, VAR_COMNET/PRD
* - G_OVERLAP
  - 
  - Scalar
  <br>\[0,100\]
  <br>Default value: TIMESTEP/2
  - Used only when time-stepped solution is activated with the TIMESTEP control variable.
  - Overlap of stepped solutions (in years).
  - <span>--</span>
* - G_TLIFE
  - NCAP_TLIFE
  - Scalar
  <br>\[1,∞);
  <br>default value = 10
  - 
  - Default value for the technical lifetime of a process if not provided by the user.
  - 
* - G_YRFR
  <br>(all_r,s)
  - RTCS_TSFR, RS_STGPRD
  - Fraction
  <br>\[0,1\];
  <br>default value: none; only for the ANNUAL timeslice a value of 1 is predefined
  - Must be provided for each region and timeslice.
  - Duration of timeslice s as fraction of a year. Used for shaping the load curve and lining up timeslice duration for inter-regional exchanges.
  - Applied to various variables (VAR_NCAP+PASTI, VAR_COMX, VAR_IRE, VAR_FLO, VAR_SIN/OUT) in the commodity balance equation (EQ(l)\_COMBAL).
* - IRE_BND
  <br>(r,datayear,c,s,all_r,ie,bd)
  - top_ire
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Only applicable for inter-regional exchange processes (IRE).
  <br>If the bound is specified for a timeslice (s) being above the commodity (c) timeslice resolution, the bound is applied to the sum of the imports/exports according to the timeslice tree.
  <br>Standard aggregation.
  - Bound on the total import (export) of commodity (c) from (to) region all_r in (out of) region r.
  - Controls the instances for which the trade bound constraint (EQ(l)\_IREBND) is generated, and the RHS.
* - IRE_CCVT
  <br>(r1,c1,r2,c2))
  - IRE_TSCVT, top_ire
  - Scalar
  <br>(0,∞)
  <br>Default value: 1 if commodity names are the same in both regions
  <br>I/e: N/A
  - Required for mapping commodities involved in inter-regional exchanges between two regions whenever commodities traded are in different units in the regions.
  - Conversion factor between commodity units in region r1 and region r2. Expresses the amount of commodity c2 in region r2 equivalent to 1 unit of commodity c1 in region r1.
  - The conversion factor is applied to the flow variable (VAR_IRE) in the inter-regional balance constraint (EQ_IRE).
  <br>Similarly, applied to the flow variable (VAR_IRE) when an inter-regional exchange is bounded in the limit constraint (EQ(l)\_IREBND).
  <br>Similarly, applied to the flow variable (VAR_IRE) when an exchange with an external region is bounded (EQ(l)\_XBND).
* - IRE_FLO
  <br>(r1,datayear,p,c1,r2,c2,s2)
  - top_ire
  - Commodity unit c2/commodity unit c1
  <br>\[0,∞);
  <br>default value: 1
  <br>Default i/e: STD
  - Only applicable for inter-regional exchange processes (IRE) between two internal regions.
  <br>Note that for each direction of trade a separate IRE_FLO needs to be specified.
  <br>Similar to FLO_FUNC for standard processes.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Efficiency of exchange process from commodity c1 in region r1 to commodity c2 in the region2 in timeslice s2; the timeslice s2 refers to the r2 region.
  - Applied to the exchange flow variable (VAR_IRE) in the inter-regional trade equation (EQ_IRE).
  <br>Applied to the exchange flow variable (VAR_IRE) when a bound on inter-regional trade is to be applied (EQ(l)\_IREBND).
* - IRE_FLOSUM
  <br>(r,datayear,p,c1,s,ie,c2,io)
  - top_ire
  - Commodity unit c2/commodity unit c1
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Only applicable for inter-regional exchange processes (IRE).
  <br>Since the efficiency IRE_FLO can only be used for exchange between internal regions, IRE_FLOSUM may be used to define an efficiency for an import/export with an external region by specifying the same commodity for c1 and c2 and the value 1-efficiency as auxiliary consumption.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Auxiliary consumption (io = IN, owing to the commodity entering the process) or production/ emission (io = OUT, owing to the commodity leaving the process) of commodity c2 due to the IMPort / EXPort (index ie) of the commodity c1 in region r[^30]
  - The multiplier is applied to the flow variable (VAR_IRE) associated with an inter-reginal exchange in the commodity balance constraint (EQ(l)\_COMBAL).
  <br>If a flow share (FLO_SHAR) is provided for an inter-regional exchange process then the multiplier is applied to the flow variable (VAR_IRE) in the share constraint (EQ(l)\_IN/OUTSHR).
  <br>If a cost is provided for the flow (FLO_COST or FLO_DELIV) then the factor is applied to the flow variable (VAR_IRE) in the variable component of the objective function (EQ_OBJVAR).
* - IRE_PRICE
  <br>(r,datayear,p,c,s,all_r,ie,cur)
  - OBJ_IPRIC, CST_COMC, CST_PVP, top_ire
  - Monetary unit / commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Only applicable for inter-regional exchange processes (IRE).
  <br>Ignored if all_r is an internal region.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - IMPort/EXPort price (index ie) for to/from an internal region of a commodity (c) originating from/heading to an external region all_r.
  - The price of the exchange commodity is applied to the trade flow variable (VAR_IRE) in the variable costs component of the objective function (EQ_OBJVAR).
* - IRE_TSCVT
  <br>(r1,s1,r2,s2)
  - IRE_CCVT, top_ire
  - Scalar
  <br>(0,∞);
  <br>default value: 1 if timeslice tree and names are the same in both regions
  <br>I/e: N/A
  - Used for mapping timeslices in different regions.
  <br>Required if timeslice definitions are different in the regions.
  - Matrix for mapping timeslices; the value for (r1,s1,r2,s2) gives the fraction of timeslice s2 in region r2 that falls in timeslice s1 in region r1.
  - The conversion factor is applied to the flow variable (VAR_IRE) in the inter-regional balance constraint (EQ_IRE).
  <br>Similarly, applied to the flow variable (VAR_IRE) when an inter-regional exchange is bounded in the limit constraint (EQ(l)\_IREBND).
  <br>Similarly, applied to the flow variable (VAR_IRE) when an exchange with an external region is bounded (EQ(l)\_XBND).
* - IRE_XBND
  <br>(all_r,datayear,c,s ie,bd)
  - top_ire
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Only applicable for inter-regional exchange processes (IRE).
  <br>Provide whenever a trade flow is to be constrained.
  <br>Note that the limit is either imposed by summing lower or splitting higher flow variables (VAR_IRE) when specified at other than the actual flow level (as determined by the commodity and process levels (COM_TSL/ PRC_TSL ).
  - Bound on the total IMPort (EXPort) (index ie) of commodity c in region all_r with all sources (destinations).
  - The trade limit equation EQ(l)\_XBND generated either sums lower flow variables (VAR_IRE) or splits (according to the timeslice tree) coarser variables.
* - MULTI
  <br>(j,allyear)
  - NCAP_AFM, NCAP_FOMM, NCAP_FSUBM, NCAP_FTAXM
  - Scalar
  <br>\[open\];
  <br>default value: none
  <br>I/e: Full dense interpolation and extrapolation
  - Only provided when the related shaping parameters are to be used.
  - Multiplier table used for any shaping parameters (\*\_\*M) to adjust the corresponding technical data as function of the year; the table contains different multiplier curves identified by the index j.
  - *{See Related Parameters}*
* - NCAP_AF
  <br>(r,datayear,p,s,bd)
  - NCAP_AFA, NCAP_AFS, NCAP_AFM, NCAP_AFX, COEF_AF
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: 1
  <br>Default i/e: STD
  <br>Remark: In special cases values \>1 can also be used (when PRC_CAPACT does not represent the max. technical level of activity per unit of capacity).
  - NCAP_AF, NCAP_AFA and NCAP_AFS can be applied simultaneously.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  <br>(Important remark: No inheritance/aggregation if any value is specified at process timeslices.)
  - Availability factor relating a unit of production (process activity) in timeslice s to the current installed capacity.
  - The corresponding capacity-activity constraint (EQ(l)\_CAPACT) will be generated for any timeslice s.
  <br>If the process timeslice level (PRC_TSL) is below said level, the activity variables will be summed.
* - NCAP_AFA
  <br>(r,datayear,p,bd)
  - NCAP_AFA, NCAP_AFS, NCAP_AFM, NCAP_AFX, COEF_AF
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: none
  <br>Default i/e: STD
  <br>Remark: In special cases values \>1 can also be used (when PRC_CAPACT has been chosen not to represent the max. technical level of activity per unit of capacity).
  - Provided when 'ANNUAL' level process operation is to be controlled.
  <br>NCAP_AF, NCAP_AFA and NCAP_AFS can be applied simultaneously.
  <br>NCAP_AFA is always assumed to be non-vintage dependent, even if the process is defined as a vintaged one; for vintage-dependent annual availability NCAP_AFS with s='ANNUAL' can be used.
  - Annual availability factor relating the annual activity of a process to the installed capacity.
  - The corresponding capacity-activity constraint (EQ(l)\_CAPACT) will be generated for the 'ANNUAL' timeslice.
  <br>If the process timeslice level (PRC_TSL) is below said level, the activity variables will be summed.
* - NCAP_AFC
  <br>(r,datayear,p,cg,tsl)
  - NCAP_AFCS
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - If the commodities are in the PCG, constraint is applied to the flows in the PCG as a whole (linear combination of flows).
  <br>Independent equations are generated for commodities not in the PCG, or when NCAP_AFC(r,'0',p,'ACT',tsl)=--1 is also specified.
  - Commodity-specific availability of capacity for commodity group cg, at given timeslice level.
  <br>Applies also matching NCAP_AF / AFS / AFA as a multiplier, unless the independent option is used.
  - Generates instances of
  <br>EQ(l)\_CAFLAC (thereby disabling EQ(l)\_CAPACT generation), or EQL_CAPFLO.
* - NCAP_AFCS
  <br>(r,datayear,p,cg,ts)
  - NCAP_AFC
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - See NCAP_AFC.
  <br>NCAP_AFCS is similar to NCAP_AFC but is defined on individual timeslices. Overrides NCAP_AFC.
  - Commodity-specific availability of capacity for commodity group cg, timeslice-specific.
  - See NCAP_AFC.
* - NCAP_AFM
  <br>(r,datayear,p)
  - NCAP_AF, NCAP_AFA, NCAP_AFS, MULTI, COEF_AF
  - Integer number
  <br>Default value: 0 (no multiplier applied)
  <br>Default extrapolation: MIG
  - Provided when multiplication of NCAP_AF / NCAP_AFS based upon year is desired.
  <br>Note: Multiplier index 1 is reserved for constant 1.
  - Period sensitive multiplier curve (MULTI) to be applied to the availability factor parameters (NCAP_AF/AFA/AFS) of a process.
  - *{See Related Parameters}*
* - NCAP_AFS
  <br>(r,datayear,p,s,bd)
  - 
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: none
  <br>Default i/e: STD
  <br>Remark: In special cases values \>1 can also be used (in cases where PRC_CAPACT has been chosen not to represent the maximum technical level of activity per unit of capacity).
  - NCAP_AF, NCAP_AFA and NCAP_AFS can be applied simultaneously.
  <br>NCAP_AFS being specified for timeslices s being below the process timeslice level are ignored.
  <br>No inheritance.
  <br>No aggregation.
  <br>Can be used also on the process timeslices, and will then override the levelized NCAP_AF availability factors.
  - Availability factor relating the activity of a process in a timeslice s being at or above the process timeslice level (prc_tsl) to the installed capacity. If for example the process timeslice level is 'DAYNITE' and NCAP_AFS is specified for timeslices on the 'SEASONAL' level, the sum of the 'DAYNITE' activities within a season are restricted, but not the 'DAYNITE' activities directly.
  - The corresponding capacity-activity constraint (EQ(l)\_CAPACT) will be generated for a timeslice s being at or above the process timeslice level (prc_tsl).
  <br>If the process timeslice level is below said level, the activity variables will be summed.
* - NCAP_AFSX
  <br>(r,datayear,p,bd)
  - NCAP_AFS, SHAPE, COEF_AF
  - Integer number
  <br>Default value: 0 (no shape curve applied)
  <br>Default extrapolation: MIG
  - Provided when shaping based upon age is desired.
  <br>NCAP_AFSX is applied to NCAP_AFS, but not on the annual level if availability is also defined by NCAP_AFA.
  <br>The SHAPE parameter is applied even for non-vintaged process whenever NCAP_AFSX is specified, i.e. NCAP_AFS availabilities will then be vintaged.
  <br>Note: Shape index 1 is reserved for constant 1.
  - Age-based shaping curve (SHAPE) to be applied to the seasonal availability factor parameters (NCAP\_ AFS) of a process.
  - *{See Related Parameters}*
* - NCAP_AFX
  <br>(r,datayear,p)
  - NCAP_AF, NCAP_AFA, NCAP_AFS, SHAPE, COEF_AF
  - Integer number
  <br>Default value: 0 (no shape curve applied)
  <br>Default extrapolation: MIG
  - Provided when shaping based upon age is desired.
  <br>NCAP_AFX is applied to NCAP_AF and NCAP_AFS, but not the annual availability NCAP_AFA.
  <br>For non-vintaged process, the SHAPE parameter is only applied to NCAP_AF, i.e. availabilities at process timeslices will be vintaged.
  <br>Note: Shape index 1 is reserved for constant 1.
  - Age-based shaping curve (SHAPE) to be applied to the availability factor parameters (NCAP_AF/AFA/AFS) of a process.
  - *{See Related Parameters}*
* - NCAP_BND
  <br>(r,datayear,p,bd)
  - 
  - Capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Provided for each process to have its overall installed capacity (VAR_NCAP) limited in a period.
  <br>Since inter-/extrapolation default is MIG, a bound must be specified for each period desired, if no explicit inter-/extrapolation option is given, e.g. NCAP_BND(R,'0',P) =2.
  - Bound on the permitted level on investment in new capacity
  - Imposes an indirect limit on the capacity transfer equation (EQ_CPT) by means of a direct bound on the new investments capacity variable (VAR_NCAP).
* - NCAP_BPME
  <br>(r,datayear,p)
  - NCAP_CDME
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - The parameter is only taken into account when the process is of type CHP, and NCAP_CDME has been also defined.
  - Back pressure mode efficiency (or total efficiency in full CHP mode).
  - Process transformation equation, either EQE_ACTEFF or EQ_PTRANS
* - NCAP_CDME
  <br>(r,datayear,p)
  - NCAP_BPME
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - The parameter can only be used for standard processes having electricity output in the PCG. The efficiency is applied between the default shadow group and the electricity. If the process is also defined as a CHP, heat efficiency is also included.
  - Condensing mode efficiency
  - Process transformation equation, either EQE_ACTEFF or EQ_PTRANS
* - NCAP_CEH
  <br>(r,datayear,p)
  - NCAP_CHPR, ACT_EFF
  - Decimal fraction
  <br>\[--1,∞\];
  <br>default value: none
  <br>Default i/e: STD
  - The parameter is only taken into account when the process is defined to be of type CHP. According to the CEH value, the process activity will be defined as:
  <br>CEH ≤ 0: Max. electricity output according to CHPR
  <br>0 \< CEH ≤1: Condensing mode electricity output
  <br>CEH ≥ 1: Total energy output in full CHP mode.
  - Coefficient of electricity to heat along the iso-fuel line in a pass-out CHP technology.
  - Process transformation equation, either EQE_ACTEFF or EQ_PTRANS
* - NCAP_CHPR
  <br>(r,datayear,p,lim)
  - FLO_SHAR
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: 1 (only when process type is CHP, for lim=\'UP\')
  <br>Default i/e: STD
  - The parameter is only taken into account when the process is defined to be of type CHP. The defaults can be disabled by defining any i/e value with lim=\'N\', which will eliminate the output share equations.
  - Heat-to-power ratio of a CHP technology (fixed / minimum / maximum ratio). If no ratio equations should be generated, one can define any I/E value with lim=\'N\'.
  - Activates the generation of output share equations, implemented with EQ(l)\_OUTSHR
* - NCAP_CLAG
  <br>(r,datayear,p,c,io)
  - NCAP_CLED, NCAP_COM
  - Years
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a delay in commodity output after commissioning new capacity. So, if the process is available in the year K, the commodity is produced during the years \[K+CLAG, K+NCAP_TLIFE--1\].
  - Lagtime of a commodity after new capacity is installed.
  - Applied to the investment variable (VAR_NCAP) in the commodity balance (EQ(l)\_COMBAL) of the investment period or previous periods.
* - NCAP_CLED
  <br>(r,datayear,p,c)
  - NCAP_ICOM, COEF_ICOM
  - Years
  <br>\[open\];
  <br>default value: = NCAP_ILED
  <br>Default i/e: STD
  - Provided when a commodity must be available prior to availability of a process. So, if the process is available in the year B(v) +NCAP_ILED--1, the commodity is produced during the time span \[B(v)+ILED--CLED, B(v) +NCAP_ILED--1\].
  <br>Usually used when modelling the need for fabrication of reactor fuel the period before a reactor goes online.
  - Lead time requirement for a commodity during construction (NCAP_ICOM), prior to the initial availability of the capacity.
  - Applied to the investment variable (VAR_NCAP) in the commodity balance (EQ(l)\_COMBAL) of the investment period or previous periods.
* - NCAP_COM
  <br>(r,datayear,p,c,io)
  - rpc_capflo, rpc_conly
  - Commodity unit per capacity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Provided when the consumption or production of a commodity is tied to the level of the installed capacity.
  - Emission (or land-use) of commodity c associated with the capacity of a process for each year said capacity exists.
  - Applied to the capacity variable (VAR_CAP) in the commodity balance (EQ_COMBAL).
* - NCAP_COST
  <br>(r,datayear,p)
  - OBJ_ICOST, OBJSCC, CST_INVC, CST_PVP
  - Monetary unit per capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided whenever there is a cost associated with putting new capacity in place.
  - Investment costs of new installed capacity according to the installation year.
  - Applied to the investment variable (VAR_NCAP) when entering the objective function (EQ_OBJNV).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - NCAP_CPX
  <br>(r,datayear,prc)
  - COEF_CPT
  - Integer number
  <br>Default value: 0
  <br>(no shape curve applied)
  <br>Default extrapolation:
  <br>MIG
  - Provided when shaping based upon age is desired.
  <br>The SHAPE index given by NCAP_CPX is applied to the internal capacity transfer parameter (COEF_CPT).
  <br>Note: Shape index 1 is reserved for constant 1.
  - Defines a shape index for shaping the capacity transfer coefficients by the age of each process vintage. As a result, the capacity will have a survival rate as a function of age.
  - Impacts all calculations that are dependent upon the availability of capacity (VAR_NCAP), most directly the capacity transfer (EQ_CPT), and capacity availability equations (EQ(l)\_CAPACT).
* - NCAP_DCOST
  <br>(r,datayear,p,cur)
  - NCAP_DLAG, COR_SALVD, OBJ_DCOST, CST_DECC, CST_PVP
  - Monetary unit per capacity unit
  <br>\[0,∞); default value: none
  <br>Default i/e: STD
  - Provided when there are decommissioning costs associated with a process.
  <br>Decommissioning of a process and the payment of decommissioning costs may be delayed by a lag time (NCAP_DLAG).
  - Cost of dismantling a facility after the end of its lifetime.
  - Applied to the current capacity subject to decommissioning (VAR_NCAP+NCAP_PASTI) when entering the objective function (EQ_OBJNV).
* - NCAP_DELIF
  <br>(r,datayear,p)
  - NCAP_DLIFE, COR_SALVD, DUR_MAX, OBJ_CRFD, SALV_DEC
  - Years
  <br>(0,∞);
  <br>default value: NCAP_DLIFE
  <br>Default i/e: STD
  - Provided when the timeframe for paying for decommission is different from that of the actual decommissioning.
  - Economic lifetime of the decommissioning activity.
  - Applied to the investment variable (VAR_NCAP) when entering the salvage portion of the objective function (EQ_OBJSALV).
* - NCAP_DISC
  <br>(r,datayear,p,unit)
  - rp_dscncap
  - Capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Used for lumpy investments.
  <br>Requires MIP.
  <br>Since inter-/extrapolation default is MIG, a value must be specified for each period desired, if no explicit inter-/extrapolation option is given.
  - Size of capacity units that can be added.
  - Applied to the lumpy investment integer variable (VAR_DNCAP) in the discrete investment equation (EQ_DSCNCAP) to set the corresponding standard investment variable level (VAR_NCAP).
* - NCAP_DLAG
  <br>(r,datayear,p)
  - COEF_OCOM, DUR_MAX, OBJ_DLAGC
  - Years
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a lag in the decommissioning of a process (e.g., to allow the nuclear core to reduce its radiation).
  - Number of years delay before decommissioning can begin after the lifetime of a technology has ended.
  - Delay applied to a decommissioning flow (VAR_FLO) in the balance equation (EQ(l)\_COMBAL) as production.
  <br>Delay applied to the current capacity subject to decommissioning (VAR_NCAP+NCAP_PASTI) when entering the objective function components (EQ_OBJINV, EQ_OBJFIX, EQ_OBJSALV).
* - NCAP_DLAGC
  <br>(r,datayear,p,cur)
  - NCAP_DLAG, OBJ_DLAGC, CST_DECC, CST_PVP
  - Monetary unit per capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a cost during any lag in the decommissioning (e.g., security).
  - Cost occurring during the lag time after the technical lifetime of a process has ended and before its decommissioning starts.
  - Cost during delay applied to the current capacity subject to decommissioning (VAR_NCAP+NCAP_PASTI) when entering the objective function components (EQ_OBJFIX, EQ_OBJSALV).
* - NCAP_DLIFE
  <br>(r,datayear,p)
  - DUR_MAX
  - Years
  <br>(0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when a process has a decommissioning phase.
  - Technical time for dismantling a facility after the end its technical lifetime, plus any lag time (NCAP_DLAG).
  - Decommissioning time impacting (VAR_NCAP+NCAP_PASTI) when entering the objective function components (EQ_OBJINV, EQ_OBJSALV).
* - NCAP_DRATE
  <br>(r,datayear,p)
  - G_DRATE, COR_SALVI, COR_SALVD
  - Percent
  <br>(0,∞);
  <br>default value: G_DRATE
  <br>Default i/e: STD
  - Provided if the cost of borrowing for a process is different from the standard discount rate.
  - Technology specific discount rate.
  - Discount rate applied to investments (VAR_NCAP+NCAP_PASTI) when entering the objective function components (EQ_OBJINV, EQ_OBJSALV).
* - NCAP_ELIFE
  <br>(r,datayear,p)
  - NCAP_TLIFE, COR_SALVI, OBJ_CRF
  - years
  <br>(0,∞);
  <br>default value: NCAP_TLIFE
  <br>Default i/e: STD
  - Provided only when the economic lifetime differs from the technical lifetime (NCAP_TLIFE).
  - Economic lifetime of a process.
  - Economic lifetime of a process when costing investment (VAR_NCAP+NCAP_PASTI) or capacity in the objective function components (EQ_OBJINV, EQ_OBJSALV, EQ_OBJFIX).
* - NCAP_FDR
  <br>(r,datayear,prc)
  - NCAP_COST
  - Decimal fraction (0,∞);
  <br>default value:none
  <br>Default i/e: STD
  - Provided when the effect of functional depreciation is considered significant to justify accelerated decrease in salvage value.
  - Defines an annual rate of additional depreciation in the salvage value.
  - Affects the salvage value coefficients in EQ_OBJSALV
* - NCAP_FOM
  <br>(r,datayear,p,cur)
  - OBJ_FOM, CST_FIXC, CST_PVP
  - Monetary unit per capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a fixed cost associated with the installed capacity.
  - Fixed operating and maintenance cost per unit of capacity according to the installation year.
  - Fixed operating and maintenance costs associated with total installed capacity (VAR_NCAP+NCAP_PASTI) when entering the objective function components (EQ_OBJFIX).
* - NCAP_FOMM
  <br>(r,datayear,p)
  - NCAP_FOM, MULTI
  - Integer number
  <br>Default value: 0 (no multiplier curve applied)
  <br>Default i/e: MIG
  - Provided when shaping based upon the period is desired.
  <br>Note: Multiplier index 1 is reserved for constant 1.
  - Period sensitive multiplier curve (MULTI) applied to the fixed operating and maintenance costs (NCAP_FOM).
  - *{See Related Parameters}*
* - NCAP_FOMX
  <br>(r,datayear,p)
  - NCAP_FOM, SHAPE
  - Integer number
  <br>Default value: 0 (no shape curve applied)
  <br>Default i/e: MIG
  - Provided when shaping based upon age is desired.
  <br>Note: Shape index 1 is reserved for constant 1.
  - Age-based shaping curve (SHAPE) to be applied to the fixed operating and maintenance cost.
  - *{See Related Parameters}*
* - NCAP_FSUB
  <br>(r,datayear,p,cur)
  - OBJ_FSB, CST_FIXX, CST_PVP
  - Monetary unit per capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a subsidy for associated with the level of installed capacity.
  - Subsidy per unit of installed capacity.
  - Fixed subsidy associated with total installed capacity (VAR_NCAP+NCAP_PASTI) when entering the objective function component (EQ_OBJFIX) with a minus sign.
* - NCAP_FSUBM
  <br>(r,datayear,p)
  - NCAP_FSUB, MULTI
  - Integer number
  <br>Default value: 0 (no multiplier curve applied)
  <br>Default i/e: MIG
  - Provided when shaping based upon the period is desired.
  <br>Note: Multiplier index 1 is reserved for constant 1.
  - Period sensitive multiplier curve (MULTI) applied to the subsidy (NCAP_FSUB).
  - *{See Related Parameters}*
* - NCAP_FSUBX
  <br>(r,datayear,p)
  - NCAP_FSUB, SHAPE
  - Integer number
  <br>Default value: 0 (no shape curve applied)
  <br>Default i/e: MIG
  - Provided when shaping based upon age is desired.
  <br>Note: Shape index 1 is reserved for constant 1.
  - Age-based shaping curve (SHAPE) to be applied to the fixed subsidy (NCAP_FSUB).
  - *{See Related Parameters}*
* - NCAP_FTAX
  <br>(r,datayear,p,cur)
  - OBJ_FTX, CST_FIXX, CST_PVP
  - monetary unit per capacity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a fixed tax based upon the level of the installed capacity.
  - Tax per unit of installed capacity.
  - Fixed subsidy associated with total installed capacity (VAR_NCAP+NCAP_PASTI) when entering the objective function components (EQ_OBJFIX).
* - NCAP_FTAXM
  <br>(r,datayear,p)
  - NCAP_FTAX, MULTI
  - Integer number
  <br>Default value: 0 (no multiplier curve applied)
  <br>Default i/e: MIG
  - Provided when shaping based upon the period is desired.
  <br>Note: Multiplier index 1 is reserved for constant 1.
  - Period sensitive multiplier curve (MULTI) applied to the tax (NCAP_FTAX).
  - *{See Related Parameters}*
* - NCAP_FTAXX
  <br>(r,datayear,p)
  - NCAP_FTAX, SHAPE
  - Integer number
  <br>Default value: 0 (no shape curve applied)
  <br>Default i/e: MIG
  - Provided when shaping based upon age is desired.
  <br>Note: Shape index 1 is reserved for constant 1.
  - Age-based shaping curve (SHAPE) to be applied to the fixed tax (NCAP_FTAX).
  - *{See Related Parameters}*
* - NCAP_ICOM
  <br>(r,datayear,p,c)
  - NCAP_CLED, rpc_capflo, rpc_conly
  - Commodity unit per capacity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Provided when a commodity is needed in the period in which the new capacity is to be available, or before NCAP_CLED.
  <br>If NCAP_CLED is provided, the commodity is required during the years \[B(v)+NCAP_CLED,B(v)+NCAP_ILED-NCAP_CLED\]. If this time spans more than one period, the commodity flow is split up proportionally between the periods.
  <br>For the commodity balance the commodity requirement in a period is converted to an average annual commodity flow for the entire period, although the construction may take place only for a few years of the period.
  <br>Negative value describes production (e.g. emissions) at the time of a new investment.
  - Amount of commodity (c) required for the construction of new capacity.
  - Applied to the investment variable (VAR_NCAP) in the appropriate commodity constraints (EQ(l)\_COMBAL) as part of consumption.
* - NCAP_ILED
  <br>(r,t,p)
  - NCAP_ICOM, NCAP_COST, COEF_CPT, COEF_ICOM, DUR_MAX
  - Years
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a delay between when the investment decision occurs and when the capacity (new capacity or past investment) is initially available. If NCAP_ILED\>0, the investment decision is assumed to occur at B(v) and the capacity becomes available at B(v)+NCAP-ILED. If NCAP_ILED\<0, the investment decision is assumed to occur at B(v)-NCAP_ILED and the capacity becomes available at B(v). Causes an IDC overhead in the investment costs accounting.
  - Lead time between investment decision and actual availability of new capacity (= construction time).
  - Applied to the investment variable (VAR_NCAP) balance constraints (EQ(l)\_COMBAL) as part of consumption, if there is an associated flow (NCAP_ICOM).
  <br>Used as to distinguish between small and large investments (VAR_NCAP) and thus influences the way the investment and fixed costs are treated in the objective function (EQ_OBJINV, EQ_OBJFIX, EQ_OBJSALV).
* - NCAP_ISPCT
  <br>(r,datayear,p)
  - NCAP_ISUB, OBJ_ISUB, CST_INVX
  - Decimal fraction
  <br>(−∞,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when defining an investment subsidy in proportion to the investment cost.
  <br>Requires that NCAP_COST is defined.
  - Unit investment subsidy as a fraction of unit investment costs, in the same currency unit, per unit of new capacity.
  - Applied to the investment variable (VAR_NCAP) when entering the objective function (EQ_OBJNV) with a minus sign.
* - NCAP_ISUB
  <br>(r,datayear,p,cur)
  - OBJ_ISUB, OBJSCC, CST_INVX, CST_SALV, CST_PVP
  - monetary unit per capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a subsidy for new investments in a period.
  - Subsidy per unit of new installed capacity.
  - Applied to the investment variable (VAR_NCAP) when entering the objective function (EQ_OBJNV) with a minus sign.
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - NCAP_ITAX
  <br>(r,datayear,p,cur)
  - OBJ_ITAX, OBJSCC, CST_INVX, CST_SALV, CST_PVP
  - monetary unit per capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a tax associated with new investments in a period.
  - Tax per unit of new installed capacity
  - Applied to the investment variable (VAR_NCAP) when entering the objective function (EQ_OBJNV).
  <br>May appear in user constraints (EQ_UC\*) if specified in UC_NAME.
* - NCAP_MSPRF
  <br>(r,datayear,c,p,lim)
  - COM_MSHGV
  - Unit: dimensionless
  <br>(0, ∞);
  <br>Default value: none
  <br>Default i/e: STD
  - Optional parameter for the logit market sharing mechanism, for process p supplying market c.
  - In the logit market sharing mechanism, defines preference weights (lim=\'N\') and intangible costs (lim=\'LO\')
  - EQ_MSNCAPB
* - NCAP_OCOM
  <br>(r,datayear,p,c)
  - NCAP_VALU, rpc_capflo, rpc_conly
  - Commodity unit per capacity unit
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Provided when there is a commodity release associated with the decommissioning.
  <br>The year index of the parameter corresponds to the vintage year.
  <br>If the decommissioning time (NCAP_DLIFE) falls in more than one period, is split up proportionally among the periods.
  <br>For the commodity balance the commodity release in a period is converted to an average annual commodity flow for the entire period, although the dismantling may take place only for a few years of the period.
  - Amount of commodity c per unit of capacity released during the dismantling of a process.
  - Applied to the investment variable (VAR_NCAP) in the appropriate commodity constraints (EQ(l)\_COMBAL) as part of production in the appropriate period.
* - NCAP_OLIFE
  <br>(r,datayear,p)
  - NCAP_TLIFE
  - Years
  <br>(0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Requires that early retirements are enabled and the process is vintaged.
  - Maximum operating lifetime of a process, in terms of full-load years.
  - EQL_SCAP
* - NCAP_PASTI
  <br>(r,pastyear,p)
  - NCAP_PASTY, OBJ_PASTI, PAR_PASTI, PRC_RESID
  - capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>No i/e
  - Past investment can also be specified for milestone years, e.g. if the milestone year is a historic year, so that capacity additions are known or if planned future investments are already known.
  - Investment in new capacity made before the beginning of the model horizon (in the year specified by pastyear).
  - EQ(l)\_COMBAL, EQ_CPT, EQ_OBJINV, EQ_OBJSALV, EQ_OBJFIX
* - NCAP_PASTY
  <br>(r,pastyear,p)
  - NCAP_PASTI
  - Years
  <br>\[1,999\];
  <br>default value: none
  <br>No i/e
  - Provided to spread a single past investment (NCAP_PASTI) back over several years (e.g., cars in the period before the 1^st^ milestoneyr were bought over the previous 15 years).
  <br>If overlaps with other past investments, the capacity values are added.
  - Number of years to go back to calculate a linear build-up of past investments
  - *{See NCAP_PASTI}*
* - NCAP_PKCNT
  <br>(r,datayear,p,s)
  - com_peak, com_pkts, prc_pkaf, prc_pkno
  - Decimal fraction
  <br>\[0,1\];
  <br>default value: 1
  <br>Default i/e: STD
  - If the indicator PRC_PKAF is specified, the NCAP_PKCNT is set equal to the availabilities NCAP_AF.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Fraction of capacity that can contribute to peaking equations.
  - Applied to investments in capacity (VAR_NCAP, NCAP_PASTI) in the peaking constraint (EQ_PEAK).
* - NCAP_SEMI
  <br>(r,datayear,p)
  - NCAP_DISC
  - Capacity unit
  <br>(0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Upper bound for the capacity must be defined by NCAP_BND; if not defined, assumed to be equal to the lower bound.
  <br>Requires MIP.
  - Semi-continuous new capacity, lower bound. (See Section 5.9)
  - Applied to the semi-continuous investment variable VAR_SNCAP in the discrete investment equation EQ_DSCNCAP
* - NCAP_START
  <br>(r,p)
  - PRC_NOFF
  - Year
  <br>\[1000,∞);
  <br>default value: none
  - NCAP_START(r,p)=y
  <br>is equivalent to
  <br>PRC_NOFF(r,p,BOH,y--1).
  - Start year for new investments
  - Affects the availability of investment variable (VAR_NCAP)
* - NCAP_TLIFE
  <br>(r,datayear,p)
  - NCAP_ELIFE, COEF_CPT, COEF_RPTI, DUR_MAX
  - Years
  <br>(0,∞);
  <br>default value: G_TLIFE
  <br>Default i/e: STD
  - Expected for all technologies that have investment costs.
  <br>Values below 0.5 cannot be well accounted in the objective function, and should thus be avoided (they are automatically resetted to 1).
  - Technical lifetime of a process.
  - Impacts all calculations that are dependent upon the availability of investments (VAR_NCAP) including capacity transfer (EQ_CPT), commodity flow (EQ(l)\_COMBAL), costs (EQ_OBJINV, EQ_OBJFIX, EQ_OBJVAR, EQ_OBJSALV).
* - NCAP_VALU
  <br>(r,datayear,p,c,cur)
  - NCAP_OCOM
  - Monetary unit / commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Provided when a released commodity has a value.
  - Value of a commodity released at decommissioning (NCAP_OCOM).
  - Applied to the investment related (VAR_NCAP, NCAP_PASTI) release flow at decommissioning in the objective function (EQ_OBJSALV).
* - PRC_ACTFLO
  <br>(r,datayear,p,cg)
  - PRC_CAPACT, prc_actunt, prc_spg, rpc_aire
  - Commodity unit / activity unit
  <br>(0,∞);
  <br>default value: 1
  <br>Default i/e: STD
  - Only (rarely) provided when either the activity and flow variables of a process are in different units, or if there is a conversion efficiency between the activity and the flow(s) in the PCG.
  <br>The group (cg) can be the whole PCG or any individual commodity in the PCG, or \'ACT\' (=PCG).
  - 1\) Conversion factor from units of activity to units of those flow variables that define the activity (primary commodity group),
  <br>or,
  <br>2\) Conversion multiplier representing the amount of flow(s) in the cg per 1 unit of activity.
  - Applied to the primary commodity (prc_pcg) flow variables (VAR_FLO, VAR_IRE) to relate overall activity (VAR_ACT in EQ_ACTFLO).
  <br>When the Reduction algorithm activated it is applied to the activity variable (VAR_ACT) in those cases where the flow variable (VAR_FLO) can be replaced by the activity variable (e.g. the activity is defined by one commodity flow).
* - PRC_CAPACT
  <br>(r,p)
  - PRC_ACTFLO, PRC_ACTUNT
  - Activity unit / capacity unit
  <br>(0,∞);
  <br>default value: 1
  <br>Default i/e: none
  - 
  - Conversion factor from capacity unit to activity unit assuming that the capacity is used for one year.
  - Applied along with the availability factor (NCAP_AF) to the investment (VAR_NCAP + NCAP_PASTI) in the utilization equations (EQ(l)\_CAPACT, EQ(l)\_CAFLAC).
  <br>Applied to the investment (VAR_NCAP + NCAP_PASTI) in the peak constraint (EQ_PEAK).
  <br>Applied to the investment (VAR_NCAP + NCAP_PASTI) in the capacity utilization constraint for CHP plants (ECT_AFCHP) and peak constraint in the IER extension (see Part III).
* - PRC_GMAP
  <br>(r,prc,item)
  - GR_GENMAP
  - Dimensionless
  <br>(∞,∞);
  <br>default value: none
  <br>Default i/e: none
  - Provided when process groupings are needed for custom processing e.g. in a TIMES code extension.
  - User-defined grouping of processes by group indicator **item**.
  - *None*
* - PRC_MARK
  <br>(r,datayear,p,item,c,bd)
  - FLO_MARK
  - Decimal fraction
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: 11
  - Combined limit on commodity production is derived as the sum of the process-specific productions multiplied by the inverse values of PRC_MARK. The constraint is applied to the annual production of commodity.
  <br>Item can be a any desired label identifying the group.
  - Process group-wise market share, which defines a constraint for the combined market share of multiple processes in the total commodity production.
  - EQ(l)\_FLOMRK, VAR_COMPRD
* - PRC_REFIT
  <br>(r,prc,p)
  - PRC_RCAP
  - Dimensionless
  <br>\[--3,3\];
  <br>default value: none
  <br>Default i/e: n/a
  - Requires that early retirements are allowed in the model. The parameter value determines the type of the refurbishment option as follows:
  <br>- Value=(±1 mod 2): Technology p will be a lifetime extension option (+1), or a retrofit option (−1), for the host prc
  <br>- Value=2 for p=prc: refitted capacity in each period is forced to be equal to the retired capacity of the host prc
  - Defines a mapping of host process prc to a retrofit or lifetime extension option p in region r, where p is another process representing the refurbishment option. The value of the parameter determines the type of the refurbishment option (see column on the left).
  - Activates generation of the retrofit / lifetime extension equations (EQL_REFIT)
* - PRC_RESID
  <br>(r,datayear,p)
  - NCAP_PASTI
  - Capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: 1
  <br>(options 5/15 may be used for extrapolation over TLIFE, other i/e options are ignored)
  - If only a single data point is specified, linear decay of the specified residual capacity over technical lifetime is assumed.
  <br>Used as an alternative to NCAP_PASTI, not to use both for the same process.
  - Residual existing capacity stock of process (p) still available in the year specified (datayear).
  <br>PRC_RESID is most useful for describing the stock of capacity with mixed vintages, while NCAP_PASTI is suited for capacities of a certain vintages, such as an individual power plants.
  - EQ(l)\_CAPACT, EQ(l)\_CAFLAC, EQL_CAPFLO, EQ(l)\_CPT, VAR_CAP
* - R_CUREX
  <br>(r,cur1,cur2)
  - G_CUREX
  - Scalar
  <br>(0,∞)
  <br>Default value: none
  <br>Default i/e: N/A
  - The target currency cur2 must have a discount rate defined with G_DRATE.
  - Conversion factor from currency cur1 to currency cur2 in region r, in order to use cur2 in the objective function.
  - Affects cost coefficients in EQ_OBJ
* - RCAP_BLK
  <br>(r,datayear,p)
  - PRC_RCAP, RCAP_BND
  - Capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Only effective when lumpy early capacity retirements are active (RETIRE=MIP). Requires MIP.
  - Retirement block size.
  - EQ_DSCRET, VAR_DRCAP, VAR_SCAP
* - RCAP_BND
  <br>(r,datayear,p,bd)
  - PRC_RCAP, RCAP_BLK
  - Capacity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Unless the control variable DSCAUTO=YES, requires that PRC_RCAP is defined for process p.
  - Bound on the retired amount of capacity in a period (same bound for all vintages).
  - VAR_RCAP, VAR_SCAP
* - REG_BDNCAP
  <br>(all_r,bd)
  - REG_FIXT
  - Year
  <br>\[1000,∞);
  <br>default value: none
  - Only taken into account when a previous solution is loaded by using the LPOINT control variable.
  <br>If several bound types are specified, one can use NCAP_BND(r,\'0\',p,\'N\')=±1 for assigning only an UP/LO bound for any process p.
  - Defines the year up to which capacities are to be bounded by previous solution,
  <br>by model region. One can choose FX/UP/LO bounds, as well as lower bounds only for selected processes.
  - VAR_NCAP
* - REG_BNDCST
  <br>(r,datayear,agg,cur,bd)
  - REG_CUMCST
  - Monetary unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - The cost aggregations (agg) supported are listed in the set COSTAGG (see Table 1).
  - Bound on regional costs by type of cost aggregation.
  - EQ_BNDCST, VAR_CUMCST
* - REG_CUMCST
  <br>(r,y1,y2,agg,cur,bd)
  - REG_BNDCST
  - Monetary unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: N/A
  - The cost aggregations (agg) supported are listed in the set COSTAGG (see Table 1).
  - Cumulative bound on regional costs by type of cost aggregation.
  - EQ_BNDCST VAR_CUMCST
* - REG_FIXT
  <br>(all_r)
  - 
  - Year
  <br>\[1000,∞);
  <br>default value: none
  - Only taken into account when the first periods are fixed by using the FIXBOH control variable.
  - Defines the year up to which periods are fixed to previous solution, by region
  - <span>--</span>
* - RPT_OPT
  <br>(item,j)
  - 
  - Integer value
  <br>\[open\];
  <br>default value: none
  - See Part III, Table 15 for a list and descriptions of available options.
  - Miscellaneous reporting options
  - <span>--</span>
* - SHAPE
  <br>(j,age)
  - FLO_FUNC, FLO_SUM, NCAP_AFX, NCAP_FOMX, NCAP_FSUBX, NCAP_FTAXX
  - Scalar
  <br>\[open\];
  <br>default value: none
  <br>I/e: Full dense interpolation and extrapolation
  - Provided for each age dependent shaping curve that is to be applied.
  - Multiplier table used for any shaping parameters (\*\_\*X) to adjust the corresponding technical data as function of the age; the table can contain different multiplier curves that are identified by the index j.
  - *{See Related Parameters}*
* - STG_CHRG
  <br>(r,datayear,p,s)
  - prc_nstts, prc_stgips, prc_stgtss
  - Scalar
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Only applicable to storage processes (STG): timeslice storage, inter-period storage or night storage devices.
  - Annual exogenous charging of a storage technology in a particular timeslice s.
  - Exogenous charging of storage enters storage equations (EQ_STGTSS, EQ_STGIPS) as right-hand side constant.
* - STG_EFF
  <br>(r,datayear,p)
  - prc_nstts, prc_stgips, prc_stgtss
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: 1
  <br>Default i/e: STD
  - Only applicable to storage processes (STG): timeslice storage, inter-period storage or night storage devices.
  - Efficiency of storage process.
  - Applied to the storage output flow (VAR_SOUT) in the commodity balance (EQ(l)\_COMBAL) for the stored commodity.
* - STG_LOSS
  <br>(r,datayear,p,s)
  - prc_nstts, prc_stgips, prc_stgtss
  - Scalar
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Only applicable to storage processes (STG): timeslice storage, inter-period storage or night storage devices.
  <br>STG_LOSS\>0 defines the loss in proportion to the initial storage level during one year's storage time.
  <br>STG_LOSS\<0 defines an equilibrium loss, i.e. how much the annual losses would be if the storage level is kept constant.
  - Annual loss of a storage process per unit of average energy stored.
  - Timeslice storage process (EQ_STGTSS): applied to the average storage level (VAR_ACT) between two consecutive timeslices.
  <br>Inter-period storage process (EQ_STGIPS): applied to the average storage level from the pre-period (VAR_ACT) and the net inflow (VAR_SIN-VAR_SOUT) of the current period.
* - STG_MAXCYC
  <br>(r,datayear,p)
  - NCAP_AF
  - Number of cycles
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can only be used for genuine storage processes. The limit can be exceeded by paying for additional replacement capacity, with a penalty cost equal to the investment annuity.
  - Defines the maximum number of storage cycles over the lifetime. Sets a limit for the total discharge divided by storage capacity.
  - Activates generation of the cycle limit/penalty equations (EQL_STGCCL).
* - STG_SIFT
  <br>(r,datayear,prc,com,ts)
  - ACT_TIME
  - Decimal fraction
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: STD
  - Can only be used for a timeslice storage process. Levelized to the timeslice level of the process flow.
  <br>Direct inheritance.
  <br>By specifying com=\'ACT\' one can define a limit in total shifting over a season, in proportion to demand.
  - Defines process prc as a load-shifting process, and limits the load shifting of demand com in timeslice ts to at most the fraction specified by the parameter value.
  - Activates generation of load shifting constraints (EQ(l)\_SLSIFT).
* - STGIN_BND
  <br>(r,datayear,p,c,s,bd)
  - prc_nstts, prc_stgips, prc_stgtss
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Only applicable to storage processes (STG): timeslice storage, inter-period storage or night storage devices.
  - Bound on the input flow of a storage process in a timeslice s.
  - Storage input bound constraint (EQ(l)\_STGIN) when s is above prc_tsl of the storage process.
  <br>Direct bound on storage input flow (VAR_SIN) when at the prc_tsl level.
* - STGOUT_BND
  <br>(r,datayear,p,c,s,bd)
  - prc_nstts, prc_stgips, prc_stgtss
  - Commodity unit
  <br>\[0,∞);
  <br>default value: none
  <br>Default i/e: MIG
  - Only applicable to storage processes (STG): timeslice storage, inter-period storage or night storage devices.
  - Bound on the output flow of a storage process in a timeslice s.
  - Storage output bound constraint (EQ(l)\_STGIN) when s is above prc_tsl of the storage process.
  <br>Direct bound on storage output flow variable (VAR_SOUT) when at the prc_tsl level.
* - TL_CCAP0
  <br>(r,teg)
  - (Alias: CCAP0), PAT, CCOST0
  - Capacity unit
  <br>\[open\];
  <br>default value: none
  - Requires using ETL.
  <br>For learning technologies teg when ETL is used.
  - Initial cumulative capacity of a learning technology.
  - Cumulative investment constraint (EQ_CUINV) and cumulative capacity variable (VAR_CCAP) in endogenous technological learning formulation.
* - TL_CCAPM
  <br>(r,teg)
  - (Alias: CCAPM), CCOSTM
  - Capacity unit
  <br>\[open\];
  <br>default value: none
  - Requires using ETL.
  <br>For learning technologies teg when ETL is used.
  - Maximum cumulative capacity.
  - Core ETL equations.
* - TL_CLUSTER
  <br>(r,teg,prc)
  - (Alias: CLUSTER), TL_MRCLUST
  - Decimal fraction.
  <br>\[0-1\];
  <br>default value: none
  - Requires using ETL (MIP).
  <br>Provided to model clustered endogenous technology learning.
  <br>Each of the learning parameters must also be specified for the key learning technology.
  - Indicator that a technology (teg) is a learning component that is part of another technology (prc) in region r; teg is also called key component.
  - EQ_CLU
* - TL_MRCLUST
  <br>(r,teg,reg,p)
  - TL_CLUSTER
  - Decimal fraction.
  <br>\[0-1\];
  <br>default value: none
  - Requires using ETL (MIP).
  <br>Provided to model clustered endogenous technology learning.
  <br>Each of the learning parameters must also be specified for the key learning technology.
  - Mapping for multi-region clustering between learning key components (teg) and processes (p) that utilize the key component.
  - EQ_MRCLU
* - TL_PRAT
  <br>(r,teg)
  - (Alias: PRAT), ALPH, BETA, CCAPK, CCOST0, PAT, PBT
  - Scalar
  <br>\[0,1\];
  <br>default value none
  - Requires using ETL.
  <br>Provided for learning technologies (teg) when ETL is used.
  - Progress ratio indicating the drop in the investment cost each time there is a doubling of the installed capacity.
  - Fundamental factor to describe the learning curve and thus effects nearly all equations and variables related to endogenous technology learning (ETL).
* - TL_SC0
  <br>(r,teg)
  - (Alias: SC0)
  - Monetary unit / capacity unit
  <br>\[open\];
  <br>default value: none
  - Requires using ETL.
  <br>For learning technologies teg when ETL is used.
  - Initial specific investment costs.
  - Defines together with CCAP0 initial point of learning curve and affects thus the core equations and variables of endogenous technological learning (ETL).
* - TL_SEG
  <br>(r,teg)
  - (Alias: SEG)
  - Integer
  <br>\[open\];
  - Requires using ETL.
  <br>For learning technologies teg when ETL is used.
  <br>Currently limited to six segments by set kp.
  - Number of segments.
  - Influences the piecewise linear approximation of the cumulative cost curve (EQ_COS, EQ_LA1, EQ_LA2).
* - TS_CYCLE
  <br>(r,ts)
  - G_CYCLE
  - Number of days
  <br>\[1,∞);
  <br>Default values:
  <br>- 365 for ts=ANNUAL
  <br>- 7 for any ts above the WEEKLY level
  <br>- 1 for any ts above the DAYNITE level
  - Recommended to be used whenever timeslice cycles are different from the default, instead of changing G_CYCLE. Does not affect interpretation of availability factors for storage level, which thus remain to be according to G_CYCLE.
  - Defines the length of the timeslice cycles under timeslice ts, in days, and thereby also the number of timeslice cycles under each parent.
  - Affects the calculation of actual timeslice lengths and number of timeslice cycles in various equations, notably storage and dispatching equations.
* - UC_ACT
  <br>(uc_n,side,r,datayear,p,s)
  - uc_n, uc_gmap_p
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Coefficient of the activity variable VAR_ACT in a user constraint.
  - EQ(l)\_UCXXX
* - UC_CAP
  <br>(uc_n,side,r,datayear,p)
  - uc_n, uc_gmap_p
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  - Coefficient of the activity variable VAR_CAP in a user constraint.
  - EQ(l)\_UCXXX
* - UC_CLI
  <br>(uc_n,side,r,datayear,item)
  - 
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Used in user constraints.
  <br>Climate variable can be at least any of CO2-GTC, CO2-ATM, CO2-UP, CO2-LO, FORCING, DELTA-ATM,
  <br>DELTA-LO (for carbon).
  <br>See Appendix on Climate Module for details.
  - Multiplier of climate variable in user constraint
  - EQ(l)\_UCXXX
* - UC_COMCON
  <br>(uc_n,side,r,datayear,c,s)
  - uc_n, uc_gmap_c
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  <br>No inheritance/aggregation (might be changed in the future).
  - Coefficient of the commodity consumption variable VAR_COMCON in a user constraint.
  - EQ(l)\_UCXXX
* - UC_COMNET
  <br>(uc_n,side,r,datayear,c,s)
  - uc_n, uc_gmap_c
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  <br>No inheritance/aggregation (might be changed in the future).
  - Coefficient of the net commodity production variable VAR_COMNET in a user constraint.
  - EQ(l)\_UCXXX
* - UC_COMPRD
  <br>(uc_n,side,r,datayear,c,s)
  - uc_n, uc_gmap_c
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  <br>No inheritance/aggregation (might be changed in the future).
  - Coefficient of the total commodity production variable VAR_COMPRD in a user constraint.
  - EQ(l)\_UCXXX
* - UC_CUMACT
  <br>(uc_n,r,p,y1,y2)
  - ACT_CUM
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>I/e: N/A
  - Used in cumulative user constraints only.
  - Multiplier of cumulative process activity variable in user constraint.
  - EQ(l)\_UC, EQ(l)\_UCR, VAR_CUMFLO
* - UC_CUMCOM
  <br>(uc_n,r,type,c,y1,y2)
  - COM_CUMNET, COM_CUMPRD
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>I/e: N/A
  - Used in cumulative user constraints only.
  <br>Type=NET/PRD determines the variable referred to (CUMNET/ CUMPRD).
  - Multiplier of cumulative commodity variable in user constraint.
  - EQ(l)\_UC, EQ(l)\_UCR, VAR_CUMCOM
* - UC_CUMFLO
  <br>(uc_n,r,p,c,y1,y2)
  - FLO_CUM
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>I/e: N/A
  - Used in cumulative user constraints only.
  - Multiplier of cumulative process flow variable in user constraint.
  - EQ(l)\_UC, EQ(l)\_UCR, VAR_CUMFLO
* - UC_FLO
  <br>(uc_n,side,r,datayear,p,c,s)
  - uc_n
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Coefficient of the flow VAR_FLO variable in a user constraint.
  - EQ(l)\_UCXXX
* - UC_IRE
  <br>(uc_n,side,r,datayear,p,c,s)
  - uc_n
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  <br>Direct inheritance.
  <br>Weighted aggregation.
  - Coefficient of the trade variable VAR_IRE in a user constraint.
  - EQ(l)\_UCXXX
* - UC_NCAP
  <br>(uc_n,side,r,datayear,p)
  - uc_n, uc_gmap_p
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default: i/e: STD
  - Used in user constraints.
  - Coefficient of the activity variable VAR_NCAP in a user constraint.
  - EQ(l)\_UCXXX
* - UC_RHS
  <br>(uc_n,lim)
  - uc_n, uc_r_sum, uc_t_sum, uc_ts_sum
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: none
  - Used in user constraints.
  <br>Binding user constraints are defined using bound types lim=UP/LO/FX.
  <br>Non-binding (free) user constraints can be defined using the lim type lim=N.
  - RHS constant with bound type of bd of a user constraint.
  - RHS (right-hand side) constant of a user constraint, which is summing over regions (uc_r_sum), periods (uc_t_sum) and timeslices (uc_ts_sum) (EQ(l)\_UC).
* - UC_RHSR
  <br>(r,uc_n,lim)
  - uc_n, uc_r_each, uc_t_sum, uc_ts_sum
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: none
  - Used in user constraints.
  <br>Binding user constraints are defined using bound types lim=UP/LO/FX.
  <br>Non-binding (free) user constraints can be defined using the lim type lim=N.
  - RHS constant with bound type of bd of a user constraint.
  - RHS constant of user constraints, which are generated for each region (uc_r_each) and are summing over periods (uc_t_sum) and timeslices (uc_ts_sum) (EQ(l)\_UCR).
* - UC_RHSRT
  <br>(r,uc_n,datayear,lim)
  - uc_n, uc_r_each, uc_t_each, uc_t_succ, uc_ts_sum
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: MIG
  - Used in user constraints.
  <br>Binding user constraints are defined using bound types lim=UP/LO/FX.
  <br>Non-binding (free) user constraints can be defined using the lim type lim=N.
  - RHS constant with bound type of bd of a user constraint.
  - RHS constant of user constraints, which are generated for each region (uc_r_each) and period (uc_t_each) and are summing over timeslices (uc_ts_sum) (EQ(l)\_UCRT).
  <br>If dynamic, constraints will be generated between two successive periods (EQ(l)\_UCRSU).
* - UC_RHSRTS
  <br>(r,uc_n,datayear,s,lim)
  - uc_n, uc_r_each, uc_t_each, uc_t_succ, uc_ts_each
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: MIG
  - Used in user constraints.
  <br>No inheritance / aggregation, unless the target timeslice level is specified by UC_TSL.
  <br>Direct inheritance, if the target timeslice level is specified by UC_TSL.
  <br>Binding user constraints are defined using bound types lim=UP/LO/FX.
  <br>Non-binding (free) user constraints can be defined using the lim type lim=N.
  - RHS constant with bound type of bd of a user constraint.
  - RHS constant of user constraints, which are generated for each specified region (uc_r_each), period (uc_t_each) and timeslice (uc_ts_each) (EQ(l)\_UCRTS).
  <br>If dynamic, constraints will be generated between two successive periods (EQ(l)\_UCRSUS).
* - UC_RHST
  <br>(uc_n,datayear,lim)
  - uc_n, uc_r_sum, uc_t_each, uc_t_succ, uc_ts_sum
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: MIG
  - Used in user constraints.
  <br>Binding user constraints are defined using bound types lim=UP/LO/FX.
  <br>Non-binding (free) user constraints can be defined using the lim type lim=N.
  - RHS constant with bound type of bd of a user constraint.
  - RHS constant of user constraints, which are generated for each specified period (uc_t_each) and are summing over regions (uc_r_sum) and timeslices (uc_ts_sum) (EQ(l)\_UCT).
  <br>If dynamic, constraints will be generated between two successive periods (EQ(l)\_UCSU).
* - UC_RHSTS
  <br>(uc_n,datayear,s,lim)
  - uc_n, uc_r_sum, uc_t_each, uc_t_succ, uc_ts_each
  - None
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: MIG
  - Used in user constraints.
  <br>No inheritance/aggregation.
  <br>Binding user constraints are defined using bound types lim=UP/LO/FX.
  <br>Non-binding (free) user constraints can be defined using the lim type lim=N.
  - RHS constant with bound type of bd of a user constraint.
  - RHS constant of user constraints, which are generated for each period (uc_t_each) and timeslice (uc_ts_each) and are summing over regions (uc_r_sum) (EQ(l)\_UCTS).
  <br>If dynamic, constraints will be generated between two successive periods (EQ(l)\_UCSUS).
* - UC_TIME
  <br>(uc_n,r,datayear)
  - 
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Used in user constraints.
  <br>Adds a time constant to the RHS side.
  - Multiplier for the number of years in model periods (static UCs), or between milestone years (dynamic UCs)
  - EQ(l)\_UCXXX
* - UC_UCN
  <br>(uc_n,side,r,datayear, ucn)
  - UC_RHSRT
  - Dimensionless
  <br>\[open\];
  <br>default value: none
  <br>Default i/e: STD
  - Only taken into account if the user constraint is by region & period, and summing over timeslices and the RHS side is activated (EQ(l)\_UCRSU).
  - Multiplier of user constraint variable in another user constraint.
  - EQ(l)\_UCRSU, VAR_UCRT
* - VDA_EMCB
  <br>(r,datayear,c,com)
  - FLO_EMIS, FLO_EFF
  - Emission units per flow units
  <br>default value: none
  <br>Default i/e: STD
  - Available in the VEDA shell.
  <br>Any process-specific FLO_EMIS / FLO_EFF with the commodities c and com will override VDA_EMCB.
  - Emissions (com) from the combustion of commodity (c) in region (r).
  - EQ_PTRANS
```

```{figure} assets/indexing-aux-consumption.svg
:name: indexing-aux-consumption
:align: center

Indexing of auxiliary consumption/emission.
```

(internal-parameters)=
##  Internal parameters

{numref}`internal-parameters` gives an overview of internal parameters generated by the TIMES preprocessor. Similar to the description of the internal sets, not all internal parameters used within TIMES are discussed. The list given in {numref}`internal-parameters` focuses mainly on the parameters used in the preparation and creation of the equations in Chapter 6. In addition to the internal parameters listed here, the TIMES preprocessor computes additional internal parameters which are either used only as auxiliary parameters being valid only in a short section of the code or which are introduced to improve the performance of the code regarding computational time.

```{list-table} Internal parameters in TIMES
:name: internal-parameters
:header-rows: 1

* - Internal parameter[^31] (Indexes)
  - Instances (Required / Omit / Special conditions)
  - Description
* - ALPH
  <br>(r,kp,teg)
  - For learning technologies teg when ETL is used.
  - Axis intercept on cumulative cost axis for description of linear equation valid for segment kp.
* - BETA
  <br>(r,kp,teg)
  - For learning technologies teg when ETL is used.
  - Slope of cumulative cost curve in segment kp (= specific investment cost).
* - CCAPK
  <br>(r,kp,teg)
  - For learning technologies teg when ETL is used.
  - Cumulative capacity at kinkpoint kp.
* - CCOST0
  <br>(r,teg)
  - For learning technologies teg when ETL is used.
  - Initial cumulative cost of learning technology teg.
* - CCOSTK
  <br>(r,kp,teg)
  - For learning technologies teg when ETL is used.
  - Cumulative investment cost at kinkpoint kp.
* - CCOSTM
  <br>(r,teg)
  - For learning technologies teg when ETL is used.
  - Maximum cumulative cost based on CCAPM.
* - COEF_AF
  <br>(r,v,t,p,s,bd)
  - For each technology, at the level of process operation (PRC_TSL).
  - Availability coefficient of the capacity (new investment variable VAR_NCAP plus still existing past investments NCAP_PASTI) in EQ(l)\_CAPACT; COEF_AF is derived from the availability input parameters NCAP_AF, NCAP_AFA and NCAP_AFS taking into account any specified MULTI or SHAPE multipliers.
* - COEF_CPT
  <br>(r,v,t,p)
  - For each technology the amount of an investment (VAR_NCAP) available in the period.
  - Fraction of capacity built in period v that is available in period t; might be smaller than 1 due to NCAP_ILED in vintage period or the fact that the lifetime ends within a period.
* - COEF_ICOM
  <br>(r,v,t,p,c)
  - Whenever there is a commodity required during construction, the consuming being taken from the balance constraint (EQ(l)\_COMBAL).
  <br>Applied to the investment variable (VAR_NCAP) of period v in the commodity balance (EQ(l)\_COMBAL) of period t.
  <br>The duration during which the commodity is produced starts in the year B(v)+NCAP_ILE D(v)--NCAP_CLED(v) and ends in the year B(v)+NCAP_ILED(v)--1.
  - Coefficient for commodity requirement during construction in period t due to investment decision in period v (see also NCAP_ICOM).
* - COEF_OCOM
  <br>(r,v,t,p,c)
  - Whenever there is a commodity released during decommissioning, the production being added to the balance constraint (EQ(l)\_COMBAL).
  <br>Applied to the investment variable (VAR_NCAP) of period v in the commodity balance (EQ(l)\_COMBAL) of period t.
  <br>The release occurs during the decommissioning lifetime NCAP_DLIFE.
  - Coefficient for commodity release during decommissioning time in period t due to investment made in period v.
* - COEF_PTRAN
  <br>(r,v,t,p,cg,c,com_grp)
  - For each flow through a process.
  - Coefficient of flow variable of commodity c belonging to commodity group cg in EQ_PTRANS equation between the commodity groups cg and com_grp.
* - COEF_PVT
  <br>(r,t)
  - For each region, the present value of the time in each period.
  - Coefficient for the present value of periods, used primarily for undiscounting the solution marginals.
* - COEF_RPTI
  <br>(r,v,p)
  - For each technology whose technical life (NCAP_TLIFE) is shorter than the period.
  - Number of repeated investment of process p in period v when the technical lifetime minus the construction time is shorter than the period duration; Rounded to the next largest integer number.
* - COR_SALVD
  <br>(r,v,p,cur)
  - For each technology existing past the end of the modelling horizon with decommissioning costs, adjustment in the objective function.
  - Correction factor for decommissioning costs taking into account technical discount rates and economic decommissioning times.
* - COR_SALVI
  <br>(r,v,p,cur)
  - For each process extending past the end of the modelling horizon adjustment in the objective function.
  - Correction factor for investment costs taking into account technical discount rates, economic lifetimes and a user-defined discount shift (triggered by the control switch MIDYEAR (see Section 6.2 EQ_OBJ).
* - D
  <br>(t)
  - For each period, D(t) = E(t)--B(t)+1.
  - Duration of period t.
* - DUR_MAX
  - For the model.
  - Maximum of NCAP_ILED + NCAP_TLIFE + NCAP_DLAG + NCAP_DLIFE + NCAP_DELIF over all regions, periods and processes.
* - LEAD
  <br>(t)
  - For each milestone year.
  - Time between milestone years **t**--1 and **t**, in years. For the first milestone year t1, LEAD(t1)=M(t1)--B(t1)+1.
* - M
  <br>(v)
  - For each period, if the duration of the period is even, the middle year of the period is B(t) + D(t)/2 -- 1, if the period is uneven, the middle year is B(t) + D(t)/2 -- 0.5.
  - Middle year of period t.
* - MINYR
  - For the model
  - Minimum year over t = M(t) -- D(t) +1; used in objective function.
* - MIYR_V1
  - For the model
  - First year of model horizon.
* - MIYR_VL
  - For the model
  - Last year of model horizon.
* - NTCHTEG
  <br>(r,teg)
  - For learning technologies teg when ETL with technology clusters is used.
  - Number of processes using the same key technology teg.
* - OBJ_ACOST
  <br>(r,y,p,cur)
  - For each process with activity costs.
  <br>Enters the objective function (EQ_OBJVAR).
  - Inter-/Extrapolated variable costs (ACT_COST) for activity variable (VAR_ACT) for each year.
* - OBJ_COMNT
  <br>(r,y,c,s,type,cur)
  - For each commodity with costs, taxes or subsidies on the net production.
  <br>Enters the objective function (EQ_OBJVAR).
  - Inter-/Extrapolated cost, tax and subsidy (distinguished by the type index) on net production of commodity (c) for each year associated with the variable VAR_COMNET. Cost types (type) are COST, TAX and SUB.
* - OBJ_COMPD
  <br>(r,y,c,s,type,cur)
  - For each commodity with costs, taxes or subsidies on the commodity production.
  <br>Enters the objective function (EQ_OBJVAR).
  - Inter-/Extrapolated cost, tax and subsidy (distinguished by the type index) on production of commodity (c) for each year associated with the variable VAR_COMPRD. Cost types (type) are COST, TAX and SUB.
* - OBJ_CRF
  <br>(r,y,p,cur)
  - For each technology with investment costs.
  <br>Enters objective function (EQ_OBJINV).
  - Capital recovery factor of investment in technology p in objective function taking into account the economic lifetime (NCAP_ELIFE) and the technology specific discount rate (NCAP_DRATE) or, if the latter is not specified, the general discount rate (G_DRATE).
* - OBJ_CRFD
  <br>(r,y,p,cur)
  - For each technology with decommissioning costs.
  <br>Enters objective function (EQ_OBJINV).
  - Capital recovery factor of decommissioning costs in technology p taking into account the economic lifetime (NCAP_DELIF) and the technology specific discount rate (NCAP_DRATE) or, if the latter is not specified, the general discount rate (G_DRATE).
* - OBJ_DCEOH
  <br>(r,cur)
  - Enters objective function (EQ_OBJSALV).
  - Discount factor for the year EOH + 1 based on the general discount rate (G_DRATE).
* - OBJ_DCOST
  <br>(r,y,p,cur)
  - For each technology with decommissioning costs.
  <br>Enters objective function (EQ_OBJINV).
  - Inter-/Extrapolated decommissioning costs (NCAP_DCOST) for each year related to the investment (VAR_NCAP) of process p.
* - OBJ_DISC
  <br>(r,y,cur)
  - Enters objective function (EQ_OBJINV, EQ_OBJVAR, EQ_OBJFIX, EQ_OBJSALV, EQ_OBJELS).
  - Annual discount factor based on the general discount rate (G_DRATE) to discount costs in the year y to the base year (G_DYEAR).
* - OBJ_DIVI
  <br>(r,v,p)
  - Enters objective function (EQ_OBJINV).
  - Divisor for investment costs (period duration, technical lifetime or investment lead time depending on the investment cases 1a, 1b, 2a, 2b).
* - OBJ_DIVIII
  <br>(r,v,p)
  - Enters objective function (EQ_OBJINV).
  - Divisor for decommissioning costs and salvaging of decommissioning costs (period duration, technical lifetime or decommissioning time depending on the investment cases 1a, 1b, 2a, 2b).
* - OBJ_DIVIV
  <br>(r,v,p)
  - Enters objective function (EQ_OBJFIX).
  - Divisor for fixed operating and maintenance costs and salvaging of investment costs.
* - OBJ_DLAGC
  <br>(r,y,p,cur)
  - Enters objective function (EQ_OBJFIX).
  - Inter-/Extrapolated fixed capacity (VAR_NCAP+NCAP_PASTI) costs between the end of the technical lifetime and the beginning of the decommissioning for each year.
* - OBJ_FCOST
  <br>(r,y,p,c,s,cur)
  - For each flow variable with flow related costs.
  <br>Enters objective function (EQ_OBJVAR).
  - Inter-/Extrapolated flow costs (FLO_COST) for each year for the flow or trade variable (VAR_FLO, VAR_IRE) as well as capacity related flows (specified by NCAP_COM, NCP_ICOM, NCAP_OCOM).
* - OBJ_FDELV
  <br>(r,y,p,c,s,cur)
  - For each flow with delivery costs.
  <br>Enters objective function (EQ_OBJVAR).
  - Inter-/Extrapolated delivery costs (FLO_DELIV) for each year for the flow or trade variable (VAR_FLO, VAR_IRE) as well as capacity related flows (specified by NCAP_COM, NCP_ICOM, NCAP_OCOM).
* - OBJ_FOM
  <br>(r,y,p,cur)
  - For each process with fixed operating and maintenance costs.
  <br>Enters the objective function (EQ_OBJFIX).
  - Inter-/Extrapolated fixed operating and maintenance costs (NCAP_FOM) for the installed capacity (VAR_NCAP+NCAP_PASTI) for each year.
* - OBJ_FSB
  <br>(r,y,p,cur)
  - For each process with subsidy on existing capacity.
  <br>Enters objective function (EQ_OBJFIX).
  - Inter-/Extrapolated subsidy (NCAP_FSUB) on installed capacity (VAR_NCAP+NCAP_PASTI) for each year.
* - OBJ_FSUB
  <br>(r,y,p,c,s,cur)
  - For each flow variable with subsidies.
  <br>Enters objective function (EQ_OBJVAR).
  - Inter-/Extrapolated subsidy (FLO_SUB) for the flow or trade variable (VAR_FLO, VAR_IRE) for each year as well as capacity related flows (specified by NCAP_COM, NCP_ICOM, NCAP_OCOM).
* - OBJ_FTAX
  <br>(r,y,p,c,s,cur)
  - For each flow variable with taxes.
  <br>Enters objective function (EQ_OBJVAR).
  - Inter-/Extrapolated tax (FLO_TAX) for flow or trade variable (VAR_FLO, VAR_IRE) for each year as well as capacity related flows (specified by NCAP_COM, NCP_ICOM, NCAP_OCOM).
* - OBJ_FTX
  <br>(r,y,p,cur)
  - For each process with taxes on existing capacity.
  <br>Enters objective function (EQ_OBJFIX).
  - Inter-/Extrapolated tax (NCAP_FTAX) on installed capacity (VAR_NCAP+NCAP_PASTI) for each year.
* - OBJ_ICOST
  <br>(r,y,p,cur)
  - For each process with investment costs.
  <br>Enters objective function (EQ_OBJINV).
  - Inter-/Extrapolated investment costs (NCAP_COST) for investment variable (VAR_NCAP) for each year.
* - OBJ_IPRIC
  <br>(r,y,p,c,s,all_r,ie,cur)
  - For each import/export flow with prices assigned to it.
  <br>Enters objective function (EQ_OBJVAR).
  - Inter-/Extrapolated import/export prices (IRE_PRICE) for import/export variable (VAR_IRE) for each year.
* - OBJ_ISUB
  <br>(r,y,p,cur)
  - For each process with subsidy on new investment.
  <br>Enters objective function (EQ_OBJINV).
  - Inter-/Extrapolated subsidy (NCAP_ISUB) on new capacity (VAR_NCAP) for each year.
* - OBJ_ITAX
  <br>(r,y,p,cur)
  - For each process with taxes on new investment.
  <br>Enters objective function (EQ_OBJINV).
  - Inter-/Extrapolated tax (NCAP_ITAX) on new capacity (VAR_NCAP) for each year.
* - OBJ_PASTI
  <br>(r,v,p,cur)
  - Enters objective function (EQ_OBJINV).
  - Correction factor for past investments.
* - OBJ_PVT
  <br>(r,t,cur)
  - Used as a multiplier in objective function in a few sparse cases.
  - Present value of time (in years) in period **t**, according to currency **cur** in region **r**, discounted to the base year.
* - OBJSIC
  <br>(r,v,teg)
  - For learning technologies.
  <br>Enters objective function (EQ_OBJINV).
  - Investment cost related salvage value of learning technology teg with vintage period v at year EOH+1.
* - OBJSSC
  <br>(r,v,p,cur)
  - For processes with investment costs.
  <br>Enters objective function (EQ_OBJSALV).
  - Investment cost related salvage value of process p with vintage period v at year EOH+1.
* - PAT
  <br>(r,teg)
  - For learning technologies teg when ETL is used.
  - Learning curve coefficient in the relationship: SC = PAT \* VAR_CCAP\^(-PBT).
* - PBT
  <br>(r,teg)
  - For learning technologies teg when ETL is used.
  - Learning curve exponent PBT(r,teg) = LOG(PRAT(r,teg))/LOG(2).
* - PYR_V1
  - For the model
  - Minimum of pastyears and MINYR.
* - RS_FR
  <br>(r,s,ts)
  - Defined for all commodities. Applied to flow variables in all equations in order to take into account cases where the variables may be defined at a different timeslice level than the level of the equation.
  - Fraction of timeslice s in timeslice ts, if s is below ts, otherwise 1. In other words, RS_FR(r,s,ts) = G_YRFR(r,s) / G_YRFR(r,ts), if s is below ts, and otherwise 1.
* - RS_STG
  <br>(r,s)
  - Mainly applied for the modelling of storace cycles, but also in dispatching equations.
  - Lead from previous timeslice in the same cycle under the parent timeslice.
* - RS_STGAV
  <br>(r,s)
  - Only applicable to storage processes (STG): timeslice storage devices, to calculate activity costs in proportion to the time the commodity is stored.
  - Average residence time of storage activity.
* - RS_STGPRD
  <br>(r,s)
  - Only applicable to storage processes (STG): timeslice storage, inter-period storage or night storage devices.
  - Number of storage periods in a year for each timeslice.
* - RS_UCS
  <br>(r,s,side)
  - Applied in timeslice-dynamic user constraints, to refer to the previous timeslice in the same cycle.
  - Lead from previous timeslice in the same cycle under the parent timeslice.
* - RTP_FFCX
  <br>(r,v,t,p,cg,c,cg)
  - The efficiency parameter COEF_PTRAN is multiplied by the factor (1+RTP_FFCX).
  <br>Enters EQ_PTRANS equation.
  - Average SHAPE multiplier of the parameter FLO_FUNC and FLO_SUM efficiencies in the EQ_PTRANS equation in the period (t) for capacity with vintage period (v). The SHAPE curve that should be used is specified by the user parameter FLO_FUNCX. The SHAPE feature allows to alter technical parameter given for the vintage period as a function of the age of the installation.
* - RTCS_TSFR
  <br>(r,t,c,s,ts)
  - Defined for each commodity with COM_FR. Applied to flow variables in all equations in order to take into account cases where some of the variables may be defined at a different timeslice level than the level of the equation.
  - The effective handling of timeslice aggregation/disaggregation. If ts is below s in the timeslice tree, the value is 1, if s is below ts the value is COM_FR(r,s) / COM_FR(r,ts) for demand commodities with COM_FR given and G_YRFR(r,s) / G_YRFR(r,ts) for all other commodities.
  <br>The parameter is used to match the timeslice resolution of flow variables (VAR_FLO/VAR_IRE) and commodities. RTCS_TSFR is the coefficient of the flow variable, which is producing or consuming commodity c, in the commodity balance of c. If timeslice s corresponds to the commodity timeslice resolution of c and timeslice ts to the timeslice resolution of the flow variable two cases may occur:
  <br>The flow variables are on a finer timeslice level than the commodity balance: in this case the flow variables with timeslices s being below ts in the timeslice tree are summed to give the aggregated flow within timeslice ts. RTCS_TSFR has the value 1.
  <br>The flow variables are on coarser timeslice level than the commodity balance: in this case the flow variable is split-up on the finer timeslice level of the commodity balance according to the ratio of the timeslice duration of s to ts: RTCS_TSFR has the value = COM_FR(r,s) / COM_FR(r,s1) for demand commodities and G_YRFR(r,s) / G_YRFR(r,s1) otherwise. When COM_FR is used, the demand load curve is moved to the demand process. Thus, it is possible to model demand processes on an ANNUAL level and ensure at the same time that the process follows the given load curve COM_FR.
* - SALV_DEC
  <br>(r,v,p,k,ll)
  - For those technologies with salvage costs incurred after the model horizon the contribution to the objective function.
  - Salvage proportion of decommissioning costs made at period v with commissioning year k.
* - SALV_INV
  <br>(r,v,p,k)
  - For those technologies with salvage costs incurred after the model horizon the contribution to the objective function.
  - Salvage proportion of investment made at period v with commissioning year k.
* - YEARVAL
  <br>(y)
  - A value for each year.
  - Numerical value of year index (e.g. YEARVAL(\'1984\') equals 1984).
```

(report-parameters)=
##  Report parameters

### Overview of report parameters

The parameters generated internally by TIMES to document the results of a model run are listed in Table 15. These parameters can be imported into the **VEDA-BE** tool for further result analysis. They are converted out of the **GDX**[^32] file via the **gdx2veda** GAMS utility into a **VEDA-BE** compatible format according to the file **times2veda.vdd**[^33]. Note that some of the results are not transferred into parameters, but are directly accessed through the **times2veda.vdd** file (levels of commodity balances and peaking equation, total discounted value of objective function). The following naming conventions apply to the prefixes of the report parameters:
- CST\_: detailed annual undiscounted cost parameters; note that also the costs of past investments, which are constants in the objective function, are being reported;
- $PAR\_$: various primal and dual solution parameters;
- $EQ(l)\_$: directly accessed GAMS equation levels/marginals
- $REG\_$: regional total cost indicators.

```{list-table} Report parameters in TIMES
:name: times-report-parameters
:header-rows: 1

* - Report parameter[^34] (Indexes)
  - VEDA-BE attribute name
  - Description
* - AGG_OUT
  <br>(r,t,c,s)
  - VAR_FOut
  - Commodity production by an aggregation process:
  <br>Production of commodity (c) in period (t) and timeslice (s) from other commodities aggregated into c.
* - CAP_NEW
  <br>(r,v,p,t,uc_n)
  - Cap_New
  - Newly installed capacity and lumpsum investment by vintage and commissioning period:
  <br>New capacity and lumpsum investment of process (p) of vintage (v) commissioned in period (t).
* - CM_RESULT
  <br>(c,t)
  - VAR_Climate
  - Climate module results for the levels of climate variable (c) in period (t).
* - CM_MAXC_M
  <br>(c,t)
  - Dual_Clic
  - Climate module results for the duals of constraint related to climate variable (c) in period (t).
* - CST_ACTC
  <br>(r,v,t,p,uc_n)
  - Cost_Act
  - Annual activity costs:
  <br>Annual undiscounted variable costs (caused by ACT_COST) in period (t) associated with the operation (activity) of a process (p) with vintage period (v). Additional indicator (uc_n) for start-up costs.
* - CST_COMC
  <br>(r,t,c)
  - Cost_Com
  - Annual commodity costs:
  <br>Annual undiscounted costs for commodity (c) (caused by COM_CSTNET and COM_CSTPRD) in period (t).
* - CST_COME
  <br>(r,t,c)
  - Cost_Els
  - Annual elastic demand cost term:
  <br>Annual costs (losses) due to elastic demand changes of commodity (c). When elastic demands are used the objective function describes the total surplus of producers and consumers, which reaches its maximum in the equilibrium of demand and supply.
* - CST_COMX
  <br>(r,t,c)
  - Cost_Comx
  - Annual commodity taxes/subsidies:
  <br>Annual undiscounted taxes and subsidies for commodity (c) (caused by COM_TAXNET, COM_SUBNET, COM_TAXPRD, COM_SUBPRD) in period (t).
* - CST_DAM
  <br>(r,t,c)
  - Cost_Dam
  - Annual damage cost term:
  <br>Annual undiscounted commodity (c) related costs, caused by DAM_COST, in period (t).
* - CST_DECC
  <br>(r,v,t,p)
  - Cost_Dec
  - Annual decommissioning costs:
  <br>Annual undiscounted decommissioning costs (caused by NCAP_DCOST and NCAP_DLAGC) in period (t), associated with the dismantling of process (p) with vintage period (v).
* - CST_FIXC
  <br>(r,v,t,p)
  - Cost_Fom
  - Annual fixed operating and maintenance costs:
  <br>Annual undiscounted fixed operating and maintenance costs (caused by NCAP_FOM) in period (t) associated with the installed capacity of process (p) with vintage period (v).
* - CST_FIXX
  <br>(r,v,t,p)
  - Cost_Fixx
  - Annual fixed taxes/subsidies:
  <br>Annual undiscounted fixed operating and maintenance costs (caused by NCAP_FTAX, NCAP_FSUB) in period (t) associated with the installed capacity of process (p) with vintage period (v).
* - CST_FLOC
  <br>(r,v,t,p,c)
  - Cost_Flo
  - Annual flow costs (including import/export prices):
  <br>Annual undiscounted flow related costs (caused by FLO_COST, FLO_DELV, IRE_PRICE) in period (t) associated with a commodity (c) flow in/out of a process (p) with vintage period (v) as well as capacity related commodity flows (specified by NCAP_COM, NCAP_ICOM, NCAP_OCOM).
* - CST_FLOX
  <br>(r,v,t,p,c)
  - Cost_Flox
  - Annual flow taxes/subsidies:
  <br>Annual undiscounted flow related costs (caused by FLO_TAX, FLO_SUB) in period (t) associated with a commodity (c) flow in/out of a process (p) with vintage period (v) as well as capacity related commodity flows (specified by NCAP_COM, NCAP_ICOM, NCAP_OCOM).
* - CST_INVC
  <br>(r,v,t,p,uc_n)
  - Cost_Inv
  - Annual investment costs:
  <br>Annual undiscounted investment costs (caused by NCAP_COST) in period (t) spread over the economic lifetime (NCAP_ELIFE) of a process (p) with vintage period (v).
* - CST_INVX
  <br>(r,v,t,p,uc_n)
  - Cost_Invx
  - Annual investment taxes/subsidies:
  <br>Annual undiscounted investment costs (caused by NCAP_ITAX, NCAP_ISUB) in period (t) spread over the economic lifetime (NCAP_ELIFE) of a process (p) with vintage period (v).
* - CST_IREC
  <br>(r,v,t,p,c)
  - Cost_ire
  - Annual implied costs of endogenous trade:
  <br>Annual undiscounted costs from endogenous imports/exports of commodity (c) in period (t) associated with process (p) and vintage period (v), valued according to the marginal(s) of the trade equation of process p.
* - CST_PVC
  <br>(uc_n,r,c)
  - Cost_NPV
  - Total discounted costs by commodity (optional, activate by setting RPT_OPT(\'OBJ\',\'1\')=1):
  <br>Total present value of commodity-related costs in the base year, by type (with types COM, ELS, DAM). See Part III, Section 3.10 on the reporting options, and Table 16 below for acronym explanations.
* - CST_PVP
  <br>(uc_n,r,p)
  - Cost_NPV
  - Total discounted costs by process (optional, activate by setting RPT_OPT(\'OBJ\',\'1\')=1):
  <br>Total present value of process-related costs in the base year, by type (with types INV, INV+, FIX, ACT, FLO, IRE, where INV+ is only used for the split according to hurdle rate). See Part III, Section 3.10 on the reporting options, and Table 16 below for acronym explanations.
* - CST_SALV
  <br>(r,v,p)
  - Cost_Salv
  - Salvage values of capacities at EOH+1:
  <br>Salvage value of investment cost, taxes and subsidies of process (p) with vintage period (v), for which the technical lifetime exceeds the end of the model horizon, value at year EOH+1.
* - CST_TIME
  <br>(r,t,s,uc_n)
  - Time_NPV
  - Discounted value of time by period:
  <br>Present value of the time in each model period (t) by region (r), with s=\'ANNUAL\' and uc_n=\'COST\'/\'LEVCOST\' depending on whether the \$SET ANNCOST LEV reporting option has been used.
* - EQ_PEAK.L
  <br>(r,t,c,s)
  - EQ_Peak
  - Peaking Constraint Slack:
  <br>Level of the peaking equation (EQ_PEAK) of commodity (c) in period (t) and timeslice (s).
* - EQE_COMBAL.L
  <br>(r,t,c,s)
  - EQ_Combal
  - Commodity Slack/Levels:
  <br>Level of the commodity balance equation (EQE_COMBAL) of commodity (c) in period (t) and timeslice (s), where the equation is a strict equality.
* - EQG_COMBAL.L
  <br>(r,t,c,s)
  - EQ_Combal
  - Commodity Slack/Levels:
  <br>Level of the commodity balance equation (EQG_COMBAL) of commodity (c) in period (t) and timeslice (s), where the equation is an inequality.
* - F_IN
  <br>(r,v,t,p,c,s)
  - VAR_FIn
  - Commodity Consumption by Process:
  <br>Input flow (consumption) of commodity (c) in period (t) and timeslice (s) into process (p) with vintage period (v), including exchange processes.
* - F_OUT
  <br>(r,v,t,p,c,s)
  - VAR_FOut
  - Commodity Production by Process:
  <br>Output flow (production) of commodity (c) in period (t) and timeslice (s) from process (p) with vintage period (v), including exchange processes.
* - OBJZ.L
  <br>()
  - ObjZ
  - Total discounted system cost:
  <br>Level of the ObjZ variable, equal to the value of the objective function.
* - P_OUT
  <br>(r,t,p,c,s)
  - VAR_POut
  - Commodity Flow Levels by Process (set RPT_OPT(NRG_TYPE,\'1\')=1 to activate, see Part III):
  <br>Output flow level (power level) of commodity (c) in period (t) and timeslice (s) of process (p). By default only Output levels are reported, but with RPT_OPT(NRG_TYPE,\'3\')=2, input levels are reported as negative values.
* - PAR_ACTL
  <br>(r,v,t,p,s)
  - VAR_Act
  - Process Activity:
  <br>Level value of activity variable (VAR_ACT) in period (t), timeslice (s) of process (p) in vintage period (v).
* - PAR_ACTM
  <br>(r,v,t,p,s)
  - VAR_ActM
  - Process Activity -- Marginals:
  <br>Undiscounted annual reduced costs of activity variable (VAR_ACT) in period (t) and timeslice (s) of process (p) with vintage period (v); when the variable is at its lower (upper) bound, the reduced cost describes the increase (decrease) in the objective function caused by an increase of the lower (upper) bound by one unit; the reduced cost can also be interpreted as the necessary decrease or increase of the cost coefficient of the activity variable in the objective function, for the activity variable to leave its lower (upper) bound.
* - PAR_CAPL
  <br>(r,t,p)
  - VAR_Cap
  - Technology Capacity:
  <br>Capacity of process (p) in period (t), derived from VAR_NCAP in previous periods summed over all vintage periods. For still existing past investments, see PAR_PASTI.
* - PAR_CAPLO
  <br>(r,t,p)
  - PAR_CapLO
  - Capacity Lower Limit:
  <br>Lower bound on capacity variable (CAP_BND('LO')), only reported, if the lower bound is greater than zero.
* - PAR_CAPM
  <br>(r,t,p)
  - VAR_CapM
  - Technology Capacity -- Marginals:
  <br>Undiscounted reduced costs of capacity variable (VAR_CAP); only reported in those cases, in which the capacity variable is generated (bound CAP_BND specified or endogenous technology learning is used); the reduced costs describe in the case, that the capacity variable is at its lower (upper) bound, the cost increase (decrease) of the objective function caused by an increase of the lower (upper) bound by one unit. The reduced cost is undiscounted with COEF_PVT.
* - PAR_CAPUP
  <br>(r,t,p)
  - PAR_CapUP
  - Capacity Upper Limit:
  <br>Upper bound on capacity variable (CAP_BND('UP')), only reported, if upper bound is smaller than infinity.
* - PAR_COMBALEM
  <br>(r,t,c,s)
  - EQ_CombalM
  - Commodity Slack/Levels -- Marginals:
  <br>Undiscounted annual shadow price of commodity balance (EQE_COMBAL) being a strict equality. The marginal value describes the cost increase in the objective function, if the difference between production and consumption is increased by one unit. The marginal value can be determined by the production side (increasing production), but can also be set by the demand side (e.g., decrease of consumption by energy saving or substitution measures).
* - PAR_COMBALGM
  <br>(r,t,c,s)
  - EQ_CombalM
  - Commodity Slack/Levels -- Marginals:
  <br>Undiscounted annual shadow price of commodity balance (EQG_COMBAL) being an inequality (production being greater than or equal to consumption); positive number, if production equals consumption; the marginal value describes the cost increase in the objective function, if the difference between production and consumption is increased by one unit. The marginal value can be determined by the production side (increasing production), but can also be set by the demand side (e.g., decrease of consumption by energy saving or substitution measures).
* - PAR_COMNETL
  <br>(r,t,c,s)
  - VAR_Comnet
  - Commodity Net:
  <br>Level value of the variable corresponding the net level of a commodity (c) (VAR_COMNET). The net level of a commodity is equivalent to the total production minus total consumption of said commodity. It is only reported, if a bound or cost is specified for it or it is used in a user constraint.
* - PAR_COMNETM
  <br>(r,t,c,s)
  - VAR_ComnetM
  - Commodity Net -- Marginal:
  <br>Undiscounted annual reduced costs of the VAR_COMNET variable of commodity (c). It is only reported, if a bound or cost is specified for it or it is used in a user constraint.
* - PAR_COMPRDL
  <br>(r,t,c,s)
  - VAR_Comprd
  - Commodity Total Production:
  <br>Level value of the commodity production variable (VAR_COMPRD). The variable represents the total production of a commodity. It is only reported, if a bound or cost is specified for it or it is used in a user constraint.
* - PAR_COMPRDM
  <br>(r,t,c,s)
  - VAR_ComprdM
  - Commodity Total Production -- Marginal:
  <br>Undiscounted annual reduced costs of the commodity production variable (VAR_COMPRD). It is only reported, if a bound or cost is specified for it or it is used in a user constraint.
* - PAR_CUMCST
  <br>(r,v,t,uc_n,c)
  - VAR_CumCst
  - Cumulative costs by type (if constrained);\ Level of cumulative constraint for costs of type (uc_n) and currency (c) in region (r).
  <br>
* - PAR_CUMFLOL
  <br>(r,p,c,v,t)
  - EQ_Cumflo
  - Cumulative flow constraint -- Levels:
  <br>Level of cumulative constraint for flow of commodity (c) of process (p) between the year range (v--t).
* - PAR_CUMFLOM
  <br>(r,p,c,v,t)
  - EQ_CumfloM
  - Cumulative flow constraint -- Marginals:
  <br>Shadow price of cumulative constraint for flow of commodity (c) of process (p) between the year range (v--t). Not undiscounted.
* - PAR_EOUT
  <br>(r,v,t,p,c)
  - VAR_Eout
  - Electricity supply by technology and energy source (optional):
  <br>Electricity output of electricity supply processes by energy source; based on using NRG_TMAP to identify electricity commodities, but excludes standard and storage processes having electricity as input.
  <br>(Opted out by default -- set RPT_OPT(\'FLO\',\'5\')=1 to activate; see Part III, Section 3.10).
* - PAR_FLO
  <br>(r,v,t,p,c,s)
  - see: F_IN/F_OUT
  - Flow of commodity (c) entering or leaving process (p) with vintage period (v) in period (t).
* - PAR_FLO
  <br>(r,v,t,p,c,s)
  - none
  - Discounted reduced costs of flow variable of commodity (c) in period (t) of process (p) with vintage period (v); the reduced costs describe that the flow variable is at its lower (upper) bound, and give the cost increase (decrease) of the objective function caused by an increase of the lower (upper) bound by one unit; the undiscounted reduced costs can be interpreted as the necessary decrease / increase of the cost coefficient of the flow variable, such that the flow will leave its lower (upper) bound.
* - PAR_IRE
  <br>(r,v,t,p,c,s,ie)
  - see: F_IN/F_OUT
  - Inter-regional exchange flow of commodity (c) in period (t) via exchange process (p) entering region (r) as import (ie='IMP') or leaving region (r) as export (ie='EXP').
* - PAR_IREM
  <br>(r,v,t,p,c,s,ie)
  - none
  - Discounted reduced costs of inter-regional exchange flow variable of commodity (c) in period (t) of exchange process (p) with vintage period (v); the reduced costs describe that the flow variable is at its lower (upper) bound, and give the cost increase (or decrease) of the objective function caused by an increase of the lower (upper bound) by one unit; the undiscounted reduced costs can be interpreted as the necessary decrease / increase of the cost coefficient of the flow variable in the objective function, such that the flow will leave its lower (upper) bound.
* - PAR_IPRIC
  <br>(r,t,p,c,s,uc_n)
  - EQ_IreM
  - Inter-regional trade equations -- Marginals:
  <br>Undiscounted shadow price of the inter-regional trade equation of commodity (c) via exchange process (p) in period (t) and timeslice (s). The undiscounted shadow price can be interpreted as the import/export price of the traded commodity. Note: ucn={IMP/EXP}.
* - PAR_NCAPL
  <br>(r,t,p)
  - VAR_Ncap
  - Technology Investment -- New capacity:
  <br>Level value of investment variable (VAR_NCAP) of process (p) in period (v).
* - PAR_NCAPM
  <br>(r,t,p)
  - VAR_NcapM
  - Technology Investment -- Marginals:
  <br>Undiscounted reduced costs of investment variable (VAR_NCAP) of process (p); only reported, when the capacity variable is at its lower or upper bound; the reduced costs describe in the case, that the investment variable is at its lower (upper) bound, the cost increase (decrease) of the objective function caused by an increase of the lower (upper) bound by one unit; the undiscounted reduced costs can be interpreted as the necessary decrease / increase in the investment cost coefficient, such that the investment variable will leave its lower (upper) bound.
* - PAR_NCAPR
  <br>(r,t,p,uc_n)
  - VAR_NcapR
  - Technology Investment -- BenCost + ObjRange (see Part III, Section 3.10 for more details):
  <br>Cost-benefit and ranging indicators for process (p) in period (t), where uc_n is the name of the indicator:
  <br>COST - the total unit costs of VAR_NCAP (in terms of an equivalent investment cost)
  <br>CGAP - competitiveness gap (in terms of investment costs), obtained directly from the VAR_NCAP marginals (and optional ranging information)
  <br>GGAP - competitiveness gap (in terms of investment costs), obtained by checking also the VAR_ACT, VAR_FLO and VAR_CAP marginals, in case VAR_NCAP is basic at zero
  <br>RATIO - benefit / cost ratio, based on CGAP
  <br>GRATIO - benefit / cost ratio, based on GGAP
  <br>RNGLO - ranging information (LO) for VAR_NCAP (if ranging is activated; in terms of investment costs)
  <br>RNGUP - ranging information (UP) for VAR_NCAP (if ranging is activated; in terms of investment costs)
* - PAR_PASTI
  <br>(r,t,p,v)
  - VAR_Cap
  - Technology Capacity:
  <br>Residual capacity of past investments (NCAP_PASTI) of process (p) still existing in period (t), where vintage (v) is set to \'0\' to distinguish residual capacity from new capacity.
* - PAR_PEAKM
  <br>(r,t,c,s)
  - EQ_PeakM
  - Peaking Constraint Slack -- Marginals:
  <br>Undiscounted annual shadow price of peaking equation (EQ_PEAK) associated with commodity (c); since the peaking equation is at most only binding for one timeslice (s), a shadow price only exists for one timeslice. The shadow price can be interpreted as an additional premium to the shadow price of the commodity balance that consumers of commodity (c) have to pay for consumption during peak times. The premium is used (besides other sources) to cover the capacity related costs (e.g., investment costs) of capacity contributing reserve capacity during peak times.
* - PAR_TOP
  <br>(r,t,p,c,uc_n)
  - PAR_Top
  - Process topology:
  <br>Process topology indicators for reporting use. Values are all zero, period (t) is the first milestone year, and uc_n = IN/OUT. (Opted out by default -- SET RPT_TOP YES to activate.)
* - PAR_UCMRK
  <br>(r,t,uc_n,c,s)
  - User_conFXM
  - Marginal cost of market-share constraint:
  <br>Undiscounted shadow price of group-wise market share constraint (defined with PRC_MARK) for commodity c, identified with name uc_n, in period t and timeslice s.
* - PAR_UCRTP
  <br>(uc_n,r,t,p,c)
  - User_DynbM
  - Marginal cost of dynamic process bound constraint:
  <br>Undiscounted shadow price of dynamic process-wise bound constraint, identified with name uc_n, for variable c (CAP / NCAP / ACT), in period t and timeslice s.
* - PAR_UCSL
  <br>(uc_n,r,t,s)
  - User_con
  - Level of user constraint (or its slack) (only reported when the VAR_UC variables are used):
  <br>The level of user constraint (uc_n) by region (r), period (t) and timeslice (s). The levels should be zero whenever the RHS constant is zero and the equation is binding. If the constraint is not binding, the level together with the RHS constant gives the gap for the equation to become binding.
* - PAR_UCSM
  <br>(uc_n,r,t,s)
  - User_conFXM
  - Marginal cost of user constraint (all bound types):
  <br>Marginal of user constraint (uc_n) by region (r), period (t) and timeslice (s). The marginals are undiscounted, if the constraint is defined by region and period. The marginals of cumulative and multi-region user constraints are not undiscounted (reported with **r** or **t** as \'NONE\') due to ambiguity. However, ambiguously undiscounted marginals of multi-region constraints are also reported by each region involved.
* - REG_ACOST
  <br>(r,t,uc_n)
  - Reg_ACost
  - Regional total annualized costs by period:
  <br>Total annualized costs in region (r) by period (t) and cost category. The cost categories are INV, INVX, FIX, FIXX, VAR, VARX, IRE, ELS and DAM (see Table 16 below for more information).
* - REG_IREC
  <br>(r)
  - Reg_irec
  - Regional total discounted implied trade cost:
  <br>Total discounted implied trade costs in region (r), derived by multiplying the shadow prices of the trade equations by the trade volumes. The sum of REG_IREC over regions is zero.
* - REG_OBJ
  <br>(r)
  - Reg_obj
  - Regional total discounted system cost:
  <br>Discounted objective value (EQ_OBJ) for each region (r).
* - REG_WOBJ
  <br>(r,uc_n,c)
  - Reg_wobj
  - Regional total discounted system cost by component:
  <br>Discounted objective value (EQ_OBJ) for each region (r), by cost type (uc_n) and currency (c). The cost types are: INV, INVX, FIX, FIXX, VAR, VARX, ELS, DAM (see Table 16 below for more information).
* - VAL_FLO
  <br>(r,v,t,p,c)
  - Val_Flo
  - Annual commodity flow values:
  <br>Flows of process (p) multiplied by the commodity balance marginals of those commodities (c) in period (t); the values can be interpreted as the market values of the process inputs and outputs. |
```

### Acronyms used in cost reporting parameters

The acronyms used in the reporting parameters for referring to certain types of costs are summarized in {numref}`acronyms-in-cost-reporting`. The acronyms are used as qualifiers in the $uc\_n$ index of each reporting attribute, and are accessible in VEDA-BE through that same dimension.

```{list-table} Acronyms used in the cost reporting parameters.
:name: acronyms-in-cost-reporting
:header-rows: 1

* - Cost parameter
  - Component acronyms
* - CAP_NEW (r,v,p,t,uc_n)
  - Newly installed capacity and lump-sum investment costs by vintage and commissioning period:
  <br>INSTCAP New capacity of vintage v commissioned in period t
  <br>LUMPINV Lump-sum investment costs for vintage v in period t
  <br>LUMPIX Lump-sum investment taxes & subsidies for vintage v, period t
  <br>INV+ Lump-sum investment portion attributable to hurdle rate in excess of the general discount rate
  <br>INVX+ Lump-sum tax & subsidy portion attributable to hurdle rate in excess of the general discount rate
* - CST_PVC (uc_n,r,c)
  - Total discounted costs by commodity (optional):
  <br>COM Commodity-related costs, taxes and subsidies
  <br>ELS Losses in elastic demands
  <br>DAM Damage costs
* - CST_PVP (uc_n,r,p)
  - Total discounted costs by process (optional):
  <br>INV Investment costs, taxes and subsidies, excluding portions attributable to hurdle rates in excess of the general discount rate
  <br>INV+ Investment costs, taxes and subsidies, portions attributable to hurdle rates in excess of the general discount rate
  <br>FIX Fixed costs, taxes and subsidies
  <br>ACT Activity costs
  <br>FLO Flows costs taxes and subsidies (including exogenous IRE prices)
  <br>IRE Implied trade costs minus revenues
 * - REG_ACOST (r,t,uc_n)
   - Regional total annualized costs by period:
  <br>INV Annualized investment costs
  <br>INVX Annualized investment taxes and subsidies
  <br>FIX Annual fixed costs
  <br>FIXX Annual fixed taxes and subsidies
  <br>VAR Annual variable costs
  <br>VARX Annual variable taxes and subsidies
  <br>IRE Annual implied trade costs minus revenues
  <br>ELS Annual losses in elastic demands
  <br>DAM Annual damage costs
* - REG_WOBJ (r,uc_n,c)
  - Regional total discounted system cost by component:
  <br>INV Investment costs
  <br>INVX Investment taxes and subsidies
  <br>FIX Fixed costs
  <br>FIXX Fixed taxes and subsidies
  <br>VAR Variable costs
  <br>VARX Variable taxes and subsidies
  <br>ELS Losses in elastic demands
  <br>DAM Damage costs
```

### The levelized cost reporting option

As indicated in {numref}`times-report-parameters` above, the reporting of levelized costs for each process can be requested by setting the option RPT_OPT(\'NCAP\', \'1\'). The results are stored in the VEDA-BE $Var\_NcapR$ result attribute, with the qualifier \'LEVCOST\' (with a possible system label prefix).

The levelized cost calculation option looks to weight all the costs influencing the choice of a technology by TIMES. It takes into consideration investment, operating, fuel, and other costs as a means of comparing the full cost associated with each technology.

Levelized cost can be calculated according to the following general formula:

$$LEC = \frac{\sum_{t = 1}^{n}{\frac{IC_{t}}{(1 + r)^{t - 1}} + \frac{OC_{t} + VC_{t} + \sum_{i}^{}{FC_{i,t} + FD_{i,t}} + \sum_{j}^{}{ED_{j,t}}}{(1 + r)^{t - 0.5}} -}\frac{\sum_{k}^{}{BD_{k,t}}}{(1 + r)^{t - 0.5}}}{\sum_{t = 1}^{n}\frac{\sum_{m}^{}{MO_{m,t}}}{(1 + r)^{t - 0.5}}}$$ (3-1)

where
- $r$ = discount rate (e.g. 5%)
- $IC_t$ = investment expenditure in (the beginning of) year $t$
- $OC_t$ = fixed operating expenditure in year $t$
- $VC_t$ = variable operating expenditure in year $t$
- $FC_{it}$ = fuel-specific operating expenditure for fuel $i$ in year $t$
- $FD_{it}$ = fuel-specific acquisition expenditure for fuel $i$ in year $t$
- $ED_{jt}$ = emission-specific allowance expenditure for emission $j$ in year $t$ (optional)
- $BD_{kt}$ = revenues from by-product $k$ in year $t$ (optional; see below)
- $MO_{mt}$ = output of main product $m$ in year $t$

The exponent $(t-0.5)$ in the formula indicates the good practice of using mid-year discounting for continuous streams of annual expenditures.

In TIMES, the specific investment, fixed and variable O&M costs and fuel-specific flow costs are calculated directly from the input data. However, for the fuel acquisition prices, emission prices and by-product prices, ***commodity marginals*** from the model solution are used. All the unit costs are multiplied by the corresponding ***variable levels*** as given by the model solution: investment cost and fixed operating costs are multiplied by the amounts of capacity installed / existing, variable operation costs by the activity levels, and fuel-specific costs by the process flow levels. Mid-year discounting can also be activated.

The outputs of the main products are taken from the flow levels of the commodities in the primary group (PG) of the process. An exception is CHP processes, for which the electricity output is considered the sole main output, and heat is considered as a by-product.

**Options for variants of levelized cost reporting:**

1. <ins>Do not include emission prices or by-product revenues in the calculation</ins> (RPT_OPT('NCAP','1') = --1):

> In this option emission prices are omitted from the calculation, in accordance with the most commonly used convention for LEC calculation. Consequently, any by-product revenues need to be omitted as well, because if emissions have prices, the by-product prices in the solution would of course be polluted by those prices, and thus it would be inconsistent to use them in the calcu­lation. Instead, in this case any amount of by-product energy produced by ELE, CHP and HPL processes is indirectly credited by reducing the fuel-specific costs in the calculation to the fraction of the main output in the total amount of energy produced.

2. <ins>Include both emission prices and by-product revenues in the calculation</ins> (RPT_OPT('NCAP','1') = 1):

> In this option both emission prices and by-product revenues are included in the calculation. The levelized cost thus represents the unit cost after subtracting the levelized value of all by-products from the gross value of the levelized cost. This approach of crediting for by-products in the LEC calculation has been utilized, for example, in the IEA *Projected Costs of Generating Electricity* studies.

3. <ins>Include not only emission prices and by-product revenues, but also the revenues from the main product in the calculation</ins> (RPT_OPT('NCAP','1') = 2):

> This option is similar to option (2) above, but in this case all product revenues are included in the calculation, including also the peak capacity credit from the TIMES peaking equation (when defined). The calculated LEC value thus represents the levelized **net** unit cost after subtracting the value of all products from the gross levelized cost. For competitive new capacity vintages, the resulting levelized cost should in this case generally be *negative*, because investments into technologies that enter the solution are normally profitable. For the marginal technologies the levelized cost can be expected to be very close to zero. Only those technologies that have been in some way forced into the solution, e.g. by specifying lower bounds on the capacity or by some other types of constraints, should normally have a positive levelized cost when using this option.

In the TIMES calculation, the expenditures for technology investments and process commodity flows include also taxes minus subsidies, if such have been specified. The levelized costs are calculated by process vintage, but only for new capacity vintages, as for them both the full cost data influencing technology choice and the operating history starting from the commissioning date are available, which is rarely the case for existing vintages.


[^21]: The term *target timeslice level* or *target timeslice* is used in the following as synonym for the timeslice level or timeslices which are required by the model generators depending on the process or commodity timeslice resolution (**prc_tsl** and **com_tsl** respectively).

[^22]: Note that as an exception, for NCAP_AF direct inheritance and aggregation will be disabled if any values are specified at the process timeslice level. However, this may be circumvented by using NCAP_AFS for defining the values at process timeslices.

[^23]: The first row contains the parameter name, the second row contains in brackets the index domain over which the parameter is defined.

[^24]: This column gives references to related input parameters (in upper case) or sets (in lower case) being used in the context of this parameter as well as internal parameters/sets or result parameters being derived from the input parameter.

[^25]: This column lists the unit of the parameter, the possible range of its numeric value \[in square brackets\] and the inter-/extrapolation rules that apply.

[^26]: An indication of circumstances for which the parameter is to be provided or omitted, as well as description of inheritance/aggregation rules applied to parameters having the timeslice (**s)** index.

[^27]: Equations or variables that are directly affected by the parameter.

[^28]: Abbreviation i/e = inter-/extrapolation

[^29]: Standard aggregation not implemented for FLO_BND.

[^30]: The indexing of auxiliary consumption flows or emissions of inter-regional exchange processes is illustrated in {numref}`indexing-aux-consumption`.

[^31]: The first row contains the parameter name, the second row contains in brackets the index domain, for which the parameter is defined.

[^32]: GDX stands for GAMS Data Exchange. A GDX file is a binary file that stores the values of one or more GAMS symbols such as sets, parameters variables and equations. GDX files can be used to prepare data for a GAMS model, present results of a GAMS model, store results of the same model using different parameters etc. They do not store a model formulation or executable statements.

[^33]: The use of the **gdx2veda** tool together with the **times2veda.vdd** control file and the **VEDA-BE** software are described in Part V.

[^34]: First row: parameter name; second row (in brackets): the index domain, for which the parameter is defined.
