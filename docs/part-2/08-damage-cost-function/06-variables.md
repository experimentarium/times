(b-variables)=
# Variables

There are only two sets of new variables in the damage cost formulation, VAR_DAM and VAR_OBJDAM, which are shown below in {numref}`dam-variables`. The variables VAR_DAM represent the steps in the emissions in each period. In the linearized formulation, there are DAM_STEP(\...,\'LO\') number of step variables on the lower side and DAM_STEP(\...\'UP\') number of step variables on the higher side of emissions. In addition, one step variable of type \'FX\' corresponds to the middle step that includes the reference level of emissions, and an optional additional step variable of type \'FX\' corresponds to the zero-damage fraction of emissions, as defined by the difference between DAM_BQTY(..) and DAM_VOC(\...,\'LO\').

The variables VAR_OBJDAM represent the total discounted damage costs by region. The undiscounted costs in each period described in Section {numref}`%s <b-mathematical-formulations>` are discounted and summed over all periods and emissions in each region. As emissions are in TIMES assumed to be constant within each period, damage costs are likewise assumed to be constant within each period.

```{list-table} Model variables specific to the Damage Cost Functions.
:name: dam-variables
:header-rows: 1

* - Variable (Indexes)
  - Variable Description
* - VAR_DAM (r,t,c,bd,j)
  - The emission step variable for the damage function of commodity **c** in region **r**, for each step **j** in each direction **bd**.
* - VAR_OBJ (r,\'OBJDAM\',cur)
  - The variable is equal to the sum of the total discounted damage costs in each region **r** with currency **cur**.
```

## VAR_DAMAGE(r,t,c,bd,j)

**Description:** The amount of emission indicator **c** at cost step **j** in direction **bd**, in period **t**.

**Purpose:** This variable tracks the amount of an emission indicator by cost step and period, in both the lower and upper direction from the reference level.

**Occurrence:** The variable is generated for emission indicator that has damage costs specified, whenever the damage cost functions are included in the objective function.

**Units:** Units of the emission commodity **c**.

**Bounds:** This variable cannot be directly bounded by the user.

## VAR_OBJ(r,\'OBJDAM\',cur)

**Description:** The total present value of damage costs by region.

**Purpose:** This variable is included in the objective function in order to include damage costs in the objective when requested by the user.

**Occurrence:** This variable is generated for each region when damage cost functions are included in the objective function

**Units:** Currency units used for damage functions.

**Bounds:** This variable cannot be directly bounded by the user.
