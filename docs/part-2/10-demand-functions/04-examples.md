# Examples

Assume that we wish to define a non-linear CES demand function for the aggregate demand TLPKM (passenger land travel), having the following component demands:

- TRT -- passenger car travel
- TRB -- passenger bus travel
- TRW -- passenger two-wheeler travel
- TTP -- passenger rail travel

The demand function can be set up with the following input parameters (where **r** stands for regions, **t** for milestone years, and \'**0**\' for interpolation option placeholder):

```{list-table} Non-linear CES demand function example.
:name: dem-nl-ces-example
:header-rows: 1

* - Parameters
  - Description
* - COM_AGG(r,\'0\',\'TRT\',\'TLPKM\') = 2;
  - Aggregation of TRT into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRB\',\'TLPKM\') = 2;
  - Aggregation of TRB into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRW\',\'TLPKM\') = 2;
  - Aggregation of TRW into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TTP\',\'TLPKM\') = 2;
  - Aggregation of TTP into TPASS with price ratios
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'FX\')=0.35;
  - Own-price elasticity of aggregate demand
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'N\')=1.2;
  - Elasticity of substitution between components
* - COM_VOC(r,t,\'TLPKM\',\'UP\')=1;
  - Max. upper variance of aggregate demand
```

Assume now that we wish to define the same demand function but with the linear formulation for the CES function. The demand function can be set up with the following input parameters (where **r** stands for regions, **t** for milestone years, and **bd** for the inequality bound types (\'LO\', \'UP\')):

```{list-table} Linear CES demand function example.
:name: dem-linear-ces-example
:header-rows: 1

* - Parameters
  - Description
* - COM_AGG(r,\'0\',\'TRT\',\'TLPKM\') = 2;
  - Aggregation of TRT into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRB\',\'TLPKM\') = 2;
  - Aggregation of TRB into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TRW\',\'TLPKM\') = 2;
  - Aggregation of TRW into TPASS with price ratios
* - COM_AGG(r,\'0\',\'TTP\',\'TLPKM\') = 2;
  - Aggregation of TTP into TPASS with price ratios
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'FX\')=0.35;
  - Own-price elasticity of aggregate demand
* - COM_ELAST(r,t,\'TLPKM\',\'ANNUAL\',\'N\')=1.2;
  - Elasticity of substitution between components
* - COM_STEP(r,\'TRT\',\'FX\')=100;
  - Number of steps for TRT in both directions
* - COM_STEP(r,\'TRB\',\'FX\')=100;
  - Number of steps for TRB in both directions
* - COM_STEP(r,\'TRW\',\'FX\')=100;
  - Number of steps for TRW in both directions
* - COM_STEP(r,\'TTP\',\'FX\')=100;
  - Number of steps for TTP in both directions
* - COM_STEP(r,\'TLPKM\',\'LO\')=120;
  - Number of steps for TLPKM in lower direction
* - COM_STEP(r,\'TLPKM\',\'UP\')=80;
  - Number of steps for TLPKM in upper direction
* - COM_VOC(r,t,\'TRT\',bd)=0.8;
  - Max. variance of TRT, given in both directions
* - COM_VOC(r,t,\'TRB\',bd)=0.8;
  - Max. variance of TRB, given in both directions
* - COM_VOC(r,t,\'TRW\',bd)=0.8;
  - Max. variance of TRW, given in both directions
* - COM_VOC(r,t,\'TTP\',bd)=0.8;
  - Max. variance of TTP, given in both directions
* - COM_VOC(r,t,\'TLPKM\',\'LO\')=0.5;
  - Max. lower variance of aggregate demand
* - COM_VOC(r,t,\'TLPKM\',\'UP\')=0.3;
  - Max. upper variance of aggregate demand
```

Note that using \'FX\' as a shortcut for bd={\'LO\',\'UP\'} in *COM_STEP* is only supported in TIMES v4.4.0 and above, and that *COM_VOC* does not have any such shortcut.
