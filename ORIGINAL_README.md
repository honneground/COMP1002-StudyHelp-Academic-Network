Readme

Project Structure 

This Python program contains a Python-based Academic Database System that allows users to manage student and unit data, track tutoring relationships, and perform various academic-related operations. The system is designed to provide a user-friendly interface for interacting with the database and accessing relevant functionalities.

The project consists of the following Python files.

testHarness.py The testHarness file serves as a demonstration class for the Academic Database System, showcasing its various functionalities. This file includes methods to retrieve student details, unit details, and tutorship relationships, as well as the capability to load and save data, all without requiring manual user input. The Demonstration class encompasses a comprehensive set of test cases that thoroughly assess the functionality of the program. These tests are conducted after major updates during the program's development process, ensuring the robustness and reliability of the system. By utilizing the testHarness.py file, I  can gain confidence in the Study Help Academic Database System's performance and verify that all implemented features work as intended. The provided test cases cover various scenarios, enabling thorough testing of the program's capabilities.

FileIO.py This file handles file input/output operations. It provides methods to read data from CSV files, write serialized data, and access the academic database.

menuFileIO.py The menuFileIO file extends the FileIO module and provides a user-friendly menu interface. It allows users to interact with the Academic Database System by selecting various options such as loading data, finding student and unit details, displaying tutoring relationships, and more.

trickyEntryFinder.py The trickyEntryFinder file contains a class that assists in finding complex cases within the academic database. It provides methods to analyze peer and student counts, helping identify tricky entries in the system and design the test cases.

AcademicDatabase.py The AcademicDatabase file represents the core module of the system. It manages student and unit data, tutoring relationships, and various academic operations. It includes classes such as StudentTree, UnitTree, Tutorship, and CycleCounter.

StudyHelp.py The StudyHelp file provides the main entry point for the Academic Database System. It offers methods to print usage instructions, run the system in interactive mode, and generate reports based on student, unit, and network data.

DSAGraph.py The DSAGraph file contains classes for creating and managing graph structures. It includes classes such as DSAVertex and DSAEdge, representing vertices and edges in the graph, and the DSAGraph class to manage the overall graph. The main database AcademicDatabase is inherited and built on top of this graph implementation.

DSATree.py The DSATree file focuses on tree structures and related operations. It includes the DSANode class representing a node in a tree, and the DSAVertexNode class extending DSANode for managing outgoing and incoming edges. The DSATree class contains a simplified implementation of a binary search tree. This binary search tree focuses on accelerating the search speed for retrieving specific objects while omitting the deletion functionality as it is not required in this particular scenario.

DSALinkedList.py The DSALinkedList file provides an implementation of a linked list data structure. It includes the DSAListNode class representing a node in the linked list, and the DSALinkedList class for managing the list and performing operations such as insertion, removal, and searching.

AcademicTree.py The AcademicTree file extends the DSATree module and focuses on academic-specific functionalities, specifically designed to store and manage student and unit data within the Academic Database System.  It includes the Unit and Student classes, representing units and students in the academic system, and provides methods for managing them.

Dependencies

The Study Help Academic Database System has the following dependencies

Main Program

Python module pickle Used for serialization and deserialization of data, allowing data to be stored and retrieved from files.

Python module sys Provides access to system-specific parameters and functions, used for handling command-line arguments and system interactions.

DSA Practical04 Refers to the work done in the fourth practical session of the Data Structures and Algorithms course. The DSALinkedList model in this assignment is built on top of the practical work including the concepts and pseudo-code covered in that session.

UML Diagram 

www.umletino.com An online tool for creating UML diagrams. It is used to generate the UML diagram visualizing the structure of the Academic Database System.

PlantUML A text-based tool for creating UML diagrams. It is used along with the UMLetino website to generate the UML diagram based on the provided code.

Python module pylint A Python code analysis tool used for checking code quality and identifying potential errors or issues. It is likely used to analyze and ensure the code adheres to best practices and coding standards.

The mentioned Python modules (pickle, sys, pylint) are standard modules available in the Python Standard Library and should be included by default with any Python installation.
