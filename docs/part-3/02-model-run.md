# The TIMES source code and the model run process

As discussed in the previous section, the heart of TIMES is embodied in the GAMS source code, comprised of the matrix generator that digests the input data prepared from ANSWER or VEDA-FE and prepares the mathematical representation of the model instance, an optimizer to solve the resulting mathematical programming problem, and a report writer that post-processes the solution and prepares results files for ANSWER and VEDA-BE. It is this collection of GAMS source code routines that correspond to the TIMES model, where each TIMES model run proceeds through the appropriate path in the source code based upon the user specified runtime switches, described in Section 3, and the provided input data.

For the most part, this process is seamless to the user, as the model management shells extract the scenario data and prepare ASCII text files in the layout required by GAMS, set up the top level GAMS control file, and initiate the model run (in a Command Prompt box). GAMS then compiles the source and data, constructs the model, invokes the solvers, and dumps the model results for importing back into the model management environment. However, knowledge of the run process and the files produced along the way can be helpful in diagnosing model errors (e.g., a division by zero may necessitate turning on the source code listing (`$ONLISTING`/`$OFFLIST` at the top/bottom of the routine where the error is reported) to determine which parameter is causing the problem) or if a user is considering modifying the model formulation to, say, add a new kind of constraint (note that any such undertaking should be closely coordinated with ETSAP).

## Overview of the model run process

Once a model is readied, a run can be initiated from the model management systems by means of the Case Manager in VEDA-FE or the Run Model option on the ANSWER Home screen. In both systems the user assembles the list of scenarios to comprise the model run, taking care to ensure that the order of the scenarios is such that all RES components are first declared (that is their item name and set membership specified) and then assigned data.

In the model management shells, the user can also adjust the TIMES model variant, run control switches, and solver options. For VEDA-FE this is done through the Case Manager, via the Control Panel, RUNFile template, and solver settings. {numref}`case-manager-control-form` shows an example of the VEDA-FE Control Panel. See Part IV for more on the use of the Case Manager in VEDA-FE.

In ANSWER, the Run Model button brings up the Run Model Form, from which the model variant and most run control switches can be set. (The others need to be set using the Edit GAMS Control Options feature.) However the \<Solver\>.OPT file needs to be handled manually outside of ANSWER. See the separate ANSWER documentation for more details on these ANSWER facilities.

When a model run is initiated, three kinds of files are created by VEDA and ANSWER. The first is a Windows command script file VTRUN/ANSRUN.CMD (for VEDA/ANSWER respectively), which just identifies the run name, indicates where the source code resides, and perhaps any restart (see Section 3.8), and then calls the VEDA/ANSWER driver command script (VT_GAMS/ANS_RUN.CMD). The second is the top-level GAMS command file \<Case\>.RUN/GEN (for VEDA/ANSWER), which is passed to GAMS to initiate and control the model run. It sets the model variant, identifies the Milestone (run) years, lists the scenario data files (DD/DDS) to include, and invokes the main GAMS routine to have the model actually assembled mathematically, solved, and reported upon. It is discussed further in Section . The third group of files comprise the data dictionary \<scenario\>.DD/DDS file(s), which contain the user input sets and parameters in the format required by GAMS to fully describe the energy system to be analyzed.

GAMS is a two pass language, first compiling and then executing. In the first pass, GAMS reads the input data prepared by ANSWER or VEDA-FE, and then proceeds to compile the data as well as the actual TIMES source code to ready it for execution (unless a Runtime license is employed in which case only the data is compiled).

In the second pass, GAMS then proceeds to execute the complied data and code to declare the equations and variables that are to make up this particular TIMES incarnation and generate the appropriate coefficients for matrix intersection, that is the multiplier for the individual variables comprising each equation. With the matrix assembled GAMS then turns over the problem to the solver.

```{figure} assets/image4.png
:name: case-manager-control-form
:align: center
VEDA-FE Case Manager Control Form.
```

As a result of a model run a listing file (\<Case\>.LST), and a \<case\>.GDX file (GAMS dynamic data exchange file with all the model data and results) are created. The \<Case\>.LST file may contain compilation calls and execution path through the code, an echo print of the GAMS source code and the input data, a listing of the concrete model equations and variables, error messages, model statistics, model status, and solution dump. The amount of information displayed in the listing file can be adjusted by the user through GAMS options in the \<Case\>.RUN file.

The \<Case\>.GDX file is an internal GAMS file. It is processed according to the information provided in the TIMES2VEDA.VDD to create results input files for the VEDA-BE software to analyze the model results in the \<case\>.VD\* text files. A dump of the solution results is also done to the \<case\>.ANT file for importing into ANSWER, if desired. At this point, model results can be imported into VEDA-BE and ANSWER respectively for post-process and analysis. More information on VEDA-BE and ANSWER results processing can be found in Part V and the separate ANSWER documentation respectively.

In addition to these output files, TIMES may create a file called QA_CHECK.LOG to inform the user of possible errors or inconsistencies in the model formulation. The QA_CHECK file should be examined by the user on a regular basis to make sure no "surprises" have crept into a model. The content and use of each of these files is discussed further in Section 2.3.

For the ETSAP Runtime GAMS license, which does not allow for adjustments to the TIMES source code by users (which in general is not encouraged anyway), a special TIMES.g00 file is used that contains the declaration of each variable and equation that is part of the model definition, thereby initializing the basic model structure.

## The TIMES source code

The TIMES model generator is comprised of a host of GAMS source code routines, which are simple text files that reside in the user\'s \\VEDA\\VEDA-FE\\GAMS_SrcTIMESv### folder, as discussed in Section 1.3 (or \\AnswerTIMESv6\\GAMS_SrcTI). Careful naming conventions are employed for all the source code routines. These conventions are characterized, for the most part, by prefixes and extensions corresponding to collections of files handling each aspect of the code (e.g., set bounds, prepare coefficients, specify equations), as summarized in {numref}`times-routines-naming`.

```{list-table} TIMES Routines Naming Conventions
:name: times-routines-naming
:header-rows: 1

* - **Type**
  - **Nature of the Routine**
* - **Prefix**
  - 
* - **ans**
  - ANSWER TIMES specific pre-processor code
* - **bnd**
  - set bounds on model variables
* - **cal**
  - calculations performed in support of the preprocessor and report writer
* - **coef**
  - prepare the actual matrix intersection coefficients
* - **eq**
  - equations specification (the actual assembling of the coefficients of the matrix)
* - **err**
  - Error trapping and handling
* - **fil**
  - handles the fundamental interpolation/extrapolation/normalization of the original input data
* - **init**
  - initialize all sets and parameters potentially involved in assembling a TIMES model
* - **main**
  - Top level routines according to the model variant to be solved
* - **mod**
  - the declaration of the equations and variables for each model variant
* - **pp**
  - preprocess routines responsible for preparing the TIMES internal parameters by assembling, interpolating, levelizing, normalizing, and processing the input data to prepare the data structures needed to produce the model coefficients
* - **qa**
  - Quality assurance checking and reporting
* - **rpt**
  - main reporting components performing the calculations needed and assembling the relevant parameters from the model results
* - **sol**
  - components of the results report writer that prepares the solution for outputting
* - **solve**
  - manage the actual call to solve the model (that is the call to invoke the optimizer)
* - **uc**
  - handles the user constraints
* - **Extension**
  - 
* - **ABS**
  - Ancillary Balancing Services routines
* - **ANS**
  - ANSWER specific code
* - **CLI**
  - climate module routines
* - **CMD**
  - Windows command scripts to invoke GAMS/GDX2VEDA in order to solve and afterwards dump the model results
* - **DEF**
  - setting of defaults
* - **DSC**
  - discrete (lumpy) investment routines
* - **ETL**
  - endogenous technology learning routines
* - **GMS**
  - lower level GAMS routines to perform interpolation, apply shaping of input parameters, etc.
* - **RUN/GEN**
  - VEDA-FE/ANSWER specific GAMS TIMES command templates for dynamic substitution of the switches and parameters needed at run submission to identify the model variant and other options that will guide the current model run
* - **IER**
  - routines and extensions prepared by the University of Stuttgart (Institute for the Rational Use of Energy, IER) (e.g., for more advanced modeling of CHPs)
* - **LIN**
  - routines related to the alternative objective formulations
* - **MOD**
  - core TIMES routines preparing the actual model
* - **MLF**
  - code related to the MLF implementation of TIMES-MACRO
* - **MSA**
  - code related to the MSA implementation of decomposed TIMES-MACRO
* - **RED**
  - reduction algorithm routines
* - **RPT**
  - report writer routines
* - **STC**
  - code related to stochastics
* - **STP**
  - code related to time-stepped or partially fixed-horizon solution
* - **TM**
  - the core TIMES MACRO code
* - **VDA**
  - routines related to new TIMES features implemented under the VDA extension
* - **VDD**
  - directives for the VEDA-BE result analysis software
```

Note that these don't cover every single routine in the TIMES source code folder, but do cover most all of the core routines involved in the construction and reporting of the model. They guide the steps of the run process as follows:
- **GAMS Compile:** As mentioned above, GAMS operates as a two-phase compile then execute system. As such it first reads and assembles all the control, data, and code files into a ready executable; substituting user and/or shell provided values for all GAMS environment switches and subroutine parameter references (the %EnvVar% and %Param% references in the source code) that determine the path through the code for the requested model instance and options desired. If there are inconsistencies in input data they may result in compile-time errors (e.g., \$170 for a domain definition error), causing a run to stop. See Section for more on identifying the source of such errors.
- **Initialization:** Upon completion of the compile step, all possible GAMS sets and parameters of the TIMES model generator are declared and initialized, then established for this instance of the model from the user's data dictionary file(s) (\<Case\>.DD[^14]). Model units are also initialized using the UNITS.DEF file, which contains the short names for the most common sets of units that are normally used in TIMES models, and which can be adjusted by the user.
- **Execution:** After the run has been prepared, the maindrv.mod routine controls all the remaining tasks of the model run. The basic steps are as follows.
    - **Pre-processing:** One major task is the pre-processing of the model input data. During pre-processing control sets defining the valid domain of parameters, equations and variables are generated (e.g., for which periods each process is available, at what timeslice level (after inheritance) is each commodity tracked and does each process operate), input parameters are inter-/extrapolated, and time-slice specific input parameters are inherited/aggregated to the correct timeslice level as required by the model generator.
    - **Preparation of coefficients:** A core activity of the model generator is the proper derivation of the actual coefficients used in the model equations. In some cases coefficients correspond directly to input data (e.g., FLO_SHAR to the flow variables), but in other cases they must be transformed. For example, the investment cost (NCAP_COST) must be annualized, spread for the economic lifetime, and discounted before being applied to the investment variable (VAR_NCAP) in the objective function (EQ_OBJ), and based upon the technical lifetime the coefficients in the capacity transfer constraint (EQ_CPT**)** are determined to make sure that new investment are accounted for and retired appropriately.
    - **Generation of model equations:** Once all the coefficients are prepared, the file eqmain.mod controls the generation of the model equations. It calls the individual GAMS routines responsible for the actual generation of the equations of this particular instance of the TIMES model. The generation of the equations is controlled by sets, parameters, and switches carefully assembled by the pre-processor to ensure that no superfluous equations or matrix intersections are generated.
    - **Setting variable bounds:** The task of applying bounds to the model variables corresponding to user input parameters is handled by the bndmain.mod file. In some cases it is not appropriate to apply bounds directly to individual variables, but instead applying a bound may require the generation of an equation (e.g. the equation EQ(l)\_ACTBND is created when an annual activity bound is specified for a process having a diurnal timeslice resolution).
    - **Solving the model:** After construction of the actual matrix (rows, columns, intersections and bounds) the problem is passed to an optimizing solver employing the appropriate technique (LP, MIP, or NLP). The solver returns the solution of the optimization back to GAMS. The information regarding the solver status is written by TIMES in a text file called END_GAMS, which allows the user to quickly check whether the optimisation run was successful or not without having to go through the listing file. Information from this file is displayed by VEDA-FE and ANSWER at the completion of the run.
    - **Reporting:** Based on the optimal solution the reporting routines calculate result parameters, e.g. annual cost information by type, year and technology or commodity. These result parameters together with the solution values of the variables and equations (both primal and dual), as well as selected input data, are assembled in the \<case\>.GDX file. The gdx file is then processed by the GAMS GDX2VEDA.EXE utility according to the directives contained in TIMES2VEDA.VDD control file to generate files for the result analysis software VEDA-BE[^15]. The \<case\>.ANT file for providing results for import into ANSWER may also be produced, if desired.

## Files produced during the run process

Several files are produced by the run process. These include the files produced by the shell for model initiation, the .LST listing file, which echoes the GAMS compilation and execution process and reports on any errors encountered during solve, results files, and the QAcheck.log file. These files are summarized in {numref}`files-produced-by-times-run` and discussed in this section.

```{list-table} Files Produced by a TIMES Model Run
:name: files-produced-by-times-run
:header-rows: 1

* - Extension
  - Produced By
  - Nature of the Output
* - ant
  - TIMES report writer
  - ANSWER model results dump
* - gdx
  - GAMS
  - Internal (binary) GAMS Data eXchange file with all the information associated with a model run
* - log
  - TIMES quality check routine
  - List of quality assurance checks (warnings and possible errors)
* - lst
  - GAMS
  - The basic echo of the model run, including indication of the version of TIMES being run, the compilation and execution steps, model summary statistics and error (if encountered), along with optionally an equation listing and/or solution print
* - vd
  - GDX2VEDA utility
  - The core model results dump of the solution including the variable/equations levels/slack and marginals, along with cost and other post-processing calculations
* - vde
  - GDX2VEDA utility
  - The elements of the model sets (and the definition of the attributes)
* - vds
  - GDX2VEDA utility
  - The set membership of the elements of the model
* - vdt
  - VEDA-FE or ANSWER
  - The RES topology information for the model
```

### Files produced by model initiation

As discussed in Section 2.1, three sets of files are created by VEDA and ANSWER upon run initiation, the command script file VTRUN/ANSRUN.CMD, the top-level GAMS command file \<Case\>.RUN/GEN (for VEDA/ANSWER), and the data dictionary \<scenario\>.DD/DDS text file(s) that contain all the model data to be used in the run.

The VTRUN/ANSRUN.CMD script file calls GAMS, referring to the \<case\> file and identifying the location of the TIMES source code and gdx file. For VEDA-FE the CMD file consists of the line:

```
Call ..<source_code_folder>\vt_gams <case>.run <source_code_folder> gamssave\<case>
```

Along with a 2<sup>nd</sup> line to call the GDX2VEDA utility to process the TIMES2VEDA.VDD file to prepare the \<case\>.VD\* result files for VEDA-BE. The ANSRUN.CMD file has a similar setup calling ANS_GAMS.CMD in the source code folder which invokes GAMS and subsequently the GDX2VEDA utility.

The \<case\>.RUN/GEN file is the key file controlling the model run. It instructs the TIMES code what data to grab, what model variant to employ, how to handle the objective function, and other aspects of the model run controlled by the switches discussed in Section . An example .RUN file is displayed in . Rows beginning with an asterisk (\*) are comment lines for the user\'s convenience and are ignored by the code. Rows beginning with a dollar-sign (\$) are switches that can be set by the user (usually by means of VEDA/ANSWER).

Both VEDA and ANSWER have facilities to allow the user to tailor the content of the RUN/GEN files, though somewhat differently. In VEDA-FE the Case Manager RUNFile_Tmpl button allows the basic RUN template to be brought up, and if desired carefully edited. However, the Case Manager also has a Control Panel, shown in , where many of the more common switches can be set.

At the beginning of a \<case\>.RUN file the version of the TIMES code being used is identified and some option control statements that influence the information output (e.g., SOLPRINT ON/OFF to see a dump of the solution, OFF recommended) are provided. The LIMROW/LIMCOL options allow the user to turn on equation listing in the .LST file (discussed in the next section) by setting the number of rows/columns of each type to be shown.

Then compile-time dollar control options indicating which solver to use (if not the default to the particular solution algorithm), whether to echo the source code (`$ON`/`$OFFLISTING`) by printing it to the LST file, and that multiple definitions of sets and parameters (`$ONMULTI`) are permitted (that is they can appear more than one time, which TIMES requires since first there are empty declarations for every possible parameter followed by the actual data provided by the user). Further possible dollar control options are also described in the GAMS manual.

Afterwards the content of several so-called TIMES dollar control (or environment) switches are specified. Within the source code the use of these control switches in combination with queries enables the model to skip or activate specific parts of the code. Thus it is possible to turn-on/off variants of the code, e.g. the use of the reduction algorithm, without changing the input data. The meaning and use of the different control switches is discussed in Section . Again these are generally set using the Case Manager/Run form in VEDA/ANSWER.

After the basic control switches, the definition of the set of all timeslices is established by means of the call to the \<case\>\_TS.DD file before any other declarations carried out in the initialization file INITSYS.MOD. This is necessary to ensure the correct ordering of the timeslices for seasonal, weekly, or daynite storage processes. After the definition of the timeslices, the files INITSYS.COM and INITMTY.MOD, which are responsible for the declaration and initialization of all sets and parameters of the model generator, are included.

```{figure} assets/image5.png
:name: image-5
:align: center
```

```{figure} assets/image6.png
:name: example-veda-fe-times
:align: center
Example of a VEDA-FE TIMES \<case\>.RUN file[^16]
```

The line containing the include command for the file initmty.mod can be supplemented by calls for additional user extensions that trigger the use of additional special equations or report routines. The use of these extension options are described in more detail in Section 0.

Afterwards the data dictionary file(s) (BASE.DD, ..., CO2_TAX_HIGH.DD in {numref}`example-veda-fe-times`) containing the user input sets and parameters are included, inserted automatically by VEDA-FE/ANSWER according to the list of scenarios in the Case Manager/Run forms by means of the \$INCLUDE statements. It is normally advisable to segregate user data into "packets" as scenarios, where there may be a single Base scenario containing the core descriptions of the energy system being studied and a series of alternate scenario depicting other aspects of the system. For example, one \<scenario\>.DD file may contain the description of the energy system for a reference scenario, and additional \<alt_scenario\>.DD files (.DDS for ANSWER) may be included containing additions or changes relative to the reference file, for example CO<sub>2</sub> mitigation targets for a reduction scenario, or alternative technology specifications.

The SET MILESTONYR declaration identifies years for this model run based upon those years identified in in VEDA via the Period Defs selected on the Case Manager (and maintained in SysSettings) and the Milestone Years button on the ANSWER run form. The dollar control switch RUN_NAME contains the short name of the scenario, and is used for the name of the results files (\<case\>.VD\*) passed to VEDA-BE.

Next in the example shown in , some runtime switches are activated to request levelized cost reporting and splitting of investment costs into core and the incremental additional cost arising from any technology based discount rate specified in the data. See Section for the full description of these and other control switches.

The last line of the \<case\>.RUN file invokes the file main driver routine (maindrv.mod) that initiates all the remaining tasks related to the model run (pre-processing, coefficient calculation, setting of bounds, equation generation, solution, reporting). Thus any information provided after the inclusion of the maindrv.mod file will not be considered in the main model solve request, though if the user wishes to introduce specialized post-processing of the result that could be added (or better yet handled externally by GAMS code that processes the GDX file).

### GAMS listing file (.LST)

```{figure} assets/image7.png
:name: image-7
:align: center
```

The GAMS listing file echoes the model run. In this file GAMS reports the compile and execution steps, presents a summary of the model statistics and objective function results, and reports any errors, if incurred. Optionally the user can request that the equation listing be turned on by specifying the LIMROW/LIMCOL (number of rows/columns of each type to be shown) and/or the solution dumped (via SOLPRINT) by means of the VEDA-FE Case Manager settings, as shown here.

```{figure} assets/image8.png
:name: request-equation-list-sol-print
:align: center
Requesting Equation Listing and Solution Print.
```

For ANSWER these are handled by manually editing these entries in the GEN file either at runtime, or via the Run menu if the change is to be retrained as the default,

When GAMS takes its 1<sup>st</sup> pass the \<Case\>.LST file will report each of the individual source code modules compiled. \[Note that for any particular TIMES model instance, according to the Run Switch settings, only the routines needed are invoked, as discussed in Section 3.\]

A small snippet from the LST file compilation trace from an ANSWER-TIMES model run of is shown in , where the \"\...\" shows the nesting as one GAMS routine calls another with the appropriate parameters needed.

```{figure} assets/image9.png
:name: gams-compilation-source-code
:align: center
GAMS Compilation of the TIMES Source Code.
```

If an error is encountered during the compilation operation GAMS will tag where the error occurred and report an error code. Most common in this regard is a Domain Error (\$170) where perhaps there was a typo in an item name, as in the example shown in , or the scenarios were not in the proper order and data was attempted to be assigned to a process before it was declared. Further discussion of errors encountered at this and other stages of the run process is found in Section .

```{figure} assets/image10.png
:name: gams-compilation-error
:align: center
GAMS Compilation Error.
```

Once the data and code have been successfully complied, execution takes place, with GAMS calling each TIMES routine needed according to the switches and data for this particular run. Again the LST file echoes this execution phase, as shown in . It is possible, though unlikely, to encounter a GAMS Execution error. The most common cause of this is the explicit specification of zero (0) as the efficiency of a process. An execution error is reported in the \<Case\>.LST file in a manner similar to a compilation error, tagged by "Error" at the point that the problem was encountered.

```{figure} assets/image11.png
:name: gams-execution-times
:align: center
GAMS Execution of the TIMES Source Code.
```

Once execution of the matrix generator has completed GAMS reports the model run statistics (), and automatically invokes the solver.

```{figure} assets/image12.png
:name: cplex-solver-stats
:align: center
CPLEX Solver Statistics.
```

If the OPTION LIMROW/LIMCOL is set to non-0 the equation mathematics are displayed in the list file, by equation block and/or column intersection, as shown in and 12 respectively.

```{figure} assets/image13.png
:name: eq-list
:align: center
Equation Listing Example.
```

 ```{figure} assets/image14.png
:name: var-list
:align: center
Variable Listing Example.
```

And if the SOLPRINT=ON option is activated then the level and marginals are reported as shown in .

 ```{figure} assets/image15.png
:name: solution-dump
:align: center
Solution Dump Example.
```

Upon successful solving the model the solution statistics are reported (Figure 14), where in this case CPLEX was used to solve a MIP model variant (in this example), and the report writer invoked to finish up by preparing the report. If the solver is not able to find an optimal solution, a non-Normal solve status will be reported, and the user can search the LST file for the string \"INFES\" for an indication of which equations are preventing model solution. Again, further information on the possible causes and resolution of such errors is found in Section .

 ```{figure} assets/image16.png
:name: solver-solution-summary
:align: center
Solver Solution Summary.
```

The actual production of the dump of the model results is performed by the report writer for ANSWER resulting in a \<Case\>.ANT file which is imported back into ANSWER after the run complete and/or the GDX2VEDA utility prepared by GAMS and DecisionWare to facilitate the exchange of information from GAMS to VEDA-BE, which may be used with both VEDA-FE and ANSWER.

### Results files

The TIMES report writing routine produces two sets of results-related outputs (along with the quality control LOG discussed in the next section). The \<case\>.ANT file is an ASCII text file, with results ready for import into ANSWER. The GAMS Data eXchange file (GDX) contains all the information associated with a model run \[input data, intermediate parameters, model results (primal and dual)\] in binary form. The GDX file may be examined by means of the GAMSIDE, available from the Windows Start Menu in the GAMS folder (or as a shortcut from the desktop if put there), if one really wants to dig into what's happening inside of a TIMES run (that is, the set members, preprocessor calculations, the model solution and the reporting parameters calculated).

A more powerful feature within the GAMSIDE is a GDXDIFF facility under Utilities. As seen in  15, the utility shows the differences between all components, comparing two model runs. Within the GDXDIFF utility, the user identifies the GDX files from the two runs and requests the resulting comparison GDX be prepared. The display then shows any differences between the two runs. The GDXDIFF is most effectively used by instructing VEDA to Create DD for the two runs via the Options and Case Manager forms, as shown in . Once the comparison GDX has been created, it is viewed in the GAMSIDE. By sorting by Type and scanning down one Symbol at a time, one can determine exactly what input data being sent to GAMS for the two runs is different.

 ```{figure} assets/image17.png
:name: gams-ide-view-gdxdiff
:align: center
GAMSIDE View of the GDXDIFF Run Comparison.
```

However, the most common use of the GDX is its further processing to generate files for the result analysis software VEDA-BE[^17]. ETSAP worked with GAMS a number of years ago to develop a standalone utility (GDX2VEDA) to process the GAMS GDX file and produce the files read into VEDA-BE. The GDX2VEDA utility process a directives file (TIMES2VEDA.VDD) to determine which sets and model results are to be included and prepare said information for VEDA-BE. A general default version of the VDD is distributed with TIMES in the source code folder (for core TIMES, Stochastics, and MACRO), but may be augmented by the user if other information is desired from the solution. However, the process of changing the VDD should be done in consultation with someone fully familiar with the GAMS GDX file for TIMES and the basics of the GDX2VEDA utility. See Part V, Appendix B, for further information on the GDX2VEDA utility and VDD directives file.

 ```{figure} assets/image18.png
:name: image18
:align: center
```

 ```{figure} assets/image19.png
:name: veda-setup-data-only-gdx
:align: center
VEDA Setup for Data Only GDX Request.
```

The call to the GDX2VEDA routine is embedded in the VTRUN/ANSRUN.CMD command routines. There are three files produced for VEDA-BE by the GDX2VEDA utility: the \<Case\>.VD data dump with the attributes, and associated VDE (set elements), VDS (sets definition). In addition, VEDA-FE and ANSWER produce a \<Case\>.VDT (topology) file with the RES connectivity information. These files never require user intervention, though users wishing to post-process the GDX2VEDA results with their own tailored software, rather than VEDA-BE, might choose to parse the VD\* files to extract the desired information.

Note that for both ANSWER and VEDA-BE, for the most part low-level (that is commodity/process) results are reported, along with some aggregate cost numbers (such as regional and overall objective function). It is left up to the user to construct relevant sets and tables in VEDA-BE to organize and aggregate the results into meaningful tables. Refer to Part V for a discussion of how to go about assembling report tables in VEDA-BE. For ANSWER the user is left with only the raw results and thereby needs to come up with their own approach to producing useful usable reporting tables, or use VEDA-BE.

In addition, as discussed in Section 3.10, there are a number of switches that control the report writer itself in terms of how it calculates certain outputs and prepares the results as part of the post-processing. Collectively these mechanisms provide the user with a wide range of reporting results and tools for dissecting and assembling the modeling results as part of effectively using TIMES to conduct energy policy analyses.

### QA check report (LOG)

In order to assist the user with identifying accidental modelling errors, a number of sanity checks are done by the model generator. If incorrect or suspicious specifications are found in these checks, a message is written in a text file named QA_CHECK.LOG, in the working folder. The checks implemented in TIMES Version 4.8.0 are listed in {numref}`times-qa-checks`. The "Log entry" column shows the identification given for each suspicious specification.

```{list-table} TIMES Quality Assurance Checks (as of Version 4.8.0)
:name: times-qa-checks
:header-rows: 1

* - Type[^18]
  - Message / Description
  - Severity
  - Log entry
* - STD
  - User-provided G_YRFR values are not valid year fractions:
  <br>The sum of year fractions over timeslices does  not sum up correctly. The fractions are normalized so that they sum up to 1 over the  full year.
  - warning
  - region, ts-level, timeslice
* - STD
  - Delayed Process but PAST Investment:
  <br>Process availability has been delayed by using PRC_NOFF or NCAP_START, but also has existing capacity.
  - warning
  - region, process
* - STD
  - Commodities/processes defined at non-existing TSLVL:
  <br>PRC_TSL or COM_TSL has been specified on a timeslice level not used in the model.
  - severe error
  - number of COM/PRC reset to ANNUAL
* - STD
  - NCAP_TLIFE out of feasible range:
  <br>NCAP_TLIFE specified has a value of either less than 0.5 or greater than 200. Values less than 0.5 are reset to 1.
  - warning
  - region, process, vintage
* - STD
  - Inconsistent CAP_BND(UP/FX) defined for process capacity:
  <br>CAP_BND(UP/FX) value specified has a value lower than the residual capacity remaining available in the period, and retirements are disabled.
  - warning
  - region, process, period
* - STD
  - Flow OFF TS level below variable TS level:
  <br>A PRC_FOFF attribute with a timeslice below the flow level has been specified; the OFF specification is ignored.
  - warning
  - region, process, commodity, timeslice
* - STD
  - COM_FR does not sum to unity (T=first year):
  <br>The sum of COM_FR over all timeslices at the COM_TSL level is not equal to 1, and is therefore normalized to 1.
  - warning
  - region, commodity, milestone
* - STD
  - Unsupported diverging trade topology:
  <br>The model generator detects an unsupported complex topology of an IRE process, which cannot be properly handled
  - error
  - region, process
* - STD
  - FLO_EMIS with no members of source group in process:
  <br>A FLO_EMIS with a source group that has no members for the process has been specified. The parameter is ignored.
  - severe error
  - region, process, group, commodity
* - STD
  - Unsupported FLO_SHAR: C not in RPC or CG:
  <br>The commodity in FLO_SHAR is either not in the process topology or not a member of the group specified
  - error
  - region, process, commodity, group
* - STD
  - FLO_SHAR conflict: Both FX + LO/UP specified, latter ignored:
  <br>Too many FLO_SHAR bounds are specified, if both FX and LO/UP are specified at the same time.
  - warning
  - region, process, vintage, commodity, group
* - STD
  - Inconsistent sum of fixed FLO_SHARs in Group:
  <br>All flows in a group have a fixed share, but the sum of the fixed FLO_SHAR values is not equal to 1.
  - warning
  - region, process, vintage, group
* - STD
  - Defective sum of FX and UP FLO_SHARs in Group:
  <br>All flows in a group have either a fixed or an upper share, but the sum of the FLO_SHAR values is less than 1.
  - warning
  - region, process, vintage, group
* - STD
  - Excessive sum of FX and LO FLO_SHARs in Group:
  <br>All flows in a group have either a fixed or a lower share, but the sum of the FLO_SHAR values is greater than 1.
  - warning
  - region, process, vintage, group
* - STD
  - NCAP_AF/ACT_BND Bounds conflict:
  <br>Value at PRC_TS level and below, latter ignored
  - warning
  - region, process, vintage, timeslice
* - STD
  - NCAP_AF Bounds conflict:
  <br>FX + LO/UP at same TS-level, latter ignored
  - warning
  - region, process, vintage, timeslice
* - STD
  - FLO_SHAR/FLO_FR Bounds conflict:
  <br>Value at RPCS_VAR level and below, latter ignored
  - warning
  - region, process, vintage, timeslice
* - STD
  - FLO_SHAR Bounds conflict:
  <br>FX + LO/UP at same TS-level, latter ignored
  - warning
  - region, process, vintage, commodity, group
* - STD
  - COM_BNDNET/COM_BNDPRD/IRE_BND Bounds conflict:
  <br>Value at COM_TS level and below, latter ignored
  - warning
  - region, milestone, commodity, timeslice
* - STD
  - IRE_FLO import commodity not in TOP_IRE:
  <br>An invalid IRE_FLO with the imported commodity not in the process topology has been specified
  - error
  - region, process, commodity
* - STD
  - CHP process with zero CEH but only upper bound on CHPR:
  <br>A CHP process has only an upper bound on NCAP_CHPR, but a zero or missing NCAP_CEH, which indicates a modelling error
  - error
  - region, process
* - STD
  - Year Fraction G_YRFR is ZERO:
  <br>A timeslice with G_YRFR is within the timeslice tree. This should actually never happen, because TIMES automatically removes timeslices with a zero year fraction from the active timeslices.
  - fatal
  - region, timeslice
* - STD
  - Illegal system commodity in topology:
  <br>ACT / ACTGRP is a reserved name which should never be used as a commodity in the model topology.
  - fatal
  - region, process
* - STD
  - Commodity in CG of process P but not in topology:
  <br>A commodity group assigned to a process contains members not in the process topology (or no members in the process topology).
  - severe error
  - region, process, comm.group
* - STD
  - Elastic Demand but either COM_BPRICE/ELAST/VOC missing:
  <br>Either a demand that has COM_ELAST or COM_STEP defined but does not have COM_BPRICE, COM_ELAST, or COM_VOC, defined.
  - warning
  - region, commodity, LO/UP
* - STD
  - Commodity type is also a commodity:
  <br>Commodity types are reserved names that cannot be used as commodity names.
  - fatal
  - region, commodity type
* - STD
  - Commodity has ambiguous base type:
  <br>The base type for some commodity is not uniquely defined. All commodities should have a unique base type defined (NRG/MAT/DEM/ENV/FIN).
  - severe error
  - region, commodity
* - STD
  - Demand: DEM commodity with missing COM_PROJ Projection:
  <br>A demand commodity without any demand projection is found.
  - warning
  - region, commodity
* - STD
  - Demand: COM_PROJ specified for non-DEM commodity:
  <br>Demand is projected for a non-demand commodity.
  - warning
  - region, commodity
* - STD
  - Phantom entries found in topology (process/commodity not in SET PRC/COM):
  <br>This error is usually triggered when a GAMSTD domain violation has occurred, which may cause unexpected behaviour of the GAMS code.
  - fatal
  - region, process, commodity
* - STD
  - Process with missing or mismatched CG/PRC_ACTUNIT:
  <br>Process with missing or several PRC_ACTUNT entries.
  - fatal
  - region, process
* - STD
  - Illegal dependency of substituted auxiliary commodities C1 and C2 in FLO_SUM:
  <br>This error should not occur, because the GAMSTD code should make sure that C1 and C2 are not both substituted. If this error is issued, contact TIMES maintenance.
  - fatal
  - region, process, commodity1, commodity2
* - STD
  - NCAP_AFX defined for NON-vintaged dispatchable process with ACT_MINLD:
  <br>Shaping of NCAP_AF is not supported for non-vintaged processes having ACT_MINLD defined.
  - warning
  - region, process
* - STD
  - Active currency but not member of set CUR:
  <br>Currency referred to in some attributes is not defined in the set CUR.
  - fatal
  - currency
* - STD
  - Internal Region without Discount Rate:
  <br>TIMES requires a discount rate defined for all internal regions.
  - fatal
  - region
* - STD
  - Active Currency without Discount Rate:
  <br>A currency is being used without discount rate, or conversion to another currency that has a discount rate.
  - fatal
  - region, currency
* - STD
  - Process with zero PRC_ACTFLO for C in PG:
  <br>A zero PRC_ACTFLO has been specified for a commodity in the primary group.
  - fatal
  - region, process, commodity
* - STD
  - Duplicate parent timeslices –- Fatal error:
  <br>A timeslice has been mapped below several parent timeslices.
  - fatal error
  - region, timeslice
* - STD
  - Inconsistent CAP_BND(UP/LO/FX) defined for process capacity:
  <br>CAP_BND(…,UP) is lower than CAP_BND(…,LO), and therefore the lower bound is automatically reduced to the upper bound.
  - warning
  - region, milestone, process
* - STD
  - Elastic Demand but missing BPRICE for some MILESTONYR - using tail extrapolation:
  <br>When elastic demands are used and Base Prices are defined but are missing for some Milestone year(s), they are completed by extrapolation.
  - warning
  - region, commodity
* - STD
  - Flow OFF TS level below VARiable TS level:
  <br>A PRC_FOFF attribute has been defined for a timeslice below the timeslice level of the flow variable, and therefore the specification can only be ignored.
  - warning
  - region, process, commodity, timeslice
* - STD
  - ACT_EFF shadow group contains only an auxiliary flow:
  <br>ACT_EFF has been specified for a shadow group that does not contain any other flows but an auxiliary.  In this case the efficiency is applied to the auxiliary flow (while normally auxiliary flows are excluded from ACT_EFF).
  - warning
  - region, process, commodity
* - STD
  - Inconsistent/spurious process transformation parameters:
  <br>A process commodity flow has been defined by several transformation attributes, which are mutually inconsistent.
  - severe error
  - region, process, commodity
* - STD
  - Unsupported dynamic timeslice trees with overlap -- Fatal:
  <br> When using the dynamic timeslice tree functionality, the timeslice tree has been defined with branches that are shared by the different configurations. Such timeslice trees are not supported.
  - fatal error
  - region, milestone
* - XTD
  - Same Commodity IN and OUT of non-STG process:
  <br>A process has been defined to have the same commodity as an input and an output, and it is not a storage process; that is not supported.
  - severe error
  - region, process, commodity
* - XTD
  - IRE Process with invalid Parameters:
  <br>Some FLO_FUNC, FLO_SUM, FLO_SHAR or UC_FLO parameter not supported for IRE processes has been specified.
  - error
  - region, process, com-group
* - XTD
  - Invalid Commodity / Group used in ACT_EFF - parameter ignored:
  <br>An invalid ACT_EFF attribute with a CG not containing members on the shadow side or in the PG has been specified.
  - error
  - region, process, group
* - XTD
  - FLO_SUM Commodity Not in RPC - parameter ignored:
  <br>An invalid FLO_SUM has been defined where the commodity is not in the process topology.
  - error
  - region, process, group, commodity
* - XTD
  - FLO_SUM Commodity Not in CG1 - parameter ignored:
  <br>An invalid FLO_SUM has been defined where the commodity is not a member of the first group, CG1.
  - error
  - region, process, group, commodity
* - XTD
  - PTRANS between CG1 and CG2 in both directions:
  <br>A FLO_FUNC or FLO_SUM between groups CG1 and CG2 has been specified in both directions.
  - severe error
  - region, process, group1, group2
* - XTD
  - RPC in TOP not found in any ACTFLO / FLO_SHAR / FLO_FUNC / FLO_SUM:
  <br>Some commodity in the topology does not seem to be tied to anything, at least by means of any of the most common attributes; the user is advised to check that this is not a modelling error.
  - warning
  - region, process, commodity, IN/OUT
* - XTD
  - Empty Group in FLO_SUM/FLO_FUNC/FLO_SHAR:
  <br>A group that has no members in the process topology has been used for a process attribute. Detects also an empty primary group.
  - severe error
  - region, process, group
* - XTD
  - Both NCAP_AF and NCAP_AFA specified for same process:
  <br>Specifying both NCAP_AF(bd) and NCAP_AFA(bd) for an ANNUAL level process is ambiguous and should be avoided.
  - warning
  - region, process, vintage
* - XTD
  - Too Long Commodity Lead Time:
  <br>A value of NCAP_CLED \> NCAP_ILED has been specified
  - warning
  - region, process, commodity
* - XTD
  - CHP parameter specified for Non-CHP process:
  <br>An NCAP_BPME, NCAP_CHPR or NCAP_CEH parameter has been specified for a process that is not defined to be CHP.
  - error
  - region, process, vintage
* - XTD
  - PG of CHP process consists of single commodity yet has a CHP-ratio:
  <br>A CHP process has a NCAP_CHPR specified but has only a single commodity in the primary group.
  - warning
  - region, process
* - XTD
  - Found CHP processes without CHP-ratio defined:
  <br>A CHP process has no NCAP_CHPR defined
  - warning
  - number of such processes
* - XTD
  - Found CHP processes with PG commodity efficiencies - unsupported:
  <br>Specifying ACT_EFF on some flow(s) in the PG is not supported for CHP processes, and may lead to unexpected results.
  - warning
  - region, process
* - XTD
  - Found CHP processes without electricity in the PG:
  <br>A CHP process is found with no electricity commodity in the PG.
  - warning
  - region, process
* - XTD
  - Standard Flow Process with invalid Attributes:
  <br>A standard process has IRE qualification or UC_IRE parameters.
  - warning
  - region, process
```

## Errors and their resolution

Errors may be encountered during the compilation, execution (rarely), or solve stages of a TIMES model run. During the compilation step, if GAMS encounters any improperly defined item the run will be halted with a Domain or similar error and the user will need to examine the TIMES quality control LOG or GAMS listing (LST) files to ascertain the cause of the problem. While such problems are not normally encountered, some that might occur include:
- an item name was mistyped and therefore not defined;
- an item was previously defined in one scenario but defined differently in another;
- an item was not properly declared for a particular parameters (e.g., a non-trade process using an IRE parameter), and
- scenarios were specified for the run in the wrong order so a data reference is encountered before the declaration (e.g., a bound on a new technology option is provided before it has been identified).

During the execution phase, if GAMS encounters any runtime errors it will halt and report where the error occurred in the LST file. While such problems are not normally encountered some causes of an execution error might be:
- an explicit 0 is provided for an efficiency resulting in a divide by 0, and
- there is a conflict between a lower and upper bound.

Most commonly errors are encountered during the solve process, resulting in an infeasibility. Some causes of the model not being able to solve might be:
- due to bounds, the energy system cannot be configured in such a way as to meet the limit;
- owing to mis-specifying the demand serviced by a device, there is no or not enough capacity to satisfy said demand, and
- the RES is not properly connected so a needed commodity is not able to reach the processes needing it.

To identify the cause of a solve error, if using CPLEX the user can activate the Infeasibility Finder (set in the CPLEX.OPT as default (via the IIS command) in VEDA-FE Case Manager or said file distributed with ANSWER). The CPLEX Infeasibility Finder will identify the explicit row/columns corresponding to the first infeasibility encountered and list the conflict involved in the \<Case\>.LST file, such as shown here where the electricity balance equation can't be satisfied (due
to a limit being imposed on the first year electric grid capacity that is too small).

```
Implied bounds make row 'EQG_COMBAL('STARTER'.2013.'ELCD'.'FAD')' infeasible.
```

This helps with tracking down the culprit, but the user still needs to figure out why the problem occurred. When using a solver other than CPLEX, or if the Infeasibility Finder is not activated, then the solution dump will be tagged for all the potentially interrelated model variables/equations that were not in equilibrium at the time the solve stopped. The user can find these by searching the LST file for the string \"INFES\".

As a last resort, the model can be run with the equation listing turned on by setting LIMROW/LIMCOL to, say, 1000 in the \<case\>.RUN (via the Case Manager) / GEN (via Edit the GEN from the Run form) file, although the equations in this form can be challenging to interpret.


[^14]: For simplicity, it has been assumed in this description that the name of the \<case\>.run/gen (for VEDA-FE/ANSWER respectively) file and the \*.dd files are the same (\<case_name\>). The names of the two files can be different, and usually are with BASE.dd the main dataset with non-Base scenarios included in a run having \<scenario\>.dd/dds names (for VEDA-FE/ANSWER respectively). The listing file generated by GAMS always has the same name of the \<case\>.run/gen file. The name of the gdx files can be chosen by the user on the command line calling GAMS (e.g. gams mymodel.run gdx = myresults will result in a file called myresults.gdx), however, out of VEDA-FE/ANSWER the files are \<case\>.gdx.

[^15]: The basics of the TIMES2VEDA.VDD control file and the use of the result analysis software VEDA-BE are described in Part V.

[^16]: The ANSWER GEN file will have similar content though with some syntax and perhaps slightly augmented scripts.

[^17]: The basics of the TIMES2VEDA.VDD control file and the use of the result analysis software VEDA-BE are described in Part V.

[^18]: STD=standard QA check (always done), XTD=extended QA check (activate with XTQA)