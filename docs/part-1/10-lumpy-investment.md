# The Lumpy Investment extension

In some cases, the linearity property of the TIMES model may become a
drawback for the accurate modeling of certain investment decisions.
Consider for example a TIMES model for a relatively small community such
as a city. For such a scope the *granularity* of some investments may
have to be taken into account. For instance, the size of an electricity
generation plant proposed by the model would have to conform to an
implementable minimum size (it would make no sense to decide to
construct a 50 MW nuclear plant). Another example for multi-region
modeling might be whether or not to build cross-region electric grid(s)
or gas pipeline(s) in discrete size increments. Processes subject to
investments of only specific size increments are described as "lumpy"
investments.

For other types of investments, size does not matter: for instance the
model may decide to purchase 10,950.52 electric cars, which is easily
rounded to 10,950 without any serious inconvenience, especially since
this number is an annual figure. The situation is similar for a number
of residential or commercial heating devices; or for the capacity of
wind turbines; or of industrial boilers; in short, for any technologies
with relatively small minimum feasible sizes. Such technologies would
not be candidates for treatment as "lumpy" investments.

This chapter describes the basic concept and mathematics of lumpy
investment option, whereas the implementation details are available in
Part II, section 6.3.24. We simply note here that this option, while
introducing new variables and constraints, does not affect existing
TIMES constraints.

It is the user's responsibility to decide whether or not certain
technologies should respect the minimum size constraint, weighing the
pros and cons of so doing. This chapter explains how the TIMES LP is
transformed into a Mixed Integer Program (MIP) to accommodate minimum or
multiple size constraints, and states the consequences of so doing on
computational time and on the interpretation of duality results.

The lumpy investment option available in TIMES is slightly more general
than the one described above. It insures that investment in technology
***k*** is equal to one of a finite number ***N*** of pre-determined
sizes: ***0, S~1~(t), S~2~(t), ...,S~N~(t).*** This is useful when
several typical plant sizes are feasible in the real world. As implied
by the notation, these discrete sizes may be different at different time
periods. Note that by choosing the ***N*** sizes as the successive
multiples of a fixed number ***S***, it is possible to invest (perhaps
many times) in a technology with fixed standard size.

Imposing such a constraint on an investment is unfortunately impossible
to formulate using standard LP constraints and variables. It requires
the introduction of *integer variables* into the formulation. The
optimization problem resulting from the introduction of integer
variables into a Linear Program is called a Mixed Integer Program (MIP).

## Formulation and solution of the Mixed Integer Linear Program

Typically, the modeling of a lumpy investment involves Integer
Variables, i.e. variables whose values may only be non-negative integers
(0, 1, 2, ...). The mathematical formulation is as follows:

$${VAR\_ NCAP(p,t) = \sum_{i = 1}^{N}{S_{i}(p,t) \times}Z_{i}(p,t)each ⥂ t = 1,..,T
}{with
}
{Z_{i}(p,t) = 0or1
}
{and
}
{\sum_{i = 1}^{N}Z_{i}(p,t) \leq 1}$$

The second and third constraints taken together imply that at most one
of the ***Z*** variables is equal to 1 and all others are equal to zero.
Therefore, the first constraint now means that ***NCAP*** is equal to
one of the preset sizes or is equal to 0, which is the desired result.

Although the formulation of lumpy investments *looks* simple, it has a
profound effect on the resulting optimization program. Indeed, MIP
problems are notoriously more difficult to solve than LPs, and in fact
many of the properties of linear programs discussed in the preceding
chapters do not hold for MIPs, including duality theory, complementary
slackness, etc. Note that the constraint that *Z(p,t)* should be 0 or 1
departs from the *divisibility* property of linear programs. This means
that the *feasibility domain* of integer variables (and therefore of
some investment variables) is no longer contiguous, thus making it
vastly more difficult to apply purely algebraic methods to solve MIP's.
In fact, practically all MIP solution algorithms make use (at least to
some degree) of partial enumerative schemes, which tend to be time
consuming and less reliable[^36] than the algebraic methods used in LP.

The reader interested in more technical details on the solution of LPs
and of MIPs is referred to references (Hillier and Lieberman, 1990,
Nemhauser et al. 1989). In the next section we shall be content to state
one important remark on the interpretation of the dual results from MIP
optimization.

## Discrete early retirement of capacity

The discrete retirement of capacity that was briefly mentioned in
section 5.4.11 requires a treatment quite similar to that of discrete
addition to capacity presented here. The complete mathematical
formulation mimics that presented above, and is fully described in Part
II, section 6.3.26, of the TIMES documentation.

## Important remark on the MIP dual solution (shadow prices)

Using MIP rather than LP has an important impact on the interpretation
of the TIMES shadow prices. Once the optimal MIP solution has been
found, it is customary for MIP solvers to fix all integer variables at
their optimal (integer) values, and to perform an additional iteration
of the LP algorithm, so as to obtain the dual solution (i.e. the shadow
prices of all constraints). However, the interpretation of these prices
is different from that of a pure LP. Consider for instance the shadow
price of the natural gas balance constraint: in a pure LP, this value
represents the price of natural gas. In MIP, this value represents the
price of gas *conditional on having fixed the lumpy investments at their
optimal integer values.* What does this mean? We shall attempt an
explanation via one example: suppose that one lumpy investment was the
investment in a gas pipeline; then, *the gas shadow price will not
include the investment cost of the pipeline, since that investment was
fixed when the dual solution was computed*.

In conclusion, when using MIP, only the primal solution is fully
reliable. In spite of this major caveat, modeling lumpy investments may
be of paramount importance in some instances, and may thus justify the
extra computing time and the partial loss of dual information.


------------

[^36]: A TIMES LP program of a given size tends to have fairly constant solution time, even if the database is modified. In contrast, a TIMES MIP may show some erratic solution times. One may observe reasonable solution times (although significantly longer than LP solution times) for most instances, with an occasional *very* long solution time for some instances. This phenomenon is predicted by the theory of complexity as applied to MIP, see Papadimitriou and Stieglitz (1982).
