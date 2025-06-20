(b-examples)=
# Examples

Assume that we wish to define linearized damage costs for the emission commodity \'EM\' so that the cost function has the following properties:

- The reference level of emissions is 80 units;
- The marginal cost at the reference level are 10 cost units per emission unit;
- The cost elasticity is 1 in the lower direction, and 0.7 in the upper direction;

The damage function can be specified with the following parameters:

```
PARAMETER DAM_COST / REG.2000.EM.CUR 10 /;
PARAMETER DAM_BQTY / REG.EM 80 /;
PARAMETER DAM_ELAST / REG.EM.LO 1, REG.EM.UP 0.7 /;
```

```{figure} /part-2/assets/linearized-damage-function.svg
:name: example-linearized-function-111
:align: center

Example of a linearized damage function with 1+1+1 steps (1 lower step, 1 middle step, 1 upper step).
```

As we did not specify the number of steps, but we did specify the elasticities in both directions, the number of steps is assumed to be 1 in both directions. The resulting damage cost function is illustrated in {numref}`example-linearized-function-111`. Because the damage function has a very coarse representation, the total costs have notable deviations from the accurate non-linear function. Note that the step size has been automatically determined to be **DAM_BQTY/(DAM_STEP+0.5)** = 80/1.5. However, the last step has no upper bound.

Assume next that we would like to refine the damage function by the following specifications:

- We want to have 5 steps below the reference, and 3 steps above it;
- The threshold level of damage costs is 20 units of emissions;
- The steps above the reference level should cover 100 units of emissions.

The damage function can be specified with the following parameters:

```
PARAMETER DAM_COST / REG.2000.EM.CUR 10 /;
PARAMETER DAM_BQTY / REG.EM 80 /;
PARAMETER DAM_ELAST / REG.EM.LO 1, REG.EM.UP 0.7 /;
PARAMETER DAM_STEP / REG.EM.LO 5, REG.EM.UP 3 /;
PARAMETER DAM_VOC / REG.EM.LO 60, REG.EM.UP 100 /;
```

The resulting damage cost function is illustrated in {numref}`example-linearized-function-1513`. The cost function follows now very closely the accurate non-linear function. Note that the step sizes derived from the VOC specifications are 10 units for the lower steps, 20 for the middle step, and 30 units for the upper steps. However, the last step of course has no upper bound.

 ```{figure} /part-2/assets/linearized-damage-function-2.svg
:name: example-linearized-function-1513
:align: center
Example of a linearized damage function with 1+5+1+3 steps (one zero cost step, 5 lower steps, one middle step, 3 upper steps).
```
