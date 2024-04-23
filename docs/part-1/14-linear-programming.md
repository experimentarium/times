# Appendix B: Linear Programming complements

This section is not strictly needed for a basic understanding of the TIMES model and may be skipped a first reading. However, it provides additional insight into the microeconomics of the TIMES equilibrium. In particular, it contains a review of the theoretical foundation of Linear Programming and Duality Theory. This knowledge may help the user to better understand the central role shadow prices and reduced costs play in the economics of the TIMES model. More complete treatments of Linear Programming and Duality Theory may be found in several standard textbooks such as Chvátal (1983) or Hillier and Lieberman (1990 and subsequent editions). Samuelson and Nordhaus (1977) contains a treatment of micro-economics based on mathematical programming.

## A brief primer on Linear Programming and Duality Theory

### Basic definitions

In this subsection, the superscript *t* following a vector or matrix represents the transpose of that vector or matrix. A Linear Program may always be represented as the following *Primal Problem* in canonical form:

> $Max \ \ c^tx$ (14-1)

s.t. $Ax ≤ b$ (14-2)

> $x ≥ 0$ (14-3)

where $x$ is a vector of *decision variables*, $c^tx$ is a linear function representing the *objective* to maximize, and $Ax ≤ b$ is a set of inequality *constraints*. Assume that the LP has a finite optimal solution, $x$.

Then each decision variable, $x_j^*$ falls into one of three categories. $x_j^*$ may be:

- equal to its lower bound (as defined in a constraint), or
- equal to its upper bound, or
- strictly between the two bounds.

In the last case, the variable $x_j^*$ is called *basic*. Otherwise it is *non-basic*.

For each primal problem, there corresponds a *Dual problem* derived as follows:

> $Min \ \  b^ty$ (14-4)

s.t. $A^ty ≥ c$ (14-5)

> $y ≥ 0$ (14-6)

Note that the number of dual variables equals the number of constraints in the primal problem. In fact, each dual variable $y_i$ may be assigned to its corresponding primal constraint, which we represent as: $A_ix ≤ b_i$, where $A_i$ is the $i^{th}$ *row of matrix A*.

### Duality Theory

Duality theory consists mainly of three theorems[^48]: weak duality, strong duality, and complementary slackness.

*Weak Duality Theorem*

If $x$ is any feasible solution to the primal problem and $y$ is any feasible solution to the dual, then the following inequality holds:

> $c^tx≤ b^ty$ (14-7)

The weak duality theorem states that the value of a feasible dual objective is never smaller than the value of a feasible primal objective. The difference between the two is called the *duality gap* for the pair of feasible primal and dual solutions $(x,y)$.

*Strong duality theorem*

If the primal problem has a *finite, optimal* solution $x^*$, then so does the dual problem ($y^*$), and both problems have the same optimal objective value (their duality gap is zero):

$c^tx^* = b^ty^*$ (14-8)

Note that the optimal values of the dual variables are also called the *shadow prices* of the primal constraints.

*Complementary Slackness theorem*

At an optimal solution to an LP problem:

- If $y_i^*$ is $> 0$ then the corresponding primal constraint is satisfied at equality (i.e. $A_ix^* = b_i$ and the $i^{th}$ primal constraint is called *tight*. Conversely, if the $i^{th}$ primal constraint is *slack* (not tight), then $y_i^* = 0$,
- If $x_j^*$ is basic, then the corresponding dual constraint is satisfied at equality, (i.e. $A_j^ty^* = c_j$, where $A_j^ty^*$ is the $j^{th}$ row of $A^t$, i.e. the $j^{th}$ column of $A$. Conversely, if the $j^{th}$ dual constraint is slack, then $x_j^*$ is equal to one of its bounds.

*Remark*: Note however that a primal constraint may have zero slack and yet have a dual equal to 0. And, a primal variable may be non basic (i.e. be equal to one of its bounds), and yet the corresponding dual slack be still equal to 0. These situations are different cases of the so-called degeneracy of the LP. They often occur when constraints are over specified (a trivial case occurs if a constraint is repeated twice in the LP)

## Sensitivity analysis and the economic interpretation of dual variables

It may be shown that if the $j^{th}$ RHS $b_j$ of the primal is changed by an infinitesimal amount $d$, and if the primal LP is solved again, then its new optimal objective value is equal to the old optimal value plus the quantity $y_j^*.d$, where $y_j^*$ is the *optimal dual variable value*.

Loosely speaking[^49], one may say that the partial derivative of the optimal primal objective function's value with respect to the RHS of the $i^{th}$ primal constraint is equal to the optimal shadow price of that constraint.

### Economic interpretation of the dual variables

If the primal problem consists of maximizing the surplus (objective function $c^tx^*$), by choosing an activity vector $x*$, subject to upper limits on several resources (the $b$ vector) then:

- Each $a_{ij}$ coefficient of the dual problem matrix, $A$, then represents the consumption of resource $b_j$ by activity $x_i$;
- The optimal dual variable value $y_j$ is the unit price of resource $j$, and
- The total optimal surplus derived from the optimal activity vector, $x^*$, is equal to the total value of all resources, $b$, priced at the optimal dual values $y^*$ (strong duality theorem).

Furthermore, each dual constraint $A^t_jy^* ≥ c_j$  has an important economic interpretation. Based on the Complementary Slackness theorem, if an LP solution $x^*$ is optimal, then for each $x^*_j$ that is not equal to its upper or lower bound (i.e. each basic variable $x^*_j$), there corresponds a *tight* dual constraint $y^*A'_j = c_j$, which means that the revenue coefficient $c_j$ must be exactly equal to the cost of purchasing the resources needed to produce one unit of $x_j$. *In economists' terms, *marginal cost equals marginal revenue, and both are equal to the market price of $x^*_j$. If a variable is not basic, then by definition it is equal to its lower bound or to its upper bound. In both cases, the unit revenue $c_j$ need not be equal to the cost of the required resources. The technology is then either non-competitive (if it is at its lower bound) or it is super competitive and makes a surplus (if it is at its upper bound).

*Example*: The optimal dual value attached to the balance constraint of commodity $c$ represents the change in objective function value resulting from one additional unit of the commodity. This is precisely the internal unit price of that commodity.

### Reduced surplus and reduced cost

In a maximization problem, the difference $y*A'_j - c_j$ is called the *reduced surplus* of technology $j$, and is available from the solution of a TIMES problem. It is a useful indicator of the competitiveness of a technology, as follows:

- If $x^*_j$ is at its lower bound, its unit revenue $c_j$ is *less* than the resource cost (i.e. its reduced surplus is positive). The technology is not competitive (and stays at its lower bound in the equilibrium);
- If $x^*_j$ is at its upper bound, revenue $c_j$ is *larger* than the cost of resources (i.e. its reduced surplus is negative). The technology is super competitive and produces a surplus; and
- If $x^*_j$ is basic, its reduced surplus is equal to 0. The technology is competitive but does not produce a surplus.

We now restate the above summary in the case of a Linear Program that minimizes cost subject to constraints:

> $Min \ \  c^tx^*$

s.t. $Ax ≥ b$

> $x ≥ 0$

In a minimization problem (such as the usual formulation of TIMES), the difference $c_j - y^*A'_j$ is called the *reduced cost* of technology $j$. The following holds:

- If $x^*_j$ is at its lower bound, its unit cost $c_j$ is *larger* than the value created (i.e. its reduced cost is positive). The technology is not competitive (and stays at its lower bound in the equilibrium);
- if $x^*_j$ is at its upper bound, its cost $c_j$ is *less* than the value created (i.e. its reduced cost is negative). The technology is super competitive and produces a profit; and
- if $x^*_j$ is basic, its reduced cost is equal to 0. The technology is competitive but does not produce a profit

The reduced costs/surpluses may thus be used to rank all technologies, *including those that are not selected by the model.*


------------

[^48]: Their proofs may be found in the textbooks on Linear Programming already referenced.

[^49]: Strictly speaking, the partial derivative may not exist for some values of the RHS, and may then be replaced by a directional derivative (see Rockafellar 1970).
