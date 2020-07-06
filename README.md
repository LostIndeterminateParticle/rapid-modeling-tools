# Rapid Modeling Tools

## Why Was This Tool Made?

Rapid Modeling Tools (RMT) capitalizes on the wealth of system model information described in a small number of common modeling patterns, from a modeling structure perspective. After identifying a common modeling pattern, the systems engineering task becomes that of a data entry problem resulting in many systems engineering products capturing data in spreadsheets. Spreadsheets alone lack the structure to mark differences in the kinds of information captured (components vs. functions), readily apparent to computers or even non-subject matter experts. Meanwhile, subject matter experts endow the data with semantic annotations without understanding how to express those annotations through the data structures. Thus, RMT seeks to address these issues by combining the data collection, semantic annotation and model creation into one workflow. Inspired by the approach taken by the Maple MBSE tool and the Excel Import in Cameo Systems Modeler, RMT collects data from subject matter experts and non-subject matter experts in the form of an Excel spreadsheet and then creates a fully formed system model in the MagicDraw/Cameo Systems Modeler authoring tool.

Commonly on MBSE projects, modeling professionals find themselves overwhelmed by the volume of information to capture, spending inordinate amounts of time transcribing those data. Ultimately, hurting the productivity of the team and preventing them from taking full advantage of their models; preparing queries and reports to support the larger engineering team. Automating the most straightforward and voluminous parts of the data wrangling effort, collecting and structuring the data according to common modeling patterns, allows the modeling experts to focus on best uses of those data.

### If Inspired by Commercial Tools, Why Make a New One?

Primarily because it involves filling in gaps left behind by existing tools.

For one - Maple MBSE does not do comparisons between baseline models and updates on its own. It relies upon the facilities of the Teamwork Cloud or other modeling tools. Having Ingrid perform the change calculations makes it independent of the modeling tool used. It should be compatible with Cameo, Integrity Modeler, Rhapsody, Papyrus, or any other modeling tool. This also allows for engineers that do not have access to any of these tools to act as configuration managers to check that the collected and updated data are ready to go into the model.

For another - Cameo importers work well with string or value fields but do not handle importing the connections between modeling elements gracefully. Thus, making complete model updates requires additional effort. Here we can point out that the existence of the Excel and CSV imports lead the Ingrid team to de-emphasize bulk loading of these values and focus on the development of importing model elements and their links to each other.

## About

RMT affords the engineer SME the ability to quickly add, update, or delete design information via a spreadsheet interface which is converted to a set of instructions generated by the `ingrid`  component of RMT.  RMT consists of two seperate components: 

* `ingrid` is a python application which translates spreadsheet data into a set of JSON instructions which are read by the other component of RMT, the `player-piano`.
* `player-piano` is a Groovy script that is used as a macro within the MagicDraw UML/SysML authoring tool to create, modify, or remove model elements based upon the JSON instructions produced by `ingrid`. 

> **Note:** RMT requires MagicDraw or Cameo Systems Modeler. RMT has been tested with **Cameo 19.0**.

## Installation

- Clone `Rapid Modeling Tools`
  ```bash
  git clone https://github.com/gtri/rapid-modeling-tools.git
  ```
    > Cloning the repository provides you access to add meta model JSON descriptions and update the `player-piano` to create novel model elements.

### Ingrid
#### Windows
- Install [miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Install the Ingrid application
  ```bash
  cd ingrid
  bash install.bat
  ```
#### Linux / Mac
- Install [miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Install the Ingrid application
  ```bash
  cd ingrid
  bash install.sh
  conda activate model_processing
  ```
#### Additional Details

- Detailed instructions can be found in the [README.md](ingrid/README.md) in the `ingrid` directory for usage with anaconda-project and without anaconda-project

### Player Piano

- With MagicDraw open locate the **Tools** menu
- Select `Tools > Macros > Organize Macros`
- Select the `New` button to create a new macro. This will open the `Macro Information` dialog box.
- In the `Macro Information` dialog box, enter the following information:
  - `Name`: Player Piano
  - `Macro Language`: Groovy
  - `File`: browse the file explorer (opened by clicking on the three dots button) to the `.../Rapid Modeling Tools/player-piano/player-piano-script.groovy` groovy script.

- Detailed instructions with images can be found in the [README.md](player-piano/README.md) in the `player-piano` directory

## Getting Started

The [ingrid-quick-start](ingrid-quick-start/README.md) provides a basic starting spreadsheet with an example (model included) to show how to calculate model modification commands, both create and compare.

Each of these projects has their own sub README with more details. Please contact `ingrid-nerdman@gtri.gatech.edu` with questions.

## Goals to Bring Rapid Modeling Tools to a 1.0 Release:

Owing to the difficulty of automatic testing with the MagicDraw software the exact MagicDraw versions supported remains unknown. However, we have seen success with Cameo 19.0 and Python 3.6+.

- Establish Ingrid Nerdman as a MagicDraw plugin
- Expand coverage of the UML Metamodel in both JSON subgraph definition and Player Piano capability

This tool is intended for MBSE professionals and advanced technical users. Users of this tool set do so at their own risk.
Each of these projects has their own sub README with more details. Please contact ingrid-nerdman@gtri.gatech.edu with questions.

## Design

### Use Cases (purposes)
Rapid Modeling Tools (RMT) are designed to help domain experts and engineers express their efforts in a system model without having to know the intimate details of SysML.  The below use cases capture the essence of how domain expert engineers and modeling engineer interact with RMT to support system engineering and domain engineering processes.

![UseCases](diagrams/Rapid%20Modeling%20Tool%20-%20Use%20Cases.png)

### Components
The RMT is comprised of four major components: an ingestion grid that captures design patterns, a set of model patterns, a translator which matches design patterns to model patterns and creates lists of model transformations, and then the player piano which will execute the model transformations using the Cameo Systems Modeler API.  The component hierarchy, and the hiearchy within usage context are shown in the next two images below.

![ComponentHierarchy](diagrams/Rapid%20Modeling%20Tool%20-%20Component%20Hierarchy.png)

![ComponentHierarchyInContext](diagrams/Rapid%20Modeling%20Tool%20Context.png)


### Workflows
At a high level, the notional workflow is captured below in a sequence diagram.  The domain expert / engineer will inform the modeling expert of the design patterns they wish to capture.  The modeling expert will create a way of capturing that in a spreadsheet (ingestion grid) and a modeling pattern file (captured in JSON) that matches that design pattern.  The domain expert will then fill out the spreadsheet and give it to the modeling expert.  The modeling expert will then use the rest of the rapid modeling tools suite to translate the design patterns captured in the spreadsheet(s) into model transformation lists, then execute those model transformations using the Cameo Systems Modeler built-in API.


![HighLevelSequencing](diagrams/Usage%20-%20High%20Level%20Sequence%20Diagram.png)

![LowLevelSequencing](diagrams/Usage%20-%20Low%20Level%20Sequence%20Diagram.png)

### Item Flows

The items flowing across the components are depicted below.  There are four major items that flow using three major formats:

 - Design Patterns <--> Excel Workbook / Worksheets
 - Modeling Patterns <--> JSON
 - Model Transformation Lists <--> JSON
 - Model Transformations <--> CSM (MagicDraw) API Calls

![ComponentHierarchyInContext](diagrams/Rapid%20Modeling%20Tool%20-%20Internal%20Flows.png)

![ComponentHierarchyInContext](diagrams/Rapid%20Modeling%20Tool%20Context%20-%20Internal%20Flows.png)

## Attribution

Developed at Georgia Tech Research Institute by Shane Connelly and Bjorn Cole. Government sponsorship (SOCOM TALOS) acknowledged.
