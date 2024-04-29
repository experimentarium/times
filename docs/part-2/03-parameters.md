# Parameters

While sets describe structural information of the energy system or qualitative characteristics of its entities (e.g. processes or commodities), parameters contain numerical information. Examples of parameters are the import price of an energy carrier or the investment cost of a technology. Most parameters are time-series where a value is provided (or interpolated) for each year ($datayear$). The TIMES model generator distinguishes between user input parameters and internal parameters. The former are provided by the modeller (usually by way of a data handling system or "shell" such a VEDA-FE or ANSWER-TIMES), while the latter are internally derived from the user input parameters, in combination with information given by sets, in order to calculate for example the cost coefficients in the objective function. This Chapter first covers the user input parameters in Section 3.1 and then describes the most important internal parameters as far as they are relevant for the basic understanding of the equations (Section 3.2). Section 3.3 presents the parameters used for reporting the results of a model run.

## User input parameters

This section provides an overview of the user input parameters that are available in TIMES to describe the energy system. Before presenting the various parameters in detail in Section 3.1.3 two preprocessing algorithms applied to the user input data are presented, namely the inter-/extrapolation and the inheritance/aggregation routines. User input parameters that are time-dependent can be provided by the user for those years for which statistical information or future projections are available, and the inter-/extrapolation routine described in Section 3.1.1 used to adjust the input data to the years required for the model run. Timeslice dependent parameters do not have to be provided on the timelice level of a process, commodity or commodity flow. Instead the so-called inheritance/aggregation routine described in Section 3.1.2 assigns the input data from the user provided timeslice level to the appropriate timeslice level as necessary.

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

:::{table} Option codes for the control of time series data interpolation.
:name: ie-control-options

| Option code  | Action                                                                                                                            | Applies to  |
| :----------: | --------------------------------------------------------------------------------------------------------------------------------- | :---------: |
| 0 (or none)  | Interpolation and extrapolation of data in the default way as predefined in TIMES (see below)                                     |     All     |
|     \<0      | No interpolation or extrapolation of data (only valid for non-cost parameters).                                                   |     All     |
|      1       | Interpolation between data points but no extrapolation.                                                                           |     All     |
|      2       | Interpolation between data points entered, and filling-in all points outside the inter­polation window with the EPS value.        |     All     |
|      3       | Forced interpolation and both forward and backward extrapolation throughout the time horizon.                                     |     All     |
|      4       | Interpolation and backward extrapolation                                                                                          |     All     |
|      5       | Interpolation and forward extrapolation                                                                                           |     All     |
|      10      | Migrated interpolation/extrapolation within periods                                                                               | Bounds, RHS |
|      11      | Interpolation migrated at end-points, no extrapolation                                                                            | Bounds, RHS |
|      12      | Interpolation migrated at ends, extrapolation with EPS                                                                            | Bounds, RHS |
|      14      | Interpolation migrated at end, backward extrapolation                                                                             | Bounds, RHS |
|      15      | Interpolation migrated at start, forward extrapolation                                                                            | Bounds, RHS |
| YEAR (≥1000) | Log-linear interpolation beyond the specified YEAR, and both forward and backward extrapolation outside the interpolation window. |     All     |

:::

Migration means that data points are interpolated and extrapolated within each period but not across periods. This method thus migrates any data point specified for other than $milestoneyr$ year to the corresponding $milestoneyr$ year within the period, so that it will be effective in that period.

Log-linear interpolation means that the values in the data series are interpreted as coefficients of annual change beyond a given $YEAR$. The $YEAR$ can be any year, including model years. The user only has to take care that the data values in the data series correspond to the interpretation given to them when using the log-linear option. For simplicity, however, the first data point is always interpreted as an absolute value, because log-linear interpolation requires at least one absolute data point to start with.

#### Default inter/extrapolation

The standard default method of inter-/extrapolation corresponds to the option 3, which interpolates linearly between data points, while it extrapolates the first/last data point constantly backward/forward. This method, full interpolation and extrapolation, is by default applied to most TIMES time series parameters. However, the parameters listed in {numref}`no-default-full-ie` are by default **NOT** inter/extrapolated in this way, but have a different default method.

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

:::{table} Parameters not being fully inter/extrapolated by default
:name: no-default-full-ie

| Parameter                                                                                                                                                                                                                 | Justification                                                                                                                      |  Default I/E   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | :------------: |
| ACT_BND <br>CAP_BND <br>NCAP_BND <br>NCAP_DISC <br>FLO_FR <br>FLO_SHAR <br>STGIN_BND <br>STGOUT_BND <br>COM_BNDNET <br>COM_BNDPRD <br>COM_CUMNET <br>COM_CUMPRD <br>REG_BNDCST <br>RCAP_BND <br>IRE_BND <br>IRE_XBND <br> | Bound may be intended at specific periods only.                                                                                    | 10 (migration) |
| PRC_MARK                                                                                                                                                                                                                  | Constraint may be intended at specific periods only                                                                                |       11       |
| PRC_RESID                                                                                                                                                                                                                 | Residual capacity usually intended to be only interpolated                                                                         |      1\*       |
| UC_RHST <br>UC_RHSRT<br>UC_RHSRTS                                                                                                                                                                                         | User constraint may be intended for specific periods only                                                                          | 10 (migration) |
| NCAP_AFM <br>NCAP_FOMM <br>NCAP_FSUBM <br>NCAP_FTAXM<br>                                                                                                                                                                  | Interpolation meaningless for these parameters (parameter value is a discrete number indicating which MULTI curve should be used). | 10 (migration) |
| COM_ELASTX <br>FLO_FUNCX <br>NCAP_AFX <br>NCAP_FOMX <br>NCAP_FSUBX <br>NCAP_FTAXX                                                                                                                                         | Interpolation meaningless for these parameters (parameter value is a discrete number indicating which SHAPE curve should be used). | 10 (migration) |
| NCAP_PASTI                                                                                                                                                                                                                | Parameter describes past investment for a single vintage year.                                                                     |      none      |
| NCAP_PASTY                                                                                                                                                                                                                | Parameter describes number of years over which to distribute past investments.                                                     |      none      |
| CM_MAXC                                                                                                                                                                                                                   | Bound may be intended at specific years only                                                                                       |      none      |
| PEAKDA_BL                                                                                                                                                                                                                 | Blending parameters at the moment not interpolated                                                                                 |      none      |

:::

\* If only a single $PRC\_RESID$ value is specified, assumed to decay linearly over $NCAP\_TLIFE$ years

**Example 2:**

Assume that we define the following log-linear I/E option for a $FLO\_SHAR$ data series:

```
FLO_SHAR('REG','0','PRC1','COAL','IN_PRC1','ANNUAL','UP') = 2005;
```

This parameter specifies a log-linear control option with the value for the threshold YEAR of log-linear interpolation taken from 2005. The option specifies that all data points up to the year 2005 should be interpreted normally (as absolute data values), but all values beyond that year should be interpreted as coefficients of annual change. By using this interpretation, TIMES will then apply full inter­polation and extrapolation to the whole data series. It is the responsibility of the user to ensure that the first data point and all data points up to (and including) the year 2005 represent absolute values of the parameter, and that all subsequent data points represent coefficients of annual change. Using the data of the example above, the first data point beyond 2005 is found for the year 2010, and it has the value of 0.12. The inter­pretation thus requires that the maximum flow share of COAL in the commodity group IN_PRC1 is actually meant to increase by as much as 12% per annum between the years 1995 and 2010, and by 5% per annum between 2010 and 2020.

#### Applicability

All the enhanced I/E options described above are available for all TIMES timeseries parameters, excluding $PRC\_RESID$ and $COM\_BPRICE$. $PRC\_RESID$ is always interpolated, as if option 1 were used, but is also extrapolated forwards over $TLIFE$ when either I/E option 5 or 15 is specified. $COM\_BPRICE$ is not interpolated at all, as it is obtained from the Baseline solution. Moreover, the I/E options are not applicable to the integer-valued parameters related to the $SHAPE$ and $MULTI$ tables, which are listed in {numref}`interpolation-not-applicable`.

:::{table} Parameters which cannot be interpolated.
:name: interpolation-not-applicable

| Parameter                                                                         | Comment                                                                                                         |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| NCAP_AFM <br>NCAP_FOMM <br>NCAP_FSUBM <br>NCAP_FTAXM                              | Parameter value is a discrete numbers indicating which MULTI curve should be used, and not a time series datum. |
| COM_ELASTX <br>FLO_FUNCX <br>NCAP_AFX <br>NCAP_FOMX <br>NCAP_FSUBX <br>NCAP_FTAXX | Parameter value is a discrete number indicating which SHAPE curve should be used, and not a time series datum.  |

:::

Nonetheless, a few options are supported also for the extrapolation of the $MULTI$ and $SHAPE$ index parameters, as shown in {numref}`e-option-codes-shape-multi`. The extrapolation can be done either only inside the data points provided by the user, or both inside and outside those data points. When using the inside data points option, the index specified for any $datayear$ is extrapolated to all model years ($v$) between that $datayear$ and the following $datayear$ for which the $SHAPE$ index is specified. The extrapolation options are available for all of the $SHAPE$ and $MULTI$ parameters listed in {numref}`interpolation-not-applicable`.

:::{table} Option codes for the extrapolation of SHAPE/MULTI indexes.
:name: e-option-codes-shape-multi

|  Option code  | Action                                                    |
| :-----------: | --------------------------------------------------------- |
| <=0 (or none) | No extrapolation (default)                                |
|       1       | Extrapolation between data points only                    |
|       2       | Extrapolation between and outside data points             |
|       4       | Extrapolation between data points and backwards           |
|       5       | Extrapolation between data points and forwards            |
|      11       | Extrapolation between data points only, migration at ends |

:::

**Example:**

The user has specified the following two SHAPE indexes and a control option for extrapolation:

```
NCAP_AFX('REG', '0', 'PRC1') = 1;
NCAP_AFX('REG', '1995', 'PRC1') = 12;
NCAP_AFX('REG', '2010', 'PRC1') = 13;
``` 
 
 In this case, all model years ($v$) between 1995 and 2010 will get the shape index 12. No extrapolation is done for model years ($v$) beyond 2010 or before 1995.

### Inheritance and aggregation of timesliced input parameters

As mentioned before, processes and commodities can be modelled in TIMES on different timeslice levels. Some of the input parameters that describe a process or a commodity are timeslice specific, i.e. they have to be provided by the user for specific timeslices, e.g. the availability factor $NCAP\_AF$ of a power plant operating on a \'DAYNITE\' timeslice level. During the process of developing a model, the timeslice resolution of some processes or even the entire model may be refined. One could imagine for example the situation that a user starts developing a model on an \'ANNUAL\' timeslice level and refines the model later by refining the timeslice definition of the processes and commodities. In order to avoid the need for all the timeslice related parameters to be re-entered again for the finer timeslices, TIMES supports inheritance and aggregation of parameter values along the timeslice tree.

Inheritance in this context means that input data being specified on a coarser timeslice level (higher up the tree) are inherited to a finer timeslice level (lower down the tree), whereas aggregation means that timeslice specific data are aggregated from a finer timeslice level (lower down the tree) to a coarser one (further up the tree). The inheritance feature may also be useful in some cases where the value of a parameter should be the same over all timeslices, since in this case it is sufficient to provide the parameter value for the \'ANNUAL\' timeslice which is then inherited to the required finer target timeslices.[^21]

```{list-table} Inheritance and aggregation rules
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

```{figure} assets/image9.png
:name: inheritance-aggregation-rules-parameters
:align: center
Inheritance and aggregation rules for timeslice specific parameters in TIMES.
```

### Overview of user input parameters

A list of all user input parameters (except for those specific to the TIMES-MACRO variants) is given in Table 13. For the MACRO input parameters, the reader is advised to consult the separate documentation. In order to facilitate the recognition by the user of to which part of the model a parameter relates the following naming conventions apply to the prefixes of the parameters ({numref}`uip-naming-conventions`).

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

:::{table} Abbreviations for default I/E method in Table 13.
:name: ie-abbreviations

| Abbreviation | Description                                   |
| ------------ | --------------------------------------------- |
| STD          | Standard full inter-/extrapolation (option 3) |
| MIG          | Migration (option 10)                         |
| \<number\>   | Option code for any other default method      |
| none         | No default inter-/extrapolation               |
| N/A          | Inter-/extrapolation not applicable           |

:::

+-----------+--------+----------+-------------+----------+-----------+
| **Input   | **R    | **Units  | **Insta     | **Descr  | *         |
| pa        | elated | / Ranges | nces**[^26] | iption** | *Affected |
| rameter** | sets / | &        |             |          | equations |
|           | param  | Default  | (Required / |          | or        |
| (Inde     | eters* | values & | Omit /      |          | variabl   |
| xes)[^23] | *[^24] | Default  | Special     |          | es**[^27] |
|           |        | int      | conditions) |          |           |
|           |        | er-/extr |             |          |           |
|           |        | apolatio |             |          |           |
|           |        | n**[^25] |             |          |           |
+===========+========+==========+=============+==========+===========+
| ACT_BND   |        | Units of | Since       | Bound on | Activity  |
|           |        | activity | inter-/ex   | the      | limit     |
| (         |        |          | trapolation | overall  | c         |
| r,datayea |        | \[0,∞);\ | default is  | activity | onstraint |
| r,p,s,bd) |        | default  | MIG, the    | a        | (EQ(l)    |
|           |        | value:   | bound must  | process. | \_ACTBND) |
|           |        | none     | be          |          | when s is |
|           |        |          | explicitly  |          | above     |
|           |        | Default  | specified   |          | prc_tsl.  |
|           |        | i        | for each    |          |           |
|           |        | /e[^28]: | period,     |          | Direct    |
|           |        | MIG      | unless an   |          | bound on  |
|           |        |          | inter-/ex   |          | activity  |
|           |        |          | trapolation |          | variable  |
|           |        |          | option is   |          | (VAR_ACT) |
|           |        |          | set.        |          | when at   |
|           |        |          |             |          | the       |
|           |        |          | If the      |          | prc_tsl   |
|           |        |          | bound is    |          | level.    |
|           |        |          | specified   |          |           |
|           |        |          | for a       |          |           |
|           |        |          | timeslice s |          |           |
|           |        |          | above the   |          |           |
|           |        |          | process     |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | resolution  |          |           |
|           |        |          | (prc_tsl),  |          |           |
|           |        |          | the bound   |          |           |
|           |        |          | is applied  |          |           |
|           |        |          | to the sum  |          |           |
|           |        |          | of the      |          |           |
|           |        |          | activity    |          |           |
|           |        |          | variables   |          |           |
|           |        |          | according   |          |           |
|           |        |          | to the      |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | tree.       |          |           |
|           |        |          |             |          |           |
|           |        |          | Standard    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_COST  | OBJ_   | Monetary |             | Variable | Applied   |
|           | ACOST, | unit per |             | costs    | to the    |
| (r,dataye | CST    | unit of  |             | as       | activity  |
| ar,p,cur) | _ACTC, | activity |             | sociated | variable  |
|           |        |          |             | with the | (VAR_ACT) |
|           | C      | \[       |             | activity | as a      |
|           | ST_PVP | open\];\ |             | of a     | component |
|           |        | default  |             | process. | of the    |
|           |        | value:   |             |          | objective |
|           |        | none     |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        | Default  |             |          | _OBJVAR). |
|           |        | i/e: STD |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_CSTPL | ACT_   | Monetary | Used as an  | Partial  | Generates |
| (r,dataye | MINLD\ | unit per | alternative | load     | an        |
| ar,p,cur) | ACT    | unit of  | or          | cost     | a         |
|           | _LOSPL | activity | supplement  | penalty, | dditional |
|           |        |          | to using    | defined  | term in   |
|           |        | \[0,∞);\ | AC          | as an    | EQ_OBJVAR |
|           |        | default  | T_LOSPL(r,y | ad       | for the   |
|           |        | value:   | ,p,\'FX\'). | ditional | increase  |
|           |        | none     | When used   | cost per | in        |
|           |        |          | as an       | activity | operating |
|           |        | Default  | a           | at the   | cost.     |
|           |        | i/e: STD | lternative, | minimum  |           |
|           |        |          | the fuel    | o        |           |
|           |        |          | increase at | perating |           |
|           |        |          | the minimum | level,   |           |
|           |        |          | operating   | corre    |           |
|           |        |          | level that  | sponding |           |
|           |        |          | should be   | to the   |           |
|           |        |          | included in | ef       |           |
|           |        |          | the cost    | ficiency |           |
|           |        |          | penalty     | loss at  |           |
|           |        |          | must be     | that     |           |
|           |        |          | embedded in | load     |           |
|           |        |          | the         | level.   |           |
|           |        |          | ACT_CSTPL   |          |           |
|           |        |          | c           | Added as |           |
|           |        |          | oefficient. | an extra |           |
|           |        |          |             | term to  |           |
|           |        |          |             | variable |           |
|           |        |          |             | costs in |           |
|           |        |          |             | the      |           |
|           |        |          |             | o        |           |
|           |        |          |             | bjective |           |
|           |        |          |             | and      |           |
|           |        |          |             | re       |           |
|           |        |          |             | porting. |           |
+-----------+--------+----------+-------------+----------+-----------+
| AC        | A      | Corrency | Can be used | Defines  | Activates |
| T_CSTRMP\ | CT_UPS | unit per | for         | ramp-up  | g         |
| (r,       |        | unit of  | standard    | (L=UP)   | eneration |
| datayear, |        | capacity | processes   | or       | of        |
| p,bd,cur) |        | (change  | in basic,   | r        | EQ        |
|           |        | in load) | advanced    | amp-down | _ACTRMPC. |
|           |        |          | and         | (L=LO)   |           |
|           |        | \[0,∞);\ | discrete    | cost per | Generates |
|           |        | default  | unit        | unit of  | an        |
|           |        | value:   | commitment  | load     | a         |
|           |        | none     | extensions. | change   | dditional |
|           |        |          |             | (in      | term in   |
|           |        | Default  | Can also be | capacity | EQ_OBJVAR |
|           |        | i/e: STD | used for    | units).  | for the   |
|           |        |          | lo          |          | increase  |
|           |        |          | ad-shifting | For      | in        |
|           |        |          | processes   | *        | operating |
|           |        |          | for         | *load-sh | cost.     |
|           |        |          | defining    | ifting** |           |
|           |        |          | the cost of | p        |           |
|           |        |          | shifting    | rocesses |           |
|           |        |          | loads per   | defines  |           |
|           |        |          | unit of     | the cost |           |
|           |        |          | demand load | of       |           |
|           |        |          | by one      | shifting |           |
|           |        |          | hour.       | one unit |           |
|           |        |          |             | of load  |           |
|           |        |          |             | by one   |           |
|           |        |          |             | hour,    |           |
|           |        |          |             | forward  |           |
|           |        |          |             | (UP) or  |           |
|           |        |          |             | backward |           |
|           |        |          |             | (LO).    |           |
+-----------+--------+----------+-------------+----------+-----------+
| A         | ACT_   | Currency | Activates   | Defines  | Generates |
| CT_CSTSD\ | CSTUP\ | units    | the         | start-up | an        |
| (r,data   | ACT_S  | per unit | advanced    | (bd=UP)  | a         |
| year,p,up | DTIME\ | of       | unit        | and      | dditional |
| t,bd,cur) | ACT_   | st       | commitment  | shutdown | term in   |
|           | MAXNON | arted-up | option.     | costs    | EQ_OBJVAR |
|           |        | capacity |             | (bd=LO)  | for the   |
|           |        |          | In the case | per unit | increase  |
|           |        | \[0,∞);\ | of the      | of       | in        |
|           |        | Default  | shut-down   | st       | operating |
|           |        | value:   | costs, only | arted-up | cost.     |
|           |        | none     | the tuple   | c        |           |
|           |        |          | (upt, bd) = | apacity, |           |
|           |        | Default  | (HOT, LO)   | differ   |           |
|           |        | i/e: STD | is a valid  | entiated |           |
|           |        |          | instance    | by       |           |
|           |        |          | for this    | start-up |           |
|           |        |          | parameter.  | type     |           |
|           |        |          |             | (upt).\  |           |
|           |        |          | Requires    | The      |           |
|           |        |          | the         | start-up |           |
|           |        |          | parameter   | type of  |           |
|           |        |          | ACT_MAXNON  | a power  |           |
|           |        |          | to be       | plant    |           |
|           |        |          | defined as  | depends  |           |
|           |        |          | well.       | on its   |           |
|           |        |          |             | non-ope  |           |
|           |        |          |             | rational |           |
|           |        |          |             | time     |           |
|           |        |          |             | after    |           |
|           |        |          |             | sh       |           |
|           |        |          |             | ut-down, |           |
|           |        |          |             | as       |           |
|           |        |          |             | defined  |           |
|           |        |          |             | by using |           |
|           |        |          |             | ACT      |           |
|           |        |          |             | _MAXNON. |           |
+-----------+--------+----------+-------------+----------+-----------+
| A         | ACT_   | Monetary | The tslvl   | Cost of  | Activates |
| CT_CSTUP\ | MINLD\ | unit per | level       | process  | g         |
| (r,dat    | A      | unit of  | refers to   | start-up | eneration |
| ayear,p,t | CT_UPS | capacity | the         | per unit | of        |
| slvl,cur) |        |          | timeslice   | of       | E         |
|           |        | \[0,∞);\ | cycle for   | st       | QL_ACTUPS |
|           |        | default  | which the   | arted-up | eqs.      |
|           |        | value:   | start-up    | c        |           |
|           |        | none     | cost is     | apacity. | Generates |
|           |        |          | defined.    |          | an        |
|           |        | Default  |             | Added as | a         |
|           |        | i/e: STD | Only        | an extra | dditional |
|           |        |          | applicable  | term to  | term in   |
|           |        |          | when the    | variable | the       |
|           |        |          | min. stable | costs in | variable  |
|           |        |          | operating   | the      | operating |
|           |        |          | level has   | o        | costs     |
|           |        |          | been        | bjective | included  |
|           |        |          | defined     | and      | in        |
|           |        |          | with        | re       | E         |
|           |        |          | ACT_MINLD.  | porting. | Q_OBJVAR. |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_CUM   | F      | Activity | The years   | Bound on | Generates |
| (r,p,     | LO_CUM | unit     | y1 and y2   | the      | an        |
| y1,y2,bd) |        |          | may be any  | cu       | instance  |
|           |        | \[0,∞);\ | years of    | mulative | of the    |
|           |        | default  | the set     | amount   | c         |
|           |        | value:   | allyear;    | of       | umulative |
|           |        | none     | where y1    | annual   | c         |
|           |        |          | may also be | process  | onstraint |
|           |        | Default  | \'BOH\' for | activity |           |
|           |        | i/e: N/A | first year  | between  | (E        |
|           |        |          | of first    | the      | Q_CUMFLO) |
|           |        |          | period and  | years y1 |           |
|           |        |          | y2 may be   | and y2,  |           |
|           |        |          | \'EOH\' for | within a |           |
|           |        |          | last year   | region.  |           |
|           |        |          | of last     |          |           |
|           |        |          | period.     |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_EFF\  |        | Activity | The group   | Activity | Generates |
| (         |        | unit per | cg may be a | ef       | instances |
| r,datayea |        | flow     | single      | ficiency | of the    |
| r,p,cg,s) |        | unit     | commodity,  | for      | activity  |
|           |        |          | group, or   | process, | e         |
|           |        | \[0,∞);\ | commodity   | i.e.     | fficiency |
|           |        | Default  | type on the | amount   | c         |
|           |        | value:   | shadow      | of       | onstraint |
|           |        | none     | side, or a  | activity | (EQ       |
|           |        |          | single      | per unit | E_ACTEFF) |
|           |        | Default  | commodity   | of       |           |
|           |        | group    | in the PCG; | c        |           |
|           |        | ef       | cg=\'ACT\'  | ommodity |           |
|           |        | ficiency | refers to   | flows in |           |
|           |        | =1 when  | the default | the      |           |
|           |        | values   | shadow      | group    |           |
|           |        | are      | group. If   | cg.      |           |
|           |        | s        | no group    |          |           |
|           |        | pecified | efficiency  | For more |           |
|           |        | only for | is defined, | inf      |           |
|           |        | in       | shadow      | ormation |           |
|           |        | dividual | group is    | on       |           |
|           |        | comm     | assumed to  | usage,   |           |
|           |        | odities. | be the      | see      |           |
|           |        |          | commodity   | Section  |           |
|           |        | Default  | type.       | 6.3 for  |           |
|           |        | i/e: STD | Individual  | details  |           |
|           |        |          | commodity   | about    |           |
|           |        |          | e           | EQE      |           |
|           |        |          | fficiencies | _ACTEFF. |           |
|           |        |          | are         |          |           |
|           |        |          | multiplied  |          |           |
|           |        |          | with the    |          |           |
|           |        |          | shadow      |          |           |
|           |        |          | group       |          |           |
|           |        |          | efficiency  |          |           |
|           |        |          | (           |          |           |
|           |        |          | default=1). |          |           |
|           |        |          |             |          |           |
|           |        |          | Levelized   |          |           |
|           |        |          | to the      |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | level of    |          |           |
|           |        |          | the flow    |          |           |
|           |        |          | variables   |          |           |
|           |        |          | in the      |          |           |
|           |        |          | shadow      |          |           |
|           |        |          | group.\     |          |           |
|           |        |          | Direct      |          |           |
|           |        |          | i           |          |           |
|           |        |          | nheritance. |          |           |
|           |        |          | Weighted    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_FLO\  |        | Flow     | Inherited   | Flow of  | Es        |
| (         |        | unit per | /aggregated | com      | tablishes |
| r,datayea |        | activity | to the      | modities | a         |
| r,p,cg,s) |        | unit     | timeslice   | in cg in | trans     |
|           |        |          | levels of   | pr       | for­mation |
|           |        | \[0,∞);\ | the the     | oportion | rel       |
|           |        | default  | process     | to the   | ationship |
|           |        | value:   | flow        | process  | (E        |
|           |        | none     | (cg=com) or | a        | Q_PTRANS) |
|           |        |          | the process | ctivity, | between   |
|           |        | Default  | activity\   | in       | the flows |
|           |        | i/e: STD | (when       | t        | in the    |
|           |        |          | cg=genuine  | imeslice | PCG and   |
|           |        |          | group).     | s.       | one or    |
|           |        |          |             |          | more      |
|           |        |          | Direct      |          | input (or |
|           |        |          | i           |          | output)   |
|           |        |          | nheritance. |          | com       |
|           |        |          |             |          | modities. |
|           |        |          | Weighted    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| A         | ACT    | Decimal  | Endogenous  | Partial  | Generates |
| CT_LOSPL\ | _MINLD | fraction | partial     | load     | instances |
| (r,datay  |        |          | load        | ef       | of the    |
| ear,p,bd) | ACT    | \[0,∞);\ | modeling    | ficiency | partial   |
|           | _CSTPL | default  | can only be | par      | load      |
|           |        | values:  | used for    | ameters. | e         |
|           |        |          | processes   |          | fficiency |
|           |        | FX: none | that have   | 1\)      | c         |
|           |        |          | their       | (bd=     | onstraint |
|           |        | LO:      | efficiency  | \'FX\'): | EQ_ACTPL. |
|           |        | default  | modelled by | Prop     |           |
|           |        | value is | the ACT_EFF | ortional |           |
|           |        | A        | parameter,  | increase |           |
|           |        | CT_MINLD | which must  | in       |           |
|           |        | or 0.1\  | be defined  | specific |           |
|           |        | if that  | on the      | fuel     |           |
|           |        | is not   | shadow side | con      |           |
|           |        | defined  | of the      | ­sumption |           |
|           |        |          | process.    | at       |           |
|           |        | UP: 0.6  |             | minimum  |           |
|           |        |          | For other   | o        |           |
|           |        | Default  | processes,  | perating |           |
|           |        | i/e: STD | the         | level\   |           |
|           |        |          | ACT_CSTPL   | 2)       |           |
|           |        |          | parameter   | (bd=\    |           |
|           |        |          | can be used | 'LO\'):\ |           |
|           |        |          | for         | Minimum  |           |
|           |        |          | modeling a  | o        |           |
|           |        |          | cost        | perating |           |
|           |        |          | penalty at  | level of |           |
|           |        |          | partial     | partial  |           |
|           |        |          | loads.      | load     |           |
|           |        |          |             | op       |           |
|           |        |          |             | eration\ |           |
|           |        |          |             | 3)       |           |
|           |        |          |             | (bd=\    |           |
|           |        |          |             | 'UP\'):\ |           |
|           |        |          |             | Fraction |           |
|           |        |          |             | of       |           |
|           |        |          |             | feasible |           |
|           |        |          |             | load     |           |
|           |        |          |             | range    |           |
|           |        |          |             | above    |           |
|           |        |          |             | the      |           |
|           |        |          |             | minimum  |           |
|           |        |          |             | o        |           |
|           |        |          |             | perating |           |
|           |        |          |             | level,   |           |
|           |        |          |             | below    |           |
|           |        |          |             | which    |           |
|           |        |          |             | the      |           |
|           |        |          |             | ef       |           |
|           |        |          |             | ficiency |           |
|           |        |          |             | losses   |           |
|           |        |          |             | are      |           |
|           |        |          |             | assumed  |           |
|           |        |          |             | to       |           |
|           |        |          |             | occur.   |           |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_LOSSD | ACT_   | Dimen    | Can only be | Used for | Activates |
|           | LOSPL\ | sionless | used when   | modeling | g         |
| (r,       | ACT_   |          | the         | en       | eneration |
| datayear, | MINLD\ | \[0,∞);\ | advanced    | dogenous | of        |
| p,upt,bd) | ACT_S  | default  | unit        | partial  | EQ_SUDPLL |
|           | DTIME\ | value:   | commitment  | load     |           |
|           | A      | none     | option is   | ef       |           |
|           | CT_EFF |          | used for    | ficiency |           |
|           |        | Default  | the process | losses   |           |
|           |        | i/e: STD | (therefore, | during   |           |
|           |        |          | defining\   | the      |           |
|           |        |          | both        | start-up |           |
|           |        |          | ACT_CSTSD   | and      |           |
|           |        |          | and         | s        |           |
|           |        |          | ACT_MAXNON  | hut-down |           |
|           |        |          | is          | phase.   |           |
|           |        |          | required)   |          |           |
|           |        |          |             | -   With |           |
|           |        |          | Requires    |          |           |
|           |        |          | also that   |    bd=UP |           |
|           |        |          | ACT_EFF has |          |           |
|           |        |          | been used   |  defines |           |
|           |        |          | for         |          |           |
|           |        |          | defining    | increase |           |
|           |        |          | the process |     in   |           |
|           |        |          | efficiency  |          |           |
|           |        |          | (on the     | specific |           |
|           |        |          | shadow side |     fuel |           |
|           |        |          | of the      |     con  |           |
|           |        |          | process).   | ­sump­tion |           |
|           |        |          |             |     at   |           |
|           |        |          |             |     the  |           |
|           |        |          |             |          |           |
|           |        |          |             |    start |           |
|           |        |          |             |     up   |           |
|           |        |          |             |     load |           |
|           |        |          |             |          |           |
|           |        |          |             |    level |           |
|           |        |          |             |          |           |
|           |        |          |             |  defined |           |
|           |        |          |             |     by   |           |
|           |        |          |             |     the  |           |
|           |        |          |             |          |           |
|           |        |          |             |    ratio |           |
|           |        |          |             |     A    |           |
|           |        |          |             | CT_MINLD |           |
|           |        |          |             |     /    |           |
|           |        |          |             |          |           |
|           |        |          |             |   ACT_SD |           |
|           |        |          |             | TIME(upt |           |
|           |        |          |             | ,\'UP\') |           |
|           |        |          |             |     for  |           |
|           |        |          |             |          |           |
|           |        |          |             | start-up |           |
|           |        |          |             |     type |           |
|           |        |          |             |     upt; |           |
|           |        |          |             |          |           |
|           |        |          |             | -   With |           |
|           |        |          |             |          |           |
|           |        |          |             |    bd=LO |           |
|           |        |          |             |          |           |
|           |        |          |             |  defines |           |
|           |        |          |             |     the  |           |
|           |        |          |             |          |           |
|           |        |          |             | increase |           |
|           |        |          |             |     in   |           |
|           |        |          |             |          |           |
|           |        |          |             | specific |           |
|           |        |          |             | fuel     |           |
|           |        |          |             | con      |           |
|           |        |          |             | sump­tion |           |
|           |        |          |             | at the   |           |
|           |        |          |             | start up |           |
|           |        |          |             | load     |           |
|           |        |          |             | level    |           |
|           |        |          |             | defined  |           |
|           |        |          |             | by the   |           |
|           |        |          |             | ratio    |           |
|           |        |          |             | A        |           |
|           |        |          |             | CT_MINLD |           |
|           |        |          |             | /        |           |
|           |        |          |             | ACT      |           |
|           |        |          |             | _SDTIME( |           |
|           |        |          |             | \'HOT\', |           |
|           |        |          |             | \'LO\'). |           |
+-----------+--------+----------+-------------+----------+-----------+
| AC        | ACT_   | hours    | Can only be | Max.     | Activates |
| T_MAXNON\ | CSTSD\ |          | used when   | non-ope  | g         |
| (r,dataye | ACT_   | \[0,∞);\ | the         | rational | eneration |
| ar,p,upt) | SDTIME | default  | advanced    | time     | of        |
|           |        | value:   | unit        | before   | EQ_SUDUPT |
|           |        | none     | commitment  | tr       |           |
|           |        |          | option is   | ansition |           |
|           |        | Default  | used for    | to next  |           |
|           |        | i/e: STD | the process | stand-by |           |
|           |        |          | (thus       | co       |           |
|           |        |          | defining\   | ndition, |           |
|           |        |          | ACT_CSTSD   | by       |           |
|           |        |          | is          | start-up |           |
|           |        |          | required)   | type, in |           |
|           |        |          |             | hours    |           |
|           |        |          |             |          |           |
|           |        |          |             | -        |           |
|           |        |          |             |  Defines |           |
|           |        |          |             |     the  |           |
|           |        |          |             |     max. |           |
|           |        |          |             |          |           |
|           |        |          |             |  non-ope |           |
|           |        |          |             | rational |           |
|           |        |          |             |     time |           |
|           |        |          |             |          |           |
|           |        |          |             |   before |           |
|           |        |          |             |     a    |           |
|           |        |          |             |     su   |           |
|           |        |          |             | bsequent |           |
|           |        |          |             |          |           |
|           |        |          |             | start-up |           |
|           |        |          |             |     of   |           |
|           |        |          |             |     type |           |
|           |        |          |             |     upt. |           |
+-----------+--------+----------+-------------+----------+-----------+
| A         | AC     | Decimal  | Can only be | Minimum  | Generates |
| CT_MINLD\ | T_UPS\ | fraction | used for    | stable   | instances |
| (r,da     | ACT    |          | standard    | o        | of        |
| tayear,p) | _CSTUP | \[0,∞);\ | processes   | perating | equations |
|           |        | default  | (not IRE or | level of |           |
|           | ACT_   | value:   | STG). Must  | a        | E         |
|           | CSTPL\ | none     | be defined  | disp     | Q_CAPLOAD |
|           | ACT    |          | if          | atchable | and       |
|           | _LOSPL | Default  | ACT_CSTUP   | process. |           |
|           |        | i/e: STD | or ACT_TIME |          | EQ        |
|           |        |          | is          |          | E_ACTUPS. |
|           |        |          | specified.  |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| AC        | ACT_   | hours    | Can only be | Defines  | Activates |
| T_SDTIME\ | CSTSD\ |          | used when   | the      | g         |
| (r,       | ACT_   | \[0,∞);\ | ACT_CSTSD   | duration | eneration |
| datayear, | MAXNON | default  | is          | of       | of        |
| p,upt,bd) |        | value:   | specified   | start-up | EQ        |
|           |        | none     | for the     | (bd=UP)  | _SUDTIME, |
|           |        |          | process     | and      | and       |
|           |        | Default  | (advanced   | s        |           |
|           |        | i/e: STD | unit        | hut-down | used also |
|           |        |          | commitment  | (bd=LO)  | in the    |
|           |        |          | option)     | phases,  | e         |
|           |        |          |             | by       | quations\ |
|           |        |          | When        | start-up | EQ_ACTPL  |
|           |        |          | specifying  | type, in |           |
|           |        |          | the         | hours.   | E         |
|           |        |          | duration of |          | Q_SDSLANT |
|           |        |          | the         |          |           |
|           |        |          | shut-down   |          | E         |
|           |        |          | phase, only |          | Q_SDMINON |
|           |        |          | the tuple   |          |           |
|           |        |          | (upt,b      |          | EQ_SUDPLL |
|           |        |          | d)=(HOT,LO) |          |           |
|           |        |          | is valid    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_TIME  | ACT    | Hours    | Can be used | 1\)      | Generates |
| (r,dataye | _MINLD |          | for         | Minimum  | instances |
| ar,p,lim) |        | \[0,∞);\ | standard    | online   | of        |
|           | ACT    | default  | processes   |          | EQ        |
|           | _CSTUP | value:   | when        | (UP) /   | L_ACTUPC. |
|           |        | none     | start-up    | offline  |           |
|           | AC     |          | costs have  | (LO)     | For       |
|           | T_UPS\ | Default  | been        |          | load      |
|           | ST     | i/e: STD | modeled,    | hours of | -shifting |
|           | G_SIFT |          | using both  | a        | storage   |
|           |        |          | ACT_MINLD   | process  | p         |
|           |        |          | and         |          | rocesses, |
|           |        |          |             | with     | generates |
|           |        |          | ACT_CSTUP   | start-up | instances |
|           |        |          | at the      | costs    | of        |
|           |        |          |             |          |           |
|           |        |          | DAY         | modeled  | E         |
|           |        |          | NITE/WEEKLY | (li      | Q_SLSIFT. |
|           |        |          | level.      | m=LO/UP) |           |
|           |        |          |             |          |           |
|           |        |          | The lim     | 2\)      |           |
|           |        |          | type \'FX\' | Maximum  |           |
|           |        |          | is not      | number   |           |
|           |        |          | supported   |          |           |
|           |        |          | for this    | of       |           |
|           |        |          | use, and is | start-up |           |
|           |        |          | ignored.    | cycles   |           |
|           |        |          |             |          |           |
|           |        |          | Can also be | within   |           |
|           |        |          | used for    | process  |           |
|           |        |          | lo          | t        |           |
|           |        |          | ad-shifting | ime­slice |           |
|           |        |          | storage     | cycles   |           |
|           |        |          | processes,  | (lim=N). |           |
|           |        |          | for         |          |           |
|           |        |          | defining    | 3\)      |           |
|           |        |          | the maximum | Maximum  |           |
|           |        |          | de          | delay or |           |
|           |        |          | lay/advance | advance  |           |
|           |        |          | of load     | of load  |           |
|           |        |          | shift, or   | shift    |           |
|           |        |          | the         | (lim=U   |           |
|           |        |          | time-window | P/LO/FX) |           |
|           |        |          | for load    | or load  |           |
|           |        |          | balancing   | b        |           |
|           |        |          | (cf. Sect.  | alancing |           |
|           |        |          | 4.3.9).     | time     |           |
|           |        |          |             | (lim=N)  |           |
|           |        |          |             | for a    |           |
|           |        |          |             | load-    |           |
|           |        |          |             | shifting |           |
|           |        |          |             | storage. |           |
+-----------+--------+----------+-------------+----------+-----------+
| ACT_UPS\  | ACT_   | Decimal  | Inherited   | Maximum  | Generates |
| (         | MINLD\ | fraction | /aggregated | r        | instances |
| r,datayea | ACT    |          | to the      | amp-rate | of        |
| r,p,s,bd) | _CSTUP | \[0,∞);\ | timeslice   | (        | equation  |
|           |        | default  | levels of   | down/up) | EQ        |
|           | ACT_   | value:   | the process | of       | _ACTRAMP. |
|           | CSTPL\ | none     | activity.   | process  |           |
|           | ACT    |          |             | activity |           |
|           | _LOSPL | Default  | Direct      | as a     |           |
|           |        | i/e: STD | i           | fraction |           |
|           |        |          | nheritance. | of       |           |
|           |        |          |             | nominal  |           |
|           |        |          | Weighted    | on-line  |           |
|           |        |          | a           | capacity |           |
|           |        |          | ggregation. | per      |           |
|           |        |          |             | hour.    |           |
|           |        |          | The ramp    |          |           |
|           |        |          | rates can   |          |           |
|           |        |          | only be     |          |           |
|           |        |          | specified   |          |           |
|           |        |          | with        |          |           |
|           |        |          | bd=LO/UP.   |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| B         | M, D,  |          | Required    | B        |           |
|           | E,     |          | for each    | eginning |           |
| \(t\)     | COE    |          | milestone   | year of  |           |
|           | F_CPT, |          | year, but   | period   |           |
|           | rtp_   |          | is          | t.       |           |
|           | vintyr |          | aut         |          |           |
|           |        |          | o-generated |          |           |
|           |        |          | if not      |          |           |
|           |        |          | specified   |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| CAP_BND   | PAR_   | Capacity | Since       | Bound on | Imposes   |
|           | CAPLO, | unit     | inter-/ex   | in       | an        |
| (r,datay  | PAR    |          | trapolation | vestment | indirect  |
| ear,p,bd) | _CAPUP | \[0,∞);\ | is default  | in new   | limit on  |
|           |        | default  | is MIG, a   | c        | the       |
|           |        | value:   | bound must  | apacity. | capacity  |
|           |        | none     | be          |          | transfer  |
|           |        |          | specified   |          | equation  |
|           |        | Default  | for each    |          | (EQ_CPT)  |
|           |        | i/e: MIG | period      |          | by means  |
|           |        |          | desired, if |          | of a      |
|           |        |          | no explicit |          | direct    |
|           |        |          | inter-/ex   |          | bound on  |
|           |        |          | trapolation |          | the       |
|           |        |          | option is   |          | capacity  |
|           |        |          | given.      |          | variable  |
|           |        |          | Relaxed if  |          | (         |
|           |        |          | upper bound |          | VAR_CAP). |
|           |        |          | less than   |          |           |
|           |        |          | existing    |          |           |
|           |        |          | no          |          |           |
|           |        |          | n-retirable |          |           |
|           |        |          | capacity.   |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| CM_CONST  |        | Constant | See         | Various  | EQ_CLITOT |
|           |        | specific | Appendix on | climate  |           |
| (item)    |        | unit     | Climate     | module   | E         |
|           |        |          | Module for  | co       | Q_CLICONC |
|           |        | \        | details.    | nstants, |           |
|           |        | [open\]; |             | e.g. phi | E         |
|           |        |          |             | and      | Q_CLITEMP |
|           |        | default  |             | sigma    |           |
|           |        | value:   |             | values   | E         |
|           |        | See      |             | between  | Q_CLIBEOH |
|           |        | Appendix |             | res      |           |
|           |        |          |             | ervoirs. |           |
|           |        | Default  |             |          |           |
|           |        | i/e: N/A |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         |        | Forcing  | Default     | R        | EQ_CLITOT |
| M_EXOFORC |        | unit     | values are  | adiative |           |
|           |        |          | provided.   | forcing  |           |
| (year)    |        | \        | See         | from     |           |
|           |        | [open\]; | Appendix on | e        |           |
|           |        |          | Climate     | xogenous |           |
|           |        | default  | Module for  | sources  |           |
|           |        | value:   | details.    |          |           |
|           |        | none     |             |          |           |
|           |        |          |             |          |           |
|           |        | Default  |             |          |           |
|           |        | i/e: STD |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         |        | Units of | The global  | Mapping  | EQ_CLITOT |
| M_GHGMAP\ |        | climate  | emissions   | and      |           |
| (r,       |        | module   | in the      | co       |           |
| c,cm_var) |        | e        | climate     | nversion |           |
|           |        | missions | module      | of       |           |
|           |        | per      | (cm_var)    | regional |           |
|           |        | units of | are         | GHG      |           |
|           |        | regional | \'CO2-GtC\' | e        |           |
|           |        | e        | (GtC),      | missions |           |
|           |        | missions | \'CH4-Mt\'  | to       |           |
|           |        |          | (Mt) and    | global   |           |
|           |        | \[0, ∞); | \'N2O-Mt\'  | e        |           |
|           |        |          | (Mt). See   | missions |           |
|           |        | default  | Appendix on | in the   |           |
|           |        | value:   | Climate     | climate  |           |
|           |        | none     | Module for  | module   |           |
|           |        |          | details.    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         |        | Climate  | Default     | Cal      | EQ_CLITOT |
| M_HISTORY |        | variable | values are  | ibration |           |
|           |        | unit     | provided    | values   | E         |
| (y        |        |          | until 2010. | for CO2  | Q_CLICONC |
| ear,item) |        | \[0, ∞); | See         | and      |           |
|           |        |          | Appendix on | forcing  | E         |
|           |        | default  | Climate     |          | Q_CLITEMP |
|           |        | value:   | Module for  |          |           |
|           |        | none     | details.    |          | E         |
|           |        |          |             |          | Q_CLIBEOH |
|           |        | Default  |             |          |           |
|           |        | i/e: STD |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| CM_LINFOR |        | Forcing  | With lim    | Pa       | EQ_CLITOT |
|           |        | unit per | types       | rameters |           |
| (         |        | conce    | LO/UP, CO2  | of       |           |
| datayear, |        | ntration | forcing     | li       |           |
| item,lim) |        | unit     | function    | nearized |           |
|           |        |          | can be      | forcing  |           |
|           |        | \        | au          | f        |           |
|           |        | [open\]; | tomatically | unctions |           |
|           |        |          | linearized  |          |           |
|           |        | default  | between the |          |           |
|           |        | value:   | co          |          |           |
|           |        | none     | ncent­ration |          |           |
|           |        |          | levels      |          |           |
|           |        | Default  | given. For  |          |           |
|           |        | i/e: STD | CH4 and     |          |           |
|           |        |          | N2O, lim    |          |           |
|           |        |          | types FX/N  |          |           |
|           |        |          | must be     |          |           |
|           |        |          | used        |          |           |
|           |        |          | (N=co       |          |           |
|           |        |          | n­cent­ration |          |           |
|           |        |          | multiplier, |          |           |
|           |        |          | FX=constant |          |           |
|           |        |          | term). See  |          |           |
|           |        |          | Appendix on |          |           |
|           |        |          | Climate     |          |           |
|           |        |          | Module for  |          |           |
|           |        |          | details.    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| CM_MAXC   |        | Climate  | Since no    | Maximum  | EQ_CLIMAX |
|           |        | variable | default     | level of |           |
| (datay    |        | unit     | inter-/ext  | climate  |           |
| ear,item) |        |          | rapolation, | variable |           |
|           |        | \[0, ∞); | bounds must |          |           |
|           |        |          | be          |          |           |
|           |        | default  | explicitly  |          |           |
|           |        | value:   | specified   |          |           |
|           |        | none     | for each    |          |           |
|           |        |          | desired     |          |           |
|           |        | Default  | year,       |          |           |
|           |        | i/e:     | unless an   |          |           |
|           |        | none     | explicit    |          |           |
|           |        |          | inter-/ex   |          |           |
|           |        |          | trapolation |          |           |
|           |        |          | option is   |          |           |
|           |        |          | set.\       |          |           |
|           |        |          | See         |          |           |
|           |        |          | Appendix on |          |           |
|           |        |          | Climate     |          |           |
|           |        |          | Module for  |          |           |
|           |        |          | details.    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| COM_AGG   |        | C        | When        | Agg      | Adds a    |
| (r,dayaye |        | ommodity | commodity   | regation | term in   |
| ar,c1,c2) |        | units    | lim_type is | of       | EQ(l      |
|           |        |          | LO and      | c        | )\_COMBAL |
|           |        | \[       | commodity   | ommodity | and       |
|           |        | open\];\ | type is not | NET/PRD  |           |
|           |        | default  | DEM,        | pr       | EQ(l)     |
|           |        | value:   | VAR_COMNET  | oduction | \_COMPRD. |
|           |        | none     | of c1 is    | to the   |           |
|           |        |          | aggregated  | pr       |           |
|           |        | Default  | to c2;      | oduction |           |
|           |        | i/e: STD |             | side of  |           |
|           |        |          | When        | the      |           |
|           |        |          | commodity   | balance  |           |
|           |        |          | lim_type is | of       |           |
|           |        |          | FX/N or     | another  |           |
|           |        |          | commodity   | co       |           |
|           |        |          | type is     | mmodity. |           |
|           |        |          | DEM,        |          |           |
|           |        |          | VAR_COMPRD  |          |           |
|           |        |          | of c1 is    |          |           |
|           |        |          | aggregated  |          |           |
|           |        |          | to c2.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         | rhs_c  | C        | Since       | Limit on | The       |
| OM_BNDNET | ombal, | ommodity | inter-/ex   | the net  | balance   |
|           | rcs_   | unit     | trapolation | amount   | c         |
| (         | combal |          | default is  | of a     | onstraint |
| r,datayea |        | \[       | MIG, a      | c        | is set to |
| r,c,s,bd) |        | open\];\ | bound must  | ommodity | an        |
|           |        | default  | be          | (v       | equality  |
|           |        | value:   | specified   | ariable\ | (EQE      |
|           |        | none     | for each    | VAR      | _COMBAL). |
|           |        |          | period      | _COMNET) |           |
|           |        | Default  | desired, if | within a | Either    |
|           |        | i/e: MIG | no explicit | region   | the finer |
|           |        |          | inter-/ex   | for a    | timeslice |
|           |        | Remark:  | trapolation | pa       | variables |
|           |        | All      | option is   | rticular | are       |
|           |        | VA       | given.      | ti       | summed    |
|           |        | R_COMNET |             | meslice. | (EQ(l)    |
|           |        | v        | If the      |          | \_BNDNET) |
|           |        | ariables | bound is    |          | or the    |
|           |        | are by   | specified   |          | bound     |
|           |        | default  | for a       |          | applied   |
|           |        | non-n    | timeslice s |          | direct to |
|           |        | egative, | above the   |          | the       |
|           |        | i.e.     | commodity   |          | commodity |
|           |        | have     | timeslice   |          | net       |
|           |        | lower    | resolution  |          | va        |
|           |        | bounds   | (com_tsl),  |          | riable(VA |
|           |        | of zero  | the bound   |          | R_COMNET) |
|           |        |          | is applied  |          | when at   |
|           |        |          | to the sum  |          | the       |
|           |        |          | of the net  |          | commodity |
|           |        |          | commodity   |          | level     |
|           |        |          | variables   |          | (         |
|           |        |          | (           |          | com_tsl). |
|           |        |          | VAR_COMNET) |          |           |
|           |        |          | below it,   |          |           |
|           |        |          | according   |          |           |
|           |        |          | to the      |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | tree.       |          |           |
|           |        |          |             |          |           |
|           |        |          | Standard    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         | rhs_c  | C        | Since       | Limit on | The       |
| OM_BNDPRD | omprd, | ommodity | inter-/ex   | the      | balance   |
|           | rcs_   | unit     | trapolation | amount   | c         |
| (         | comprd |          | default is  | of a     | onstraint |
| r,datayea |        | \[0,∞);\ | MIG, a      | c        | is set to |
| r,c,s,bd) |        | default  | bound must  | ommodity | an        |
|           |        | value:   | be          | produced | equality  |
|           |        | none     | specified   | (        | (EQE      |
|           |        |          | for each    | variable | _COMBAL). |
|           |        | Default  | period      |          |           |
|           |        | i/e: MIG | desired, if | VAR      | Finer     |
|           |        |          | no explicit | _COMPRD) | timeslice |
|           |        | Remark:  | inter-/ex   |          | variables |
|           |        | All      | trapolation | within a | summed    |
|           |        | VA       | option is   | region   | (EQ(l)\   |
|           |        | R_COMPRD | given.      | for a    | _BNDPRD). |
|           |        | v        |             | pa       |           |
|           |        | ariables | If the      | rticular | or the    |
|           |        | are by   | bound is    | ti       | bound is  |
|           |        | default  | specified   | meslice. | applied   |
|           |        | non-n    | for a       |          | direct to |
|           |        | egative, | timeslice s |          | the       |
|           |        | i.e.     | being above |          | commodity |
|           |        | have     | the         |          | p         |
|           |        | lower    | commodity   |          | roduction |
|           |        | bounds   | timeslice   |          | variable  |
|           |        | of zero  | resolution  |          | (VA       |
|           |        |          | (com_tsl),  |          | R_COMPRD) |
|           |        |          | the bound   |          | when at   |
|           |        |          | is applied  |          | the       |
|           |        |          | to the sum  |          | commodity |
|           |        |          | of the      |          | level     |
|           |        |          | commodity   |          | (         |
|           |        |          | production  |          | com_tsl). |
|           |        |          | variables   |          |           |
|           |        |          | (           |          |           |
|           |        |          | VAR_COMPRD) |          |           |
|           |        |          | below it,   |          |           |
|           |        |          | according   |          |           |
|           |        |          | to the      |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | tree.       |          |           |
|           |        |          |             |          |           |
|           |        |          | Standard    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         | COM_   | Monetary | The control | Base     | Controls  |
| OM_BPRICE | ELAST, | unit per | parameter   | price of | the       |
|           | COM    | c        | \$SET       | a demand | inclusion |
| (r,t      | _STEP, | ommodity | TIMESED     | c        | of the    |
| ,c,s,cur) | C      | unit     | 'YES' to    | ommodity | elastic   |
|           | OM_VOC |          | activate    | for the  | demand    |
|           |        | \[       | elastic     | elastic  | variable  |
|           |        | open\];\ | demands     | demand   | (V        |
|           |        | default  | must be     | form     | AR_ELAST) |
|           |        | value:   | set.        | ulation. | in the    |
|           |        | none     |             |          | commodity |
|           |        |          |             |          | balance   |
|           |        | Default  |             |          | equat     |
|           |        | i/e:     |             |          | ion(EQ(l) |
|           |        | none     |             |          | \_COMBAL) |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | elastic   |
|           |        |          |             |          | demand    |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (V        |
|           |        |          |             |          | AR_ELAST) |
|           |        |          |             |          | in the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJELS). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | OBJ_   | Monetary | Direct      | Cost on  | Forces    |
| OM_CSTNET | COMNT, | unit per | i           | the net  | the net   |
|           |        | c        | nheritance. | amount   | commodity |
| (r        | CST    | ommodity |             | of a     | variable  |
| ,datayear | _COMC, | unit     | Weighted    | c        | (VA       |
| ,c,s,cur) |        |          | a           | ommodity | R_COMNET) |
|           | CS     | \[       | ggregation. | within a | to be     |
|           | T_PVC, | open\];\ |             | region   | included  |
|           |        | default  |             | for a    | in the    |
|           | rhs_c  | value:   |             | pa       | equality  |
|           | ombal, | none     |             | rticular | balance   |
|           | rcs_   |          |             | ti       | c         |
|           | combal | Default  |             | meslice. | onstraint |
|           |        | i/e: STD |             |          | (EQE      |
|           |        |          |             |          | _COMBAL). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to said   |
|           |        |          |             |          | variable  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | cost      |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | OBJ_   | Monetary | Direct      | Cost on  | Forces    |
| OM_CSTPRD | COMPD, | unit per | i           | the      | the       |
|           | CST    | c        | nheritance. | pr       | commodity |
| (r        | _COMC, | ommodity |             | oduction | p         |
| ,datayear |        | unit     | Weighted    | of a     | roduction |
| ,c,s,cur) | CS     |          | a           | co       | variable  |
|           | T_PVC, | \[       | ggregation. | mmodity, | (VA       |
|           | rhs_c  | open\];\ |             | within a | R_COMPRD) |
|           | omprd, | default  |             | region   | to be     |
|           | rcs_   | value:   |             | for a    | included  |
|           | comprd | none     |             | pa       | in the    |
|           |        |          |             | rticular | equality  |
|           |        | Default  |             | ti       | balance   |
|           |        | i/e: STD |             | meslice. | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQE      |
|           |        |          |             |          | _COMBAL). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to said   |
|           |        |          |             |          | variable  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | cost      |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | bo     | C        | The years   | Bound on | Forces    |
| OM_CUMNET | hyear, | ommodity | y1 and y2   | the      | the net   |
|           | eo     | unit     | may be any  | cu       | commodity |
| (r,       | hyear, |          | years of    | mulative | variable  |
| y1,y2,bd) | rhs_c  | \[0,∞);\ | the set     | net      | (VA       |
|           | ombal, | default  | allyear;    | amount   | R_COMNET) |
|           | rcs_c  | value:   | where y1    | of a     | to be     |
|           | ombal, | none     | may also be | c        | included  |
|           | rtc_   |          | 'BOH' for   | ommodity | in the    |
|           | cumnet | Default  | first year  | between  | equality  |
|           |        | i/e: not | of first    | the      | balance   |
|           |        | possible | period and  | years y1 | c         |
|           |        |          | y2 may be   | and y2,  | onstraint |
|           |        |          | 'EOH' for   | within a | (EQE      |
|           |        |          | last year   | region   | _COMBAL). |
|           |        |          | of last     | over     |           |
|           |        |          | period.     | tim      | Generates |
|           |        |          |             | eslices. | the       |
|           |        |          |             |          | c         |
|           |        |          |             |          | umulative |
|           |        |          |             |          | commodity |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQ(l)\   |
|           |        |          |             |          | _CUMNET). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | bo     | C        | The years   | Bound on | Forces    |
| OM_CUMPRD | hyear, | ommodity | y1 and y2   | the      | the net   |
|           | eo     | unit     | may be any  | cu       | commodity |
| (r,       | hyear, |          | years of    | mulative | variable  |
| y1,y2,bd) | rhs_c  | \[0,∞);\ | the set     | pr       | (VA       |
|           | omprd, | default  | allyear;    | oduction | R_COMPRD) |
|           | rcs_c  | value:   | where y1    | of a     | to be     |
|           | omprd, | none     | may also be | c        | included  |
|           | rtc_   |          | 'BOH' for   | ommodity | in the    |
|           | cumprd | Default  | first year  | between  | balance   |
|           |        | i/e: not | of first    | the      | equation  |
|           |        | possible | period and  | years y1 | (EQE      |
|           |        |          | y2 may be   | and y2   | _COMBAL). |
|           |        |          | 'EOH' for   | within a |           |
|           |        |          | last year   | region   | The       |
|           |        |          | of last     | over     | c         |
|           |        |          | period.     | tim      | umulative |
|           |        |          |             | eslices. | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | is        |
|           |        |          |             |          | generated |
|           |        |          |             |          | (EQ(l)\   |
|           |        |          |             |          | _CUMPRD). |
+-----------+--------+----------+-------------+----------+-----------+
| COM_ELAST | COM_B  | Dimen    | The control | El       | Controls  |
|           | PRICE, | sionless | parameter   | asticity | the       |
| (r        | COM    |          |             | of       | inclusion |
| ,datayear | _STEP, | \[       | \$SET       | demand   | of the    |
| ,c,s,lim) | COM    | open\];\ | TIMESED YES | in       | elastic   |
|           | _VOC,\ | default  | must be set | dicating | demand    |
|           | C      | value:   | to activate | how much | variable  |
|           | OM_AGG | none     | elastic     | the      | (V        |
|           |        |          | demands.    | demand   | AR_ELAST) |
|           |        | Default  |             | ris      | in the    |
|           |        | i/e: STD | An          | es/falls | commodity |
|           |        |          | elasticity  | in       | balance   |
|           |        |          | is required | response | equat     |
|           |        |          | for each    | to a     | ion(EQ(l) |
|           |        |          | direction   | unit     | \_COMBAL) |
|           |        |          | the demand  | change   |           |
|           |        |          | is          | in the   | Applied   |
|           |        |          | permitted   | marginal | to the    |
|           |        |          | to move.    | cost of  | elastic   |
|           |        |          |             | meeting  | demand    |
|           |        |          | The index   | a demand | variable  |
|           |        |          | lim =       | that is  | (V        |
|           |        |          | \'LO\'      | elastic. | AR_ELAST) |
|           |        |          | corresponds |          | in the    |
|           |        |          | to demand   | See also | objective |
|           |        |          | decrease,   | Appendix | function  |
|           |        |          | while lim = | D for    | costs     |
|           |        |          | \'UP\'      | ad       | (EQ       |
|           |        |          | denotes the | ditional | _OBJELS). |
|           |        |          | direction   | details  |           |
|           |        |          | for demand  | on       |           |
|           |        |          | increase.   | defining |           |
|           |        |          |             | demand   |           |
|           |        |          | A different | fu       |           |
|           |        |          | value may   | nctions. |           |
|           |        |          | be provided |          |           |
|           |        |          | for each    |          |           |
|           |        |          | direction,  |          |           |
|           |        |          | thus curves |          |           |
|           |        |          | may be      |          |           |
|           |        |          | asymmetric. |          |           |
|           |        |          |             |          |           |
|           |        |          | S           |          |           |
|           |        |          | ubstitution |          |           |
|           |        |          | e           |          |           |
|           |        |          | lasticities |          |           |
|           |        |          | can be      |          |           |
|           |        |          | defined     |          |           |
|           |        |          | with        |          |           |
|           |        |          | lim=\'N\',  |          |           |
|           |        |          | among a     |          |           |
|           |        |          | group of    |          |           |
|           |        |          | demands     |          |           |
|           |        |          | aggregated  |          |           |
|           |        |          | by COM_AGG. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         | COM    | Integer  | Provided    | Shape    | Affects   |
| OM_ELASTX | _ELAST | scalar   | when        | index    | the       |
| (r,datay  |        |          | shaping of  | for the  | demand    |
| ear,c,bd) |        | \[       | elasticity  | el       | ela       |
|           |        | 1,999\]; | based upon  | asticity | sticities |
|           |        |          | demand      | of       | applied   |
|           |        | default  | level is    | demand   | in        |
|           |        | value:   | desired.    |          | EQ_OBJELS |
|           |        | none\    |             |          |           |
|           |        | Default  | Note: Shape |          |           |
|           |        | extrap   | index 1 is  |          |           |
|           |        | olation: | reserved    |          |           |
|           |        | MIG      | for         |          |           |
|           |        |          | constant 1. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| COM_FR    | COM    | Decimal  | Normally    | Fraction | Applied   |
|           | _PROJ, | fraction | defined     | of the   | to the    |
| (r,data   | c      |          | only for    | annual   | annual    |
| year,c,s) | om_ts, | \        | demand      | demand   | demand    |
|           | co     | [0,1\];\ | commodities | (C       | (         |
|           | m_tsl, | default  | (com_type = | OM_PROJ) | COM_PROJ) |
|           |        | value:   | \'DEM\'),   | or       | as the    |
|           | RTC    | t        | but can be  | c        | RHS of    |
|           | S_TSFR | imeslice | applied to  | ommodity | the       |
|           |        | duration | any         | flow     | balance   |
|           |        | (G_YRFR) | commodity   | o        | equation  |
|           |        |          | for         | ccurring | (EQ(l)\   |
|           |        | Default  | defining    | in       | _COMBAL). |
|           |        | i/e: STD | load        | t        |           |
|           |        |          | profiles.   | imeslice | Enters    |
|           |        |          |             | s;       | the       |
|           |        |          | Affects     | d        | peaking   |
|           |        |          | timeslice   | escribes | equation  |
|           |        |          | resolution  | the      | (         |
|           |        |          | at which a  | shape of | EQ_PEAK), |
|           |        |          | commodity   | the load | if a      |
|           |        |          | is tracked  | curve.   | peaking   |
|           |        |          | (           |          | c         |
|           |        |          | RTCS_TSFR), |          | ommodity. |
|           |        |          | and thereby |          |           |
|           |        |          | may affect  |          | Applied   |
|           |        |          | when a      |          | to the    |
|           |        |          | process     |          | bounds of |
|           |        |          | cannot      |          | elastic   |
|           |        |          | operate     |          | demand    |
|           |        |          | (rtps_off). |          | step      |
|           |        |          |             |          | variables |
|           |        |          | Weighted    |          | (VA       |
|           |        |          | i           |          | R_ELAST). |
|           |        |          | nheritance. |          |           |
|           |        |          |             |          | Applied   |
|           |        |          | Weighted    |          | via       |
|           |        |          | a           |          | RTFCS_FR  |
|           |        |          | ggregation. |          | in all    |
|           |        |          |             |          | equations |
|           |        |          |             |          | to flows  |
|           |        |          |             |          | having a  |
|           |        |          |             |          | timeslice |
|           |        |          |             |          | level     |
|           |        |          |             |          | coarser   |
|           |        |          |             |          | than      |
|           |        |          |             |          | target    |
|           |        |          |             |          | level.    |
+-----------+--------+----------+-------------+----------+-----------+
| COM_IE    |        | Decimal  | Direct      | Infras   | Overall   |
|           |        | fraction | i           | tructure | e         |
| (r,data   |        |          | nheritance. | or       | fficiency |
| year,c,s) |        | (0,∞);\  |             | tran     | applied   |
|           |        | default  | Weighted    | smission | to the    |
|           |        | value: 1 | a           | ef       | total     |
|           |        |          | ggregation. | ficiency | p         |
|           |        | Default  |             | of a     | roduction |
|           |        | i/e: STD |             | co       | of a      |
|           |        |          |             | mmodity. | commodity |
|           |        |          |             |          | in the    |
|           |        |          |             |          | commodity |
|           |        |          |             |          | balance   |
|           |        |          |             |          | equation  |
|           |        |          |             |          | (EQ(l)\   |
|           |        |          |             |          | _COMBAL). |
+-----------+--------+----------+-------------+----------+-----------+
| COM_PKFLX | com    | Scalar   | Direct      | Di       | Applied   |
|           | _peak, |          | i           | fference | to the    |
| (r,data   | com    | \[       | nheritance. | between  | total     |
| year,c,s) | _pkts, | open\];\ |             | the      | co        |
|           | COM_   | default  | Weighted    | average  | nsumption |
|           | PKRSV, | value:   | a           | demand   | of a      |
|           | FLO    | none     | ggregation. | and the  | commodity |
|           | _PKCOI |          |             | peak     | to raise  |
|           |        | Default  |             | demand   | the       |
|           |        | i/e: STD |             | in       | capacity  |
|           |        |          |             | t        | needed to |
|           |        |          |             | imeslice | satisfy   |
|           |        |          |             | s,       | the       |
|           |        |          |             | e        | peaking   |
|           |        |          |             | xpressed | c         |
|           |        |          |             | as       | onstraint |
|           |        |          |             | fraction | (         |
|           |        |          |             | of the   | EQ_PEAK). |
|           |        |          |             | average  |           |
|           |        |          |             | demand.  |           |
+-----------+--------+----------+-------------+----------+-----------+
| COM_PKRSV | com    | Scalar   | Requires    | Peak     | Applied   |
|           | _peak, |          | that        | reserve  | to the    |
| (r,da     | com    | \[0,∞);\ | commodity c | margin   | total     |
| tayear,c) | _pkts, | default  | is also     | as       | co        |
|           | COM_   | value:   | requested   | fraction | nsumption |
|           | PKFLX, | none     | to have     | of peak  | of a      |
|           | FLO    |          | peaking     | demand,  | commodity |
|           | _PKCOI | Default  | c           | e.g. if  | to raise  |
|           |        | i/e: STD | onstraints, | C        | the       |
|           |        |          | by defining | OM_PKRSV | capacity  |
|           |        |          | COM_PEAK or | = 0.2,   | needed to |
|           |        |          | COM_PKTS    | the      | satisfy   |
|           |        |          |             | total    | the       |
|           |        |          |             | i        | peaking   |
|           |        |          |             | nstalled | c         |
|           |        |          |             | capacity | onstraint |
|           |        |          |             | must     | (         |
|           |        |          |             | exceed   | EQ_PEAK). |
|           |        |          |             | the peak |           |
|           |        |          |             | load by  |           |
|           |        |          |             | 20%.     |           |
+-----------+--------+----------+-------------+----------+-----------+
| COM_PROJ  | COM_FR | C        | In standard | P        | Serves as |
|           |        | ommodity | usage, only | rojected | the RHS   |
| (r,da     |        | unit     | applicable  | annual   | (after    |
| tayear,c) |        |          | to demand   | demand   | COM_FR    |
|           |        | \[0,∞);\ | commodities | for a    | applied)  |
|           |        | default  | (com_type = | co       | of the    |
|           |        | value:   | 'DEM').\    | mmodity. | commodity |
|           |        | none     | In advanced |          | balance   |
|           |        |          | usage, may  |          | c         |
|           |        | Default  | also be     |          | onstraint |
|           |        | i/e: STD | specified   |          | (EQ(l)\   |
|           |        |          | for other   |          | _COMBAL). |
|           |        |          | commodities |          |           |
|           |        |          | for         |          | Enters    |
|           |        |          | defining an |          | the       |
|           |        |          | exogenous   |          | peaking   |
|           |        |          | demand.\    |          | equation  |
|           |        |          | Demand is   |          | (         |
|           |        |          | allocated   |          | EQ_PEAK), |
|           |        |          | to          |          | if a      |
|           |        |          | sub-annual  |          | peaking   |
|           |        |          | timeslices  |          | c         |
|           |        |          | according   |          | ommodity. |
|           |        |          | to COM_FR.  |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | when      |
|           |        |          |             |          | setting   |
|           |        |          |             |          | the upper |
|           |        |          |             |          | bound of  |
|           |        |          |             |          | an        |
|           |        |          |             |          | elastic   |
|           |        |          |             |          | demand    |
|           |        |          |             |          | step      |
|           |        |          |             |          | (VA       |
|           |        |          |             |          | R_ELAST). |
+-----------+--------+----------+-------------+----------+-----------+
| COM_STEP  | COM_B  | Integer  | The control | Number   | Controls  |
|           | PRICE, | number   | parameter   | of steps | the       |
| (r,c,bd)  | COM_   |          | \$SET       | to use   | instance  |
|           | ELAST, | \[1,∞);\ | TIMESED     | for the  | of the    |
|           | CO     | default  | 'YES' must  | appro    | elastic   |
|           | M_VOC, | value:   | be set to   | ximation | demand    |
|           |        | none     | activate    | of       | variable  |
|           | rcj    |          | elastic     | change   | (V        |
|           |        |          | demands.    | of       | AR_ELAST) |
|           |        |          | The number  | p        | in:       |
|           |        |          | of steps is | roducer/ |           |
|           |        |          | required    | consumer | the       |
|           |        |          | for each    | surplus  | commodity |
|           |        |          | direction   | when     | balance   |
|           |        |          | the demand  | using    | equation  |
|           |        |          | is          | the      | (EQ(l)\   |
|           |        |          | permitted   | li       | _COMBAL); |
|           |        |          | to move.    | nearized |           |
|           |        |          |             | elastic  | setting   |
|           |        |          | The index   | demand   | of the    |
|           |        |          | bd=LO       | formu    | step      |
|           |        |          | denotes the | lations. | limit for |
|           |        |          | direction   |          | the       |
|           |        |          | of demand   |          | elastic   |
|           |        |          | decrease,   |          | demand    |
|           |        |          | bd=UP       |          | variable  |
|           |        |          | increase,   |          | (VA       |
|           |        |          | and bd=FX   |          | R_ELAST); |
|           |        |          | is a        |          |           |
|           |        |          | shortcut    |          | enters    |
|           |        |          | for both. A |          | the       |
|           |        |          | different   |          | objective |
|           |        |          | value may   |          | function  |
|           |        |          | be provided |          | costs     |
|           |        |          | for each    |          | (EQ       |
|           |        |          | direction,  |          | _OBJELS). |
|           |        |          | thus curves |          |           |
|           |        |          | may be      |          |           |
|           |        |          | asymmetric. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| C         | OBJ_   | Monetary | Direct      | Subsidy  | Forces    |
| OM_SUBNET | COMNT, | unit per | i           | on the   | the net   |
|           | CST    | c        | nheritance. | net      | commodity |
| (r        | _COMX, | ommodity |             | amount   | variable  |
| ,datayear |        | unit     | Weighted    | of a     | (VA       |
| ,c,s,cur) | CS     |          | a           | c        | R_COMNET) |
|           | T_PVC, | \[0,∞);\ | ggregation. | ommodity | to be     |
|           | rhs_c  | default  |             | within a | included  |
|           | ombal, | value:   |             | region   | in the    |
|           | rcs_   | none     |             | for a    | equality  |
|           | combal |          |             | pa       | balance   |
|           |        | Default  |             | rticular | c         |
|           |        | i/e: STD |             | ti       | onstraint |
|           |        |          |             | meslice. | (EQE      |
|           |        |          |             |          | _COMBAL). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | (-) to    |
|           |        |          |             |          | said      |
|           |        |          |             |          | variable  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | cost      |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | OBJ_   | Monetary | Direct      | Subsidy  | Forces    |
| OM_SUBPRD | COMPD, | unit per | i           | on the   | the       |
|           | CST    | c        | nheritance. | pr       | commodity |
| (r        | _COMX, | ommodity |             | oduction | p         |
| ,datayear |        | unit     | Weighted    | of a     | roduction |
| ,c,s,cur) | CS     |          | a           | c        | variable  |
|           | T_PVC, | \[0,∞);\ | ggregation. | ommodity | (VA       |
|           | rhs_c  | default  |             | within a | R_COMPRD) |
|           | omprd, | value:   |             | region   | to be     |
|           | rcs_   | none     |             | for a    | included  |
|           | comprd |          |             | pa       | in the    |
|           |        | Default  |             | rticular | equality  |
|           |        | i/e: STD |             | ti       | balance   |
|           |        |          |             | meslice. | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQE      |
|           |        |          |             |          | _COMBAL). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | (-) to    |
|           |        |          |             |          | said      |
|           |        |          |             |          | variable  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | cost      |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | OBJ_   | Monetary | Direct      | Tax on   | Forces    |
| OM_TAXNET | COMNT, | unit per | i           | the net  | the net   |
|           | CST    | c        | nheritance. | amount   | commodity |
| (r        | _COMX, | ommodity |             | of a     | variable  |
| ,datayear |        | unit     | Weighted    | c        | (VA       |
| ,c,s,cur) | CS     |          | a           | ommodity | R_COMNET) |
|           | T_PVC, | \[0,∞);\ | ggregation. | within a | to be     |
|           | rhs_c  | default  |             | region   | included  |
|           | ombal, | value:   |             | for a    | in the    |
|           | rcs_   | none     |             | pa       | equality  |
|           | combal |          |             | rticular | balance   |
|           |        | Default  |             | ti       | c         |
|           |        | i/e: STD |             | meslice. | onstraint |
|           |        |          |             |          | (EQE      |
|           |        |          |             |          | _COMBAL). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to said   |
|           |        |          |             |          | variable  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | cost      |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| C         | OBJ_   | Monetary | Direct      | Tax on   | Forces    |
| OM_TAXPRD | COMPD, | unit per | i           | the      | the       |
|           | CST    | c        | nheritance. | pr       | commodity |
| (r        | _COMX, | ommodity |             | oduction | p         |
| ,datayear |        | unit     | Weighted    | of a     | roduction |
| ,c,s,cur) | CS     |          | a           | c        | variable  |
|           | T_PVC, | \[0,∞);\ | ggregation. | ommodity | (VA       |
|           | rhs_c  | default  |             | within a | R_COMPRD) |
|           | omprd, | value:   |             | region   | to be     |
|           | rcs_   | none     |             | for a    | included  |
|           | comprd |          |             | pa       | in the    |
|           |        | Default  |             | rticular | equality  |
|           |        | i/e: STD |             | ti       | balance   |
|           |        |          |             | meslice. | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQE      |
|           |        |          |             |          | _COMBAL). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to said   |
|           |        |          |             |          | variable  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | cost      |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| COM_VOC   | COM_B  | Dimen    | The control | Possible | Applied   |
|           | PRICE, | sionless | parameter   | v        | when      |
| (r,datay  | COM    |          | \$SET       | ariation | setting   |
| ear,c,bd) | _STEP, | \[0,∞);\ | TIMESED     | of       | the bound |
|           | COM    | default: | 'YES' to    | demand   | of an     |
|           | _ELAST | none     | activate    | in both  | elastic   |
|           |        |          | elastic     | di       | demand    |
|           |        | Default  | demands     | rections | step      |
|           |        | i/e: STD | must be     | when     | (VA       |
|           |        |          | set.        | using    | R_ELAST). |
|           |        |          |             | the      |           |
|           |        |          | A number is | elastic  | Applied   |
|           |        |          | required    | demand   | to the    |
|           |        |          | for each    | form     | e         |
|           |        |          | direction   | ulation. | lasticity |
|           |        |          | the demand  |          | variable  |
|           |        |          | is          |          | in the    |
|           |        |          | permitted   |          | objective |
|           |        |          | to move.    |          | function  |
|           |        |          |             |          | costs     |
|           |        |          | The index   |          | (EQ       |
|           |        |          | bd = LO     |          | _OBJELS). |
|           |        |          | corresponds |          |           |
|           |        |          | to the      |          |           |
|           |        |          | direction   |          |           |
|           |        |          | of          |          |           |
|           |        |          | decreasing  |          |           |
|           |        |          | the demand, |          |           |
|           |        |          | while bd =  |          |           |
|           |        |          | UP denotes  |          |           |
|           |        |          | the         |          |           |
|           |        |          | direction   |          |           |
|           |        |          | for demand  |          |           |
|           |        |          | increase.   |          |           |
|           |        |          |             |          |           |
|           |        |          | A different |          |           |
|           |        |          | value may   |          |           |
|           |        |          | be provided |          |           |
|           |        |          | for each    |          |           |
|           |        |          | direction,  |          |           |
|           |        |          | thus curves |          |           |
|           |        |          | may be      |          |           |
|           |        |          | asymmetric. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| DAM_BQTY\ | DA     | C        | Only        | Base     | EQ_DAMAGE |
| (r,c)     | M_COST | ommodity | effective   | quantity |           |
|           |        | unit     | when        | of       | EQ_OBJDAM |
|           |        |          | DAM_COST    | e        |           |
|           |        | \[0,∞);  | has been    | missions |           |
|           |        |          | defined for | for      |           |
|           |        | default  | commodity   | damage   |           |
|           |        | value:   | c.          | cost     |           |
|           |        | none     |             | ac       |           |
|           |        |          |             | counting |           |
|           |        | Default  |             |          |           |
|           |        | i/e: N/A |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| DAM_COST  | DA     | Monetary | Damage      | Marginal | EQ_DAMAGE |
| (r,dataye | M_BQTY | unit per | costs are   | damage   |           |
| ar,c,cur) |        | c        | by default  | cost of  | EQ_OBJDAM |
|           |        | ommodity | endogenous  | e        |           |
|           |        | unit     | (included   | missions |           |
|           |        |          | in the      | at Base  |           |
|           |        | \[0,∞);  | objective). | q        |           |
|           |        |          |             | uantity. |           |
|           |        | default  | To set them |          |           |
|           |        | value:   | exogenous,  |          |           |
|           |        | none     | use \$SET   |          |           |
|           |        |          | DAMAGE NO   |          |           |
|           |        | Default  |             |          |           |
|           |        | i/e: STD |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| D         | DA     | Dimen    | Only        | El       | EQ_OBJDAM |
| AM_ELAST\ | M_COST | sionless | effective   | asticity |           |
| (r,c,lim) |        |          | when        | of       |           |
|           | DA     | \[0,∞);\ | DAM_COST    | damage   |           |
|           | M_BQTY | default  | has been    | cost in  |           |
|           |        | value:   | defined for | the      |           |
|           |        | none     | commodity   | lower or |           |
|           |        |          | c.          | upper    |           |
|           |        | Default  |             | d        |           |
|           |        | i/e: N/A |             | irection |           |
|           |        |          |             | from     |           |
|           |        |          |             | Base     |           |
|           |        |          |             | q        |           |
|           |        |          |             | uantity. |           |
+-----------+--------+----------+-------------+----------+-----------+
| DAM_STEP\ | DA     | Integer  | Only        | Number   | EQ_DAMAGE |
| (r,c,lim) | M_COST | number   | effective   | of steps |           |
|           |        |          | when        | for      | EQ_OBJDAM |
|           | DA     | \[1,∞);\ | DAM_COST    | lin      |           |
|           | M_BQTY | default  | has been    | earizing |           |
|           |        | value:   | defined for | damage   |           |
|           |        | none     | commodity   | costs in |           |
|           |        |          | c.          | the      |           |
|           |        | Default  |             | lower or |           |
|           |        | i/e: N/A |             | upper    |           |
|           |        |          |             | d        |           |
|           |        |          |             | irection |           |
|           |        |          |             | from     |           |
|           |        |          |             | Base     |           |
|           |        |          |             | q        |           |
|           |        |          |             | uantity. |           |
+-----------+--------+----------+-------------+----------+-----------+
| DAM_VOC\  | DA     | Decimal  | Only        | Variance | EQ_OBJDAM |
| (r,c,lim) | M_COST | fraction | effective   | of       |           |
|           |        |          | when        | e        |           |
|           | DA     | LO:      | DAM_COST    | missions |           |
|           | M_BQTY | \[0,1\]; | has been    | in the   |           |
|           |        | UP:      | defined for | lower or |           |
|           |        | \[0,∞);\ | commodity   | upper    |           |
|           |        | default  | c.          | d        |           |
|           |        | value:   |             | irection |           |
|           |        | none     |             | from     |           |
|           |        |          |             | Base     |           |
|           |        | Default  |             | quantity |           |
|           |        | i/e: N/A |             | as a     |           |
|           |        |          |             | fraction |           |
|           |        |          |             | of Base  |           |
|           |        |          |             | q        |           |
|           |        |          |             | uantity. |           |
+-----------+--------+----------+-------------+----------+-----------+
| E         | B, D,  |          | For each    | End year | The       |
|           | M,     |          | modelyear   | of       | amount of |
| \(t\)     | COE    |          | period      | period   | new       |
|           | F_CPT, |          |             | t, used  | i         |
|           |        |          |             | in       | nvestment |
|           | rtp_   |          |             | det      | (         |
|           | vintyr |          |             | ermining | VAR_NCAP) |
|           |        |          |             | the      | carried   |
|           |        |          |             | length   | over in   |
|           |        |          |             | of each  | the       |
|           |        |          |             | period   | capacity  |
|           |        |          |             |          | transfer  |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQ(      |
|           |        |          |             |          | l)\_CPT). |
|           |        |          |             |          |           |
|           |        |          |             |          | Amount of |
|           |        |          |             |          | in        |
|           |        |          |             |          | vestments |
|           |        |          |             |          | (         |
|           |        |          |             |          | VAR_NCAP) |
|           |        |          |             |          | remaining |
|           |        |          |             |          | past the  |
|           |        |          |             |          | modelling |
|           |        |          |             |          | horizon   |
|           |        |          |             |          | that      |
|           |        |          |             |          | needs to  |
|           |        |          |             |          | be        |
|           |        |          |             |          | credited  |
|           |        |          |             |          | back to   |
|           |        |          |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJINV). |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_BND   |        | C        | If the      | Bound on | Flow      |
|           |        | ommodity | bound is    | the flow | activity  |
| (r,d      |        | unit     | specified   | of a     | limit     |
| atayear,p |        |          | for a       | c        | c         |
| ,cg,s,bd) |        | \[0,∞);\ | timeslice s | ommodity | onstraint |
|           |        | default: | being above | or the   | (EQ(l)    |
|           |        | none     | the flow    | sum of   | \_FLOBND) |
|           |        |          | timeslice   | flows    | when s is |
|           |        | Default  | resolution  | within a | above     |
|           |        | i/e: MIG | (r          | c        | r         |
|           |        |          | tpcs_varf), | ommodity | tpcs_varf |
|           |        |          | the bound   | group.   |           |
|           |        |          | is applied  |          | Direct    |
|           |        |          | to the sum  |          | bound on  |
|           |        |          | of the flow |          | activity  |
|           |        |          | variables   |          | variable  |
|           |        |          | (VAR_FLO)   |          | (VAR_FLO) |
|           |        |          | according   |          | when at   |
|           |        |          | to the      |          | the       |
|           |        |          | timeslice   |          | r         |
|           |        |          | tree,       |          | tpcs_varf |
|           |        |          | otherwise   |          | level.    |
|           |        |          | directly to |          |           |
|           |        |          | the flow    |          |           |
|           |        |          | variable.   |          |           |
|           |        |          |             |          |           |
|           |        |          | No          |          |           |
|           |        |          | aggreg      |          |           |
|           |        |          | ation.[^29] |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_COST  | OBJ_   | Monetary | Direct      | Variable | Applied   |
|           | FCOST, | unit per | inheritance | cost of  | to the    |
| (r,d      | CST    | c        |             | a        | flow      |
| atayear,p | _FLOC, | ommodity | Weighted    | process  | variable  |
| ,c,s,cur) |        | unit     | aggregation | as       | (VAR_FLO) |
|           | C      |          |             | sociated | when      |
|           | ST_PVP | \[       |             | with the | entering  |
|           |        | open\];\ |             | pro      | the       |
|           |        | default: |             | duction/ | objective |
|           |        | none     |             | con      | function  |
|           |        |          |             | sumption | (EQ       |
|           |        | Default  |             | of a     | _OBJVAR). |
|           |        | i/e: STD |             | co       |           |
|           |        |          |             | mmodity. | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_CUM   | A      | Flow     | The years   | Bound on | Generates |
| (r,p,c,   | CT_CUM | unit     | y1 and y2   | the      | an        |
| y1,y2,bd) |        |          | may be any  | cu       | instance  |
|           |        | \[0,∞);\ | years of    | mulative | of the    |
|           |        | default  | the set     | amount   | c         |
|           |        | value:   | allyear;    | of       | umulative |
|           |        | none     | where y1    | annual   | c         |
|           |        |          | may also be | process  | onstraint |
|           |        | Default  | \'BOH\' for | activity |           |
|           |        | i/e: N/A | first year  | between  | (E        |
|           |        |          | of first    | the      | Q_CUMFLO) |
|           |        |          | period and  | years y1 |           |
|           |        |          | y2 may be   | and y2,  |           |
|           |        |          | \'EOH\' for | within a |           |
|           |        |          | last year   | region.  |           |
|           |        |          | of last     |          |           |
|           |        |          | period.     |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_DELIV | OBJ_   | Monetary | Direct      | Cost of  | Applied   |
|           | FDELV, | unit per | i           | a        | to the    |
| (r,d      | CST    | c        | nheritance. | de       | flow      |
| atayear,p | _FLOC, | ommodity |             | livering | variable  |
| ,c,s,cur) |        | unit     | Weighted    | (co      | (VAR_FLO) |
|           | C      |          | a           | nsuming) | when      |
|           | ST_PVP | \[       | ggregation. | a        | entering  |
|           |        | open\];\ |             | c        | the       |
|           |        | default: |             | ommodity | objective |
|           |        | none     |             | to a     | function  |
|           |        |          |             | process. | (EQ       |
|           |        | Default  |             |          | _OBJVAR). |
|           |        | i/e: STD |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_EFF   | FLO    | C        | Inherited   | Defines  | Generates |
| (r,       | _EMIS\ | ommodity | /aggregated | the      | process   |
| datayear, | PRC_   | unit of  | to the      | amount   | trans     |
| p,cg,c,s) | ACTFLO | c /      | timeslice   | of       | formation |
|           |        | c        | levels of   | c        | equation  |
|           |        | ommodity | the flow    | ommodity | (E        |
|           |        | unit of  | variables   | flow of  | Q_PTRANS) |
|           |        | cg       | of the      | c        | between   |
|           |        |          | commodities | ommodity | one or    |
|           |        | \[       | in group    | (c) per  | more      |
|           |        | open\];\ | cg. All     | unit of  | input (or |
|           |        | default  | parameters  | other    | output)   |
|           |        | value:   | with the    | process  | co        |
|           |        | none     | same        | flow(s)  | mmodities |
|           |        |          | process (p) | or       | and one   |
|           |        | Default  | and target  | activity | output    |
|           |        | i/e: STD | commodity   | (cg).    | (or       |
|           |        |          | (c) are     |          | input)    |
|           |        |          | combined in |          | com       |
|           |        |          | the same    |          | modities. |
|           |        |          | tra         |          |           |
|           |        |          | nsformation |          |           |
|           |        |          | equation.   |          |           |
|           |        |          |             |          |           |
|           |        |          | By using    |          |           |
|           |        |          | cg=\'ACT\', |          |           |
|           |        |          | the         |          |           |
|           |        |          | attribute   |          |           |
|           |        |          | will be     |          |           |
|           |        |          | defined per |          |           |
|           |        |          | unit of     |          |           |
|           |        |          | activity,   |          |           |
|           |        |          | by applying |          |           |
|           |        |          | it on all   |          |           |
|           |        |          | PCG flows   |          |           |
|           |        |          | with the    |          |           |
|           |        |          | value       |          |           |
|           |        |          | divided by  |          |           |
|           |        |          | any         |          |           |
|           |        |          | u           |          |           |
|           |        |          | ser-defined |          |           |
|           |        |          | PRC_ACTFLO. |          |           |
|           |        |          |             |          |           |
|           |        |          | FLO_EFF     |          |           |
|           |        |          | defined for |          |           |
|           |        |          | an          |          |           |
|           |        |          | individual  |          |           |
|           |        |          | flow will   |          |           |
|           |        |          | override    |          |           |
|           |        |          | any value   |          |           |
|           |        |          | for a       |          |           |
|           |        |          | group.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_EMIS  | F      | C        | See         | Defines  | See       |
| (r,da     | LO_EFF | ommodity | FLO_EFF.    | the      | FLO_EFF.  |
| tayear,p, | (      | unit of  |             | amount   |           |
| cg,com,s) | alias) | c /      | If com is   | of       |           |
|           |        | c        | of type ENV | e        |           |
|           |        | ommodity | and is not  | missions |           |
|           |        | unit of  | in the      | (c) per  |           |
|           |        | cg       | process     | unit of  |           |
|           |        |          | topology,   | process  |           |
|           |        | \[       | it is added | flow(s)  |           |
|           |        | open\];\ | to it as an | or       |           |
|           |        | default  | output      | activity |           |
|           |        | value:   | flow.       | (cg).    |           |
|           |        | none     |             |          |           |
|           |        |          |             |          |           |
|           |        | Default  |             |          |           |
|           |        | i/e: STD |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_FR    |        | Decimal  | FLO_FR may  | 1\)      | A share   |
|           |        | fraction | be          | Bounds   | equation  |
| (r,       |        |          | specified   | the flow | (EQ(l     |
| datayear, |        | \[0,1\]  | as lower,   | of       | )\_FLOFR) |
| p,c,s,bd) |        | /        | upper or    | c        | limiting  |
|           |        | \[0,∞);\ | fixed       | ommodity | the       |
|           |        | default  | bounds, in  | (c)      | amount of |
|           |        | value:   | contrast to | entering | commodity |
|           |        | none     | COM_FR.     | or       | (c) is    |
|           |        |          |             | leaving  | generated |
|           |        | Default  | Can be      | process  | according |
|           |        | i/e: MIG | specified   | (p) in a | to the    |
|           |        |          | for any     | ti       | bound     |
|           |        |          | flow        | meslice, | type (bd  |
|           |        |          | variable    | in       | = l       |
|           |        |          | having a    | pr       | in        |
|           |        |          | subannual   | o­por­tion | dicator). |
|           |        |          | timeslice   | to       |           |
|           |        |          | resolution. | annual   |           |
|           |        |          |             | flow.    |           |
|           |        |          | Weighted    |          |           |
|           |        |          | a           | 2\) If   |           |
|           |        |          | ggregation. | s        |           |
|           |        |          |             | pecified |           |
|           |        |          | Direct      | also at  |           |
|           |        |          | i           | the      |           |
|           |        |          | nheritance, | ANNUAL   |           |
|           |        |          | if defined  | level,   |           |
|           |        |          | at the      | bounds   |           |
|           |        |          | ANNUAL      | the flow |           |
|           |        |          | level.      | *        |           |
|           |        |          |             | *level** |           |
|           |        |          |             | in       |           |
|           |        |          |             | pr       |           |
|           |        |          |             | oportion |           |
|           |        |          |             | to the   |           |
|           |        |          |             | average  |           |
|           |        |          |             | level    |           |
|           |        |          |             | under    |           |
|           |        |          |             | the      |           |
|           |        |          |             | parent   |           |
|           |        |          |             | t        |           |
|           |        |          |             | imeslice |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_FUNC  | FL     | C        | If for the  | A key    | Es        |
|           | O_SUM, | ommodity | same        | p        | tablishes |
| (r,dat    | FLO_   | unit of  | indexes the | arameter | the basic |
| ayear,p,c | FUNCX, | cg2/c    | parameter   | de       | trans     |
| g1,cg2,s) | COEF_  | ommodity | FLO_SUM is  | scribing | formation |
|           | PTRAN, | unit of  | specified   | the      | rel       |
|           | rpc_   | cg1      | but no      | basic    | ationship |
|           | ffunc, |          | FLO_FUNC,   | o        | (E        |
|           | rpcg   | \[       | the         | peration | Q_PTRANS) |
|           | _ptran | open\];\ | FLO_FUNC is | of or    | between   |
|           |        | default  | set to 1.   | within a | one or    |
|           |        | value:   |             | process. | more      |
|           |        | see next | Important   | Sets the | input (or |
|           |        | column   | factor in   | ratio    | output)   |
|           |        |          | determining | between  | co        |
|           |        | Default  | the level   | the sum  | mmodities |
|           |        | i/e: STD | at which a  | of flows | and one   |
|           |        |          | process     | in       | or more   |
|           |        |          | operates in | c        | output    |
|           |        |          | that the    | ommodity | (or       |
|           |        |          | derived     | group    | input)    |
|           |        |          | tra         | cg2 to   | com       |
|           |        |          | nsformation | the sum  | modities. |
|           |        |          | parameter   | of flows |           |
|           |        |          | (           | in       | Es        |
|           |        |          | COEF_PTRAN) | c        | tablishes |
|           |        |          | is          | ommodity | the       |
|           |        |          | inherited   | group    | rel       |
|           |        |          | /aggregated | cg1,     | ationship |
|           |        |          | to the      | thereby  | between   |
|           |        |          | timeslice   | defining | storage   |
|           |        |          | levels of   | the      | charging  |
|           |        |          | the flow    | ef       | /         |
|           |        |          | variables   | ficiency | di        |
|           |        |          | associated  | of       | scharging |
|           |        |          | with the    | p        | and a     |
|           |        |          | commodities | roducing | related   |
|           |        |          | in the      | cg2 from | commodity |
|           |        |          | group cg1.  | cg1      | flow      |
|           |        |          |             | (subject | (VAR_FLO) |
|           |        |          |             | to any   | in the    |
|           |        |          |             | F        | auxiliary |
|           |        |          |             | LO_SUM). | storage   |
|           |        |          |             | cg1 and  | flow      |
|           |        |          |             | cg2 may  | equation  |
|           |        |          |             | be also  | (EQ       |
|           |        |          |             | single   | _STGAUX). |
|           |        |          |             | comm     |           |
|           |        |          |             | odities. |           |
+-----------+--------+----------+-------------+----------+-----------+
| F         | FLO    | Integer  | Provided    | A        | Applied   |
| LO_FUNCX\ | _FUNC, | scalar   | when        | ge-based | to the    |
| (r,d      | FL     |          | shaping     | shaping  | flow      |
| atayear,p | O_SUM, | \[       | based upon  | curve    | variable  |
| ,cg1,cg2) | COEF   | 1,999\]; | age is      | (SHAPE)  | (VAR_FLO) |
|           | _PTRAN |          | desired.    | to be    | in a      |
|           |        | default  |             | applied  | trans     |
|           |        | value:   | Vintaged    | to the   | formation |
|           |        | none\    | processes   | flow     | equation  |
|           |        | Default  | only.       | pa       | (         |
|           |        | extrap   |             | rameters | EQ_PTRANS |
|           |        | olation: | Note: Shape | (        | /         |
|           |        | MIG      | index 1 is  | ACT_EFF/ | EQ        |
|           |        |          | reserved    | ACT_FLO/ | E_ACTEFF) |
|           |        |          | for         | FL       | to        |
|           |        |          | constant 1. | O_FUNC/F | account   |
|           |        |          |             | LO_SUM/F | for       |
|           |        |          | A           | LO_EMIS/ | changes   |
|           |        |          | CT_EFF(cg): | FLO_EFF) | in the    |
|           |        |          | cg1=cg,     |          | trans     |
|           |        |          | cg2=\'ACT\' |          | for­mation |
|           |        |          |             |          | e         |
|           |        |          | A           |          | fficiency |
|           |        |          | CT_FLO(cg): |          | according |
|           |        |          | c           |          | to the    |
|           |        |          | g1=\'ACT\', |          | age of    |
|           |        |          | cg2=cg      |          | each      |
|           |        |          |             |          | process   |
|           |        |          | FLO_        |          | vintage.  |
|           |        |          | EMIS(cg,c): |          |           |
|           |        |          | cg1=cg2=c   |          |           |
|           |        |          |             |          |           |
|           |        |          | FLO         |          |           |
|           |        |          | _EFF(cg,c): |          |           |
|           |        |          | cg1=cg2=c   |          |           |
|           |        |          |             |          |           |
|           |        |          | FLO_FUN     |          |           |
|           |        |          | C(cg1,cg2): |          |           |
|           |        |          | cgN=cgN     |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_MARK  | PR     | Decimal  | The same    | Proc     | The       |
|           | C_MARK | fraction | given       | ess-wise | i         |
| (         |        |          | fraction is | market   | ndividual |
| r,datayea |        | \        | applied to  | share in | process   |
| r,p,c,bd) |        | [0,1\];\ | all         | total    | flow      |
|           |        | default  | time­slices  | c        | variables |
|           |        | value:   | of the      | ommodity | (VAR_FLO, |
|           |        | none     | commodity   | pro      | VAR_IN,   |
|           |        |          | (this could | duction. | VAR_S     |
|           |        | Default  | be          |          | TGIN/OUT) |
|           |        | i/e: STD | generalized |          | are       |
|           |        |          | to allow    |          | co        |
|           |        |          | time-sli    |          | nstrained |
|           |        |          | ce-specific |          | (EQ(l)    |
|           |        |          | fractions,  |          | \_FLOMRK) |
|           |        |          | if deemed   |          | to a      |
|           |        |          | useful).    |          | fraction  |
|           |        |          |             |          | of the    |
|           |        |          | If an       |          | total     |
|           |        |          | ANNUAL      |          | p         |
|           |        |          | level       |          | roduction |
|           |        |          | m           |          | of a      |
|           |        |          | arket-share |          | commodity |
|           |        |          | is desired  |          | (VAR      |
|           |        |          | for a       |          | _COMPRD). |
|           |        |          | timesliced  |          |           |
|           |        |          | commodity,  |          | Forces    |
|           |        |          | PRC_MARK    |          | the       |
|           |        |          | can be used |          | commodity |
|           |        |          | instead.    |          | p         |
|           |        |          |             |          | roduction |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (VA       |
|           |        |          |             |          | R_COMPRD) |
|           |        |          |             |          | to be     |
|           |        |          |             |          | included  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | equality  |
|           |        |          |             |          | balance   |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQE      |
|           |        |          |             |          | _COMBAL). |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_PKCOI | COM_   | Scalar   | FLO_PKCOI   | Factor   | Applied   |
|           | PKRSV, |          | is          | that     | to the    |
| (r,dataye | COM_   | \[       | specified   | permits  | flow      |
| ar,p,c,s) | PKFLX, | open\];\ | for         | att      | variable  |
|           | com    | default  | individual  | ributing | (VAR_FLO) |
|           | _peak, | value: 1 | processes p | more (or | to adjust |
|           | co     |          | consuming   | less)    | the       |
|           | m_pkts | Default  | the peak    | demand   | amount of |
|           |        | i/e: STD | commodity   | to the   | a         |
|           |        |          | c.          | peaking  | commodity |
|           |        |          |             | equation | consumed  |
|           |        |          | Direct      | (        | when      |
|           |        |          | i           | EQ_PEAK) | co        |
|           |        |          | nheritance. | than the | nsidering |
|           |        |          |             | average  | the       |
|           |        |          | Weighted    | demand   | average   |
|           |        |          | ag          | ca       | demand    |
|           |        |          | gregation.\ | lculated | con       |
|           |        |          | \           | by the   | tributing |
|           |        |          | Used when   | model,   | to the    |
|           |        |          | the         | to       | peaking   |
|           |        |          | timeslices  | handle   | c         |
|           |        |          | are not     | the      | onstraint |
|           |        |          | necessarily | s        | (         |
|           |        |          | fine enough | ituation | EQ_PEAK). |
|           |        |          | to pick up  | where    |           |
|           |        |          | the actual  | peak     |           |
|           |        |          | peak within | usage is |           |
|           |        |          | the peak    | t        |           |
|           |        |          | timeslices. | ypically |           |
|           |        |          |             | higher   |           |
|           |        |          |             | (or      |           |
|           |        |          |             | lower)   |           |
|           |        |          |             | due to   |           |
|           |        |          |             | coin     |           |
|           |        |          |             | cidental |           |
|           |        |          |             | (or      |           |
|           |        |          |             | n        |           |
|           |        |          |             | on-coinc |           |
|           |        |          |             | idental) |           |
|           |        |          |             | loads at |           |
|           |        |          |             | the time |           |
|           |        |          |             | of the   |           |
|           |        |          |             | peak     |           |
|           |        |          |             | demand.  |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_SHAR  |        | Decimal  | Direct      | Share of | When the  |
|           |        | fraction | i           | flow     | commodity |
| (r,dat    |        |          | nheritance. | c        | is an     |
| ayear,p,c |        | \        |             | ommodity | input an  |
| ,cg,s,bd) |        | [0,1\];\ | Weighted    | c based  | EQ(       |
|           |        | default  | a           | upon the | l)\_INSHR |
|           |        | value:   | ggregation. | sum of   | equation  |
|           |        | none     |             | in       | is        |
|           |        |          | A common    | dividual | g         |
|           |        | Default  | example of  | flows    | enerated. |
|           |        | i/e: MIG | using       | defined  |           |
|           |        | over     | FLO_SHAR is | by the   | When the  |
|           |        | milesto  | to specify  | c        | commodity |
|           |        | neyears, | the         | ommodity | is an     |
|           |        | STD over | po          | group cg | output an |
|           |        | p        | wer-to-heat | b        | EQ(l      |
|           |        | astyears | ratio of    | elonging | )\_OUTSHR |
|           |        |          | CHP plants  | to       | equation  |
|           |        |          | in the      | process  | is        |
|           |        |          | b           | p.       | g         |
|           |        |          | ackpressure |          | enerated. |
|           |        |          | point. For  |          |           |
|           |        |          | example,    |          |           |
|           |        |          | for a heat  |          |           |
|           |        |          | output of a |          |           |
|           |        |          | CHP         |          |           |
|           |        |          | technology, |          |           |
|           |        |          | the         |          |           |
|           |        |          | FLO_SHAR    |          |           |
|           |        |          | parameter   |          |           |
|           |        |          | would have  |          |           |
|           |        |          | the value   |          |           |
|           |        |          | CHP         |          |           |
|           |        |          | R/(1+CHPR), |          |           |
|           |        |          | with CHPR   |          |           |
|           |        |          | being the   |          |           |
|           |        |          | he          |          |           |
|           |        |          | at-to-power |          |           |
|           |        |          | ratio.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_SUB   | OBJ    | Monetary | Direct      | Subsidy  | Applied   |
|           | _FSUB, | unit per | i           | on a     | with a    |
| (r,d      | CST    | c        | nheritance. | process  | minus     |
| atayear,p | _FLOX, | ommodity |             | flow.    | sign to   |
| ,c,s,cur) |        | unit     | Weighted    |          | the flow  |
|           | C      |          | a           |          | variable  |
|           | ST_PVP | \[0,∞);\ | ggregation. |          | (VAR_FLO) |
|           |        | default  |             |          | when      |
|           |        | value:   |             |          | entering  |
|           |        | none     |             |          | the       |
|           |        |          |             |          | objective |
|           |        | Default  |             |          | function  |
|           |        | i/e: STD |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
|           |        |          |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_SUM   | FLO    | C        | If a        | Mu       | The       |
|           | _FUNC\ | ommodity | FLO_SUM is  | ltiplier | FLO_SUM   |
| (r,datay  | FLO    | unit of  | specified   | applied  | m         |
| ear,p,cg1 | _FUNCX | cg2/c    | and no      | for      | ultiplier |
| ,c,cg2,s) |        | ommodity | co          | c        | is        |
|           | COEF_P | unit of  | rresponding | ommodity | applied   |
|           | TRANS, | c        | FLO_FUNC,   | c of     | along     |
|           | fs     |          | the         | group    | with      |
|           | _emis, | \[       | FLO_FUNC is | cg1      | FLO_FUNC  |
|           | rpc    | open\];\ | set to 1.   | corre    | parameter |
|           | _emis, | default  |             | sponding | in the    |
|           | rpc_   | value:   | If FLO_FUNC | to the   | trans     |
|           | ffunc, | see next | is          | flow     | formation |
|           | rpcg   | column   | specified   | rate     | co        |
|           | _ptran |          | for a true  | based    | efficient |
|           |        | Default  | commodity   | upon the | (COEF     |
|           |        | i/e: STD | group cg1,  | sum of   | _PTRANS), |
|           |        |          | and no      | in       | which is  |
|           |        |          | FLO_SUM is  | dividual | applied   |
|           |        |          | specified   | flows    | to the    |
|           |        |          | for the     | defined  | flow      |
|           |        |          | commodities | by the   | variable  |
|           |        |          | in cg1,     | c        | (VAR_FLO) |
|           |        |          | these       | ommodity | in the    |
|           |        |          | FLO_SUM are | group    | trans     |
|           |        |          | set to 1.   | cg2 of   | formation |
|           |        |          |             | process  | equation  |
|           |        |          | The derived | p. Most  | (EQ       |
|           |        |          | parameter   | often    | _PTRANS). |
|           |        |          | COEF_PTRANS | used to  |           |
|           |        |          | is          | define   |           |
|           |        |          | inherited   | the      |           |
|           |        |          | /aggregated | emission |           |
|           |        |          | to the      | rate, or |           |
|           |        |          | timeslice   | to       |           |
|           |        |          | level of    | adjust   |           |
|           |        |          | the flow    | the      |           |
|           |        |          | variable of | overall  |           |
|           |        |          | the         | ef       |           |
|           |        |          | commodity   | ficiency |           |
|           |        |          | c.          | of a     |           |
|           |        |          |             | te       |           |
|           |        |          |             | chnology |           |
|           |        |          |             | based    |           |
|           |        |          |             | upon     |           |
|           |        |          |             | fuel     |           |
|           |        |          |             | c        |           |
|           |        |          |             | onsumed. |           |
+-----------+--------+----------+-------------+----------+-----------+
| FLO_TAX   | OBJ    | Monetary | Direct      | Tax on a | Applied   |
|           | _FTAX, | unit per | i           | process  | to the    |
| (r,d      | CST    | c        | nheritance. | flow.    | flow      |
| atayear,p | _FLOX, | ommodity |             |          | variable  |
| ,c,s,cur) |        | unit     | Weighted    |          | (VAR_FLO) |
|           | C      |          | a           |          | when      |
|           | ST_PVP | \[0,∞);\ | ggregation. |          | entering  |
|           |        | default: |             |          | the       |
|           |        | none     |             |          | objective |
|           |        |          |             |          | function  |
|           |        | Default  |             |          | (EQ       |
|           |        | i/e: STD |             |          | _OBJVAR). |
|           |        |          |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| G_CUREX\  | R      | Scalar\  | The target  | Co       | Affects   |
| (c        | _CUREX | (0,∞)    | currency    | nversion | cost      |
| ur1,cur2) |        |          | cur2 must   | factor   | coe       |
|           |        | Default  | have a      | from     | fficients |
|           |        | value:   | discount    | currency | in EQ_OBJ |
|           |        | none     | rate        | cur1 to  |           |
|           |        |          | defined     | currency |           |
|           |        |          | with        | cur2,    |           |
|           |        |          | G_DRATE.    | with     |           |
|           |        |          |             | cur2 to  |           |
|           |        |          |             | be used  |           |
|           |        |          |             | in the   |           |
|           |        |          |             | o        |           |
|           |        |          |             | bjective |           |
|           |        |          |             | f        |           |
|           |        |          |             | unction. |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_CYCLE\  | TS     | Number   | Not         | Defines  | Affects   |
| (tslvl)   | _CYCLE | of       | recommended | the      | inter     |
|           |        | cycles\  | to be       | total    | ­pretation |
|           |        | \[1,∞);  | changed;    | number   | of        |
|           |        |          | use         | of       | ava       |
|           |        | Default  | TS_CYCLE    | cycles   | ilability |
|           |        | values:  | instead,    | on level | factors   |
|           |        |          | whenever    | tslvl,   | for the   |
|           |        | -   1    | the         | in a     | storage   |
|           |        |     for  | timeslice   | year.    | level,    |
|           |        |          | cycles are  |          | whenever  |
|           |        |   ANNUAL | different   | Provides | capacity  |
|           |        |          | from the    | default  | r         |
|           |        | -   1    | default,    | values   | epresents |
|           |        |     for  | because     | for      | the       |
|           |        |          | changing    | TS_CYCLE | maximum   |
|           |        |   SEASON | G_CYCLE     | (see     | nominal   |
|           |        |          | would       | entry    | output    |
|           |        | -   52   | change the  | for      | level     |
|           |        |     for  | meaning of  | that).   | (EQ(l)    |
|           |        |          | storage     |          | \_CAPACT, |
|           |        |   WEEKLY | a           |          | EQL       |
|           |        |          | vailability |          | _CAPFLO). |
|           |        | -   365  | factors.    |          |           |
|           |        |     for  |             |          |           |
|           |        |          |             |          |           |
|           |        |  DAYNITE |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_DRATE   | OBJ    | Decimal  | A value     | Sys      | The       |
|           | _DISC, | fraction | must be     | tem-wide | discount  |
| (r,all    | OBJ_   |          | provided    | discount | rate is   |
| year,cur) | DCEOH, | (0,1\];\ | for each    | rate in  | taken     |
|           | NCAP_  | default  | region.     | region r | into      |
|           | DRATE, | value =  | In          | for each | cons      |
|           | COR_   | none     | terpolation | time     | ideration |
|           | SALVI, |          | is dense    | -period. | when      |
|           | COR_S  | Default  | (all        |          | con       |
|           | ALVD,\ | i/e: STD | individual  |          | structing |
|           | COE    |          | years       |          | the       |
|           | F_PVT\ |          | included).  |          | objective |
|           | VD     |          |             |          | function  |
|           | A_DISC |          |             |          | di        |
|           |        |          |             |          | scounting |
|           |        |          |             |          | m         |
|           |        |          |             |          | ultiplier |
|           |        |          |             |          | (O        |
|           |        |          |             |          | BJ_DISC), |
|           |        |          |             |          | which is  |
|           |        |          |             |          | applied   |
|           |        |          |             |          | in each   |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJVAR, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJINV, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJFIX, |
|           |        |          |             |          | EQ        |
|           |        |          |             |          | _OBJSALV, |
|           |        |          |             |          | EQ        |
|           |        |          |             |          | _OBJELS). |
+-----------+--------+----------+-------------+----------+-----------+
| G_DYEAR   | OB     | Year     |             | Base     | The year  |
|           | J_DISC |          |             | year for | to which  |
|           |        | \[B      |             | disc     | all costs |
|           | CO     | OTIME,EO |             | ounting. | are to be |
|           | EF_PVT | TIME\];\ |             |          | d         |
|           |        | default  |             |          | iscounted |
|           |        | value =  |             |          | is taken  |
|           |        | M(       |             |          | into      |
|           |        | MIYR_1), |             |          | cons      |
|           |        | i.e. the |             |          | ideration |
|           |        | first    |             |          | when      |
|           |        | m        |             |          | con       |
|           |        | ilestone |             |          | structing |
|           |        | year     |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | di        |
|           |        |          |             |          | scounting |
|           |        |          |             |          | m         |
|           |        |          |             |          | ultiplier |
|           |        |          |             |          | (O        |
|           |        |          |             |          | BJ_DISC), |
|           |        |          |             |          | which is  |
|           |        |          |             |          | applied   |
|           |        |          |             |          | in each   |
|           |        |          |             |          | of the    |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJVAR, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJINV, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJFIX, |
|           |        |          |             |          | EQ        |
|           |        |          |             |          | _OBJSALV, |
|           |        |          |             |          | EQ        |
|           |        |          |             |          | _OBJELS). |
+-----------+--------+----------+-------------+----------+-----------+
| G_RFRIR   | G_     | Decimal  | Optional    | R        | The rate  |
|           | DRATE, | fraction | parameter.\ | isk-free | is taken  |
| (r        | NCAP_  |          | If value is | real     | into      |
| ,allyear) | DRATE, | (0,1\];\ | not         | interest | cons      |
|           | COR_   | default  | provided,   | rate in  | ideration |
|           | SALVI, | value =  | G_DRATE is  | region r | when      |
|           | COR    | none     | assumed as  | for each | con       |
|           | _SALVD |          | the         | time     | structing |
|           |        | Default  | risk-free   | -period. | the       |
|           |        | i/e: STD | rate.       |          | objective |
|           |        |          |             | Provides | function  |
|           |        |          | By          | the      | coe       |
|           |        |          | providing   | r        | fficients |
|           |        |          | G_RFRIR,    | eference | for       |
|           |        |          | the         | rate for | i         |
|           |        |          | technolo    | NCA      | nvestment |
|           |        |          | gy-specific | P_DRATE, | costs.    |
|           |        |          | risk        | such     | E         |
|           |        |          | premiums    | that the | Q_OBJINV, |
|           |        |          | can be kept | risk     | E         |
|           |        |          | unchanged   | premium  | Q_OBJSALV |
|           |        |          | over any    | will be  |           |
|           |        |          | sensitivity | ca       |           |
|           |        |          | analyses    | lculated |           |
|           |        |          | with        | against  |           |
|           |        |          | different   | the      |           |
|           |        |          | G_DRATE     | r        |           |
|           |        |          | values.     | isk-free |           |
|           |        |          |             | rate.    |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_ILEDNO  | NCA    | Decimal  | Only        | If the   | Prevents  |
|           | P_ILED | fraction | provided    | ratio of | the       |
|           |        |          | when the    | l        | i         |
|           |        | \        | costs       | ead-time | nvestment |
|           |        | [0,1\];\ | associated  | (NC      | costs     |
|           |        | default  | with the    | AP_ILED) | a         |
|           |        | value:   | lead-time   | to the   | ssociated |
|           |        | 0.1      | for new     | period   | with      |
|           |        |          | capacity    | duration | i         |
|           |        |          | (NCAP_ILED) | (D) is   | nvestment |
|           |        |          | are not to  | below    | l         |
|           |        |          | be included | this     | ead-times |
|           |        |          | in the      | t        | from      |
|           |        |          | objective   | hreshold | energy    |
|           |        |          | function.   | then the | the       |
|           |        |          |             | l        | i         |
|           |        |          | Not taken   | ead-time | nvestment |
|           |        |          | into        | consi    | component |
|           |        |          | account if  | deration | of the    |
|           |        |          | the OBLONG  | will be  | objective |
|           |        |          | switch or   | ignored  | function  |
|           |        |          | any         | in the   | (EQ       |
|           |        |          | alternative | o        | _OBJINV). |
|           |        |          | objective   | bjective |           |
|           |        |          | formulation | function |           |
|           |        |          | is used.    | costs.   |           |
+-----------+--------+----------+-------------+----------+-----------+
| G         | All    | Binary   | Only        | Switch   |           |
| _NOINTERP | para   | i        | provide     | for      |           |
|           | meters | ndicator | when        | g        |           |
|           | that   |          | in          | enerally |           |
|           | are    | \[0 or   | terpolation | tu       |           |
|           | no     | 1\];\    | /           | rning-on |           |
|           | rmally | default  | ex          | (= 0 )   |           |
|           | sub    | value =  | trapolation | and      |           |
|           | jected | 0        | is to be    | tur      |           |
|           | to     |          | turned off  | ning-off |           |
|           | i      |          | for all     | (= 1 )   |           |
|           | nterpo |          | parameters. | sparse   |           |
|           | lation |          |             | inter- / |           |
|           | /      |          | In          | extrap   |           |
|           | e      |          | terpolation | olation. |           |
|           | xtrapo |          | of cost     |          |           |
|           | lation |          | parameters  |          |           |
|           |        |          | is always   |          |           |
|           |        |          | done.       |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_OFFTHD\ | PR     | Scalar\  | Setting     | T        | Affects   |
| (         | C_NOFF | \[0,1\]  | G_OFFTHD=1  | hreshold | ava       |
| datayear) |        |          | will make   | for      | ilability |
|           | PR     | Default  | the \*\_OFF | con      | of        |
|           | C_AOFF | value: 0 | attributes  | sidering |           |
|           |        |          | effective   | an       | V         |
|           | PR     | Default  | only for    | \*\_OFF  | AR_NCAP,\ |
|           | C_FOFF | i/e: 5   | periods     | a        | VAR_ACT,  |
|           |        |          | fully       | ttribute | VAR_FLO,  |
|           | C      |          | included in | d        |           |
|           | OM_OFF |          | the OFF     | isabling | VAR_C     |
|           |        |          | range       | a        | OMNET/PRD |
|           |        |          | specified.  | p        |           |
|           |        |          |             | rocess/c |           |
|           |        |          |             | ommodity |           |
|           |        |          |             | variable |           |
|           |        |          |             | in       |           |
|           |        |          |             | period.  |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_OVERLAP |        | Scalar\  | Used only   | Overlap  | --        |
|           |        | \        | when        | of       |           |
|           |        | [0,100\] | t           | stepped  |           |
|           |        |          | ime-stepped | s        |           |
|           |        | Default  | solution is | olutions |           |
|           |        | value:   | activated   | (in      |           |
|           |        | TI       | with the    | years).  |           |
|           |        | MESTEP/2 | TIMESTEP    |          |           |
|           |        |          | control     |          |           |
|           |        |          | variable.   |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_TLIFE   | NCAP   | Scalar   |             | Default  |           |
|           | _TLIFE |          |             | value    |           |
|           |        | \[1,∞);\ |             | for the  |           |
|           |        | default  |             | t        |           |
|           |        | value =  |             | echnical |           |
|           |        | 10       |             | lifetime |           |
|           |        |          |             | of a     |           |
|           |        |          |             | process  |           |
|           |        |          |             | if not   |           |
|           |        |          |             | provided |           |
|           |        |          |             | by the   |           |
|           |        |          |             | user.    |           |
+-----------+--------+----------+-------------+----------+-----------+
| G_YRFR    | RTCS   | Fraction | Must be     | Duration | Applied   |
|           | _TSFR, |          | provided    | of       | to        |
| (all_r,s) | RS_    | \        | for each    | t        | various   |
|           | STGPRD | [0,1\];\ | region and  | imeslice | variables |
|           |        | default  | timeslice.  | s as     | (VAR_NC   |
|           |        | value:   |             | fraction | AP+PASTI, |
|           |        | none;    |             | of a     | VAR_COMX, |
|           |        | only for |             | year.    | VAR_IRE,  |
|           |        | the      |             | Used for | VAR_FLO,  |
|           |        | ANNUAL   |             | shaping  | VAR       |
|           |        | t        |             | the load | _SIN/OUT) |
|           |        | imeslice |             | curve    | in the    |
|           |        | a value  |             | and      | commodity |
|           |        | of 1 is  |             | lining   | balance   |
|           |        | pr       |             | up       | equation  |
|           |        | edefined |             | t        | (EQ(l)\   |
|           |        |          |             | imeslice | _COMBAL). |
|           |        |          |             | duration |           |
|           |        |          |             | for      |           |
|           |        |          |             | inter-   |           |
|           |        |          |             | regional |           |
|           |        |          |             | ex       |           |
|           |        |          |             | changes. |           |
+-----------+--------+----------+-------------+----------+-----------+
| IRE_BND   | t      | C        | Only        | Bound on | Controls  |
|           | op_ire | ommodity | applicable  | the      | the       |
| (         |        | unit     | for         | total    | instances |
| r,datayea |        |          | int         | import   | for which |
| r,c,s,all |        | \[0,∞);\ | er-regional | (export) | the trade |
| _r,ie,bd) |        | default  | exchange    | of       | bound     |
|           |        | value:   | processes   | c        | c         |
|           |        | none     | (IRE).      | ommodity | onstraint |
|           |        |          |             | (c) from | (EQ(l)    |
|           |        | Default  | If the      | (to)     | \_IREBND) |
|           |        | i/e: MIG | bound is    | region   | is        |
|           |        |          | specified   | all_r in | g         |
|           |        |          | for a       | (out of) | enerated, |
|           |        |          | timeslice   | region   | and the   |
|           |        |          | (s) being   | r.       | RHS.      |
|           |        |          | above the   |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | (c)         |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | resolution, |          |           |
|           |        |          | the bound   |          |           |
|           |        |          | is applied  |          |           |
|           |        |          | to the sum  |          |           |
|           |        |          | of the      |          |           |
|           |        |          | impo        |          |           |
|           |        |          | rts/exports |          |           |
|           |        |          | according   |          |           |
|           |        |          | to the      |          |           |
|           |        |          | timeslice   |          |           |
|           |        |          | tree.       |          |           |
|           |        |          |             |          |           |
|           |        |          | Standard    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| IRE_CCVT  | IRE_   | Scalar\  | Required    | Co       | The       |
|           | TSCVT, | (0,∞)    | for mapping | nversion | c         |
| (r1,c     | t      |          | commodities | factor   | onversion |
| 1,r2,c2)) | op_ire | Default  | involved in | between  | factor is |
|           |        | value: 1 | int         | c        | applied   |
|           |        | if       | er-regional | ommodity | to the    |
|           |        | c        | exchanges   | units in | flow      |
|           |        | ommodity | between two | region   | variable  |
|           |        | names    | regions     | r1 and   | (VAR_IRE) |
|           |        | are the  | whenever    | region   | in the    |
|           |        | same in  | commodities | r2.      | inter     |
|           |        | both     | traded are  | E        | -regional |
|           |        | regions  | in          | xpresses | balance   |
|           |        |          | different   | the      | c         |
|           |        | I/e: N/A | units in    | amount   | onstraint |
|           |        |          | the         | of       | (EQ_IRE). |
|           |        |          | regions.    | c        |           |
|           |        |          |             | ommodity | S         |
|           |        |          |             | c2 in    | imilarly, |
|           |        |          |             | region   | applied   |
|           |        |          |             | r2       | to the    |
|           |        |          |             | eq       | flow      |
|           |        |          |             | uivalent | variable  |
|           |        |          |             | to 1     | (VAR_IRE) |
|           |        |          |             | unit of  | when an   |
|           |        |          |             | c        | inter     |
|           |        |          |             | ommodity | -regional |
|           |        |          |             | c1 in    | exchange  |
|           |        |          |             | region   | is        |
|           |        |          |             | r1.      | bounded   |
|           |        |          |             |          | in the    |
|           |        |          |             |          | limit     |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQ(l)\   |
|           |        |          |             |          | _IREBND). |
|           |        |          |             |          |           |
|           |        |          |             |          | S         |
|           |        |          |             |          | imilarly, |
|           |        |          |             |          | applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | flow      |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (VAR_IRE) |
|           |        |          |             |          | when an   |
|           |        |          |             |          | exchange  |
|           |        |          |             |          | with an   |
|           |        |          |             |          | external  |
|           |        |          |             |          | region is |
|           |        |          |             |          | bounded   |
|           |        |          |             |          | (EQ(l     |
|           |        |          |             |          | )\_XBND). |
+-----------+--------+----------+-------------+----------+-----------+
| IRE_FLO   | t      | C        | Only        | Ef       | Applied   |
|           | op_ire | ommodity | applicable  | ficiency | to the    |
| (r1,datay |        | unit     | for         | of       | exchange  |
| ear,p,c1, |        | c2/c     | int         | exchange | flow      |
| r2,c2,s2) |        | ommodity | er-regional | process  | variable  |
|           |        | unit c1  | exchange    | from     | (VAR_IRE) |
|           |        |          | processes   | c        | in the    |
|           |        | \[0,∞);\ | (IRE)       | ommodity | inter     |
|           |        | default  | between two | c1 in    | -regional |
|           |        | value: 1 | internal    | region   | trade     |
|           |        |          | regions.    | r1 to    | equation  |
|           |        | Default  |             | c        | (EQ_IRE). |
|           |        | i/e: STD | Note that   | ommodity |           |
|           |        |          | for each    | c2 in    | Applied   |
|           |        |          | direction   | the      | to the    |
|           |        |          | of trade a  | region2  | exchange  |
|           |        |          | separate    | in       | flow      |
|           |        |          | IRE_FLO     | t        | variable  |
|           |        |          | needs to be | imeslice | (VAR_IRE) |
|           |        |          | specified.  | s2; the  | when a    |
|           |        |          |             | t        | bound on  |
|           |        |          | Similar to  | imeslice | inter     |
|           |        |          | FLO_FUNC    | s2       | -regional |
|           |        |          | for         | refers   | trade is  |
|           |        |          | standard    | to the   | to be     |
|           |        |          | processes.  | r2       | applied   |
|           |        |          |             | region.  | (EQ(l)\   |
|           |        |          | Direct      |          | _IREBND). |
|           |        |          | i           |          |           |
|           |        |          | nheritance. |          |           |
|           |        |          |             |          |           |
|           |        |          | Weighted    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| I         | t      | C        | Only        | A        | The       |
| RE_FLOSUM | op_ire | ommodity | applicable  | uxiliary | m         |
|           |        | unit     | for         | con      | ultiplier |
| (         |        | c2/c     | int         | sumption | is        |
| r,datayea |        | ommodity | er-regional | (io =    | applied   |
| r,p,c1,s, |        | unit c1  | exchange    | IN,      | to the    |
| ie,c2,io) |        |          | processes   | owing to | flow      |
|           |        | \[       | (IRE).      | the      | variable  |
|           |        | open\];\ |             | c        | (VAR_IRE) |
|           |        | default  | Since the   | ommodity | a         |
|           |        | value:   | efficiency  | entering | ssociated |
|           |        | none     | IRE_FLO can | the      | with an   |
|           |        |          | only be     | process) | inte      |
|           |        | Default  | used for    | or       | r-reginal |
|           |        | i/e: STD | exchange    | pro      | exchange  |
|           |        |          | between     | duction/ | in the    |
|           |        |          | internal    | emission | commodity |
|           |        |          | regions,    | (io =    | balance   |
|           |        |          | IRE_FLOSUM  | OUT,     | c         |
|           |        |          | may be used | owing to | onstraint |
|           |        |          | to define   | the      | (EQ(l)\   |
|           |        |          | an          | c        | _COMBAL). |
|           |        |          | efficiency  | ommodity |           |
|           |        |          | for an      | leaving  | If a flow |
|           |        |          | im          | the      | share     |
|           |        |          | port/export | process) | (         |
|           |        |          | with an     | of       | FLO_SHAR) |
|           |        |          | external    | c        | is        |
|           |        |          | region by   | ommodity | provided  |
|           |        |          | specifying  | c2 due   | for an    |
|           |        |          | the same    | to the   | inter     |
|           |        |          | commodity   | IMPort / | -regional |
|           |        |          | for c1 and  | EXPort   | exchange  |
|           |        |          | c2 and the  | (index   | process   |
|           |        |          | value       | ie) of   | then the  |
|           |        |          | 1           | the      | m         |
|           |        |          | -efficiency | c        | ultiplier |
|           |        |          | as          | ommodity | is        |
|           |        |          | auxiliary   | c1 in    | applied   |
|           |        |          | c           | region   | to the    |
|           |        |          | onsumption. | r[^30]   | flow      |
|           |        |          |             |          | variable  |
|           |        |          | Direct      |          | (VAR_IRE) |
|           |        |          | i           |          | in the    |
|           |        |          | nheritance. |          | share     |
|           |        |          |             |          | c         |
|           |        |          | Weighted    |          | onstraint |
|           |        |          | a           |          | (         |
|           |        |          | ggregation. |          | EQ(l)\_IN |
|           |        |          |             |          | /OUTSHR). |
|           |        |          |             |          |           |
|           |        |          |             |          | If a cost |
|           |        |          |             |          | is        |
|           |        |          |             |          | provided  |
|           |        |          |             |          | for the   |
|           |        |          |             |          | flow      |
|           |        |          |             |          | (FLO_COST |
|           |        |          |             |          | or        |
|           |        |          |             |          | F         |
|           |        |          |             |          | LO_DELIV) |
|           |        |          |             |          | then the  |
|           |        |          |             |          | factor is |
|           |        |          |             |          | applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | flow      |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (VAR_IRE) |
|           |        |          |             |          | in the    |
|           |        |          |             |          | variable  |
|           |        |          |             |          | component |
|           |        |          |             |          | of the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJVAR). |
+-----------+--------+----------+-------------+----------+-----------+
| IRE_PRICE | OBJ_   | Monetary | Only        | IMPor    | The price |
|           | IPRIC, | unit /   | applicable  | t/EXPort | of the    |
| (r,d      | CST    | c        | for         | price    | exchange  |
| atayear,p | _COMC, | ommodity | int         | (index   | commodity |
| ,c,s,all_ |        | unit     | er-regional | ie) for  | is        |
| r,ie,cur) | CS     |          | exchange    | to/from  | applied   |
|           | T_PVP, | \[0,∞);\ | processes   | an       | to the    |
|           |        | default  | (IRE).      | internal | trade     |
|           | t      | value:   |             | region   | flow      |
|           | op_ire | none     | Ignored if  | of a     | variable  |
|           |        |          | all_r is an | c        | (VAR_IRE) |
|           |        | Default  | internal    | ommodity | in the    |
|           |        | i/e: STD | region.     | (c)      | variable  |
|           |        |          |             | ori      | costs     |
|           |        |          | Direct      | ginating | component |
|           |        |          | i           | from     | of the    |
|           |        |          | nheritance. | /heading | objective |
|           |        |          |             | to an    | function  |
|           |        |          | Weighted    | external | (EQ       |
|           |        |          | a           | region   | _OBJVAR). |
|           |        |          | ggregation. | all_r.   |           |
+-----------+--------+----------+-------------+----------+-----------+
| IRE_TSCVT | IRE    | Scalar   | Used for    | Matrix   | The       |
|           | _CCVT, |          | mapping     | for      | c         |
| (r1,      |        | (0,∞);\  | timeslices  | mapping  | onversion |
| s1,r2,s2) | t      | default  | in          | tim      | factor is |
|           | op_ire | value: 1 | different   | eslices; | applied   |
|           |        | if       | regions.    | the      | to the    |
|           |        | t        |             | value    | flow      |
|           |        | imeslice | Required if | for      | variable  |
|           |        | tree and | timeslice   | (r1,s    | (VAR_IRE) |
|           |        | names    | definitions | 1,r2,s2) | in the    |
|           |        | are the  | are         | gives    | inter     |
|           |        | same in  | different   | the      | -regional |
|           |        | both     | in the      | fraction | balance   |
|           |        | regions  | regions.    | of       | c         |
|           |        |          |             | t        | onstraint |
|           |        | I/e: N/A |             | imeslice | (EQ_IRE). |
|           |        |          |             | s2 in    |           |
|           |        |          |             | region   | S         |
|           |        |          |             | r2 that  | imilarly, |
|           |        |          |             | falls in | applied   |
|           |        |          |             | t        | to the    |
|           |        |          |             | imeslice | flow      |
|           |        |          |             | s1 in    | variable  |
|           |        |          |             | region   | (VAR_IRE) |
|           |        |          |             | r1.      | when an   |
|           |        |          |             |          | inter     |
|           |        |          |             |          | -regional |
|           |        |          |             |          | exchange  |
|           |        |          |             |          | is        |
|           |        |          |             |          | bounded   |
|           |        |          |             |          | in the    |
|           |        |          |             |          | limit     |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (EQ(l)\   |
|           |        |          |             |          | _IREBND). |
|           |        |          |             |          |           |
|           |        |          |             |          | S         |
|           |        |          |             |          | imilarly, |
|           |        |          |             |          | applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | flow      |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (VAR_IRE) |
|           |        |          |             |          | when an   |
|           |        |          |             |          | exchange  |
|           |        |          |             |          | with an   |
|           |        |          |             |          | external  |
|           |        |          |             |          | region is |
|           |        |          |             |          | bounded   |
|           |        |          |             |          | (EQ(l     |
|           |        |          |             |          | )\_XBND). |
+-----------+--------+----------+-------------+----------+-----------+
| IRE_XBND  | t      | C        | Only        | Bound on | The trade |
|           | op_ire | ommodity | applicable  | the      | limit     |
| (         |        | unit     | for         | total    | equation  |
| all_r,dat |        |          | int         | IMPort   | EQ        |
| ayear,c,s |        | \[0,∞);\ | er-regional | (EXPort) | (l)\_XBND |
| ie,bd)    |        | default  | exchange    | (index   | generated |
|           |        | value:   | processes   | ie) of   | either    |
|           |        | none     | (IRE).      | c        | sums      |
|           |        |          |             | ommodity | lower     |
|           |        | Default  | Provide     | c in     | flow      |
|           |        | i/e: MIG | whenever a  | region   | variables |
|           |        |          | trade flow  | all_r    | (VAR_IRE) |
|           |        |          | is to be    | with all | or splits |
|           |        |          | c           | sources  | (         |
|           |        |          | onstrained. | (destin  | according |
|           |        |          |             | ations). | to the    |
|           |        |          | Note that   |          | timeslice |
|           |        |          | the limit   |          | tree)     |
|           |        |          | is either   |          | coarser   |
|           |        |          | imposed by  |          | v         |
|           |        |          | summing     |          | ariables. |
|           |        |          | lower or    |          |           |
|           |        |          | splitting   |          |           |
|           |        |          | higher flow |          |           |
|           |        |          | variables   |          |           |
|           |        |          | (VAR_IRE)   |          |           |
|           |        |          | when        |          |           |
|           |        |          | specified   |          |           |
|           |        |          | at other    |          |           |
|           |        |          | than the    |          |           |
|           |        |          | actual flow |          |           |
|           |        |          | level (as   |          |           |
|           |        |          | determined  |          |           |
|           |        |          | by the      |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | and process |          |           |
|           |        |          | levels      |          |           |
|           |        |          | (COM_TSL/   |          |           |
|           |        |          | PRC_TSL ).  |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| MULTI     | NCA    | Scalar   | Only        | Mu       | *{See     |
|           | P_AFM, |          | provided    | ltiplier | Related   |
| (j        | NCAP   | \[       | when the    | table    | Par       |
| ,allyear) | _FOMM, | open\];\ | related     | used for | ameters}* |
|           |        | default  | shaping     | any      |           |
|           | NCAP_  | value:   | parameters  | shaping  |           |
|           | FSUBM, | none     | are to be   | pa       |           |
|           |        |          | used.       | rameters |           |
|           | NCAP   | I/e:     |             | (        |           |
|           | _FTAXM | Full     |             | \*\_\*M) |           |
|           |        | dense    |             | to       |           |
|           |        | inter    |             | adjust   |           |
|           |        | polation |             | the      |           |
|           |        | and      |             | corre    |           |
|           |        | extra    |             | sponding |           |
|           |        | polation |             | t        |           |
|           |        |          |             | echnical |           |
|           |        |          |             | data as  |           |
|           |        |          |             | function |           |
|           |        |          |             | of the   |           |
|           |        |          |             | year;    |           |
|           |        |          |             | the      |           |
|           |        |          |             | table    |           |
|           |        |          |             | contains |           |
|           |        |          |             | d        |           |
|           |        |          |             | ifferent |           |
|           |        |          |             | mu       |           |
|           |        |          |             | ltiplier |           |
|           |        |          |             | curves   |           |
|           |        |          |             | id       |           |
|           |        |          |             | entified |           |
|           |        |          |             | by the   |           |
|           |        |          |             | index j. |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AF   | NCA    | Decimal  | NCAP_AF,    | Avai     | The       |
|           | P_AFA, | fraction | NCAP_AFA    | lability | corr      |
| (         | NCA    |          | and         | factor   | esponding |
| r,datayea | P_AFS, | \        | NCAP_AFS    | relating | capacity  |
| r,p,s,bd) | NCA    | [0,1\];\ | can be      | a unit   | -activity |
|           | P_AFM, | default  | applied     | of       | c         |
|           | NCA    | value: 1 | simu        | pr       | onstraint |
|           | P_AFX, |          | ltaneously. | oduction | (EQ(l)    |
|           | C      | Default  |             | (process | \_CAPACT) |
|           | OEF_AF | i/e: STD | Direct      | a        | will be   |
|           |        |          | i           | ctivity) | generated |
|           |        | Remark:  | nheritance. | in       | for any   |
|           |        | In       |             | t        | timeslice |
|           |        | special  | Weighted    | imeslice | s.        |
|           |        | cases    | ag          | s to the |           |
|           |        | values   | gregation.\ | current  | If the    |
|           |        | \>1 can  | (Important  | i        | process   |
|           |        | also be  | remark:\    | nstalled | timeslice |
|           |        | used     | No          | c        | level     |
|           |        | (when    | i           | apacity. | (PRC_TSL) |
|           |        | PR       | nheritance/ |          | is below  |
|           |        | C_CAPACT | aggregation |          | said      |
|           |        | does not | if any      |          | level,    |
|           |        | r        | value is    |          | the       |
|           |        | epresent | specified   |          | activity  |
|           |        | the max. | at process  |          | variables |
|           |        | t        | t           |          | will be   |
|           |        | echnical | imeslices.) |          | summed.   |
|           |        | level of |             |          |           |
|           |        | activity |             |          |           |
|           |        | per unit |             |          |           |
|           |        | of       |             |          |           |
|           |        | ca       |             |          |           |
|           |        | pacity). |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AFA  | NCA    | Decimal  | Provided    | Annual   | The       |
|           | P_AFA, | fraction | when        | avai     | corr      |
| (r,datay  | NCA    |          | 'ANNUAL'    | lability | esponding |
| ear,p,bd) | P_AFS, | \        | level       | factor   | capacity  |
|           | NCA    | [0,1\];\ | process     | relating | -activity |
|           | P_AFM, | default  | operation   | the      | c         |
|           | NCA    | value:   | is to be    | annual   | onstraint |
|           | P_AFX, | none     | controlled. | activity | (EQ(l)    |
|           | C      |          |             | of a     | \_CAPACT) |
|           | OEF_AF | Default  | NCAP_AF,    | process  | will be   |
|           |        | i/e: STD | NCAP_AFA    | to the   | generated |
|           |        |          | and         | i        | for the   |
|           |        | Remark:  | NCAP_AFS    | nstalled | 'ANNUAL'  |
|           |        | In       | can be      | c        | t         |
|           |        | special  | applied     | apacity. | imeslice. |
|           |        | cases    | simu        |          |           |
|           |        | values   | ltaneously. |          | If the    |
|           |        | \>1 can  |             |          | process   |
|           |        | also be  | NCAP_AFA is |          | timeslice |
|           |        | used     | always      |          | level     |
|           |        | (when    | assumed to  |          | (PRC_TSL) |
|           |        | PR       | be          |          | is below  |
|           |        | C_CAPACT | non-vintage |          | said      |
|           |        | has been | dependent,  |          | level,    |
|           |        | chosen   | even if the |          | the       |
|           |        | not to   | process is  |          | activity  |
|           |        | r        | defined as  |          | variables |
|           |        | epresent | a vintaged  |          | will be   |
|           |        | the max. | one; for    |          | summed.   |
|           |        | t        | vintag      |          |           |
|           |        | echnical | e-dependent |          |           |
|           |        | level of | annual      |          |           |
|           |        | activity | a           |          |           |
|           |        | per unit | vailability |          |           |
|           |        | of       | NCAP_AFS    |          |           |
|           |        | ca       | with        |          |           |
|           |        | pacity). | s='ANNUAL'  |          |           |
|           |        |          | can be      |          |           |
|           |        |          | used.       |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AFC\ | NCA    | Decimal  | If the      | Co       | Generates |
| (r,       | P_AFCS | fraction | commodities | mmodity- | instances |
| datayear, |        |          | are in the  | specific | of        |
| p,cg,tsl) |        | \[0,∞);\ | PCG,        | avai     |           |
|           |        | default  | constraint  | lability | EQ(l      |
|           |        | value:   | is applied  | of       | )\_CAFLAC |
|           |        | none     | to the      | capacity | (thereby  |
|           |        |          | flows in    | for      | disabling |
|           |        | Default  | the PCG as  | c        | EQ(l      |
|           |        | i/e: STD | a whole     | ommodity | )\_CAPACT |
|           |        |          | (linear     | group    | gen       |
|           |        |          | combination | cg, at   | eration), |
|           |        |          | of flows).\ | given    | or        |
|           |        |          | Independent | t        | EQ        |
|           |        |          | equations   | imeslice | L_CAPFLO. |
|           |        |          | are         | level.   |           |
|           |        |          | generated   |          |           |
|           |        |          | for         |          |           |
|           |        |          | commodities |          |           |
|           |        |          | not in the  |          |           |
|           |        |          | PCG, or     |          |           |
|           |        |          | when        |          |           |
|           |        |          | NCAP_AFC(   |          |           |
|           |        |          | r,'0',p,'AC |          |           |
|           |        |          | T',tsl)=--1 |          |           |
|           |        |          | is also     |          |           |
|           |        |          | specified.  |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NC     | Decimal  | See         | Co       | See       |
| CAP_AFCS\ | AP_AFC | fraction | NCAP_AFC.   | mmodity- | NCAP_AFC. |
| (r        |        |          |             | specific |           |
| ,datayear |        | \[0,∞);\ | NCAP_AFCS   | avai     |           |
| ,p,cg,ts) |        | default  | is similar  | lability |           |
|           |        | value:   | to NCAP_AFC | of       |           |
|           |        | none     | but is      | capacity |           |
|           |        |          | defined on  | for      |           |
|           |        | Default  | individual  | c        |           |
|           |        | i/e: STD | timeslices. | ommodity |           |
|           |        |          | Overrides   | group    |           |
|           |        |          | NCAP_AFC.   | cg,      |           |
|           |        |          |             | tim      |           |
|           |        |          |             | eslice-s |           |
|           |        |          |             | pecific. |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AFM  | NC     | Integer  | Provided    | Period   | *{See     |
|           | AP_AF, | number   | when        | s        | Related   |
| (r,da     | NCA    |          | mul         | ensitive | Par       |
| tayear,p) | P_AFA, | Default  | tiplication | mu       | ameters}* |
|           | NCA    | value: 0 | of NCAP_AF  | ltiplier |           |
|           | P_AFS, | (no      | / NCAP_AFS  | curve    |           |
|           | MULTI, | mu       | based upon  | (MULTI)  |           |
|           | C      | ltiplier | year is     | to be    |           |
|           | OEF_AF | applied) | desired.    | applied  |           |
|           |        |          |             | to the   |           |
|           |        | Default  | Note:       | avai     |           |
|           |        | extrap   | Multiplier  | lability |           |
|           |        | olation: | index 1 is  | factor   |           |
|           |        | MIG      | reserved    | pa       |           |
|           |        |          | for         | rameters |           |
|           |        |          | constant 1. | (        |           |
|           |        |          |             | NCAP_AF/ |           |
|           |        |          |             | AFA/AFS) |           |
|           |        |          |             | of a     |           |
|           |        |          |             | process. |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AFS  |        | Decimal  | NCAP_AF,    | Avai     | The       |
|           |        | fraction | NCAP_AFA    | lability | corr      |
| (         |        |          | and         | factor   | esponding |
| r,datayea |        | \        | NCAP_AFS    | relating | capacity  |
| r,p,s,bd) |        | [0,1\];\ | can be      | the      | -activity |
|           |        | default  | applied     | activity | c         |
|           |        | value:   | simu        | of a     | onstraint |
|           |        | none     | ltaneously. | process  | (EQ(l)    |
|           |        |          |             | in a     | \_CAPACT) |
|           |        | Default  | NCAP_AFS    | t        | will be   |
|           |        | i/e: STD | being       | imeslice | generated |
|           |        |          | specified   | s being  | for a     |
|           |        | Remark:  | for         | at or    | timeslice |
|           |        | In       | timeslices  | above    | s being   |
|           |        | special  | s being     | the      | at or     |
|           |        | cases    | below the   | process  | above the |
|           |        | values   | process     | t        | process   |
|           |        | \>1 can  | timeslice   | imeslice | timeslice |
|           |        | also be  | level are   | level    | level     |
|           |        | used (in | ignored.    | (        | (         |
|           |        | cases    |             | prc_tsl) | prc_tsl). |
|           |        | where    | No          | to the   |           |
|           |        | PR       | i           | i        | If the    |
|           |        | C_CAPACT | nheritance. | nstalled | process   |
|           |        | has been |             | c        | timeslice |
|           |        | chosen   | No          | apacity. | level is  |
|           |        | not to   | a           | If for   | below     |
|           |        | r        | ggregation. | example  | said      |
|           |        | epresent |             | the      | level,    |
|           |        | the      | Can be used | process  | the       |
|           |        | maximum  | also on the | t        | activity  |
|           |        | t        | process     | imeslice | variables |
|           |        | echnical | timeslices, | level is | will be   |
|           |        | level of | and will    | '        | summed.   |
|           |        | activity | then        | DAYNITE' |           |
|           |        | per unit | override    | and      |           |
|           |        | of       | the         | NCAP_AFS |           |
|           |        | ca       | levelized   | is       |           |
|           |        | pacity). | NCAP_AF     | s        |           |
|           |        |          | a           | pecified |           |
|           |        |          | vailability | for      |           |
|           |        |          | factors.    | ti       |           |
|           |        |          |             | meslices |           |
|           |        |          |             | on the   |           |
|           |        |          |             | 'S       |           |
|           |        |          |             | EASONAL' |           |
|           |        |          |             | level,   |           |
|           |        |          |             | the sum  |           |
|           |        |          |             | of the   |           |
|           |        |          |             | '        |           |
|           |        |          |             | DAYNITE' |           |
|           |        |          |             | ac       |           |
|           |        |          |             | tivities |           |
|           |        |          |             | within a |           |
|           |        |          |             | season   |           |
|           |        |          |             | are      |           |
|           |        |          |             | res      |           |
|           |        |          |             | tricted, |           |
|           |        |          |             | but not  |           |
|           |        |          |             | the      |           |
|           |        |          |             | '        |           |
|           |        |          |             | DAYNITE' |           |
|           |        |          |             | ac       |           |
|           |        |          |             | tivities |           |
|           |        |          |             | d        |           |
|           |        |          |             | irectly. |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AFSX | NCA    | Integer  | Provided    | A        | *{See     |
|           | P_AFS, | number   | when        | ge-based | Related   |
| (r,datay  | SHAPE, |          | shaping     | shaping  | Par       |
| ear,p,bd) | C      | Default  | based upon  | curve    | ameters}* |
|           | OEF_AF | value: 0 | age is      | (SHAPE)  |           |
|           |        | (no      | desired.    | to be    |           |
|           |        | shape    |             | applied  |           |
|           |        | curve    | NCAP_AFSX   | to the   |           |
|           |        | applied) | is applied  | seasonal |           |
|           |        |          | to          | avai     |           |
|           |        | Default  | NCAP_AFS,   | lability |           |
|           |        | extrap   | but not on  | factor   |           |
|           |        | olation: | the annual  | pa       |           |
|           |        | MIG      | level if    | rameters |           |
|           |        |          | a           | (NCAP\_  |           |
|           |        |          | vailability | AFS) of  |           |
|           |        |          | is also     | a        |           |
|           |        |          | defined by  | process. |           |
|           |        |          | NCAP_AFA.   |          |           |
|           |        |          |             |          |           |
|           |        |          | The SHAPE   |          |           |
|           |        |          | parameter   |          |           |
|           |        |          | is applied  |          |           |
|           |        |          | even for    |          |           |
|           |        |          | n           |          |           |
|           |        |          | on-vintaged |          |           |
|           |        |          | process     |          |           |
|           |        |          | whenever    |          |           |
|           |        |          | NCAP_AFSX   |          |           |
|           |        |          | is          |          |           |
|           |        |          | specified,  |          |           |
|           |        |          | i.e.        |          |           |
|           |        |          | NCAP_AFS    |          |           |
|           |        |          | ava         |          |           |
|           |        |          | ilabilities |          |           |
|           |        |          | will then   |          |           |
|           |        |          | be          |          |           |
|           |        |          | vintaged.   |          |           |
|           |        |          |             |          |           |
|           |        |          | Note: Shape |          |           |
|           |        |          | index 1 is  |          |           |
|           |        |          | reserved    |          |           |
|           |        |          | for         |          |           |
|           |        |          | constant 1. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_AFX  | NC     | Integer  | Provided    | A        | *{See     |
|           | AP_AF, | number   | when        | ge-based | Related   |
| (r,da     | NCA    |          | shaping     | shaping  | Par       |
| tayear,p) | P_AFA, | Default  | based upon  | curve    | ameters}* |
|           | NCA    | value: 0 | age is      | (SHAPE)  |           |
|           | P_AFS, | (no      | desired.    | to be    |           |
|           | SHAPE, | shape    |             | applied  |           |
|           | C      | curve    | NCAP_AFX is | to the   |           |
|           | OEF_AF | applied) | applied to  | avai     |           |
|           |        |          | NCAP_AF and | lability |           |
|           |        | Default  | NCAP_AFS,   | factor   |           |
|           |        | extrap   | but not the | pa       |           |
|           |        | olation: | annual      | rameters |           |
|           |        | MIG      | a           | (        |           |
|           |        |          | vailability | NCAP_AF/ |           |
|           |        |          | NCAP_AFA.   | AFA/AFS) |           |
|           |        |          |             | of a     |           |
|           |        |          | For         | process. |           |
|           |        |          | n           |          |           |
|           |        |          | on-vintaged |          |           |
|           |        |          | process,    |          |           |
|           |        |          | the SHAPE   |          |           |
|           |        |          | parameter   |          |           |
|           |        |          | is only     |          |           |
|           |        |          | applied to  |          |           |
|           |        |          | NCAP_AF,    |          |           |
|           |        |          | i.e.        |          |           |
|           |        |          | ava         |          |           |
|           |        |          | ilabilities |          |           |
|           |        |          | at process  |          |           |
|           |        |          | timeslices  |          |           |
|           |        |          | will be     |          |           |
|           |        |          | vintaged.   |          |           |
|           |        |          |             |          |           |
|           |        |          | Note: Shape |          |           |
|           |        |          | index 1 is  |          |           |
|           |        |          | reserved    |          |           |
|           |        |          | for         |          |           |
|           |        |          | constant 1. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_BND  |        | Capacity | Provided    | Bound on | Imposes   |
|           |        | unit     | for each    | the      | an        |
| (r,datay  |        |          | process to  | p        | indirect  |
| ear,p,bd) |        | \[0,∞);\ | have its    | ermitted | limit on  |
|           |        | default  | overall     | level on | the       |
|           |        | value:   | installed   | in       | capacity  |
|           |        | none     | capacity    | vestment | transfer  |
|           |        |          | (VAR_NCAP)  | in new   | equation  |
|           |        | Default  | limited in  | capacity | (EQ_CPT)  |
|           |        | i/e: MIG | a period.   |          | by means  |
|           |        |          |             |          | of a      |
|           |        |          | Since       |          | direct    |
|           |        |          | inter-/ex   |          | bound on  |
|           |        |          | trapolation |          | the new   |
|           |        |          | default is  |          | in        |
|           |        |          | MIG, a      |          | vestments |
|           |        |          | bound must  |          | capacity  |
|           |        |          | be          |          | variable  |
|           |        |          | specified   |          | (V        |
|           |        |          | for each    |          | AR_NCAP). |
|           |        |          | period      |          |           |
|           |        |          | desired, if |          |           |
|           |        |          | no explicit |          |           |
|           |        |          | inter-/ex   |          |           |
|           |        |          | trapolation |          |           |
|           |        |          | option is   |          |           |
|           |        |          | given, e.g. |          |           |
|           |        |          | NCAP_B      |          |           |
|           |        |          | ND(R,'0',P) |          |           |
|           |        |          | =2.         |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCA    | Decimal  | The         | Back     | Process   |
| CAP_BPME\ | P_CDME | fraction | parameter   | pressure | trans     |
| (r,da     |        |          | is only     | mode     | formation |
| tayear,p) |        | \[0,∞);\ | taken into  | ef       | equation, |
|           |        | default  | account     | ficiency | either    |
|           |        | value:   | when the    | (or      |           |
|           |        | none     | process is  | total    | E         |
|           |        |          | of type     | ef       | QE_ACTEFF |
|           |        | Default  | CHP, and    | ficiency | or\       |
|           |        | i/e: STD | NCAP_CDME   | in full  | EQ_PTRANS |
|           |        |          | has been    | CHP      |           |
|           |        |          | also        | mode).   |           |
|           |        |          | defined.    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCA    | Decimal  | The         | Co       | Process   |
| CAP_CDME\ | P_BPME | fraction | parameter   | ndensing | trans     |
| (r,da     |        |          | can only be | mode     | formation |
| tayear,p) |        | \[0,∞);\ | used for    | ef       | equation, |
|           |        | default  | standard    | ficiency | either    |
|           |        | value:   | process­es   |          |           |
|           |        | none     | having      |          | E         |
|           |        |          | electricity |          | QE_ACTEFF |
|           |        | Default  | output in   |          | or\       |
|           |        | i/e: STD | the PCG.    |          | EQ_PTRANS |
|           |        |          | The         |          |           |
|           |        |          | efficiency  |          |           |
|           |        |          | is applied  |          |           |
|           |        |          | between the |          |           |
|           |        |          | default     |          |           |
|           |        |          | shadow      |          |           |
|           |        |          | group and   |          |           |
|           |        |          | the         |          |           |
|           |        |          | e           |          |           |
|           |        |          | lectricity. |          |           |
|           |        |          | If the      |          |           |
|           |        |          | process is  |          |           |
|           |        |          | also        |          |           |
|           |        |          | defined as  |          |           |
|           |        |          | a CHP, heat |          |           |
|           |        |          | efficiency  |          |           |
|           |        |          | is also     |          |           |
|           |        |          | included.   |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_CEH\ | NCA    | Decimal  | The         | Coe      | Process   |
| (r,da     | P_CHPR | fraction | parameter   | fficient | trans     |
| tayear,p) |        |          | is only     | of       | formation |
|           | A      | \[       | taken into  | ele      | equation, |
|           | CT_EFF | --1,∞\]; | account     | ctricity | either    |
|           |        |          | when the    | to heat  |           |
|           |        | default  | process is  | along    | E         |
|           |        | value:   | defined to  | the      | QE_ACTEFF |
|           |        | none     | be of type  | iso-fuel | or\       |
|           |        |          | CHP.        | line in  | EQ_PTRANS |
|           |        | Default  | According   | a        |           |
|           |        | i/e: STD | to the CEH  | pass-out |           |
|           |        |          | value, the  | CHP      |           |
|           |        |          | process     | tec      |           |
|           |        |          | activity    | hnology. |           |
|           |        |          | will be     |          |           |
|           |        |          | defined as: |          |           |
|           |        |          |             |          |           |
|           |        |          | CEH ≤ 0:    |          |           |
|           |        |          | Max.        |          |           |
|           |        |          | electricity |          |           |
|           |        |          | output      |          |           |
|           |        |          | according   |          |           |
|           |        |          | to CHPR     |          |           |
|           |        |          |             |          |           |
|           |        |          | 0           |          |           |
|           |        |          |  \< CEH ≤1: |          |           |
|           |        |          | Condensing  |          |           |
|           |        |          | mode        |          |           |
|           |        |          | electricity |          |           |
|           |        |          | output      |          |           |
|           |        |          |             |          |           |
|           |        |          | CEH ≥ 1:    |          |           |
|           |        |          | Total       |          |           |
|           |        |          | energy      |          |           |
|           |        |          | output in   |          |           |
|           |        |          | full CHP    |          |           |
|           |        |          | mode.       |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | FL     | Decimal  | The         | Heat-    | Activates |
| CAP_CHPR\ | O_SHAR | fraction | parameter   | to-power | the       |
| (r,dataye |        |          | is only     | ratio of | g         |
| ar,p,lim) |        | \[0,∞);  | taken into  | a CHP    | eneration |
|           |        |          | account     | te       | of output |
|           |        | default  | when the    | chnology | share     |
|           |        | value: 1 | process is  | (fixed / | e         |
|           |        | (only    | defined to  | minimum  | quations, |
|           |        | when     | be of type  | /        | im        |
|           |        | process  | CHP. The    | maximum  | plemented |
|           |        | type is  | defaults    | ratio).  | with      |
|           |        | CHP, for | can be      | If no    |           |
|           |        | lim      | disabled by | ratio    | EQ(l      |
|           |        | =\'UP\') | defining    | e        | )\_OUTSHR |
|           |        |          | any i/e     | quations |           |
|           |        | Default  | value with  | should   |           |
|           |        | i/e: STD | lim=\'N\',  | be       |           |
|           |        |          | which will  | ge       |           |
|           |        |          | eliminate   | nerated, |           |
|           |        |          | the output  | one can  |           |
|           |        |          | share       | define   |           |
|           |        |          | equations.  | any I/E  |           |
|           |        |          |             | value    |           |
|           |        |          |             | with     |           |
|           |        |          |             | li       |           |
|           |        |          |             | m=\'N\'. |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCA    | Years    | Provided    | Lagtime  | Applied   |
| CAP_CLAG\ | P_CLED |          | when there  | of a     | to the    |
| (         |        | \[       | is a delay  | c        | i         |
| r,datayea | NC     | open\];\ | in          | ommodity | nvestment |
| r,p,c,io) | AP_COM | default  | commodity   | after    | variable  |
|           |        | value:   | output      | new      | (         |
|           |        | none     | after       | capacity | VAR_NCAP) |
|           |        |          | co          | is       | in the    |
|           |        | Default  | mmissioning | in       | commodity |
|           |        | i/e: STD | new         | stalled. | balance   |
|           |        |          | capacity.   |          | (EQ(l)    |
|           |        |          | So, if the  |          | \_COMBAL) |
|           |        |          | process is  |          | of the    |
|           |        |          | available   |          | i         |
|           |        |          | in the year |          | nvestment |
|           |        |          | K, the      |          | period or |
|           |        |          | commodity   |          | previous  |
|           |        |          | is produced |          | periods.  |
|           |        |          | during the  |          |           |
|           |        |          | years       |          |           |
|           |        |          | \[K+CLAG,   |          |           |
|           |        |          | K+NCAP_     |          |           |
|           |        |          | TLIFE--1\]. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_CLED | NCA    | Years    | Provided    | Lead     | Applied   |
|           | P_ICOM |          | when a      | time     | to the    |
| (r,data   |        | \[       | commodity   | req      | i         |
| year,p,c) | COE    | open\];\ | must be     | uirement | nvestment |
|           | F_ICOM | default  | available   | for a    | variable  |
|           |        | value: = | prior to    | c        | (         |
|           |        | N        | a           | ommodity | VAR_NCAP) |
|           |        | CAP_ILED | vailability | during   | in the    |
|           |        |          | of a        | cons     | commodity |
|           |        | Default  | process.    | truction | balance   |
|           |        | i/e: STD | So, if the  | (NCA     | (EQ(l)    |
|           |        |          | process is  | P_ICOM), | \_COMBAL) |
|           |        |          | available   | prior to | of the    |
|           |        |          | in the year | the      | i         |
|           |        |          | B(v)        | initial  | nvestment |
|           |        |          | +NC         | avai     | period or |
|           |        |          | AP_ILED--1, | lability | previous  |
|           |        |          | the         | of the   | periods.  |
|           |        |          | commodity   | c        |           |
|           |        |          | is produced | apacity. |           |
|           |        |          | during the  |          |           |
|           |        |          | time span   |          |           |
|           |        |          | \[B(v)+     |          |           |
|           |        |          | ILED--CLED, |          |           |
|           |        |          | B(v)        |          |           |
|           |        |          | +NCAP       |          |           |
|           |        |          | _ILED--1\]. |          |           |
|           |        |          |             |          |           |
|           |        |          | Usually     |          |           |
|           |        |          | used when   |          |           |
|           |        |          | modelling   |          |           |
|           |        |          | the need    |          |           |
|           |        |          | for         |          |           |
|           |        |          | fabrication |          |           |
|           |        |          | of reactor  |          |           |
|           |        |          | fuel the    |          |           |
|           |        |          | period      |          |           |
|           |        |          | before a    |          |           |
|           |        |          | reactor     |          |           |
|           |        |          | goes        |          |           |
|           |        |          | online.     |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_COM  | rpc_c  | C        | Provided    | Emission | Applied   |
|           | apflo, | ommodity | when the    | (or      | to the    |
| (         | rpc    | unit per | consumption | l        | capacity  |
| r,datayea | _conly | capacity | or          | and-use) | variable  |
| r,p,c,io) |        | unit     | production  | of       | (VAR_CAP) |
|           |        |          | of a        | c        | in the    |
|           |        | \[       | commodity   | ommodity | commodity |
|           |        | open\];\ | is tied to  | c        | balance   |
|           |        | default  | the level   | as       | (EQ       |
|           |        | value:   | of the      | sociated | _COMBAL). |
|           |        | none     | installed   | with the |           |
|           |        |          | capacity.   | capacity |           |
|           |        | Default  |             | of a     |           |
|           |        | i/e: STD |             | process  |           |
|           |        |          |             | for each |           |
|           |        |          |             | year     |           |
|           |        |          |             | said     |           |
|           |        |          |             | capacity |           |
|           |        |          |             | exists.  |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_COST | OBJ_   | Monetary | Provided    | In       | Applied   |
|           | ICOST, | unit per | whenever    | vestment | to the    |
| (r,da     | O      | capacity | there is a  | costs of | i         |
| tayear,p) | BJSCC, | unit     | cost        | new      | nvestment |
|           | CST    |          | associated  | i        | variable  |
|           | _INVC, | \[0,∞);\ | with        | nstalled | (         |
|           |        | default  | putting new | capacity | VAR_NCAP) |
|           | C      | value:   | capacity in | a        | when      |
|           | ST_PVP | none     | place.      | ccording | entering  |
|           |        |          |             | to the   | the       |
|           |        | Default  |             | inst     | objective |
|           |        | i/e: STD |             | allation | function  |
|           |        |          |             | year.    | (E        |
|           |        |          |             |          | Q_OBJNV). |
|           |        |          |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_CPX  | CO     | Integer  | Provided    | Defines  | Impacts   |
|           | EF_CPT | number   | when        | a shape  | all       |
| (r,data   |        |          | shaping     | index    | cal       |
| year,prc) |        | Default  | based upon  | for      | culations |
|           |        | value: 0 | age is      | shaping  |           |
|           |        |          | desired.    | the      | that are  |
|           |        | (no      |             | capacity | dependent |
|           |        | shape    | The SHAPE   | transfer |           |
|           |        | curve    | index given | coef     | upon the  |
|           |        | applied) | by NCAP_CPX | ficients | ava       |
|           |        |          | is applied  | by the   | ilability |
|           |        | Default  | to the      | age of   | of        |
|           |        | extrap   | internal    | each     |           |
|           |        | olation: | capacity    | process  | capacity  |
|           |        |          | transfer    | vintage. | (V        |
|           |        | MIG      | parameter   | As a     | AR_NCAP), |
|           |        |          | (COEF_CPT). | result,  | most      |
|           |        |          |             | the      | directly  |
|           |        |          | Note: Shape | capacity | the       |
|           |        |          | index 1 is  | will     | capacity  |
|           |        |          | reserved    | have a   | transfer  |
|           |        |          | for         | survival | (EQ_CPT), |
|           |        |          | constant 1. | rate as  | and       |
|           |        |          |             | a        | capacity  |
|           |        |          |             | function | ava       |
|           |        |          |             | of age.  | ilability |
|           |        |          |             |          | equations |
|           |        |          |             |          |           |
|           |        |          |             |          | (EQ(l)\   |
|           |        |          |             |          | _CAPACT). |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Monetary | Provided    | Cost of  | Applied   |
| CAP_DCOST | _DLAG, | unit per | when there  | dis      | to the    |
|           | COR_   | capacity | are         | mantling | current   |
| (r,dataye | SALVD, | unit     | deco        | a        | capacity  |
| ar,p,cur) | OBJ_   |          | mmissioning | facility | subject   |
|           | DCOST, | \[0,∞);  | costs       | after    | to        |
|           | CST    | default  | associated  | the end  | decomm    |
|           | _DECC, | value:   | with a      | of its   | issioning |
|           |        | none     | process.    | l        | (VA       |
|           | C      |          |             | ifetime. | R_NCAP+NC |
|           | ST_PVP | Default  | Deco        |          | AP_PASTI) |
|           |        | i/e: STD | mmissioning |          | when      |
|           |        |          | of a        |          | entering  |
|           |        |          | process and |          | the       |
|           |        |          | the payment |          | objective |
|           |        |          | of          |          | function  |
|           |        |          | deco        |          | (E        |
|           |        |          | mmissioning |          | Q_OBJNV). |
|           |        |          | costs may   |          |           |
|           |        |          | be delayed  |          |           |
|           |        |          | by a lag    |          |           |
|           |        |          | time        |          |           |
|           |        |          | (           |          |           |
|           |        |          | NCAP_DLAG). |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP_  | Years    | Provided    | Economic | Applied   |
| CAP_DELIF | DLIFE, |          | when the    | lifetime | to the    |
|           | COR_   | (0,∞);\  | timeframe   | of the   | i         |
| (r,da     | SALVD, | default  | for paying  | decommi  | nvestment |
| tayear,p) | DU     | value:   | for         | ssioning | variable  |
|           | R_MAX, | NC       | d           | a        | (         |
|           | OBJ    | AP_DLIFE | ecommission | ctivity. | VAR_NCAP) |
|           | _CRFD, |          | is          |          | when      |
|           | SA     | Default  | different   |          | entering  |
|           | LV_DEC | i/e: STD | from that   |          | the       |
|           |        |          | of the      |          | salvage   |
|           |        |          | actual      |          | portion   |
|           |        |          | decom       |          | of the    |
|           |        |          | missioning. |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ_      |
|           |        |          |             |          | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_DISC | rp_d   | Capacity | Used for    | Size of  | Applied   |
|           | scncap | unit     | lumpy       | capacity | to the    |
| (         |        |          | i           | units    | lumpy     |
| r,datayea |        | \[0,∞);\ | nvestments. | that can | i         |
| r,p,unit) |        | default  |             | be       | nvestment |
|           |        | value:   | Requires    | added.   | integer   |
|           |        | none     | MIP.\       |          | variable  |
|           |        |          | Since       |          | (V        |
|           |        | Default  | inter-/ex   |          | AR_DNCAP) |
|           |        | i/e: MIG | trapolation |          | in the    |
|           |        |          | default is  |          | discrete  |
|           |        |          | MIG, a      |          | i         |
|           |        |          | value must  |          | nvestment |
|           |        |          | be          |          | equation  |
|           |        |          | specified   |          | (EQ       |
|           |        |          | for each    |          | _DSCNCAP) |
|           |        |          | period      |          | to set    |
|           |        |          | desired, if |          | the       |
|           |        |          | no explicit |          | corr      |
|           |        |          | inter-/ex   |          | esponding |
|           |        |          | trapolation |          | standard  |
|           |        |          | option is   |          | i         |
|           |        |          | given.      |          | nvestment |
|           |        |          |             |          | variable  |
|           |        |          |             |          | level     |
|           |        |          |             |          | (V        |
|           |        |          |             |          | AR_NCAP). |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_DLAG | COEF   | Years    | Provided    | Number   | Delay     |
|           | _OCOM, |          | when there  | of years | applied   |
| (r,da     | DU     | \[0,∞);\ | is a lag in | delay    | to a      |
| tayear,p) | R_MAX, | default  | the         | before   | decomm    |
|           | OBJ    | value:   | deco        | decommi  | issioning |
|           | _DLAGC | none     | mmissioning | ssioning | flow      |
|           |        |          | of a        | can      | (VAR_FLO) |
|           |        | Default  | process     | begin    | in the    |
|           |        | i/e: STD | (e.g., to   | after    | balance   |
|           |        |          | allow the   | the      | equation  |
|           |        |          | nuclear     | lifetime | (EQ(l)    |
|           |        |          | core to     | of a     | \_COMBAL) |
|           |        |          | reduce its  | te       | as        |
|           |        |          | radiation). | chnology | pr        |
|           |        |          |             | has      | oduction. |
|           |        |          |             | ended.   |           |
|           |        |          |             |          | Delay     |
|           |        |          |             |          | applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | current   |
|           |        |          |             |          | capacity  |
|           |        |          |             |          | subject   |
|           |        |          |             |          | to        |
|           |        |          |             |          | decomm    |
|           |        |          |             |          | issioning |
|           |        |          |             |          | (VA       |
|           |        |          |             |          | R_NCAP+NC |
|           |        |          |             |          | AP_PASTI) |
|           |        |          |             |          | when      |
|           |        |          |             |          | entering  |
|           |        |          |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJINV, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJFIX, |
|           |        |          |             |          | EQ_       |
|           |        |          |             |          | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Monetary | Provided    | Cost     | Cost      |
| CAP_DLAGC | _DLAG, | unit per | when there  | o        | during    |
|           |        | capacity | is a cost   | ccurring | delay     |
| (r,dataye | OBJ_   | unit     | during any  | during   | applied   |
| ar,p,cur) | DLAGC, |          | lag in the  | the lag  | to the    |
|           | CST    | \[0,∞);\ | deco        | time     | current   |
|           | _DECC, | default  | mmissioning | after    | capacity  |
|           |        | value:   | (e.g.,      | the      | subject   |
|           | C      | none     | security).  | t        | to        |
|           | ST_PVP |          |             | echnical | decomm    |
|           |        | Default  |             | lifetime | issioning |
|           |        | i/e: STD |             | of a     | (VA       |
|           |        |          |             | process  | R_NCAP+NC |
|           |        |          |             | has      | AP_PASTI) |
|           |        |          |             | ended    | when      |
|           |        |          |             | and      | entering  |
|           |        |          |             | before   | the       |
|           |        |          |             | its      | objective |
|           |        |          |             | decommi  | function  |
|           |        |          |             | ssioning | c         |
|           |        |          |             | starts.  | omponents |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJFIX, |
|           |        |          |             |          | EQ_       |
|           |        |          |             |          | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| N         | D      | Years    | Provided    | T        | Decomm    |
| CAP_DLIFE | UR_MAX |          | when a      | echnical | issioning |
|           |        | (0,∞);\  | process has | time for | time      |
| (r,da     |        | default  | a           | dis      | impacting |
| tayear,p) |        | value:   | deco        | mantling | (VA       |
|           |        | none     | mmissioning | a        | R_NCAP+NC |
|           |        |          | phase.      | facility | AP_PASTI) |
|           |        | Default  |             | after    | when      |
|           |        | i/e: STD |             | the end  | entering  |
|           |        |          |             | its      | the       |
|           |        |          |             | t        | objective |
|           |        |          |             | echnical | function  |
|           |        |          |             | l        | c         |
|           |        |          |             | ifetime, | omponents |
|           |        |          |             | plus any | (E        |
|           |        |          |             | lag time | Q_OBJINV, |
|           |        |          |             | (NCA     | EQ_       |
|           |        |          |             | P_DLAG). | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| N         | G_     | Percent  | Provided if | Te       | Discount  |
| CAP_DRATE | DRATE, |          | the cost of | chnology | rate      |
|           | COR_   | (0,∞);\  | borrowing   | specific | applied   |
| (r,da     | SALVI, | default  | for a       | discount | to        |
| tayear,p) | COR    | value:   | process is  | rate.    | in        |
|           | _SALVD | G_DRATE  | different   |          | vestments |
|           |        |          | from the    |          | (VA       |
|           |        | Default  | standard    |          | R_NCAP+NC |
|           |        | i/e: STD | discount    |          | AP_PASTI) |
|           |        |          | rate.       |          | when      |
|           |        |          |             |          | entering  |
|           |        |          |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJINV, |
|           |        |          |             |          | EQ_       |
|           |        |          |             |          | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP_  | years    | Provided    | Economic | Economic  |
| CAP_ELIFE | TLIFE, |          | only when   | lifetime | lifetime  |
|           | COR_   | (0,∞);\  | the         | of a     | of a      |
| (r,da     | SALVI, | default  | economic    | process. | process   |
| tayear,p) | O      | value:   | lifetime    |          | when      |
|           | BJ_CRF | NC       | differs     |          | costing   |
|           |        | AP_TLIFE | from the    |          | i         |
|           |        |          | technical   |          | nvestment |
|           |        | Default  | lifetime    |          | (VA       |
|           |        | i/e: STD | (N          |          | R_NCAP+NC |
|           |        |          | CAP_TLIFE). |          | AP_PASTI) |
|           |        |          |             |          | or        |
|           |        |          |             |          | capacity  |
|           |        |          |             |          | in the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJINV, |
|           |        |          |             |          | EQ        |
|           |        |          |             |          | _OBJSALV, |
|           |        |          |             |          | EQ        |
|           |        |          |             |          | _OBJFIX). |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_FDR\ | NCA    | Decimal  | Provided    | Defines  | Affects   |
| (r,data   | P_COST | fraction | when the    | an       | the       |
| year,prc) |        | (0,∞);\  | effect of   | annual   | salvage   |
|           |        | default  | functional  | rate of  | value     |
|           |        | va       | d           | ad       | coe       |
|           |        | lue:none | epreciation | ditional | fficients |
|           |        |          | is          | depr     | in        |
|           |        | Default  | considered  | eciation | E         |
|           |        | i/e: STD | significant | in the   | Q_OBJSALV |
|           |        |          | to justify  | salvage  |           |
|           |        |          | accelerated | value.   |           |
|           |        |          | decrease in |          |           |
|           |        |          | salvage     |          |           |
|           |        |          | value.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_FOM  | OB     | Monetary | Provided    | Fixed    | Fixed     |
|           | J_FOM, | unit per | when there  | o        | operating |
| (r,dataye | CST_   | capacity | is a fixed  | perating | and       |
| ar,p,cur) | FIXC,\ | unit     | cost        | and      | ma        |
|           | C      |          | associated  | mai      | intenance |
|           | ST_PVP | \[0,∞);\ | with the    | ntenance | costs     |
|           |        | default  | installed   | cost per | a         |
|           |        | value:   | capacity.   | unit of  | ssociated |
|           |        | none     |             | capacity | with      |
|           |        |          |             | a        | total     |
|           |        | Default  |             | ccording | installed |
|           |        | i/e: STD |             | to the   | capacity  |
|           |        |          |             | inst     | (VA       |
|           |        |          |             | allation | R_NCAP+NC |
|           |        |          |             | year.    | AP_PASTI) |
|           |        |          |             |          | when      |
|           |        |          |             |          | entering  |
|           |        |          |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJFIX). |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_FOMM | NCA    | Integer  | Provided    | Period   | *{See     |
|           | P_FOM, | number   | when        | s        | Related   |
| (r,da     | MULTI  |          | shaping     | ensitive | Par       |
| tayear,p) |        | Default  | based upon  | mu       | ameters}* |
|           |        | value: 0 | the period  | ltiplier |           |
|           |        | (no      | is desired. | curve    |           |
|           |        | mu       |             | (MULTI)  |           |
|           |        | ltiplier | Note:       | applied  |           |
|           |        | curve    | Multiplier  | to the   |           |
|           |        | applied) | index 1 is  | fixed    |           |
|           |        |          | reserved    | o        |           |
|           |        | Default  | for         | perating |           |
|           |        | i/e: MIG | constant 1. | and      |           |
|           |        |          |             | mai      |           |
|           |        |          |             | ntenance |           |
|           |        |          |             | costs    |           |
|           |        |          |             | (NC      |           |
|           |        |          |             | AP_FOM). |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_FOMX | NCA    | Integer  | Provided    | A        | *{See     |
|           | P_FOM, | number   | when        | ge-based | Related   |
| (r,da     | SHAPE  |          | shaping     | shaping  | Par       |
| tayear,p) |        | Default  | based upon  | curve    | ameters}* |
|           |        | value: 0 | age is      | (SHAPE)  |           |
|           |        | (no      | desired.    | to be    |           |
|           |        | shape    |             | applied  |           |
|           |        | curve    | Note: Shape | to the   |           |
|           |        | applied) | index 1 is  | fixed    |           |
|           |        |          | reserved    | o        |           |
|           |        | Default  | for         | perating |           |
|           |        | i/e: MIG | constant 1. | and      |           |
|           |        |          |             | mai      |           |
|           |        |          |             | ntenance |           |
|           |        |          |             | cost.    |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_FSUB | OB     | Monetary | Provided    | Subsidy  | Fixed     |
|           | J_FSB, | unit per | when there  | per unit | subsidy   |
| (r,dataye | CST    | capacity | is a        | of       | a         |
| ar,p,cur) | _FIXX, | unit     | subsidy for | i        | ssociated |
|           |        |          | associated  | nstalled | with      |
|           | C      | \[0,∞);\ | with the    | c        | total     |
|           | ST_PVP | default  | level of    | apacity. | installed |
|           |        | value:   | installed   |          | capacity  |
|           |        | none     | capacity.   |          | (VA       |
|           |        |          |             |          | R_NCAP+NC |
|           |        | Default  |             |          | AP_PASTI) |
|           |        | i/e: STD |             |          | when      |
|           |        |          |             |          | entering  |
|           |        |          |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | component |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJFIX) |
|           |        |          |             |          | with a    |
|           |        |          |             |          | minus     |
|           |        |          |             |          | sign.     |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Integer  | Provided    | Period   | *{See     |
| CAP_FSUBM | _FSUB, | number   | when        | s        | Related   |
|           | MULTI  |          | shaping     | ensitive | Par       |
| (r,da     |        | Default  | based upon  | mu       | ameters}* |
| tayear,p) |        | value: 0 | the period  | ltiplier |           |
|           |        | (no      | is desired. | curve    |           |
|           |        | mu       |             | (MULTI)  |           |
|           |        | ltiplier | Note:       | applied  |           |
|           |        | curve    | Multiplier  | to the   |           |
|           |        | applied) | index 1 is  | subsidy  |           |
|           |        |          | reserved    | (NCA     |           |
|           |        | Default  | for         | P_FSUB). |           |
|           |        | i/e: MIG | constant 1. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Integer  | Provided    | A        | *{See     |
| CAP_FSUBX | _FSUB, | number   | when        | ge-based | Related   |
|           | SHAPE  |          | shaping     | shaping  | Par       |
| (r,da     |        | Default  | based upon  | curve    | ameters}* |
| tayear,p) |        | value: 0 | age is      | (SHAPE)  |           |
|           |        | (no      | desired.\   | to be    |           |
|           |        | shape    | Note: Shape | applied  |           |
|           |        | curve    | index 1 is  | to the   |           |
|           |        | applied) | reserved    | fixed    |           |
|           |        |          | for         | subsidy  |           |
|           |        | Default  | constant 1. | (NCA     |           |
|           |        | i/e: MIG |             | P_FSUB). |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_FTAX | OB     | monetary | Provided    | Tax per  | Fixed     |
|           | J_FTX, | unit per | when there  | unit of  | subsidy   |
| (r,dataye | CST    | capacity | is a fixed  | i        | a         |
| ar,p,cur) | _FIXX, | unit     | tax based   | nstalled | ssociated |
|           |        |          | upon the    | c        | with      |
|           | C      | \[       | level of    | apacity. | total     |
|           | ST_PVP | open\];\ | the         |          | installed |
|           |        | default  | installed   |          | capacity  |
|           |        | value:   | capacity.   |          | (VA       |
|           |        | none     |             |          | R_NCAP+NC |
|           |        |          |             |          | AP_PASTI) |
|           |        | Default  |             |          | when      |
|           |        | i/e: STD |             |          | entering  |
|           |        |          |             |          | the       |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | c         |
|           |        |          |             |          | omponents |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | _OBJFIX). |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Integer  | Provided    | Period   | *{See     |
| CAP_FTAXM | _FTAX, | number   | when        | s        | Related   |
|           | MULTI  |          | shaping     | ensitive | Par       |
| (r,da     |        | Default  | based upon  | mu       | ameters}* |
| tayear,p) |        | value: 0 | the period  | ltiplier |           |
|           |        | (no      | is desired. | curve    |           |
|           |        | mu       |             | (MULTI)  |           |
|           |        | ltiplier | Note:       | applied  |           |
|           |        | curve    | Multiplier  | to the   |           |
|           |        | applied) | index 1 is  | tax      |           |
|           |        |          | reserved    | (NCA     |           |
|           |        | Default  | for         | P_FTAX). |           |
|           |        | i/e: MIG | constant 1. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Integer  | Provided    | A        | *{See     |
| CAP_FTAXX | _FTAX, | number   | when        | ge-based | Related   |
|           | SHAPE  |          | shaping     | shaping  | Par       |
| (r,da     |        | Default  | based upon  | curve    | ameters}* |
| tayear,p) |        | value: 0 | age is      | (SHAPE)  |           |
|           |        | (no      | desired.    | to be    |           |
|           |        | shape    |             | applied  |           |
|           |        | curve    | Note: Shape | to the   |           |
|           |        | applied) | index 1 is  | fixed    |           |
|           |        |          | reserved    | tax      |           |
|           |        | Default  | for         | (NCA     |           |
|           |        | i/e: MIG | constant 1. | P_FTAX). |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_ICOM | NCAP   | C        | Provided    | Amount   | Applied   |
|           | _CLED, | ommodity | when a      | of       | to the    |
| (r,data   | rpc_c  | unit per | commodity   | c        | i         |
| year,p,c) | apflo, | capacity | is needed   | ommodity | nvestment |
|           | rpc    | unit     | in the      | (c)      | variable  |
|           | _conly |          | period in   | required | (         |
|           |        | \[       | which the   | for the  | VAR_NCAP) |
|           |        | open\];\ | new         | cons     | in the    |
|           |        | default  | capacity is | truction | ap        |
|           |        | value:   | to be       | of new   | propriate |
|           |        | none     | available,  | c        | commodity |
|           |        |          | or before   | apacity. | co        |
|           |        | Default  | NCAP_CLED.  |          | nstraints |
|           |        | i/e: STD |             |          | (EQ(l)    |
|           |        |          | If          |          | \_COMBAL) |
|           |        |          | NCAP_CLED   |          | as part   |
|           |        |          | is          |          | of        |
|           |        |          | provided,   |          | con       |
|           |        |          | the         |          | sumption. |
|           |        |          | commodity   |          |           |
|           |        |          | is required |          |           |
|           |        |          | during the  |          |           |
|           |        |          | years       |          |           |
|           |        |          | \[B(v)+NCAP |          |           |
|           |        |          | _CLED,B(v)+ |          |           |
|           |        |          | NCAP_ILED-N |          |           |
|           |        |          | CAP_CLED\]. |          |           |
|           |        |          | If this     |          |           |
|           |        |          | time spans  |          |           |
|           |        |          | more than   |          |           |
|           |        |          | one period, |          |           |
|           |        |          | the         |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | flow is     |          |           |
|           |        |          | split up    |          |           |
|           |        |          | pro         |          |           |
|           |        |          | portion­ally |          |           |
|           |        |          | between the |          |           |
|           |        |          | periods.    |          |           |
|           |        |          |             |          |           |
|           |        |          | For the     |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | balance the |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | requirement |          |           |
|           |        |          | in a period |          |           |
|           |        |          | is          |          |           |
|           |        |          | converted   |          |           |
|           |        |          | to an       |          |           |
|           |        |          | average     |          |           |
|           |        |          | annual      |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | flow for    |          |           |
|           |        |          | the entire  |          |           |
|           |        |          | period,     |          |           |
|           |        |          | although    |          |           |
|           |        |          | the         |          |           |
|           |        |          | c           |          |           |
|           |        |          | onstruction |          |           |
|           |        |          | may take    |          |           |
|           |        |          | place only  |          |           |
|           |        |          | for a few   |          |           |
|           |        |          | years of    |          |           |
|           |        |          | the period. |          |           |
|           |        |          |             |          |           |
|           |        |          | Negative    |          |           |
|           |        |          | value       |          |           |
|           |        |          | describes   |          |           |
|           |        |          | production  |          |           |
|           |        |          | (e.g.       |          |           |
|           |        |          | emissions)  |          |           |
|           |        |          | at the time |          |           |
|           |        |          | of a new    |          |           |
|           |        |          | investment. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_ILED | NCAP   | Years    | Provided    | Lead     | Applied   |
|           | _ICOM, |          | when there  | time     | to the    |
| (r,t,p)   |        | \[       | is a delay  | between  | i         |
|           | NCAP   | open\];\ | between     | in       | nvestment |
|           | _COST, | default  | when the    | vestment | variable  |
|           |        | value:   | investment  | decision | (         |
|           | COE    | none     | decision    | and      | VAR_NCAP) |
|           | F_CPT, |          | occurs and  | actual   | balance   |
|           | COEF   | Default  | when the    | avai     | co        |
|           | _ICOM, | i/e: STD | capacity    | lability | nstraints |
|           | D      |          | (new        | of new   | (EQ(l)    |
|           | UR_MAX |          | capacity or | capacity | \_COMBAL) |
|           |        |          | past        | (=       | as part   |
|           |        |          | investment) | cons     | of        |
|           |        |          | is          | truction | con       |
|           |        |          | initially   | time).   | sumption, |
|           |        |          | available.  |          | if there  |
|           |        |          | If          |          | is an     |
|           |        |          | NC          |          | a         |
|           |        |          | AP_ILED\>0, |          | ssociated |
|           |        |          | the         |          | flow      |
|           |        |          | investment  |          | (NC       |
|           |        |          | decision is |          | AP_ICOM). |
|           |        |          | assumed to  |          |           |
|           |        |          | occur at    |          | Used as   |
|           |        |          | B(v) and    |          | to        |
|           |        |          | the         |          | di        |
|           |        |          | capacity    |          | stinguish |
|           |        |          | becomes     |          | between   |
|           |        |          | available   |          | small and |
|           |        |          | at          |          | large     |
|           |        |          | B(v)        |          | in        |
|           |        |          | +NCAP-ILED. |          | vestments |
|           |        |          | If          |          | (         |
|           |        |          | NC          |          | VAR_NCAP) |
|           |        |          | AP_ILED\<0, |          | and thus  |
|           |        |          | the         |          | i         |
|           |        |          | investment  |          | nfluences |
|           |        |          | decision is |          | the way   |
|           |        |          | assumed to  |          | the       |
|           |        |          | occur at    |          | i         |
|           |        |          | B(v         |          | nvestment |
|           |        |          | )-NCAP_ILED |          | and fixed |
|           |        |          | and the     |          | costs are |
|           |        |          | capacity    |          | treated   |
|           |        |          | becomes     |          | in the    |
|           |        |          | available   |          | objective |
|           |        |          | at B(v).    |          | function  |
|           |        |          | Causes an   |          | (E        |
|           |        |          | IDC         |          | Q_OBJINV, |
|           |        |          | overhead in |          | E         |
|           |        |          | the         |          | Q_OBJFIX, |
|           |        |          | investment  |          | EQ_       |
|           |        |          | costs       |          | OBJSALV). |
|           |        |          | accounting. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP_  | Decimal  | Provided    | Unit     | Applied   |
| CAP_ISPCT | ISUB,\ | fraction | when        | in       | to the    |
|           | OBJ    |          | defining an | vestment | i         |
| (r,da     | _ISUB, | (−∞,∞);\ | investment  | subsidy  | nvestment |
| tayear,p) | CS     | default  | subsidy in  | as a     | variable  |
|           | T_INVX | value:   | proportion  | fraction | (         |
|           |        | none     | to the      | of unit  | VAR_NCAP) |
|           |        |          | investment  | in       | when      |
|           |        | Default  | cost.\      | vestment | entering  |
|           |        | i/e: STD | Requires    | costs,   | the       |
|           |        |          | that        | in the   | objective |
|           |        |          | NCAP_COST   | same     | function  |
|           |        |          | is defined. | currency | (         |
|           |        |          |             | unit,    | EQ_OBJNV) |
|           |        |          |             | per unit | with a    |
|           |        |          |             | of new   | minus     |
|           |        |          |             | c        | sign.     |
|           |        |          |             | apacity. |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_ISUB | OBJ    | monetary | Provided    | Subsidy  | Applied   |
|           | _ISUB, | unit per | when there  | per unit | to the    |
| (r,dataye | O      | capacity | is a        | of new   | i         |
| ar,p,cur) | BJSCC, | unit     | subsidy for | i        | nvestment |
|           | CST    |          | new         | nstalled | variable  |
|           | _INVX, | \[0,∞);\ | investments | c        | (         |
|           | CST    | default  | in a        | apacity. | VAR_NCAP) |
|           | _SALV, | value:   | period.     |          | when      |
|           |        | none     |             |          | entering  |
|           | C      |          |             |          | the       |
|           | ST_PVP | Default  |             |          | objective |
|           |        | i/e: STD |             |          | function  |
|           |        |          |             |          | (         |
|           |        |          |             |          | EQ_OBJNV) |
|           |        |          |             |          | with a    |
|           |        |          |             |          | minus     |
|           |        |          |             |          | sign.     |
|           |        |          |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_ITAX | OBJ    | monetary | Provided    | Tax per  | Applied   |
|           | _ITAX, | unit per | when there  | unit of  | to the    |
| (r,dataye | O      | capacity | is a tax    | new      | i         |
| ar,p,cur) | BJSCC, | unit     | associated  | i        | nvestment |
|           | CST    |          | with new    | nstalled | variable  |
|           | _INVX, | \[0,∞);\ | investments | capacity | (         |
|           | CST    | default  | in a        |          | VAR_NCAP) |
|           | _SALV, | value:   | period.     |          | when      |
|           |        | none     |             |          | entering  |
|           | C      |          |             |          | the       |
|           | ST_PVP | Default  |             |          | objective |
|           |        | i/e: STD |             |          | function  |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJNV). |
|           |        |          |             |          |           |
|           |        |          |             |          | May       |
|           |        |          |             |          | appear in |
|           |        |          |             |          | user      |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | (EQ_UC\*) |
|           |        |          |             |          | if        |
|           |        |          |             |          | specified |
|           |        |          |             |          | in        |
|           |        |          |             |          | UC_NAME.  |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | C        | Provided    | Amount   | Applied   |
| CAP_OCOM\ | _VALU, | ommodity | when there  | of       | to the    |
| (r,data   | rpc_c  | unit per | is a        | c        | i         |
| year,p,c) | apflo, | capacity | commodity   | ommodity | nvestment |
|           | rpc    | unit     | release     | c per    | variable  |
|           | _conly |          | associated  | unit of  | (         |
|           |        | \[       | with the    | capacity | VAR_NCAP) |
|           |        | open\];\ | decom       | released | in the    |
|           |        | default  | missioning. | during   | ap        |
|           |        | value:   |             | the      | propriate |
|           |        | none     | The year    | dis      | commodity |
|           |        |          | index of    | mantling | co        |
|           |        | Default  | the         | of a     | nstraints |
|           |        | i/e: STD | parameter   | process. | (EQ(l)    |
|           |        |          | corresponds |          | \_COMBAL) |
|           |        |          | to the      |          | as part   |
|           |        |          | vintage     |          | of        |
|           |        |          | year.       |          | p         |
|           |        |          |             |          | roduction |
|           |        |          | If the      |          | in the    |
|           |        |          | deco        |          | ap        |
|           |        |          | mmissioning |          | propriate |
|           |        |          | time        |          | period.   |
|           |        |          | (           |          |           |
|           |        |          | NCAP_DLIFE) |          |           |
|           |        |          | falls in    |          |           |
|           |        |          | more than   |          |           |
|           |        |          | one period, |          |           |
|           |        |          | is split up |          |           |
|           |        |          | pro         |          |           |
|           |        |          | portionally |          |           |
|           |        |          | among the   |          |           |
|           |        |          | periods.    |          |           |
|           |        |          |             |          |           |
|           |        |          | For the     |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | balance the |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | release in  |          |           |
|           |        |          | a period is |          |           |
|           |        |          | converted   |          |           |
|           |        |          | to an       |          |           |
|           |        |          | average     |          |           |
|           |        |          | annual      |          |           |
|           |        |          | commodity   |          |           |
|           |        |          | flow for    |          |           |
|           |        |          | the entire  |          |           |
|           |        |          | period,     |          |           |
|           |        |          | although    |          |           |
|           |        |          | the         |          |           |
|           |        |          | dismantling |          |           |
|           |        |          | may take    |          |           |
|           |        |          | place only  |          |           |
|           |        |          | for a few   |          |           |
|           |        |          | years of    |          |           |
|           |        |          | the period. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NC        | NCAP   | Years    | Requires    | Maximum  | EQL_SCAP  |
| AP_OLIFE\ | _TLIFE |          | that early  | o        |           |
| (r,da     |        | (0,∞);\  | retirements | perating |           |
| tayear,p) |        | default  | are enabled | lifetime |           |
|           |        | value:   | and the     | of a     |           |
|           |        | none     | process is  | process, |           |
|           |        |          | vintaged.   | in terms |           |
|           |        | Default  |             | of       |           |
|           |        | i/e: STD |             | f        |           |
|           |        |          |             | ull-load |           |
|           |        |          |             | years.   |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP_  | capacity | Past        | In       | EQ(l      |
| CAP_PASTI | PASTY, | unit     | investment  | vestment | )\_COMBAL |
|           | OBJ_   |          | can also be | in new   |           |
| (r,pa     | PASTI, | \[0,∞);\ | specified   | capacity | EQ_CPT    |
| styear,p) | PAR_   | default  | for         | made     |           |
|           | PASTI, | value:   | milestone   | before   | E         |
|           |        | none     | years, e.g. | the      | Q_OBJINV, |
|           | PRC    |          | if the      | b        | EQ        |
|           | _RESID | No i/e   | milestone   | eginning | _OBJSALV, |
|           |        |          | year is a   | of the   | EQ_OBJFIX |
|           |        |          | historic    | model    |           |
|           |        |          | year, so    | horizon  |           |
|           |        |          | that        | (in the  |           |
|           |        |          | capacity    | year     |           |
|           |        |          | additions   | s        |           |
|           |        |          | are known   | pecified |           |
|           |        |          | or if       | by       |           |
|           |        |          | planned     | pa       |           |
|           |        |          | future      | styear). |           |
|           |        |          | investments |          |           |
|           |        |          | are already |          |           |
|           |        |          | known.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP   | Years    | Provided to | Number   | *{See     |
| CAP_PASTY | _PASTI |          | spread a    | of years | NCA       |
|           |        | \[1      | single past | to go    | P_PASTI}* |
| (r,pa     |        | ,999\];\ | investment  | back to  |           |
| styear,p) |        | default  | (           | c        |           |
|           |        | value:   | NCAP_PASTI) | alculate |           |
|           |        | none     | back over   | a linear |           |
|           |        |          | several     | build-up |           |
|           |        | No i/e   | years       | of past  |           |
|           |        |          | (e.g., cars | inv      |           |
|           |        |          | in the      | estments |           |
|           |        |          | period      |          |           |
|           |        |          | before the  |          |           |
|           |        |          | 1^st^       |          |           |
|           |        |          | milestoneyr |          |           |
|           |        |          | were bought |          |           |
|           |        |          | over the    |          |           |
|           |        |          | previous 15 |          |           |
|           |        |          | years).     |          |           |
|           |        |          |             |          |           |
|           |        |          | If overlaps |          |           |
|           |        |          | with other  |          |           |
|           |        |          | past        |          |           |
|           |        |          | i           |          |           |
|           |        |          | nvestments, |          |           |
|           |        |          | the         |          |           |
|           |        |          | capacity    |          |           |
|           |        |          | values are  |          |           |
|           |        |          | added.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| N         | com    | Decimal  | If the      | Fraction | Applied   |
| CAP_PKCNT | _peak, | fraction | indicator   | of       | to        |
|           | com    |          | PRC_PKAF is | capacity | in        |
| (r,data   | _pkts, | \        | specified,  | that can | vestments |
| year,p,s) | prc    | [0,1\];\ | the         | co       | in        |
|           | _pkaf, | default  | NCAP_PKCNT  | ntribute | capacity  |
|           | pr     | value: 1 | is set      | to       | (         |
|           | c_pkno |          | equal to    | peaking  | VAR_NCAP, |
|           |        | Default  | the         | eq       | NC        |
|           |        | i/e: STD | ava         | uations. | AP_PASTI) |
|           |        |          | ilabilities |          | in the    |
|           |        |          | NCAP_AF.    |          | peaking   |
|           |        |          |             |          | c         |
|           |        |          | Direct      |          | onstraint |
|           |        |          | i           |          | (         |
|           |        |          | nheritance. |          | EQ_PEAK). |
|           |        |          |             |          |           |
|           |        |          | Weighted    |          |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_SEMI | NCA    | Capacity | Upper bound | Semi-co  | Applied   |
| (r,da     | P_DISC | unit     | for the     | ntinuous | to the    |
| tayear,p) |        |          | capacity    | new      | semi-c    |
|           |        | (0,∞);   | must be     | c        | ontinuous |
|           |        |          | defined by  | apacity, | i         |
|           |        | default  | NCAP_BND;   | lower    | nvestment |
|           |        | value:   | if not      | bound.   | variable  |
|           |        | none     | defined,    | (See     | VAR_SNCAP |
|           |        |          | assumed to  | Section  |           |
|           |        | Default  | be equal to | 5.9)     | in the    |
|           |        | i/e: MIG | the lower   |          | discrete  |
|           |        |          | bound.      |          | i         |
|           |        |          |             |          | nvestment |
|           |        |          | Requires    |          | equation  |
|           |        |          | MIP.        |          | E         |
|           |        |          |             |          | Q_DSCNCAP |
+-----------+--------+----------+-------------+----------+-----------+
| NC        | PR     | Year     | NCAP_S      | Start    | Affects   |
| AP_START\ | C_NOFF |          | TART(r,p)=y | year for | the       |
| (r,p)     |        | \[1      |             | new      | ava       |
|           |        | 000,∞);\ | is          | inv      | ilability |
|           |        | default  | equivalent  | estments | of        |
|           |        | value:   | to          |          | i         |
|           |        | none     |             |          | nvestment |
|           |        |          | P           |          | variable  |
|           |        |          | RC_NOFF(r,p |          | (         |
|           |        |          | ,BOH,y--1). |          | VAR_NCAP) |
+-----------+--------+----------+-------------+----------+-----------+
| N         | NCAP_  | Years    | Expected    | T        | Impacts   |
| CAP_TLIFE | ELIFE, |          | for all     | echnical | all       |
|           | COE    | (0,∞);\  | t           | lifetime | cal       |
| (r,da     | F_CPT, | default  | echnologies | of a     | culations |
| tayear,p) | COEF   | value:   | that have   | process. | that are  |
|           | _RPTI, | G_TLIFE  | investment  |          | dependent |
|           | D      |          | costs.\     |          | upon the  |
|           | UR_MAX | Default  | Values      |          | ava       |
|           |        | i/e: STD | below 0.5   |          | ilability |
|           |        |          | cannot be   |          | of        |
|           |        |          | well        |          | in        |
|           |        |          | accounted   |          | vestments |
|           |        |          | in the      |          | (         |
|           |        |          | objective   |          | VAR_NCAP) |
|           |        |          | function,   |          | including |
|           |        |          | and should  |          | capacity  |
|           |        |          | thus be     |          | transfer  |
|           |        |          | avoided     |          | (EQ_CPT), |
|           |        |          | (they are   |          | commodity |
|           |        |          | au          |          | flow      |
|           |        |          | tomatically |          | (EQ(l)\   |
|           |        |          | resetted to |          | _COMBAL), |
|           |        |          | 1).         |          | costs     |
|           |        |          |             |          | (E        |
|           |        |          |             |          | Q_OBJINV, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJFIX, |
|           |        |          |             |          | E         |
|           |        |          |             |          | Q_OBJVAR, |
|           |        |          |             |          | EQ_       |
|           |        |          |             |          | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| NCAP_VALU | NCA    | Monetary | Provided    | Value of | Applied   |
|           | P_OCOM | unit /   | when a      | a        | to the    |
| (r        |        | c        | released    | c        | i         |
| ,datayear |        | ommodity | commodity   | ommodity | nvestment |
| ,p,c,cur) |        | unit     | has a       | released | related   |
|           |        |          | value.      | at       | (         |
|           |        | \[0,∞);\ |             | decommi  | VAR_NCAP, |
|           |        | default  |             | ssioning | NC        |
|           |        | value:   |             | (NCA     | AP_PASTI) |
|           |        | none     |             | P_OCOM). | release   |
|           |        |          |             |          | flow at   |
|           |        | Default  |             |          | decomm    |
|           |        | i/e: STD |             |          | issioning |
|           |        |          |             |          | in the    |
|           |        |          |             |          | objective |
|           |        |          |             |          | function  |
|           |        |          |             |          | (EQ_      |
|           |        |          |             |          | OBJSALV). |
+-----------+--------+----------+-------------+----------+-----------+
| P         | PRC_C  | C        | Only        | 1\)      | Applied   |
| RC_ACTFLO | APACT, | ommodity | (rarely)    | Co       | to the    |
|           | prc_a  | unit /   | provided    | nversion | primary   |
| (r,datay  | ctunt, | activity | when either | factor   | commodity |
| ear,p,cg) | pr     | unit     | the         | from     | (prc_pcg) |
|           | c_spg, |          | activity    | units of | flow      |
|           | rp     | (0,∞);\  | and flow    | activity | variables |
|           | c_aire | default  | variables   | to units | (VAR_FLO, |
|           |        | value: 1 | of a        | of those | VAR_IRE)  |
|           |        |          | process are | flow     | to relate |
|           |        | Default  | in          | v        | overall   |
|           |        | i/e: STD | different   | ariables | activity  |
|           |        |          | units, or   | that     | (VAR_ACT  |
|           |        |          | if there is | define   | in        |
|           |        |          | a           | the      | EQ        |
|           |        |          | conversion  | activity | _ACTFLO). |
|           |        |          | efficiency  | (primary |           |
|           |        |          | between the | c        | When the  |
|           |        |          | activity    | ommodity | Reduction |
|           |        |          | and the     | group),  | algorithm |
|           |        |          | flow(s) in  |          | activated |
|           |        |          | the PCG.    | or,      | it is     |
|           |        |          |             |          | applied   |
|           |        |          | The group   | 2\)      | to the    |
|           |        |          | (cg) can be | Co       | activity  |
|           |        |          | the whole   | nversion | variable  |
|           |        |          | PCG or any  | mu       | (VAR_ACT) |
|           |        |          | individual  | ltiplier | in those  |
|           |        |          | commodity   | repr     | cases     |
|           |        |          | in the PCG, | esenting | where the |
|           |        |          | or \'ACT\'  | the      | flow      |
|           |        |          | (=PCG).     | amount   | variable  |
|           |        |          |             | of       | (VAR_FLO) |
|           |        |          |             | flow(s)  | can be    |
|           |        |          |             | in the   | replaced  |
|           |        |          |             | cg per 1 | by the    |
|           |        |          |             | unit of  | activity  |
|           |        |          |             | a        | variable  |
|           |        |          |             | ctivity. | (e.g. the |
|           |        |          |             |          | activity  |
|           |        |          |             |          | is        |
|           |        |          |             |          | defined   |
|           |        |          |             |          | by one    |
|           |        |          |             |          | commodity |
|           |        |          |             |          | flow).    |
+-----------+--------+----------+-------------+----------+-----------+
| P         | PRC_A  | Activity |             | Co       | Applied   |
| RC_CAPACT | CTFLO, | unit /   |             | nversion | along     |
|           | PRC_   | capacity |             | factor   | with the  |
| (r,p)     | ACTUNT | unit     |             | from     | ava       |
|           |        |          |             | capacity | ilability |
|           |        | (0,∞);\  |             | unit to  | factor    |
|           |        | default  |             | activity | (NCAP_AF) |
|           |        | value: 1 |             | unit     | to the    |
|           |        |          |             | assuming | i         |
|           |        | Default  |             | that the | nvestment |
|           |        | i/e:     |             | capacity | (V        |
|           |        | none     |             | is used  | AR_NCAP + |
|           |        |          |             | for one  | NC        |
|           |        |          |             | year.    | AP_PASTI) |
|           |        |          |             |          | in the    |
|           |        |          |             |          | ut        |
|           |        |          |             |          | ilization |
|           |        |          |             |          | equations |
|           |        |          |             |          | (EQ(l)    |
|           |        |          |             |          | \_CAPACT, |
|           |        |          |             |          | EQ(l)\    |
|           |        |          |             |          | _CAFLAC). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | i         |
|           |        |          |             |          | nvestment |
|           |        |          |             |          | (V        |
|           |        |          |             |          | AR_NCAP + |
|           |        |          |             |          | NC        |
|           |        |          |             |          | AP_PASTI) |
|           |        |          |             |          | in the    |
|           |        |          |             |          | peak      |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | (         |
|           |        |          |             |          | EQ_PEAK). |
|           |        |          |             |          |           |
|           |        |          |             |          | Applied   |
|           |        |          |             |          | to the    |
|           |        |          |             |          | i         |
|           |        |          |             |          | nvestment |
|           |        |          |             |          | (V        |
|           |        |          |             |          | AR_NCAP + |
|           |        |          |             |          | NC        |
|           |        |          |             |          | AP_PASTI) |
|           |        |          |             |          | in the    |
|           |        |          |             |          | capacity  |
|           |        |          |             |          | ut        |
|           |        |          |             |          | ilization |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | for CHP   |
|           |        |          |             |          | plants    |
|           |        |          |             |          | (E        |
|           |        |          |             |          | CT_AFCHP) |
|           |        |          |             |          | and peak  |
|           |        |          |             |          | c         |
|           |        |          |             |          | onstraint |
|           |        |          |             |          | in the    |
|           |        |          |             |          | IER       |
|           |        |          |             |          | extension |
|           |        |          |             |          | (see Part |
|           |        |          |             |          | III).     |
+-----------+--------+----------+-------------+----------+-----------+
| PRC_GMAP\ | GR_    | Dimen    | Provided    | User     | *None*    |
| (r,       | GENMAP | sionless | when        | -defined |           |
| prc,item) |        |          | process     | grouping |           |
|           |        | (∞,∞);\  | groupings   | of       |           |
|           |        | default  | are needed  | p        |           |
|           |        | value:   | for custom  | rocesses |           |
|           |        | none     | processing  | by group |           |
|           |        |          | e.g. in a   | i        |           |
|           |        | Default  | TIMES code  | ndicator |           |
|           |        | i/e:     | extension.  | *        |           |
|           |        | none     |             | *item**. |           |
+-----------+--------+----------+-------------+----------+-----------+
| PRC_MARK  | FL     | Decimal  | Combined    | Process  | EQ(l      |
| (r,dat    | O_MARK | fraction | limit on    | gr       | )\_FLOMRK |
| ayear,p,i |        |          | commodity   | oup-wise |           |
| tem,c,bd) |        | \[       | production  | market   | V         |
|           |        | open\];\ | is derived  | share,   | AR_COMPRD |
|           |        | default  | as the sum  | which    |           |
|           |        | value:   | of the      | defines  |           |
|           |        | none     | proce       | a        |           |
|           |        |          | ss-specific | co       |           |
|           |        | Default  | productions | nstraint |           |
|           |        | i/e: 11  | multiplied  | for the  |           |
|           |        |          | by the      | combined |           |
|           |        |          | inverse     | market   |           |
|           |        |          | values of   | share of |           |
|           |        |          | PRC_MARK.   | multiple |           |
|           |        |          | The         | p        |           |
|           |        |          | constraint  | rocesses |           |
|           |        |          | is applied  | in the   |           |
|           |        |          | to the      | total    |           |
|           |        |          | annual      | c        |           |
|           |        |          | production  | ommodity |           |
|           |        |          | of          | pro      |           |
|           |        |          | commodity.  | duction. |           |
|           |        |          |             |          |           |
|           |        |          | Item can be |          |           |
|           |        |          | a any       |          |           |
|           |        |          | desired     |          |           |
|           |        |          | label       |          |           |
|           |        |          | identifying |          |           |
|           |        |          | the group.  |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| P         | PR     | Dimen    | Requires    | Defines  | Activates |
| RC_REFIT\ | C_RCAP | sionless | that early  | a        | g         |
| (r,prc,p) |        |          | retirements | mapping  | eneration |
|           |        | \[       | are allowed | of host  | of the    |
|           |        | --3,3\]; | in the      | process  | r         |
|           |        |          | model. The  | prc to a | etrofit / |
|           |        | default  | parameter   | retrofit |  lifetime |
|           |        | value:   | value       | or       | extension |
|           |        | none     | determines  | lifetime | equations |
|           |        |          | the type of | e        | (E        |
|           |        | Default  | the         | xtension | QL_REFIT) |
|           |        | i/e: n/a | re          | option p |           |
|           |        |          | furbishment | in       |           |
|           |        |          | option as   | region   |           |
|           |        |          | follows:    | r, where |           |
|           |        |          |             | p is     |           |
|           |        |          | -           | another  |           |
|           |        |          |   Value=(±1 | process  |           |
|           |        |          |     mod 2): | repr     |           |
|           |        |          |             | esenting |           |
|           |        |          |  Technology | the      |           |
|           |        |          |     p will  | refur    |           |
|           |        |          |     be a    | bishment |           |
|           |        |          |             | option.  |           |
|           |        |          |    lifetime | The      |           |
|           |        |          |             | value of |           |
|           |        |          |   extension | the      |           |
|           |        |          |     option  | p        |           |
|           |        |          |     (+1),   | arameter |           |
|           |        |          |     or a    | de       |           |
|           |        |          |             | termines |           |
|           |        |          |    retrofit | the type |           |
|           |        |          |     option  | of the   |           |
|           |        |          |     (−1),   | refur    |           |
|           |        |          |     for the | bishment |           |
|           |        |          |     host    | option   |           |
|           |        |          |     prc     | (see     |           |
|           |        |          |             | column   |           |
|           |        |          | -   Value=2 | on the   |           |
|           |        |          |     for     | left).   |           |
|           |        |          |     p=prc:  |          |           |
|           |        |          |             |          |           |
|           |        |          |    refitted |          |           |
|           |        |          |             |          |           |
|           |        |          |    capacity |          |           |
|           |        |          |     in each |          |           |
|           |        |          |     period  |          |           |
|           |        |          |     is      |          |           |
|           |        |          |     forced  |          |           |
|           |        |          |     to be   |          |           |
|           |        |          |     equal   |          |           |
|           |        |          |     to the  |          |           |
|           |        |          |     retired |          |           |
|           |        |          |             |          |           |
|           |        |          |    capacity |          |           |
|           |        |          |     of the  |          |           |
|           |        |          |     host    |          |           |
|           |        |          |     prc     |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| P         | NCAP   | Capacity | If only a   | Residual | EQ(l      |
| RC_RESID\ | _PASTI | unit     | single data | existing | )\_CAPACT |
| (r,da     |        |          | point is    | capacity |           |
| tayear,p) |        | \[0,∞);\ | specified,  | stock of | EQ(l      |
|           |        | default  | linear      | process  | )\_CAFLAC |
|           |        | value:   | decay of    | (p)      |           |
|           |        | none     | the         | still    | E         |
|           |        |          | specified   | a        | QL_CAPFLO |
|           |        | Default  | residual    | vailable |           |
|           |        | i/e: 1\  | capacity    | in the   | E         |
|           |        | (options | over        | year     | Q(l)\_CPT |
|           |        | 5/15 may | technical   | s        |           |
|           |        | be used  | lifetime is | pecified | VAR_CAP   |
|           |        | for      | assumed.    | (dat     |           |
|           |        | extra    |             | ayear).\ |           |
|           |        | polation | Used as an  | P        |           |
|           |        | over     | alternative | RC_RESID |           |
|           |        | TLIFE,   | to          | is most  |           |
|           |        | other    | NCAP_PASTI, | useful   |           |
|           |        | i/e      | not to use  | for      |           |
|           |        | options  | both for    | de       |           |
|           |        | are      | the same    | scribing |           |
|           |        | ignored) | process.    | the      |           |
|           |        |          |             | stock of |           |
|           |        |          |             | capacity |           |
|           |        |          |             | with     |           |
|           |        |          |             | mixed    |           |
|           |        |          |             | v        |           |
|           |        |          |             | intages, |           |
|           |        |          |             | while    |           |
|           |        |          |             | NC       |           |
|           |        |          |             | AP_PASTI |           |
|           |        |          |             | is       |           |
|           |        |          |             | suited   |           |
|           |        |          |             | for      |           |
|           |        |          |             | ca       |           |
|           |        |          |             | pacities |           |
|           |        |          |             | of a     |           |
|           |        |          |             | certain  |           |
|           |        |          |             | v        |           |
|           |        |          |             | intages, |           |
|           |        |          |             | such as  |           |
|           |        |          |             | an       |           |
|           |        |          |             | in       |           |
|           |        |          |             | dividual |           |
|           |        |          |             | power    |           |
|           |        |          |             | plants.  |           |
+-----------+--------+----------+-------------+----------+-----------+
| R_CUREX\  | G      | Scalar\  | The target  | Co       | Affects   |
| (r,c      | _CUREX | (0,∞)    | currency    | nversion | cost      |
| ur1,cur2) |        |          | cur2 must   | factor   | coe       |
|           |        | Default  | have a      | from     | fficients |
|           |        | value:   | discount    | currency | in EQ_OBJ |
|           |        | none     | rate        | cur1 to  |           |
|           |        |          | defined     | currency |           |
|           |        | Default  | with        | cur2 in  |           |
|           |        | i/e: N/A | G_DRATE.    | region   |           |
|           |        |          |             | r, in    |           |
|           |        |          |             | order to |           |
|           |        |          |             | use cur2 |           |
|           |        |          |             | in the   |           |
|           |        |          |             | o        |           |
|           |        |          |             | bjective |           |
|           |        |          |             | f        |           |
|           |        |          |             | unction. |           |
+-----------+--------+----------+-------------+----------+-----------+
| RCAP_BLK\ | PR     | Capacity | Only        | Re       | EQ_DSCRET |
| (r,da     | C_RCAP | unit     | effective   | tirement |           |
| tayear,p) |        |          | when lumpy  | block    | VAR_DRCAP |
|           | RC     | \[0,∞);\ | early       | size.    |           |
|           | AP_BND | default  | capacity    |          | VAR_SCAP  |
|           |        | value:   | retirements |          |           |
|           |        | none     | are active  |          |           |
|           |        |          | (R          |          |           |
|           |        | Default  | ETIRE=MIP). |          |           |
|           |        | i/e: STD | Requires    |          |           |
|           |        |          | MIP.        |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| RCAP_BND\ | PR     | Capacity | Unless the  | Bound on | VAR_RCAP  |
| (r,datay  | C_RCAP | unit     | control     | the      |           |
| ear,p,bd) |        |          | variable    | retired  | VAR_SCAP  |
|           | RC     | \[0,∞);\ | D           | amount   |           |
|           | AP_BLK | default  | SCAUTO=YES, | of       |           |
|           |        | value:   | requires    | capacity |           |
|           |        | none     | that        | in a     |           |
|           |        |          | PRC_RCAP is | period   |           |
|           |        | Default  | defined for | (same    |           |
|           |        | i/e: STD | process p.  | bound    |           |
|           |        |          |             | for all  |           |
|           |        |          |             | vi       |           |
|           |        |          |             | ntages). |           |
+-----------+--------+----------+-------------+----------+-----------+
| RE        | RE     | Year     | Only taken  | Defines  | VAR_NCAP  |
| G_BDNCAP\ | G_FIXT |          | into        | the year |           |
| (         |        | \[       | account     | up to    |           |
| all_r,bd) |        | 1000,∞); | when a      | which    |           |
|           |        |          | previous    | ca       |           |
|           |        | default  | solution is | pacities |           |
|           |        | value:   | loaded by   | are to   |           |
|           |        | none     | using the   | be       |           |
|           |        |          | LPOINT      | bounded  |           |
|           |        |          | control     | by       |           |
|           |        |          | variable.   | previous |           |
|           |        |          |             | so       |           |
|           |        |          | If several  | lution,\ |           |
|           |        |          | bound types | by model |           |
|           |        |          | are         | region.  |           |
|           |        |          | specified,  | One can  |           |
|           |        |          | one can use | choose   |           |
|           |        |          | NCAP_B      | FX/UP/LO |           |
|           |        |          | ND(r,\'0\', | bounds,  |           |
|           |        |          | p,\'N\')=±1 | as well  |           |
|           |        |          | for         | as lower |           |
|           |        |          | assigning   | bounds   |           |
|           |        |          | only an     | only for |           |
|           |        |          | UP/LO bound | selected |           |
|           |        |          | for any     | pr       |           |
|           |        |          | process p.  | ocesses. |           |
+-----------+--------+----------+-------------+----------+-----------+
| RE        | REG_   | Monetary | The cost    | Bound on | EQ_BNDCST |
| G_BNDCST\ | CUMCST | unit     | a           | regional |           |
| (r,da     |        |          | ggregations | costs by | V         |
| tayear,ag |        | \[0,∞);\ | (agg)       | type of  | AR_CUMCST |
| g,cur,bd) |        | default  | supported   | cost     |           |
|           |        | value:   | are listed  | aggr     |           |
|           |        | none     | in the set  | egation. |           |
|           |        |          | COSTAGG     |          |           |
|           |        | Default  | (see Table  |          |           |
|           |        | i/e: MIG | 1).         |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| R         | REG_   | Monetary | The cost    | Cu       | EQ_BNDCST |
| EG_CUMCST | BNDCST | unit     | a           | mulative | V         |
| (r        |        |          | ggregations | bound on | AR_CUMCST |
| ,y1,y2,ag |        | \[0,∞);\ | (agg)       | regional |           |
| g,cur,bd) |        | default  | supported   | costs by |           |
|           |        | value:   | are listed  | type of  |           |
|           |        | none     | in the set  | cost     |           |
|           |        |          | COSTAGG     | aggr     |           |
|           |        | Default  | (see Table  | egation. |           |
|           |        | i/e: N/A | 1).         |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| REG_FIXT\ |        | Year     | Only taken  | Defines  | --        |
| (all_r)   |        |          | into        | the year |           |
|           |        | \[       | account     | up to    |           |
|           |        | 1000,∞); | when the    | which    |           |
|           |        |          | first       | periods  |           |
|           |        | default  | periods are | are      |           |
|           |        | value:   | fixed by    | fixed to |           |
|           |        | none     | using the   | previous |           |
|           |        |          | FIXBOH      | s        |           |
|           |        |          | control     | olution, |           |
|           |        |          | variable.   | by       |           |
|           |        |          |             | region   |           |
+-----------+--------+----------+-------------+----------+-----------+
| RPT_OPT\  |        | Integer  | See Part    | Misce    | --        |
| (item,j)  |        | value    | III, Table  | llaneous |           |
|           |        |          | 15 for a    | r        |           |
|           |        | \        | list and    | eporting |           |
|           |        | [open\]; | d           | options  |           |
|           |        |          | escriptions |          |           |
|           |        | default  | of          |          |           |
|           |        | value:   | available   |          |           |
|           |        | none     | options.    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| SHAPE     | FLO    | Scalar   | Provided    | Mu       | *{See     |
|           | _FUNC, |          | for each    | ltiplier | Related   |
| (j,age)   | FL     | \[       | age         | table    | Par       |
|           | O_SUM, | open\];\ | dependent   | used for | ameters}* |
|           | NCA    | default  | shaping     | any      |           |
|           | P_AFX, | value:   | curve that  | shaping  |           |
|           | NCAP   | none     | is to be    | pa       |           |
|           | _FOMX, |          | applied.    | rameters |           |
|           | NCAP_  | I/e:     |             | (        |           |
|           | FSUBX, | Full     |             | \*\_\*X) |           |
|           | NCAP   | dense    |             | to       |           |
|           | _FTAXX | inter    |             | adjust   |           |
|           |        | polation |             | the      |           |
|           |        | and      |             | corre    |           |
|           |        | extra    |             | sponding |           |
|           |        | polation |             | t        |           |
|           |        |          |             | echnical |           |
|           |        |          |             | data as  |           |
|           |        |          |             | function |           |
|           |        |          |             | of the   |           |
|           |        |          |             | age; the |           |
|           |        |          |             | table    |           |
|           |        |          |             | can      |           |
|           |        |          |             | contain  |           |
|           |        |          |             | d        |           |
|           |        |          |             | ifferent |           |
|           |        |          |             | mu       |           |
|           |        |          |             | ltiplier |           |
|           |        |          |             | curves   |           |
|           |        |          |             | that are |           |
|           |        |          |             | id       |           |
|           |        |          |             | entified |           |
|           |        |          |             | by the   |           |
|           |        |          |             | index j. |           |
+-----------+--------+----------+-------------+----------+-----------+
| STG_CHRG  | prc_   | Scalar   | Only        | Annual   | Exogenous |
|           | nstts, |          | applicable  | e        | charging  |
| (r,data   | prc_s  | \[0,∞);\ | to storage  | xogenous | of        |
| year,p,s) | tgips, | default  | processes   | charging | storage   |
|           | prc_   | value:   | (STG):      | of a     | enters    |
|           | stgtss | none     | timeslice   | storage  | storage   |
|           |        |          | storage,    | te       | equations |
|           |        | Default  | i           | chnology | (E        |
|           |        | i/e: STD | nter-period | in a     | Q_STGTSS, |
|           |        |          | storage or  | pa       | E         |
|           |        |          | night       | rticular | Q_STGIPS) |
|           |        |          | storage     | t        | as        |
|           |        |          | devices.    | imeslice | r         |
|           |        |          |             | s.       | ight-hand |
|           |        |          |             |          | side      |
|           |        |          |             |          | constant. |
+-----------+--------+----------+-------------+----------+-----------+
| STG_EFF   | prc_   | Decimal  | Only        | Ef       | Applied   |
|           | nstts, | fraction | applicable  | ficiency | to the    |
| (r,da     | prc_s  |          | to storage  | of       | storage   |
| tayear,p) | tgips, | \[0,∞);\ | processes   | storage  | output    |
|           | prc_   | default  | (STG):      | process. | flow      |
|           | stgtss | value: 1 | timeslice   |          | (         |
|           |        |          | storage,    |          | VAR_SOUT) |
|           |        | Default  | i           |          | in the    |
|           |        | i/e: STD | nter-period |          | commodity |
|           |        |          | storage or  |          | balance   |
|           |        |          | night       |          | (EQ(l)    |
|           |        |          | storage     |          | \_COMBAL) |
|           |        |          | devices.    |          | for the   |
|           |        |          |             |          | stored    |
|           |        |          |             |          | c         |
|           |        |          |             |          | ommodity. |
+-----------+--------+----------+-------------+----------+-----------+
| STG_LOSS  | prc_   | Scalar   | Only        | Annual   | Timeslice |
|           | nstts, |          | applicable  | loss of  | storage   |
| (r,data   | prc_s  | \[       | to storage  | a        | process   |
| year,p,s) | tgips, | open\];\ | processes   | storage  | (EQ       |
|           | prc_   | default  | (STG):      | process  | _STGTSS): |
|           | stgtss | value:   | timeslice   | per unit | applied   |
|           |        | none     | storage,    | of       | to the    |
|           |        |          | i           | average  | average   |
|           |        | Default  | nter-period | energy   | storage   |
|           |        | i/e: STD | storage or  | stored.  | level     |
|           |        |          | night       |          | (VAR_ACT) |
|           |        |          | storage     |          | between   |
|           |        |          | devices.    |          | two       |
|           |        |          |             |          | co        |
|           |        |          | STG_LOSS\>0 |          | nsecutive |
|           |        |          | defines the |          | ti        |
|           |        |          | loss in     |          | meslices. |
|           |        |          | proportion  |          |           |
|           |        |          | to the      |          | Int       |
|           |        |          | initial     |          | er-period |
|           |        |          | storage     |          | storage   |
|           |        |          | level       |          | process   |
|           |        |          | during one  |          | (EQ       |
|           |        |          | year's      |          | _STGIPS): |
|           |        |          | storage     |          | applied   |
|           |        |          | time.       |          | to the    |
|           |        |          |             |          | average   |
|           |        |          | STG_LOSS\<0 |          | storage   |
|           |        |          | defines an  |          | level     |
|           |        |          | equilibrium |          | from the  |
|           |        |          | loss, i.e.  |          | p         |
|           |        |          | how much    |          | re-period |
|           |        |          | the annual  |          | (VAR_ACT) |
|           |        |          | losses      |          | and the   |
|           |        |          | would be if |          | net       |
|           |        |          | the storage |          | inflow    |
|           |        |          | level is    |          | (VAR_SIN- |
|           |        |          | kept        |          | VAR_SOUT) |
|           |        |          | constant.   |          | of the    |
|           |        |          |             |          | current   |
|           |        |          |             |          | period.   |
+-----------+--------+----------+-------------+----------+-----------+
| ST        | N      | Number   | Can only be | Defines  | Activates |
| G_MAXCYC\ | CAP_AF | of       | used for    | the      | g         |
| (r,da     |        | cycles\  | genuine     | maximum  | eneration |
| tayear,p) |        | \[0,∞);  | storage     | number   | of the    |
|           |        |          | processes.  | of       | cycle     |
|           |        | default  | The limit   | storage  | limi      |
|           |        | value:   | can be      | cycles   | t/penalty |
|           |        | none     | exceeded by | over the | equations |
|           |        |          | paying for  | l        | (EQL      |
|           |        | Default  | additional  | ifetime. | _STGCCL). |
|           |        | i/e: STD | replacement | Sets a   |           |
|           |        |          | capacity,   | limit    |           |
|           |        |          | with a      | for the  |           |
|           |        |          | penalty     | total    |           |
|           |        |          | cost equal  | d        |           |
|           |        |          | to the      | ischarge |           |
|           |        |          | investment  | divided  |           |
|           |        |          | annuity.    | by       |           |
|           |        |          |             | storage  |           |
|           |        |          |             | c        |           |
|           |        |          |             | apacity. |           |
+-----------+--------+----------+-------------+----------+-----------+
| STG_SIFT\ | AC     | Decimal  | Can only be | Defines  | Activates |
| (r,da     | T_TIME | fraction | used for a  | process  | g         |
| tayear,pr |        |          | timeslice   | prc as a | eneration |
| c,com,ts) |        | \[0,∞);\ | storage     | load-    | of load   |
|           |        | default  | process.    | shifting | shifting  |
|           |        | value:   | Levelized   | process, | co        |
|           |        | none     | to the      | and      | nstraints |
|           |        |          | timeslice   | limits   | (EQ(l)\   |
|           |        | Default  | level of    | the load | _SLSIFT). |
|           |        | i/e: STD | the process | shifting |           |
|           |        |          | flow.       | of       |           |
|           |        |          |             | demand   |           |
|           |        |          | Direct      | com in   |           |
|           |        |          | i           | t        |           |
|           |        |          | nheritance. | imeslice |           |
|           |        |          |             | ts to at |           |
|           |        |          | By          | most the |           |
|           |        |          | specifying  | fraction |           |
|           |        |          | com=\'ACT\' | s        |           |
|           |        |          | one can     | pecified |           |
|           |        |          | define a    | by the   |           |
|           |        |          | limit in    | p        |           |
|           |        |          | total       | arameter |           |
|           |        |          | shifting    | value.   |           |
|           |        |          | over a      |          |           |
|           |        |          | season, in  |          |           |
|           |        |          | proportion  |          |           |
|           |        |          | to demand.  |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| STGIN_BND | prc_   | C        | Only        | Bound on | Storage   |
|           | nstts, | ommodity | applicable  | the      | input     |
| (r,       | prc_s  | unit     | to storage  | input    | bound     |
| datayear, | tgips, |          | processes   | flow of  | c         |
| p,c,s,bd) | prc_   | \[0,∞);\ | (STG):      | a        | onstraint |
|           | stgtss | default  | timeslice   | storage  | (EQ(l     |
|           |        | value:   | storage,    | process  | )\_STGIN) |
|           |        | none     | i           | in a     | when s is |
|           |        |          | nter-period | t        | above     |
|           |        | Default  | storage or  | imeslice | prc_tsl   |
|           |        | i/e: MIG | night       | s.       | of the    |
|           |        |          | storage     |          | storage   |
|           |        |          | devices.    |          | process.  |
|           |        |          |             |          |           |
|           |        |          |             |          | Direct    |
|           |        |          |             |          | bound on  |
|           |        |          |             |          | storage   |
|           |        |          |             |          | input     |
|           |        |          |             |          | flow      |
|           |        |          |             |          | (VAR_SIN) |
|           |        |          |             |          | when at   |
|           |        |          |             |          | the       |
|           |        |          |             |          | prc_tsl   |
|           |        |          |             |          | level.    |
+-----------+--------+----------+-------------+----------+-----------+
| S         | prc_   | C        | Only        | Bound on | Storage   |
| TGOUT_BND | nstts, | ommodity | applicable  | the      | output    |
|           | prc_s  | unit     | to storage  | output   | bound     |
| (r,       | tgips, |          | processes   | flow of  | c         |
| datayear, | prc_   | \[0,∞);\ | (STG):      | a        | onstraint |
| p,c,s,bd) | stgtss | default  | timeslice   | storage  | (EQ(l     |
|           |        | value:   | storage,    | process  | )\_STGIN) |
|           |        | none     | i           | in a     | when s is |
|           |        |          | nter-period | t        | above     |
|           |        | Default  | storage or  | imeslice | prc_tsl   |
|           |        | i/e: MIG | night       | s.       | of the    |
|           |        |          | storage     |          | storage   |
|           |        |          | devices.    |          | process.  |
|           |        |          |             |          |           |
|           |        |          |             |          | Direct    |
|           |        |          |             |          | bound on  |
|           |        |          |             |          | storage   |
|           |        |          |             |          | output    |
|           |        |          |             |          | flow      |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (         |
|           |        |          |             |          | VAR_SOUT) |
|           |        |          |             |          | when at   |
|           |        |          |             |          | the       |
|           |        |          |             |          | prc_tsl   |
|           |        |          |             |          | level.    |
+-----------+--------+----------+-------------+----------+-----------+
| TL_CCAP0  | (      | Capacity | Requires    | Initial  | C         |
|           | Alias: | unit     | using ETL.  | cu       | umulative |
| (r,teg)   | CCAP0) |          |             | mulative | i         |
|           |        | \[       | For         | capacity | nvestment |
|           | PAT,\  | open\];\ | learning    | of a     | c         |
|           | CCOST0 | default  | t           | learning | onstraint |
|           |        | value:   | echnologies | tec      | (         |
|           |        | none     | teg when    | hnology. | EQ_CUINV) |
|           |        |          | ETL is      |          | and       |
|           |        |          | used.       |          | c         |
|           |        |          |             |          | umulative |
|           |        |          |             |          | capacity  |
|           |        |          |             |          | variable  |
|           |        |          |             |          | (         |
|           |        |          |             |          | VAR_CCAP) |
|           |        |          |             |          | in        |
|           |        |          |             |          | e         |
|           |        |          |             |          | ndogenous |
|           |        |          |             |          | tech      |
|           |        |          |             |          | nological |
|           |        |          |             |          | learning  |
|           |        |          |             |          | for       |
|           |        |          |             |          | mulation. |
+-----------+--------+----------+-------------+----------+-----------+
| TL_CCAPM  | (      | Capacity | Requires    | Maximum  | Core ETL  |
|           | Alias: | unit     | using ETL.  | cu       | e         |
| (r,teg)   | CCAPM) |          |             | mulative | quations. |
|           |        | \[       | For         | c        |           |
|           | CCOSTM | open\];\ | learning    | apacity. |           |
|           |        | default  | t           |          |           |
|           |        | value:   | echnologies |          |           |
|           |        | none     | teg when    |          |           |
|           |        |          | ETL is      |          |           |
|           |        |          | used.       |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| TL        | (      | Decimal  | Requires    | I        | EQ_CLU    |
| _CLUSTER\ | Alias: | f        | using ETL   | ndicator |           |
| (r        | CL     | raction. | (MIP).      | that a   |           |
| ,teg,prc) | USTER) |          |             | te       |           |
|           |        | \[0-1\]; | • Provided  | chnology |           |
|           | TL_M   |          | to model    | (teg) is |           |
|           | RCLUST | default  | clustered   | a        |           |
|           |        | value:   | endogenous  | learning |           |
|           |        | none     | technology  | c        |           |
|           |        |          | learning.   | omponent |           |
|           |        |          |             | that is  |           |
|           |        |          | • Each of   | part of  |           |
|           |        |          | the         | another  |           |
|           |        |          | learning    | te       |           |
|           |        |          | parameters  | chnology |           |
|           |        |          | must also   | (prc) in |           |
|           |        |          | be          | region   |           |
|           |        |          | specified   | r; teg   |           |
|           |        |          | for the key | is also  |           |
|           |        |          | learning    | called   |           |
|           |        |          | technology. | key      |           |
|           |        |          |             | co       |           |
|           |        |          |             | mponent. |           |
+-----------+--------+----------+-------------+----------+-----------+
| TL        | TL_C   | Decimal  | Requires    | Mapping  | EQ_MRCLU  |
| _MRCLUST\ | LUSTER | f        | using ETL   | for      |           |
| (r,t      |        | raction. | (MIP).      | mult     |           |
| eg,reg,p) |        |          |             | i-region |           |
|           |        | \[0-1\]; | • Provided  | cl       |           |
|           |        |          | to model    | ustering |           |
|           |        | default  | clustered   | between  |           |
|           |        | value:   | endogenous  | learning |           |
|           |        | none     | technology  | key      |           |
|           |        |          | learning.   | co       |           |
|           |        |          |             | mponents |           |
|           |        |          | • Each of   | (teg)    |           |
|           |        |          | the         | and      |           |
|           |        |          | learning    | p        |           |
|           |        |          | parameters  | rocesses |           |
|           |        |          | must also   | (p) that |           |
|           |        |          | be          | utilize  |           |
|           |        |          | specified   | the key  |           |
|           |        |          | for the key | co       |           |
|           |        |          | learning    | mponent. |           |
|           |        |          | technology. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| TL_PRAT   | (      | Scalar   | Requires    | Progress | Fu        |
|           | Alias: |          | using ETL.  | ratio    | ndamental |
| (r,teg)   | PRAT)  | \        |             | in       | factor to |
|           |        | [0,1\];\ | Provided    | dicating | describe  |
|           | ALPH   | default  | for         | the drop | the       |
|           |        | value    | learning    | in the   | learning  |
|           | BETA   | none     | t           | in       | curve and |
|           |        |          | echnologies | vestment | thus      |
|           | CCAPK  |          | (teg) when  | cost     | effects   |
|           |        |          | ETL is      | each     | nearly    |
|           | CCOST0 |          | used.       | time     | all       |
|           |        |          |             | there is | equations |
|           | PAT    |          |             | a        | and       |
|           |        |          |             | doubling | variables |
|           | PBT    |          |             | of the   | related   |
|           |        |          |             | i        | to        |
|           |        |          |             | nstalled | e         |
|           |        |          |             | c        | ndogenous |
|           |        |          |             | apacity. | t         |
|           |        |          |             |          | echnology |
|           |        |          |             |          | learning  |
|           |        |          |             |          | (ETL).    |
+-----------+--------+----------+-------------+----------+-----------+
| TL_SC0    | (      | Monetary | Requires    | Initial  | Defines   |
|           | Alias: | unit /   | using ETL.  | specific | together  |
| (r,teg)   | SC0)   | capacity |             | in       | with      |
|           |        | unit     | For         | vestment | CCAP0     |
|           |        |          | learning    | costs.   | initial   |
|           |        | \[       | t           |          | point of  |
|           |        | open\];\ | echnologies |          | learning  |
|           |        | default  | teg when    |          | curve and |
|           |        | value:   | ETL is      |          | affects   |
|           |        | none     | used.       |          | thus the  |
|           |        |          |             |          | core      |
|           |        |          |             |          | equations |
|           |        |          |             |          | and       |
|           |        |          |             |          | variables |
|           |        |          |             |          | of        |
|           |        |          |             |          | e         |
|           |        |          |             |          | ndogenous |
|           |        |          |             |          | tech      |
|           |        |          |             |          | nological |
|           |        |          |             |          | learning  |
|           |        |          |             |          | (ETL).    |
+-----------+--------+----------+-------------+----------+-----------+
| TL_SEG    | (      | Integer  | Requires    | Number   | I         |
|           | Alias: |          | using ETL.  | of       | nfluences |
| (r,teg)   | SEG)   | \        |             | s        | the       |
|           |        | [open\]; | For         | egments. | piecewise |
|           |        |          | learning    |          | linear    |
|           |        |          | t           |          | appr      |
|           |        |          | echnologies |          | oximation |
|           |        |          | teg when    |          | of the    |
|           |        |          | ETL is      |          | c         |
|           |        |          | used.       |          | umulative |
|           |        |          |             |          | cost      |
|           |        |          | Currently   |          | curve     |
|           |        |          | limited to  |          | (EQ_COS,  |
|           |        |          | six         |          | EQ_LA1,   |
|           |        |          | segments by |          | EQ_LA2).  |
|           |        |          | set kp.     |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| TS_CYCLE\ | G      | Number   | Recommended | Defines  | Affects   |
| (r,ts)    | _CYCLE | of days\ | to be used  | the      | the       |
|           |        | \[1,∞);  | whenever    | length   | ca        |
|           |        |          | timeslice   | of the   | lculation |
|           |        | Default  | cycles are  | t        | of actual |
|           |        | values:  | different   | imeslice | timeslice |
|           |        |          | from the    | cycles   | lengths   |
|           |        | -   365  | default,    | under    | and       |
|           |        |     for  | instead of  | t        | number of |
|           |        |     t    | changing    | imeslice | timeslice |
|           |        | s=ANNUAL | G_CYCLE.    | ts, in   | cycles in |
|           |        |          | Does not    | days,    | various   |
|           |        | -   7    | affect      | and      | e         |
|           |        |     for  | int         | thereby  | quations, |
|           |        |     any  | er­pretation | also the | notably   |
|           |        |     ts   | of          | number   | storage   |
|           |        |          | a           | of       | and       |
|           |        |    above | vailability | t        | di        |
|           |        |     the  | factors for | imeslice | spatching |
|           |        |          | storage     | cycles   | e         |
|           |        |   WEEKLY | level,      | under    | quations. |
|           |        |          | which thus  | each     |           |
|           |        |    level | remain to   | parent.  |           |
|           |        |          | be          |          |           |
|           |        | -   1    | according   |          |           |
|           |        |     for  | to G_CYCLE. |          |           |
|           |        |     any  |             |          |           |
|           |        |     ts   |             |          |           |
|           |        |          |             |          |           |
|           |        |    above |             |          |           |
|           |        |     the  |             |          |           |
|           |        |          |             |          |           |
|           |        |  DAYNITE |             |          |           |
|           |        |          |             |          |           |
|           |        |    level |             |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_ACT    | uc_n,  | None     | Used in     | Coe      | EQ(       |
|           | uc_    |          | user        | fficient | l)\_UCXXX |
| (uc_n,si  | gmap_p | \[       | c           | of the   |           |
| de,r,data |        | open\];\ | onstraints. | activity |           |
| year,p,s) |        | default  |             | variable |           |
|           |        | value:   | Direct      | VAR_ACT  |           |
|           |        | none     | i           | in a     |           |
|           |        |          | nheritance. | user     |           |
|           |        | Default: |             | con      |           |
|           |        | i/e: STD | Weighted    | straint. |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_CAP    | uc_n,  | None     | Used in     | Coe      | EQ(       |
|           | uc_    |          | user        | fficient | l)\_UCXXX |
| (uc_n,    | gmap_p | \[       | c           | of the   |           |
| side,r,da |        | open\];\ | onstraints. | activity |           |
| tayear,p) |        | default  |             | variable |           |
|           |        | value:   |             | VAR_CAP  |           |
|           |        | none     |             | in a     |           |
|           |        |          |             | user     |           |
|           |        | Default: |             | con      |           |
|           |        | i/e: STD |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_CLI    |        | Dimen    | Used in     | Mu       | EQ(       |
|           |        | sionless | user        | ltiplier | l)\_UCXXX |
| (uc_n     |        |          | c           | of       |           |
| ,side,r,d |        | \        | onstraints. | climate  |           |
| atayear,\ |        | [open\]; |             | variable |           |
| item)     |        |          | Climate     | in user  |           |
|           |        | default  | variable    | co       |           |
|           |        | value:   | can be at   | nstraint |           |
|           |        | none     | least any   |          |           |
|           |        |          | of CO2-GTC, |          |           |
|           |        | Default  | CO2-ATM,    |          |           |
|           |        | i/e: STD | CO2-UP,     |          |           |
|           |        |          | CO2-LO,     |          |           |
|           |        |          | FORCING,    |          |           |
|           |        |          | DELTA-ATM,  |          |           |
|           |        |          |             |          |           |
|           |        |          | DELTA-LO    |          |           |
|           |        |          | (for        |          |           |
|           |        |          | carbon).    |          |           |
|           |        |          |             |          |           |
|           |        |          | See         |          |           |
|           |        |          | Appendix on |          |           |
|           |        |          | Climate     |          |           |
|           |        |          | Module for  |          |           |
|           |        |          | details.    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_COMCON | uc_n,  | None     | Used in     | Coe      | EQ(       |
|           | uc_    |          | user        | fficient | l)\_UCXXX |
| (uc_n,si  | gmap_c | \[       | c           | of the   |           |
| de,r,data |        | open\];\ | onstraints. | c        |           |
| year,c,s) |        | default  |             | ommodity |           |
|           |        | value:   | No          | con      |           |
|           |        | none     | i           | sumption |           |
|           |        |          | nheritance/ | variable |           |
|           |        | Default: | aggregation | VA       |           |
|           |        | i/e: STD | (might be   | R_COMCON |           |
|           |        |          | changed in  | in a     |           |
|           |        |          | the         | user     |           |
|           |        |          | future).    | con      |           |
|           |        |          |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_COMNET | uc_n,  | None     | Used in     | Coe      | EQ(       |
|           | uc_    |          | user        | fficient | l)\_UCXXX |
| (uc_n,si  | gmap_c | \[       | c           | of the   |           |
| de,r,data |        | open\];\ | onstraints. | net      |           |
| year,c,s) |        | default  |             | c        |           |
|           |        | value:   | No          | ommodity |           |
|           |        | none     | i           | pr       |           |
|           |        |          | nheritance/ | oduction |           |
|           |        | Default: | aggregation | variable |           |
|           |        | i/e: STD | (might be   | VA       |           |
|           |        |          | changed in  | R_COMNET |           |
|           |        |          | the         | in a     |           |
|           |        |          | future).    | user     |           |
|           |        |          |             | con      |           |
|           |        |          |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_COMPRD | uc_n,  | None     | Used in     | Coe      | EQ(       |
|           | uc_    |          | user        | fficient | l)\_UCXXX |
| (uc_n,si  | gmap_c | \[       | c           | of the   |           |
| de,r,data |        | open\];\ | onstraints. | total    |           |
| year,c,s) |        | default  |             | c        |           |
|           |        | value:   | No          | ommodity |           |
|           |        | none     | i           | pr       |           |
|           |        |          | nheritance/ | oduction |           |
|           |        | Default: | aggregation | variable |           |
|           |        | i/e: STD | (might be   | VA       |           |
|           |        |          | changed in  | R_COMPRD |           |
|           |        |          | the         | in a     |           |
|           |        |          | future).    | user     |           |
|           |        |          |             | con      |           |
|           |        |          |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_CUMACT | A      | Dimen    | Used in     | Mu       | EQ(l)\_UC |
| (uc_n,r   | CT_CUM | sionless | cumulative  | ltiplier |           |
| ,p,y1,y2) |        |          | user        | of       | E         |
|           |        | \        | constraints | cu       | Q(l)\_UCR |
|           |        | [open\]; | only.       | mulative |           |
|           |        |          |             | process  | V         |
|           |        | default  |             | activity | AR_CUMFLO |
|           |        | value:   |             | variable |           |
|           |        | none     |             | in user  |           |
|           |        |          |             | con      |           |
|           |        | I/e: N/A |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_CUMCOM | COM_   | Dimen    | Used in     | Mu       | EQ(l)\_UC |
| (uc       | CUMNET | sionless | cumulative  | ltiplier |           |
| _n,r,type |        |          | user        | of       | E         |
| ,c,y1,y2) | COM_   | \        | constraints | cu       | Q(l)\_UCR |
|           | CUMPRD | [open\]; | only.\      | mulative |           |
|           |        |          | T           | c        | V         |
|           |        | default  | ype=NET/PRD | ommodity | AR_CUMCOM |
|           |        | value:   | determines  | variable |           |
|           |        | none     | the         | in user  |           |
|           |        |          | variable    | con      |           |
|           |        | I/e: N/A | referred to | straint. |           |
|           |        |          | (CUMNET/    |          |           |
|           |        |          | CUMPRD).    |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_CUMFLO | F      | Dimen    | Used in     | Mu       | EQ(l)\_UC |
| (uc_n,r,p | LO_CUM | sionless | cumulative  | ltiplier |           |
| ,c,y1,y2) |        |          | user        | of       | E         |
|           |        | \        | constraints | cu       | Q(l)\_UCR |
|           |        | [open\]; | only.       | mulative |           |
|           |        |          |             | process  | V         |
|           |        | default  |             | flow     | AR_CUMFLO |
|           |        | value:   |             | variable |           |
|           |        | none     |             | in user  |           |
|           |        |          |             | con      |           |
|           |        | I/e: N/A |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_FLO    | uc_n   | None     | Used in     | Coe      | EQ(       |
|           |        |          | user        | fficient | l)\_UCXXX |
| (         |        | \[       | c           | of the   |           |
| uc_n,side |        | open\];\ | onstraints. | flow     |           |
| ,r,dataye |        | default  |             | VAR_FLO  |           |
| ar,p,c,s) |        | value:   | Direct      | variable |           |
|           |        | none     | i           | in a     |           |
|           |        |          | nheritance. | user     |           |
|           |        | Default: |             | con      |           |
|           |        | i/e: STD | Weighted    | straint. |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_IRE    | uc_n   | None     | Used in     | Coe      | EQ(       |
|           |        |          | user        | fficient | l)\_UCXXX |
| (         |        | \[       | c           | of the   |           |
| uc_n,side |        | open\];\ | onstraints. | trade    |           |
| ,r,dataye |        | default  |             | variable |           |
| ar,p,c,s) |        | value:   | Direct      | VAR_IRE  |           |
|           |        | none     | i           | in a     |           |
|           |        |          | nheritance. | user     |           |
|           |        | Default: |             | con      |           |
|           |        | i/e: STD | Weighted    | straint. |           |
|           |        |          | a           |          |           |
|           |        |          | ggregation. |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_NCAP   | uc_n,  | None     | Used in     | Coe      | EQ(       |
|           | uc_    |          | user        | fficient | l)\_UCXXX |
| (uc_n,    | gmap_p | \[       | c           | of the   |           |
| side,r,da |        | open\];\ | onstraints. | activity |           |
| tayear,p) |        | default  |             | variable |           |
|           |        | value:   |             | VAR_NCAP |           |
|           |        | none     |             | in a     |           |
|           |        |          |             | user     |           |
|           |        | Default: |             | con      |           |
|           |        | i/e: STD |             | straint. |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_RHS    | uc_n,  | None     | Used in     | RHS      | RHS       |
|           | uc_    |          | user        | constant | (r        |
| (         | r_sum, | \[       | co          | with     | ight-hand |
| uc_n,lim) | uc_    | open\];\ | nstraints.\ | bound    | side)     |
|           | t_sum, | default  | Binding     | type of  | constant  |
|           | uc_    | value:   | user        | bd of a  | of a user |
|           | ts_sum | none     | constraints | user     | co        |
|           |        |          | are defined | con      | nstraint, |
|           |        | Default  | using bound | straint. | which is  |
|           |        | i/e:     | types       |          | summing   |
|           |        | none     | lim         |          | over      |
|           |        |          | =UP/LO/FX.\ |          | regions   |
|           |        |          | Non-binding |          | (u        |
|           |        |          | (free) user |          | c_r_sum), |
|           |        |          | constraints |          | periods   |
|           |        |          | can be      |          | (         |
|           |        |          | defined     |          | uc_t_sum) |
|           |        |          | using the   |          | and       |
|           |        |          | lim type    |          | t         |
|           |        |          | lim=N.      |          | imeslices |
|           |        |          |             |          | (u        |
|           |        |          |             |          | c_ts_sum) |
|           |        |          |             |          | (EQ       |
|           |        |          |             |          | (l)\_UC). |
+-----------+--------+----------+-------------+----------+-----------+
| UC_RHSR   | uc_n,  | None     | Used in     | RHS      | RHS       |
|           | uc_r   |          | user        | constant | constant  |
| (r,       | _each, | \[       | c           | with     | of user   |
| uc_n,lim) | uc_    | open\];\ | onstraints. | bound    | con       |
|           | t_sum, | default  |             | type of  | straints, |
|           | uc_    | value:   | Binding     | bd of a  | which are |
|           | ts_sum | none     | user        | user     | generated |
|           |        |          | constraints | con      | for each  |
|           |        | Default  | are defined | straint. | region    |
|           |        | i/e:     | using bound |          | (u        |
|           |        | none     | types       |          | c_r_each) |
|           |        |          | lim         |          | and are   |
|           |        |          | =UP/LO/FX.\ |          | summing   |
|           |        |          | Non-binding |          | over      |
|           |        |          | (free) user |          | periods   |
|           |        |          | constraints |          | (         |
|           |        |          | can be      |          | uc_t_sum) |
|           |        |          | defined     |          | and       |
|           |        |          | using the   |          | t         |
|           |        |          | lim type    |          | imeslices |
|           |        |          | lim=N.      |          | (u        |
|           |        |          |             |          | c_ts_sum) |
|           |        |          |             |          | (EQ(      |
|           |        |          |             |          | l)\_UCR). |
+-----------+--------+----------+-------------+----------+-----------+
| UC_RHSRT  | uc_n,  | None     | Used in     | RHS      | RHS       |
|           | uc_r   |          | user        | constant | constant  |
| (r,       | _each, | \[       | co          | with     | of user   |
| uc_n,data | uc_t   | open\];\ | nstraints.\ | bound    | con       |
| year,lim) | _each, | default  | \           | type of  | straints, |
|           | uc_t   | value:   | Binding     | bd of a  | which are |
|           | _succ, | none     | user        | user     | generated |
|           | uc_    |          | constraints | con      | for each  |
|           | ts_sum | Default  | are defined | straint. | region    |
|           |        | i/e: MIG | using bound |          | (u        |
|           |        |          | types       |          | c_r_each) |
|           |        |          | lim         |          | and       |
|           |        |          | =UP/LO/FX.\ |          | period    |
|           |        |          | Non-binding |          | (u        |
|           |        |          | (free) user |          | c_t_each) |
|           |        |          | constraints |          | and are   |
|           |        |          | can be      |          | summing   |
|           |        |          | defined     |          | over      |
|           |        |          | using the   |          | t         |
|           |        |          | lim type    |          | imeslices |
|           |        |          | lim=N.      |          | (u        |
|           |        |          |             |          | c_ts_sum) |
|           |        |          |             |          | (EQ(l     |
|           |        |          |             |          | )\_UCRT). |
|           |        |          |             |          |           |
|           |        |          |             |          | If        |
|           |        |          |             |          | dynamic,  |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | will be   |
|           |        |          |             |          | generated |
|           |        |          |             |          | between   |
|           |        |          |             |          | two       |
|           |        |          |             |          | s         |
|           |        |          |             |          | uccessive |
|           |        |          |             |          | periods   |
|           |        |          |             |          | (EQ(l)    |
|           |        |          |             |          | \_UCRSU). |
+-----------+--------+----------+-------------+----------+-----------+
| UC_RHSRTS | uc_n,  | None     | Used in     | RHS      | RHS       |
|           | uc_r   |          | user        | constant | constant  |
| (r,uc     | _each, | \[       | c           | with     | of user   |
| _n,dataye | uc_t   | open\];\ | onstraints. | bound    | con       |
| ar,s,lim) | _each, | default  |             | type of  | straints, |
|           | uc_t   | value:   | No          | bd of a  | which are |
|           | _succ, | none     | inheritance | user     | generated |
|           | uc_t   |          | /           | con      | for each  |
|           | s_each | Default  | a           | straint. | specified |
|           |        | i/e: MIG | ggregation, |          | region    |
|           |        |          | unless the  |          | (uc       |
|           |        |          | target      |          | _r_each), |
|           |        |          | timeslice   |          | period    |
|           |        |          | level is    |          | (u        |
|           |        |          | specified   |          | c_t_each) |
|           |        |          | by UC_TSL.\ |          | and       |
|           |        |          | Direct      |          | timeslice |
|           |        |          | i           |          | (uc       |
|           |        |          | nheritance, |          | _ts_each) |
|           |        |          | if the      |          | (EQ(l)    |
|           |        |          | target      |          | \_UCRTS). |
|           |        |          | timeslice   |          |           |
|           |        |          | level is    |          | If        |
|           |        |          | specified   |          | dynamic,  |
|           |        |          | by UC_TSL.\ |          | co        |
|           |        |          | Binding     |          | nstraints |
|           |        |          | user        |          | will be   |
|           |        |          | constraints |          | generated |
|           |        |          | are defined |          | between   |
|           |        |          | using bound |          | two       |
|           |        |          | types       |          | s         |
|           |        |          | lim         |          | uccessive |
|           |        |          | =UP/LO/FX.\ |          | periods   |
|           |        |          | Non-binding |          | (EQ(l)\   |
|           |        |          | (free) user |          | _UCRSUS). |
|           |        |          | constraints |          |           |
|           |        |          | can be      |          |           |
|           |        |          | defined     |          |           |
|           |        |          | using the   |          |           |
|           |        |          | lim type    |          |           |
|           |        |          | lim=N.      |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_RHST   | uc_n,  | None     | Used in     | RHS      | RHS       |
|           | uc_    |          | user        | constant | constant  |
| (         | r_sum, | \[       | co          | with     | of user   |
| uc_n,data | uc_t   | open\];\ | nstraints.\ | bound    | con       |
| year,lim) | _each, | default  | \           | type of  | straints, |
|           | uc_t   | value:   | Binding     | bd of a  | which are |
|           | _succ, | none     | user        | user     | generated |
|           | uc_    |          | constraints | con      | for each  |
|           | ts_sum | Default  | are defined | straint. | specified |
|           |        | i/e: MIG | using bound |          | period    |
|           |        |          | types       |          | (u        |
|           |        |          | lim         |          | c_t_each) |
|           |        |          | =UP/LO/FX.\ |          | and are   |
|           |        |          | Non-binding |          | summing   |
|           |        |          | (free) user |          | over      |
|           |        |          | constraints |          | regions   |
|           |        |          | can be      |          | (         |
|           |        |          | defined     |          | uc_r_sum) |
|           |        |          | using the   |          | and       |
|           |        |          | lim type    |          | t         |
|           |        |          | lim=N.      |          | imeslices |
|           |        |          |             |          | (u        |
|           |        |          |             |          | c_ts_sum) |
|           |        |          |             |          | (EQ(      |
|           |        |          |             |          | l)\_UCT). |
|           |        |          |             |          |           |
|           |        |          |             |          | If        |
|           |        |          |             |          | dynamic,  |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | will be   |
|           |        |          |             |          | generated |
|           |        |          |             |          | between   |
|           |        |          |             |          | two       |
|           |        |          |             |          | s         |
|           |        |          |             |          | uccessive |
|           |        |          |             |          | periods   |
|           |        |          |             |          | (EQ(l     |
|           |        |          |             |          | )\_UCSU). |
+-----------+--------+----------+-------------+----------+-----------+
| UC_RHSTS  | uc_n,  | None     | Used in     | RHS      | RHS       |
|           | uc_    |          | user        | constant | constant  |
| (uc       | r_sum, | \[       | c           | with     | of user   |
| _n,dataye | uc_t   | open\];\ | onstraints. | bound    | con       |
| ar,s,lim) | _each, | default  |             | type of  | straints, |
|           | uc_t   | value:   | No          | bd of a  | which are |
|           | _succ, | none     | in          | user     | generated |
|           | uc_t   |          | heritance/a | con      | for each  |
|           | s_each | Default  | ggregation. | straint. | period    |
|           |        | i/e: MIG |             |          | (u        |
|           |        |          | Binding     |          | c_t_each) |
|           |        |          | user        |          | and       |
|           |        |          | constraints |          | timeslice |
|           |        |          | are defined |          | (uc       |
|           |        |          | using bound |          | _ts_each) |
|           |        |          | types       |          | and are   |
|           |        |          | lim         |          | summing   |
|           |        |          | =UP/LO/FX.\ |          | over      |
|           |        |          | Non-binding |          | regions   |
|           |        |          | (free) user |          | (         |
|           |        |          | constraints |          | uc_r_sum) |
|           |        |          | can be      |          | (EQ(l     |
|           |        |          | defined     |          | )\_UCTS). |
|           |        |          | using the   |          |           |
|           |        |          | lim type    |          | If        |
|           |        |          | lim=N.      |          | dynamic,  |
|           |        |          |             |          | co        |
|           |        |          |             |          | nstraints |
|           |        |          |             |          | will be   |
|           |        |          |             |          | generated |
|           |        |          |             |          | between   |
|           |        |          |             |          | two       |
|           |        |          |             |          | s         |
|           |        |          |             |          | uccessive |
|           |        |          |             |          | periods   |
|           |        |          |             |          | (EQ(l)    |
|           |        |          |             |          | \_UCSUS). |
+-----------+--------+----------+-------------+----------+-----------+
| UC_TIME   |        | Dimen    | Used in     | Mu       | EQ(       |
| (uc_n,r,  |        | sionless | user        | ltiplier | l)\_UCXXX |
| datayear) |        |          | c           | for the  |           |
|           |        | \        | onstraints. | number   |           |
|           |        | [open\]; |             | of years |           |
|           |        |          | Adds a time | in model |           |
|           |        | default  | constant to | periods  |           |
|           |        | value:   | the RHS     | (static  |           |
|           |        | none     | side.       | UCs), or |           |
|           |        |          |             | between  |           |
|           |        | Default  |             | m        |           |
|           |        | i/e: STD |             | ilestone |           |
|           |        |          |             | years    |           |
|           |        |          |             | (dynamic |           |
|           |        |          |             | UCs)     |           |
+-----------+--------+----------+-------------+----------+-----------+
| UC_UCN    | UC     | Dimen    | Only taken  | Mu       | EQ(       |
| (uc_n     | _RHSRT | sionless | into        | ltiplier | l)\_UCRSU |
| ,side,r,d |        |          | account if  | of user  |           |
| atayear,\ |        | \        | the user    | co       | VAR_UCRT  |
| ucn)      |        | [open\]; | constraint  | nstraint |           |
|           |        |          | is by       | variable |           |
|           |        | default  | region &    | in       |           |
|           |        | value:   | period, and | another  |           |
|           |        | none     | summing     | user     |           |
|           |        |          | over        | con      |           |
|           |        | Default  | timeslices  | straint. |           |
|           |        | i/e: STD | and the RHS |          |           |
|           |        |          | side is     |          |           |
|           |        |          | activated   |          |           |
|           |        |          | (EQ(        |          |           |
|           |        |          | l)\_UCRSU). |          |           |
+-----------+--------+----------+-------------+----------+-----------+
| VDA_EMCB\ | FL     | Emission | Available   | E        | EQ_PTRANS |
| (r,dataye | O_EMIS | units    | in the VEDA | missions |           |
| ar,c,com) |        | per flow | shell.      | (com)    |           |
|           | F      | units    |             | from the |           |
|           | LO_EFF |          | Any         | co       |           |
|           |        | default  | proce       | mbustion |           |
|           |        | value:   | ss-specific | of       |           |
|           |        | none     | FLO_EMIS /  | c        |           |
|           |        |          | FLO_EFF     | ommodity |           |
|           |        | Default  | with the    | (c) in   |           |
|           |        | i/e: STD | commodities | region   |           |
|           |        |          | c and com   | (r).     |           |
|           |        |          | will        |          |           |
|           |        |          | override    |          |           |
|           |        |          | VDA_EMCB.   |          |           |
+-----------+--------+----------+-------------+----------+-----------+

: Table 13: User input parameters in TIMES

##  Internal parameters

Table 14 gives an overview of internal parameters generated by the TIMES preprocessor. Similar to the description of the internal sets, not all internal parameters used within TIMES are discussed. The list given in Table 14 focuses mainly on the parameters used in the preparation and creation of the equations in Chapter 6. In addition to the internal parameters listed here, the TIMES preprocessor computes additional internal parameters which are either used only as auxiliary parameters being valid only in a short section of the code or which are introduced to improve the performance of the code regarding computational time.

+------------+--------------------+------------------------------------+
| **Internal | **Instances**      | **Description**                    |
| parame     |                    |                                    |
| ter**[^31] | **(Required / Omit |                                    |
|            | / Special          |                                    |
| **(        | conditions)**      |                                    |
| Indexes)** |                    |                                    |
+============+====================+====================================+
| ALPH       | For learning       | Axis intercept on cumulative cost  |
|            | technologies teg   | axis for description of linear     |
| (r,kp,teg) | when ETL is used.  | equation valid for segment kp.     |
+------------+--------------------+------------------------------------+
| BETA       | For learning       | Slope of cumulative cost curve in  |
|            | technologies teg   | segment kp ( = specific investment |
| (r,kp,teg) | when ETL is used.  | cost).                             |
+------------+--------------------+------------------------------------+
| CCAPK      | For learning       | Cumulative capacity at kinkpoint   |
|            | technologies teg   | kp.                                |
| (r,kp,teg) | when ETL is used.  |                                    |
+------------+--------------------+------------------------------------+
| CCO        | For learning       | Initial cumulative cost of         |
| ST0(r,teg) | technologies teg   | learning technology teg.           |
|            | when ETL is used.  |                                    |
+------------+--------------------+------------------------------------+
| CCOSTK     | For learning       | Cumulative investment cost at      |
|            | technologies teg   | kinkpoint kp.                      |
| (r,kp,teg) | when ETL is used.  |                                    |
+------------+--------------------+------------------------------------+
| CCOSTM     | For learning       | Maximum cumulative cost based on   |
|            | technologies teg   | CCAPM.                             |
| (r,teg)    | when ETL is used.  |                                    |
+------------+--------------------+------------------------------------+
| COEF_AF    | For each           | Availability coefficient of the    |
|            | technology, at the | capacity (new investment variable  |
| (r,v       | level of process   | VAR_NCAP plus still existing past  |
| ,t,p,s,bd) | operation          | investments NCAP_PASTI) in         |
|            | (PRC_TSL).         | EQ(l)\_CAPACT; COEF_AF is derived  |
|            |                    | from the availability input        |
|            |                    | parameters NCAP_AF, NCAP_AFA and   |
|            |                    | NCAP_AFS taking into account any   |
|            |                    | specified MULTI or SHAPE           |
|            |                    | multipliers.                       |
+------------+--------------------+------------------------------------+
| COEF_CPT   | For each           | Fraction of capacity built in      |
|            | technology the     | period v that is available in      |
| (r,v,t,p)  | amount of an       | period t; might be smaller than 1  |
|            | investment         | due to NCAP_ILED in vintage period |
|            | (VAR_NCAP)         | or the fact that the lifetime ends |
|            | available in the   | within a period.                   |
|            | period.            |                                    |
+------------+--------------------+------------------------------------+
| COEF_ICOM  | Whenever there is  | Coefficient for commodity          |
|            | a commodity        | requirement during construction in |
| (          | required during    | period t due to investment         |
| r,v,t,p,c) | construction, the  | decision in period v (see also     |
|            | consuming being    | NCAP_ICOM).                        |
|            | taken from the     |                                    |
|            | balance constraint |                                    |
|            | (EQ(l)\_COMBAL).   |                                    |
|            |                    |                                    |
|            | Applied to the     |                                    |
|            | investment         |                                    |
|            | variable           |                                    |
|            | (VAR_NCAP) of      |                                    |
|            | period v in the    |                                    |
|            | commodity balance  |                                    |
|            | (EQ(l)\_COMBAL) of |                                    |
|            | period t.          |                                    |
|            |                    |                                    |
|            | The duration       |                                    |
|            | during which the   |                                    |
|            | commodity is       |                                    |
|            | produced starts in |                                    |
|            | the year           |                                    |
|            | B(v)+NCAP_ILE      |                                    |
|            | D(v)--NCAP_CLED(v) |                                    |
|            | and ends in the    |                                    |
|            | year               |                                    |
|            | B(v                |                                    |
|            | )+NCAP_ILED(v)--1. |                                    |
+------------+--------------------+------------------------------------+
| COEF_OCOM  | Whenever there is  | Coefficient for commodity release  |
|            | a commodity        | during decommissioning time in     |
| (          | released during    | period t due to investment made in |
| r,v,t,p,c) | decommissioning,   | period v.                          |
|            | the production     |                                    |
|            | being added to the |                                    |
|            | balance constraint |                                    |
|            | (EQ(l)\_COMBAL).   |                                    |
|            |                    |                                    |
|            | Applied to the     |                                    |
|            | investment         |                                    |
|            | variable           |                                    |
|            | (VAR_NCAP) of      |                                    |
|            | period v in the    |                                    |
|            | commodity balance  |                                    |
|            | (EQ(l)\_COMBAL) of |                                    |
|            | period t.          |                                    |
|            |                    |                                    |
|            | The release occurs |                                    |
|            | during the         |                                    |
|            | decommissioning    |                                    |
|            | lifetime           |                                    |
|            | NCAP_DLIFE.        |                                    |
+------------+--------------------+------------------------------------+
| COEF_PTRAN | For each flow      | Coefficient of flow variable of    |
|            | through a process. | commodity c belonging to commodity |
| (r         |                    | group cg in EQ_PTRANS equation     |
| ,v,t,p,cg, |                    | between the commodity groups cg    |
| c,com_grp) |                    | and com_grp.                       |
+------------+--------------------+------------------------------------+
| COEF_PVT   | For each region,   | Coefficient for the present value  |
|            | the present value  | of periods, used primarily for     |
| (r,t)      | of the time in     | undiscounting the solution         |
|            | each period.       | marginals.                         |
+------------+--------------------+------------------------------------+
| COEF_RPTI  | For each           | Number of repeated investment of   |
|            | technology whose   | process p in period v when the     |
| (r,v,p)    | technical life     | technical lifetime minus the       |
|            | (NCAP_TLIFE) is    | construction time is shorter than  |
|            | shorter than the   | the period duration; Rounded to    |
|            | period.            | the next largest integer number.   |
+------------+--------------------+------------------------------------+
| COR_SALVD  | For each           | Correction factor for              |
|            | technology         | decommissioning costs taking into  |
| (          | existing past the  | account technical discount rates   |
| r,v,p,cur) | end of the         | and economic decommissioning       |
|            | modelling horizon  | times.                             |
|            | with               |                                    |
|            | decommissioning    |                                    |
|            | costs, adjustment  |                                    |
|            | in the objective   |                                    |
|            | function.          |                                    |
+------------+--------------------+------------------------------------+
| COR_SALVI  | For each process   | Correction factor for investment   |
|            | extending past the | costs taking into account          |
| (          | end of the         | technical discount rates, economic |
| r,v,p,cur) | modelling horizon  | lifetimes and a user-defined       |
|            | adjustment in the  | discount shift (triggered by the   |
|            | objective          | control switch MIDYEAR (see        |
|            | function.          | Section 6.2 EQ_OBJ).               |
+------------+--------------------+------------------------------------+
| D          | For each period,   | Duration of period t.              |
|            | D(t) =             |                                    |
| \(t\)      | E(t)--B(t)+1.      |                                    |
+------------+--------------------+------------------------------------+
| DUR_MAX    | For the model.     | Maximum of NCAP_ILED +             |
|            |                    | NCAP_TLIFE + NCAP_DLAG +           |
|            |                    | NCAP_DLIFE + NCAP_DELIF over all   |
|            |                    | regions, periods and processes.    |
+------------+--------------------+------------------------------------+
| LEAD\      | For each milestone | Time between milestone years       |
| (t)        | year.              | **t**--1 and **t**, in years. For  |
|            |                    | the first milestone year t1,       |
|            |                    | LEAD(t1)=M(t1)--B(t1)+1.           |
+------------+--------------------+------------------------------------+
| M          | For each period,   | Middle year of period t.           |
|            | if the duration of |                                    |
| \(v\)      | the period is      |                                    |
|            | even, the middle   |                                    |
|            | year of the period |                                    |
|            | is B(t) + D(t)/2   |                                    |
|            | -- 1, if the       |                                    |
|            | period is uneven,  |                                    |
|            | the middle year is |                                    |
|            | B(t) + D(t)/2 --   |                                    |
|            | 0.5.               |                                    |
+------------+--------------------+------------------------------------+
| MINYR      | For the model      | Minimum year over t = M(t) -- D(t) |
|            |                    | +1; used in objective function.    |
+------------+--------------------+------------------------------------+
| MIYR_V1    | For the model      | First year of model horizon.       |
+------------+--------------------+------------------------------------+
| MIYR_VL    | For the model      | Last year of model horizon.        |
+------------+--------------------+------------------------------------+
| NTCHTEG    | For learning       | Number of processes using the same |
|            | technologies teg   | key technology teg.                |
| (r,teg)    | when ETL with      |                                    |
|            | technology         |                                    |
|            | clusters is used.  |                                    |
+------------+--------------------+------------------------------------+
| OBJ_ACOST  | For each process   | Inter-/Extrapolated variable costs |
|            | with activity      | (ACT_COST) for activity variable   |
| (          | costs.             | (VAR_ACT) for each year.           |
| r,y,p,cur) |                    |                                    |
|            | Enters the         |                                    |
|            | objective function |                                    |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_COMNT  | For each commodity | Inter-/Extrapolated cost, tax and  |
|            | with costs, taxes  | subsidy (distinguished by the type |
| (r,y,c,s   | or subsidies on    | index) on net production of        |
| ,type,cur) | the net            | commodity (c) for each year        |
|            | production.        | associated with the variable       |
|            |                    | VAR_COMNET. Cost types (type) are  |
|            | Enters the         | COST, TAX and SUB.                 |
|            | objective function |                                    |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_COMPD  | For each commodity | Inter-/Extrapolated cost, tax and  |
|            | with costs, taxes  | subsidy (distinguished by the type |
| (r,y,c,s   | or subsidies on    | index) on production of commodity  |
| ,type,cur) | the commodity      | (c) for each year associated with  |
|            | production.        | the variable VAR_COMPRD. Cost      |
|            |                    | types (type) are COST, TAX and     |
|            | Enters the         | SUB.                               |
|            | objective function |                                    |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_CRF    | For each           | Capital recovery factor of         |
|            | technology with    | investment in technology p in      |
| (          | investment costs.  | objective function taking into     |
| r,y,p,cur) |                    | account the economic lifetime      |
|            | Enters objective   | (NCAP_ELIFE) and the technology    |
|            | function           | specific discount rate             |
|            | (EQ_OBJINV).       | (NCAP_DRATE) or, if the latter is  |
|            |                    | not specified, the general         |
|            |                    | discount rate (G_DRATE).           |
+------------+--------------------+------------------------------------+
| OBJ_CRFD   | For each           | Capital recovery factor of         |
|            | technology with    | decommissioning costs in           |
| (          | decommissioning    | technology p taking into account   |
| r,y,p,cur) | costs.             | the economic lifetime (NCAP_DELIF) |
|            |                    | and the technology specific        |
|            | Enters objective   | discount rate (NCAP_DRATE) or, if  |
|            | function           | the latter is not specified, the   |
|            | (EQ_OBJINV).       | general discount rate (G_DRATE).   |
+------------+--------------------+------------------------------------+
| OBJ_DCEOH  | Enters objective   | Discount factor for the year EOH + |
|            | function           | 1 based on the general discount    |
| (r,cur)    | (EQ_OBJSALV).      | rate (G_DRATE).                    |
+------------+--------------------+------------------------------------+
| OBJ_DCOST  | For each           | Inter-/Extrapolated                |
|            | technology with    | decommissioning costs (NCAP_DCOST) |
| (          | decommissioning    | for each year related to the       |
| r,y,p,cur) | costs.             | investment (VAR_NCAP) of process   |
|            |                    | p.                                 |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJINV).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_DISC   | Enters objective   | Annual discount factor based on    |
|            | function           | the general discount rate          |
| (r,y,cur)  | (EQ_OBJINV,        | (G_DRATE) to discount costs in the |
|            | EQ_OBJVAR,         | year y to the base year (G_DYEAR). |
|            | EQ_OBJFIX,         |                                    |
|            | EQ_OBJSALV,        |                                    |
|            | EQ_OBJELS).        |                                    |
+------------+--------------------+------------------------------------+
| OBJ_DIVI   | Enters objective   | Divisor for investment costs       |
|            | function           | (period duration, technical        |
| (r,v,p)    | (EQ_OBJINV).       | lifetime or investment lead time   |
|            |                    | depending on the investment cases  |
|            |                    | 1a, 1b, 2a, 2b).                   |
+------------+--------------------+------------------------------------+
| OBJ_DIVIII | Enters objective   | Divisor for decommissioning costs  |
|            | function           | and salvaging of decommissioning   |
| (r,v,p)    | (EQ_OBJINV).       | costs (period duration, technical  |
|            |                    | lifetime or decommissioning time   |
|            |                    | depending on the investment cases  |
|            |                    | 1a, 1b, 2a, 2b).                   |
+------------+--------------------+------------------------------------+
| OBJ_DIVIV  | Enters objective   | Divisor for fixed operating and    |
|            | function           | maintenance costs and salvaging of |
| (r,v,p)    | (EQ_OBJFIX).       | investment costs.                  |
+------------+--------------------+------------------------------------+
| OBJ_DLAGC  | Enters objective   | Inter-/Extrapolated fixed capacity |
|            | function           | (VAR_NCAP+NCAP_PASTI) costs        |
| (          | (EQ_OBJFIX).       | between the end of the technical   |
| r,y,p,cur) |                    | lifetime and the beginning of the  |
|            |                    | decommissioning for each year.     |
+------------+--------------------+------------------------------------+
| OBJ_FCOST  | For each flow      | Inter-/Extrapolated flow costs     |
|            | variable with flow | (FLO_COST) for each year for the   |
| (r,y,      | related costs.     | flow or trade variable (VAR_FLO,   |
| p,c,s,cur) |                    | VAR_IRE) as well as capacity       |
|            | Enters objective   | related flows (specified by        |
|            | function           | NCAP_COM, NCP_ICOM, NCAP_OCOM).    |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_FDELV  | For each flow with | Inter-/Extrapolated delivery costs |
|            | delivery costs.    | (FLO_DELIV) for each year for the  |
| (r,y,      |                    | flow or trade variable (VAR_FLO,   |
| p,c,s,cur) | Enters objective   | VAR_IRE) as well as capacity       |
|            | function           | related flows (specified by        |
|            | (EQ_OBJVAR).       | NCAP_COM, NCP_ICOM, NCAP_OCOM).    |
+------------+--------------------+------------------------------------+
| OBJ_FOM    | For each process   | Inter-/Extrapolated fixed          |
|            | with fixed         | operating and maintenance costs    |
| (          | operating and      | (NCAP_FOM) for the installed       |
| r,y,p,cur) | maintenance costs. | capacity (VAR_NCAP+NCAP_PASTI) for |
|            |                    | each year.                         |
|            | Enters the         |                                    |
|            | objective function |                                    |
|            | (EQ_OBJFIX).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_FSB    | For each process   | Inter-/Extrapolated subsidy        |
|            | with subsidy on    | (NCAP_FSUB) on installed capacity  |
| (          | existing capacity. | (VAR_NCAP+NCAP_PASTI) for each     |
| r,y,p,cur) |                    | year.                              |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJFIX).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_FSUB   | For each flow      | Inter-/Extrapolated subsidy        |
|            | variable with      | (FLO_SUB) for the flow or trade    |
| (r,y,      | subsidies.         | variable (VAR_FLO, VAR_IRE) for    |
| p,c,s,cur) |                    | each year as well as capacity      |
|            | Enters objective   | related flows (specified by        |
|            | function           | NCAP_COM, NCP_ICOM, NCAP_OCOM).    |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_FTAX   | For each flow      | Inter-/Extrapolated tax (FLO_TAX)  |
|            | variable with      | for flow or trade variable         |
| (r,y,      | taxes.             | (VAR_FLO, VAR_IRE) for each year   |
| p,c,s,cur) |                    | as well as capacity related flows  |
|            | Enters objective   | (specified by NCAP_COM, NCP_ICOM,  |
|            | function           | NCAP_OCOM).                        |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_FTX    | For each process   | Inter-/Extrapolated tax            |
|            | with taxes on      | (NCAP_FTAX) on installed capacity  |
| (          | existing capacity. | (VAR_NCAP+NCAP_PASTI) for each     |
| r,y,p,cur) |                    | year.                              |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJFIX).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_ICOST  | For each process   | Inter-/Extrapolated investment     |
|            | with investment    | costs (NCAP_COST) for investment   |
| (          | costs.             | variable (VAR_NCAP) for each year. |
| r,y,p,cur) |                    |                                    |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJINV).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_IPRIC  | For each           | Inter-/Extrapolated import/export  |
|            | import/export flow | prices (IRE_PRICE) for             |
| (r,y       | with prices        | import/export variable (VAR_IRE)   |
| ,p,c,s,all | assigned to it.    | for each year.                     |
| _r,ie,cur) |                    |                                    |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJVAR).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_ISUB   | For each process   | Inter-/Extrapolated subsidy        |
|            | with subsidy on    | (NCAP_ISUB) on new capacity        |
| (          | new investment.    | (VAR_NCAP) for each year.          |
| r,y,p,cur) |                    |                                    |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJINV).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_ITAX   | For each process   | Inter-/Extrapolated tax            |
|            | with taxes on new  | (NCAP_ITAX) on new capacity        |
| (          | investment.        | (VAR_NCAP) for each year.          |
| r,y,p,cur) |                    |                                    |
|            | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJINV).       |                                    |
+------------+--------------------+------------------------------------+
| OBJ_PASTI  | Enters objective   | Correction factor for past         |
|            | function           | investments.                       |
| (          | (EQ_OBJINV).       |                                    |
| r,v,p,cur) |                    |                                    |
+------------+--------------------+------------------------------------+
| OBJ_PVT\   | Used as a          | Present value of time (in years)   |
| (r,t,cur)  | multiplier in      | in period **t**, according to      |
|            | objective function | currency **cur** in region **r**,  |
|            | in a few sparse    | discounted to the base year.       |
|            | cases.             |                                    |
+------------+--------------------+------------------------------------+
| OBJSIC     | For learning       | Investment cost related salvage    |
|            | technologies.      | value of learning technology teg   |
| (r,v,teg)  |                    | with vintage period v at year      |
|            | Enters objective   | EOH+1.                             |
|            | function           |                                    |
|            | (EQ_OBJINV).       |                                    |
+------------+--------------------+------------------------------------+
| OBJSSC     | For processes with | Investment cost related salvage    |
|            | investment costs.  | value of process p with vintage    |
| (          |                    | period v at year EOH+1.            |
| r,v,p,cur) | Enters objective   |                                    |
|            | function           |                                    |
|            | (EQ_OBJSALV).      |                                    |
+------------+--------------------+------------------------------------+
| PAT        | For learning       | Learning curve coefficient in the  |
|            | technologies teg   | relationship:                      |
| (r,teg)    | when ETL is used.  |                                    |
|            |                    | SC = PAT \* VAR_CCAP\^(-PBT).      |
+------------+--------------------+------------------------------------+
| PBT        | For learning       | Learning curve exponent PBT(r,teg) |
|            | technologies teg   | = LOG(PRAT(r,teg))/LOG(2).         |
| (r,teg)    | when ETL is used.  |                                    |
+------------+--------------------+------------------------------------+
| PYR_V1     | For the model      | Minimum of pastyears and MINYR.    |
+------------+--------------------+------------------------------------+
| RS_FR      | Defined for all    | Fraction of timeslice s in         |
|            | commodities.       | timeslice ts, if s is below ts,    |
| (r,s,ts)   | Applied to flow    | otherwise 1. In other words,       |
|            | variables in all   | RS_FR(r,s,ts) = G_YRFR(r,s) /      |
|            | equations in order | G_YRFR(r,ts), if s is below ts,    |
|            | to take into       | and otherwise 1.                   |
|            | account cases      |                                    |
|            | where the          |                                    |
|            | variables may be   |                                    |
|            | defined at a       |                                    |
|            | different          |                                    |
|            | timeslice level    |                                    |
|            | than the level of  |                                    |
|            | the equation.      |                                    |
+------------+--------------------+------------------------------------+
| RS_STG\    | Mainly applied for | Lead from previous timeslice in    |
| (r,s)      | the modelling of   | the same cycle under the parent    |
|            | storace cycles,    | timeslice.                         |
|            | but also in        |                                    |
|            | dispatching        |                                    |
|            | equations.         |                                    |
+------------+--------------------+------------------------------------+
| RS_STGAV   | Only applicable to | Average residence time of storage  |
|            | storage processes  | activity.                          |
| (r,s)      | (STG): timeslice   |                                    |
|            | storage devices,   |                                    |
|            | to calculate       |                                    |
|            | activity costs in  |                                    |
|            | proportion to the  |                                    |
|            | time the commodity |                                    |
|            | is stored.         |                                    |
+------------+--------------------+------------------------------------+
| RS_STGPRD  | Only applicable to | Number of storage periods in a     |
|            | storage processes  | year for each timeslice.           |
| (r,s)      | (STG): timeslice   |                                    |
|            | storage,           |                                    |
|            | inter-period       |                                    |
|            | storage or night   |                                    |
|            | storage devices.   |                                    |
+------------+--------------------+------------------------------------+
| RS_UCS\    | Applied in         | Lead from previous timeslice in    |
| (r,s,side) | timeslice-dynamic  | the same cycle under the parent    |
|            | user constraints,  | timeslice.                         |
|            | to refer to the    |                                    |
|            | previous timeslice |                                    |
|            | in the same cycle. |                                    |
+------------+--------------------+------------------------------------+
| RTP_FFCX   | The efficiency     | Average SHAPE multiplier of the    |
|            | parameter          | parameter FLO_FUNC and FLO_SUM     |
| (r,v,t,    | COEF_PTRAN is      | efficiencies in the EQ_PTRANS      |
| p,cg,c,cg) | multiplied by the  | equation in the period (t) for     |
|            | factor             | capacity with vintage period (v).  |
|            | (1+RTP_FFCX).      | The SHAPE curve that should be     |
|            |                    | used is specified by the user      |
|            | Enters EQ_PTRANS   | parameter FLO_FUNCX. The SHAPE     |
|            | equation.          | feature allows to alter technical  |
|            |                    | parameter given for the vintage    |
|            |                    | period as a function of the age of |
|            |                    | the installation.                  |
+------------+--------------------+------------------------------------+
| RTCS_TSFR  | Defined for each   | The effective handling of          |
|            | commodity with     | timeslice                          |
| (r         | COM_FR. Applied to | aggregation/disaggregation. If ts  |
| ,t,c,s,ts) | flow variables in  | is below s in the timeslice tree,  |
|            | all equations in   | the value is 1, if s is below ts   |
|            | order to take into | the value is COM_FR(r,s) /         |
|            | account cases      | COM_FR(r,ts) for demand            |
|            | where some of the  | commodities with COM_FR given and  |
|            | variables may be   | G_YRFR(r,s) / G_YRFR(r,ts) for all |
|            | defined at a       | other commodities.                 |
|            | different          |                                    |
|            | timeslice level    | The parameter is used to match the |
|            | than the level of  | timeslice resolution of flow       |
|            | the equation.      | variables (VAR_FLO/VAR_IRE) and    |
|            |                    | commodities. RTCS_TSFR is the      |
|            |                    | coefficient of the flow variable,  |
|            |                    | which is producing or consuming    |
|            |                    | commodity c, in the commodity      |
|            |                    | balance of c. If timeslice s       |
|            |                    | corresponds to the commodity       |
|            |                    | timeslice resolution of c and      |
|            |                    | timeslice ts to the timeslice      |
|            |                    | resolution of the flow variable    |
|            |                    | two cases may occur:               |
|            |                    |                                    |
|            |                    | The flow variables are on a finer  |
|            |                    | timeslice level than the commodity |
|            |                    | balance: in this case the flow     |
|            |                    | variables with timeslices s being  |
|            |                    | below ts in the timeslice tree are |
|            |                    | summed to give the aggregated flow |
|            |                    | within timeslice ts. RTCS_TSFR has |
|            |                    | the value 1.                       |
|            |                    |                                    |
|            |                    | The flow variables are on coarser  |
|            |                    | timeslice level than the commodity |
|            |                    | balance: in this case the flow     |
|            |                    | variable is split-up on the finer  |
|            |                    | timeslice level of the commodity   |
|            |                    | balance according to the ratio of  |
|            |                    | the timeslice duration of s to ts: |
|            |                    | RTCS_TSFR has the value =          |
|            |                    | COM_FR(r,s) / COM_FR(r,s1) for     |
|            |                    | demand commodities and G_YRFR(r,s) |
|            |                    | / G_YRFR(r,s1) otherwise. When     |
|            |                    | COM_FR is used, the demand load    |
|            |                    | curve is moved to the demand       |
|            |                    | process. Thus, it is possible to   |
|            |                    | model demand processes on an       |
|            |                    | ANNUAL level and ensure at the     |
|            |                    | same time that the process follows |
|            |                    | the given load curve COM_FR.       |
+------------+--------------------+------------------------------------+
| SALV_DEC   | For those          | Salvage proportion of              |
|            | technologies with  | decommissioning costs made at      |
| (r         | salvage costs      | period v with commissioning year   |
| ,v,p,k,ll) | incurred after the | k.                                 |
|            | model horizon the  |                                    |
|            | contribution to    |                                    |
|            | the objective      |                                    |
|            | function.          |                                    |
+------------+--------------------+------------------------------------+
| SALV_INV   | For those          | Salvage proportion of investment   |
|            | technologies with  | made at period v with              |
| (r,v,p,k)  | salvage costs      | commissioning year k.              |
|            | incurred after the |                                    |
|            | model horizon the  |                                    |
|            | contribution to    |                                    |
|            | the objective      |                                    |
|            | function.          |                                    |
+------------+--------------------+------------------------------------+
| YEARVAL    | A value for each   | Numerical value of year index      |
|            | year.              | (e.g. YEARVAL(\'1984\') equals     |
| \(y\)      |                    | 1984).                             |
+------------+--------------------+------------------------------------+

: Table 14: Internal parameters in TIMES

##  Report parameters

### Overview of report parameters

The parameters generated internally by TIMES to document the results of a model run are listed in Table 15. These parameters can be imported into the **VEDA-BE** tool for further result analysis. They are converted out of the **GDX**[^32] file via the **gdx2veda** GAMS utility into a **VEDA-BE** compatible format according to the file **times2veda.vdd**[^33]. Note that some of the results are not transferred into parameters, but are directly accessed through the **times2veda.vdd** file (levels of commodity balances and peaking equation, total discounted value of objective function). The following naming conventions apply to the prefixes of the report parameters:
- CST\_: detailed annual undiscounted cost parameters; note that also the costs of past investments, which are constants in the objective function, are being reported;
- $PAR\_$: various primal and dual solution parameters;
- $EQ(l)\_$: directly accessed GAMS equation levels/marginals
- $REG\_$: regional total cost indicators.


| Report parameter<sup>[^34]</sup> (Indexes) | VEDA-BE attribute name | Description |
| --- | --- | --- |
| AGG_OUT <br> (r,t,c,s) </br>    | VAR_FOut   | Commodity production by an aggregation process: <br> Production of commodity (c) in period (t) and timeslice (s) from other commodities aggregated into c. </br>|
| CAP_NEW <br> (r,v,p,t,uc_n) </br>  | Cap_New  | Newly installed capacity and lumpsum investment by vintage and commissioning period: <br> New capacity and lumpsum investment of process (p) of vintage (v) commissioned in period (t). </br>|

+--------+-------+-----------------------------------------------------+
| CM_R   | V     | Climate module results for the levels of climate    |
| ESULT\ | AR_Cl | variable (c) in period (t).                         |
| (c,t)  | imate |                                                     |
+--------+-------+-----------------------------------------------------+
| CM_M   | Dual  | Climate module results for the duals of constraint  |
| AXC_M\ | _Clic | related to climate variable (c) in period (t).      |
| (c,t)  |       |                                                     |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual activity costs:                              |
| _ACTC\ | t_Act |                                                     |
| (r     |       | Annual undiscounted variable costs (caused by       |
| ,v,t,p |       | ACT_COST) in period (t) associated with the         |
| ,uc_n) |       | operation (activity) of a process (p) with vintage  |
|        |       | period (v). Additional indicator (uc_n) for         |
|        |       | start-up costs.                                     |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual commodity costs:                             |
| _COMC\ | t_Com |                                                     |
| (      |       | Annual undiscounted costs for commodity (c) (caused |
| r,t,c) |       | by COM_CSTNET and COM_CSTPRD) in period (t).        |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual elastic demand cost term:                    |
| _COME\ | t_Els |                                                     |
| (      |       | Annual costs (losses) due to elastic demand changes |
| r,t,c) |       | of commodity (c). When elastic demands are used the |
|        |       | objective function describes the total surplus of   |
|        |       | producers and consumers, which reaches its maximum  |
|        |       | in the equilibrium of demand and supply.            |
+--------+-------+-----------------------------------------------------+
| CST    | Cost  | Annual commodity taxes/subsidies:                   |
| _COMX\ | _Comx |                                                     |
| (      |       | Annual undiscounted taxes and subsidies for         |
| r,t,c) |       | commodity (c) (caused by COM_TAXNET, COM_SUBNET,    |
|        |       | COM_TAXPRD, COM_SUBPRD) in period (t).              |
+--------+-------+-----------------------------------------------------+
| CS     | Cos   | Annual damage cost term:                            |
| T_DAM\ | t_Dam |                                                     |
| (      |       | Annual undiscounted commodity (c) related costs,    |
| r,t,c) |       | caused by DAM_COST, in period (t).                  |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual decommissioning costs:                       |
| _DECC\ | t_Dec |                                                     |
| (r,    |       | Annual undiscounted decommissioning costs (caused   |
| v,t,p) |       | by NCAP_DCOST and NCAP_DLAGC) in period (t),        |
|        |       | associated with the dismantling of process (p) with |
|        |       | vintage period (v).                                 |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual fixed operating and maintenance costs:       |
| _FIXC\ | t_Fom |                                                     |
| (r,    |       | Annual undiscounted fixed operating and maintenance |
| v,t,p) |       | costs (caused by NCAP_FOM) in period (t) associated |
|        |       | with the installed capacity of process (p) with     |
|        |       | vintage period (v).                                 |
+--------+-------+-----------------------------------------------------+
| CST    | Cost  | Annual fixed taxes/subsidies:                       |
| _FIXX\ | _Fixx |                                                     |
| (r,    |       | Annual undiscounted fixed operating and maintenance |
| v,t,p) |       | costs (caused by NCAP_FTAX, NCAP_FSUB) in period    |
|        |       | (t) associated with the installed capacity of       |
|        |       | process (p) with vintage period (v).                |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual flow costs (including import/export prices): |
| _FLOC\ | t_Flo |                                                     |
| (r,v,  |       | Annual undiscounted flow related costs (caused by   |
| t,p,c) |       | FLO_COST, FLO_DELV, IRE_PRICE) in period (t)        |
|        |       | associated with a commodity (c) flow in/out of a    |
|        |       | process (p) with vintage period (v) as well as      |
|        |       | capacity related commodity flows (specified by      |
|        |       | NCAP_COM, NCAP_ICOM, NCAP_OCOM).                    |
+--------+-------+-----------------------------------------------------+
| CST    | Cost  | Annual flow taxes/subsidies:                        |
| _FLOX\ | _Flox |                                                     |
| (r,v,  |       | Annual undiscounted flow related costs (caused by   |
| t,p,c) |       | FLO_TAX, FLO_SUB) in period (t) associated with a   |
|        |       | commodity (c) flow in/out of a process (p) with     |
|        |       | vintage period (v) as well as capacity related      |
|        |       | commodity flows (specified by NCAP_COM, NCAP_ICOM,  |
|        |       | NCAP_OCOM).                                         |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual investment costs:                            |
| _INVC\ | t_Inv |                                                     |
| (r     |       | Annual undiscounted investment costs (caused by     |
| ,v,t,p |       | NCAP_COST) in period (t) spread over the economic   |
| ,uc_n) |       | lifetime (NCAP_ELIFE) of a process (p) with vintage |
|        |       | period (v).                                         |
+--------+-------+-----------------------------------------------------+
| CST    | Cost  | Annual investment taxes/subsidies:                  |
| _INVX\ | _Invx |                                                     |
| (r     |       | Annual undiscounted investment costs (caused by     |
| ,v,t,p |       | NCAP_ITAX, NCAP_ISUB) in period (t) spread over the |
| ,uc_n) |       | economic lifetime (NCAP_ELIFE) of a process (p)     |
|        |       | with vintage period (v).                            |
+--------+-------+-----------------------------------------------------+
| CST    | Cos   | Annual implied costs of endogenous trade:           |
| _IREC\ | t_ire |                                                     |
| (r,v,  |       | Annual undiscounted costs from endogenous           |
| t,p,c) |       | imports/exports of commodity (c) in period (t)      |
|        |       | associated with process (p) and vintage period (v), |
|        |       | valued according to the marginal(s) of the trade    |
|        |       | equation of process p.                              |
+--------+-------+-----------------------------------------------------+
| CS     | Cos   | Total discounted costs by commodity (optional,      |
| T_PVC\ | t_NPV | activate by setting RPT_OPT(\'OBJ\',\'1\')=1):      |
| (uc_   |       |                                                     |
| n,r,c) |       | Total present value of commodity-related costs in   |
|        |       | the base year, by type (with types COM, ELS, DAM).  |
|        |       | See Part III, Section 3.10 on the reporting         |
|        |       | options, and Table 16 below for acronym             |
|        |       | explanations.                                       |
+--------+-------+-----------------------------------------------------+
| CS     | Cos   | Total discounted costs by process (optional,        |
| T_PVP\ | t_NPV | activate by setting RPT_OPT(\'OBJ\',\'1\')=1):      |
| (uc_   |       |                                                     |
| n,r,p) |       | Total present value of process-related costs in the |
|        |       | base year, by type (with types INV, INV+, FIX, ACT, |
|        |       | FLO, IRE, where INV+ is only used for the split     |
|        |       | according to hurdle rate). See Part III, Section    |
|        |       | 3.10 on the reporting options, and Table 16 below   |
|        |       | for acronym explanations.                           |
+--------+-------+-----------------------------------------------------+
| CST    | Cost  | Salvage values of capacities at EOH+1:              |
| _SALV\ | _Salv |                                                     |
| (      |       | Salvage value of investment cost, taxes and         |
| r,v,p) |       | subsidies of process (p) with vintage period (v),   |
|        |       | for which the technical lifetime exceeds the end of |
|        |       | the model horizon, value at year EOH+1.             |
+--------+-------+-----------------------------------------------------+
| CST    | Tim   | Discounted value of time by period:                 |
| _TIME\ | e_NPV |                                                     |
| (r,t,s |       | Present value of the time in each model period (t)  |
| ,uc_n) |       | by region (r), with s=\'ANNUAL\' and                |
|        |       | uc_n=\'COST\'/\'LEVCOST\' depending on whether the  |
|        |       | \$SET ANNCOST LEV reporting option has been used.   |
+--------+-------+-----------------------------------------------------+
| EQ_P   | EQ    | Peaking Constraint Slack:                           |
| EAK.L\ | _Peak |                                                     |
| (r,    |       | Level of the peaking equation (EQ_PEAK) of          |
| t,c,s) |       | commodity (c) in period (t) and timeslice (s).      |
+--------+-------+-----------------------------------------------------+
| E      | EQ_C  | Commodity Slack/Levels:                             |
| QE_COM | ombal |                                                     |
| BAL.L\ |       | Level of the commodity balance equation             |
| (r,    |       | (EQE_COMBAL) of commodity (c) in period (t) and     |
| t,c,s) |       | timeslice (s), where the equation is a strict       |
|        |       | equality.                                           |
+--------+-------+-----------------------------------------------------+
| E      | EQ_C  | Commodity Slack/Levels:                             |
| QG_COM | ombal |                                                     |
| BAL.L\ |       | Level of the commodity balance equation             |
| (r,    |       | (EQG_COMBAL) of commodity (c) in period (t) and     |
| t,c,s) |       | timeslice (s), where the equation is an inequality. |
+--------+-------+-----------------------------------------------------+
| F_IN\  | VA    | Commodity Consumption by Process:                   |
| (      | R_FIn |                                                     |
| r,v,t, |       | Input flow (consumption) of commodity (c) in period |
| p,c,s) |       | (t) and timeslice (s) into process (p) with vintage |
|        |       | period (v), including exchange processes.           |
+--------+-------+-----------------------------------------------------+
| F_OUT\ | VAR   | Commodity Production by Process:                    |
| (      | _FOut |                                                     |
| r,v,t, |       | Output flow (production) of commodity (c) in period |
| p,c,s) |       | (t) and timeslice (s) from process (p) with vintage |
|        |       | period (v), including exchange processes.           |
+--------+-------+-----------------------------------------------------+
| O      | ObjZ  | Total discounted system cost:                       |
| BJZ.L\ |       |                                                     |
| ()     |       | Level of the ObjZ variable, equal to the value of   |
|        |       | the objective function.                             |
+--------+-------+-----------------------------------------------------+
| P_OUT\ | VAR   | Commodity Flow Levels by Process (set               |
| (r,t,  | _POut | RPT_OPT(NRG_TYPE,\'1\')=1 to activate, see Part     |
| p,c,s) |       | III):                                               |
|        |       |                                                     |
|        |       | Output flow level (power level) of commodity (c) in |
|        |       | period (t) and timeslice (s) of process (p). By     |
|        |       | default only Output levels are reported, but with   |
|        |       | RPT_OPT(NRG_TYPE,\'3\')=2, input levels are         |
|        |       | reported as negative values.                        |
+--------+-------+-----------------------------------------------------+
| PAR    | VA    | Process Activity:                                   |
| _ACTL\ | R_Act |                                                     |
| (r,v,  |       | Level value of activity variable (VAR_ACT) in       |
| t,p,s) |       | period (t), timeslice (s) of process (p) in vintage |
|        |       | period (v).                                         |
+--------+-------+-----------------------------------------------------+
| PAR    | VAR   | Process Activity -- Marginals:                      |
| _ACTM\ | _ActM |                                                     |
| (r,v,  |       | Undiscounted annual reduced costs of activity       |
| t,p,s) |       | variable (VAR_ACT) in period (t) and timeslice (s)  |
|        |       | of process (p) with vintage period (v); when the    |
|        |       | variable is at its lower (upper) bound, the reduced |
|        |       | cost describes the increase (decrease) in the       |
|        |       | objective function caused by an increase of the     |
|        |       | lower (upper) bound by one unit; the reduced cost   |
|        |       | can also be interpreted as the necessary decrease   |
|        |       | or increase of the cost coefficient of the activity |
|        |       | variable in the objective function, for the         |
|        |       | activity variable to leave its lower (upper) bound. |
+--------+-------+-----------------------------------------------------+
| PAR    | VA    | Technology Capacity:                                |
| _CAPL\ | R_Cap |                                                     |
| (      |       | Capacity of process (p) in period (t), derived from |
| r,t,p) |       | VAR_NCAP in previous periods summed over all        |
|        |       | vintage periods. For still existing past            |
|        |       | investments, see PAR_PASTI.                         |
+--------+-------+-----------------------------------------------------+
| PAR_   | PAR_  | Capacity Lower Limit:                               |
| CAPLO\ | CapLO |                                                     |
| (      |       | Lower bound on capacity variable (CAP_BND('LO')),   |
| r,t,p) |       | only reported, if the lower bound is greater than   |
|        |       | zero.                                               |
+--------+-------+-----------------------------------------------------+
| PAR    | VAR   | Technology Capacity -- Marginals:                   |
| _CAPM\ | _CapM |                                                     |
| (      |       | Undiscounted reduced costs of capacity variable     |
| r,t,p) |       | (VAR_CAP); only reported in those cases, in which   |
|        |       | the capacity variable is generated (bound CAP_BND   |
|        |       | specified or endogenous technology learning is      |
|        |       | used); the reduced costs describe in the case, that |
|        |       | the capacity variable is at its lower (upper)       |
|        |       | bound, the cost increase (decrease) of the          |
|        |       | objective function caused by an increase of the     |
|        |       | lower (upper) bound by one unit. The reduced cost   |
|        |       | is undiscounted with COEF_PVT.                      |
+--------+-------+-----------------------------------------------------+
| PAR_   | PAR_  | Capacity Upper Limit:                               |
| CAPUP\ | CapUP |                                                     |
| (      |       | Upper bound on capacity variable (CAP_BND('UP')),   |
| r,t,p) |       | only reported, if upper bound is smaller than       |
|        |       | infinity.                                           |
+--------+-------+-----------------------------------------------------+
| P      | EQ_Co | Commodity Slack/Levels -- Marginals:                |
| AR_COM | mbalM |                                                     |
| BALEM\ |       | Undiscounted annual shadow price of commodity       |
| (r,    |       | balance (EQE_COMBAL) being a strict equality. The   |
| t,c,s) |       | marginal value describes the cost increase in the   |
|        |       | objective function, if the difference between       |
|        |       | production and consumption is increased by one      |
|        |       | unit. The marginal value can be determined by the   |
|        |       | production side (increasing production), but can    |
|        |       | also be set by the demand side (e.g., decrease of   |
|        |       | consumption by energy saving or substitution        |
|        |       | measures).                                          |
+--------+-------+-----------------------------------------------------+
| P      | EQ_Co | Commodity Slack/Levels -- Marginals:                |
| AR_COM | mbalM |                                                     |
| BALGM\ |       | Undiscounted annual shadow price of commodity       |
| (r,    |       | balance (EQG_COMBAL) being an inequality            |
| t,c,s) |       | (production being greater than or equal to          |
|        |       | consumption); positive number, if production equals |
|        |       | consumption; the marginal value describes the cost  |
|        |       | increase in the objective function, if the          |
|        |       | difference between production and consumption is    |
|        |       | increased by one unit. The marginal value can be    |
|        |       | determined by the production side (increasing       |
|        |       | production), but can also be set by the demand side |
|        |       | (e.g., decrease of consumption by energy saving or  |
|        |       | substitution measures).                             |
+--------+-------+-----------------------------------------------------+
| PAR_CO | VAR_C | Commodity Net:                                      |
| MNETL\ | omnet |                                                     |
| (r,    |       | Level value of the variable corresponding the net   |
| t,c,s) |       | level of a commodity (c) (VAR_COMNET). The net      |
|        |       | level of a commodity is equivalent to the total     |
|        |       | production minus total consumption of said          |
|        |       | commodity. It is only reported, if a bound or cost  |
|        |       | is specified for it or it is used in a user         |
|        |       | constraint.                                         |
+--------+-------+-----------------------------------------------------+
| PAR_CO | V     | Commodity Net -- Marginal:                          |
| MNETM\ | AR_Co |                                                     |
| (r,    | mnetM | Undiscounted annual reduced costs of the VAR_COMNET |
| t,c,s) |       | variable of commodity (c). It is only reported, if  |
|        |       | a bound or cost is specified for it or it is used   |
|        |       | in a user constraint.                               |
+--------+-------+-----------------------------------------------------+
| PAR_CO | VAR_C | Commodity Total Production:                         |
| MPRDL\ | omprd |                                                     |
| (r,    |       | Level value of the commodity production variable    |
| t,c,s) |       | (VAR_COMPRD). The variable represents the total     |
|        |       | production of a commodity. It is only reported, if  |
|        |       | a bound or cost is specified for it or it is used   |
|        |       | in a user constraint.                               |
+--------+-------+-----------------------------------------------------+
| PAR_CO | V     | Commodity Total Production -- Marginal:             |
| MPRDM\ | AR_Co |                                                     |
| (r,    | mprdM | Undiscounted annual reduced costs of the commodity  |
| t,c,s) |       | production variable (VAR_COMPRD). It is only        |
|        |       | reported, if a bound or cost is specified for it or |
|        |       | it is used in a user constraint.                    |
+--------+-------+-----------------------------------------------------+
| PAR_C  | VAR_C | Cumulative costs by type (if constrained);\         |
| UMCST\ | umCst | Level of cumulative constraint for costs of type    |
| (r     |       | (uc_n) and currency (c) in region (r).              |
| ,v,t,u |       |                                                     |
| c_n,c) |       |                                                     |
+--------+-------+-----------------------------------------------------+
| PAR_CU | EQ_C  | Cumulative flow constraint -- Levels:               |
| MFLOL\ | umflo |                                                     |
| (r,p,  |       | Level of cumulative constraint for flow of          |
| c,v,t) |       | commodity (c) of process (p) between the year range |
|        |       | (v--t).                                             |
+--------+-------+-----------------------------------------------------+
| PAR_CU | EQ_Cu | Cumulative flow constraint -- Marginals:            |
| MFLOM\ | mfloM |                                                     |
| (r,p,  |       | Shadow price of cumulative constraint for flow of   |
| c,v,t) |       | commodity (c) of process (p) between the year range |
|        |       | (v--t). Not undiscounted.                           |
+--------+-------+-----------------------------------------------------+
| PAR    | VAR   | Electricity supply by technology and energy source  |
| _EOUT\ | _Eout | (optional):                                         |
| (r,v,  |       |                                                     |
| t,p,c) |       | Electricity output of electricity supply processes  |
|        |       | by energy source; based on using NRG_TMAP to        |
|        |       | identify electricity commodities, but excludes      |
|        |       | standard and storage processes having electricity   |
|        |       | as input.                                           |
|        |       |                                                     |
|        |       | (Opted out by default -- set                        |
|        |       | RPT_OPT(\'FLO\',\'5\')=1 to activate; see Part III, |
|        |       | Section 3.10).                                      |
+--------+-------+-----------------------------------------------------+
| PA     | see:  | Flow of commodity (c) entering or leaving process   |
| R_FLO\ | F_IN/ | (p) with vintage period (v) in period (t).          |
| (      | F_OUT |                                                     |
| r,v,t, |       |                                                     |
| p,c,s) |       |                                                     |
+--------+-------+-----------------------------------------------------+
| PA     | none  | Discounted reduced costs of flow variable of        |
| R_FLO\ |       | commodity (c) in period (t) of process (p) with     |
| (      |       | vintage period (v); the reduced costs describe that |
| r,v,t, |       | the flow variable is at its lower (upper) bound,    |
| p,c,s) |       | and give the cost increase (decrease) of the        |
|        |       | objective function caused by an increase of the     |
|        |       | lower (upper) bound by one unit; the undiscounted   |
|        |       | reduced costs can be interpreted as the necessary   |
|        |       | decrease / increase of the cost coefficient of the  |
|        |       | flow variable, such that the flow will leave its    |
|        |       | lower (upper) bound.                                |
+--------+-------+-----------------------------------------------------+
| PA     | see:  | Inter-regional exchange flow of commodity (c) in    |
| R_IRE\ | F_IN/ | period (t) via exchange process (p) entering region |
| (r,v   | F_OUT | (r) as import (ie='IMP') or leaving region (r) as   |
| ,t,p,c |       | export (ie='EXP').                                  |
| ,s,ie) |       |                                                     |
+--------+-------+-----------------------------------------------------+
| PAR    | none  | Discounted reduced costs of inter-regional exchange |
| _IREM\ |       | flow variable of commodity (c) in period (t) of     |
| (r,v   |       | exchange process (p) with vintage period (v); the   |
| ,t,p,c |       | reduced costs describe that the flow variable is at |
| ,s,ie) |       | its lower (upper) bound, and give the cost increase |
|        |       | (or decrease) of the objective function caused by   |
|        |       | an increase of the lower (upper bound) by one unit; |
|        |       | the undiscounted reduced costs can be interpreted   |
|        |       | as the necessary decrease / increase of the cost    |
|        |       | coefficient of the flow variable in the objective   |
|        |       | function, such that the flow will leave its lower   |
|        |       | (upper) bound.                                      |
+--------+-------+-----------------------------------------------------+
| PAR_   | EQ    | Inter-regional trade equations -- Marginals:        |
| IPRIC\ | _IreM |                                                     |
| (r,t   |       | Undiscounted shadow price of the inter-regional     |
| ,p,c,s |       | trade equation of commodity (c) via exchange        |
| ,uc_n) |       | process (p) in period (t) and timeslice (s). The    |
|        |       | undiscounted shadow price can be interpreted as the |
|        |       | import/export price of the traded commodity. Note:  |
|        |       | ucn={IMP/EXP}.                                      |
+--------+-------+-----------------------------------------------------+
| PAR_   | VAR   | Technology Investment -- New capacity:              |
| NCAPL\ | _Ncap |                                                     |
| (      |       | Level value of investment variable (VAR_NCAP) of    |
| r,t,p) |       | process (p) in period (v).                          |
+--------+-------+-----------------------------------------------------+
| PAR_   | VAR_  | Technology Investment -- Marginals:                 |
| NCAPM\ | NcapM |                                                     |
| (      |       | Undiscounted reduced costs of investment variable   |
| r,t,p) |       | (VAR_NCAP) of process (p); only reported, when the  |
|        |       | capacity variable is at its lower or upper bound;   |
|        |       | the reduced costs describe in the case, that the    |
|        |       | investment variable is at its lower (upper) bound,  |
|        |       | the cost increase (decrease) of the objective       |
|        |       | function caused by an increase of the lower (upper) |
|        |       | bound by one unit; the undiscounted reduced costs   |
|        |       | can be interpreted as the necessary decrease /      |
|        |       | increase in the investment cost coefficient, such   |
|        |       | that the investment variable will leave its lower   |
|        |       | (upper) bound.                                      |
+--------+-------+-----------------------------------------------------+
| PAR_   | VAR_  | Technology Investment -- BenCost + ObjRange (see    |
| NCAPR\ | NcapR | Part III, Section 3.10 for more details):           |
| (r,t,p |       |                                                     |
| ,uc_n) |       | Cost-benefit and ranging indicators for process (p) |
|        |       | in period (t), where uc_n is the name of the        |
|        |       | indicator:                                          |
|        |       |                                                     |
|        |       | • COST - the total unit costs of VAR_NCAP (in terms |
|        |       | of an equivalent investment cost)                   |
|        |       |                                                     |
|        |       | • CGAP - competitiveness gap (in terms of           |
|        |       | investment costs), obtained directly from the       |
|        |       | VAR_NCAP marginals (and optional ranging            |
|        |       | information)                                        |
|        |       |                                                     |
|        |       | • GGAP - competitiveness gap (in terms of           |
|        |       | investment costs), obtained by checking also the    |
|        |       | VAR_ACT, VAR_FLO and VAR_CAP marginals, in case     |
|        |       | VAR_NCAP is basic at zero                           |
|        |       |                                                     |
|        |       | • RATIO - benefit / cost ratio, based on CGAP       |
|        |       |                                                     |
|        |       | • GRATIO - benefit / cost ratio, based on GGAP      |
|        |       |                                                     |
|        |       | • RNGLO - ranging information (LO) for VAR_NCAP (if |
|        |       | ranging is activated; in terms of investment costs) |
|        |       |                                                     |
|        |       | • RNGUP - ranging information (UP) for VAR_NCAP (if |
|        |       | ranging is activated; in terms of investment costs) |
+--------+-------+-----------------------------------------------------+
| PAR_   | VA    | Technology Capacity:                                |
| PASTI\ | R_Cap |                                                     |
| (r,    |       | Residual capacity of past investments (NCAP_PASTI)  |
| t,p,v) |       | of process (p) still existing in period (t), where  |
|        |       | vintage (v) is set to \'0\' to distinguish residual |
|        |       | capacity from new capacity.                         |
+--------+-------+-----------------------------------------------------+
| PAR_   | EQ_   | Peaking Constraint Slack -- Marginals:              |
| PEAKM\ | PeakM |                                                     |
| (r,    |       | Undiscounted annual shadow price of peaking         |
| t,c,s) |       | equation (EQ_PEAK) associated with commodity (c);   |
|        |       | since the peaking equation is at most only binding  |
|        |       | for one timeslice (s), a shadow price only exists   |
|        |       | for one timeslice. The shadow price can be          |
|        |       | interpreted as an additional premium to the shadow  |
|        |       | price of the commodity balance that consumers of    |
|        |       | commodity (c) have to pay for consumption during    |
|        |       | peak times. The premium is used (besides other      |
|        |       | sources) to cover the capacity related costs (e.g., |
|        |       | investment costs) of capacity contributing reserve  |
|        |       | capacity during peak times.                         |
+--------+-------+-----------------------------------------------------+
| PA     | PA    | Process topology:                                   |
| R_TOP\ | R_Top |                                                     |
| (r     |       | Process topology indicators for reporting use.      |
| ,t,p,c |       | Values are all zero, period (t) is the first        |
| ,uc_n) |       | milestone year, and uc_n = IN/OUT. (Opted out by    |
|        |       | default -- SET RPT_TOP YES to activate.)            |
+--------+-------+-----------------------------------------------------+
| PAR_   | U     | Marginal cost of market-share constraint:           |
| UCMRK\ | ser_c |                                                     |
| (r     | onFXM | Undiscounted shadow price of group-wise market      |
| ,t,uc_ |       | share constraint (defined with PRC_MARK) for        |
| n,c,s) |       | commodity c, identified with name uc_n, in period t |
|        |       | and timeslice s.                                    |
+--------+-------+-----------------------------------------------------+
| PAR_   | User_ | Marginal cost of dynamic process bound constraint:  |
| UCRTP\ | DynbM |                                                     |
| (u     |       | Undiscounted shadow price of dynamic process-wise   |
| c_n,r, |       | bound constraint, identified with name uc_n, for    |
| t,p,c) |       | variable c (CAP / NCAP / ACT), in period t and      |
|        |       | timeslice s.                                        |
+--------+-------+-----------------------------------------------------+
| PAR    | Use   | Level of user constraint (or its slack) (only       |
| _UCSL\ | r_con | reported when the VAR_UC variables are used):       |
| (uc_n, |       |                                                     |
| r,t,s) |       | The level of user constraint (uc_n) by region (r),  |
|        |       | period (t) and timeslice (s). The levels should be  |
|        |       | zero whenever the RHS constant is zero and the      |
|        |       | equation is binding. If the constraint is not       |
|        |       | binding, the level together with the RHS constant   |
|        |       | gives the gap for the equation to become binding.   |
+--------+-------+-----------------------------------------------------+
| PAR    | U     | Marginal cost of user constraint (all bound types): |
| _UCSM\ | ser_c |                                                     |
| (uc_n, | onFXM | Marginal of user constraint (uc_n) by region (r),   |
| r,t,s) |       | period (t) and timeslice (s). The marginals are     |
|        |       | undiscounted, if the constraint is defined by       |
|        |       | region and period. The marginals of cumulative and  |
|        |       | multi-region user constraints are not undiscounted  |
|        |       | (reported with **r** or **t** as \'NONE\') due to   |
|        |       | ambiguity. However, ambiguously undiscounted        |
|        |       | marginals of multi-region constraints are also      |
|        |       | reported by each region involved.                   |
+--------+-------+-----------------------------------------------------+
| REG_   | Reg_  | Regional total annualized costs by period:          |
| ACOST\ | ACost |                                                     |
| (r,t   |       | Total annualized costs in region (r) by period (t)  |
| ,uc_n) |       | and cost category. The cost categories are INV,     |
|        |       | INVX, FIX, FIXX, VAR, VARX, IRE, ELS and DAM (see   |
|        |       | Table 16 below for more information).               |
+--------+-------+-----------------------------------------------------+
| REG    | Reg   | Regional total discounted implied trade cost:       |
| _IREC\ | _irec |                                                     |
| (r)    |       | Total discounted implied trade costs in region (r), |
|        |       | derived by multiplying the shadow prices of the     |
|        |       | trade equations by the trade volumes. The sum of    |
|        |       | REG_IREC over regions is zero.                      |
+--------+-------+-----------------------------------------------------+
| RE     | Re    | Regional total discounted system cost:              |
| G_OBJ\ | g_obj |                                                     |
| (r)    |       | Discounted objective value (EQ_OBJ) for each region |
|        |       | (r).                                                |
+--------+-------+-----------------------------------------------------+
| REG    | Reg   | Regional total discounted system cost by component: |
| _WOBJ\ | _wobj |                                                     |
| (r,u   |       | Discounted objective value (EQ_OBJ) for each region |
| c_n,c) |       | (r), by cost type (uc_n) and currency (c). The cost |
|        |       | types are: INV, INVX, FIX, FIXX, VAR, VARX, ELS,    |
|        |       | DAM (see Table 16 below for more information).      |
+--------+-------+-----------------------------------------------------+
| VA     | Va    | Annual commodity flow values:                       |
| L_FLO\ | l_Flo |                                                     |
| (r,v,  |       | Flows of process (p) multiplied by the commodity    |
| t,p,c) |       | balance marginals of those commodities (c) in       |
|        |       | period (t); the values can be interpreted as the    |
|        |       | market values of the process inputs and outputs.    |
+--------+-------+-----------------------------------------------------+

: Table 15: Report parameters in TIMES

### Acronyms used in cost reporting parameters

The acronyms used in the reporting parameters for referring to certain types of costs are summarized in Table 16. The acronyms are used as qualifiers in the $uc\_n$ index of each reporting attribute, and are accessible in VEDA-BE through that same dimension.

+--------------+-------------------------------------------------------+
| **Cost       | **Component acronyms**                                |
| parameter**  |                                                       |
+--------------+-------------------------------------------------------+
| CAP_NEW\     | Newly installed capacity and lump-sum investment      |
| (r           | costs by vintage and commissioning period:            |
| ,v,p,t,uc_n) |                                                       |
|              | INSTCAP New capacity of vintage v commissioned in     |
|              | period t                                              |
|              |                                                       |
|              | LUMPINV Lump-sum investment costs for vintage v in    |
|              | period t                                              |
|              |                                                       |
|              | LUMPIX Lump-sum investment taxes & subsidies for      |
|              | vintage v, period t                                   |
|              |                                                       |
|              | INV+ Lump-sum investment portion attributable to      |
|              | hurdle rate in excess of the general discount rate    |
|              |                                                       |
|              | INVX+ Lump-sum tax & subsidy portion attributable to  |
|              | hurdle rate in excess of the general discount rate    |
+--------------+-------------------------------------------------------+
| CST_PVC\     | Total discounted costs by commodity (optional):       |
| (uc_n,r,c)   |                                                       |
|              | COM Commodity-related costs, taxes and subsidies      |
|              |                                                       |
|              | ELS Losses in elastic demands                         |
|              |                                                       |
|              | DAM Damage costs                                      |
+--------------+-------------------------------------------------------+
| CST_PVP\     | Total discounted costs by process (optional):         |
| (uc_n,r,p)   |                                                       |
|              | INV Investment costs, taxes and subsidies, excluding  |
|              | portions attributable to hurdle rates in excess of    |
|              | the general discount rate                             |
|              |                                                       |
|              | INV+ Investment costs, taxes and subsidies, portions  |
|              | attributable to hurdle rates in excess of the general |
|              | discount rate                                         |
|              |                                                       |
|              | FIX Fixed costs, taxes and subsidies                  |
|              |                                                       |
|              | ACT Activity costs                                    |
|              |                                                       |
|              | FLO Flows costs taxes and subsidies (including        |
|              | exogenous IRE prices)                                 |
|              |                                                       |
|              | IRE Implied trade costs minus revenues                |
+--------------+-------------------------------------------------------+
| REG_ACOST\   | Regional total annualized costs by period:            |
| (r,t,uc_n)   |                                                       |
|              | INV Annualized investment costs                       |
|              |                                                       |
|              | INVX Annualized investment taxes and subsidies        |
|              |                                                       |
|              | FIX Annual fixed costs                                |
|              |                                                       |
|              | FIXX Annual fixed taxes and subsidies                 |
|              |                                                       |
|              | VAR Annual variable costs                             |
|              |                                                       |
|              | VARX Annual variable taxes and subsidies              |
|              |                                                       |
|              | IRE Annual implied trade costs minus revenues         |
|              |                                                       |
|              | ELS Annual losses in elastic demands                  |
|              |                                                       |
|              | DAM Annual damage costs                               |
+--------------+-------------------------------------------------------+
| REG_WOBJ\    | Regional total discounted system cost by component:   |
| (r,uc_n,c)   |                                                       |
|              | INV Investment costs                                  |
|              |                                                       |
|              | INVX Investment taxes and subsidies                   |
|              |                                                       |
|              | FIX Fixed costs                                       |
|              |                                                       |
|              | FIXX Fixed taxes and subsidies                        |
|              |                                                       |
|              | VAR Variable costs                                    |
|              |                                                       |
|              | VARX Variable taxes and subsidies                     |
|              |                                                       |
|              | ELS Losses in elastic demands                         |
|              |                                                       |
|              | DAM Damage costs                                      |
+--------------+-------------------------------------------------------+

: Table 16: Acronyms used in the cost reporting parameters.

### The levelized cost reporting option

As indicated in Table 15 above, the reporting of levelized costs for each process can be requested by setting the option RPT_OPT(\'NCAP\', \'1\'). The results are stored in the VEDA-BE $Var\_NcapR$ result attribute, with the qualifier \'LEVCOST\' (with a possible system label prefix).

The levelized cost calculation option looks to weight all the costs influencing the choice of a technology by TIMES. It takes into consideration investment, operating, fuel, and other costs as a means of comparing the full cost associated with each technology.

Levelized cost can be calculated according to the following general formula:

------------------------------------------------------------------
  $$LEC = \frac{\sum_{t = 1}^{n}{\frac{IC_{t}}{(1 + r)^{t - 1}} + \frac{OC_{t} + VC_{t} + \sum_{i}^{}{FC_{i,t} + FD_{i,t}} + \sum_{j}^{}{ED_{j,t}}}{(1 + r)^{t - 0.5}} -}\frac{\sum_{k}^{}{BD_{k,t}}}{(1 + r)^{t - 0.5}}}{\sum_{t = 1}^{n}\frac{\sum_{m}^{}{MO_{m,t}}}{(1 + r)^{t - 0.5}}}$$   \(1\)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 17: Core TIMES parameters related to the modelling of CHP processes.

where
-   $r$ = discount rate (e.g. 5%)
-   $IC_t$ = investment expenditure in (the beginning of) year $t$
-   $OC_t$ = fixed operating expenditure in year $t$
-   $VC_t$ = variable operating expenditure in year $t$
-   $FC_{it}$ = fuel-specific operating expenditure for fuel $i$ in year $t$
-   $FD_{it}$ = fuel-specific acquisition expenditure for fuel $i$ in year $t$
-   $ED_{jt}$ = emission-specific allowance expenditure for emission $j$ in year $t$ (optional)
-   $BD_{kt}$ = revenues from by-product $k$ in year $t$ (optional; see below)
-   $MO_{mt}$ = output of main product $m$ in year $t$

The exponent $(t-0.5)$ in the formula indicates the good practice of using mid-year discounting for continuous streams of annual expenditures.

In TIMES, the specific investment, fixed and variable O&M costs and fuel-specific flow costs are calculated directly from the input data. However, for the fuel acquisition prices, emission prices and by-product prices, ***commodity marginals*** from the model solution are used. All the unit costs are multiplied by the corresponding ***variable levels*** as given by the model solution: investment cost and fixed operating costs are multiplied by the amounts of capacity installed / existing, variable operation costs by the activity levels, and fuel-specific costs by the process flow levels. Mid-year discounting can also be activated.

The outputs of the main products are taken from the flow levels of the commodities in the primary group (PG) of the process. An exception is CHP processes, for which the elec­tricity output is considered the sole main output, and heat is considered as a by-product.

**Options for variants of levelized cost reporting:**

1.  <ins>Do not include emission prices or by-product revenues in the calculation</ins> (RPT_OPT('NCAP','1') = --1):

> In this option emission prices are omitted from the calculation, in accordance with the most commonly used convention for LEC calculation. Consequently, any by-product revenues need to be omitted as well, because if emissions have prices, the by-product prices in the solution would of course be polluted by those prices, and thus it would be inconsistent to use them in the calcu­lation. Instead, in this case any amount of by-product energy produced by ELE, CHP and HPL processes is indirectly credited by reducing the fuel-specific costs in the calculation to the fraction of the main output in the total amount of energy produced.

2.  <ins>Include both emission prices and by-product revenues in the calculation</ins> (RPT_OPT('NCAP','1') = 1):

> In this option both emission prices and by-product revenues are included in the calculation. The levelized cost thus represents the unit cost after subtracting the levelized value of all by-products from the gross value of the levelized cost. This approach of crediting for by-products in the LEC calculation has been utilized, for example, in the IEA *Projected Costs of Generating Electricity* studies.

3.  <ins>Include not only emission prices and by-product revenues, but also the revenues from the main product in the calculation</ins> (RPT_OPT('NCAP','1') = 2):

> This option is similar to option (2) above, but in this case all product revenues are included in the calculation, including also the peak capacity credit from the TIMES peaking equation (when defined). The calculated LEC value thus represents the levelized **net** unit cost after subtracting the value of all products from the gross levelized cost. For competitive new capacity vintages, the resulting levelized cost should in this case generally be *negative*, because investments into technologies that enter the solution are normally profitable. For the marginal technologies the levelized cost can be expected to be very close to zero. Only those technologies that have been in some way forced into the solution, e.g. by specifying lower bounds on the capacity or by some other types of constraints, should normally have a positive levelized cost when using this option.

In the TIMES calculation, the expenditures for technology investments and process commodity flows include also taxes minus subsidies, if such have been specified. The levelized costs are calculated by process vintage, but only for new capacity vintages, as for them both the full cost data influencing technology choice and the operating history starting from the commissioning date are available, which is rarely the case for existing vintages.
