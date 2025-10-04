(a-equations)=
# Equations

There are three blocks of definitional equations: the first block of equations calculates the global emissions of GHG (either all in CO<sub>2</sub> eq., or separately for CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O) as well as the total (linearized) radiative forcing, the next block calculates the concentrations of the greenhouse gases in the reservoirs, and the third block calculates the atmospheric temperature and lower ocean temperature at period t.

In addition, there is a generic block of equations expressing the upper bounding of the five climate quantities discussed in subsection {numref}`%s <a-upport-bounds-on-climate-variablaes>`. This generic equation is generated as many times as an upper bound on any climate variable is specified by the user, and is not generated if no upper bound is specified.

We now give the formulations of these constraints.

:::{admonition} Reminder

The Climate Module formulation is activated at run time from the data handling system, which in turn set the `$SET CLI YES` switch.
:::

General notation:

- *D(t):* duration of period *t, t=1 to T*
- *B(t):* first year in period *t, t=1 to T*
- *m(t):* milestone year of period t (approximate middle year of period, defined as $m(t) = B(t) + \left\lfloor (D(t) - 1)/2 \right\rfloor$)
- *y:* designates a year, while *t* designates a period (ranging from 1 to T)
- *Υ:* designates the calibration year, which can be chosen by the user to be either *B*(1)--1, *m*(1)--1, or *m*(1)*,* see section {numref}`%s <a-calibration>` above.

```{list-table} Climate Module specific constraints (all in the GAMS file equ_ext.cli).
:name: cli-specific-constraints
:header-rows: 1

* - Constraints (Indexes)
  - Constraint Description
* - EQ_CLITOT (cm_var,t)
  - Defines the amount of global greenhouse gas emissions in each period; defines the amount of total radiative forcing from the greenhouse gas concentrations in each period *t*.
* - EQ_CLICONC (cm_var,cm_box,t)
  - Defines the mass of each greenhouse gas *cm_var* in each reservoir *cm_box* at the end of the milestoneyr **m(t)** of period *t*.
* - EQ_CLITEMP (cm_box,t)
  - Defines the temperature increase in the each reservoir *cm_box* (the lower atmosphere and the lower ocean layer) over its pre-industrial temperature measured at the end of milestoneyr **m(t)** of period *t*.
* - EQ_CLIMAX (y,cm_var)
  - Imposes an upper bound on any or all of the climate variables *cm_var* (*CO2-GTC, CH4-MT, N2O-MT, CO2-ATM, CO2-PPM, CH4-PPB, N2O-PPB, FORCING, DELTA-ATM)*, at any desired year *y*, according to the user-defined input parameter CM_MAXC.
```

## EQ_CLITOT(cm_var,t)

**Description:** Defines the total amount of aggregate climate indicator in period t.

**Purpose:** This constraint defines the amount of global greenhouse gas emissions in each period and the amount of total radiative forcing from the greenhouse gas concentrations in each period *t*.

This equation is generated in each time period for all indicators considered.

**Units:** Global emission units (GtC, Mt) or forcing units (W/m<sup>2</sup>)

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variables represent the marginal prices of the global emissions / forcing (when undiscounted).

**Remarks**:

- For CO<sub>2</sub>, the linear forcing function parameters $CM\_LINFOR_{t,cm\_emis,'FX'}$ and $CM\_LINFOR_{t,cm\_emis,'N'}$ are automatically calculated by the model generator from any user-defined $CM\_LINFOR_{t,cm\_emis,'LO'}$ and $CM\_LINFOR_{t,cm\_emis,'UP'}$.

**Equation:**

$$EQ\_CLITOT_{cm\_tkind,t}\forall\left\lbrack \left( t \in milestonyr \right) \right\rbrack$$

$${\sum_{\begin{aligned}
 & cm\_tkind \in cm\_emis \\ \\
 & (r,c,s) \in rtcs\_varc_{r,c,t,s}
 \end{aligned}}{VAR\_COMNET_{r,t,c,s} \times CM\_GHGMAP_{r,c,cm\_tkind}}
} \\ \\ {\sum_{cm\_emis_{cm\_tkind}}
\left (\begin{aligned}
& CM\_LINFOR_{t,cm\_emis,'N'} \times \\
& \left (\sum_{\begin{aligned}
& cm\_atbox_{cm\_emis,cm\_box} \\
& cm\_boxmap_{cm\_emis,cm\_var,cm\_box}
\end{aligned}}
{VAR\_CLIBOX_{cm\_var}} \right) \\
& CM\_LINFOR_{t,cm\_emis,'FX'}
\end{aligned} \right) + 
} \\ \\ {+ CM\_EXOFORC_{t}
} \\ \\ {\left\{ = \right\}
} \\ \\ {VAR\_CLITOT_{cm\_tkind,t}}$$

## EQ_CLICONC(cm_var,cm_box,t)

**Description:** Defines the reservoir-specific amounts of concentration indicator in each period.

**Purpose:** Defines the dynamic relationship between emissions and the concentration in the reservoirs modelled for each greenhouse gas, such that the amount of concentration in reservoir *i* and period *t* may depend on the amounts of concentrations in any reservoir *k* in period *t--1*, and on the emissions in period *t*.

**Units:** Global emission units (GtC, Mt).

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variable of this constraint in the solution is of little interest.

**Remarks:**
- See expressions for the transfer matrices on next page.
- The equations beyond the last milestone year m(T) are similar, but omitted here.

**Equation:**

$$EQ\_CLICONC_{cm\_emis,cm\_box,t}\forall\left\lbrack \left( t \in milestonyr \right) \right\rbrack$$

$${\sum_{cm\_boxmap_{cm\_emis,cm\_var,cm\_box2}}{VAR\_CLIBOX_{cm\_var,t - 1} \times CM\_AA_{cm\_emis,t,cm\_box,cm\_box2}} + 
} \\ \\ {CM\_BB_{cm\_emis,t,cm\_box} \times VAR\_CLITOT_{cm\_emis,t} + 
} \\ \\ {CM\_CC_{cm\_emis,t,cm\_box} \times VAR\_CLITOT_{cm\_emis,t - 1} + 
} \\ \\ {\sum_{\begin{matrix}
miyr\_1_{t} \\
cm\_boxmap_{cm\_emis,cm\_var,cm\_box2}
\end{matrix}}{CM\_CONST_{cm\_var} \times CM\_AA_{cm\_emis,t,cm\_box,cm\_box2}}
} \\ \\ {\left\{ = \right\}
} \\ \\ {\sum_{cm\_boxmap_{cm\_emis,cm\_var,cm\_box}}{VAR\_CLIBOX_{cm\_var,t}}}$$

$${CM\_AA_{cm\_emis,t,i,j} = \left\{ A_{ij}(t) \right\} = \space PHI^{n(t)}(PHI^{0} = I), \space \text{where} \space
} \\ \\ {PHI\text{  is the 3} \times \text{3 matrix}:\begin{bmatrix}
(1 - PHI\_AT\_UP) & PHI\_UP\_AT & 0 \\
PHI\_AT\_UP & (1 - PHI\_U\_AT - PHI\_UP\_LO) & PHI\_LO\_UP \\
0 & PHI\_UP\_LO & (1 - PHI\_LO\_UP)
\end{bmatrix}
} \\ \\ {CM\_BB_{cm\_emis,t,i} = \left\{ BB_{i1}(t) \right\}\text{  is the first column of the matrix: }
} \\ \\ {BB(t) = \space \sum_{i = 0}^{p(t) - 1}{PHI^{i}} \space if \space p(t) \geq 1
} \\ \\ {BB(t) = 0 \space if \space p(t) = 0
} \\ \\ {CM\_CC_{cm\_emis,t,i} = \left\{CC_{i1}(t) \right\} \text{  is the first column of the matrix :}
} \\ \\ {CC(t) = \ \sum_{i = p(t)}^{n(t) - 1}{PHI^{i}} \space if \space n(t) \geq p(t) + 1
} \\ \\ {CC(t) = 0 \space if \space n(t) = p(t)
} \\ \\ {p(t) \space = \space \left\lfloor \frac{D(t) + 1}{2} \right\rfloor,n(t) \space = \space m(t) - m(t - 1) \space if \space t \neq 1,\space
} \\ \\ {p(t) \space = \space m(t) - \Upsilon,n(t) \space = \space p(t) \space if \space t = 1
} \\ \\ {D(t) \text{  is the number of years in period }t,and m(t)\text{ is the middle year of period}\space t\text{ defined as} \space
} \\ \\ {m(t) = B(t) + \left\lfloor \frac{D(t) - 1}{2} \right\rfloor
} \\ \\ {\left\lfloor x \right\rfloor\ \text{ denotes the largest integer smaller than or equal to} \space x}$$

## EQ_CLITEMP(cm_var,cm_box,t)

**Description:** Defines the reservoir-specific amounts of temperature indicator in each period.

**Purpose:** Defines the dynamic relationship between forcing and the temperature increase in the reservoirs modelled, such that the amount of temperatures increase in reservoir *i* and period *t* may depend on the amounts of temperature increase in any reservoir *k* in period *t--1*, and on the radiative forcing in period *t*.

**Units:** Global temperature units (°C).

**Type:** *Binding.* The equation is an equality (=) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be zero in a feasible solution.

*Dual variable:* The dual variable of this constraint in the solution is of little interest.

**Remarks:**
- See expressions for the transfer matrices on next page.
- The equations for years beyond m(T) are similar, but omitted here.

**Equation:**

$$EQ\_CLITEMP_{cm\_box,t}\forall\left\lbrack \left( t \in milestonyr \right) \right\rbrack$$

$${\sum_{cm\_boxmap_{'FORCING',cm\_var,cm\_box2}}{VAR\_CLIBOX_{cm\_var,t - 1} \times CM\_AA_{'FORCING',t,cm\_box,cm\_box2}} + 
} \\ \\ {CM\_BB_{'FORCING',t,cm\_box} \times VAR\_CLITOT_{'FORCING',t} + 
} \\ \\ {CM\_CC_{'FORCING',t,cm\_box} \times VAR\_CLITOT_{'FORCING',t - 1} + 
} \\ \\ {\sum_{\begin{matrix}
miyr\_1_t \\
cm\_boxmap_{'FORCING',cm\_var,cm\_box2}
\end{matrix}}{CM\_CONST_{cm\_var} \times {CM\_AA_{'FORCING,t,cm\_box,cm\_box2}}}
} \\ \\ {\left\{ = \right\}
} \\ \\ {\sum_{cm\_boxmap_{'FORCING',cm\_var,cm\_box}}{VAR\_CLIBOX_{cm\_var,t}}}$$

$${CM\_AA_{'FORCING',t,i,j} = \left \{ A_{ij}(t) \right\} = \space PHI^{n(t)}(PHI^{0} = I), \space \text{where} \space
} \\ \\ {PHI \text{  is the 3} \times \text{3 matrix}:\begin{bmatrix}
(1 - SIGMA1 \times (LAMBDA + SIGMA2) & SIGMA1 \times SIGMA2 & 0 \\
SIGMA3 & (1 - SIGMA3) & 0 \\
0 & 0 & 0
\end{bmatrix}
} \\ \\ {CM\_BB_{'FORCING',t,i} = \left \{ BB_{i1}(t) \right\} \text{  is the first column of the matrix: }
} \\ \\ {BB(t) = SIGMA1 \times \space \sum_{i = 0}^{n(t) - 1}{\frac{n(t) - i}{n(t)} \times PHI^{i}} \space
} \\ \\ {CM\_CC_{'FORCING',t,i} = \left \{ CC_{i1}(t) \right \} \text{  is the first column of the matrix :}
} \\ \\ {CC(t) = \space SIGMA1 \times \sum_{i = 0}^{n(t) - 1}{\frac{i}{n(t)} \times PHI^{i}}
} \\ \\ {n(t) \space = \space m(t) - m(t - 1) \space if \space t \neq 1, \space
} \\ \\ {n(t) \space = \space m(t) - Y \space if \space t = 1
} \\ \\ {D(t) \text{  is the number of years in period } t, \text{ and } m(t) \text{ is the middle year of period} \space t\text{ defined as}
} \\ \\ {m(t) = B(t) + \left\lfloor \frac{D(t) - 1}{2} \right\rfloor
} \\ \\ {\left\lfloor x \right\rfloor\ \text{ denotes the largest integer smaller than or equal to} \space x}$$

## EQ_CLIMAX(y,cm_var)

**Description:** Constraint that sets an upper bound on the climate indicator in a give year.

**Purpose:** To set an upper bound for a climate indicator variable in any desired year y. The variables that can be bounded are the total global emissions and the total radiative forcing (VAR_CLITOT), the atmospheric concentrations of greenhouse gases (sum of VAR_CLIBOX variables), and the increase in atmospheric temperature (VAR_CLIBOX). The bounds can be specified by using the *CM_MAXC<sub>y,cm_var</sub>* attribute.

**Units:** Units of the variable(s) bounded.

**Type:** *Binding.* The equation is a less than or equal to inequality (≤) constraint.

**Interpretation of the results:**

*Primal:* The level of this constraint must be less than or equal to zero in a feasible solution.

*Dual variable:* The dual variable of this constraint in the solution may be used to derive the marginal price of the climate indicator constrained (when undiscounted; global dual values are, ex officio, reported without undiscounting, as no well-defined "global discount factors" exist, only regional ones).

**Remarks:**
- The *CM_MAXC* bounds defined on CO2-ATM are automatically converted into equivalent bounds on CO2-PPM.
- The coefficients $\alpha_y$ and $\beta_y$ in the equations are such that $y = \alpha_y(m(t)-y) + \beta_y(y-m(t-1))$, for all $y$ in the range $m(t-1) < y ≤ m(t)$.

**Equation:**

$$EQ\_CLIMA{X_{y,cm\_var}}\forall\left\lbrack \left\{ (y,cm\_{var})|CM\_MAXC_{y,cm\_var} \right\} \right\rbrack$$

**Case A. For total emissions, up to m(T)**

$${\alpha_{y} \times VAR\_CLITOT_{cm\_emis,t - 1} + \beta_{y} \times VAR\_CLITOT_{cm\_emis,t}
} \\ \\ {\leq CM\_MAXC_{y,cm\_emis}}$$

**Case B. For atmospheric GHG concentrations, up to m(T)**

$${\sum_{\begin{matrix}
cm\_atbox_{cm\_emis,cm\_box} \\
cm\_boxmap_{cm\_emis,cm\_var,cm\_box}
\end{matrix}}{\alpha_{y} \times VAR\_CLIBOX_{cm\_var,t - 1} + \beta_{y} \times VAR\_CLIBOX_{cm\_var,t}}
} \\ \\ {\leq CM\_MAXC_{y,cm\_var}}$$

**Case C. For total radiative forcing, up to m(T)**

$${\alpha_{y} \times VAR\_CLITOT_{'FORCING',t - 1} + \beta_{y} \times VAR\_CLITOT_{'FORCING',t}
} \\ \\ {\leq CM\_MAXC_{y,'FORCING'}}$$

**Case D. For increase in global atmospheric temperature, up to m(T):**

$${\sum_{cm\_boxmap_{'FORCING',cm\_var,'ATM'}}{\alpha_{y} \times VAR\_CLIBOX_{cm\_var,t - 1} + \beta_{y} \times VAR\_CLIBOX_{cm\_var,t}}
} \\ \\ {\leq CM\_MAXC_{y,cm\_var}}$$

**Case E. For atmospheric GHG concentrations, beyond m(T):**

$$\sum_{\begin{matrix}
cm\_atbox_{cm\_emis,cm\_box} \\
cm\_boxmap_{cm\_emis,cm\_var,cm\_box}
\end{matrix}}{VAR\_CLIBOX_{cm\_var,y}}\quad \leq \quad CM\_MAXC_{y,cm\_var}$$

**Case F. For total radiative forcing, beyond m(T):**

$$VAR\_ CLITOT_{'FORCING',y}\quad \leq \quad CM\_ MAXC_{y,'FORCING'}$$

**Case G. For increase in global atmospheric temperature, beyond m(T):**

$$\sum_{cm\_boxmap_{'FORCING',cm\_var,'ATM'}}{VAR\_CLIBOX_{cm\_var,y}}\quad \leq \quad CM\_MAXC_{y,cm\_var}$$
