# [MC number] [Manuscript Title] Validation and Replication results

> INSTRUCTIONS: Once you've read these instructions, DELETE THESE AND SIMILAR LINES. Also delete lines that include "{{  SOME-TEXT }}".

> INSTRUCTIONS: In the above title, replace [Manuscript Title] with the actual title of the paper, and [MC number] with the Manuscript Central number (e.g., AEJPol-2017-0097)

> INSTRUCTIONS: Go through the steps to download and attempt a replication. Document your steps here, the errors generated, and the steps you took to alleviate those errors. This includes apparently minor steps, such as adjusting directories, or installing packages, any deviations from the README. If the README did not specify a certain step or action, describe why you chose that action, and whether it should be detailed in the README. All figures and tables should be evident once you are done, i.e., saved to disk. If this is not done in code, please add code to do so.

> INSTRUCTIONS: To compare images and tables, annotated screenshots from the manuscript can be helpful for comparison, highlighting where differences were found.

> INSTRUCTIONS: Leave these lines here:

> Some useful links:
> - [Official Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code)
> - [Step by step guidance](https://aeadataeditor.github.io/aea-de-guidance/) 
> - [Template README](https://social-science-data-editors.github.io/template_README/)

## SUMMARY

> INSTRUCTION: The Data Editor will fill this part out. It will be based on any [REQUIRED] and [SUGGESTED] action items that the report makes a note of.

> INSTRUCTION: The next line CLOSES the summary.

In assessing compliance with our [Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code), we have identified the following issues, which we ask you to address:


### Action Items (manuscript)

> INSTRUCTION: Add all manuscript related items here.

> INSTRUCTION: If any changes are needed, leave the following text in; otherwise, remove it:

> [REQUIRED] If making changes to the manuscript, please describe in a response letter to the Editor and Data Editor any deviations from the conditionally accepted version (as approved by the Editor) and their impact, especially of key estimates or outcomes. Email that response letter to the Data Editor at dataeditor@aeapubs.org, referencing the manuscript number.


### Action Items (openICPSR)

> INSTRUCTION: leave the next few lines in, do not delete them.

-----action items go here------

> If your openICPSR deposit appears to be "locked", please follow [these instructions](https://aeadataeditor.github.io/aea-de-guidance/FAQ.html#you-can-recall-the-submission).

> The openICPSR submission process has changed. If you have not already done so, please "Change Status -> Submit to AEA" from your deposit Workspace.

> [NOTE] Since July 1, 2021, we will publish replication packages as soon as all requested changes to the deposit have been made. Please process any requested changes as soon as possible.

> INSTRUCTION: ALWAYS do "Data description", "Code description". If data is present, ALWAYS do "Data checks". If time is sufficient (initial assessment!), do "Replication steps", if not, explain why not.

## General


> INSTRUCTIONS: Check off the following sections/elements that you find in either the README provided by the authors, or in the authors' online appendix (rare).
> INSTRUCTIONS: ==>  Workflow stage: You are now going from *In Progress* to *Code*

- [ ] Data Availability and Provenance Statements
  - [ ] Statement about Rights
  - [ ] License for Data (optional, but recommended)
  - [ ] Details on each Data Source
- [ ] Dataset list
- [ ] Computational requirements
  - [ ] Software Requirements
  - [ ] Controlled Randomness (as necessary)
  - [ ] Memory, Runtime, and Storage Requirements
- [ ] Description of programs/code
  - [ ] License for Code (Optional, but recommended) 
- [ ] Instructions to Replicators
  - [ ] Details (as necessary)
- [ ] List of tables and programs
- [ ] References


> INSTRUCTIONS: Leave this in, when any of the sections is lacking. Remove the entire section only if the README has all the pieces necessary (up to minor imprecisions).

> [REQUIRED] As specified in the [Policy](https://www.aeaweb.org/journals/data/data-code-policy) and the [DCAF](https://www.aeaweb.org/journals/forms/data-code-availability), the README shall follow the schema provided by the [Social Science Data Editors' template README](https://social-science-data-editors.github.io/guidance/template-README.html).
  - All elements are required, unless a modifier is used in the above list.

## Data description

### Data Sources

> INSTRUCTIONS: Identify all INPUT data sources. Create a list (and commit the list together with this report) (not needed if filling out the "Data Citation and Information report"). For each data source, list in THIS document presence or absence of source, codebook/information on the data, and summary statistics. Summary statistics and codebook may not be necessary if they are available for public use data. In all cases, if the author of the article points to an online location for such information, that is OK. IN THIS DOCUMENT, point out only a summary of shortcomings.

> INSTRUCTIONS: For all data sources, check for a data citation. Oftentimes authors will cite the **paper** in which a dataset is originally used, but this is not a *data* citation. If you have found what you think to be a data citation, quote it in the report as shown below for the "Example data". 

#### Example data

- Dataset is not provided, but a link is provided in the README
- Access conditions are not described. It turns out, the website requires registration and payment of a fee
- The data are cited in the references section of the manuscript and the README. Data citation:

> Bureau of Labor Statistics. 2000–2010. “Current Employment Statistics: Colorado, Total Nonfarm, Seasonally adjusted - SMS08000000000000001.” United States Department of Labor. http://data.bls.gov/cgi-bin/surveymost?sm+08 (accessed February 9, 2011).

#### All data files provided

> INSTRUCTIONS: Please verify that the following list is complete, if pre-filled.
> INSTRUCTIONS: You can generate a similar list manually, or add manually to this list.
> INSTRUCTIONS: For large deposits, this can be done using the "Git Bash" program:
> INSTRUCTIONS: > find . -name \*.dta
> INSTRUCTIONS:  will list all Stata datasets. Replace `dta` with `.Rdata` or any other extension to find other datafiles.

```
{{ data-list.txt }}
```

### Analysis Data Files

> INSTRUCTIONS: Separately, identify any analysis data file provided. Analysis data files are produced by code in the deposit from data sources. Not every deposit will have these.

- [ ] No analysis data file mentioned
- [ ] Analysis data files mentioned, not provided (explain reasons below)
- [ ] Analysis data files mentioned, provided. File names listed below.
- [ ] Analysis data files not mentioned, but provided.

Example:

```
./Output_Empirical/data/regression_main.dta
```

## Data deposit

> INSTRUCTIONS: Most deposits will be at openICPSR, but all need to be checked for complete metadata. Detailed guidance is at [https://aeadataeditor.github.io/aea-de-guidance/](https://aeadataeditor.github.io/aea-de-guidance/). 

### Requirements 

> INSTRUCTIONS: Check that these requirements are met. All of these should be met for openICPSR deposits, for other deposits, check out [this page](https://aeadataeditor.github.io/aea-de-guidance/guidelines-other-repositories).

- [ ] README is in TXT, MD, PDF format
- [ ] Deposit has no ZIP files
- [ ] Title conforms to guidance (starts with "Data and Code for:" or "Code for:", is properly capitalized)
- [ ] Authors (with affiliations) are listed in the same order as on the paper

> INSTRUCTIONS: If any of the above are NOT checked, leave the related [REQUIRED] element here. Otherwise, delete the line.

> [REQUIRED] Please ensure that a ASCII (txt), Markdown (md), or PDF version of the README are available in the data and code deposit.

> [REQUIRED] Deposit should not have ZIP files visible. 
  - on openICPSR: ZIP files should be uploaded to openICPSR via "Import from ZIP" instead of "Upload Files". Please delete the ZIP files, and re-upload using the "Import from ZIP" function.
  - on other platforms: Please consult with your repository helpdesk how to "import from ZIP".

> [REQUIRED] Please review the title of the deposit as per our guidelines (below).

> [REQUIRED] Please review authors and affiliations on the deposit. In general, they are the same, and in the same order, as for the manuscript; however, authors can deviate from that order.

> INSTRUCTIONS: Leave the following line in the report if any of the above are checked:

> Detailed guidance is at [https://aeadataeditor.github.io/aea-de-guidance/](https://aeadataeditor.github.io/aea-de-guidance/), for non-ICPSR deposits, check out [this guidance](https://aeadataeditor.github.io/aea-de-guidance/guidelines-other-repositories).

### Deposit Metadata

> INSTRUCTIONS: Some of these are specific to openICPSR (JEL, Manuscript Number). Others may or may not be present at other trusted repositories (Dataverse, Zenodo, etc.). Verify all items for openICPSR, check with supervisor for other deposits.

- [ ] JEL Classification (required)
- [ ] Manuscript Number (required)
- [ ] Subject Terms (highly recommended)
- [ ] Geographic coverage (highly recommended)
- [ ] Time period(s) (highly recommended)
- [ ] Collection date(s) (suggested)
- [ ] Universe (suggested)
- [ ] Data Type(s) (suggested)
- [ ] Data Source (suggested)
- [ ] Units of Observation (suggested)

> INSTRUCTIONS: Go through the checklist above, and then choose ONE of the following results:

- [NOTE] openICPSR metadata is sufficient.

or

- [REQUIRED] Please update the openICPSR metadata fields marked as (required), in order to improve findability of your data and code supplement. 

and/or

- [SUGGESTED] We suggest you update the openICPSR metadata fields marked as (highly recommended), in order to improve findability of your data and code supplement. 
- [SUGGESTED] We suggest you update the openICPSR metadata fields marked as (suggested), in order to improve findability of your data and code supplement. 


For additional guidance, see [https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html).


> INSTRUCTIONS: ==>  Workflow stage: You have now completed *PartA*. Please update Jira and prepare to discuss with lead RA or supervisor!

