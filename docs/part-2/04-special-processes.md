# Usage notes on special types of processes

## Combined heat and power

### Overview

Cogeneration power plants or combined heat and power plants (CHP) are plants that consume one or more commodities and produce two commodities, electricity and heat. One can distinguish two different types of cogeneration power plants according to the flexibility of the outputs, a back-pressure turbine process and a pass-out turbine process.

Back-pressure turbines are systems where the ratio of heat production to electricity production is fixed, and the electricity generation is therefore directly proportional to the heat generation. Pass-out turbines are systems where the ratio of heat production to electricity production is flexible, usually having a minimum value of zero and a maximum value usually in the range of 0.8-3 (but can be even smaller or larger).

However, both types of CHP systems often additionally support so-called reduction operation, where the turbine can be by-passed, whereby all the steam is directed to a heat exchanger for producing heat. As a result, in a back-pressure turbine system, the ratio of heat production to
electricity production may in such systems vary from the fixed value to infinity, and in a pass-out turbine system it may vary from zero to infinity.

All these different cases are illustrated in {numref}`chp-characteristics` below, which shows the relations between heat and electricity production in different modes of a flexible CHP system, of which the back-pressure turbine system is a special case. Taking into account that thermal power plants usually have a minimum stable operation level, the operating area of the fixed back-pressure turbine system is represented by the line E--F in the Figure. The corresponding operating area of a pass-out turbine system (without reduction operation) is represented by the polygon A--B--F--E. In some cases the turbine characteristics require a minimum level of heat production in proportion to electricity, and with such a constraint the feasible operating area is reduced to C--D--F--E. Finally, with a reduction operation the feasible operating area is expanded to the polygon C--D--F--H--G--E in the Figure. Similarly, the operating area of a back-pressure turbine system with a reduction operation capability would be expanded to E--F--H--G.

Denoting the electrical efficiency in the full condensing mode (point B) by $η_B$, the total efficiency in the full CHP mode (point F) by $η_F$, the heat-to-power ratio (inverse slope of line E--F) by $R$, and the slope of the iso-fuel line (B--F) by $S$, we can easily write the relations between these as follows:

$${\eta_{B} = \frac{\eta_{F} \times (1 + R \times S)}{(1 + R)}
}$$
$${\eta_{F} = \frac{\eta_{B} \times (1 + R)}{1 + R \times S}
}$$
$${S = \frac{\eta_{B} \times (1 + R) - \eta_{F}}{\eta_{F} \times R}}$$

The core TIMES parameters for modeling the CHP attributes are listed in {numref}`core-chp-parameters`.

:::{table} Core TIMES parameters related to the modelling of CHP processes.
:name: core-chp-parameters

| Attribute name      | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| ACT_EFF             | Efficiency: amount of activity produced by 1 unit of input flow |
| ACT_MINLD           | Minimum stable level of operation                               |
| NCAP_CHPR           | Heat-to-power ratio \*                                          |
| NCAP_CEH            | Coefficient of electricity to heat \*                           |
| NCAP_CDME           | Efficiency in full condensing mode                              |
| NCAP_BPME           | Efficiency in back-pressure mode (full CHP mode) \*             |
| NCAP_AFA / NCAP_AFC | Bound on the annual utilization factor                          |

:::

\* Only taken into account for processes defined to be of type CHP with the set .     

  : Table 18: Alternative ways of modelling efficiencies of CHP processes.

```{figure} assets/image11.png
:name: cph-characteristics
:align: center
Illustration of basic CHP characteristics supported in TIMES.
```

### Defining CHP attributes in TIMES
#### Back-pressure turbine systems

For modelling a fixed back-pressure turbine system in TIMES, the following approach is recommended:
- Define the PCG of the process to consist of both the electricity and heat output commodities (using the set $prc\_actunt$);
- Define the process type to be CHP (using the set $prc\_map$);
- Use the electrical output as the basis of the process activity, and choose the capacity unit accordingly (using the parameter $PRC\_CAPACT$).
- Define the process electrical efficiency (by using the parameter $ACT\_EFF$);
- Define the process cost parameters accordingly; for example, specify the investment and fixed O&M costs per electrical capacity;
- Define the fixed heat-to-power ratio (using the parameter $NCAP\_CHPR$);
- Optionally, define also a maximum annual utilization factor considering the typical optimal sizing of CHP plants in proportion to the heat demand in the heat network represented (using the parameter $NCAP\_AFA$);
- Optionally, define a minimum stable operation level (using $ACT\_MINLD$).

All the input data specifications mentioned above should be quite straightforward. Note that the $NCAP\_CEH$ parameter is not needed at all in the fixed turbine case.

For back-pressure turbine technologies that have a reduction operation capability, one can enable the reduction option by adding to the process a third output of a dummy commodity, which is of type NRG and has a limit type \'N\', and is also a member of the PCG. The model generator will automatically assign such a dummy output to the reduction operation, and will adjust the process transformation equation accordingly.

#### Pass-out turbine systems

For modelling a flexible pass-out turbine system in TIMES, the following approach is recommended (but see additional remarks below):

- Define the PCG of the process to consist of both the electricity and heat output commodities (using the set $prc\_actunt$);
- Define the process type to be CHP (using the set $prc\_map$);
- Use the maximum electrical output as the basis of the process activity, and choose the capacity unit accordingly (using the parameter $PRC\_CAPACT$). [^35]
- Define the process electrical efficiency according to the maximum electrical efficiency (at point D in {numref}`cph-characteristics`), by using the parameter $ACT\_EFF$;
- Define the process cost parameters accordingly, for example, specify the investment and fixed O&M costs per unit of electrical capacity;
- Define the maximum heat-to-power ratio (excluding any reduction operation), and optionally also the minimum heat-to-power ratio (using the parameter $NCAP\_CHPR$);
- Define the slope $S$ of the iso-fuel line (the line B--F in {numref}`chp-characteristics`) by specifying $NCAP\_CEH=S$ (where $-1< S< 0$, as in {numref}`chp-characteristics`);
- Optionally, define also a maximum annual utilization factor considering the typical optimal sizing of CHP plants in the heat network represented (using the parameter $NCAP\_AFA$ and/or $NCAP\_AFC$);
- Optionally, define a minimum stable operation level (using $ACT\_MINLD$).

Again, the specifications should be quite straightforward. The slope $S$ of the iso-fuel line represents the amount of electricity lost per heat gained. In the example of {numref}`chp-characteristics`, the inverse of the slope has the value 7 and so one would define $NCAP\_CEH = -1/7$.

Alternatively, if it would seem more convenient to define both the condensing mode efficiency and the full CHP efficiency, that can be done by using the parameters $NCAP\_CDME$ (condensing mode efficiency) and $NCAP\_BPME$ (back-pressure mode efficiency). When these two parameters are used, the $NCAP\_CEH$ and $ACT\_EFF$ parameters should then not be used at all. The activity will in this alternative approach always represent the electricity output in condensing mode.

For pass-out turbine technologies that have a reduction operation capability, one can enable the reduction option by adding to the process a third output of a dummy commodity, which is of type NRG and has a limit type \'N\', and is also a member of the PCG. The model generator will automatically assign such a dummy output to the reduction operation, and will adjust the process transformation equation accordingly.

#### Alternative choices for defining the activity basis

As indicated above, the recommended basis of the activity of a CHP technology is the maximum electricity output, because the available technology data is usually best suited for using the electricity output as the basis for the activity. However, also the total energy output in full CHP mode can be used as the basis for the activity, should that be a more convenient way of defining the process data.

The table below summarizes the different options modelling CHP processes according to the choice of the main efficiency parameters. Note that the cases with $-1<CEH≤0$ and $0≤CEH<1$ are identical when there is no lower bound for $NCAP\_CHPR$ specified, apart from the handling of emission factors defined using the \'ACT\' placeholder in $FLO\_EMIS$.

+-------------+-------------+-------------+-------------+------------+
| **Chara     | **Choices   |             |             |            |
| cteristic** | of          |             |             |            |
|             | parameters  |             |             |            |
|             | for         |             |             |            |
|             | modelling   |             |             |            |
|             | CHP         |             |             |            |
|             | eff         |             |             |            |
|             | iciencies** |             |             |            |
+=============+=============+=============+=============+============+
| Efficiency  | ACT_EFF +   |             |             | NCAP_CDME+ |
| parameters  | NCAP_CEH    |             |             |            |
|             |             |             |             | NCAP_BPME  |
+-------------+-------------+-------------+-------------+------------+
| Value of    | --1\<CEH≤0  | 0≤CEH\<1    | CEH ≥ 1     | None       |
| CEH         |             |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| Inte        | Decrease in | Loss in     | Loss in     | None       |
| rpretation\ | electricity | electricity | heat output |            |
| of CEH      | output per  | output per  | per unit of |            |
|             | unit of     | unit of     | electricity |            |
|             | heat gained | heat gained | gained      |            |
|             | (when       | (when       |             |            |
|             | moving      | moving      | (when       |            |
|             | towards     | towards     | moving      |            |
|             | full CHP    | full CHP    | towards     |            |
|             | mode)       | mode)       | con­densing  |            |
|             |             |             | mode)       |            |
+-------------+-------------+-------------+-------------+------------+
| Activity    | Max.        | Electricity | Total       | E          |
|             | electricity | output in   | energy      | lectricity |
|             | output      | full        | output in   | output in  |
|             |             | condensing  | full CHP    | condensing |
|             |             | mode        | mode        | mode       |
+-------------+-------------+-------------+-------------+------------+
| Capacity    | Electrical  | Electrical  | Elec        | Electrical |
|             | capacity    | capacity    | trical+heat | capacity   |
|             |             |             | capacity    |            |
+-------------+-------------+-------------+-------------+------------+
| Efficiency  | Max.        | Electrical  | Total       | Electrical |
| sp          | electrical  | efficiency  | efficiency  | efficiency |
| ecification | efficiency  | in full     | in full CHP | in         |
|             | (=ACT_EFF)\ | condensing  | mode        | condensing |
|             | + the CEH   | mode        |             | mode +     |
|             | sp          | (=ACT_EFF)\ | (=ACT_EFF)\ | total      |
|             | ecification | + the CEH   | + the CEH   | efficiency |
|             |             | sp          | sp          | in full    |
|             |             | ecification | ecification | CHP mode   |
+-------------+-------------+-------------+-------------+------------+
| Investment  | Per         | Per         | Per         | Per        |
| & fixed O&M | electrical  | electrical  | elec        | electrical |
| costs       | capacity    | capacity    | trical+heat | capacity   |
|             |             |             | capacity    |            |
+-------------+-------------+-------------+-------------+------------+
| Variable    | Per         | Per         | Per         | Per        |
| costs       | activity    | activity    | activity    | activity   |
|             | (see above) | (see above) | (see above) | (see       |
|             |             |             |             | above)     |
+-------------+-------------+-------------+-------------+------------+
| Emission    | Applied     | Applied to  | Applied to  | Applied to |
| factors     | directly to | the PCG     | the PCG     | the PCG    |
| defined per | the         | flows       | flows       | flows      |
| \'ACT\'     | activity    |             |             |            |
|             | levels      |             |             |            |
+-------------+-------------+-------------+-------------+------------+

: Table 19: Specific TIMES parameters related to the modelling of trade processes.

## Inter-regional exchange processes 

### Structure and types of endogenous trade

In TIMES, the inter-regional trading structure of a given commodity basically consists of one or several exchange processes (called IRE processes), each of which defines a portion of the trading network for the commodity. The individual sub-networks can be linked together through common intermediating regions. As an example, electricity trade can be conveniently described by bi-lateral exchange processes (see {numref}`bilateral-trade`). But bi-lateral trading between all pairs of regions may become onerous in terms of data and model size. It is therefore useful to consider the other trade structure of TIMES, called multi-lateral trade, where regions trade with a common market ({numref}`trading-subnetwork-exchange`). For either structure, the topology of the trading possibilities are all defined via the set $top\_ire$ of quintuples $\{r1,c1,r2,c2,p\}$, where $r1$, $r2$ are the exporting and importing regions respectively; $c1$, $c2$ are the names of the traded commodity in regions $r1$ and $r2$ respectively; and $p$ is the process identifier. Process $p$ is a process in both regions. It has to be defined only once, but one can add parameters to it in both regions (e.g. costs, bounds, etc.). Nearly every piece of data in TIMES has to be assigned to a region.

```{figure} assets/image12.png
:name: trading-subnetwork-exchange
:align: center
General structure of the pair-wise specification of the trading sub-network allowed in TIMES for a single exchange process.
```

TIMES provides considerable flexibility in the definition of trading structures. Each sub-network defined for a single exchange process can have the general structure shown in {numref}`trading-subnetwork-exchange`. A trading structure that involves both several supply (export) regions and several demand (import) regions cannot be defined without introducing an intermediating \'market\' region ($R_M$). Whenever such an intermediate region is defined between (at least) two different regions, the model generator will assume that the structure is actually meant to ignore the intermediate node-region shown in {numref}`trading-subnetwork-exchange`, by generating a single trade balance equation directly between all the export and all the import flows. If the intermediate step should nonetheless be included, for example, to reflect a physical market hub in the region $R_M$, this can be accomplished by dividing the sub-network into two parts, by using two exchange processes. Consequently, depending on the user\'s choice, the trading relationships shown in {numref}`trading-subnetwork-exchange` can be modeled both with and without the intermediate transportation step through the market region.

The general structure allowed for the trading sub-networks can be further divided into four cases, which will be discussed below in more detail:
- Case 1: Bi-lateral trading.
- Case 2: Unidirectional trade from some export regions into a single importing region
- Case 3: Multi-directional trade from a single export region to several importing regions
- Case 4: General multi-lateral trading structure

```{figure} assets/image13.png
:name: bilateral-trade
:align: center
Case 1: Bi-lateral trade (both R_1 and R_2 qualify as R_M).
```

<ins>Trading without need for explicit marketplace definition:</ins>

Cases 1, 2 and 3 fall in this category. Bi-lateral trade takes place between pairs of regions. An ordered pair of regions together with an exchange process is first identified, and the trade through the exchange process is balanced between these two regions. Whatever amount is exported from region $i$ to region $j$ is imported by region $j$ from region $i$ (possibly with an adjustment for transportation losses). The basic structure is shown in {numref}`bilateral-trade`. Bi-lateral trading can be fully described in TIMES by specifying the two pair-wise connections in $top\_ire$. The capacity and investment costs of the exchange process can be described individually for both regions. For Cases 2 and 3, the general structure of the trade relationships is shown in {numref}`case2-case3-trade`. Also in these cases the definition of the trading structure is easy, because the relationships can be unambiguously described by pair-wise $top\_ire$ specifications between two regions.

<ins>Trading based on marketplace:</ins>

Case 4 is covered by the generic structure shown in {numref}`trading-subnetwork-exchange`. Trading occurs in this case between at least three regions, and involves both several exporting regions and several importing regions. In this type of trade, the commodity is 'put on the market' by each region participating in the supply side of the market and may be bought by any region participating in the demand side of the market. This case is convenient for global commodities such as emission permits or crude oil where the transportation cost from $R_i$ to $R_j$ may be approximated by $Cost_i+Cost_j$ (rather than a more accurate cost such as $C_{ij}$). When the exact cost (or losses) are strictly dependent on the pair $i$,$j$ of trading regions, it may be more accurate to use bilateral trade.

In general, there are many different possibilities for defining the multi-lateral structure by using the pair-wise $top\_ire$ specifications. In order to comply with the structure allowed in TIMES, the user has to decide which of the regions represents the \'marketplace\', i.e. is chosen to be the $R_M$ shown in {numref}`trading-subnetwork-exchange`. Note that the market region will participate both in the supply and demand side of the market. The TIMES model generator automatically identifies this general type of trading on the basis of the $top\_ire$ topology defined by the user. Therefore, the user only needs to define the possible trading relationships between regions into the set $top\_ire$. If there are $n$ supply regions and $m$ demand regions, the total number of entries needed in $top\_ire$ for defining all the trade possibilities is $n+m-2$ (counting the market region to be included in both the supply and demand regions. Although the market region has to be defined to be an intermediate node in the structure, the model generator will actually <ins>not</ins> introduce any intermediate step between the export and import regions.

The timeslice levels of the traded commodity may be different in each region (as well as the commodity name). However, some appropriate common timeslice level must be chosen for writing the market balance equation. *That common level is the level attached to the exchange process in the market region*. In all other respects, ***the market region is not treated in any way differently*** from the other regions participating in the market. Nevertheless, the user can of course provide different data for the different regions, for example investment costs or efficiencies for the exchange process can be differentiated by region.

```{figure} assets/image14.png
:name: case2-case3-trade
:align: center
General structure of unidirectional trade into a single import region (Case 2, left) and multidirectional trade from a single export region (Case 3, right)
```

If the sets of supply and demand regions participating in the market should actually be disjoint, even in that case the user has to choose one of the regions to be used as the intermediate market region. The imports to or exports from the market region can then be switched off by using an $IRE\_XBND$ parameter, if that is considered necessary.

<ins>Remarks on flexibility</ins>
1. Any number of exchange processes can be defined for describing the total trade relationships of a single commodity (but see warning 1 below).
2. The names of traded commodities can be different in each region participating in the trade. In addition, also the import and export names of the traded commodities can be different (but see warning 2 below). This could be useful e.g. in the case of electricity, for which it is common to assume that the export commodity is taken from the system after grid transport, while the import commodity is introduced into the system before the grid.
3. Any number of commodities can be, in general imported to a region or exported from a region through the same process (but see warning 2 below).

<ins>Warnings</ins>
1. For each exchange process of any traded commodity, the total structure of the trading sub-network, as defined in $top\_ire$, must comply with one of the basic structures supported by TIMES (Cases 1--4). If, for example, several bi-lateral trading relationships are defined for the same commodity, they should, of course, not be defined under the same process, but each under a different process.
2. If the export and import names for a market-based commodity ($c$) are different in the market region, no other commodities should be imported to the market region through the same exchange process as commodity $c$.
3. The model generator combines the trading relationships of a single process into a single market whenever there is an intermediate region between two different regions. If, however, the intermediate exchange step should be explicitly included in the model, the trading sub-network should be divided between two different exchange processes.

<ins>Example</ins>

Assume that we want to set up a market-based trading where the commodity CRUD can be exported by regions A, B, C, and D, and that it can be imported by regions C, D, E and F. First, the exchange process and marketplace should be defined. For example, we may choose (C,XP,CRUD) as the marketplace, where XP has been chosen to be the name of the exchange process (recall that process XP is declared only once but exists in all trading regions, possibly with different parameters). The trade possibilities can then be defined simply by the following six $top\_ire$ entries:

```
SET PRC / XP /;

SET TOP_IRE /
'A'.'CRUD'.'C'.'CRUD'.'XP'
'B'.'CRUD'.'C'.'CRUD'.'XP'
'D'.'CRUD'.'C'.'CRUD'.'XP'
'C'.'CRUD'.'D'.'CRUD'.'XP'
'C'.'CRUD'.'E'.'CRUD'.'XP'
'C'.'CRUD'.'F'.'CRUD'.'XP'
/;
```

To complete the RES definition needed for the exchange process, in addition only the set $prc\_actunt(r,p,c,u)$ needs be defined for the exchange process XP:

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

These definitions are sufficient for setting up of the market-based trade. Additionally, the user can, of course, specify various other data for the exchange processes, for example investment and distribution costs, efficiencies and bounds.

### Input sets and parameters specific to trade processes

TIMES input SETs that have a special role in trade processes are the following:
- $top\_ire(r1,c1,r2,c2,p)$: For bi-lateral trade, unidirectional trade into a single destination region, and multidirectional trade from a single source region, $top\_ire$ should contain the corresponding entries from the exporting region(s) $r1$ to the importing region(s) $r2$. <br>For market-based trade, $top\_ire$ must contain entries for each exporting region to the intermediate market region, and from the market region to each importing region. Each region may be both exporting and importing. One may thus force even a bi-lateral exchange to be modeled as market-based trade, by introducing an additional $top\_ire$ entry within the desired market region between the exported and imported commodity. Instead of two trade balance equations, only one market balance equation is then generated.
- $prc\_aoff(r,p,y1,y2)$: Override used to control in what years (not periods) a process is unavailable. This set is not specifically related to exchange processes. However, in the case of market-based trading it can be used to switch off the entire commodity market for periods that fall within the range of years given by $prc\_aoff$. The market will be closed for all commodities exchanged through the process ($p$). If trading should be possible only between certain years, even multiple entries of $prc\_aoff$ can be specified.

All the $top\_ire$ specifications are handled for the user by the user shell (VEDA/ANSWER) according to the characterization of the trade processes.

*<ins>Additional remarks:</ins>*
1. Commodity type can be used as the primary group of IRE processes. All commodities of that type, traded through the process, will then be included in the PCG.
2. Topology entries are automatically created on the basis of $IRE\_FLOSUM$ and $FLO\_EMIS$ defined for IRE processes (the latter only for ENV commodities).
3. In any non-bilateral trade, the marketplaces are automatically set by the model generator for any trade that involves an intermediate region between two different regions for the same exchange process ($p$) and same commodity ($c$), or if there are multiple destination (importing) regions for the same exporting region.
4. In market-based trade with **r** as the market region, the import/export regions participating in the market consist of all those regions that import/export commodity $c$ from/into region $r$ through process $p$ (as defined in $top\_ire$). The market region **r** by itself always participates in the market both as an importing and exporting region. However, the imports/exports of commodity ($c$) to/from the market region ($r$) can be switched off by using an $IRE\_XBND$ parameter, if necessary.

**<ins>Input parameters</ins>**

Input parameters specific to inter-regional exchange processes are listed in Table 19.

| Attribute name (indexes)               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| $IRE\_FLO$ $(r1,y,p,c1,r2,c2,s2)$      | Coefficient that represents the efficiency of exchange from $r1$ to $r2$, inside an inter-regional process where both regions are internal. Note that separate $IRE\_FLO$ are required for import and export. Default =1 for each $top\_ire$ direction specified. Timeslice $s2$ refers to the region where the commodity arrives. Units: none                                                                                                                                                                           |
| $IRE\|_FLOSUM$ $(r,y,p,c1,s,ie,c2,io)$ | Special attribute to represent auxiliary consumption ($io='IN'$), or production/emission ($io='OUT'$) of commodity $c2$ due to the import / export (index $ie$) of the commodity $c1$ in region $r$ by an inter-regional process $p$[^36]. It is a fixed $FLO\_SUM$ with (one of) the pcg in that region. These relate commodities on the same side of the process. Auxiliary flows can also be specified on the process activity, by setting $c1='ACT'$ in the $IRE\_FLOSUM$ parameter (or in a $FLO\_EMIS$ parameter). |
| $IRE\_BND$ $(r1,y,c,s,r2,ie,bd)$       | Bound on the total import/export (index $ie$) into/from internal region $r1$, from/to region $r2$, where region $r2$ may be internal or external^37; $c$ is the name of commodity in region $r1$. Default none.                                                                                                                                                                                                                                                                                                          |
| $IRE\_XBND$ $(r,y,c,s,ie,bd)$          | Bound on total imports/exports of commodity $c$ in region $r$, to/from all destinations/sources, where $r$ may be an internal or external region. (Default value: none)                                                                                                                                                                                                                                                                                                                                                  |
| $IRE\_CCVT$ $(r1,c1,r2,c2)$            | Conversion factor between commodity units, from unit of $c1$ in region $r1$ to unit of $c2$ in region $r2$, as part of inter-regional exchanges. Default = 1, when exchange permitted. Units: none.                                                                                                                                                                                                                                                                                                                      |
| $IRE\_TSCVT$ $(r1,s1,r2,s2)$           | A matrix that transforms timeslices of region $r1$ to region $r2$ as part of inter-regional exchanges, including both internal and external. Default value = 1 when exchange permitted. Units: none.                                                                                                                                                                                                                                                                                                                     |

  : Table 20: Limitations of using standard process parameters for IRE processes.

*<ins>Remarks:</ins>*
1. In market-based trading the $IRE\_FLO$ parameter is taken into account on the export side only (representing the efficiency from the export region to the common marketplace). By using this convention, any bi-lateral exchange can be represented by a fully equivalent market-based exchange simply by choosing one of the two regions to be the marketplace, and adding the corresponding entry to the set $rpc\_market(r,p,c)$. The efficiency of the exports from the market region itself to the marketplace should also be specified with an IRE_FLO parameter, when necessary ($r1=r2=$ market region).
2. If the user wants to specify efficiency on the import side of a market-based exchange, this can be done by using an $IRE\_FLOSUM$ parameter on the import side.
3. Similarly to any other pair of regions, the total amount of commodity imported to a region from the commodity market can be constrained by the $IRE\_BND$ parameter, by specifying the market region as the export region. Correspondingly, the total amount of commodity exported from a supply region to the marketplace can be constrained by the $IRE\_BND$ parameter by specifying the market region as the import region.

### Availability factors for trade processes

In TIMES, capacity by default bounds only the activity. However, with the $NCAP\_AFC$ / $NCAP\_AFCS$ attributes, one can bound the import / export flows instead. Capacity then also refers to the nominal maximum import (or export) capacity, e.g. the capacity of a transmission line in either direction. One can thus simultaneously bound the import and export flows by the same capacity but with different availabilities, which can be useful with bi-directional exchange links with different availabilities in the import/export direction. All these availability factors can be defined either on a desired timeslice level ($NCAP\_AFC$), or on individual timeslices ($NCAP\_AFCS$).

The rules for defining the availabilities for trade flows can be summarized as follows:
- If the import/export commodities are different ($c1$/$c2$): Use $NCAP\_AFC(c1)$ for bounding the import flow and $NCAP\_AFC(c2)$ for bounding the export flow, or use $NCAP\_AFC('NRG')$ for applying the same availability to both flows.
- If $input=output=c$, specifying ***either*** $NCAP\_AFC(c)$ ***or*** $NCAP\_AFC('NRG')$ alone applies to both imports and exports (unless the process type is DISTR, see Section 4.2.4 below). However, if they are both specified, then $NCAP\_AFC(c)$ applies to the import flow while $NCAP\_AFC('NRG')$ applies to the export flow.

*<ins>Remarks:</ins>*
1. As any process has only a single capacity variable, the availabilities specified for the import/export flows are always proportional to the same overall capacity.
2. Note that the availability factors defined by $NCAP\_AFC$ are multiplied by any $NCAP\_AF$/$NCAP\_AFS$/$NCAP\_AFA$ value if defined for the same timeslice.

### Notes on other attributes for trade processes

There are important limitations of using the parameters for standard processes for IRE processes. The most important limitations are summarized Table 20 with regard to the parameters with the prefixes $ACT\_$, $FLO\_$ and $PRC\_$. In addition, none of the CHP parameters, storage parameters ($STG\_*$), or dispatching parameters ($ACT\_MINLD$, $ACT\_UPS$, $ACT\_CSTUP$, $ACT\_LOSPL$, $ACT\_CSTPL$, $ACT\_TIME$), can be used for IRE processes, and are ignored if used.

| Attribute name | Description                                                                 | Limitations                                                                                                                                                                                       |
| -------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ACT_EFF        | Activity efficiency                                                         | Can not be used                                                                                                                                                                                   |
| FLO_BND        | Bound on a process flow variable                                            | The bound will apply to the sum of both imports and exports of the given commodity, or, alternatively, to the net imports when a true commodity group is specified in the parameter (e.g. NRG). |
| FLO_EFF        | Amount of process flow per unit of other process flow(s) or activity.       | Same as for FLO_EMIS.                                                                                                                                                                             |
| FLO_EMIS       | Amount of emissions per unit of process flow(s) or activity.                | Can only be used on the activity, by specifying \'ACT\' as the source group.                                                                                                                      |
| FLO_FR         | Process flow fraction                                                       | Can not be used                                                                                                                                                                                   |
| FLO_FUNC       | Relationship between 2 groups of flows                                      | Can not be used                                                                                                                                                                                   |
| FLO_MARK       | Process market share bound                                                  | The bound will apply to import flow if FLO_MARK≥0, and to export flow if FLO_MARK≤0.                                                                                                              |
| FLO_SHAR       | Process flow share                                                          | Can not be used                                                                                                                                                                                   |
| FLO_SUM        | Multiplier for a commodity flow in a relationship between 2 groups of flows | Can not be used                                                                                                                                                                                   |
| PRC_MARK       | Process group-wise market share bound                                       | Same as for FLO_MARK.                                                                                                                                                                             |

  : Table 21: Specific TIMES parameters related to the modelling of storage processes.

Additional remarks with respect to inter-regional trade (IRE) processes:
- By using the process type indicator \'DISTR\', the activity and capacity of an IRE process will be based on the import flow only, if the same commodity is both imported and exported. In this case also $NCAP\_AFC(c)$ will only apply to the import flow of $c$.
- In peaking equations, IRE processes are by default taken into account by having gross imports on the supply side and gross exports on the consumption side. By defining the IRE process as a member of the set $PRC\_PKNO$, and also defining $NCAP\_PKCNT>0$, only the net imports are taken into account on the supply side, which can be useful for regions having trade flows passing through the region.

## Storage processes 

### Overview

The TIMES model generator provides tools for specifying the following types of storage processes:
- Standard timeslice storage (STG without additional storage type qualifier)
- Generalized timeslice storage (STG+STS)
- Day/night storage (STG+NST, or just NST if at ANNUAL level)
- Inter-period storage (STG+STK)

The process type indicator STG is automatically assigned also to all processes that have been defined to be of type STS, NST or STK, with the exception of ANNUAL level NST processes, which are implemented as normal processes (see Section 4.3.3 below). Therefore, the user only needs to specify one of {STG, STS, NST, STK} as the process type of a storage process.

In addition to the charged and discharged commodity, storage processes can also produce and consume auxiliary commodities (emissions, electricity, fuels, waste etc.). The flows of such auxiliary commodities can be defined to be proportional either to the activity, the main input flows, or the main output flows of the storage (see Section below).

### Timeslice storage

The standard timeslice storage operates within the timeslice cycles under the timeslices of the level immediately above the process timeslice level. Consequently, the commodity charged can be only stored over the cycle of timeslices under a single parent timeslice, and not between timeslices under different parent timeslices. For example, a standard DAYNITE level storage can only store the charged commodity over the timeslices under one season, and not between seasons.

The activity of a timeslice storage represents the storage level, i.e. the amount of energy/material stored in the storage, measured at the beginning of each timeslice. However, one should note that for a DAYNITE level storage, the level of the activity variable for each timeslice is the actual storage level multiplied by the number of days under the parent timeslice, in the same way as the level of the activity variables for standard processes is the daily activity in that timeslice multiplied by the number of days under the parent timeslice.

If a storage technology is capable of storing energy for longer periods than over daily cycles, one may consider combining a SEASON/WEEKLY level storage process with a DAYNITE storage. However, a DAYNITE level storage may also be generalized to provide a storage capability between seasons, and even between periods, by using the generalized timeslice storage type qualifier \'STS\' (and both \'STS\' and \'STK\', if the inter-period storage capability should be included). Because the same storage capacity can be utilized on all timeslice levels, the general storage process type may thus provide a somewhat improved modeling of a multi-cycle storage.

### Day/Night storage

Day/Night storage (NST) is a timeslice storage, which can store energy over the day-night cycles, but not over weekly or seasonal cycles. In its basic functionality, an NST storage does not differ much from a standard timeslice storage, the main difference being that one can define the charging timeslices by specifying them in the set $prc\_nstts$.

Day/Night storage processes that produce ANNUAL level demand commodities can be modeled either as genuine storage processes or as standard processes with a night storage capability. In both cases \'NST\' should be specified as the process type. If the process itself is defined to operate at the DAYNITE level, the process will be a genuine storage process, but if it is defined to operate at the ANNUAL level, it will be a standard process. For any such night storage devices, the charging and discharging commodity may be different, as defined via the set $top$.

When the NST process $p$ is a genuine storage process, the input set $prc_nstts(r,p,s)$ may be used for defining the charging timeslices $s$. Discharging can then only occur in timeslices other than the charging timeslices. Defining $prc\_nstts$ is required for all other genuine NST processes, except those serving an ANNUAL level demand, which can always discharge at the level of the demand, regardless of any $prc\_nstts$ defined. By defining $prc\_nstts$ on the ANNUAL level for a storage with an ANNUAL level input commodity, one can impose its $COM\_FR$ profile as the predefined inflow load profile.

In both types of NST storage, if the process is serving any ANNUAL level demand, the demand commodity is produced according to the load curve, while the charging can be optimized so that it occurs at night timeslices only. However, when the NST process is a normal process, it can be described in all other respects just as any other end-use technologies. For example, electric heating systems with accumulators can be described basically in the same way as direct electric heating systems, but with the additional night storage capability for which operational constraints may be defined e.g. with $FLO\_FR$.

### Inter-period storage

An inter-period storage process is able to store energy or material over periods. For example, a coal stockpile or a waste disposal site can be modeled as an inter-period storage. All inter-period storage processes should be defined to operate at the ANNUAL level, unless the generic timeslice process characterization (STS) is also specified.

The initial stock of an inter-period storage process can be specified by using the $STG\_CHRG$ parameter, which is interpolated such that it always includes the year at the beginning of the model horizon ($B(t1)-1$). The value of $STG\_CHRG$ in the year $B(t1)-1$ is used as the initial stock for inter-period storage. The allocation of the initial stock between the process vintages that are available at the beginning of the model horizon is left to be optimized by the model.

The activity of an inter-period storage is measured at the end of each period. Therefore, either by setting a lower bound on the activity or on the process availability, the storage can be prevented from getting fully discharged during any period. However, as there is no explicit accounting of the salvage value of the remaining contents of an inter-period storage, it may also be considered reasonable to allow discharging the storage fully in the last period, for taking into account the value of the storage.

### Auxiliary storage flows

Storage processes can have any amount of auxiliary input or output commodities, as long as they are distinct from the main storage commodity. The flows of the auxiliary commodities can only be defined to be fixedly proportional either to the activity, the main input flows, or the main output flows. The main flows of timeslice and inter-period storage processes are the flows of the charged and discharged commodities included in the set primary commodity group PCG of the process. In the day/night storage processes, the main flows consist of all commodities in the primary and shadow groups of the process (see documentation).

The relation between the auxiliary flows and the activity or main flows should be defined by using the $PRC\_ACTFLO$ and the $FLO\_FUNC$ parameters. For example, if the main storage flows of the process consist of the commodity \'STORED\', and the auxiliary commodity is \'AUX\', the auxiliary flow can be defined in the three following ways, corresponding to the cases where the auxiliary flow is proportional to the activity, the input flow, or the output flow, respectively:
- $PRC\_ACTFLO(r,t,p,'AUX')$ -- AUX proportional to activity
- $FLO\_FUNC(r,t,p,'STORED','AUX',s)$ -- AUX proportional to input flow
- $FLO\_FUNC(r,t,p,'AUX','STORED',s)$ -- AUX inversely proportional to output flow

These auxiliary storage flow relations have been implemented by adding a new TIMES equation $EQ\_STGAUX(r, v, t, p, c, s)$. As the auxiliary storage flows are represented by standard flow variables, any flow-related cost attributes and UC constraints can be additionally defined on these auxiliary flows. However, no transformation equations can be defined between any auxiliary storage flows. Therefore, if, for example, some auxiliary flows should also produce emissions, also these emissions should be defined on the basis of the activity or main flows, and not by defining a relation between the auxiliary flow and the emission flow. Consequently, it is required that all auxiliary commodity flows related to storage processes, whether energy, material, or emissions, are described by using the three types of relations shown above.

A concrete example where these enhancements to the storage processes can be very useful is the modeling of waste management, and, in particular, the modeling of landfilling of different types of waste. Using inter-period storage processes for this purpose makes it possible to conveniently incorporate e.g. the following features in the waste management model:
- Modeling of methane emissions from landfilling in a dynamic way by using first-order decay functions for the gradual waste decomposition (optionally with different rates of decay for different waste qualities);
- Modeling of other waste management and emission reduction options both before and after landfilling;
- Incorporating gate fees to landfill sites (by defining costs on an input-based auxiliary storage flow).

### Input sets and parameters specifically related to storage processes

**<ins>Input sets</ins>**

There is only one TIMES input set specifically related to storage: $prc\_nstts$. However, there are important storage-specific aspects related to each of the following input sets:
- $prc\_map(r,prc\_grp,p)$: Defines the process as a storage process, where $prc\_grp$ equals STG/STS/NST/STK according to the desired storage type.
- $prc\_actunt(r,p,cg,units\_act)$: Definition of the commodity/commodities in the PCG, i.e. those that are stored. Set of quadruples such that the members of the commodity group $cg$ is used to define the charged and discharged commodity of storage process $p$, with activity units $units\_act$, in region $r$. If the charged and discharged commodities are different, the group $cg$ should preferably contain both of them, but if the user shell does not allow that, the model generator will automatically assign to the PCG any commodities on the shadow side that are of the same type than those already in the PCG, and are not verified to be auxiliary commodities. A commodity type can also be used as the primary group of storage processes. All commodities of that type will then be included in the PCG.
- $top(r,p,c,io)$: Definition of the charged ($io=IN$) discharged ($io=OUT$) and optional auxiliary input/output commodities for storage process $p$ in region $r$. The set $top\_ire$ should thus first and foremost contain the input/output indicators for the stored commodities defined by $prc\_actunt$ (see above), but should include also any auxiliary input/output commodities assumed for the process. When the charged and discharged commodity is the same, that commodity can optionally be defined only as an input or only as an output, and in that case it will be connected to the commodity balance equations either only on the production or only on the consumption side, instead of being connected on both sides.
- $prc\_nstts(r,p,s)$: For genuine night storage process $p$ in region $r$, defines the timeslices **s** to be the charging timeslices, at which discharging cannot occur.

*<ins>Remarks</ins>*

In TIMES, the input (charge) and output (discharge) commodity of a storage process is usually the same commodity (input=output). When so, and this commodity is defined both as an input and an output of the process, the input and output flows will be taken into account in the commodity balance equations on different sides: the input on the consumption side, and the output on the production side.

However, in some cases this design has proven to be undesirable, because due to the nature of the storage processes, the input and output flows can usually be made arbitrarily large without affecting the storage operation or costs. That is so because the input flow may also bypass the storage in the same timeslice or period, without being stored, and will then be directly converted into the output flow, without any costs or efficiency losses (unless $STG\_EFF$ is being used). Such arbitrary input/output flows can also make the total commodity production arbitrarily large, thereby rendering $VAR\_COMPRD$ a very unreliable measure of the size of the commodity market. This can be undesirable with respect to various market-share constraints that are usually defined on the basis of the $VAR\_COMPRD$ values.

In order to avoid any arbitrary storage flows on the production or consumption side, the input/output flows can be defined to be both connected either on the production or consumption side, instead of being on different sides. This will prevent the undesirable impacts of such arbitrary flows. The desired side can be chosen by the user by defining the commodity only as an output (production side) or as an input (consumption side).

**<ins>Input parameters</ins>**

The TIMES input parameters that are specific to storage processes or have a specific functionality for storage processes are summarized in Table 21.

  ------------------ -------------------------------------------------------
  **Attribute name\  **Description**
  (indexes)**        

  STG_CHRG\          Exogenous amount assumed to be charged into storage
  (r,y,p,s)          **p**, in timeslice **s** and year **y**. For timeslice
                     storage this parameter can be specified for each
                     period, while for inter-period storage this parameter
                     is only taken into account for the first period, to
                     describe the initial content of the storage at the
                     beginning of the model horizon. Units: Unit of the
                     storage input flow.

  STG_EFF\           Coefficient that represents the storage efficiency of a
  (r,y,p)            storage process **p** in region **r**. Applied at the
                     commodity balance to the output flow.

  STG_LOSS\          Coefficient that represents the annual storage losses
  (r,y,p,s)          of a storage process **p** in region **r**, as a
                     fraction of the (average) amount stored, corresponding
                     to a storage time of one year. If the value specified
                     is negative, the corresponding annual losses are
                     interpreted as an annual equilibrium loss (under
                     exponential decay).

  STG_MAXCYC\        Defines a limit for the storage cycling within each
  (r,y,p)            period, by giving the maximum number of cycles over the
                     full lifetime for process **p**, region **r**.

  STG_SIFT\          Defines the storage process **p** as a special
  (r,y,p,c,s)        load-shifting storage process for commodity **c**, and
                     defines the maximum fraction of shifted loads in
                     proportion to the demand. See section 4.3.9 for
                     additional information.

  STGIN_BND\         Bound on the input flow of commodity **c** of storage
  (r,y,p,c,s,bd)     process **p** in a timeslice **s**. Units: Unit of the
                     storage input flow. (Default value: none)

  STGOUT_BND\        Bound on the output flow of commodity **c** of storage
  (r,y,p,c,s,bd)     process **p** in a timeslice **s**. Units: Unit of the
                     storage input flow. (Default value: none)

  FLO_FUNC\          Defines the ratio between the flow of commodity **c2**
  (r,y,p,c1,c2,s)    and the flow of commodity **c1**, in timeslice **s**,
                     in other words, an efficiency coefficient giving the
                     flow of commodity **c2** per one unit of flow of
                     commodity **c1**. For storage processes, can be used
                     for defining amount of discharge in **c2** per unit of
                     auxiliary flow of **c1**, or amount of auxiliary flow
                     of **c2** per unit of charging in **c1**.

  PRC_ACTFLO\        Defines a conversion coefficient between the activity
  (r,y,p,c)          and the flow in commodity **c**. For storage processes,
                     PRC_ACTFLO can be used for the commodities in the PCG
                     in the standard way, but also for defining the amount
                     of auxiliary flow of **c** per unit of activity.

  NCAP_AFC\          Can be used for defining availability factors for the
  (r,y,p,cg,tslvl)   process activity (amount stored), process output flow,
                     or process input flow, or any combination of these. See
                     Section 6.3 for additional information.

  NCAP_AFCS\         As NCAP_AFC above, but can be specified for individual
  (r,y,p,cg,s)       timeslices. NCAP_AFCs values override NCAP_AFC values
                     defined at the same level.
  ------------------ -------------------------------------------------------

  : Table 22: Limitations of using standard process parameters for storage processes.

### Availability factors for storage processes

In TIMES, capacity by default bounds only the activity. For storage, this means the amount of stored energy. However, with the $NCAP\_AFC$/$NCAP\_AFCS$ attributes, one can bound the output (or input) flows instead. Capacity then also refers to the nominal output (or input) capacity, e.g. electrical capacity of a pumped hydro power plant. In addition, one can bound simultaneously both the output and input flows by the capacity, which can be useful if the charging rate is limited by the capacity as well. Moreover, one can simultaneously define a bound also for the activity (the amount stored) in proportion to the same capacity variable. All these availability factors can be defined either on a desired timeslice level ($NCAP\_AFC$), or on individual timeslices ($NCAP\_AFCS$).

The rules for defining the availabilities for storage flows/activity can be summarized as follows:
- If the input/output commodities are different ($c1$/$c2$): Use $NCAP\_AFC(c1)$ for bounding the input flow and $NCAP\_AFC(c2)$ for bounding the output flow.
- If $input=output=c$, $NCAP\_AFC('NRG')$ will define the availability factor for both the input and output flow, while $NCAP\_AFC(c)$ will define the availability factor for the output flow only, overriding any $NCAP\_AFC('NRG')$ value if that is also specified (assuming NRG is the type of the stored commodity).
- $NCAP\_AFC(r,y,p,'ACT',tsl)$ can additionally be used for bounding the activity (the amount stored); in this case one must bear in mind that any capacity expressed in power units (e.g. MW/GW) is assumed to represent a gross storage capacity equivalent to the amount produced by full power during one full year/week/day for SEASON/WEEKLY/DAYNITE level storage processes, respectively, assuming $STG\_EFF=1$. Knowing this, the availability factor can be adjusted to correspond to the assumed real storage capacity. For example, a capacity of 1 GW is assumed to represent a storage capacity of 24 GWh for a DAYNITE storage, and if the real daily storage capacity is, say 8 GWh/GW, the maximum availability factor should be $0.333/STG\_EFF$, on the DAYNITE level.

*<ins>Remarks:</ins>*
1.  As any storage process has only a single capacity variable, the assumption is that the availabilities specified for the output/input flows and the activity are all proportional to the same capacity.
2. Note that the availability factors defined by $NCAP\_AFC$ are multiplied by any $NCAP\_AF$ / $NCAP\_AFS$ / $NCAP\_AFA$ value if defined for the same timeslice.

### Notes on other attributes for storage processes

There are important limitations of using standard processes parameters for storage processes. The most important limitations are summarized in Table 22, with regard to the parameters with the prefixes $ACT\_$, $FLO\_$ and $PRC\_$. In addition, none of the CHP parameters, IRE parameters ($IRE\_$), or dispatching parameters ($ACT\_MINLD$, $ACT\_UPS$, $ACT\_CSTUP$, $ACT\_LOSPL$, $ACT\_CSTPL$, $ACT\_TIME$), can be used for storage processes, and are ignored if used.

  ------------------- ------------------------------- --------------------------
  **Attribute name**  **Description**                 **Limitations**

  ACT_EFF             Activity efficiency             Can not be used

  FLO_BND             Bound on a process flow         Can only be used for
                      variable                        bounding auxiliary storage
                                                      flows.

  FLO_COST            Added variable cost for         Can only be used for the
                      commodity flow                  charging (input) flow(s),
                                                      and for all auxiliary
                                                      flows.

  FLO_DELIV           Delivery cost for commodity     Can only be used for the
                      flow                            discharge (output)
                                                      flow(s), and for all
                                                      auxiliary flows.

  FLO_EFF,\           Amount of process flow per unit Can only be used for
  FLO_EMIS\           of other process flow(s) or     defining an auxiliary flow
  (r,y,p,cg,c,s)      activity.                       per unit of activity, by
                                                      specifying \'ACT\' as the
                                                      source group (cg).

  FLO_FR              Process flow fraction           Can only be used for
                                                      auxiliary storage flows.

  FLO_FUNC            Relationship between 2 groups   Can only be used for
                      of flows                        defining auxiliary storage
                                                      flows.

  FLO_MARK            Process market share bound      For a stored commodity,
                                                      the bound will apply to
                                                      discharge flow when
                                                      FLO_MARK≥0, and to
                                                      charging flow if
                                                      FLO_MARK≤0.

  FLO_SHAR\           Process flow share              Can only be used among
  (r,y,p,c,cg,s,bd)                                   auxiliary flows, and for
                                                      bounding the output flow
                                                      (c) in proportion to the
                                                      activity (cg=\'ACT\')

  FLO_SUM             Multiplier for a commodity flow Can only be used among
                      in a relationship between 2     auxiliary flows.
                      groups of flows                 

  FLO_TAX, FLO_SUB    Tax/subsidy for the             Can only be used for
                      production/use of commodity by  auxiliary storage flows
                      process                         

  PRC_MARK            Process group-wise market share Same limitations as for
                      bound                           FLO_MARK.
  ------------------- ------------------------------- --------------------------

  : Table 25. User constraint modifier attributes available in TIMES.

*<ins>Additional remark on peaking equations</ins>*

In peaking equations, processes that have a peaking commodity as the PCG (as an output) are by default taken into account by their capacity on the supply side. This holds also for storage processes, which are thus by default not contributing to the peak by their flows (charging / discharging). However, by defining the storage process as a member of the set $PRC\_PKNO$, and also defining $NCAP\_PKCNT>0$, the discharge from the storage is taken into account on the supply side instead of the capacity, and the charging into the storage is included on the consumption side (should such happen in the peak timeslice). This can be recommended, whenever the capacity represents the amount stored, and not the output capacity, and may be reasonable even for storage processes where the capacity represents the nominal maximum output flow. Conversely, if the PG of a storage process is a commodity group (e.g. NRG), only the flows are by default contributing to the peak.  Should contribution by capacity be preferred, one can request that by defining $PRC\_PKAF$ for the process and the appropriate $NCAP\_PKCNT$ factors for the capacity.

### Load-shifting storage processes

In TIMES, load-shifting for demands can be modelled by introducing load shifting processes, which are special storage processes where the input / output flows represent demand shifting upwards and downwards. For utilizing this built-in support for modelling demand shifting operation for a demand or final energy commodity *D*, the user would thus need to define a storage process *P*, such that the *D* is both an input and an output (or more generally, the input could also be another commodity upstream). In addition, the user only needs to define the proportional limits for the allowed demand shifting, by using the attribute $STG\_SIFT(r,t,p,c,s)$, on the DAYNITE level, optionally also on next the level above. The dedicated load shifting constraints will then be generated for the process (see Equation $EQ\_SLSIFT$ for the constraint formulations).

This approach based on a storage process may be more convenient than manual constraints, because for the process the user will also be able to define investment costs, fixed O&M cost and variable costs for the demand shifting operation, and one would able to refer to the process activity and capacity variables easily in additional user constraints, if needed. Unlike for normal storage, the activity of the load-shifting processes is defined to be the output flow, and so the capacity represents the maximum level of the shifted loads. Preventing load shifting in either direction in any individual time-slices would also be easy by bounding the corresponding process flows to zero using $STGIN\_BND$ / $STGOUT\_BND$.

The following constraints can be modelled for load-shifting processes:
- Maximum allowed fractions of loads shifted (required, defined by $STG\_SIFT$);
- Seasonal balance equations (automatically generated);
- Standard capacity-activity equations (optional, when the capacity is modelled);
- User-defined balance constraints over sets of adjacent timeslices (optional, defined by $ACT\_TIME$);
- Maximum allowed time to meet the shifted loads either in advance or with delay (optional, defined by $ACT\_TIME$);
- Capacity bounds, activity bounds, flow bounds (optional).

The following types of costs can be modelled for load-shifting processes:
- Activity costs (cost on the discharge flow, using $ACT\_COST$);
- Flow costs (cost on the charging and/or discharging flows, using $FLO\_COST$ and/or $FLO\_DELIV$);
- Capacity cost (cost on the discharge load capacity, using $NCAP\_COST$);
- Fixed O&M cost (cost on the discharge load capacity, using $NCAP\_FOM$);
- Cost of shifting of one unit of demand load by one hour, forward (UP) and/or backward (LO) (using $ACT\_CSTRMP$).
