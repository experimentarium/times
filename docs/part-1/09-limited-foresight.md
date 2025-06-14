(using-times-with-limited-foresight)=
# Using TIMES with limited foresight (time-stepped)

It may be useful to simulate market conditions where all agents take decisions with only a limited foresight of a few years or decades, rather than the very long term. By so doing, a modeler may attempt to simulate \"real-world\" decision making conditions, rather than socially optimal ones. Both objectives are valid provided the modeler is well aware of each approach\'s characteristics.

Be that as it may, it is possible to use TIMES in a series of time-stepped runs, each with an optimizing horizon shorter than the whole horizon. The option that enables this mode is named FIXBOH, which freezes the solution over some user chosen years, while letting the model optimize over later years. The FIXBOH feature has several applications and is first described below before a full description of the time-stepped procedure.

## The FIXBOH feature

This feature requires that an initial run be made first, and then FIXBOH sets fixed bounds for a subsequent run according to the solution values from the initial run up to the last milestone year less than or equal to the year specified by the FIXBOH control parameter. For instance, the initial run may be a reference case, which is run from 2010 to 2100, and the FIXBOH value might be set at 2015, in which case a subsequent run would have exactly the same solution values as the reference case up to 2015. This is an extremely convenient feature to use in most situations.

As a generalization to the basic scheme described above, the user can also request fixing to the previous solution different sets of fixed years according to region.

**<ins>Example</ins>**: Assume that you would like to analyze the 15-region ETSAP TIAM model with some shocks after the year 2030, and you are interested in differences in the model solution only in regions that have notable gas or LNG trade with the EU. Therefore, you would like to fix the regions AUS, CAN, CHI, IND, JPN, MEX, ODA and SKO completely to the previous solution, and all other regions to the previous solution up to 2030.

## The time-stepped option (TIMESTEP)

The purpose of the TIMESTEP option is to run the model in a stepwise manner with limited foresight. The TIMESTEP control variable specifies the number of years that should be optimized in each solution step. The total model horizon will be solved by a series of successive steps, so that in each step the periods to be optimized are advanced further in the future, and all periods before them are fixed to the solution of the previous step (using the FIXBOH feature). It is important that any two successive steps have one or more overlapping period(s), in order to insure overall continuity of the decisions between the two steps (in the absence of the overlap, decisions taken at step ***n*** would have no initial conditions and would be totally disconnected from step $n-1$ decisions.)

{numref}`p1-periods-in-time-stepped-solution` illustrates the step-wise solution approach with a horizon of 8 periods and 6 successive optimization steps. Each step has a 2 period sub-horizon, and there is also an overlap of one period between a step and the next. More explicitly: at step 2, all period 2 variables are frozen at the values indicated in the solution of step 1, and period 3 is free to be optimized. At step 3, period 3 variables are frozen and period 4 is optimized, etc.

```{figure} ../assets/periods-in-stepped-solution.svg
:name: p1-periods-in-time-stepped-solution
:align: center

Sequence of optimized periods in the stepped TIMES solution approach.
```

*Each run includes also the fixed solution of all earlier periods.*

The amount of overlapping years between successive steps is by default half of the active step length (the value of TIMESTEP), but it can be controlled by the user.

<ins>Important remark</ins>: as mentioned above, the user chooses the lengths of the sub-horizons and the length of the overlaps, *both expressed in years*. Because the time periods used in the model may be variable and may not always exactly match with the step-length and overlap, the actual active step-lengths and overlaps may differ somewhat from the values specified by the user. At each step the model generator uses a heuristic that tries to make a best match between the remaining available periods and the prescribed step length. However, at each step it is imperative that at least one of the previously solved periods must be fixed, and at least one remaining new period is taken into the active optimization in the current step.
