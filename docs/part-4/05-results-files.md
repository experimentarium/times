(pa4-appendix-b)=
# Appendix B TIMES Results Files

There are three files produced for the Results module by the GDX2VEDA utility: the \<scenarioname\>.VD data dump with the attributes, \<scenarioname\>.VDE (set elements), and \<scenarioname\>.VDS (sets definition). In addition, VEDA2.0 produces a \<scenarioname\>.VDT (topology) file with the RES connectivity information. These files are dumped in comma delimited format. They never require user intervention, though they may be processed by other software if desired. Snippets of each file are shown below, after a brief description of the layout of each.

## B.1 \<scenarioname\>.VD

The \<scenarioname\>.VD file contains the application Results module header directives (controlling the appearance of the main Results table specification form) followed by the actual model data.

<ins>Layout, after the header</ins>: Attribute, Commodity, Process, Period, Region, Vintage, Timeslice, UserConstraint, Value;

<ins>Excerpt</ins>:

\* GDX2VEDAversion- 2005-10-07

\* ImportID- Scenario:DemoS_012b

\* VEDAFlavor- TIMES

\* Dimensions-
Attribute;Commodity;Process;Period;Region;Vintage;TimeSlice;UserConstraint;PV

\* ParentDimensions- Commodity: Region; Process: Region

\* SetsAllowed- Commodity;Process

\* FieldSize-
Attribute:31;Commodity:31;Process:31;Period:31;Region:31;Vintage:31;TimeSlice:31;UserConstraint:31;PV:20

\* NotIndexed- PV

\* ValueDim- PV

\* DefaultValueDim- PV

\* FieldSeparator- ,

\* TextDelim- \"

\"VAR_Act\",\"-\",\"AOTETOT\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",564.8409

\"VAR_Act\",\"-\",\"CAPEELC\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",1148.6992095

\"VAR_Act\",\"-\",\"COTEBIO\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",3.939

\"VAR_Act\",\"-\",\"COTECOA\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",37.3712625

\"VAR_Act\",\"-\",\"COTEELC\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",63.8166227499999

\"VAR_Act\",\"-\",\"COTEGAS\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",212.309676

\"VAR_Act\",\"-\",\"COTEOIL\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",129.503715

\"VAR_Act\",\"-\",\"CSHEBIO\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",35.451

\"VAR_Act\",\"-\",\"CSHEELC\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",63.81662275

\"VAR_Act\",\"-\",\"CSHEGAS\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",495.389244

\"VAR_Act\",\"-\",\"CSHEOIL\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",302.175335

\"VAR_Act\",\"-\",\"CSHESOL\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",7.575

\"VAR_Act\",\"-\",\"ELCNENUC00\",\"2005\",\"REG1\",\"2005\",\"S\",\"-\",746.220483540681

\"VAR_Act\",\"-\",\"ELCNENUC00\",\"2005\",\"REG1\",\"2005\",\"W\",\"-\",723.929516459321

\"VAR_Act\",\"-\",\"ELCREHYD00\",\"2005\",\"REG1\",\"2005\",\"SD\",\"-\",244.125

\"VAR_Act\",\"-\",\"ELCREHYD00\",\"2005\",\"REG1\",\"2005\",\"SN\",\"-\",0.837000000000359

\"VAR_Act\",\"-\",\"ELCREHYD00\",\"2005\",\"REG1\",\"2005\",\"WD\",\"-\",243.846

\"VAR_Act\",\"-\",\"ELCRESOL00\",\"2005\",\"REG1\",\"2005\",\"SD\",\"-\",16.9805936073059

\"VAR_Act\",\"-\",\"ELCRESOL00\",\"2005\",\"REG1\",\"2005\",\"SN\",\"-\",10.4147640791476

\"VAR_Act\",\"-\",\"ELCRESOL00\",\"2005\",\"REG1\",\"2005\",\"WD\",\"-\",16.9611872146119

\"VAR_Act\",\"-\",\"ELCRESOL00\",\"2005\",\"REG1\",\"2005\",\"WN\",\"-\",12.2907153729072

\"VAR_Act\",\"-\",\"ELCREWIN00\",\"2005\",\"REG1\",\"2005\",\"SD\",\"-\",71.5472816780823

\"VAR_Act\",\"-\",\"ELCREWIN00\",\"2005\",\"REG1\",\"2005\",\"SN\",\"-\",43.3049336472603

\"VAR_Act\",\"-\",\"ELCREWIN00\",\"2005\",\"REG1\",\"2005\",\"WD\",\"-\",75.2268561643836

\"VAR_Act\",\"-\",\"ELCREWIN00\",\"2005\",\"REG1\",\"2005\",\"WN\",\"-\",71.5472816780823

\"VAR_Act\",\"-\",\"ELCTECOA00\",\"2005\",\"REG1\",\"2005\",\"S\",\"-\",1351.31629846897

\"VAR_Act\",\"-\",\"ELCTECOA00\",\"2005\",\"REG1\",\"2005\",\"W\",\"-\",1044.37445353102

\"VAR_Act\",\"-\",\"ELCTEGAS00\",\"2005\",\"REG1\",\"2005\",\"SD\",\"-\",226.711979456911

\"VAR_Act\",\"-\",\"ELCTEGAS00\",\"2005\",\"REG1\",\"2005\",\"SN\",\"-\",300.30842173892

\"VAR_Act\",\"-\",\"EXPCOA1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",745.59485

\"VAR_Act\",\"-\",\"EXPHFO1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",804.770973903333

\"VAR_Act\",\"-\",\"EXPKER1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",295.3885

\"VAR_Act\",\"-\",\"EXPLPG1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",32.1237949472747

\"VAR_Act\",\"-\",\"EXPNAP1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",400.84

\"VAR_Act\",\"-\",\"EXPOIL1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",1648.4855

\"VAR_Act\",\"-\",\"EXPOPP1\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",453.036

\"VAR_Act\",\"-\",\"FTE-AGRBIO\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",8.9265138547333

\"VAR_Act\",\"-\",\"FTE-AGRCOA\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",8.46903001967851

\"VAR_Act\",\"-\",\"FTE-AGRELC\",\"2005\",\"REG1\",\"2005\",\"SD\",\"-\",72.2276809309521

\"VAR_Act\",\"-\",\"FTE-AGRELC\",\"2005\",\"REG1\",\"2005\",\"SN\",\"-\",66.4494664564759

\"VAR_Act\",\"-\",\"FTE-AGRELC\",\"2005\",\"REG1\",\"2005\",\"WD\",\"-\",72.1451350098882

\"VAR_Act\",\"-\",\"FTE-AGRELC\",\"2005\",\"REG1\",\"2005\",\"WN\",\"-\",78.418625010748

\"VAR_Act\",\"-\",\"FTE-AGRGAS\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",160.377867843615

\"VAR_Act\",\"-\",\"FTE-AGROIL\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",97.8265808739081

\"VAR_Act\",\"-\",\"FTE-COMBIO\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",48.25275

\"VAR_Act\",\"-\",\"FTE-COMCOA\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",37.3712625

\"VAR_Act\",\"-\",\"FTE-COMELC\",\"2005\",\"REG1\",\"2005\",\"SD\",\"-\",309.846497299342

\"VAR_Act\",\"-\",\"FTE-COMELC\",\"2005\",\"REG1\",\"2005\",\"SN\",\"-\",309.846497299342

\"VAR_Act\",\"-\",\"FTE-COMELC\",\"2005\",\"REG1\",\"2005\",\"WD\",\"-\",329.999115009868

\"VAR_Act\",\"-\",\"FTE-COMELC\",\"2005\",\"REG1\",\"2005\",\"WN\",\"-\",329.999115009868

\"VAR_Act\",\"-\",\"FTE-COMGAS\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",762.742169333334

\"VAR_Act\",\"-\",\"FTE-COMOIL\",\"2005\",\"REG1\",\"2005\",\"ANNUAL\",\"-\",507.22288375

## B.2 \<scenarioname\>.VDE

The \<scenarioname\>.VDE file contains the list of individual set member elements for each index managed by Results module along with their descriptions.

<ins>Layout</ins>: Dimension Name - Region - Element name - Element Description;

<ins>Excerpt</ins>:

\"Attribute\",\"-\",\"VAR_act\",\"Process Activity\"

\"Attribute\",\"-\",\"VAR_actM\",\"Process Activity - Marginals\"

\"Attribute\",\"-\",\"VAR_cap\",\"Technology Capacity\"

\"Attribute\",\"-\",\"VAR_capM\",\"Technology Capacity - Marginals\"

\"Attribute\",\"-\",\"VAR_ncap\",\"Technology Investment - New capacity\"

\"Attribute\",\"-\",\"VAR_ncapM\",\"Technology Investment - Marginals\"

\"Attribute\",\"-\",\"VAR_ncapR\",\"Technology Investment - BenCost + ObjRange\"

\"Attribute\",\"-\",\"VAR_fin\",\"Commodity Consumption by Process\"

\"Attribute\",\"-\",\"VAR_fout\",\"Commodity Production by Process\"

\"Attribute\",\"-\",\"VAR_comprd\",\"Commodity Total Production\"

\"Attribute\",\"-\",\"VAR_comprdM\",\"Commodity Total Production - Marginal\"

\"Attribute\",\"-\",\"VAR_comnet\",\"Commodity Net\"

\"Attribute\",\"-\",\"VAR_comnetM\",\"Commodity Net - Marginal\"

\"Attribute\",\"-\",\"VAR_eout\",\"Electricity supply by technology and energy source\"

\"Attribute\",\"-\",\"EQ_combal\",\"Commodity Slack/Levels\"

\"Attribute\",\"-\",\"EQ_combalM\",\"Commodity Slack/Levels - Marginals\"

\"Attribute\",\"-\",\"EQ_peak\",\"Peaking Constraint Slack\"

\"Attribute\",\"-\",\"EQ_peakM\",\"Peaking Constraint Slack - Marginals\"

\"Attribute\",\"-\",\"EQ_Cumflo\",\"Cumulative flow constraint - Levels\"

\"Attribute\",\"-\",\"EQ_CumfloM\",\"Cumulative flow constraint - Marginals\"

\"Attribute\",\"-\",\"PAR_capLO\",\"Capacity Lower Limit\"

\"Attribute\",\"-\",\"PAR_capUP\",\"Capacity Upper Limit\"

\"Attribute\",\"-\",\"PAR_Top\",\"Process topology (Opted out - SET RPT_TOP YES to activate)\"

\"Attribute\",\"-\",\"Cap_New\",\"Newly installed capacity and lumpsum investment by vintage and commissioning period\"

\"Attribute\",\"-\",\"COST_inv\",\"Annual investment costs\"

\"Attribute\",\"-\",\"COST_dec\",\"Annual decommissioning costs\"

\"Attribute\",\"-\",\"COST_salv\",\"Salvage values of capacities at EOH+1\"

\"Attribute\",\"-\",\"COST_late\",\"Annual late costs\"

\"Attribute\",\"-\",\"COST_fom\",\"Annual fixed operating and maintenance costs\"

\"Attribute\",\"-\",\"COST_act\",\"Annual activity costs\"

\"Attribute\",\"-\",\"COST_flo\",\"Annual flow costs (including import/export prices)\"

\"Attribute\",\"-\",\"COST_com\",\"Annual commodity costs\"

\"Attribute\",\"-\",\"COST_els\",\"Annual elastic demand cost term\"

\"Attribute\",\"-\",\"COST_dam\",\"Annual damage cost term\"

\"Attribute\",\"-\",\"COST_invx\",\"Annual investment taxes/subsidies\"

\"Attribute\",\"-\",\"COST_fixx\",\"Annual fixed taxes/subsidies\"

\"Attribute\",\"-\",\"COST_flox\",\"Annual flow taxes/subsidies\"

\"Attribute\",\"-\",\"COST_comx\",\"Annual commodity taxes/subsidies\"

\"Attribute\",\"-\",\"COST_ire\",\"Annual implied costs of endogenous trade\"

\"Attribute\",\"-\",\"COST_NPV\",\"Total discounted costs by process/commodity (optional)\"

\"Attribute\",\"-\",\"Time_NPV\",\"Discounted value of time by period\"

\"Attribute\",\"-\",\"VAL_Flo\",\"Annual commodity flow values\"

\"Attribute\",\"-\",\"ObjZ\",\"Total discounted system cost\"

\"Attribute\",\"-\",\"Reg_wobj\",\"Regional total expected discounted system cost\"

\"Attribute\",\"-\",\"Reg_obj\",\"Regional total discounted system cost\"

\"Attribute\",\"-\",\"Reg_irec\",\"Regional total discounted implied trade cost\"

\"Attribute\",\"-\",\"Reg_ACost\",\"Regional total annualized costs by period\"

\"Attribute\",\"-\",\"User_Con\",\"Level of user constraint\"

\"Attribute\",\"-\",\"User_ConFXM\",\"Marginal cost of fixed bound user constraint\"

\"Attribute\",\"-\",\"User_ConLOM\",\"Marginal cost of lower bound user constraint\"

\"Attribute\",\"-\",\"User_ConUPM\",\"Marginal cost of upper bound user constraint\"

\"Attribute\",\"-\",\"User_DynbM\",\"Marginal cost of dynamic process bound constraint\"

\"Attribute\",\"-\",\"User_Maxbet\",\"Level of MaxBet constraint\"

\"Attribute\",\"-\",\"VAR_climate\",\"Climate result variables\"

\"Attribute\",\"-\",\"Dual_Clic\",\"Shadow price of climate constraint\"

\"Attribute\",\"-\",\"VAR_Macro\",\"MACRO result variables\"

\"Commodity\",\"REG2\",\"GAS\",\"Natural Gas\"

\"Commodity\",\"REG1\",\"GAS\",\"Natural Gas\"

\"Commodity\",\"REG2\",\"ELC\",\"Electricity\"

\"Commodity\",\"REG1\",\"ELC\",\"Electricity\"

\"Commodity\",\"REG2\",\"AGRBIO\",\"Agriculture Biomass\"

\"Commodity\",\"REG1\",\"AGRBIO\",\"Agriculture Biomass\"

\"Commodity\",\"REG2\",\"AGRCO2\",\"Agriculture Carbon dioxide\"

\"Commodity\",\"REG1\",\"AGRCO2\",\"Agriculture Carbon dioxide\"

\"Commodity\",\"REG2\",\"AGRCOA\",\"Agriculture Solid Fuels\"

\"Commodity\",\"REG1\",\"AGRCOA\",\"Agriculture Solid Fuels\"

\"Commodity\",\"REG2\",\"AGRELC\",\"Agriculture Electricity\"

\"Commodity\",\"REG1\",\"AGRELC\",\"Agriculture Electricity\"

\"Commodity\",\"REG2\",\"AGRGAS\",\"Agriculture Natural Gas\"

\"Commodity\",\"REG1\",\"AGRGAS\",\"Agriculture Natural Gas\"

\"Commodity\",\"REG2\",\"AGROIL\",\"Agriculture oil\"

\"Commodity\",\"REG1\",\"AGROIL\",\"Agriculture Oil\"

\"Commodity\",\"REG2\",\"BIO\",\"Biomass\"

\"Commodity\",\"REG1\",\"BIO\",\"Biomass\"

\"Commodity\",\"REG2\",\"COA\",\"Solid Fuels\"

\"Commodity\",\"REG1\",\"COA\",\"Solid Fuels\"

\"Commodity\",\"REG2\",\"COMBIO\",\"Commercial Biomass\"

\"Commodity\",\"REG1\",\"COMBIO\",\"Commercial Biomass\"

\"Commodity\",\"REG2\",\"COMCO2\",\"Commercial Carbon dioxide\"

\"Commodity\",\"REG1\",\"COMCO2\",\"Commercial Carbon dioxide\"

\"Commodity\",\"REG2\",\"COMCOA\",\"Commercial Solid Fuels\"

\"Commodity\",\"REG1\",\"COMCOA\",\"Commercial Solid Fuels\"

\"Commodity\",\"REG2\",\"COMELC\",\"Commercial Electricity\"

\"Commodity\",\"REG1\",\"COMELC\",\"Commercial Electricity\"

\"Commodity\",\"REG2\",\"COMGAS\",\"Commercial Natural Gas\"

\"Commodity\",\"REG1\",\"COMGAS\",\"Commercial Natural Gas\"

\"Commodity\",\"REG2\",\"COMOIL\",\"Commercial oil\"

\"Commodity\",\"REG1\",\"COMOIL\",\"Commercial Oil\"

\"Commodity\",\"REG2\",\"COMSOL\",\"Commercial Solar energy\"

\"Commodity\",\"REG1\",\"COMSOL\",\"Commercial Solar energy\"

## B.3 \<scenarioname\>.VDS

The \<scenarioname\>.VDS file provides the set membership information for the dimensions where sets are allowed. Note that these are different from the user-defined sets (rule-based) that are managed in the Results module. But these sets can be used as a part of those rules.

<ins>Layout</ins>: Type of set (tab), region, set name, item name;

<ins>Excerpt</ins>:

\"Commodity\",\"REG1\",\"ELC+\",\"ELC\"

\"Commodity\",\"REG2\",\"ELC+\",\"ELC\"

\"Commodity\",\"REG1\",\"ELC+\",\"AGRELC\"

\"Commodity\",\"REG2\",\"ELC+\",\"AGRELC\"

\"Commodity\",\"REG1\",\"ELC+\",\"COMELC\"

\"Commodity\",\"REG2\",\"ELC+\",\"COMELC\"

\"Commodity\",\"REG1\",\"ELC+\",\"RSDELC\"

\"Commodity\",\"REG2\",\"ELC+\",\"RSDELC\"

\"Commodity\",\"REG1\",\"ELC+\",\"TRAELC\"

\"Commodity\",\"REG2\",\"ELC+\",\"TRAELC\"

\"Commodity\",\"REG1\",\"ENV\",\"AGRCO2\"

\"Commodity\",\"REG2\",\"ENV\",\"AGRCO2\"

\"Commodity\",\"REG1\",\"ENV\",\"COMCO2\"

\"Commodity\",\"REG2\",\"ENV\",\"COMCO2\"

\"Commodity\",\"REG1\",\"ENV\",\"ELCCO2\"

\"Commodity\",\"REG2\",\"ENV\",\"ELCCO2\"

\"Commodity\",\"REG1\",\"ENV\",\"INDCO2\"

\"Commodity\",\"REG2\",\"ENV\",\"INDCO2\"

\"Commodity\",\"REG1\",\"ENV\",\"RSDCO2\"

\"Commodity\",\"REG2\",\"ENV\",\"RSDCO2\"

\"Commodity\",\"REG1\",\"ENV\",\"TOTCO2\"

\"Commodity\",\"REG2\",\"ENV\",\"TOTCO2\"

\"Commodity\",\"REG1\",\"ENV\",\"TRACO2\"

\"Commodity\",\"REG2\",\"ENV\",\"TRACO2\"

\"Commodity\",\"REG1\",\"DEM\",\"DAOT\"

\"Commodity\",\"REG2\",\"DEM\",\"DAOT\"

\"Commodity\",\"REG1\",\"DEM\",\"DCAP\"

\"Commodity\",\"REG2\",\"DEM\",\"DCAP\"

\"Commodity\",\"REG1\",\"DEM\",\"DCOT\"

\"Commodity\",\"REG2\",\"DEM\",\"DCOT\"

\"Commodity\",\"REG1\",\"DEM\",\"DCSH\"

\"Commodity\",\"REG2\",\"DEM\",\"DCSH\"

\"Commodity\",\"REG1\",\"DEM\",\"DIDM1\"

\"Commodity\",\"REG2\",\"DEM\",\"DIDM1\"

\"Commodity\",\"REG1\",\"DEM\",\"DRAP\"

\"Commodity\",\"REG2\",\"DEM\",\"DRAP\"

\"Commodity\",\"REG1\",\"DEM\",\"DROT\"

\"Commodity\",\"REG2\",\"DEM\",\"DROT\"

\"Commodity\",\"REG1\",\"DEM\",\"DRSH\"

\"Commodity\",\"REG2\",\"DEM\",\"DRSH\"

\"Commodity\",\"REG1\",\"DEM\",\"DTCAR\"

\"Commodity\",\"REG2\",\"DEM\",\"DTCAR\"

\"Commodity\",\"REG1\",\"DEM\",\"DTPUB\"

\"Commodity\",\"REG2\",\"DEM\",\"DTPUB\"

\"Commodity\",\"REG1\",\"NRG\",\"GAS\"

## B.4 \<scenarioname\>.VDT

The \<scenarioname\>.VDT file contains all the Reference Energy System (RES) topology information.

<ins>Layout</ins>: Region, Process, Commodity, IN/OUT topology indicator. VEDA BE also enables one to look at UCs that are related to a process or commodity. \<UC Name\>, Process, Commodity, "UC" entries are needed for that.

<ins>Excerpt</ins>:

\*VFEPATH=C:\\Veda\\VEDA_Models\\DemoS_012

\*ScenDesc=Demo Step 012 CO2 Tax

\*ScenEDesc=Demo Step 012 CO2 Tax

\"AU_NUC_MaxCAP\",\"ELCNENUC00\",\"-\",\"UC\"

\"AU_NUC_MaxCAP\",\"ELCNNNUC01\",\"-\",\"UC\"

\"REG1\",\"AOTETOT\",\"AGRBIO\",\"IN\"

\"REG1\",\"AOTETOT\",\"AGRCO2\",\"OUT\"

\"REG1\",\"AOTETOT\",\"AGRCOA\",\"IN\"

\"REG1\",\"AOTETOT\",\"AGRELC\",\"IN\"

\"REG1\",\"AOTETOT\",\"AGRGAS\",\"IN\"

\"REG1\",\"AOTETOT\",\"AGROIL\",\"IN\"

\"REG1\",\"AOTETOT\",\"DAOT\",\"OUT\"

\"REG1\",\"AOTETOT\",\"DEMO\",\"OUT\"

\"REG1\",\"AOTETOT\",\"NRGI\",\"IN\"

\"REG1\",\"CAPEELC\",\"COMELC\",\"IN\"

\"REG1\",\"CAPEELC\",\"DCAP\",\"OUT\"

\"REG1\",\"CAPEELC\",\"DEMO\",\"OUT\"

\"REG1\",\"CAPEELC\",\"NRGI\",\"IN\"

\"REG1\",\"CAPNELC1\",\"COMELC\",\"IN\"

\"REG1\",\"CAPNELC1\",\"DCAP\",\"OUT\"

\"REG1\",\"CAPNELC1\",\"DEMO\",\"OUT\"

\"REG1\",\"CAPNELC1\",\"NRGI\",\"IN\"

\"REG1\",\"COTEBIO\",\"COMBIO\",\"IN\"

\"REG1\",\"COTEBIO\",\"DCOT\",\"OUT\"

\"REG1\",\"COTEBIO\",\"DEMO\",\"OUT\"

\"REG1\",\"COTEBIO\",\"NRGI\",\"IN\"

\"REG1\",\"COTECOA\",\"COMCO2\",\"OUT\"

\"REG1\",\"COTECOA\",\"COMCOA\",\"IN\"

\"REG1\",\"COTECOA\",\"DCOT\",\"OUT\"

\"REG1\",\"COTECOA\",\"DEMO\",\"OUT\"

\"REG1\",\"COTECOA\",\"NRGI\",\"IN\"

\"REG1\",\"COTEELC\",\"COMELC\",\"IN\"

\"REG1\",\"COTEELC\",\"DCOT\",\"OUT\"

\"REG1\",\"COTEELC\",\"DEMO\",\"OUT\"

\"REG1\",\"COTEELC\",\"NRGI\",\"IN\"

\"REG1\",\"COTEGAS\",\"COMCO2\",\"OUT\"

\"REG1\",\"COTEGAS\",\"COMGAS\",\"IN\"

\"REG1\",\"COTEGAS\",\"DCOT\",\"OUT\"

\"REG1\",\"COTEGAS\",\"DEMO\",\"OUT\"

\"REG1\",\"COTEGAS\",\"NRGI\",\"IN\"

\"REG1\",\"COTEOIL\",\"COMCO2\",\"OUT\"

\"REG1\",\"COTEOIL\",\"COMOIL\",\"IN\"

\"REG1\",\"COTEOIL\",\"DCOT\",\"OUT\"

\"REG1\",\"COTEOIL\",\"DEMO\",\"OUT\"
