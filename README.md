# StudyHelp Academic Tutoring Network

- **Unit**: Data Structures and Algorithms (`COMP1002` / `DSA1002`) — Assignment 1
- **Study Period**: 2023 Trimester 1A
- **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
- **Overall Unit Mark**: 89 (High Distinction)

> **README for Assignment Submission**: [README for Assignment Submission](ORIGINAL_README.md)

## Assignment context

The assignment asked for a student-help system in which students tutor one another in particular academic units. It required dynamic abstract data types, student and unit queries, direct and indirect tutoring relationships, network statistics, cycle counting and serialized storage. Three entry modes were specified: usage information, an interactive environment and a report loaded from student, unit and network CSV files.

The required handover also included a README, a project report, UML relationships, complexity discussion, a feature/test traceability matrix and test harnesses.

## Design and delivered functions

`DSALinkedList.py`, `DSATree.py` and `DSAGraph.py` provide the linked-list, search-tree and graph structures used by the application. `AcademicTree.py` specializes the data nodes for students and units; `AcademicDatabase.py` builds the tutoring model on these structures. Tutors and tutees have directed relationships associated with a unit.

The interactive menu can load CSV or serialized data, look up students by ID or name, find units, show direct and indirect tutoring connections, list students receiving help in a unit, print network statistics and save the current database.

`FileIO.py` handles CSV and pickle persistence, `menuFileIO.py` supplies the interactive operations, and `StudyHelp.py` selects the entry mode. `trickyEntryFinder.py` supports examination of unusual network cases during development.

A binary search tree indexes student and unit keys, while name lookup traverses records. Pickle serializes the Python object graph for saving and loading the database.

## UML Class Diagram & Architecture

The project's object-oriented class structure, namespaces, and inheritance relationships are modeled in PlantUML and visualized in the comprehensive class diagram below:

![StudyHelp UML Class Diagram](docs/uml/studyhelp_uml.png)

- **PlantUML Source**: [`docs/uml/studyhelp_architecture.puml`](docs/uml/studyhelp_architecture.puml)
- **Inheritance & Hierarchy Design**:
  - `DSALinkedList` $\to$ `UniqueLinkedList`, `SortedLinkedList` ($\to$ `UniqueSortedLinkedList`), `CycleCounter`, `DSAPath`
  - `DSANode` $\to$ `DSAVertexNode` ($\to$ `Student`) and `Unit`
  - `DSATree` $\to$ `UnitTree`, `StudentTree`
  - `DSAGraph` $\to$ `AcademicDatabase` (graph topology and cycle detection)
  - `FileIO` $\to$ `MenuFileIO` $\to$ `StudyHelp` (application orchestration and CLI interface)
- *Readability Note*: Associations pointing to `DSALinkedList` are omitted in the diagram, retaining only inheritance and composition relationships to keep the core architectural hierarchy clear and uncluttered.

## Mock demonstration data

All supplied student and unit records, tutoring relationships and the serialized demonstration database are mock data. They are for development, demonstration and testing and do not represent real student enrollment or tutoring records.

`studentsdemo.csv`, `unitsdemo.csv` and `networkdemo.csv` contain related identifiers. Preserve those relationships when changing an example. The serialized file `studeyHelpData.pickle` is an additional demonstration input; CSV mode provides a straightforward way to construct a database from the supplied records.

## Run

Use Python 3. The main application uses the standard-library `sys` and `pickle` modules and the Python files included here; no third-party runtime package is needed for its basic entry modes.

From this project directory:

```bash
python StudyHelp.py
python StudyHelp.py -i
python StudyHelp.py -r studentsdemo.csv unitsdemo.csv networkdemo.csv
```

The first command displays usage; the second starts the interactive menu; the third loads the three CSV files for the statistics/report path. Some entry paths pause for input, so run them in an interactive terminal.

## Demonstration and testing

```bash
python testHarness.py
```

The harness exercises application operations interactively, with prompts and pauses.
