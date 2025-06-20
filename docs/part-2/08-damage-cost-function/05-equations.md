(b-equations)=
# Equations

There are two blocks of equations generated for damage cost functions, whenever they are included in the objective function. The two equations related to the damage functions are listed and briefly described below in {numref}`dam-constraints`. The equations include the balance of stepped emissions, the objective component for damage costs, and the augmented total objective function.

In addition, the standard TIMES objective function, **EQ_OBJ**, is augmented by the present value of the damage costs, as defined by the equation EQ_OBJDAM.

We now give the formulations of these constraints.

:::{admonition} Reminder
The Damage Cost Functions are activated at run time from the data handling system, which in turn sets the switch `$SET DAMAGE LP`/`NLP`/`NO`.
:::

```{list-table} Constraints specific to damage costs (in the GAMS file eqdamage.mod).
:name: dam-constraints
:header-rows: 1

* - Constraints (Indexes)
  - Constraint Description
* - EQ_DAMAGE (r,t,c)
  - The balance equation between the stepped emission variables and the total emissions in each period.
* - EQ_OBJDAM (r,cur) 
  - The total discounted damage costs by region, which will be added as a component to the objective function.
```

## EQ_DAMAGE(r,t,c)

**Description:** Allocates the total amount of emission indicator in period **t** to cost steps.

**Purpose:** This constraint allocates the total amount of emission indicator c to the cost steps of the linearized / non-linear damage cost functions in each period ***t***.

> This equation is generated in each time period for all emission indicators considered.

**Units:** Units of the emission commodity **c**.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Remarks**:

- The damage costs can be defined either on the net production (VAR_COMNET) or the gross production (VAR_COMPRD) of the commodity c. By default the damage costs are applied to the NET amount, unless $DAM\_ELAST_{ r,c,'N'}$ is also specified. $DAM\_ELAST_{r,c,'N'}$ defines a multiplier for the Base prices to be added to the damage cost function, when it is to be applied to the gross production.
- The internal parameter $DAM\_COEF_{r,t,c,s}$ is set to the base prices, if $DAM\_ELAST_{r,c,'N'}$ is specified, and otherwise to 1.

**Equation:**

$$EQ\_DAMAGE_{r,t,c} \ni \left(rtc_{r,t,c} \land \exists(cur):DAM\_COST_{r,t,c,cur} \right)$$

$$\sum_{(jj,bd) \in dam\_num_{r,c,jj,bd}}
\sum_{j \leq jj}VAR\_DAM_{r,t,c,bd,j}
\left\{ = \right\}
\sum_{com\_ts_{r,c,ts}} 
\left (\begin{aligned}
& DAM\_COEF_{r,t,c,ts} \times \\
& \left (\begin{aligned}
& VAR\_COMNET_{r,t,c,ts} \space if \space DAM\_ELAST_{r,c,'N'} \space not \space given \\
& VAR\_COMPRD_{r,t,c,ts} \space otherwise
\end{aligned} \right)
\end{aligned} \right)$$

## EQ_OBJDAM(r,cur)

**Description:** Computes the present value of all damage costs by region and currency.

**Purpose:** Defines the variable VAR_OBJ(r,\'OBJDAM\',cur), which represents the total present value of all damage costs in region r, having currency cur. This variable is included in the TIMES objective function.

**Units:** Currency units.

**Type:** *Binding.* The equation is an equality (=) constraint.

**Remarks:**

- The internal parameter $DAM\_SIZE_{r,c,bd}$ represents the sizes of cost steps of the linearized damage cost function, for both directions (bd=LO/UP) and for the middle step (bd=FX), as described above in Section {numref}`%s <b-mathematical-formulations>`.

**Equation:**

$$EQ\_OBJDAM_{r,cur} \ni \left( rdcur_{r,cur} \right)$$

**Case A: Linearized functions**

$${\sum_{(t,c) \in \left\{rtc_{r,t,c}|(DAM\_COST_{r,t} > 0) \right\}} DAM\_COST_{r,t,c,cur} \times OBJ\_PVT_{r,t,cur} \times 
} \\ \\ {\left\lbrack \begin{aligned}
& \sum_{\begin{matrix}
jj \in dam\_num_{r,c,jj,'LO'} \\
j \leq jj
\end{matrix}}{\left( \begin{aligned}
& \frac{VAR\_DAM_{r,t,c,'LO',j}}{DAM\_BQT{Y_{r,c}}^{DAM\_ELAST_{r,c,'LO'}}} \times \\
& \left( \begin{aligned}
& DAM\_BQTY_{r,c} - DAM\_VOC_{r,c,'LO'} + \\
& DAM\_SIZE_{r,c,'LO'} \times (j - 0.5)
\end{aligned} \right)^{DAM\_ELAST_{r,c,'LO'}}
\end{aligned} \right) +} \\
& VAR\_DAM_{r,t,c,'FX',1} \\
& \sum_{\begin{matrix}
jj \in dam\_num_{r,c,jj,'UP'} \\
j \leq ORD(jj)
\end{matrix}}\left( \begin{aligned}
& \frac{VAR\_DAM_{r,t,c,'UP',j}}{DAM\_BQT{Y_{r,c}}^{DAM\_ELAST_{r,c,'UP'}}} \times \\
& \left( \begin{aligned}
& DAM\_BQTY_{r,c} + \frac{DAM\_SIZE_{r,c,'FX'}}{2} + \\
& DAM\_SIZE_{r,c,'UP'} \times (j - 0.5)
\end{aligned} \right)^{DAM\_ELAST_{r,c,'UP'}}
\end{aligned} \right)
\end{aligned} \right\rbrack
} \\ \\ {\left\{ = \right\}
} \\ \\ {VAR\_OBJ_{r,'OBJDAM',cur}}$$

**\
Case B: Non-linear functions**

$${\sum_{(t,c) \in \left\{ rtc_{r,t,c}|(DAM\_COST_{r,t} > 0) \right\}}{DAM\_COST_{r,t,c,cur} \times OBJ\_PVT_{r,t,cur}} \times 
} \\ \\ {\left\lbrack \begin{aligned}
& \\
& \frac{\left( \begin{aligned}
& \left( \begin{aligned}
& VAR\_DAM_{r,t,c,'LO',j} + \\
& DAM\_BQTY_{r,c} - DAM\_VOC_{r,c,'LO'}
\end{aligned} \right)^{\left( DAM\_ELAST_{r,c,'LO'} + 1 \right)} - \\
& \left( DAM\_BQTY_{r,c} - DAM\_VOC_{r,c,'LO'} \right)^{\left( DAM\_ELAST_{r,c,'LO'} + 1 \right)}
\end{aligned} \right)}{DAM\_BQT{Y_{r,c}}^{DAM\_ELAST_{r,c,'LO'}} \times \left( DAM\_ELAST_{r,c,'LO'} + 1 \right)} + \\
& \\
& \frac{\left( \begin{aligned}
& \left( VAR\_DAM_{r,t,c,'UP',j} + DAM\_BQTY_{r,c} \right)^{\left( DAM\_ELAST_{r,c,'UP'} + 1 \right)} - \\
& \left( DAM\_BQTY_{r,c} \right)^{\left( DAM\_ELAST_{r,c,'UP'} + 1 \right)}
\end{aligned} \right)}{DAM\_BQTY_{r,c}^{DAM\_ELAST_{r,c,'UP'}} \times \left( DAM\_ELAST_{r,c,'UP'} + 1 \right)}
\end{aligned} \right\rbrack
} \\ \\ {\left\{ = \right\}
} \\ \\ {VAR\_OBJ_{r,'OBJDAM',cur}}$$
