(a-variables)=
# Variables

The variables that are used in the Climate Module in TIMES are presented in {numref}`cli-specific-variables` below. The climate indicators represented in the Climate Module are grouped according to the following internal sets, which are referred to in the GAMS formulation, presented in Section {numref}`%s <a-equations>`:

- **cm_var**: the set of all climate indicators
- **cm_tkind**: aggregate total indicators (CO2-GtC, CH4-Mt, N2O-Mt, FORCING)
- **cm_emis**: emission indicators (CO2-GtC, CH4-Mt, N2O-Mt)
- **cm_boxmap<sub>tkind,cm_var,cm_box</sub>**: mapping between aggregate indicators tkind, reservoir indicators cm_var, and corresponding box labels (ATM/UP/LO);
- **cm_atmap<sub>tkind,cm_var</sub>**: mapping between aggregate indicators *tkind* and the corresponding boundable atmospheric indicators (CO2-PPM / CH4-PPM / N2O-PPM / DELTA_ATM);
- **cm_atbox<sub>tkind,cm_box</sub>**: mapping between mapping between aggregate emission indicators *tkind* and the corresponding reservoirs that comprise the atmospheric concentration part; contains the pairs {(CO2-GtC,ATM),(CH4-Mt,ATM),(CH4-Mt,UP),(N2O-Mt,ATM),(N2O-Mt,UP)}

```{list-table} Model variables specific to the Climate Module.
:name: cli-specific-variables
:header-rows: 1

* - Variable (Indexes) 
  - Variable Description
* - VAR_CLITOT (cm_var,y)
  - Represents the total amount of climate indicator *cm_var* in year y, where *cm_var* is one of {CO2-GtC, CH4-Mt, N2O-Mt, FORCING}
* - VAR_CLIBOX (cm_var,y)
  - Represents the amount of reservoir indicator *cm_var* in a single reservoir/box in year y, where *cm_var* is one of {CO2-ATM, CO2-UP, CO2-LO, CH4-ATM, CH4-UP, N2O-ATM, N2O-UP, DELTA-ATM, DELTA-LO}.
```

## VAR_CLITOT(cm_var,y)

**Description:** The total amount of aggregate climate indicator in year y.

**Purpose and Occurrence:** This variable tracks the total amount of an aggregate climate indicator by period. This variable is generated for each main emission type of the Climate Module as well as for the total forcing from all greenhouse gas concentrations.

**Units:** GtC (for CO<sub>2</sub> emissions), Mt (for CH<sub>4</sub> and N<sub>2</sub>O emissions), or W/m<sup>2</sup> (for total radiative forcing).

**Bounds:** This variable can be directly bounded with the CM_MAXC attribute.

## VAR_CLIBOX(cm_var,y)

**Description:** The amount of climate indicator in a reservoir.

**Purpose and Occurrence:** This variable tracks the amount of reservoir-specific climate indicator by period. This variable is generated for each of the reservoirs for each of the aggregate indicators: ATM/UP/LO for CO<sub>2</sub> emissions, ATM/UP for CH<sub>4</sub> and N<sub>2</sub>O emissions, and ATM/LO for FORCING (connected to the temperature reservoirs).

**Units:** GtC (for CO<sub>2</sub> emissions), Mt (for CH<sub>4</sub> and N<sub>2</sub>O emissions), or °C (for temperature reservoirs).

**Bounds:** Only the total atmospheric amounts can be bounded with the CM_MAXC attribute (CO2-ATM, CO2-PPM, CH4-PPB, N2O-PPB, DELTA-ATM).
