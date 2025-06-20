(a-switches-and-parameters)=
# Switches and Parameters

## Activating the Climate Module

The Climate Module (CLI) extension of TIMES can be activated and employed by using the Parameters and Switches described in this chapter.

Besides the basic input data parameters described in {numref}`cli-user-input-parameters`, the user also has full control over the CLI component being activated by means of the `$SET CLI YES` switch. This switch is provided by the data handling system when the user indicates that the CLI option is to be included:

```
$SET CLI YES
```

(a-calibration)=
## Calibration

The calibration of the Climate Module to historical values is an important aspect of using the module. The mass balance and temperature equations can be calibrated for the first period by using three alternative calibration years B(1)--1, m(1)--1, and m(1). Whenever D(1)=1, the first two alternatives are equal. The default calibrating year is m(1)--1. The alternative calibration years can be activated by using one of the following two settings in the run-file:
- `$SET CM_CALIB B` ! Calibrate at the end of B(1)--1
- `$SET CM_CALIB M` ! Calibrate at the end of m(1)

## Controlling the years considered beyond EOH

The Climate Equations will be calculated beyond EOH at each of the years for which either a user-defined emission target or a temperature or concentration bound is specified. The years considered thus span between the EOH and the last year for which a CM_MAXC is specified.

In addition, by default any Climate Equations beyond EOH will be calculated only at each year having a year value divisible by 20. This default year resolution can be changed by using the Climate Module constant **\'BEOHMOD\'**. However, note that the years available in the model extend by default to 2200 only, and therefore one may need to adjust the year-span e.g. to 2300 by using the following switch:

```
$SET EOTIME 2300
```

The **reporting years** for the climate variables are the same as the calculation years.

## Input parameters

Like all other aspects of TIMES, the user defines the Climate Module components of the energy system by means of input parameters, which are described in this section. {numref}`cli-user-input-parameters` describes the User Input Parameters that are associated with the Climate Module option.

```{list-table} Definition of Climate Module user input parameters.
:name: cli-user-input-parameters
:header-rows: 1

* - Input Parameter (Indexes)
  - Units & Defaults
  - Description
* - CM_CONST (item)
  - Units: See on the right
  <br>Defaults: See below
  - Various Climate Module constants, where item can be:
  <br>PHI-UP-AT: carbon transfer coefficient UP→ATM
  <br>PHI-AT-UP: carbon transfer coefficient ATM→UP
  <br>PHI-LO-UP: carbon transfer coefficient LO→UP
  <br>PHI-UP-LO: carbon transfer coefficient UP→LO
  <br>GAMMA: radiative forcing sensitivity, in W/m<sup>2</sup>
  <br>CS: temperature sensitivity, in °C
  <br>LAMBDA: $\lambda = \gamma / C_s$
  <br>SIGMA1: speed of adjustment, in W-yr/m<sup>2</sup>/°C
  <br>SIGMA2: thermal capacity ratio, in W/m<sup>2</sup>/°C
  <br>SIGMA3: transfer rate upper to deep ocean, in yr<sup>-1</sup>
  <br>CO2-PREIND: pre-industrial atmosph. CO<sub>2</sub>, in GtC
  <br>PHI-CH4: annual decay of atmospheric CH<sub>4</sub>, fraction
  <br>PHI-N2O: annual decay of atmospheric N<sub>2</sub>O, fraction
  <br>EXT-EOH: activates horizon extension, ≥0, year
  <br>BEOHMOD: defines year interval for reporting, years
* - CM_HISTORY (y,cm_var)
  - Units: See on the right
  <br>Defaults: See below
  - Historical calibration values at years *y*, for *cm_var*:
  <br>CO2-ATM: atmospheric mass of CO<sub>2</sub>, in GtC
  <br>CO2-UP: mass of CO<sub>2</sub> in biosphere, in GtC
  <br>CO2-LO: mass of CO<sub>2</sub> in lower ocean, in GtC
  <br>DELTA-ATM: atmospheric temperature change, in °C
  <br>DELTA-LO: oceanic temperature change, in °C
  <br>CH4-ATM: anthropogenic CH<sub>4</sub> concentration, in Mt
  <br>CH4-UP: natural CH<sub>4</sub> concentration, in Mt
  <br>N2O-ATM: anthropogenic N<sub>2</sub>O concentration, in Mt
  <br>N2O-UP: natural N<sub>2</sub>O concentration, in Mt
* - CM_GHGMAP (r,c,cg)
  - Global units:
  <br>CO<sub>2</sub>: GtC
  <br>CH<sub>4</sub>: Mt
  <br>N<sub>2</sub>O: Mt
  - Conversion factors from regional GHG commodities (c) to global emissions (*cg*) in the Climate Module, where cg=
  <br>CO2-GtC: global CO<sub>2</sub> emissions in GtC
  <br>CH4-Mt: global CH<sub>4</sub> emissions in Mt
  <br>N2O-Mt: global N<sub>2</sub>O emissions in Mt
* - CM_EXOFORC (y)
  - Unit: W/m<sup>2</sup>
  - Radiative forcing from exogenous sources (from greenhouse gases not modelled) in year *y*.
* - CM_LINFOR (y,cm_var,lim)
  - Unit: For
  <br>CO<sub>2</sub>: ppm
  <br>CH<sub>4</sub>/N<sub>2</sub>O: W/m<sup>2</sup>/ppb
  <br>Default: none
  - Parameters for the linear forcing functions for cm_var:
  <br>CO2-PPM: lower (LO) and upper (UP) end of the concentration range over which the forcing function for CO<sub>2</sub> is linearized (in ppm)
  <br>CH4-PPB: multiplier (N) for the CH<sub>4</sub> concentration and constant term (FX) of the linear forcing function
  <br>N2O-PPB: multiplier (N) for the N<sub>2</sub>O concentration and constant term (FX) of the linear forcing function
* - CM_MAXC (y,cm_var)
  - Default: none
  - Maximum level of climate indicator *cm_var* in year *y*.
  <br>CO2-GtC: CO<sub>2</sub> emissions in GtC
  <br>CH4-Mt: CH<sub>4</sub> emissions in Mt
  <br>N2O-Mt: N<sub>2</sub>O emissions in Mt
  <br>CO2-ATM: atm. CO<sub>2</sub> concentration / pre-industrial ratio
  <br>CO2-PPM: atm. CO<sub>2</sub> concentration in ppm
  <br>CH4-PPB: atm. CH<sub>4</sub> concentration in ppb
  <br>N2O-PPB: atm. N<sub>2</sub>O concentration in ppb
  <br>DELTA-ATM: atmospheric temperature change, in °C
  <br>FORCING: total radiative forcing, in W/m<sup>2</sup>
* - CM_MAXCO2C (y)
  - Unit: GtC
  - Maximum level of CO<sub>2</sub> concentration in GtC. 
```


### Mapping of regional emissions to global emissions

Conversion from regional emissions to global emissions must be done by using the CM_GHGMAP(r,c,cg) parameter, in adequate units. The labels for the global emissions **cg** are \'CO2-GtC\', \'CH4-Mt\' and \'N2O-Mt\'. The parameter IRE_CCVT(r,c,r,cg) can alternatively be also used, if CM_GHGMAP is not available.

Assuming here that the total regional emissions are represented by the commodities TOTCO2, TOTCH4 and TOTN2O, and are measured in kt, as is the case in TIAM models for instance, the mapping and conversion would be the following:

```
CM_GHGMAP(R,'TOTCH4','CH4-MT') = 1E-3;
CM_GHGMAP(R,'TOTN2O','N2O-MT') = 1E-3;
CM_GHGMAP(R,'TOTCO2','CO2-GtC') = 2.727272E-7;
```

### Deterministic input parameters for CO<sub>2</sub>

- CM_CONST({PHI_AT_UP, PHI_UP_AT, PHI_UP_LO, PHI_LO_UP}) (also denoted $\varphi_{atm-up}$, $\varphi_{up-atm}$, etc, in the equations of section 2): annual CO<sub>2</sub> flow coefficients between the three reservoirs (AT=Atmosphere, UP=Upper ocean layer, LO=Deep ocean layer). These are time-independent coefficients. Units: none
- CM_HISTORY(y,{CO2-ATM, CO2-UP, CO2-LO}): Values at the end of the calibration year *y* of the masses of CO<sub>2</sub> in the atmosphere, the upper ocean layer, and the deep ocean layer, respectively. Note that these values are time- indexed so that the model generator can pick up the correct value according to the calibration year chosen by the user. Units: GtC, Mt(CH<sub>4</sub>), Mt(N<sub>2</sub>O).
- CM_CONST(CO2-PREIND): Pre-industrial atmospheric mass of CO<sub>2</sub>. Units = GtC

## Parameters for the linear CO<sub>2</sub> forcing approximation

CM_LINFOR(datayear,item,lim): lower and upper limit for the concentration of CO<sub>2</sub> in atmosphere, used in the approximation of the radiative forcing equation for CO<sub>2</sub> (see section [2.2](a-radiative-forcing) above). *item* may be equal to CO2-ATM (in which case the limit is expressed as a ratio of concentration over pre-industrial concentration), or to CO2-PPM (in which case the limit is expressed in ppm of CO2-equivalent). The index *lim* is either equal to LO or to UP, depending on whether the lower or the upper limit of the range is being specified. For example, the following specifications may be used to select a range from 375 to 550 ppm for the approximation at year 2020:

```
CM_LINFOR('2020','CO2-PPM','LO') = 375;
CM_LINFOR('2020','CO2-PPM','UP') = 550;
```

Note that the values of LINFOR are systematically interpolated. The range can also be specified in a time-dependent manner taking into account the gradual increase in the expected range of possible concentration levels over time. That would further improve the accuracy of the linearization. For example, for 2005 the range could be specified to consist of only a single value, because the actual concentration in 2005 is well-known.

### Parameters for modeling the concentrations and forcings of other greenhouse gases

**Historical base year values of natural (UP) and anthropogenic (ATM) concentrations** (in Mt), needed at for the base year of the model (default 2005):

```
CM_HISTORY('2005','CH4-UP') = 1988;
CM_HISTORY('2005','CH4-ATM') = 3067;
CM_HISTORY('2005','N2O-UP') = 2109;
CM_HISTORY('2005','N2O-ATM') = 390;
```

In the results the total concentrations (UP+ATM) are reported for both CH<sub>4</sub> and N<sub>2</sub>O.

**Annual exponential decay of concentrations (PHI-xxx = 1/Life):**

```
CM_CONST('PHI-CH4') = 0.09158;
CM_CONST('PHI-N2O') = 0.008803;
```

Here $\Phi_{CH4}$, $\Phi_{N2O}$, are the one-year decay rates for methane and N<sub>2</sub>O respectively

**Parameters for the linear CH<sub>4</sub> and N<sub>2</sub>O forcing approximations:**

Note that for specifying the linear forcing functions for CH<sub>4</sub> and N<sub>2</sub>O, the LO/UP bounds cannot be used, but the slope (\'N\') and constant (\'FX\') of the forcing functions must be directly defined by the user. Example:

```
CM_LINFOR('2010','CH4-PPB','N') = 0.000340;
CM_LINFOR('2010','CH4-PPB','FX') = -0.110;
CM_LINFOR('2010','N2O-PPB','N') = 0.00292;
CM_LINFOR('2010','N2O-PPB','FX') = -0.769;
```

**Parameter for the exogenous radiative forcing from non-modeled gases** in each year from initial year: CM_EXOFOR(y)

Units: Watts/m<sup>2</sup>.

### Parameters for the temperature equations

- CM_CONST(SIGMA1) (also denoted $\sigma_1$): speed of adjustment parameter for atmospheric temperature. $1/\sigma_1$ represents the thermal capacity of the atmospheric + upper ocean layer (W-yr/m<sup>2</sup>/°C). Note however that when SIGMA1 is assumed stochastic, its multiple values are specified via the generic S_CM_CONST parameter described below. 
- CM_CONST(SIGMA2) (also denoted $\sigma_2$): ratio of the thermal capacity of the deep oceans to the transfer rate from shallow to deep ocean (W/m<sup>2</sup>/°C). 
- CM_CONST(SIGMA3) (also denoted $\sigma_3$): $1/\sigma_3$ is the transfer rate (per year) from the upper level of the ocean to the deep ocean (yr<sup>-1</sup>). 
- CM_CONST(GAMMA) (also denoted γ): radiative forcing sensitivity to a doubling of the atmospheric CO<sub>2</sub> concentration. Units: Watts/m<sup>2</sup>. 
- CM_CONST(CS): $C_s$, the temperature sensitivity to a doubling of the CO<sub>2</sub> concentration (°C). 
- CM_CONST(LAMBDA) (also denoted $\lambda$): a feedback parameter, representing the equilibrium impact of CO<sub>2</sub> concentrations doubling on climate. $\lambda = \gamma / C_s$. Note however that when $C_s$ is assumed stochastic, its multiple values are specified via the generic S_CM_CONST parameter described below. If all three of $\lambda$, $\gamma$ and $C_s$ are specified, the user-specified $\lambda$ is overridden by the derived value $\gamma / C_s$. 
- CM_HISTORY(y,{DELTA_ATM, DELTA_LOW}): values at the end of the calibration year *y* of the temperature changes (wrt to pre-industrial time) in atmosphere and deep layer, respectively. Units: °C

(a-upport-bounds-on-climate-variablaes)=
### Upper bounds on climate variables

The following parameters are needed if constraints on some climate variables are desired. In TIMES, several climate upper bounds may be specified at any year. These upper bounds are specified via the single generic parameter CM_MAXC(datayear,item), where *datayear* is the year at which the bound applies, and *item* may be any of the following nine choices:

- CO2-ATM: for bounding the ***ratio*** of GHG concentration to the preindustrial concentration (where the pre-industrial concentration is defined by CO2-PREIND); 
- CO2-PPM: for bounding the CO<sub>2</sub> concentration expressed in ppm;
- CH4_PPB: for bounding the CH<sub>4</sub> concentration expressed in ppbv;
- N2O-PPB: for bounding the N<sub>2</sub>O concentration expressed in ppbv;
- FORCING: for bounding the total atmospheric radiative forcing expressed in W/m<sup>2</sup>. (If this bound or the next one on temperature is used, the linearized forcing equation is used rather than the exact forcing equation); 
- DELTA-ATM: for bounding the change in global atmospheric temperature over pre-industrial temperature, expressed in °C; 
- CO2-GTC: for bounding the global CO<sub>2</sub> emissions expressed in GtC;
- CH4-MT: for bounding the global CH<sub>4</sub> emissions expressed in Mt;
- N2O-MT: for bounding the global N<sub>2</sub>O emissions expressed in Mt.

In addition, the user can also bound the CO<sub>2</sub> concentration expressed in GtC, by using CM_MAXCO2C.

### Incorporating climate variables in UC constraints

When using the Climate Module extension, one can also refer to the climate variables in user constraints. The UC attribute for that purpose is the following:

> UC_CLI(uc_n, side, reg, y, item)

This parameter can be used to define climate variable coefficients in any period-wise user constraints. The UC_GRPTYPE (to be used in UC_ATTR) for this parameter is \'CLI\'. The ***item*** index can be any of the following climate variables:

- CO2-GTC - total global CO<sub>2</sub> emissions (or CO<sub>2</sub>-eq. GHGs)
- CO2-ATM - CO<sub>2</sub> concentration in the atmosphere
- CO2-UP - CO<sub>2</sub> concentration in the biosphere/upper ocean
- CO2-LO - CO<sub>2</sub> concentration in the deep ocean layer
- FORCING - radiative forcing
- DELTA-ATM - atmospheric temperature
- DELTA-LO - deep oceanic temperature

The attribute can be used for defining custom relation­ships by each region, between any of the climate variables and e.g. process flows, activities or capacities, or total commodity flows. However, if used in a global constraint, one should normally define the UC_CLI attribute only for one region (e.g. GLB).

### Random climate parameters (refer to documentation on stochastic TIMES)

If the stochastic programming version of TIMES is used, several climate parameters may be assumed random. These fall into two categories: the upper bounds on climate quantities discussed in the previous section, and the two climate coefficients, **Cs** and **SIGMA1.**

Regarding the random upper bounds, their multiple values are specified via the stochastic version of the **CM_MAX** parameter, namely **S_CM_MAX(datayear,item,stage,sow)**, where in addition to **datayear** and **item** already explained, **stage** refers to the stage of the event tree and **sow** refers to the state-of-the-world. Note that this single generic parameter will be specified as many times as there are **stages** and **sow**'s in the stochastic event tree. If this parameter is specified, the corresponding values of the deterministic parameter **CM_MAX** are superseded.

Regarding the two random coefficients, their multiple values are then declared via the single generic parameter **S_CM_CONST(item,stage,sow)**, where **item** may be equal to **CS** or to **SIGMA1**, **stage** is the stage number, and **sow** is the state-of-the-world. Note that this single generic parameter will be specified as many times as there are stages and sow's in the stochastic event tree. If this parameter is specified, the corresponding values of the deterministic parameter (**LAMBDA** and/or **SIGMA1**) are superseded.

The reader is referred to Chapter 8 of Part I and the documentation of the stochastic programming version of TIMES for the precise meaning of the **stage** and **sow** concepts.

:::{admonition} Remark

In addition to the possible values of the random parameters, the user must specify the probabilities attached to each ***sow***. This is also explained in the documentation on stochastic TIMES.
:::

### Parameters for extending the Climate Module equations beyond EOH

The main purpose of extending the climate equations beyond EOH is to be able to set climate targets beyond EOH. This is particularly useful for DeltaT targets, because there is a con­siderable time lag between the decline of emissions and the peak of DeltaT.

The extended climate equations must be explicitly activated by the user. The activation can be done by specifying any non-negative value for the new Climate Module constant **CM_CONST**(**\'EXT-EOH\')**. Different values of the constant will have the following meaning:

```{list-table}
:header-rows: 1

* - Value
  - Meaning
* - -1 (default)
  - The feature is deactivated.
* - 0
  - In this case **\'EXT-EOH\'** will be automatically adjusted to E(*M*), where *M *is the last model year ***m*** for which the end-year **E(*m*)** is specified. The adjusted parameter will then have the same meaning as in the case EXT-EOH \> 0 below.
* - \>0
  - The emissions at EOH will remain constant at the endogenous value in EOH=E(T) (where T=last **milestone year**) until the year MAX(**EXT-EOH**, EOH), and then develop linearly from that value to the first user-defined emission value in a subsequent year.
```

The setting **EXT-EOH**=**0** may be useful for ensuring that any user-defined target values for the emissions will only be taken into account beyond the last ***model year***, even in model runs where a truncated model horizon is used. In such case, when **EXT-EOH**=**0** is used, the emissions are assumed to remain constant between the truncated EOH and the end of the full model horizon.

A positive value **EXT-EOH**=**y** **≤ EOH** means that a linear development of emissions towards the first user-defined value is requested to start im­mediately at the EOH, regardless of the model horizon being truncated or not. Finally, a positive value **EXT-EOH**=**y** **\> EOH** can be useful if the user wishes the emissions to remain constant at the EOH value until a predefined year y \> EOH, before turning into the linear development towards the first user-defined value.

:::{admonition} Warning

If **0 \< EXT-EOH \< E(M) = MAX<sub>m</sub>(E(m))**, any user-defined global emission bounds for CO2-GTC, CH4-MT or N2O-MT, which may be inadvertently specified at years between **MAX(EXT-EOH, EOH)** and **E(M)**, will also be taken into account as target values for the emission trajectories.
:::

The global greenhouse gas emissions that can be considered by the extended climate equations are the three main input emissions to the Climate Module:

- CO2-GTC Global CO<sub>2</sub> emissions, expressed in GtC
- CH4-MT Global CH<sub>4</sub> emissions, expressed in Mt
- N2O-MT Global N<sub>2</sub>O emissions, expressed in Mt

The user can specify target emission values for these emissions at any year(s) beyond EOH. For simplicity, the target emission values are specified by using the **CM_MAXC** parameter, which is normally used for specifying upper bounds for the global emissions, as well as for the temperature and concentrations.

Starting from the year ***B***= MAX(EOH,EXT-EOH), the emissions will be assumed to develop linearly from the value at EOH to the first user-specified value beyond ***B***. If no target values are specified, the emissions will be assumed to remain constant at the EOH value. If several successive values are speci­fied, the emissions will develop linearly also between the successive target values.

Bounds on the global atmospheric temperature, forcing or GHG concentrations can be specified at any years beyond the EOH, in the normal way. In addition, exogenous forcing can be specified and is interpolated beyond EOH.

The Climate Equations will be calculated beyond EOH at each of the years for which either a user-defined emission target or a temperature or concentration bound is specified. The years considered thus span between the EOH and the last year for which a CM_MAXC is specified. However, as described above, any emission bounds between EOH and MAX(EOH,EXT-EOH) will be ignored.

In addition, by default the Climate Equations will be calculated also at each year having a year value divisible by 20. This default year resolution can be changed by using the new Climate Module constant **\'BEOHMOD\'**. Accordingly, if the user wishes the Climate Equations to be calculated at 10 years' intervals (in addition to the CM_MAXC years) she can specify the following parameter:

```
PARAMETER CM_CONST / BEOHMOD 10 /;
```

The **reporting years** for the climate variables are the same as the calculation years.

## Internal parameters

- *CM_PPM<sub>cm_var</sub>*: The densities of the greenhouse gases are hard coded in TIMES (via the internal parameter), with the following values:
	- density of CH<sub>4</sub>: 2.84 Mt / ppbv
	- density of N<sub>2</sub>O: 7.81 Mt / ppbv
	- density of CO<sub>2</sub>: 2.13 Gt / ppm.
- *CM_PHI<sub>cm_var,t,i,j</sub>*: The transition matrix for climate indicator cm_var between reservoirs i and j and successive years t--1 and t;
- *CM_AA<sub>cm_var,t,i,j</sub>*: The transition matrix for climate indicator cm_var between reservoirs i and j and between the milestone years of periods t--1 and t;
- *CM_BB<sub>cm_var,t,i,j</sub>*: The transition matrix for climate indicator cm_var from emissions in period t to reservoir contents in the same period;
- *CM_CC<sub>cm_var,t,i,j</sub>*: The transition matrix for climate indicator cm_var from emissions in period t--1 to reservoir contents in the period t.

## Reporting parameters

There are two reporting parameters, CM_RESULT and CM_MAXC_M, which contain the results on the levels of the climate variables (or reporting quantities) and the dual values of the constraints defined by using CM_MAXC.

CM_RESULT is indexed by year *y* and result type {e.g. CO2-ATM, CO2-PPM, FORCING, DELTA-ATM, DELTA_LO}. The values represent the quantities at the end of year y. The reporting years y include the milestone years plus any years beyond m(T) that either have some CM_MAXC bound defined or are modulo(BEOHMOD).

- CO2-GtC(y): the total global CO<sub>2</sub> emissions at the end of year **y**.
- CO2-ATM(y): the value of the atmospheric mass of CO<sub>2</sub>-equivalent at the end of year **y**, obtained directly from the variable **VAR_CLIBOX(\'CO2-ATM\',y)**.
- CO2-PPM(y): the value of the atmospheric concentration of CO<sub>2</sub>-equivalent at the end of year **y**.
- FORCING(y): forcing value at end of year y, calculated using the linearized forcing functions as defined by the user.
- FORC+TOT(y): exact forcing value at end of year y, calculated using the logarithmic forcing equation defined in section [2.2](a-radiative-forcing) and the CO2-ATM(y) value.
- DELTA_ATM(y): exact atmospheric temperature value at end of year y, calculated using the forcing FORC+TOT(y).
- DELTA_LOW(y): exact lower ocean temperature value at end of year y, calculated using the forcing FORC+TOT(y).

CM_MAXC_M is indexed by year *y* and constraint type. The values are reported for each of the EQ_CLITOT and EQ_CLIMAX equations. The values represent directly the dual values of these constraints at year y.

## Default values of the climate parameters

{numref}`cli-parameters` shows the default values of all parameters of the Climate Module except exogenous forcing. All defaults may be modified by the user.
- CS and SIGMA1 may be assumed random, in which case the default values are not used. The user must specify their values explicitly using the appropriate parameter names described earlier.
- The parameters highlighted blue are upper bounds on five climate variables (in this example, they are set high enough to be inoperative).
- The three parameters highlighted pink concern the extension of emissions beyond EOH, as described in the separate note on this subject.

{numref}`tiam-world-exoforcing-example` shows an example of specification of the EXOFORCING time series.

:::{table} Parameters of the climatic module (default values).
:name: cli-parameters

| Attribute  | Lim | DataYear | Item       | Default value |
| ---------- | :-: | :------: | ---------- | ------------: |
| CM_HISTORY |     |   2005   | CO2-ATM    |        807.27 |
| CM_HISTORY |     |   2005   | CO2-UP     |           793 |
| CM_HISTORY |     |   2005   | CO2-LO     |         19217 |
| CM_HISTORY |     |   2005   | DELTA-ATM  |          0.76 |
| CM_HISTORY |     |   2005   | DELTA-LO   |          0.06 |
| CM_HISTORY |     |   2005   | CH4-UP     |          1988 |
| CM_HISTORY |     |   2005   | CH4-ATM    |          3067 |
| CM_HISTORY |     |   2005   | N2O-UP     |          2109 |
| CM_HISTORY |     |   2005   | N2O-ATM    |           390 |
| CM_CONST   |     |          | GAMMA      |          3.71 |
| CM_CONST   |     |          | PHI-UP-AT  |        0.0453 |
| CM_CONST   |     |          | PHI-AT-UP  |        0.0495 |
| CM_CONST   |     |          | PHI-LO-UP  |       0.00053 |
| CM_CONST   |     |          | PHI-UP-LO  |        0.0146 |
| CM_CONST   |     |          | LAMBDA     |          1.41 |
| CM_CONST   |     |          | CS         |           2.9 |
| CM_CONST   |     |          | SIGMA1     |         0.024 |
| CM_CONST   |     |          | SIGMA2     |          0.44 |
| CM_CONST   |     |          | SIGMA3     |         0.002 |
| CM_CONST   |     |          | CO2-PREIND |         596.4 |
| CM_CONST   |     |          | PHI-CH4    |       0.09158 |
| CM_CONST   |     |          | PHI-N2O    |      0.008803 |
| CM_LINFOR  | LO  |   2005   | CO2-PPM    |           375 |
| CM_LINFOR  | UP  |   2005   | CO2-PPM    |           550 |
| CM_LINFOR  |  N  |   2005   | CH4-PPB    |       0.00034 |
| CM_LINFOR  | FX  |   2005   | CH4-PPB    |      -0.11000 |
| CM_LINFOR  |  N  |   2005   | N2O-PPB    |       0.00292 |
| CM_LINFOR  | FX  |   2005   | N2O-PPB    |      -0.76900 |
| CM_MAXC    |     |   2005   | CO2-PPM    |           500 |
| CM_MAXC    |     |   2005   | CO2-ATM    |          1000 |
| CM_MAXC    |     |   2005   | FORCING    |            10 |
| CM_MAXC    |     |   2005   | DELTA-ATM  |            10 |
| CM_MAXC    |     |   2005   | CO2-GTC    |            50 |
| CM_CONST   |     |          | EXT-EOH    |          2150 |
| CM_CONST   |     |          | BEOHMOD    |            20 |
| CM_MAXC    |     |   2200   | CO2-GTC    |             0 |
:::

:::{table} Example of EXOFORCING (from TIAM-WORLD, 2010 version).
:name: tiam-world-exoforcing-example

|  Attribute |  DataYear |  Value    |
| -----------|-----------|---------  |
| CM_EXOFORC |  2005     |  -0.25376 |
| CM_EXOFORC | 2010      | -0.20475  |
| CM_EXOFORC | 2015      | -0.16055  |
| CM_EXOFORC | 2020      | -0.11689  |
| CM_EXOFORC | 2025      | -0.10104  |
| CM_EXOFORC | 2030      | -0.0774   |
| CM_EXOFORC | 2035      | -0.06398  |
| CM_EXOFORC | 2040      | -0.03787  |
| CM_EXOFORC | 2045      | -0.0354   |
| CM_EXOFORC | 2050      | -0.04528  |
| CM_EXOFORC | 2055      | -0.06434  |
| CM_EXOFORC | 2060      | -0.08634  |
| CM_EXOFORC | 2065      | -0.09485  |
| CM_EXOFORC | 2070      | -0.09632  |
| CM_EXOFORC | 2075      | -0.09254  |
| CM_EXOFORC | 2080      | -0.08929  |
| CM_EXOFORC | 2085      | -0.08868  |
| CM_EXOFORC | 2090      | -0.08273  |
| CM_EXOFORC | 2095      | -0.0796   |
| CM_EXOFORC | 2100      | -0.07447  |
:::
