from StudyHelp import StudyHelp

index = 0
welcome = """

This test harness file serves as a demonstration to stimulate user operations within the StudyHelp database manually. It simulates a user going through all the functionalities of the database. The test harness showcases all the required functions by incorporating typically challenging entries found in the database. These entries were discovered during the project's development. (See more at trickyEntryFinder.py)
The test harness effectively calls all the inner private functions that the menu would normally invoke for the user in both the Database and FileIO sections. Essentially, this test harness provides comprehensive coverage of the database's robustness. It offers a testing approach that is comparable to navigating through the menu.
Such is the purpose and design of this test harness file.

@ Dependency @

Python module sys
Python module pickle

* * Please make sure these two modules are available to serialize data
* * Please make sure "studentsdemo.csv" "unitsdemo.csv" "networkdemo.csv" is in this folder to load data.
"""
notice = """

@ Formatting Instructions @

Scenarios corresponding to user actions will be indicated by the doouble (#) symbol.
User operations will be printed at the bottom of the terminal after program execution.
Important additional notes will be marked with the double (*) symbol.
Each major section will be separated by (-) symbols.
You will be prompted to press (Enter) during the demonstration to proceed to the next scenario.
Single (#) and symbol sing (*) are prompt from the database, not test harness!

##################################################################
#                                                                #
#   All options and inputs are just UI display presenting,       #  
#   and the input results will not affect the program testing.   #
#   Tests will be performed based on pre-specified parameters.   #
#                                                                #
##################################################################
"""

class Demonstration(StudyHelp):

    def _loadCsv(self, stu, uni, net):
        self.studentFile = "studentsdemo.csv"
        self.unitFile = "unitsdemo.csv"
        self.netFile = "networkdemo.csv"
        self.readCSV()
        
    def findStudent(self, name):
        input("Please enter student's name or ID: ").strip()
        if name.isdigit():
            studentObj = self.database.getStudent(name)
        else:
            studentObj = self.database.getStudentByName(name)
        if studentObj is None:
            print("\nNo matching student found.\n")
        else:
            print()
            self._studentDetail(studentObj)

    def findTutoring(self, name):
        input("Please enter student's ID: ").strip()
        if name.isdigit():
            studentObj = self.database.getStudent(name)
        else:
            studentObj = self.database.getStudentByName(name)
        if studentObj is None:
            print("\nNo matching student found.\n")
        else:
            print()
            self._tutorshipDetail(studentObj)

    def findUnit(self, name):
        input("Please enter the unit code: ").strip()
        unitObj = self.database.getUnit(name)
        if unitObj is None:
            print("\nNo matching unit found.\n")
        else:
            print()
            self._unitDetail(unitObj)
    
    def findEnrolled(self, name):
        input("Please enter the unit code: ").strip()
        unitObj = self.database.getUnit(name)
        if unitObj is None:
            print("\nNo matching unit found.\n")
        else:
            print()
            self._enrolledDetail(unitObj)
    
    def getChoice(self):
        print("\nPlease enter the numeric code of your option: ", end = "")
        option = input().strip()
        if option.isdigit():
            option = int(option)
            if option in range(1, 10) or option == 42:
                if self.database is not None or option == 1 or option == 2 or option == 9:
                    return option       
                self.rangeInError()
        print("Illegal input!")
        return None

    def loadSer(self):
        print("Please enter the serialised file name. Suffix is required. You can just press \"Enter\" to select the default preset file.\n")
        input("Enter serialised file name: ").strip()
        self.readSerialized("studeyHelpData.pickle")

    def SaveSer(self):
        print("Please enter the serialised file name. Suffix is required. You can just press \"Enter\" to select the default file name.\n")
        input("Enter serialised file name: ").strip()
        self.writeSerialized("studeyHelpData.pickle")

def pause():
    input("\nPress \"Enter\" to continue...")
    # print("TEMP PAUSE")

def section(text):
    global index
    print()
    text = f" {index}. {text} "
    textWidth = len(text)
    padding = (56 - textWidth) // 2
    print('-' * padding + text + '-' * padding,end="")
    if len(text) %2 != 0:
        print("-",end="")
    print("\n")
    index += 1

def scenario(text):
    print(f"\n# # {text}\n")

def hint(text):
    print(f"* * {text}")


Demo = Demonstration()
Data = Demo.accessDatabase()

Demo._plash()
print(welcome)
pause()
print(notice)
pause()

section("Command Line Arguments")
hint("This part cannot be fully simulated. It only demonstrates the functionality of the corresponding calls in the given scenario.")
Demo.printUsage()
scenario("No command line argument given")
pause()

print("Invalid number of arguments. Usage: StudyHelp.py -r <student_file> <unit_file> <network_file>")
scenario("Wrong numbers of command line argument given")

print("Invalid command line argument.")
print("To obtain hints, run the StudyHelp.py program without any command line arguments.")
scenario("Invalid command line argument given")
pause()

scenario("Correct usage of command-line, possessed to iterative testing environment.")
section("Main Menu")

scenario("Iterative testing environment.")

Demo._plash()
Demo._showOptions()
scenario("Please enter 1 or 2.")
option = Demo.getChoice() 
if option == 1:
    print("\nProcessing to read the file...")
if option == 2 or option == 9:
    print("\nThis is just a testing. Let's read the file first...")
else:
    print("\nBut for this demo, we would just go on.")

pause()

section("Loading Data (Menu Option 1)")

scenario("User would enter the files' names but as for the test\n# # Just Press \"Enter\" three times then.")

Demo._enterFileName()

print("Preset File loaded.")

scenario("Back to main menu aftet loading to see all option are now unlocked.")
pause()
Demo._plash()
Demo._showOptions()
scenario("Now you can enter number from range of 1 to 9.")
option = Demo.getChoice() 
if option == 3:
    print("\nProcessing to find the student info...")
if str(option).isdigit() and option !=3:
    print("\nThis is just a testing. Let's find the student info first...")
else:
    print("\nBut for this demo, we would just go on.")


section("Iterative Mode")

scenario("Find Student Detail")

print("We would look at some relatively complex cases to see the functionality of this section. Just use pressing enter to press to the next case.\n")

hint("Suggest scenario parameters will be printed first and executed, regardless of user inputs.")
pause()

section("Student Info (Menu Option 3)")

scenario("Using ID 14806272 to find student info.")
Demo.findStudent("14530101")
scenario("Using ID 14806272 to find student info.")
Demo.findStudent("14570514")
scenario("Using the name 'Ernest Doherty' to find student info.")
Demo.findStudent("Ernest Doherty")
scenario("Using the name 'Lenore Raye' to find student info.")
Demo.findStudent("Lenore Raye")
scenario("Illegal input of 99999999 demo.")
Demo.findStudent("99999999")

section("Unit Info (Menu Option 4)")

scenario("Using unit code ISYS6004 to find unit info.")  
Demo.findUnit("ISYS6004")


scenario("Using unit code CNCO5000 to find unit info.")                                   
Demo.findUnit("CNCO5000")


section("Tutoring Relationships (Menu Option 5)")


scenario("Student 14185965 Relationships")
Demo.findTutoring("14185965")

scenario("Student 14245206 Relationships")
Demo.findTutoring("14245206")


scenario("Student 14368487 Relationships")
Demo.findTutoring("14368487")


scenario("Student 14612197 Relationships")
Demo.findTutoring("14612197")


scenario("Student 14806272 Relationships")
Demo.findTutoring("14806272")


scenario("Student 14856654 Relationships")
Demo.findTutoring("14856654")


scenario("Student 14857171 Relationships")
Demo.findTutoring("14857171")

scenario("Illegal input of non-tutor student id 14359796 demo.")
Demo.findTutoring("14359796")

scenario("Let's also confirm ID 14359796 presence by finding student info.")
Demo.findStudent("14359796")

section("Unit Entrollment (Menu Option 6)")

scenario("Using unit code CNCO5000 to find entrolled tutees.")     
Demo.findEnrolled("CNCO5000")
print()
hint("Yes. Wendy Seda got two tutors in the unit.")

scenario("Illegal input of non-tutoring enabled unit code ISYS6004 demo.")     
Demo.findEnrolled("ISYS6004")
pause()

section("Save and Read Serialised File (Menu Option 7 and 2))")

hint("Since linked lists, graphs, and trees are used as the basis for supporting object-orientated programming projects, the default recursion depth is far from enough to complete the serialization process. It used the sys module to modify the maximum recursion depth.")
hint("If serialization fails, please try switching your os to Linux.")
scenario("Save the database to the serialised file named \"studeyHelpData.pickle\".")

Demo.SaveSer()

scenario("Read the database from the serialised file named \"studeyHelpData.pickle\", which we just saved.")

Demo.loadSer()
# Update the pointer to the newly loaded data.
Data = Demo.accessDatabase()
# print("Demo: the pointer to the new database updated.")

pause()
section("Report Mode (-r) A.K.A Statistics (Menu Option 7)")

hint("Before showing all the statistics, I would like to demo how cycles were count in before process to report.")
hint("To do this, I would turn on the debug mode and call the count cycle function to show the principle. Then I would turn off debug mode and show the rest of the statistical analysis.")

print()

Data.debugMode()
print()

Data._countCycle()
print()
print(f"By summing up all the weights above. We found that the cycle count in the network graph is {Data.getCycle()},")
print(f"with Direct cycle of {Data.getDirectCycle()} (sum of 0.5 weights), and indirect cycle of {Data.getIndirectCycle()} (sum of all other weights).")
print()
Data.debugMode()
print()
hint("The reason the path can be displayed in this way is that I write the string function for both the Linked List and Student object, which enabled objects to be present using the print function.")

pause()


scenario("Correct usage of command-line, possessed to report mode.\n Or user choose the \"7\" from the main menu.")

Demo.reportMode("studentsdemo.csv", "unitsdemo.csv", "networkdemo.csv")
print()
hint("Executing the report mode would load the CSV file name from the argument parameters. This would not be performed when entering the statistics option from the main menu.")
pause()
section("Exit Option (Menu Option 8)")

scenario("The user finish all the operation and choose to exit.")
Demo._exitting()

section("THE END OF DEMO (testHarness)")