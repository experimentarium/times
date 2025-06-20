# Sets, Switches and Parameters

## Switches

Besides the basic data parameters described in {numref}`dem-input-parameters` below, the user controls whether the linear or non-linear formulation is activated by means of the switches shown in {numref}`dem-switches`. These switches are provided by the data handling system when the user indicates that the option is to be included in a run.

```{list-table} Switches
:name: dem-switches
:header-rows: 1

* - Switch
  - Parameter Description
* - \$SET TIMESED NO
  - Causes the Base Prices to be saved to a GDX file, for subsequent use in a policy analysis run based on any of the elastic demand options.
* - \$SET TIMESED YES
  - Activates any of LP formulations used for Demand Functions (exact formulations depending on input data)
* - \$SET MICRO YES
  - Activates any of NLP or mixed LP/NLP formulations used for Demand Functions (exact formulations depending on input data)
```

## Sets and Parameters

Like all other aspects of TIMES the user describes the demand functions for the energy system model by means of a Set and the Parameters and Switches described in this chapter. {numref}`dem-input-parameters` below describes the User Input Parameters associated with defining the TIMES demand functions.

```{list-table} Input parameters specific to demand functions.
:name: dem-input-parameters
:header-rows: 1

* - Parameter (Indexes)
  - Units & defaults
  - Parameter Description
* - COM_PROJ (r,y,c)
  - Commodity unit;
  <br>[0,∞)
  <br>default value:none
  <br>Default i/e: STD
  - Exogenous reference (Baseline) demand projection of commodity **c** in region **r** and year **y**.
  <br>In inelastic runs (Baseline runs, and any other model runs with non-elastic demands) the demands are met at the levels of the exogenous projections defined by COM_PROJ, usually exactly, but under certain circumstances some of them may also end up at a higher level than the projection.
* - COM_AGG (r,y,c,com)
  - Commodity units
  <br>[open];
  <br>default value:none
  <br>Default i/e: STD
  - Defines an aggregation of component demand **c** into an aggregate demand **com** in region **r** and year (period) **y**.
  <br>Defining COM_AGG between the component demands and the aggregate demand is required for modeling substitution elasticities.
  <br>If defined zero (e.g. by specifying IE=2), the values will be auto-generated according to the price ratios; defining the COM_AGG values zero is required for using the proper CES functions.
* - COM_VOC (r,y,c,bd)
  - Dimensionless;
  <br>[0,∞);
  <br>default value:none
  <br>Default i/e: STD
  - Defines the maximum demand variation in the lower / upper direction (**bd**=LO/UP) for demand **c** in region **r** and year **y**. The value gives the maximum deviation in proportion to the Baseline demand. Different values may be provided for each direction, thus demand elasticity curves may be asymmetric.
* - COM_STEP (r,c,bd)
  - Integer
  <br>[1,∞);
  <br>default value:none
  - Number of steps to use for the approximation of demand variation in the lower / upper direction (**bd**=LO/UP), and the associated change in producer/consumer surplus, for commodity **c** in region **r**, when using the elastic demand formulations. The shortcut **bd**=FX may be used for defining the same number of steps in both directions.
* - COM_ELAST (r,y,c,s,bd)
  - Dimensionless;
  <br>[open]
  <br>default value:none
  <br>Default i/e: STD
  - Elasticity of demand for commodity ***c***, indicating the following:
  <br>For own-price elasticities: how much the demand rises/falls in response to a unit change in the marginal cost of meeting a demand that is elastic.
  <br>For substitution elasticities: responsiveness of the ratio in which the component demands are used to the ratio of the prices of those demands
  <br>Defines elasticities for demand ***c*** in region ***r*** and year ***y***, timeslice ***s***
  <br>***lim*** = LO/UP : defines the own-price elasticity in the lower / upper direction in the linear formulation
  <br>***lim*** = FX (s=ANNUAL): defines own-price elasticities in the non-linear formulation; can also be used in the linear formulation for defining the own-price elasticities for the aggregate demands, optionally also for defining component-differentiated susbstution elasticities
  <br>***lim*** = N (s=ANNUAL): defines the substitution elasticity for component demands of the demand aggregation represented by commodity ***c***; positive values signify the standard variant, negative values signify the volume-preserving variant formulation
```

**Important remarks:**

- *COM_PROJ* should be explicitly defined by the user only for the component demands, and never for the aggregate demands.
- As mentioned in {numref}`dem-input-parameters`, the substitution elasticities can be defined by specifying *COM_ELAST*(r,t,com,ANNUAL,\'N\') for the aggregate demands. However, \'FX\' elasticities for the *component demands* can be optionally specified for defining component-differentiated substitution elasticities. Nonetheless, even when doing so, *COM_ELAST*(r,t,com, ANNUAL,\'N\') always defines the minimum substitution elasticity among the component demands of ***com***. 
- Note that the aggregate demands are always at the ANNUAL level only, and thus only ANNUAL level own-price demand elasticities are supported for the demand aggregates. 
- When using the non-linear formulation, demand substitution is supported only at the ANNUAL level for the component demands of the CES aggregates. The demand variations will thus be proportionally the same for all timeslices. 
- Multi-level nested CES demand aggregations are also fully supported both in the non-linear and in the linearized case. 
- Recursive CES demand aggregations are not supported, neither in the non-linear nor in the linearized case.
- The Cobb-Douglas case ($σ_{k}=1$) is also supported, but in the non-linear formulation it is handled by setting $σ_{k}$ very close to unity.
