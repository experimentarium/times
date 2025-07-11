(sets)=
# Sets

Sets are used in TIMES to group elements or combinations of elements with the purpose of specifying qualitative characteristics of the energy system. One can distinguish between one-dimensional and multi-dimensional sets. The former sets contain single elements, e.g. the set $prc$ contains all processes of the model, while the elements of multi-dimensional sets are a combination of one-dimensional sets. An example for a multi-dimensional set is the set $top$, which specifies for a process the commodities entering and leaving that process.

Two types of sets are employed in the TIMES framework: user input sets and internal sets. User input sets are created by the user, and used to describe qualitative information and characteristics of the depicted energy system. One can distinguish the following functions associated with user input sets:
- definition of the elements or building blocks of the energy system model (i.e. regions, processes, commodities),
- definition of the time horizon and the sub-annual time resolution,
- definition of special characteristics of the elements of the energy system.

In addition to these user sets, TIMES also generates its own internal sets. Internal sets serve to both ensure proper exception handling (e.g., from what date is a technology available, or in which time-slices is a technology permitted to operate), as well as sometimes just to improve the performance or smooth the complexity of the actual model code.

In the following sections, the user input sets and the internal sets will be presented. A special type of set is a one-dimensional set, also called index, which is needed to build multi-dimensional sets or parameters. At the highest level of the one-dimensional sets are the master or "domain" sets that define the comprehensive list of elements (e.g., the main building blocks of the reference energy system such as the processes and commodities in all regions) permitted at all other levels, with which GAMS performs complete domain checking, helping to automatically ensure the correctness of set definition (for instance, if the process name used in a parameter is not spelled correctly, GAMS will issue a warning). Therefore, before elaborating on the various sets, the indexes used in TIMES are discussed.

## Indexes (One-dimensional sets)

Indexes (also called one-dimensional sets) contain in most cases the different elements of the energy model. A list of all indexes used in TIMES is given in {numref}`indexes-in-times`. Examples of indexes are the set $prc$ containing all processes, the set $c$ containing all commodities, or the set $all\_reg$ containing all regions of the model. Some of the one-dimensional sets are subsets of another one-dimensional set, e.g., the set $r$ comprising the so-called internal model regions is a subset of the set $all\_reg$, which in addition also contains the so-called external model regions[^2]. To express that the set $r$ depends on the set $all\_reg$, the master set $all\_reg$ is put in brackets after the set name $r$: $r(all\_reg)$.

The set $cg$ comprises all commodity groups[^3]. Each commodity $c$ is considered as a commodity group with only one element: the commodity itself. Thus the commodity set $c$ is a subset of the commodity group set $cg$.

Apart from indexes that are under user control, some indexes have fixed elements to serve as indicators within sets and parameters, most of which should not be modified by the user ({numref}`sets-with-fixed-elements`). Exceptions to this rule are the sets defined in the file MAPLISTS.DEF. For example, while the process groups ($prc\_grp$) listed in {numref}`sets-with-fixed-elements` are used within the code and must not be deleted, other process groups may be added by the user.

```{list-table} Sets with fixed elements
:name: sets-with-fixed-elements
:header-rows: 1

* - Set/Index name
  - Description
* - **Sets defined in INITSYS.MOD (never to be changed by the user)**
  - 
* - bd(lim)
  - Index of bound type; subset of the set lim having the internally fixed elements \'LO\', \'UP\', \'FX\'.
* - costagg
  - List of cost aggregation types available for user-defined cost constraints:
  <br>INV investment costs
  <br>INVTAX investment taxes
  <br>INVSUB investment subsidies
  <br>INVTAXSUB investment taxes and subsidies
  <br>INVALL all investment costs, taxes and subsidies
  <br>FOM fixed O&M costs
  <br>FOMTAX fixed operating taxes
  <br>FOMSUB fixed operating subsidies
  <br>FOMTAXSUB fixed operation taxes and subsidies
  <br>FOMALL all fixed operation costs, taxes and subsidies
  <br>COMTAX commodity taxes
  <br>COMSUB commodity subsidies
  <br>COMTAXSUB commodity taxes and subsidies
  <br>FLOTAX taxes
  <br>FLOSUB subsidies
  <br>FLOTAXSUB flow taxes and subsidies
  <br>FIX total fixed costs (investment+fixed O&M costs)
  <br>FIXTAX total fixed taxes
  <br>FIXSUB total fixed subsidies
  <br>FIXTAXSUB total fixed taxes and subsidies
  <br>FIXALL all fixed costs, taxes and subsidies
  <br>ALLTAX all taxes
  <br>ALLSUB all subsidies
  <br>ALLTAXSUB all taxes and subsidies
* - ie
  - Export/import exchange index; internally fixed to the two elements: \'IMP\' standing for import and \'EXP\' standing for export.
* - io
  - Input/Output index; internally fixed elements: \'IN\', \'OUT\'; used in combination with processes and commodities as indicator whether a commodity enters or leaves a process.
* - lim
  - Index of limit types; internally fixed to the elements \'LO\', \'UP\', \'FX\', \'N\'.
* - side
  - Index of constraint sides; internally fixed to the elements \'LHS\', \'RHS\'
* - tslvl
  - Index of timeslice levels; internally fixed to the elements \'ANNUAL\', \'SEASON\', \'WEEKLY\', \'DAYNITE\'.
* - uc_grptype
  - Index of internally fixed key types of variables:
  <br>ACT, FLO, IRE, CAP, NCAP, COMPRD, COMNET, COMCON, UCN
  <br>These are used in association with the user constraints.
* - uc_cost
  - Internally fixed list of cost types that can be used as modifier attributes in user constraints: COST, DELIV, TAX, SUB
* - uc_name
  - List of internally fixed indicators for attributes able to be referenced as coefficients in user constraints (e.g. the flow variable may be multiplied by the attribute FLO_COST in a user constraint if desired):
  <br>COST, DELIV, TAX, SUB, EFF, NET, BUILDUP, CAPACT, CAPFLO, GROWTH, NEWFLO, ONLINE, PERIOD, PERDISC, INVCOST, INVTAX, INVSUB, CUMSUM, SYNC, YES
  <br>See Section 6.4.6 for more detailed information.
* - **Sets defined in MAPLIST.DEF (additional elements may be added by user)**
  - 
* - com_type
  - Indicator of commodity type; initialized to the following elements:
  <br>DEM demand
  <br>NRG energy
  <br>MAT material
  <br>ENV environment
  <br>FIN financial
  <br>The predefined elements should never be deleted.
* - dem_sect
  - List of demand sectors; internally established in MAPLIST.DEF as:
  <br>AGR agriculture
  <br>RES residential
  <br>COM commercial and public services
  <br>IND industry
  <br>TRN transport
  <br>NE non-energy
  <br>OTH other
  <br>The predefined elements should not be deleted.
* - env_type
  - List of emission types; internally established in MAPLIST.DEF as:
  <br>GHG greenhouse gas
  <br>PEM particulate matter emissions
  <br>OEM other emissions into air or water
  <br>OTHENV other environmental indicator
* - nrg_type
  - List of energy types; internally established in MAPLIST.DEF as:
  <br>FOSSIL fossil fuel
  <br>NUCLR nuclear
  <br>SYNTH synthetic fuel
  <br>FRERENEW free renewable
  <br>LIMRENEW limited renewable (no commodity balance)
  <br>ELC electricity
  <br>HTHEAT high temperature heat
  <br>LTHEAT low temperature heat
  <br>CONSRV conservation
  <br>The predefined elements should not be deleted.
* - prc_grp
  - List of process groups; internally established in MAPLIST.DEF as:
  <br>CHP combined heat and power plant
  <br>DISTR distribution process
  <br>DMD demand device
  <br>ELE electricity producing technology excluding CHP
  <br>HPL heat plant
  <br>IRE inter-regional exchange process
  <br>MISC miscellaneous
  <br>PRE energy technology not falling in other groups
  <br>PRV technology with material output measured in volume units
  <br>PRW technology with material output measured in weight units
  <br>REF refinery process
  <br>RENEW renewable energy technology
  <br>XTRACT extraction process
  <br>NST night (off-peak) storage process
  <br>STG storage process (timeslice storage, unless also STK/NST)
  <br>STK stockpiling process (inter-period storage)
  <br>STS generalized timeslice storage
  <br>The user may augment this list with any additional groups desired. The following predefined groups affect the data processing carried out by the model generator,and should not be deleted by the user: CHP, DISTR, DMD, ELE, HPL, IRE, PRE, PRV, PRW, REF, NST, STG, STK and STS.
```

```{list-table} Indexes in TIMES
:name: indexes-in-times
:header-rows: 1

* - Index[^4]
  - Aliases[^5]
  - Related Indexes[^6]
  - Description
* - age
  - life, jot
  - 
  - Index for age (number of years since installation) into a parameter shaping curve; default elements 1--200.
* - all_r
  - all_reg
  - r
  - All internal and external regions.
* - bd
  - bnd_type
  - lim
  - Index of bound type; subset of lim, having the internally fixed elements 'LO', 'UP', 'FX'.
* - c(cg)
  - com, com1, com2, com3
  - cg
  - User defined[^7] list of all commodities in all regions; subset of cg.
* - cg
  - com_grp, cg1, cg2, cg3, cg4
  - c
  - User defined list of all commodities and commodity groups in all regions[^8]; each commodity itself is considered a commodity group; initial elements are the members of com_type.
* - com_type
  - 
  - 
  - Indicator of commodity type; initialized to the predefined types DEM, NRG, MAT, ENV, FIN (see {numref}`sets-with-fixed-elements`).
* - costagg
  - 
  - 
  - Indicator of cost aggregation type; initialized to list of predefined types (see {numref}`sets-with-fixed-elements`).
* - cur
  - cur
  - 
  - User defined list of currency units.
* - datayear (year)
  - 
  - year
  - Years for which model input data are specified.
* - dem_sect
  - 
  - 
  - Indicator of demand sector; initialized to list of predefined sectors (see {numref}`sets-with-fixed-elements`);
* - env_type
  - 
  - 
  - Indicator of environmental commodity type; initialized to list of predefined elements (see {numref}`sets-with-fixed-elements`);
* - ie
  - impexp
  - 
  - Export/import exchange indicator; internally fixed = \'EXP\' for exports and \'IMP\' for imports.
* - io
  - inout
  - 
  - Input/Output indicator for defining whether a commodity flow enters or leaves a process; internally fixed = \'IN\' for enters and \'OUT\' for leaves.
* - j
  - jj
  - 
  - Indicator for elastic demand steps and sequence number of the shape/multi curves; default elements 1--999.
* - kp
  - 
  - 
  - Index for "kink" points in ETL formulation; currently limited to 1-6 {can be extended in \<case\>.run file by including SET KP / 1\*n /; for n-kink points.
* - lim
  - lim_type, l
  - bd
  - Index of limit types; internally fixed = \'LO\', \'UP\', \'FX\' and \'N\'.
* - nrg_type
  - 
  - 
  - Indicator of energy commodity type; initialized to predefined types (see {numref}`sets-with-fixed-elements`);
* - p
  - prc
  - 
  - User defined list of all processes in all regions[^9].
* - pastyear
  - pyr
  - modlyear, year
  - Years for which past investments are specified; pastyears should usually be before the beginning of the first period but past investments may also be specified on later years.
* - prc_grp
  - 
  - 
  - List of process groups; internally established in MAPLIST.DEF (see {numref}`sets-with-fixed-elements`).
* - r(all_r)
  - reg
  - all_r
  - Explicit regions within the area of study.
* - s
  - all_ts, ts, s2, sl
  - 
  - Timeslice divisions of a year, at any of the tslvl levels.
* - side
  - 
  - 
  - Side indicator for defining coefficients in user constraints; internally fixed = \'LHS\', \'RHS\'
* - t
  - milestonyr, tt
  - year
  - Representative years for the model periods.
* - teg
  - 
  - p
  - Technologies modelled with endogenous technology learning.
* - tslvl
  - 
  - 
  - Timeslice level indicator; internally fixed = \'ANNUAL\', \'SEASON\', \'WEEKLY\', \'DAYNITE\'.
* - u
  - units
  - units_com, units_cap, units_act
  - List of all units; maintained in the file UNITS.DEF.
* - uc_grptype
  - 
  - 
  - Fixed internal list of the key types of variables (see {numref}`sets-with-fixed-elements`).
* - uc_n
  - ucn
  - 
  - User specified unique indicator for a user constraint.
* - uc_name
  - 
  - 
  - Fixed list of indicators associated with various attributes that can be referenced in user constraints to be applied when deriving a coefficient (see {numref}`sets-with-fixed-elements`).
* - unit
  - 
  - 
  - List of capacity blocks that can be added in lumpy investment option; default elements 0--100; the element \'0\' describes the case when no capacity is added.
* - units_act
  - 
  - u
  - List of activity units; maintained in the file UNITS.DEF.
* - units_cap
  - 
  - u
  - List of capacity units; maintained in the file UNITS.DEF.
* - units_com
  - 
  - u
  - List of commodity units; maintained in the file UNITS.DEF.
* - v(year)
  - modlyear
  - pastyear, t
  - Union of the set pastyear and t corresponding to all modelling periods.
* - ww
  - allsow
  - sow, w
  - States of the world that can be used; default elements 1--64; under user control by the dollar control parameter \$SET MAXSOW \<n\> in the \<case\>.RUN file.
* - year
  - allyear, ll
  - datayear, pastyear, modlyear, milestonyr
  - Years that can be used in the model; default range 1850-2200; under user control by the dollar control parameters \$SET BOTIME \<y\> and \$SET EOTIME \<y\> in the \<case\>.RUN file.
```

##  User input sets

The user input sets contain the fundamental information regarding the structure and the characteristics of the underlying energy system model. The user input sets can be grouped according to the type of information related to them:
- One dimensional sets defining the components of the energy system: regions, commodities, processes;
- Sets defining the Reference Energy System (RES) within each region;
- Sets defining the inter-connections (trade) between regions;
- Sets defining the time structure of the model: periods, timeslices, timeslice hierarchy;
- Sets defining various properties of processes or commodities.

The formulation of user constraints also uses sets to specify the type and the features of a constraint. The structure and the input information required to construct a user constraint is covered in detail in Chapter {numref}`%s <equations>`, and therefore will not be presented here.

Most of the set specifications are handled for the user by the user shell through process and commodity characterization, and the user does not need to input these sets directly.

In the following subsections first the sets related to the definition of the RES will be described (subsection {numref}`%s <definition-of-the-reference>`), then the sets related to the time horizon and the sub-annual representation of the energy system will be presented (subsection {numref}`%s <definition-of-the-time-structure>`). The mechanism for defining trade between regions of a multi-regional model is discussed in subsection {numref}`%s <multi-regional-models>`. Finally, an overview of all possible user input sets is given in subsection {numref}`%s <overview-of-all-user-input>`.

(definition-of-the-reference)=
### Definition of the Reference Energy System (RES)

A TIMES model is structured by regions ($all\_r$). One can distinguish between external regions and internal regions. The internal regions ($r$) correspond to regions within the area of study, and for which a RES has been defined by the user. Each internal region may contain processes and commodities to depict an energy system, whereas external regions serve only as origins of commodities (e.g. for import of primary energy resources or for the import of energy carriers) or as destination for the export of commodities. A region is defined as an internal region by putting it in the internal region set ($r$), which is a subset of the set of all regions **all_r**. An external region needs no explicit definition, all regions that are member of the set $all\_r$ but not member of $r$ are external regions. A TIMES model must consist of at least one internal region, the number of external regions is arbitrary. The main building blocks of the RES are processes ($p$) and commodities ($c$), which are connected by commodity flows to form a network. An example of a RES with one internal region (UTOPIA) and two external regions (IMPEXP, MINRNW) is given in {numref}`inter-external-regions`.

All components of the energy system, as well as nearly the entire input information, are identified by a region index. It is therefore possible to use the same process name in different regions with different numerical data (and description if desired), or even completely different commodities associated with the process.

```{figure} assets/ie-regions.svg
:name: inter-external-regions
:align: center
Example of internal and external regions in TIMES.
```

#### Processes

A process may represent an individual plant, e.g. a specific existing nuclear power plant, or a generic technology, e.g. the coal-fired IGCC technology. TIMES distinguishes three main types of processes:
- Standard processes;
- Inter-regional exchange processes, and
- Storage processes.

##### Standard processes

The so-called standard processes can be used to model the majority of the energy technologies, e.g., condensing power plants, heat plants, CHP plants, demand devices such as boilers, coal extraction processes, etc. Standard processes can be classified into the following groups:
- PRE for generic energy processes;
- PRW for material processing technologies (by weight);
- PRV for material processing technologies (by volume);
- REF for refinery processes;
- ELE for electricity generation technologies;
- HPL for heat generation technologies;
- CHP for combined heat and power plants;
- DMD for demand devices;
- DISTR for distribution systems;
- MISC for miscellaneous processes.

The process classification is done via the set $prc\_map(r,prc\_grp,p)$. This grouping is mainly intended for reporting purposes, but in some cases it also affects the properties of the processes[^10] and the constraint matrix. The set is maintained in the MAPLIST.DEF file, and may be adjusted by user with additional technology groups of interest, with some restrictions as noted in {numref}`sets-with-fixed-elements`.

The topology of a standard process is specified by the set $top(r,p,c,io)$ of all quadruples such that the process $p$ in region $r$ is consuming ($io =$ 'IN') or producing ($io =$ 'OUT') commodity $c$. Usually, for each entry of the topology set **top** a flow variable (see $VAR\_FLO$ in Chapter {numref}`%s <variables>`) will be created. When the so-called *reduction algorithm* is activated, some flow variables may be eliminated and replaced by other variables (see PART III, Section 3.7 for details).

The activity variable ($VAR\_ACT$) of a standard process is in most cases equal to the sum of one or several commodity flows on either the input or the output side of a process. The activity of a process is limited by the available capacity, so that the activity variable establishes a link between the installed capacity of a process and the maximum possible commodity flows entering or leaving the process during a year or a subdivision of a year. The commodity flows that define the process activity are specified by the set $prc\_actunt(r,p,cg,u)$ where the commodity index $cg$ may be a single commodity or a user-defined commodity group, and $u$ is the activity unit. The commodity group defining the activity of a process is also called **P**rimary **C**ommodity **G**roup (PCG).

```{figure} assets/cg-definition-example.svg
:name: cg-activity
:align: center
Example of the definition of a commodity group and the activity of a normal process.
```

User-defined commodity groups are specified by means of the set $com\_gmap(r,cg,c)$, which indicates the commodities ($c$) belonging to the group ($cg$). Once a user-defined commodity group has been defined, one can use it for any processes for defining attributes that require a commodity group (not only for the definition of the process activity, but also for other purposes, e.g., in the transformation equation $EQ\_PTRANS$), as long as the members of the group are valid for the particular process and the process characteristic to be defined.

An example for the definition of the activity of a process is shown in {numref}`cg-activity`. In order to define the activity of the process SRE as the sum of the two output flows of gasoline (GSL) and diesel (DSL), one has to define a commodity group called CG_SRE containing these two commodities. The name of the commodity group can be arbitrarily chosen by the modeller.

In addition to the activity of a process, one has to define the capacity unit of the process. This is done by means of the set $prc\_capunt(r,p,cg,u)$, where the index **cg** denotes the primary commodity group. In the example in {numref}`cap-unit-def` the capacity of the refinery process is defined in mtoe/a (megatonne oil equivalent). Since the capacity and activity units are different (mtoe for the capacity and PJ for the activity), the user has to supply the conversion factor from the energy unit embedded in the capacity unit to the activity unit. This is done by specifying the parameter $prc\_capact(r,p)$. In the example $prc\_capact$ has the value 41.868.

```{figure} assets/cap-unit-definition-example.svg
:name: cap-unit-def
:align: center
Example of the definition of the capacity unit.
```

It might occur that the unit in which the commodity(ies) of the primary commodity group are measured, is different from the activity unit. An example is shown in {numref}`different-cap-unit-def`. The activity of the transport technology CAR is defined by commodity TX1, which is measured in passenger kilometres PKM. The activity of the process is, however, defined in vehicle kilometres VKM, while the capacity of the process CAR is defined as number of cars NOC.

```{figure} assets/diff-cap-and-act-units-example.svg
:name: different-cap-unit-def
:align: center
Example of different activity and commodity units.
```

The conversion factor from capacity to activity unit $prc\_capact$ describes the average mileage of a car per year. The process parameter $prc\_actflo(r,y,p,cg)$ contains the conversion factor from the activity unit to the commodity unit of the primary commodity group. In the example this factor corresponds to the average number of persons per car (1.5).

##### Inter-regional exchange processes

Inter-regional exchange (IRE) processes are used for trading commodities between regions. They are needed for linking internal regions with external regions as well as for modelling trade between internal regions. A process is specified as an inter-regional exchange process by specifying it as a member of the set $prc\_map(r,'IRE',p)$. If the exchange process is connecting internal regions, this set entry is required for each of the internal regions trading with region $r$. The topology of an inter-regional exchange process $p$ is defined by the set $top\_ire(all\_reg,com,all\_r,c,p)$ stating that the commodity $com$ in region $all\_reg$ is exported to the region $all\_r$ (the traded commodity may have a different name $c$ in region $all\_r$ than in region $all\_reg$). For example the topology of the export of the commodity electricity (ELC_F) from France (FRA) to Germany (GER), where the commodity is called ELC_G via the exchange process (HV_GRID) is modelled by the $top\_ire$ entry:

```
top_ire('FRA', 'ELC_F', 'GER', 'ELC_G', 'HV_GRID')
```

The first pair of region and commodity (\'FRA\', \'ELC_F\') denotes the origin and the name of the traded commodity, while the second pair (\'GER\', \'ELC_G\') denotes the destination. The name of the traded commodity can be different in both regions, here \'ELC_F\' in France and \'ELC_G\' in Germany, depending on the chosen commodity names in both regions. As with standard processes, the activity definition set $prc\_actunt(r,p,cg,u)$ has to be specified for an exchange process belonging to each internal region. The special features related to inter-regional exchange processes are described in subsection {numref}`%s <multi-regional-models>`.

##### Storage processes

Storage processes are used to store a commodity either between periods or between timeslices. A process ($p$) can be specified to be an inter-period storage (IPS) process for commodity ($c$) by defining the process to be of the type \'**STK**\' and $c$ as its PCG (or, alternatively, including it as a member of the set $prc\_stgips(r,p,c)$). In a similar way, a process is characterised as a timeslice storage by defining the process to be of the type \'**STG**\' and $c$ as its PCG (alternatively, by inclusion in the set $prc\_stgtss(r,p,c)$). A special case of timeslice storage is a so-called night-storage device (NST) where the commodity for charging and the one for discharging the storage are different. An example for a night storage device is an electric heating technology which is charged during the night using electricity and produces heat during the day. Including a process in the set $prc\_nstts(r,p,s)$ indicates that it is a night storage device which is charged in timeslice(s) $s$. More than one timeslice can be specified as charging timeslices, the non-specified timeslices are assumed to be discharging timeslices. The charging and discharging commodity of a night storage device are specified by the topology set ($top$). It should be noted that for inter-period storage and normal timeslice storage processes (non-NST) the commodity entering and leaving the storage (the charged and discharged commodity) should be a member of the PCG (and both should be, if they are different). Other auxiliary commodity flows are also permitted in combination with these two storage types, by including them in the topology (see Section {numref}`%s <auxiliary-storage-flows>`).

As for standard processes, the flows that define the activity of a storage process are identified by providing the set $prc\_actunt(r,p,c)$ entry. In contrast to standard processes, the activity of a storage process is however interpreted as the amount of the commodity being stored in the storage process. Accordingly the capacity of a storage process describes the maximum commodity amount that can be kept in storage.

Internally, a $prc\_map(r,'STG',p)$ entry is always generated for all storage processes to put the process in the group of storage processes. A further $prc\_map$ entry is created to specify the type of storage (\'STK\' for inter-period storage, \'STS\' for general time-slice storage and \'NST\' for a night-storage device), unless already defined so by the user.

#### Commodities

As mentioned before, the set of commodities ($c$) is a subset of the commodity group set ($cg$). A commodity in TIMES is characterised by its type, which may be an energy carrier (\'NRG\'), a material (\'MAT\'), an emission or environmental impact (\'ENV\'), a demand commodity (\'DEM\') or a financial resource (\'FIN\'). The commodity type is indicated by membership in the commodity type mapping set ($com\_tmap(r,com\_type,c)$). The commodity type affects the default sense of the commodity balance equation. For NRG, ENV and DEM the commodity production is normally greater than or equal to consumption, while for MAT and FIN the default commodity balance constraint is generated as an equality. The type of the commodity balance can be modified by the user for individual commodities by means of the commodity limit set ($com\_lim(r,c,lim)$). The unit in which a commodity is measured is indicated by the commodity unit set ($com\_unit(r,c,units\_com)$). The user should note that within the GAMS code of TIMES no unit conversion, e.g., of import prices, takes place when the commodity unit is changed from one unit to another one. Therefore, the proper handling of the units is entirely the responsibility of the user (or the user interface).

(definition-of-the-time-structure)=
### Definition of the time structure

#### Time horizon

The time horizon for which the energy system is analysed may range from one year to many decades. The time horizon is usually split into several *periods* which are represented by so-called *milestone years* ($t(allyear)$ or $milestonyr(allyear)$, see {numref}`time-horizon-year-type`). Each milestone year represents a point in time where decisions may be taken by the model, e.g. installation of new capacity or changes in the energy flows. The activity and flow variables used in TIMES may therefore be considered as average values over a period. The shortest possible duration of a period is one year. However, in order to keep the number of variables and equations at a manageable size, periods are usually comprised of several years. The durations of the periods do not have to be equal, so that it is possible that the first period, which usually represents the past and is used to calibrate the model to historic data, has a length of one year, while the following periods may have longer durations. Thus in TIMES both the number of periods and the duration of each period are fully under user control. The beginning year of a period $t$, $B(t)$, and its ending year, $E(t)$, have to be specified as input parameters by the user (see Table 13 in subsection {numref}`%s <overview-of-user-input-parameters>`).

To describe capacity installations that took place before the beginning of the model horizon, and still exist during the modeling horizon, TIMES uses additional years, the so-called past years ($pastyear(allyear)$), which identify the construction completion year of the already existing technologies. The amount of capacity that has been installed in a past year is specified by the parameter $NCAP\_PASTI(r,allyear,p)$, also called *past investment*. For a process, an arbitrary number of past investments may be specified to reflect the age structure in the existing capacity stock. The union of the sets $milestonyr$ and $pastyear$ is called $modelyear$ (or $v$). The years for which input data is provided by the user are called data years ($datayear(allyear)$). The data years do not have to coincide with model years, since the preprocessor will interpolate or extrapolate the data internally to the model years. All past years are by default included in data years, but, as a general rule, any other years for which input data is provided should be explicitly included in the set $datayear$ or that information will not be seen by the model. Apart from a few exceptions (see {numref}`datayear-independent-parameters`), all parameter values defined for years other than data years (or past years) are ignored by the model generator. Due to the distinction between model years and data years, the definition of the model horizon, e.g., the duration and number of the periods, may be changed without having to adjust the input data to the new periods. The rules and options of the inter- and extrapolation routine are described in more detail in subsection {numref}`%s <inter-and-extrapolation-of-user>`.

```{figure} assets/time-horizon-and-year-types.svg
:name: time-horizon-year-type
:align: center

Definition of the time horizon and the different year types.
```

One should note that it is possible to define past investments ($NCAP\_PASTI$) not only for past years but also for any years within the model horizon, including the milestone years. Since the first period(s) of a model may cover historical data, it is useful to store the already known capacity installations made during this time-span as past investments and not as a bound on new investments in the model database. If one later changes the beginning of the model horizon to a more recent year, the capacity data of the first period(s) do not have to be changed, since they are already stored as past investments. This feature therefore supports the decoupling of the data years, for which input information is provided, and the definition of the model horizon for which the model is run, making it relatively easy to change the definition of the modeling horizon. Defining past investments for years within the actual model horizon may also be useful for identifying already planned (although not yet constructed) capacity expansions in the near future[^11].

```{list-table} Parameters that can have values defined for any year, irrespective of datayear[^12]
:name: datayear-independent-parameters
:header-rows: 1

* - Attribute name
  - Description
* - G_DRATE
  - General discount rate for currency in a particular year
* - MULTI
  - Parameter multiplier table with values by year
* - ACT_CUM
  - Cumulative limit on process activity
* - FLO_CUM
  - Cumulative limit on process flow
* - COM_CUMPRD
  - Cumulative limit on gross production of a commodity for a block of years
* - COM_CUMNET
  - Cumulative limit on net production of a commodity for a block of years
* - REG_CUMCST
  - Cumulative limit on regional costs, taxes or subsidies
* - UC_CUMACT
  - Coefficient for a cumulative amount of process activity in a user constraint
* - UC_CUMFLO
  - Coefficient for a cumulative amount of process flow in a user constraint
* - CM_EXOFORC
  - Radiative forcing from exogenous sources; included in the climate module extension (see Appendix A for a description of the climate module).
* - CM_HISTORY
  - Climate module calibration values; included in the climate module extension (see Appendix A for a description of the climate module).
* - CM_MAXC
  - Maximum level of climate variable; included in the climate module extension (see Appendix A for a description of the climate module).
```

#### Timeslices

The **milestone** years can be further divided in sub-annual timeslices in order to describe for the changing electricity load within a year, which may affect the required electricity generation capacity, or other commodity flows that need to be tracked at a finer than annual resolution. Timeslices may be organised into four hierarchy levels only: \'ANNUAL\', \'SEASON\', \'WEEKLY\' and \'DAYNITE\' defined by the internal set $tslvl$. The level ANNUAL consists of only one member, the predefined timeslice \'ANNUAL\', while the other levels may include an arbitrary number of divisions. The desired timeslice levels are activated by the user providing entries in set $ts\_group(r,tslvl,s)$, where also the individual user-provided timeslices ($s$) are assigned to each level. An additional user input set $ts\_map(r,s1,s2)$ is needed to determine the structure of a timeslice tree, where timeslice $s1$ is defined as the parent node of $s2$. {numref}`p2-timeslice-tree` illustrates a timeslice tree, in which a year is divided into four seasons consisting of working days and weekends, and each day is further divided into day and night timeslices. The name of each timeslice has to be unique in order to be used later as an index in other sets and parameters. Not all timeslice levels have to be utilized when building a timeslice tree, for example one can skip the \'WEEKLY\' level and directly connect the seasonal timeslices with the daynite timeslices. The duration of each timeslice is expressed as a fraction of the year by the parameter $G\_YRFR(r,s)$. The user is responsible for ensuring that each lower level group sums up properly to its parent timeslice, as this is not verified by the pre-processor.

The definition of a timeslice tree is region-specific.[^13] When different timeslice names and durations are used in two regions connected by exchange processes, the mapping parameters $IRE\_CCVT(r,c,reg,com)$ for commodities and $IRE\_TSCVT(r,s,reg,ts)$ for timeslices have to be provided by the user to map the different timeslice definitions. When the same timeslice definitions are used, these mapping tables do not need to be specified by the user.

The original design of TIMES assumes that within each region, the definition of the timeslice tree applies to all model periods, such that one cannot employ different subsets of timeslices in different periods. In fact, allowing dynamically changing timeslice trees would tend to make both the model pre-processing and equation formulations substantially more complex, and therefore this design decision may be considered well justified. However, an experimental \"light-weight\" implementation has been made in view of supporting also dynamic timeslice trees (see Appendix E).

```{figure} ../assets/timeslice-tree-example.svg
:name: p2-timeslice-tree
:align: center
Example of a timeslice tree.
```

Commodities may be tracked and process operation controlled at a particular timeslice level by using the sets $com\_tsl(r,c,tslvl)$ and $prc\_tsl(r,p,tslvl)$ respectively. Providing a commodity timeslice level determines for which timeslices the commodity balance will be generated, where the default is \'ANNUAL\'. For processes, the set $prc\_tsl$ determines the timeslice level of the activity variable. Thus, for instance, condensing power plants may be forced to operate on a seasonal level, so that the activity during a season is uniform, while hydropower production may vary between days and nights, if the \'DAYNITE\' level is specified for hydro power plants. Instead of specifying a timeslice level, the user can also identify individual timeslices for which a commodity or a process is available by the sets $com\_ts(r,c,s)$ and $prc\_ts(r,p,s)$ respectively. Note that when specifying individual timeslices for a specific commodity or process by means of $com\_ts$ or $prc\_ts$ they all have to be on the same timeslice level.

The timeslice level of the commodity flows entering and leaving a process are determined internally by the preprocessor. The timeslice level of a flow variable equals the timeslice level of the process when the flow variable is part of the primary commodity group (PCG) defining the activity of the process. Otherwise the timeslice level of a flow variable is set to whichever level is finer, that of the commodity or the process.

(multi-regional-models)=
### Multi-regional models

If a TIMES model consists of several internal regions, it is called a multi-regional model. Each of the internal regions contains a unique RES to represent the particularities of the region. As already mentioned, the regions can be connected by inter-regional exchange processes to enable trade of commodities between the regions. Two types of trade activities can be depicted in TIMES: bi-lateral trade between two regions and multilateral trade between several supply and demand regions.

Bi-lateral trade takes place between specific pairs of regions. A pair of regions together with an exchange process and the direction of the commodity flow are first identified, where the model ensures that trade through the exchange process is balanced between these two regions (whatever amount is exported from region A to region B must be imported by region B from region A, possibly adjusted for transportation losses). The basic structure is shown in {numref}`bilateral-trade`. Bi-lateral trading may be fully described in TIMES by defining an inter-regional exchange process and by specifying the two pair-wise connections by indicating the regions and commodities be traded via the set $top\_ire(r,c,reg,com,p)$. If trade should occur only in one direction then only that direction is provided in the set $top\_ire$ (export from region $r$ into region $reg$). The process capacity and the process related costs (e.g. activity costs, investment costs) of the exchange process can be described individually for both regions by specifying the corresponding parameters in each regions. If for example the investment costs for an electricity line between two regions A and B are 1000 monetary units (MU) per MW and 60 % of these investment costs should be allocated to region A and the remaining 40 % to region B, the investment costs for the exchange process have to be set to 600 MU/MW in region A and to 400 MU/MW in region B.

```{figure} assets/bilateral-trade-in-times.svg
:name: bilateral-trade
:align: center
Bilateral trade in TIMES.
```

Bi-lateral trade is the most detailed way to specify trade between regions. However, there are cases when it is not important to fully specify the pair of trading regions. In such cases, the so-called *multi-lateral trade* option decreases the size of the model while preserving enough flexibility. Multi-lateral trade is based on the idea that a common marketplace exists for a traded commodity with several supplying and several consuming regions for the commodity, e.g. for crude oil or GHG emission permits. To facilitate the modelling of this kind of trade scheme the concept of marketplace has been introduced in TIMES. To model a marketplace first the user has to identify one internal region that participates both in the production and consumption of the traded commodity. Then only one exchange process is used to link the supply and demand regions with the marketplace region using the set $top\_ire$.[^14]

The following example illustrates the modelling of a marketplace in TIMES. Assume that we want to set up a market-based trading where the commodity CRUD can be exported by regions A, B, C, and D, and that it can be imported by regions C, D, E and F ({numref}`multilateral-trade`).

```{figure} assets/multilateral-trade-in-times.svg
:name: multilateral-trade
:align: center
Example of multi-lateral trade in TIMES.
```

First, the exchange process and marketplace should be defined. For example, we could choose the region C as the marketplace region. The exchange process has the name XP. The trade possibilities can then be defined simply by the following six $top\_ire$ entries:

```
SET PRC /'XP'/;

SET TOP_IRE /
'A'.'CRUD'.'C'.'CRUD'.'XP'
'B'.'CRUD'.'C'.'CRUD'.'XP'
'D'.'CRUD'.'C'.'CRUD'.'XP'
'C'.'CRUD'.'D'.'CRUD'.'XP'
'C'.'CRUD'.'E'.'CRUD'.'XP'
'C'.'CRUD'.'F'.'CRUD'.'XP'
/;
```

To complete the RES definition of the exchange process, only the set $prc\_actunt(r,p,c,u)$ is needed to define the units for the exchange process XP in all regions:

```
SET PRC_ACTUNT /
'A'.'XP'.'CRUD'.'PJ'
'B'.'XP'.'CRUD'.'PJ'
'C'.'XP'.'CRUD'.'PJ'
'D'.'XP'.'CRUD'.'PJ'
'E'.'XP'.'CRUD'.'PJ'
'F'.'XP'.'CRUD'.'PJ'
/;
```

These definitions are sufficient for setting up of the market-based trade. Additionally, the user can of course specify various other data for the exchange processes, for example investment and distribution costs, and efficiencies.

(overview-of-all-user-input)=
### Overview of all user input sets

All the input sets which are under user control in TIMES are listed in Table 4. For a few sets default settings exist that are applied if no user input information is given. Set names starting with the prefix $com\_$ are associated with commodities, the prefix $prc\_$ denotes process information and the prefix $uc\_$ is reserved for sets related to user constraints. Column 3 of Table 4 is a description of each set. In some cases (especially for complex sets), two (equivalent) descriptions may be given, the first in general terms, followed by a more precise description within square brackets, given in terms of n-tuples of indices.

**Remark**

Sets are used in basically two ways:
- as the domain over which summations must be effected in some mathematical expression, or
- as the domain over which a particular expression or constraint must be enumerated (replicated).

In the case of n-dimensional sets, some indexes may be used for **enumeration and others for summation**. In each such situation, the distinction between the two uses of the indexes is made clear by the way each index is used in the expression.

An example will illustrate this important point: consider the 4-dimensional set $top$, having indexes $r,p,c,io$ (see {numref}`user-input-sets` for its precise description). If some quantity $A(r,p,c,io)$ must be enumerated for all values of the third index ($c=commodity$) and of the last index ($io=orientation$), but summed over all processes ($p$) and regions ($r$), this will be mathematically denoted:

$$EXPRESSION1_{c,io} = \sum_{r,p,c,io \in top}^{}{A(r,p,c,io)}$$

It is thus understood from the indexes listed in the name of the expression ($c,io$), that these two indexes are being enumerated, and thus, by deduction, only $r$ and $p$ are being summed upon. Thus the expression calculates the total of $A$ for each commodity $c$, in each direction $io$ ('IN' and 'OUT'), summed over all processes and regions.

Another example illustrates the case of nested summations, where index $r$ is enumerated in the inner summation, but is summed upon in the outer summation. Again here, the expression is made unambiguous by observing the positions of the different indexes (for instance, the outer summation is done on the $r$ index)

$$EXPRESSION2_{c,io} = \sum_{r,p,c,io \in top}^{}{B(r)\sum_{p}^{}{A(r,p)}}$$

```{list-table} User input sets in TIMES
:name: user-input-sets
:header-rows: 1

* - Set ID/Indexes[^15]
  - Alias[^16]
  - Description
* - all_r
  - all_reg
  - Set of all regions, internal as well as external; a region is defined as internal by putting it in the internal region set (**r**), regions that are not member of the internal region set are per definition external.
* - c (cg)
  - com, com1, com2, com3
  - User defined list of all commodities in all regions; subset of **cg**.
* - cg
  - com_grp, cg1, cg2, cg3, cg4
  - User defined list of all commodities and commodity groups (see {numref}`cg-activity`) in all regions.
* - clu (p)
  - 
  - Set of cluster technologies in endogenous technology learning.
* - com_desc (r,c)
  - 
  - Commodities by region, only to facilitate different descriptions by region. The elements are pairs **{r,c}**, for which the description is specified according to the GAMS syntax.
* - com_gmap (r,cg,c)
  - 
  - Mapping of commodity **c** to user-defined commodity group **cg,** including itself \[set of triplets {**r,cg,c**} such that commodity c in in group cg in region r\].[^17]
* - com_lim (r,c,lim)
  - 
  - Definition of commodity balance equation type \[set of triplets {**r,c,lim**}such that commodity **c** has a balance of type lim (lim=\'UP\',\'LO\',\'FX\', \'N\') in region r\]; Default: for commodities of type **NRG**, **DM** and **ENV** production is greater or equal consumption, while for **MAT** and **FIN** commodities the balance is a strict equality.
* - com_off (r,c,y1,y2)
  - 
  - Specifying that the commodity **c** in region **r** is not available between the years **y1** and **y2** \[set of quadruplets {**r,c,y1,y2**} such that commodity c is unavailable from years y1 to y1 in region r\] ; note that **y1** may be \'BOH\' for the first year of the first period and **y2** may be \'EOH\' for the last year of the last period.
* - com_peak (r,cg)
  - 
  - Set of pairs {**r,cg**} such that a peaking constraint is to be generated for commodity cg in region r; note that the peaking equation can be generated for a single commodity (**cg** also contains single commodities **c**) or for a group of commodities, e.g. electricity commodities differentiated by voltage level.
* - com_pkts (r,cg,s)
  - 
  - Set of triplets {**r,cg,s**} such that a peaking constraint for a single commodity or a group of commodities **cg** (e.g. if the model differentiates between three electricity commodities: electricity on high, middle and low voltage ) is to be generated for the timeslice **s**; Default: all timeslices of **com_ts**; note that the peaking constraint will be binding only for the timeslice with the highest load.
* - com_tmap (r,com_type,c)
  - 
  - Mapping of commodities to the main commodity types (see **com_type** in Table 1); \[set of triplets {**r,com_type,c**} such that commodity c has type com_type\];
* - com_ts (r,c,s)
  - 
  - Set of triplets {**r,c,s**} such that commodity **c** is available in timeslice **s** in region **r**; commodity balances will be generated for the given timeslices; Default: all timeslices of timeslice level specified by **com_tsl**.
* - com_tsl (r,c,tslvl)
  - 
  - Set of triplets {**r,c,tslvl**} such that commodity **c** is modelled on the timeslice level **tslvl** in region r; Default: \'ANNUAL timeslice level.
* - com_unit (r,c,units_com)
  - 
  - Set of triplets {**r,c,units_com**} such that commodity **c** is expressed in unit **units_com** in region **r**.
* - cur
  - 
  - User defined list of currency units.
* - datayear (year)
  - 
  - Years for which model input data are to be taken; No default.
* - dem_smap (r,dem_sect,c)
  - 
  - Mapping of demands to main demand sectors (see **dem_sect** in {numref}`sets-with-fixed-elements`); \[set of triplets {**r,dem_sect,c**} such that commodity c belongs to sector dem_sect\];
* - env_map (r,env_grp,c)
  - 
  - Mapping of environmental commodities to main types (see **env_grp** in {numref}`sets-with-fixed-elements`); \[set of triplets {**r,env_grp,c**} such that commodity c is of type env_grp\].
* - nrg_tmap (r,nrg_type,c)
  - 
  - Mapping of energy commodities to main types (see **nrg_type** in {numref}`sets-with-fixed-elements`); \[set of triplets {**r,nrg_type,c**} such that commodity c is of type nrg_type\].
* - p
  - prc
  - User defined list of all processes in all regions
* - pastyear (year)
  - pyr
  - Years for which past investments are specified; pastyears usually lie before the beginning of the first period; No default.
* - prc_actunt (r,p,cg,units_act)
  - 
  - Definition of activity \[Set of quadruples such that the commodity group cg is used to define the activity of the process **p**, with units **units_act**, in region **r**\].
* - prc_aoff (r,p,y1,y2)
  - 
  - Set of quadruples {**r,p,y1,y2**} such that process **p** cannot operate (activity is zero) between the years **y1** and **y2** in region r; note that y1 may be \'BOH\' for first year of first period and **y2** may be \'EOH\' for last year of last period.
* - prc_capunt (r,p,cg,units_cap)
  - 
  - Definition of capacity unit of process p \[set of quadruples {**r,p,cg,units_cap**} such that process **p** uses commodity group **cg** and units **units_cap** to define its capacity in region **r**\].
* - prc_desc (r,p)
  - 
  - Processes by region, only to facilitate different descriptions by region. The elements are pairs **{r,p}**, for which the process description is specified according to the GAMS syntax.
* - prc_dscncap (r,p)
  - 
  - Set of processes **p** to be modelled using the lumpy investment formulation in region **r**; Default: empty set. If **p** is not in this set, then any lumpy investment parameters provided for **p** are ignored.
* - prc_foff (r,p,c,s,y1,y2)
  - 
  - Set of sextuples specifying that the flow of commodity **c** at process **p** and timeslice **s** is not available between the years **y1** and **y2** in region r; note that **y1** may be \'BOH\' for first year of first period and **y2** may be \'EOH\' for last year of last period.
* - prc_grp
  - 
  - List of process groups, used mainly for reporting purposes; Predefined list of groups (defined in MAPLIST.DEF) is shown in section 2.2.1.
* - prc_map (r,prc_grp,p)
  - 
  - Grouping of processes into process groups (**prc_grp)** \[set of triplets {**r,prc_grp,p**} such that process p belongs to group **prc_grp** in region **r**\]. Note: used strictly for reporting purposes.
* - prc_noff (r,p,y1,y2)
  - 
  - Set of quadruples {**r,p,y1,y2**} such that new capacity of process **p** cannot be installed between the years **y1** and **y2** in region **r**; note that **y1** may be \'BOH\' for first year of first period and **y2** may be \'EOH\' for last year of last period.
* - prc_nstts (r,p,s)
  - 
  - Set of triplets {**r,p,s**} such that process **p** is a night storage device with charging timeslices **s** in region r; note that for night storage devices the commodity entering and the commodity leaving the storage may be different, as defined via the set **top**.
* - prc_pkaf (all_r,p)
  - 
  - Set of pairs {**all_r,p**} such that the availability factor (**ncap_af)** is to be used as value for the fraction of capacity of process **p** that can contribute to the peaking constraints **(ncap_pkcnt**), in region **r**.
* - prc_pkno (all_r,p)
  - 
  - Set of pairs {**all_r,p**}such that process **p** cannot be used in the peaking constraints in region **r**.
* - prc_rcap (r,p)
  - 
  - Set of pairs {**r,p**}such that early retirements are activated for process **p** in region **r**.
* - prc_ts (all_r,p,s)
  - prc_ts2
  - Set of triplets {**all_r,p,s**} such that process **p** can operate at timeslice **s** in region r; Default: all timeslices on the timeslice level specified by **prc_tsl**.
* - prc_tsl (r,p,tslvl)
  - 
  - Set of triplets {**r,p,tslvl**} such that process **p** can operate at timeslice level **tslvl** in region **r**; Default: \'ANNUAL\' timeslice level.
* - prc_vint (r,p)
  - 
  - Set of processes **p** that are vintaged technologies in region **r**, i.e. technical characteristics are tied to when the capacity was installed, not the current period; Default: process is not vintaged; note that vintaging increases the model size.
* - r (all_reg)
  - reg
  - Set of internal regions; Subset of **all_r**.
* - s
  - all_ts, ts, s2, sl
  - Set of all timeslices (define the sub-annual divisions of a period). Timeslices effectively defined for specific processes and technologies are subsets of this set.
* - t (year)
  - mile stonyr, tt
  - Set of representative years (middle years) for the model periods within the modelling horizon.
* - teg (p)
  - 
  - Set of technologies selected for endogenous technology learning; Subset of set **p;** if **p** not in **teg**, then any ETL investment parameters provided are ignored**.**
* - top (r,p,c,io)
  - 
  - RES topology definition indicating that commodity **c** enters (**io**='IN') or leaves (**io**=\'OUT\') the process **p** \[set of quadruples {**r,p,c,io**} such that process **p** has a flow of commodity **c** with orientation **io** in region **r**\].
* - top_ire (all_reg,com,all_r,c,p)
  - 
  - RES topology definition for trade between regions \[Set of quintuples indicating that commodity **com** from region **all_reg** is traded (exported) via exchange process **p** (where it is imported) into region **all_r** as commodity **c\]**; note: the name of the traded commodity may be different in the two regions. By using **all_reg**=**all_r**, one can also define bi-directional processes within a region, e.g. for modeling transmission lines.
* - ts_group (all_r,tslvl,s)
  - 
  - Set of triplets {**all_r,tslvl,s**} such that timeslice **s** belongs to the timeslice level **tslvl** in region **r**; needed for the definition of the timeslice tree; only default is that the \'ANNUAL\' timeslice belongs to the \'ANNUAL\' timeslice level.
* - ts_map (all_r,s,ts)
  - 
  - Set of triplets {**all_r,s,ts**} such that s is an intermediate node **s** of the timeslice tree (neither \'ANNUAL\' nor the lowest level), and **ts** is a node directly under **s** in region **r**; the set is further extended by allowing **ts** = **s** (see {numref}`inter-external-regions`).
* - ts_off (r,ts,y1,y2)
  - 
  - Set of quadruples {**r,ts,y1,y2**} such that the timeslice branch consisting of the timeslice **ts** and all the timeslices below it will not be taken into account in the model between the years **y1** and **y2** in region **r**; note that **y1** may be \'BOH\' for first year of first period and **y2** may be \'EOH\' for last year of last period. The timeslice **ts** specified in **ts_off** must be directly below ANNUAL in the timeslice tree specified (usually at the SEASON level).
* - uc_attr (r,uc_n,side,uc_grptype,uc_name)
  - 
  - Set of quintuples such that the UC modifier specified by the **uc_name** (e.g., cost, conversion factor, etc.) will be applied to the coefficient for the variable identified by **uc_grptype** in the user constraint **uc_n**, for the side **side** (\'LHS\' or \'RHS\') in region **r**; if **uc_name**=\'GROWTH\' the user constraint represents a growth constraint.
* - uc_n
  - ucn
  - List of user specified unique indicators of the user constraints.
* - uc_dynbnd (uc_n,bd)
  - 
  - List of user constraint names **uc_n** that will be handled as simplified process-wise dynamic bound constraints of type **bd**. Can be used together with UC_ACT, UC_CAP, and UC_NCAP for defining the growth/decay coefficients and RHS constants for the dynamic bounds. See EQ_UCRTP for information on usage.
* - uc_r_each (all_r,uc_n)
  - 
  - Set of pairs {**all_r,uc_n**} such that the user constraint **uc_n** is to be generated for each specified region **all_r**.
* - uc_r_sum (all_r,uc_n)
  - 
  - Set of pairs {**all_r,uc_n**} indicating that the user constraint **uc_n** is summing over all specified regions **all_r** (that is these constraints do not have a region index). Note that depending on the specified regions in **ur_r_sum**, the summation may be done only over a subset of all model regions. For example if the model contains the regions FRA, GER, ESP and one wants to create a user constraint called GHG summing over the regions FRA and GER but not ESP, the set **uc_r_sum** contains has the two entries {\'FRA\', \'GHG\'} and {\'GER\', \'GHG\'}.
* - uc_t_each (r,uc_n,t)
  - 
  - Indicator that the user constraint **uc_n** is to be generated for each specified period **t**.
* - uc_t_succ (r,uc_n,t)
  - 
  - Indicator that the user constraint **uc_n** is to be generated between the two successive periods **t** and **t**+1.
* - uc_t_sum (r,uc_n,t)
  - 
  - Indicator that the user constraint **uc_n** is to be generated summing over the periods **t**.
* - uc_ts_each (r,uc_n,s)
  - 
  - Indicator that the user constraint **uc_n** will be generated for each specified timeslice **s**.
* - uc_ts_sum (r,uc_n,s)
  - 
  - Indicator that the user constraint **uc_n** is to be generated summing over the specified timeslice **s**.
* - uc_tsl (r,uc_n,side,tslvl)
  - 
  - Indicator of the target timeslice level **tslvl** of a timeslice-dynamic (or pseudo-dynamic) user constraint **uc_n**.
* - v
  - modlyear
  - Union of the sets **pastyear** and **t** corresponding to all the years (periods) of a model run (thus actually an internal set).
```

##  Definition of internal sets

The sets internally derived by the TIMES model generator are given in {numref}`internal-sets`. The list of internal sets presented here concentrates on the ones frequently used in the model generator and the ones used in the description of the model equations in Chapter {numref}`%s <equations>`. Some internal sets are omitted from {numref}`internal-sets` as they are strictly auxiliary sets of the preprocessor whose main purpose is the reduction of the computation time for preprocessor operations.

```{list-table} Internal sets in TIMES
:name: internal-sets
:header-rows: 1

* - Set ID[^18] Indexes[^19]
  - Description
* - afs (r,t,p,s,bd)
  - Indicator that the internal parameter COEF_AF, which is used as coefficient of the capacity (new investment variable VAR_NCAP plus past investments NCAP_PASTI) in the capacity utilization constraint EQ(l)\_CAPACT, exists.
* - bohyear (\*)[^20]
  - Set **allyear** plus element \'**BOH**\' (Beginning Of Horizon).
* - dm_year (year)
  - Union of sets **datayear** and **modlyear**
* - eachyear (year)
  - Set of all years between scalars **MINYR** (first year needed for cost calculation in objective function) and **MIYR_VL + DUR_MAX** (estimation of last year possible cost terms may occur).
* - eohyear (\*)
  - Set **allyear** plus element \'**EOH**\' (Ending OF Horizon)
* - eohyears (year)
  - Set of all years between scalars **MINYR** (first year needed for cost calculation in objective function) and **MIYR_VL** (last year of model horizon).
* - finest (r,s)
  - Set of finest timeslices **s** used in region **r**.
* - fs_emis (r,p,cg,c,com)
  - Indicator that the flow variable (VAR_FLO) associated with emission **com** can be replaced by the flow variable of **c** multiplied by the emission factor **FLO_SUM**, which is used in the transformation equation (EQ_PTRANS) between the commodity group **cg** and the commodity **com**; used in the reduction algorithm (see Part III).
* - g_rcur (r,cur)
  - Indicator of main currency **cur** by region **r**. For regions having several discounted currencies, the one having highest present value factors is selected; used for undiscounting the solution marginals.
* - invspred (year,jot,k,y)
  - Set of investment years **y** and commissioning years **k** belonging to the investment spread starting with **year** and having **jot** number of steps (used for investment and fixed cost accounting).
* - invstep (year,jot,y,jot)
  - Set of investment years **y** belonging to the investment spread starting with **year** and having **jot** number of steps (used for investment and fixed cost accounting).
* - miyr_1 (t)
  - First **milestonyr**.
* - no_act (r,p)
  - List of processes **p** in region **r** not requiring the activity variable; used in reduction algorithm
* - no_cap (r,p)
  - List of processes **p** in region **r** not having any capacity related input parameters; used in reduction algorithm.
* - no_rvp (r,v,p)
  - New investment in process **p** in region **r** is not possible in period **v** and previously installed capacity does not exist anymore.
* - obj_1a (r,v,p)
  - Investment case small investment (NCAP_ILED/D(v) \<= G_ILEDNO) and no repetition of investment (NCAP_TLIFE + NCAP_ILED \>= D(v)) for process **p** in region **r** and vintage period **v**.
* - obj_1b (r,v,p)
  - Investment case small investment (NCAP_ILED/D(v) \<= G_ILEDNO) and repetition of investment (NCAP_TLIFE + NCAP_ILED \< D(v)) for process **p** in region **r** and vintage period **v**.
* - obj_2a (r,v,p)
  - Investment case large investment (NCAP_ILED/D(v) \> G_ILEDNO) and no repetition of investment (NCAP_TLIFE + NCAP_ILED \>= D(v)) for process **p** in region **r** and vintage period **v**.
* - obj_2b (r,v,p)
  - Investment case large investment (NCAP_ILED/D(v) \> G_ILEDNO) and repetition of investment (NCAP_TLIFE + NCAP_ILED \< D(v)) for process **p** in region **r** and vintage period **v**.
* - obj_idc (r,v,p,life,k,age)
  - Summation control for calculating the interest during constriction (IDC) for investment Cases 2.a and 2.b.
* - obj_sumii (r,v,p,life,y,jot)
  - Summation control for investment and capacity related taxes and subsidies of the in the annual objective function, with lifetime **life**, spread starting in commissioning year **y**, having **jot** number of steps in the spread, and vintage period **v**.
* - obj_sumiii (r,v,p,ll,k,y)
  - Summation control for decommissioning costs with for the running year index **y** of annual objective function, vintage period **v**, startup-year **ll**, and commissioning year **k** (e.g. for spreading decommissioning costs over decommissioning time).
* - obj_sumiv (r,v,p,life,y,jot)
  - Summation control for fixed costs in the annual objective function with lifetime **life**, spread starting in commissioning year **y**, having **jot** number of steps in the spread, and vintage period **v**.
* - obj_sumivs (r,v,p,k,y)
  - Summation control for decommissioning surveillance costs with running year index **y** of annual objective function, vintage period **v** and commissioning year **k**.
* - obj_sums (r,v,p)
  - Indicator that process **p** in region **r** with vintage period **v** has a salvage value for investments with a (technical) lifetime that extends past the model horizon.
* - obj_sums3 (r,v,p)
  - Indicator that process **p** in region **r** with vintage period **v** has a salvage value associated with the decommissioning or surveillance costs.
* - obj_sumsi (r,v,p,k)
  - Indicator that for commissioning years **k** process **p** in region **r** with vintage period **v** has a salvage value due to investment, decommissioning or surveillance costs arising from the technical lifetime extending past the model horizon.
* - periodyr (v,y)
  - Mapping of individual years **y** to the modlyear (milestonyr or pastyear; **v)** period they belong to; if **v** is a **pastyear**, only the pastyear itself belongs to the period; for the last period of the model horizon also the years until the very end of the model accounting horizon (MIYR_VL + DUR_MAX) are elements of **periodyr**.
* - prc_act (r,p)
  - Indicator that a process **p** in region **r** needs an activity variable (used in reduction algorithm).
* - prc_cap (r,p)
  - Indicator that a process **p** in region **r** needs a capacity variable (used in reduction algorithm).
* - prc_spg (r,p,cg)
  - Shadow primary group (SPG) of a process **p**; all commodities on the opposite process side of the primary commodity group (PCG) which have the same commodity type as the PCG, usually internally determined (though it may be specified by the user under special circumstances (e.g., when not all the commodities on the opposite side of the process, which should be in the SPG, are of the same commodity type **com_type**).
  <br>If no commodity of the same type is found:
  <br>if PCG is of type \'DEM\' and process is a material processing process (PRV or PRW), then the SPG contains all material commodities on the SPG side;
  <br>otherwise the SPG is selected as the first type among the commodity types on the SPG side, in the flowing order:
  <br>When PCG type is DEM: (NRG, MAT, ENV)
  <br>When PCG type is NRG: (MAT, DEM, ENV)
  <br>When PCG type is MAT: (NRG, DEM, ENV)
  <br>When PCG type is ENV: (NRG, MAT, DEM)
* - prc_stgips (r,p,c)
  - Set of triplets {**r,p,c**} such that process **p** is an [i]{.underline}nter-[p]{.underline}eriod [s]{.underline}torage for the commodity **c** in region **r**; the commodity **c** enters and/or leaves the storage according to the set **top**; the storage can only operate at the ANNUAL level.
* - prc_stgtss (r,p,c)
  - Set of triplets {**r,p,c**} such that process **p** is a storage process between timeslices ([e.g., seasonal hydro reservoir, day/night pumped storage]{.underline}) for commodity **c** in region **r**; commodity **c** enters and/or leaves the storage according to set **top**; the storage operates at the timeslice level **prc_tsl**.
* - rc (r,c)
  - List of all commodities **c** found in region **r**.
* - rc_agp (r,c,lim)
  - Indicator of which commodities **c** are aggregated into other commodities by aggregation type **lim**.
* - rc_cumcom (r,com_var,y1,y2,c)
  - Indicator of a cumulative constraint of type **com_var** defined for commodity **c** between years **y1** and **y2**
* - rcj (r,c,j,bd)
  - Steps **j** used in direction **bd** for the elastic demand formulation of commodity **c**.
* - rcs_combal (r,t,c,s,bd)
  - Indicator of which timeslices (**s**) associate with commodity **c** in region **r** for time period **t** the commodity balance equation (EQ(l)\_COMBAL) is to be generated, with a constraint type corresponding to **bd**.
* - rcs_comprd (r,t,c,s,bd)
  - Indicator of which timeslices (**s**) associate with commodity **c** in region **r** for time period **t** the commodity production equation (EQ(l)\_COMBAL) is to be generated, with a constraint type according to **bd,** when a corresponding **rhs_comprd** indicator exists.
* - rcs_comts (r,c,s)
  - All timeslices **s** being at or above timeslice level (**com_tsl**) of commodity **c** in region **r**.
* - rdcur\ (r,cur)
  - List of currencies **cur** that are discounted (G_DRATE provided) in each region **r**.
* - rhs_combal (r,t,c,s)
  - Indicator that the commodity net variable (VAR_COMNET) is required in commodity balance (EQE_COMBAL), owing to bounds/costs imposed on the net amount.
* - rhs_comprd (r,t,c,s)
  - Indicator that the commodity production variable (VAR_COMPRD) is required in commodity balance (EQE_COMPRD), owing to a limit/costs imposed on the production.
* - rp (r,p)
  - List of processes (**p**) in each region (**r**).
* - rp_aire\ (r,p,ie)
  - List of exchange processes (**p**) in each region (**r**) with indicators (**ie**) corresponding to the activity being defined by imports/exports or both.
* - rp_flo (r,p)
  - List of all processes in region (**r)**, except inter-regional exchange processes (**ire**).
* - rp_inout (r,p,io)
  - Indicator as to whether a process (**p**) in a region (**r**) is input or output (io = \'IN\'/\'OUT\') normalized with respect to its activity.
* - rp_ire (all_r,p)
  - List of inter-regional exchange processes (**p**) found in each region (**all_r**).
* - rp_pg (r,p,cg)
  - The primary commodity group (**cg)** of each process (**p)** in a region (**r**).
* - rp_pgtype (r,p,com_type)
  - The commodity type (**com_type**) of primary commodity group of a process (**p**) in a region (**r**).
* - rp_sgs (r,p)
  - List of those standard processes (**p)** in each region (**r)**, which have been defined to have a night storage (NST) capability.
* - rp_std (r,p)
  - List of standard processes (**p**) in each region (**r**).
* - rp_stg (r,p)
  - List of storage processes (**p**) in each region (**r**).
* - rp_sts (r,p)
  - List of generalized timeslice storage processes (**p**) in each region (**r**).
* - rp_upl (r,p,lim)
  - List of those processes (**p**) in each region (**r**) that have dispatching attributes ACT_MINLD/ACT_UPS defined, with qualifier **lim**.
* - rp_ups (r,p,tslvl,lim)
  - Timeslices (**s**) of a process (**p**) in a region (**r**) during which start-ups are permitted (used for processes in the set **rp_upl(r,p,**\'**FX**\'))
* - rpc (r,p,c)
  - List of commodities (**c**) associated with a process **p** in region **r** (by **top** or **top_ire**).
* - rpc_act (r,p,c)
  - Indicator that the primary commodity group of a process (**p**), except exchange processes (see **rpc_aire**) consists of only one commodity (**c**), enabling the corresponding flow variable to be replaced by the activity variable (used in reduction algorithm).
* - rpc_aire (r,p,c)
  - Indicator that the primary commodity group of an exchange process (**p**) consists of only one commodity (**c**), enabling the corresponding flow variable to be replaced by the activity variable (used in reduction algorithm).
* - rpc_capflo (r,v,p,c)
  - Indicator that a commodity flow **c** in region **r** is associated with the capacity of a process (**p**, due to NCAP_ICOM, NCAP_OCOM, or NCAP_COM being provided).
* - rpc_cumflo (r,p,c,y1,y2)
  - Indicator of a cumulative constraint defined for commodity flow **c** of process **p** between years **y1** and **y2**
* - rpc_noflo (r,p,c)
  - A subset of **rpc_capflo** indicating those processes (**p**) in a region (**r**) where a commodity (**c**) is only consumed or produced through capacity based flows, and thus has no flow variable for the commodity.
* - rpc_emis (r,p,cg)
  - Indicator that the flow variable of an emission commodity (**cg**) associated with process (**p**) in a region (**r**) can be replaced by the fuel flow causing the emission multiplied by the emission factor (used in reduction algorithm).
* - rpc_eqire (r,p,c)
  - Indicator of the commodities (**c**) associated with inter-regional exchange processes (**p**) in region (**r**) for which an inter-region exchange equation (EQ_IRE) is to be generated; the set does not contain the marketplace region (**rpc_market**).
* - rpcc_ffunc (r,p,c)
  - Flow variable of a commodity (**c**) associated with a process (**p**) that can be replaced by another flow variable of the process, due to a direct FLO_FUNC or FLO_SUM relationship.
* - rpc_ire (all_r,p,c,ie)
  - Commodities (**c**) imported or exported (**ie=**\'**IMP**\'**/**\'**EXP**\') via process **p** in a region (**all_r**).
* - rpc_market (all_r,p,c,ie)
  - List of market regions (subset of **all_r**) that trade a commodity (**c**) through a process (**p**) either by only multidirectional export links (**ie**=\'EXP\') or by both import and export links (**ie**=\'IMP\'). The market structure is user-defined through the set **top_ire**.
* - rpc_pg (r,p,cg,c)
  - Mapping of the commodities (**c**) in a region (**r**) that belong to the primary commodity group (**cg**) associated with process **p**.
* - rpc_spg (r,p,c)
  - The list of commodities (**c**) in a region (**r**) belonging to the shadow primary group of process (**p**).
* - rpc_stg (r,p,c)
  - List of stored (charged/discharged) commodities (**c**) of storage processes (**p**) in region (**r**).
* - rpc_stgn (r,p,c,io)
  - List of those stored (charged/discharged) commodities (**c**) of storage processes (**p**) in region (**r**), which are connected to the commodity balance on one side (**io**) only.
* - rpcg_ptran (r,p, c1,c2,cg1,cg2)
  - Indicator of the transformation equations (EQ_PTRANS) that can be eliminated by the reduction algorithm.
* - rpcs_var (r,p,c,s)
  - The list of valid timeslices for the flow variable (VAR_FLO) of commodity **c** associated with process **p** in region **r**; flow variables of commodities which are part of the primary commodity group have the timeslice resolution of the process (**prc_tsl**), while all other flow variables are created according to the **rps_s1** timeslices.
* - rps_prcts (r,p,s)
  - All (permitted) timeslices (**s**) at or above the process (**p**) timeslice level (**prc_tsl**) in a region (**r**).
* - rps_s1 (r,p,s)
  - All (permitted) timeslices (**s**) belonging to the finest timeslice level of the process (**p, prc_tsl**) and the commodity timeslice level (**com_tsl**) of the shadow primary commodity group.
* - rps_s2 (r,p,s)
  - For an ANNUAL level NST process, contains all permitted timeslices (**s**) at the level above the finest commodity timeslice levels (**com_tsl**) of the shadow primary group (spg). For all other processes, rps_s2 = rps_s1.
* - rps_stg (r,p,s)
  - Process level timeslices (**s**) of timeslice storage process (**p**) in a region (**r**).
* - rreg (all_reg,all_r)
  - Indicator that trade exists from region **all_reg** to region **all_r**.
* - rs_below (all_r,ts,s)
  - All timeslices (**s**) strictly below the higher timeslice (**ts**) in the timeslice tree.
* - rs_below1 (all_r,ts,s)
  - All timeslices (**s**) immediately (one level) below the higher timeslice (**ts**) in the timeslice tree.
* - rs_tree (all_r,ts,s)
  - For a timeslice (**ts**) all timeslices (**s**) that are on the same paths within the timeslice tree, e.g. if **ts**=SP_WD in Fig. 6, valid timeslices **s** are: ANNUAL, SP, SP_WD, SP_WD_D, SP_WD_N
* - rtc_cumnet (r,t,c)
  - Indicator that the commodity net variable (VAR_COMNET) for commodity **c** in region **r** for period **t** has a cumulative bound applied.
* - rtc_cumprd (r,t,c)
  - Indicator that the commodity production variable (VAR_COMPRD) for commodity **c** in region **r** for period **t** has a cumulative bound applied.
* - rtcs_sing (r,t,c,s,io)
  - Indicator that a commodity **c** is not available in a specific period **t** and timeslice **s**, since the all the processes producing (**io**=\'OUT\') or consuming it (**io**=\'IN\') are turned-off. In the case of **io**=\'OUT\', the commodity is not available, meaning that processes having only this commodity as input cannot operate. Similar reasoning applies to the case **io**=\'IN\'.
* - rtcs_varc (r,t,c,s)
  - For commodity (**c**) in region (**r**) indicator for the timeslices (**s**) and the periods (**t**) the commodity is available.
* - rtp = rvp (r,v,p)
  - Indication of the periods and pastyears for which process (**p**) in region (**r**) is available; all other RTP\_\* control sets are based on this set.
* - rtp_cptyr (r,v,t,p)
  - For each vintage period (**v**) an indication of the periods (**t**) for which newly installed capacity of process (**p**) in a region (**r**) is available, taking into account construction lead-time (**NCAP_ILED**) and technical lifetime (**NCAP_TLIFE**).
* - rtp_off (r,t,p)
  - Indication of the periods (**t**) in which no new investment is permitted for a process (**p**) in a region (**r**).
* - rtp_vara (r,t,p)
  - Indication of the periods (**t**) for which a process (**p**) in a region (**r**) is available.
* - rtp_varp (r,t,p)
  - Indicator that the capacity variable (**VAR_CAP**) will be generated for process (**p**) in a region (**r**) in period (**t**).
* - rtp_vintyr (r,v,t,p)
  - An indication of for which periods (**t**) a process (**p**) in a region (**r**) is available since it was first installed (**v**); for vintaged processes (**prc_vint**) identical to **rtp_cptyr**, for non-vintaged processes the **v** index in the **rtp_cptyr** entries is ignored by setting it to **t** (**v** = **t**).
* - rtpc (r,t,p,c)
  - For a process (**p**) in a region (**r**) the combination of the periods it is available (**rtp**) and commodities associated with it (**rpc**).
* - rtps_off (r,t,p,s)
  - An indication for process (**p**) of the timeslices (**s**) for which the process is turned-off (used in reduction algorithm).
* - rtpcs_varf (r,t,p,c,s)
  - The list of valid timeslices (**s**) and periods (**t**) for the flow variable (VAR_FLO) of process (**p**) and commodity (**c**); taking into account the availability of the activity, capacity and flow (**rtp_vara**, **rpcs_var** and **prc_foff**). The timeslice level of a flow variable equals the process timeslice level (**prc_tsl**) when the flow is part of the primary commodity group of the process. Otherwise the timeslice level of a flow variable is set to the finest level of the commodities in the shadow group (SPG) or the process level, whichever is finer.
* - uc_dyndir (r,uc_n,side)
  - If **side** = \'RHS\', indicator for growth constraints to be generated between the periods **t--1** and **t**; if **side** = \'LHS\', the set is ignored.
* - uc_gmap_c (r,uc_n,uc_grptype,c)
  - Indicator that a commodity variable (VAR_COMCON or VAR_COMPRD) for commodity (**c**) in a region (**r**) appears in a user constraint (**uc_n**).
* - uc_gmap_p (r,uc_n,uc_grptype,p)
  - Indicator that a variable (VAR_ACT, VAR_NCAP or VAR_CAP) associated with a process (**p**) in a region (**r**) appears in a user constraint (**uc_n**).
* - uc_gmap_u (r,uc_n,ucn)
  - Indicator that a variable (VAR_UCRT) associated with a user constraint (**ucn**) in a region (**r**) appears in another user constraint (**uc_n**).
* - uc_map_flo (uc_n,r,p,c)
  - Indicator that the flow variable (VAR_FLO) for region **r**, process **p** and commodity **c** is involved in user constraint **uc_n**.
* - uc_map_ire (uc_n,r,p,c)
  - Indicator that an import/export (according to **top_ire**) trade variable (VAR_IRE) for region **r**, process **p**, and commodity **c** is involved in a user constraint (**uc_n**).
* - v
  - Union of the input sets **pastyear** and **t**, corresponding to all the periods of a model run (=modlyear). 
```


[^2]: The meaning and the role of internal and external regions is discussed in Section 2.2.

[^3]: See Section for a more in-depth treatment of commodity groups.

[^4]: This column contains the names of the indexes as used in this document.

[^5]: For programming reasons, alternative names (aliases) may exist for some indexes. This information is only relevant for those users who are interested in gaining an understanding of the underlying GAMS code.

[^6]: This column refers to possible related indexes, e.g. the index set **c** is a subset of the index set **cg**.

[^7]: VEDA/ANSWER compiles the complete list from the union of the commodities defined in each region.

[^8]: VEDA/ANSWER compiles the complete list from the union of the commodity groups defined in each region.

[^9]: VEDA/ANSWER compiles the complete list from the union of processes defined in each region.

[^10]: Important cases are the process type CHP, which activates the CHP attributes, storage process indicators (STG, STS, STK, NST), and material conversion process types PRW and PRV, which may affect the creation of the internal set **prc_spg** (see ).

[^11]: In this case the model may still decide to add additional new capacity, if this is economical and not inhibited by any investment bounds.

[^12]: The purpose of this table is to list those parameters whose year values are independent of the input **datayear**s associated with most of the regular parameters, and therefore need not be included in the set **datayear**. For example, a value for MULTI(j,\'2012\') would not require including 2012 in **datayear**s if 2012 were not relevant to the other input parameters.

[^13]: By setting G_YRFR(r,s)=0 one can exclude any individual timeslices from specific regions, even if only a global timeslice tree is defined for all regions (as it is the case when using VEDA-FE). In this way each region can employ a different subset of the global tree.

[^14]: Note however that some flexibility is lost when using multilateral trade. For instance, it is not possible to express transportation costs in a fully accurate manner, if such cost depends upon the precise pair of trading regions in a specific way.

[^15]: The first row contains the set name. If the set is a one-dimensional subset of another set, the second row contains the parent set in brackets. If the set is a multi-dimensional set, the second row contains the index domain in brackets.

[^16]: For programming reasons, alternative names (aliases) may exist for some indexes. This information is only relevant for those users who are interested in gaining an understanding of the underlying GAMS code.

[^17]: For multidimensional sets such as this one, two definitions are sometimes given, one as an indicator function or mapping, the other (in square brackets) as a set of n-tuples.

[^18]: Name of the internal set as used in this documentation and the GAMS code.

[^19]: Index domain of the internal set is given in brackets (Note: the symbols **y**, **y1**, **y2**, **k**, and **ll** all refer to **year**).

[^20]: The asterisk denotes in the modeling system GAMS a wildcard, so that domain checking is disabled and any index may be used.
