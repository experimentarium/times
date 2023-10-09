# The TIMES source code and the model run process

As discussed in the previous section, the heart of TIMES is embodied in
the GAMS source code, comprised of the matrix generator that digests the
input data prepared from ANSWER or VEDA-FE and prepares the mathematical
representation of the model instance, an optimizer to solve the
resulting mathematical programming problem, and a report writer that
post-processes the solution and prepares results files for ANSWER and
VEDA-BE. It is this collection of GAMS source code routines that
correspond to the TIMES model, where each TIMES model run proceeds
through the appropriate path in the source code based upon the user
specified runtime switches, described in Section 3, and the provided
input data.

For the most part, this process is seamless to the user, as the model
management shells extract the scenario data and prepare ASCII text files
in the layout required by GAMS, set up the top level GAMS control file,
and initiate the model run (in a Command Prompt box). GAMS then compiles
the source and data, constructs the model, invokes the solvers, and
dumps the model results for importing back into the model management
environment. However, knowledge of the run process and the files
produced along the way can be helpful in diagnosing model errors (e.g.,
a division by zero may necessitate turning on the source code listing
(\$ONLISTING/\$OFFLIST at the top/bottom of the routine where the error
is reported) to determine which parameter is causing the problem) or if
a user is considering modifying the model formulation to, say, add a new
kind of constraint (note that any such undertaking should be closely
coordinated with ETSAP).

## Overview of the model run process

Once a model is readied, a run can be initiated from the model
management systems by means of the Case Manager in VEDA-FE or the Run
Model option on the ANSWER Home screen. In both systems the user
assembles the list of scenarios to comprise the model run, taking care
to ensure that the order of the scenarios is such that all RES
components are first declared (that is their item name and set
membership specified) and then assigned data.

In the model management shells, the user can also adjust the TIMES model
variant, run control switches, and solver options. For VEDA-FE this is
done through the Case Manager, via the Control Panel, RUNFile template,
and solver settings. Figure 4 shows an example of the VEDA-FE Control
Panel. See Part IV for more on the use of the Case Manager in VEDA-FE.

In ANSWER, the Run Model button brings up the Run Model Form, from which
the model variant and most run control switches can be set. (The others
need to be set using the Edit GAMS Control Options feature.) However the
\<Solver\>.OPT file needs to be handled manually outside of ANSWER. See
the separate ANSWER documentation for more details on these ANSWER
facilities.

When a model run is initiated, three kinds of files are created by VEDA
and ANSWER. The first is a Windows command script file VTRUN/ANSRUN.CMD
(for VEDA/ANSWER respectively), which just identifies the run name,
indicates where the source code resides, and perhaps any restart (see
Section 3.8), and then calls the VEDA/ANSWER driver command script
(VT_GAMS/ANS_RUN.CMD). The second is the top-level GAMS command file
\<Case\>.RUN/GEN (for VEDA/ANSWER), which is passed to GAMS to initiate
and control the model run. It sets the model variant, identifies the
Milestone (run) years, lists the scenario data files (DD/DDS) to
include, and invokes the main GAMS routine to have the model actually
assembled mathematically, solved, and reported upon. It is discussed
further in Section . The third group of files comprise the data
dictionary \<scenario\>.DD/DDS file(s), which contain the user input
sets and parameters in the format required by GAMS to fully describe the
energy system to be analyzed.

GAMS is a two pass language, first compiling and then executing. In the
first pass, GAMS reads the input data prepared by ANSWER or VEDA-FE, and
then proceeds to compile the data as well as the actual TIMES source
code to ready it for execution (unless a Runtime license is employed in
which case only the data is compiled).

In the second pass, GAMS then proceeds to execute the complied data and
code to declare the equations and variables that are to make up this
particular TIMES incarnation and generate the appropriate coefficients
for matrix intersection, that is the multiplier for the individual
variables comprising each equation. With the matrix assembled GAMS then
turns over the problem to the solver.

![](media/image4.png){width="3.8583333333333334in"
height="4.28456583552056in"}

[]{#_Ref321326034 .anchor}Figure 4: VEDA-FE Case Manager Control Form

As a result of a model run a listing file (\<Case\>.LST), and a
\<case\>.GDX file (GAMS dynamic data exchange file with all the model
data and results) are created. The \<Case\>.LST file may contain
compilation calls and execution path through the code, an echo print of
the GAMS source code and the input data, a listing of the concrete model
equations and variables, error messages, model statistics, model status,
and solution dump. The amount of information displayed in the listing
file can be adjusted by the user through GAMS options in the
\<Case\>.RUN file.

The \<Case\>.GDX file is an internal GAMS file. It is processed
according to the information provided in the TIMES2VEDA.VDD to create
results input files for the VEDA-BE software to analyze the model
results in the \<case\>.VD\* text files. A dump of the solution results
is also done to the \<case\>.ANT file for importing into ANSWER, if
desired. At this point, model results can be imported into VEDA-BE and
ANSWER respectively for post-process and analysis. More information on
VEDA-BE and ANSWER results processing can be found in Part V and the
separate ANSWER documentation respectively.

In addition to these output files, TIMES may create a file called
QA_CHECK.LOG to inform the user of possible errors or inconsistencies in
the model formulation. The QA_CHECK file should be examined by the user
on a regular basis to make sure no "surprises" have crept into a model.
The content and use of each of these files is discussed further in
Section 2.3.

For the ETSAP Runtime GAMS license, which does not allow for adjustments
to the TIMES source code by users (which in general is not encouraged
anyway), a special TIMES.g00 file is used that contains the declaration
of each variable and equation that is part of the model definition,
thereby initializing the basic model structure.

## The TIMES source code

The TIMES model generator is comprised of a host of GAMS source code
routines, which are simple text files that reside in the user\'s
\\VEDA\\VEDA-FE\\GAMS_SrcTIMESv### folder, as discussed in Section 1.3
(or \\AnswerTIMESv6\\GAMS_SrcTI). Careful naming conventions are
employed for all the source code routines. These conventions are
characterized, for the most part, by prefixes and extensions
corresponding to collections of files handling each aspect of the code
(e.g., set bounds, prepare coefficients, specify equations), as
summarized in Table 2.

  ----------------------------------------------------------------------------
  **Type**        **Nature of the Routine**
  --------------- ------------------------------------------------------------
  **Prefix**      

  **ans**         ANSWER TIMES specific pre-processor code

  **bnd**         set bounds on model variables

  **cal**         calculations performed in support of the preprocessor and
                  report writer

  **coef**        prepare the actual matrix intersection coefficients

  **eq**          equations specification (the actual assembling of the
                  coefficients of the matrix)

  **err**         Error trapping and handling

  **fil**         handles the fundamental
                  interpolation/extrapolation/normalization of the original
                  input data

  **init**        initialize all sets and parameters potentially involved in
                  assembling a TIMES model

  **main**        Top level routines according to the model variant to be
                  solved

  **mod**         the declaration of the equations and variables for each model variant

  **pp**          preprocess routines responsible for preparing the TIMES internal parameters by assembling, interpolating, levelizing, normalizing, and processing the input data to prepare the data structures needed to produce the model coefficients

  **qa**          Quality assurance checking and reporting

  **rpt**         main reporting components performing the calculations needed and assembling the relevant parameters from the model results

  **sol**         components of the results report writer that prepares the solution for outputting

  **solve**       manage the actual call to solve the model (that is the call to invoke the optimizer)

  **uc**          handles the user constraints

  **Extension**   

  **ABS**         Ancillary Balancing Services routines

  **ANS**         ANSWER specific code

  **CLI**         climate module routines

  **CMD**         Windows command scripts to invoke GAMS/GDX2VEDA in order to solve and afterwards dump the model results

  **DEF**         setting of defaults

  **DSC**         discrete (lumpy) investment routines

  **ETL**         endogenous technology learning routines

  **GMS**         lower level GAMS routines to perform interpolation, apply shaping of input parameters, etc.

  **RUN/GEN**     VEDA-FE/ANSWER specific GAMS TIMES command templates for dynamic substitution of the switches and parameters needed at run submission to identify the model variant and other options that will guide the current model run

  **IER**         routines and extensions prepared by the University of Stuttgart (Institute for the Rational Use of Energy, IER) (e.g., for more advanced modeling of CHPs)

  **LIN**         routines related to the alternative objective formulations

  **MOD**         core TIMES routines preparing the actual model

  **MLF**         code related to the MLF implementation of TIMES-MACRO

  **MSA**         code related to the MSA implementation of decomposed TIMES-MACRO

  **RED**         reduction algorithm routines

  **RPT**         report writer routines

  **STC**         code related to stochastics
  **STP**         code related to time-stepped or partially fixed-horizon solution

  **TM**          the core TIMES MACRO code

  **VDA**         routines related to new TIMES features implemented under the VDA extension

  **VDD**         directives for the VEDA-BE result analysis software
  ----------------------------------------------------------------------------

  : []{#_Ref425138160 .anchor}Table 2: TIMES Routines Naming Conventions

Note that these don't cover every single routine in the TIMES source
code folder, but do cover most all of the core routines involved in the
construction and reporting of the model. They guide the steps of the run
process as follows:

-   **GAMS Compile:** As mentioned above, GAMS operates as a two-phase
    > compile then execute system. As such it first reads and assembles
    > all the control, data, and code files into a ready executable;
    > substituting user and/or shell provided values for all GAMS
    > environment switches and subroutine parameter references (the
    > %EnvVar% and %Param% references in the source code) that determine
    > the path through the code for the requested model instance and
    > options desired. If there are inconsistencies in input data they
    > may result in compile-time errors (e.g., \$170 for a domain
    > definition error), causing a run to stop. See Section for more on
    > identifying the source of such errors.

-   **Initialization:** Upon completion of the compile step, all
    > possible GAMS sets and parameters of the TIMES model generator are
    > declared and initialized, then established for this instance of
    > the model from the user's data dictionary file(s)
    > (\<Case\>.DD[^14]). Model units are also initialized using the
    > UNITS.DEF file, which contains the short names for the most common
    > sets of units that are normally used in TIMES models, and which
    > can be adjusted by the user.

-   **Execution:** After the run has been prepared, the maindrv.mod
    > routine controls all the remaining tasks of the model run. The
    > basic steps are as follows.

    -   **Pre-processing:** One major task is the pre-processing of the
        > model input data. During pre-processing control sets defining
        > the valid domain of parameters, equations and variables are
        > generated (e.g., for which periods each process is available,
        > at what timeslice level (after inheritance) is each commodity
        > tracked and does each process operate), input parameters are
        > inter-/extrapolated, and time-slice specific input parameters
        > are inherited/aggregated to the correct timeslice level as
        > required by the model generator.

    -   **Preparation of coefficients:** A core activity of the model
        > generator is the proper derivation of the actual coefficients
        > used in the model equations. In some cases coefficients
        > correspond directly to input data (e.g., FLO_SHAR to the flow
        > variables), but in other cases they must be transformed. For
        > example, the investment cost (NCAP_COST) must be annualized,
        > spread for the economic lifetime, and discounted before being
        > applied to the investment variable (VAR_NCAP) in the objective
        > function (EQ_OBJ), and based upon the technical lifetime the
        > coefficients in the capacity transfer constraint (EQ_CPT**)**
        > are determined to make sure that new investment are accounted
        > for and retired appropriately.

    -   **Generation of model equations:** Once all the coefficients are
        > prepared, the file eqmain.mod controls the generation of the
        > model equations. It calls the individual GAMS routines
        > responsible for the actual generation of the equations of this
        > particular instance of the TIMES model. The generation of the
        > equations is controlled by sets, parameters, and switches
        > carefully assembled by the pre-processor to ensure that no
        > superfluous equations or matrix intersections are generated.

    -   **Setting variable bounds:** The task of applying bounds to the
        > model variables corresponding to user input parameters is
        > handled by the bndmain.mod file. In some cases it is not
        > appropriate to apply bounds directly to individual variables,
        > but instead applying a bound may require the generation of an
        > equation (e.g. the equation EQ(l)\_ACTBND is created when an
        > annual activity bound is specified for a process having a
        > diurnal timeslice resolution).

    -   **Solving the model:** After construction of the actual matrix
        > (rows, columns, intersections and bounds) the problem is
        > passed to an optimizing solver employing the appropriate
        > technique (LP, MIP, or NLP). The solver returns the solution
        > of the optimization back to GAMS. The information regarding
        > the solver status is written by TIMES in a text file called
        > END_GAMS, which allows the user to quickly check whether the
        > optimisation run was successful or not without having to go
        > through the listing file. Information from this file is
        > displayed by VEDA-FE and ANSWER at the completion of the run.

    -   **Reporting:** Based on the optimal solution the reporting
        > routines calculate result parameters, e.g. annual cost
        > information by type, year and technology or commodity. These
        > result parameters together with the solution values of the
        > variables and equations (both primal and dual), as well as
        > selected input data, are assembled in the \<case\>.GDX file.
        > The gdx file is then processed by the GAMS GDX2VEDA.EXE
        > utility according to the directives contained in
        > TIMES2VEDA.VDD control file to generate files for the result
        > analysis software VEDA-BE[^15]. The \<case\>.ANT file for
        > providing results for import into ANSWER may also be produced,
        > if desired.

## Files produced during the run process

Several files are produced by the run process. These include the files
produced by the shell for model initiation, the .LST listing file, which
echoes the GAMS compilation and execution process and reports on any
errors encountered during solve, results files, and the QAcheck.log
file. These files are summarized in Table 3 and discussed in this
section.

  ------------------------------------------------------------------------------
  **Extension**   **Produced By**     **Nature of the Output**
  --------------- ------------------- ------------------------------------------
  ant             TIMES report writer ANSWER model results dump

  gdx             GAMS                Internal (binary) GAMS Data eXchange file
                                      with all the information associated with a
                                      model run

  log             TIMES quality check List of quality assurance checks (warnings
                  routine             and possible errors)

  lst             GAMS                The basic echo of the model run, including
                                      indication of the version of TIMES being
                                      run, the compilation and execution steps,
                                      model summary statistics and error (if
                                      encountered), along with optionally an
                                      equation listing and/or solution print

  vd              GDX2VEDA utility    The core model results dump of the
                                      solution including the variable/equations
                                      levels/slack and marginals, along with
                                      cost and other post-processing
                                      calculations

  vde             GDX2VEDA utility    The elements of the model sets (and the
                                      definition of the attributes)

  vds             GDX2VEDA utility    The set membership of the elements of the
                                      model

  vdt             VEDA-FE or ANSWER   The RES topology information for the model
  ------------------------------------------------------------------------------

  : []{#_Toc449540217 .anchor}Table 3: Files Produced by a TIMES Model
  Run

### Files produced by model initiation

As discussed in Section 2.1, three sets of files are created by VEDA and
ANSWER upon run initiation, the command script file VTRUN/ANSRUN.CMD,
the top-level GAMS command file \<Case\>.RUN/GEN (for VEDA/ANSWER), and
the data dictionary \<scenario\>.DD/DDS text file(s) that contain all
the model data to be used in the run.

The VTRUN/ANSRUN.CMD script file calls GAMS, referring to the \<case\>
file and identifying the location of the TIMES source code and gdx file.
For VEDA-FE the CMD file consists of the line:

Call ..\\\<source_code_folder\>\\vt_gams \<case\>.run
\<source_code_folder\> gamssave\\\<case\>

along with a 2^nd^ line to call the GDX2VEDA utility to process the
TIMES2VEDA.VDD file to prepare the \<case\>.VD\* result files for
VEDA-BE. The ANSRUN.CMD file has a similar setup calling ANS_GAMS.CMD in
the source code folder which invokes GAMS and subsequently the GDX2VEDA
utility.

The \<case\>.RUN/GEN file is the key file controlling the model run. It
instructs the TIMES code what data to grab, what model variant to
employ, how to handle the objective function, and other aspects of the
model run controlled by the switches discussed in Section . An example
.RUN file is displayed in . Rows beginning with an asterisk (\*) are
comment lines for the user\'s convenience and are ignored by the code.
Rows beginning with a dollar-sign (\$) are switches that can be set by
the user (usually by means of VEDA/ANSWER).

Both VEDA and ANSWER have facilities to allow the user to tailor the
content of the RUN/GEN files, though somewhat differently. In VEDA-FE
the Case Manager RUNFile_Tmpl button allows the basic RUN template to be
brought up, and if desired carefully edited. However, the Case Manager
also has a Control Panel, shown in , where many of the more common
switches can be set.

At the beginning of a \<case\>.RUN file the version of the TIMES code
being used is identified and some option control statements that
influence the information output (e.g., SOLPRINT ON/OFF to see a dump of
the solution, OFF recommended) are provided. The LIMROW/LIMCOL options
allow the user to turn on equation listing in the .LST file (discussed
in the next section) by setting the number of rows/columns of each type
to be shown.

Then compile-time dollar control options indicating which solver to use
(if not the default to the particular solution algorithm), whether to
echo the source code (\$ON/OFFLISTING) by printing it to the LST file,
and that multiple definitions of sets and parameters (\$ONMULTI) are
permitted (that is they can appear more than one time, which TIMES
requires since first there are empty declarations for every possible
parameter followed by the actual data provided by the user). Further
possible dollar control options are also described in the GAMS manual.

Afterwards the content of several so-called TIMES dollar control (or
environment) switches are specified. Within the source code the use of
these control switches in combination with queries enables the model to
skip or activate specific parts of the code. Thus it is possible to
turn-on/off variants of the code, e.g. the use of the reduction
algorithm, without changing the input data. The meaning and use of the
different control switches is discussed in Section . Again these are
generally set using the Case Manager/Run form in VEDA/ANSWER.

After the basic control switches, the definition of the set of all
timeslices is established by means of the call to the \<case\>\_TS.DD
file before any other declarations carried out in the initialization
file INITSYS.MOD. This is necessary to ensure the correct ordering of
the timeslices for seasonal, weekly, or daynite storage processes. After
the definition of the timeslices, the files INITSYS.COM and INITMTY.MOD,
which are responsible for the declaration and initialization of all sets
and parameters of the model generator, are included.

![](media/image5.png){width="5.4853083989501314in"
height="7.114316491688539in"}

![](media/image6.png){width="5.909908136482939in"
height="4.98759842519685in"}

[]{#_Ref425136344 .anchor}Figure 5: Example of a VEDA-FE TIMES
\<case\>.RUN file[^16]

The line containing the include command for the file initmty.mod can be
supplemented by calls for additional user extensions that trigger the
use of additional special equations or report routines. The use of these
extension options are described in more detail in Section 0.

Afterwards the data dictionary file(s) (BASE.DD, ..., CO2_TAX_HIGH.DD in
Figure 5) containing the user input sets and parameters are included,
inserted automatically by VEDA-FE/ANSWER according to the list of
scenarios in the Case Manager/Run forms by means of the \$INCLUDE
statements. It is normally advisable to segregate user data into
"packets" as scenarios, where there may be a single Base scenario
containing the core descriptions of the energy system being studied and
a series of alternate scenario depicting other aspects of the system.
For example, one \<scenario\>.DD file may contain the description of the
energy system for a reference scenario, and additional
\<alt_scenario\>.DD files (.DDS for ANSWER) may be included containing
additions or changes relative to the reference file, for example CO~2~
mitigation targets for a reduction scenario, or alternative technology
specifications.

The SET MILESTONYR declaration identifies years for this model run based
upon those years identified in in VEDA via the Period Defs selected on
the Case Manager (and maintained in SysSettings) and the Milestone Years
button on the ANSWER run form. The dollar control switch RUN_NAME
contains the short name of the scenario, and is used for the name of the
results files (\<case\>.VD\*) passed to VEDA-BE.

Next in the example shown in , some runtime switches are activated to
request levelized cost reporting and splitting of investment costs into
core and the incremental additional cost arising from any technology
based discount rate specified in the data. See Section for the full
description of these and other control switches.

The last line of the \<case\>.RUN file invokes the file main driver
routine (maindrv.mod) that initiates all the remaining tasks related to
the model run (pre-processing, coefficient calculation, setting of
bounds, equation generation, solution, reporting). Thus any information
provided after the inclusion of the maindrv.mod file will not be
considered in the main model solve request, though if the user wishes to
introduce specialized post-processing of the result that could be added
(or better yet handled externally by GAMS code that processes the GDX
file).

### GAMS listing file (.LST)

![](media/image7.png){width="3.7402777777777776in"
height="1.3479166666666667in"}The GAMS listing file echoes the model
run. In this file GAMS reports the compile and execution steps, presents
a summary of the model statistics and objective function results, and
reports any errors, if incurred. Optionally the user can request that
the equation listing be turned on by specifying the LIMROW/LIMCOL
(number of rows/columns of each type to be shown) and/or the solution
dumped (via SOLPRINT) by means of the VEDA-FE CaseManager settings, as
shown here.

![](media/image8.png){width="2.4965277777777777in" height="0.9625in"}

[]{#_Toc449540203 .anchor}Figure 6: Requesting Equation Listing and
Solution Print

For ANSWER these are handled by manually editing these entries in the
GEN file either at runtime, or via the Run menu if the change is to be
retrained as the default,

When GAMS takes its 1^st^ pass the \<Case\>.LST file will report each of
the individual source code modules compiled. \[Note that for any
particular TIMES model instance, according to the Run Switch settings,
only the routines needed are invoked, as discussed in Section .\]

A small snippet from the LST file compilation trace from an ANSWER-TIMES
model run of is shown in , where the \"\...\" shows the nesting as one
GAMS routine calls another with the appropriate parameters needed.

![](media/image9.png){width="5.037095363079615in"
height="3.3319641294838145in"}

[]{#_Ref424779247 .anchor}Figure 7: GAMS Compilation of the TIMES Source
Code

If an error is encountered during the compilation operation GAMS will
tag where the error occurred and report an error code. Most common in
this regard is a Domain Error (\$170) where perhaps there was a typo in
an item name, as in the example shown in , or the scenarios were not in
the proper order and data was attempted to be assigned to a process
before it was declared. Further discussion of errors encountered at this
and other stages of the run process is found in Section .

![](media/image10.png){width="5.331776027996501in"
height="3.330650699912511in"}

[]{#_Ref321394441 .anchor}Figure 8: GAMS Compilation Error

Once the data and code have been successfully complied, execution takes
place, with GAMS calling each TIMES routine needed according to the
switches and data for this particular run. Again the LST file echoes
this execution phase, as shown in . It is possible, though unlikely, to
encounter a GAMS Execution error. The most common cause of this is the
explicit specification of zero (0) as the efficiency of a process. An
execution error is reported in the \<Case\>.LST file in a manner similar
to a compilation error, tagged by "Error" at the point that the problem
was encountered.

![](media/image11.png){width="4.640065616797901in" height="3.375in"}

[]{#_Ref425137029 .anchor}Figure 9: GAMS Execution of the TIMES Source
Code

Once execution of the matrix generator has completed GAMS reports the
model run statistics (), and automatically invokes the solver.

![](media/image12.png){width="5.903778433945757in"
height="2.925551181102362in"}

[]{#_Ref419731791 .anchor}Figure 10: CPLEX Solver Statistics

If the OPTION LIMROW/LIMCOL is set to non-0 the equation mathematics are
displayed in the list file, by equation block and/or column
intersection, as shown in and Figure 12 respectively.

![](media/image13.png){width="6.5in" height="2.4652777777777777in"}

[]{#_Ref447876202 .anchor}Figure 11: Equation Listing Example

![](media/image14.png){width="4.1763899825021875in"
height="3.800586176727909in"}

[]{#_Ref447876098 .anchor}Figure 12: Variable Listing Example

And if the SOLPRINT=ON option is activated then the level and marginals
are reported as shown in .

![](media/image15.png){width="6.5in" height="3.3in"}

[]{#_Ref447876120 .anchor}Figure 13: Solution Dump Example

Upon successful solving the model the solution statistics are reported
(), where in this case CPLEX was used to solve a MIP model variant (in
this example), and the report writer invoked to finish up by preparing
the report. If the solver is not able to find an optimal solution, a
non-Normal solve status will be reported, and the user can search the
LST file for the string \"INFES\" for an indication of which equations
are preventing model solution. Again, further information on the
possible causes and resolution of such errors is found in Section .

![](media/image16.png){width="6.052069116360455in"
height="2.9810378390201224in"}

[]{#_Ref419732903 .anchor}Figure 14: Solver Solution Summary

The actual production of the dump of the model results is performed by
the report writer for ANSWER resulting in a \<Case\>.ANT file which is
imported back into ANSWER after the run complete and/or the GDX2VEDA
utility prepared by GAMS and DecisionWare to facilitate the exchange of
information from GAMS to VEDA-BE, which may be used with both VEDA-FE
and ANSWER.

### Results files

The TIMES report writing routine produces two sets of results-related
outputs (along with the quality control LOG discussed in the next
section). The \<case\>.ANT file is an ASCII text file, with results
ready for import into ANSWER. The GAMS Data eXchange file (GDX) contains
all the information associated with a model run \[input data,
intermediate parameters, model results (primal and dual)\] in binary
form. The GDX file may be examined by means of the GAMSIDE, available
from the Windows Start Menu in the GAMS folder (or as a shortcut from
the desktop if put there), if one really wants to dig into what's
happening inside of a TIMES run (that is, the set members, preprocessor
calculations, the model solution and the reporting parameters
calculated).

A more powerful feature within the GAMSIDE is a GDXDIFF facility under
Utilities. As seen in Figure 15, the utility shows the differences
between all components, comparing two model runs. Within the GDXDIFF
utility, the user identifies the GDX files from the two runs and
requests the resulting comparison GDX be prepared. The display then
shows any differences between the two runs. The GDXDIFF is most
effectively used by instructing VEDA to Create DD for the two runs via
the Options and Case Manager forms, as shown in . Once the comparison
GDX has been created, it is viewed in the GAMSIDE. By sorting by Type
and scanning down one Symbol at a time, one can determine exactly what
input data being sent to GAMS for the two runs is different.

![](media/image17.png){width="3.4162489063867016in"
height="4.446232502187226in"}

[]{#_Ref321818210 .anchor}Figure 15: GAMSIDE View of the GDXDIFF Run
Comparison

However, the most common use of the GDX is its further processing to
generate files for the result analysis software VEDA-BE[^17]. ETSAP
worked with GAMS a number of years ago to develop a standalone utility
(GDX2VEDA) to process the GAMS GDX file and produce the files read into
VEDA-BE. The GDX2VEDA utility process a directives file (TIMES2VEDA.VDD)
to determine which sets and model results are to be included and prepare
said information for VEDA-BE. A general default version of the VDD is
distributed with TIMES in the source code folder (for core TIMES,
Stochastics, and MACRO), but may be augmented by the user if other
information is desired from the solution. However, the process of
changing the VDD should be done in consultation with someone fully
familiar with the GAMS GDX file for TIMES and the basics of the GDX2VEDA
utility. See Part V, Appendix B, for further information on the GDX2VEDA
utility and VDD directives file.

![](media/image18.png){width="3.561347331583552in"
height="2.8687029746281714in"}
![](media/image19.png){width="1.6375404636920385in"
height="2.8806977252843393in"}

[]{#_Ref447875229 .anchor}Figure 16: VEDA Setup for Data Only GDX
Request

The call to the GDX2VEDA routine is embedded in the VTRUN/ANSRUN.CMD
command routines. There are three files produced for VEDA-BE by the
GDX2VEDA utility: the \<Case\>.VD data dump with the attributes, and
associated VDE (set elements), VDS (sets definition). In addition,
VEDA-FE and ANSWER produce a \<Case\>.VDT (topology) file with the RES
connectivity information. These files never require user intervention,
though users wishing to post-process the GDX2VEDA results with their own
tailored software, rather than VEDA-BE, might choose to parse the VD\*
files to extract the desired information.

Note that for both ANSWER and VEDA-BE, for the most part low-level (that
is commodity/process) results are reported, along with some aggregate
cost numbers (such as regional and overall objective function). It is
left up to the user to construct relevant sets and tables in VEDA-BE to
organize and aggregate the results into meaningful tables. Refer to Part
V for a discussion of how to go about assembling report tables in
VEDA-BE. For ANSWER the user is left with only the raw results and
thereby needs to come up with their own approach to producing useful
usable reporting tables, or use VEDA-BE.

In addition, as discussed in Section 3.10, there are a number of
switches that control the report writer itself in terms of how it
calculates certain outputs and prepares the results as part of the
post-processing. Collectively these mechanisms provide the user with a
wide range of reporting results and tools for dissecting and assembling
the modeling results as part of effectively using TIMES to conduct
energy policy analyses.

### QA check report (LOG) 

In order to assist the user with identifying accidental modelling
errors, a number of sanity checks are done by the model generator. If
incorrect or suspicious specifications are found in these checks, a
message is written in a text file named QA_CHECK.LOG, in the working
folder. The checks implemented in TIMES Version 3.9.3 are listed in
Table 5. The "Log entry" column shows the identification given for each
suspicious specification.

+----+------------------------------------------------+------+--------+
| *  | **Message / Description**                      | **Se | **Log  |
| *T |                                                | veri | e      |
| yp |                                                | ty** | ntry** |
| e* |                                                |      |        |
| *[ |                                                |      |        |
| ^1 |                                                |      |        |
| 8] |                                                |      |        |
+====+================================================+======+========+
| S  | User-provided G_YRFR values are not valid year | war  | re     |
| TD | fractions:                                     | ning | gion,\ |
|    |                                                |      | ts-l   |
|    | The sum of year fractions over timeslices does |      | evel,\ |
|    | not sum up correctly. The fractions are        |      | tim    |
|    | normalized so that they sum up to 1 over the   |      | eslice |
|    | full year.                                     |      |        |
+----+------------------------------------------------+------+--------+
| S  | Delayed Process but PAST Investment:\          | war  | r      |
| TD | Process availability has been delayed by using | ning | egion, |
|    | PRC_NOFF or NCAP_START, but also has existing  |      | p      |
|    | capacity.                                      |      | rocess |
+----+------------------------------------------------+------+--------+
| S  | Commodities/processes defined at non-existing  | sev  | number |
| TD | TSLVL:                                         | ere\ | of     |
|    |                                                | e    | C      |
|    | PRC_TSL or COM_TSL has been specified on a     | rror | OM/PRC |
|    | timeslice level not used in the model.         |      | reset  |
|    |                                                |      | to     |
|    |                                                |      | ANNUAL |
+----+------------------------------------------------+------+--------+
| S  | NCAP_TLIFE out of feasible range:\             | war  | r      |
| TD | NCAP_TLIFE specified has a value of either     | ning | egion, |
|    | less than 0.5 or greater than 200. Values less |      | pr     |
|    | than 0.5 are reset to 1.                       |      | ocess, |
|    |                                                |      | v      |
|    |                                                |      | intage |
+----+------------------------------------------------+------+--------+
| S  | Inconsistent CAP_BND(UP/FX) defined for        | war  | r      |
| TD | process capacity:                              | ning | egion, |
|    |                                                |      | pro    |
|    | CAP_BND(UP/FX) value specified has a value     |      | cess,\ |
|    | lower than the residual capacity remaining     |      | period |
|    | available in the period, and retirements are   |      |        |
|    | disabled.                                      |      |        |
+----+------------------------------------------------+------+--------+
| S  | Flow OFF TS level below variable TS level:     | war  | r      |
| TD |                                                | ning | egion, |
|    | A PRC_FOFF attribute with a timeslice below    |      | pr     |
|    | the flow level has been specified; the OFF     |      | ocess, |
|    | specification is ignored.                      |      | comm   |
|    |                                                |      | odity, |
|    |                                                |      | tim    |
|    |                                                |      | eslice |
+----+------------------------------------------------+------+--------+
| S  | COM_FR does not sum to unity (T=first year):\  | war  | r      |
| TD | The sum of COM_FR over all timeslices at the   | ning | egion, |
|    | COM_TSL level is not equal to 1, and is        |      | comm   |
|    | therefore normalized to 1.                     |      | odity, |
|    |                                                |      | mil    |
|    |                                                |      | estone |
+----+------------------------------------------------+------+--------+
| S  | Unsupported diverging trade topology:\         | e    | r      |
| TD | The model generator detects an unsupported     | rror | egion, |
|    | complex topology of an IRE process, which      |      | p      |
|    | cannot be properly handled                     |      | rocess |
+----+------------------------------------------------+------+--------+
| S  | FLO_EMIS with no members of source group in    | sev  | r      |
| TD | process:\                                      | ere\ | egion, |
|    | A FLO_EMIS with a source group that has no     | e    | pr     |
|    | members for the process has been specified.    | rror | ocess, |
|    | The parameter is ignored.                      |      | group, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| S  | Unsupported FLO_SHAR: C not in RPC or CG:\     | e    | r      |
| TD | The commodity in FLO_SHAR is either not in the | rror | egion, |
|    | process topology or not a member of the group  |      | pr     |
|    | specified                                      |      | ocess, |
|    |                                                |      | comm   |
|    |                                                |      | odity, |
|    |                                                |      | group  |
+----+------------------------------------------------+------+--------+
| S  | FLO_SHAR conflict: Both FX + LO/UP specified,  | war  | r      |
| TD | latter ignored:\                               | ning | egion, |
|    | Too many FLO_SHAR bounds are specified, if     |      | pr     |
|    | both FX and LO/UP are specified at the same    |      | ocess, |
|    | time.                                          |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | comm   |
|    |                                                |      | odity, |
|    |                                                |      | group  |
+----+------------------------------------------------+------+--------+
| S  | Inconsistent sum of fixed FLO_SHARs in Group:\ | war  | r      |
| TD | All flows in a group have a fixed share, but   | ning | egion, |
|    | the sum of the fixed FLO_SHAR values is not    |      | pr     |
|    | equal to 1.                                    |      | ocess, |
|    |                                                |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | group  |
+----+------------------------------------------------+------+--------+
| S  | Defective sum of FX and UP FLO_SHARs in Group: | war  | r      |
| TD |                                                | ning | egion, |
|    | All flows in a group have either a fixed or an |      | pr     |
|    | upper share, but the sum of the FLO_SHAR       |      | ocess, |
|    | values is less than 1.                         |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | group  |
+----+------------------------------------------------+------+--------+
| S  | Excessive sum of FX and LO FLO_SHARs in        | war  | r      |
| TD | Group:\                                        | ning | egion, |
|    | All flows in a group have either a fixed or a  |      | pr     |
|    | lower share, but the sum of the FLO_SHAR       |      | ocess, |
|    | values is greater than 1.                      |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | group  |
+----+------------------------------------------------+------+--------+
| S  | NCAP_AF/ACT_BND Bounds conflict:\              | war  | r      |
| TD | Value at PRC_TS level and below, latter        | ning | egion, |
|    | ignored                                        |      | pr     |
|    |                                                |      | ocess, |
|    |                                                |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | tim    |
|    |                                                |      | eslice |
+----+------------------------------------------------+------+--------+
| S  | NCAP_AF Bounds conflict:\                      | war  | r      |
| TD | FX + LO/UP at same TS-level, latter ignored    | ning | egion, |
|    |                                                |      | pr     |
|    |                                                |      | ocess, |
|    |                                                |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | tim    |
|    |                                                |      | eslice |
+----+------------------------------------------------+------+--------+
| S  | FLO_SHAR/FLO_FR Bounds conflict:\              | war  | r      |
| TD | Value at RPCS_VAR level and below, latter      | ning | egion, |
|    | ignored                                        |      | pr     |
|    |                                                |      | ocess, |
|    |                                                |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | tim    |
|    |                                                |      | eslice |
+----+------------------------------------------------+------+--------+
| S  | FLO_SHAR Bounds conflict:\                     | war  | r      |
| TD | FX + LO/UP at same TS-level, latter ignored    | ning | egion, |
|    |                                                |      | pr     |
|    |                                                |      | ocess, |
|    |                                                |      | vi     |
|    |                                                |      | ntage, |
|    |                                                |      | comm   |
|    |                                                |      | odity, |
|    |                                                |      | group  |
+----+------------------------------------------------+------+--------+
| S  | COM_BNDNET/COM_BNDPRD/IRE_BND Bounds           | war  | r      |
| TD | conflict:\                                     | ning | egion, |
|    | Value at COM_TS level and below, latter        |      | mile   |
|    | ignored                                        |      | stone, |
|    |                                                |      | comm   |
|    |                                                |      | odity, |
|    |                                                |      | tim    |
|    |                                                |      | eslice |
+----+------------------------------------------------+------+--------+
| S  | IRE_FLO import commodity not in TOP_IRE:\      | e    | r      |
| TD | An invalid IRE_FLO with the imported commodity | rror | egion, |
|    | not in the process topology has been specified |      | pr     |
|    |                                                |      | ocess, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| S  | CHP process with zero CEH but only upper bound | e    | r      |
| TD | on CHPR:\                                      | rror | egion, |
|    | A CHP process has only an upper bound on       |      | p      |
|    | NCAP_CHPR, but a zero or missing NCAP_CEH,     |      | rocess |
|    | which indicates a modelling error              |      |        |
+----+------------------------------------------------+------+--------+
| S  | Year Fraction G_YRFR is ZERO!\                 | f    | r      |
| TD | A timeslice with G_YRFR is within the          | atal | egion, |
|    | timeslice tree. This should actually never     |      | tim    |
|    | happen, because TIMES automatically removes    |      | eslice |
|    | timeslices with a zero year fraction from the  |      |        |
|    | active timeslices.                             |      |        |
+----+------------------------------------------------+------+--------+
| S  | Illegal system commodity in topology:\         | f    | r      |
| TD | ACT / ACTGRP is a reserved name which should   | atal | egion, |
|    | never be used as a commodity in the model      |      | p      |
|    | topology.                                      |      | rocess |
+----+------------------------------------------------+------+--------+
| S  | Commodity in CG of process P but not in        | se   | r      |
| TD | topology:\                                     | vere | egion, |
|    | A commodity group assigned to a process        | e    | pr     |
|    | contains members not in the process topology   | rror | ocess, |
|    | (or no members in the process topology).       |      | comm   |
|    |                                                |      | .group |
+----+------------------------------------------------+------+--------+
| S  | Elastic Demand but either COM_BPRICE/ELAST/VOC | war  | r      |
| TD | missing:\                                      | ning | egion, |
|    | Either a demand that has COM_ELAST or COM_STEP |      | comm   |
|    | defined but does not have COM_BPRICE,          |      | odity, |
|    | COM_ELAST, or COM_VOC, defined.                |      | LO/UP  |
+----+------------------------------------------------+------+--------+
| S  | Commodity type is also a commodity:\           | f    | r      |
| TD | Commodity types are reserved names that cannot | atal | egion, |
|    | be used as commodity names.                    |      | com    |
|    |                                                |      | modity |
|    |                                                |      | type   |
+----+------------------------------------------------+------+--------+
| S  | Commodity has ambiguous base type:\            | se   | r      |
| TD | The base type for some commodity is not        | vere | egion, |
|    | uniquely defined. All commodi­ties should have  | e    | com    |
|    | a unique base type defined                     | rror | modity |
|    | (NRG/MAT/DEM/ENV/FIN).                         |      |        |
+----+------------------------------------------------+------+--------+
| S  | Demand: DEM commodity with missing COM_PROJ    | war  | r      |
| TD | Projection:\                                   | ning | egion, |
|    | A demand commodity without any demand          |      | com    |
|    | projection is found.                           |      | modity |
+----+------------------------------------------------+------+--------+
| S  | Demand: COM_PROJ specified for non-DEM         | war  | r      |
| TD | commodity:\                                    | ning | egion, |
|    | Demand is projected for a non-demand           |      | com    |
|    | commodity.                                     |      | modity |
+----+------------------------------------------------+------+--------+
| S  | Phantom entries found in topology              | f    | r      |
| TD | (process/commodity not in SET PRC/COM):\       | atal | egion, |
|    | This error is usually triggered when a GAMS    |      | pr     |
|    | domain violation has occurred, which may cause |      | ocess, |
|    | unexpected behaviour of the GAMS code.         |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| S  | Process with missing or mismatched             | f    | r      |
| TD | CG/PRC_ACTUNIT:\                               | atal | egion, |
|    | Process with missing or several PRC_ACTUNT     |      | p      |
|    | entries.                                       |      | rocess |
+----+------------------------------------------------+------+--------+
| S  | Illegal dependency of substituted auxiliary    | f    | r      |
| TD | commodities C1 and C2 in FLO_SUM:\             | atal | egion, |
|    | This error should not occur, because the GAMS  |      | pr     |
|    | code should make sure that C1 and C2 are not   |      | ocess, |
|    | both substituted. If this error is issued,     |      | commo  |
|    | contact TIMES maintenance.                     |      | dity1, |
|    |                                                |      | comm   |
|    |                                                |      | odity2 |
+----+------------------------------------------------+------+--------+
| S  | NCAP_AFX defined for NON-vintaged dispatchable | war  | r      |
| TD | process with ACT_MINLD:\                       | ning | egion, |
|    | Shaping of NCAP_AF is not supported for        |      | p      |
|    | non-vintaged processes having ACT_MINLD        |      | rocess |
|    | defined.                                       |      |        |
+----+------------------------------------------------+------+--------+
| S  | Active currency but not member of set CUR:\    | f    | cu     |
| TD | Currency referred to in some attributes is not | atal | rrency |
|    | defined in the set CUR.                        |      |        |
+----+------------------------------------------------+------+--------+
| S  | Internal Region without Discount Rate:\        | f    | region |
| TD | TIMES requires a discount rate defined for all | atal |        |
|    | internal regions.                              |      |        |
+----+------------------------------------------------+------+--------+
| S  | Active Currency without Discount Rate:\        | f    | r      |
| TD | A currency is being used without discount      | atal | egion, |
|    | rate, or conversion to another currency that   |      | cu     |
|    | has a discount rate.                           |      | rrency |
+----+------------------------------------------------+------+--------+
| S  | Process with zero PRC_ACTFLO for C in PG:      | f    | r      |
| TD |                                                | atal | egion, |
|    | A zero PRC_ACTFLO has been specified for a     |      | pr     |
|    | commodity in the primary group.                |      | ocess, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| X  | Same Commodity IN and OUT of non-STG process:\ | se   | r      |
| TD | A process has been defined to have the same    | vere | egion, |
|    | commodity as an input and an output, and it is | e    | pr     |
|    | not a storage process; that is not supported.  | rror | ocess, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| X  | IRE Process with invalid Parameters:\          | e    | r      |
| TD | Some FLO_FUNC, FLO_SUM, FLO_SHAR or UC_FLO     | rror | egion, |
|    | parameter not supported for IRE processes has  |      | pro    |
|    | been specified.                                |      | cess,\ |
|    |                                                |      | com    |
|    |                                                |      | -group |
+----+------------------------------------------------+------+--------+
| X  | Invalid Commodity / Group used in ACT_EFF -    | e    | r      |
| TD | parameter ignored:\                            | rror | egion, |
|    | An invalid ACT_EFF attribute with a CG not     |      | pro    |
|    | containing members on the shadow side or in    |      | cess,\ |
|    | the PG has been specified.                     |      | group  |
+----+------------------------------------------------+------+--------+
| X  | FLO_SUM Commodity Not in RPC - parameter       | e    | r      |
| TD | ignored:                                       | rror | egion, |
|    |                                                |      | pro    |
|    | An invalid FLO_SUM has been defined where the  |      | cess,\ |
|    | commodity is not in the process topology.      |      | group, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| X  | FLO_SUM Commodity Not in CG1 - parameter       | e    | r      |
| TD | ignored:\                                      | rror | egion, |
|    | An invalid FLO_SUM has been defined where the  |      | pro    |
|    | commodity is not a member of the first group,  |      | cess,\ |
|    | CG1.                                           |      | group, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| X  | PTRANS between CG1 and CG2 in both             | se   | r      |
| TD | directions:\                                   | vere | egion, |
|    | A FLO_FUNC or FLO_SUM between groups CG1 and   | e    | pro    |
|    | CG2 has been specified in both directions.     | rror | cess,\ |
|    |                                                |      | g      |
|    |                                                |      | roup1, |
|    |                                                |      | group2 |
+----+------------------------------------------------+------+--------+
| X  | RPC in TOP not found in any ACTFLO / FLO_SHAR  | war  | r      |
| TD | / FLO_FUNC / FLO_SUM:\                         | ning | egion, |
|    | Some commodity in the topology does not seem   |      | pro    |
|    | to be tied to anything, at least by means of   |      | cess,\ |
|    | any of the most common attributes; the user is |      | comm   |
|    | advised to check that this is not a modelling  |      | odity, |
|    | error.                                         |      | IN/OUT |
+----+------------------------------------------------+------+--------+
| X  | Empty Group in FLO_SUM/FLO_FUNC/FLO_SHAR:      | se   | r      |
| TD |                                                | vere | egion, |
|    | A group that has no members in the process     | e    | pro    |
|    | topology has been used for a process           | rror | cess,\ |
|    | attribute. Detects also an empty primary       |      | group  |
|    | group.                                         |      |        |
+----+------------------------------------------------+------+--------+
| X  | Both NCAP_AF and NCAP_AFA specified for same   | war  | r      |
| TD | process:\                                      | ning | egion, |
|    | Specifying both NCAP_AF(bd) and NCAP_AFA(bd)   |      | pr     |
|    | for an ANNUAL level process is ambiguous and   |      | ocess, |
|    | should be avoided.                             |      | v      |
|    |                                                |      | intage |
+----+------------------------------------------------+------+--------+
| X  | Too Long Commodity Lead Time:\                 | war  | r      |
| TD | A value of NCAP_CLED \> NCAP_ILED has been     | ning | egion, |
|    | specified                                      |      | pr     |
|    |                                                |      | ocess, |
|    |                                                |      | com    |
|    |                                                |      | modity |
+----+------------------------------------------------+------+--------+
| X  | CHP parameter specified for Non-CHP process:   | e    | r      |
| TD |                                                | rror | egion, |
|    | An NCAP_BPME, NCAP_CHPR or NCAP_CEH parameter  |      | pr     |
|    | has been specified for a process that is not   |      | ocess, |
|    | defined to be CHP.                             |      | v      |
|    |                                                |      | intage |
+----+------------------------------------------------+------+--------+
| X  | PG of CHP process consists of single commodity | war  | r      |
| TD | yet has a CHP-ratio:\                          | ning | egion, |
|    | A CHP process has a NCAP_CHPR specified but    |      | p      |
|    | has only a single commodity in the primary     |      | rocess |
|    | group.                                         |      |        |
+----+------------------------------------------------+------+--------+
| X  | Found CHP processes without CHP-ratio defined: | war  | number |
| TD |                                                | ning | of     |
|    | A CHP process has no NCAP_CHPR defined         |      | such   |
|    |                                                |      | pro    |
|    |                                                |      | cesses |
+----+------------------------------------------------+------+--------+
| X  | Found CHP processes with PG commodity          | war  | r      |
| TD | efficiencies - unsupported:\                   | ning | egion, |
|    | Specifying ACT_EFF on some flow(s) in the PG   |      | p      |
|    | is not supported for CHP processes, and may    |      | rocess |
|    | lead to unexpected results.                    |      |        |
+----+------------------------------------------------+------+--------+
| X  | Found CHP processes without electricity in the | war  | r      |
| TD | PG:\                                           | ning | egion, |
|    | A CHP process is found with no electricity     |      | p      |
|    | commodity in the PG.                           |      | rocess |
+----+------------------------------------------------+------+--------+

: []{#_Toc449540218 .anchor}Table 4: TIMES Quality Assurance Checks (as
of Version 4.4.0)

## Errors and their resolution

Errors may be encountered during the compilation, execution (rarely), or
solve stages of a TIMES model run. During the compilation step, if GAMS
encounters any improperly defined item the run will be halted with a
Domain or similar error and the user will need to examine the TIMES
quality control LOG or GAMS listing (LST) files to ascertain the cause
of the problem. While such problems are not normally encountered, some
that might occur include:

-   an item name was mistyped and therefore not defined;

-   an item was previously defined in one scenario but defined
    differently in another;

-   an item was not properly declared for a particular parameters (e.g.,
    a non-trade process using an IRE parameter), and

-   scenarios were specified for the run in the wrong order so a data
    reference is encountered before the declaration (e.g., a bound on a
    new technology option is provided before it has been identified).

During the execution phase, if GAMS encounters any runtime errors it
will halt and report where the error occurred in the LST file. While
such problems are not normally encountered some causes of an execution
error might be:

-   an explicit 0 is provided for an efficiency resulting in a divide by
    0, and

-   there is a conflict between a lower and upper bound.

Most commonly errors are encountered during the solve process, resulting
in an infeasibility. Some causes of the model not being able to solve
might be:

-   due to bounds, the energy system cannot be configured in such a way
    as to meet the limit;

-   owing to mis-specifying the demand serviced by a device, there is no
    or not enough capacity to satisfy said demand, and

-   the RES is not properly connected so a needed commodity is not able
    to reach the processes needing it.

To identify the cause of a solve error, if using CPLEX the user can
activate the Infeasibility Finder (set in the CPLEX.OPT as default (via
the IIS command) in VEDA-FE Case Manager or said file distributed with
ANSWER). The CPLEX Infeasibility Finder will identify the explicit
row/columns corresponding to the first infeasibility encountered and
list the conflict involved in the \<Case\>.LST file, such as shown here
where the electricity balance equation can't be satisfied
![](media/image20.png){width="6.506944444444445in" height="0.2in"}(due
to a limit being imposed on the first year electric grid capacity that
is too small).

This helps with tracking down the culprit, but the user still needs to
figure out why the problem occurred. When using a solver other than
CPLEX, or if the Infeasibility Finder is not activated, then the
solution dump will be tagged for all the potentially interrelated model
variables/equations that were not in equilibrium at the time the solve
stopped. The user can find these by searching the LST file for the
string \"INFES\".

As a last resort, the model can be run with the equation listing turned
on by setting LIMROW/LIMCOL to, say, 1000 in the \<case\>.RUN (via the
Case Manager) / GEN (via Edit the GEN from the Run form) file, although
the equations in this form can be challenging to interpret.

