from FileIO import FileIO
from DSALinkedList import UniqueSortedLinkedList
from DSALinkedList import DSALinkedList
from DSALinkedList import UniqueLinkedList

class MenuFileIO(FileIO):

    def menu(self):
        exitFlag = True
        print()
        while exitFlag:
            self._plash()
            print()
            self._showOptions()
            choice = self._getChoice()
            if choice == 9:
                self._exitting()
                exitFlag = False
            else:
                print()
                self._directing(choice)
                input("\nPress \"Enter\" to proceed to the main menu...")
        
    def _directing(self, choice):
        if choice == 3:
            self._findStudent()
        elif choice == 4:
            self._findUnit()
        elif choice == 5:
            self._findTutoring()
        elif choice == 6:
            self._findEnrolled()
        elif choice == 7:
            self._statistics()
        elif choice == 8:
            self._SaveSer()
        elif choice == 2:
            self._loadSer()
        elif choice == 1:
            self._enterFileName()
        else:
            self.clearData()
            print("Data reinitialized!")
        
    def _exitting(self):
        self._plash()
        print("Thank you! The program exited.")

    def _plash(self):
        print("--------------------------------------------------------")
        print()
        print(" _____  _               _         _   _        _        ")
        print("/  ___|| |             | |       | | | |      | |       ")
        print("\ `--. | |_  _   _   __| | _   _ | |_| |  ___ | | _ __  ")
        print(" `--. \| __|| | | | / _` || | | ||  _  | / _ \| || '_ \ ")
        print("/\__/ /| |_ | |_| || (_| || |_| || | | ||  __/| || |_) |")
        print("\____/  \__| \__,_| \__,_| \__, |\_| |_/ \___||_|| .__/ ")
        print("                            __/ |                | |    ")
        print("                           |___/                 |_|    ")
        print()
        print("--------------------------------------------------------")

    def _enterFileName(self):
        print("Please enter the following choices in order: <student_file>, <unit_file>, <network_file. Suffix is required. You can press enter to select the default preset files.\n")
        self._loadCsv(input("Students Data CSV File:").strip(), input("Units Data CSV File:").strip(), input("Network Data CSV File:").strip())

    def _testMenu(self, A, B, C):
        print("Test Test One Two Three")
        print(A, B, C)

    def _showOptions(self):
        print("#####  MAIN MENU  #####\n")
        if self.database is not None:
            print("1. Load Data from CSV File\n2. Load Serialised Cache\n3. Find Student Detail\n4. Find Unit Detail\n5. Display Student Tutoring Relationships\n6. Retrieve Unit Tutoring Enrollment\n7. Statistics Overview\n8. Save Data\n9. Exit")
        else:
            print("1. Load Data from CSV File\n2. Load Serialised Cache\n#. Find Student Detail\n#. Find Unit Detail\n#. Display Student Tutoring Relationships\n#. Retrieve Unit Tutoring Enrollment\n#. Statistics Overview\n#. Save Data\n9. Exit\n\n*The options that are prefixed with the pound symbol (#) are currently unavailable. Please load the data to unlock all available options.")

    def _getChoice(self):
        print("\nPlease enter the numeric code of your option: ", end = "")
        while True:
            option = input().strip()
            if option.isdigit():
                option = int(option)
                if option in range(1, 10) or option == 42:
                    if self.database is not None or option == 1 or option == 2 or option == 9:
                        return option       
                self.rangeInError()
            else:
                self.typeInError()

    def rangeInError(self):
        print("\nInvalid option. Please enter a valid numeric code: ", end = "")
    
    def typeInError(self):
        print("\nInvalid option. Please enter a numeric code: ", end = "")

    def _loadCsv(self, stu, uni, net):
        file1 = stu if stu != "" else "studentsdemo.csv"
        file2 = uni if uni != "" else "unitsdemo.csv"
        file3 = net if net != "" else "networkdemo.csv"
        self.studentFile = file1
        self.unitFile = file2
        self.netFile = file3
        self.readCSV()
    
    def _loadSer(self):
        print("Please enter the serialised file name. Suffix is required. You can just press \"Enter\" to select the default preset file.\n")
        SerPath = input("Enter serialised file name: ").strip()
        if SerPath == "":
            SerPath = "studeyHelpData.pickle"
        self.readSerialized(SerPath)

    def _SaveSer(self):
        print("Please enter the serialised file name. Suffix is required. You can just press \"Enter\" to select the default file name.\n")
        SerPath = input("Enter serialised file name: ").strip()
        if SerPath == "":
            SerPath = "studeyHelpData.pickle"
        self.writeSerialized(SerPath)

    def _findStudent(self):
        key = input("Please enter student's name or ID: ").strip()
        if key.isdigit():
            studentObj = self.database.getStudent(key)
        else:
            studentObj = self.database.getStudentByName(key)
        if studentObj is None:
            print("\nNo matching student found.\n")
        else:
            print()
            self._studentDetail(studentObj)

    def _findTutoring(self):
        key = input("Please enter student's ID: ").strip()
        if key.isdigit():
            studentObj = self.database.getStudent(key)
        else:
            studentObj = self.database.getStudentByName(key)
        if studentObj is None:
            print("\nNo matching student found.\n")
        else:
            print()
            self._tutorshipDetail(studentObj)

    def _findUnit(self):
        key = input("Please enter the unit code: ").strip()
        unitObj = self.database.getUnit(key)
        if unitObj is None:
            print("\nNo matching unit found.\n")
        else:
            print()
            self._unitDetail(unitObj)
    
    def _findEnrolled(self):
        key = input("Please enter the unit code: ").strip()
        unitObj = self.database.getUnit(key)
        if unitObj is None:
            print("\nNo matching unit found.\n")
        else:
            print()
            self._enrolledDetail(unitObj)

    def _studentDetail(self, studentObj):
        prompt = False
        printedEntries = UniqueLinkedList()
        print("# Student Detail\n")
        print("| Student ID   | Name")
        print("| {:<12} | {}".format(studentObj.ID, studentObj.name))
        if studentObj.enroll.isNotEmpty():
            print("\n# Enrollments\n")
            print("| Code         | Stage                | Title")
            for unit in studentObj.enroll:
                print("| {:<12} | {:<20} | {}".format(unit.code, unit.stage, unit.name))
        if studentObj.tutoring.isNotEmpty():
            print("\n# Providing Tutoring\n")
            print("| ID           | Name                 | Unit")
            for tutorship in studentObj.tutoring:
                if tutorship.tutee in printedEntries:
                    tuteeid, name , prompt= "", "", True
                else:
                    tuteeid, name = tutorship.tutee.ID, tutorship.tutee.name
                    printedEntries.add(tutorship.tutee)
                print("| {:<12} | {:<20} | {}".format(tuteeid, name, tutorship.unit.code))
        printedEntries.clear()
        if studentObj.tutored.isNotEmpty():
            print("\n# Tutored by Peers\n")
            print("| ID           | Name                 | Unit")
            for tutorship in studentObj.tutored:
                if tutorship.tutor in printedEntries:
                    tutorid, name , prompt= "", "", True
                else:
                    tutorid, name = tutorship.tutor.ID, tutorship.tutor.name
                    printedEntries.add(tutorship.tutor)
                print("| {:<12} | {:<20} | {}".format(tutorid, name, tutorship.unit.code))
        if prompt:
            print("\n* The empty space represents the same as above")

    def _enrolledDetail(self, unitObj):
        print(f"# {unitObj.name} {unitObj.stage} ({unitObj.code})")
        print("# Enrolled Tutees Roster \n")
        if unitObj.tutorships.isNotEmpty():
            prompt = False
            printedEntries = UniqueLinkedList()
            print("+                                  +")
            print("| Enrolled Tutee                   | Tutee's Peer Tutor")
            print("+                                  +")
            
            for tutorship in unitObj.tutorships:
                if tutorship.tutee in printedEntries:
                    tuteeid, name , prompt= "", "", True
                else:
                    tuteeid, name = f"({tutorship.tutee.ID})", tutorship.tutee.name

                    printedEntries.add(tutorship.tutee)
                print("| {:<20} {:<12}| {:20} {}".format(name, tuteeid, tutorship.tutor.name, f"({tutorship.tutor.ID})")) 
            if prompt:
                print("\n* The empty space represents the same as above")
        else:
            print("+\n| This unit has not been enabled with the any tutoring relationship.\n+\n")             
            
    def _unitDetail(self, unitObj):
        print("# Unit Detail\n")
        print("| Unit Code    | Stage                | Name")
        print("| {:<12} | {:<20} | {}".format(unitObj.code, unitObj.stage, unitObj.name))
        print("\n# Course Guide\n")
        print(f"| {unitObj.link}")
        if unitObj.tutorships.isNotEmpty():
            enrollees = UniqueSortedLinkedList()
            for tutorship in unitObj.tutorships:
                enrollees.add(tutorship.tutor.ID, tutorship.tutor)
                enrollees.add(tutorship.tutee.ID, tutorship.tutee)
            print("\n# Student Roster \n")
            print("| ID           | Name")
            for person in enrollees:
                print("| {:<12} | {}".format(person.ID, person.name))

    def _tutorshipDetail(self, studentObj):
        if studentObj.tutoring.isNotEmpty():
            entries = DSALinkedList()
            printedEntries = UniqueLinkedList()
            for tutorship in studentObj.tutoring:
                entries.insertLast(tutorship.tutee)
            count = 0
            print(f"# {studentObj.name}'s Tutoring Relationships\n")
            print(f"{studentObj.name} ({studentObj.ID})\n   |",end="")
            index= 1
            for tutorship in studentObj.tutoring:
                if tutorship.tutee in printedEntries:
                    arrow, tuteeid, name, unit= "", "", "", f", {tutorship.unit.code}"
                else:
                    arrow, tuteeid, name, unit = "\n   +--->", f" ({tutorship.tutee.ID})", tutorship.tutee.name, f" in {tutorship.unit.code}"
                    printedEntries.add(tutorship.tutee)
                print(f"{arrow} {name}{tuteeid}{unit}",end="")
                if count == entries.LastIndex(tutorship.tutee) and tutorship.tutee.tutoring.isNotEmpty():
                    if index == entries.getCount():
                        print("\n            |",end="")
                        pre = "\n            +--->"
                    else:
                        print("\n   |        |",end="")
                        pre = "\n   |        +--->"
                    printedParentEntries = UniqueLinkedList()
                    innnerindex = 0
                    for parenttorship in tutorship.tutee.tutoring:
                        if parenttorship.tutee in printedParentEntries:
                            arrow = "" if innnerindex == printedParentEntries.getCount() else ""
                            tuteeid, name, unit = "", "", f", {parenttorship.unit.code}"
                        else:
                            arrow, tuteeid, name, unit = pre, f" ({parenttorship.tutee.ID})", parenttorship.tutee.name, f" in {parenttorship.unit.code}"
                            printedParentEntries.add(parenttorship.tutee)
                        print(f"{arrow} {name}{tuteeid}{unit}",end="")
                    if count+1 != len(entries):
                        print("\n   |",end="")
                    innnerindex += 1
                index +=1
                count += 1
            print("\n\n* Arrows present tutoring and point from the tutor to tutees.")
        else:
            print(f"* {studentObj.name} ({studentObj.ID}) is not a tutor!!!")

    def _statistics(self):
        print("# Statistics\n")
        print("+-------------+-------------+")
        print("| Students    | Units       |")
        print("| {:<11} | {:<11} |".format(self.database.students.getCount(), self.database.units.getCount()))
        print("+-------------+-------------+")
        print("| Tutors      | Tutees      |")
        print("| {:<11} | {:<11} |".format(self.database.tutors.getCount(), self.database.tutees.getCount()))
        print("+-------------+-------------+")
        print("| Tutoring enabled Units    |")
        print("| {:<20}      |".format(self.database.enabledUnit.getCount()))
        print("+---------------------------+")
        print("| Average tutors per unit   |")
        print("| {:<20}      |".format(self.database.getTutor2Unit()))
        print("+---------------------------+")
        print("| Average tutors per        |")
        print("| tutoring enabled unit     |")
        print("| {:<20}      |".format(self.database.getTutor2Eunit()))
        print("+---------------------------+")
        print("| Ratio of tutors to tutees |")
        print("| {:<20}      |".format(self.database.getTutor2Tutee()))
        print("+---------------------------+")
        print("| Total cycle count         |")
        print("| {:<20}      |".format(self.database.getCycle()))
        print("+-------------+-------------+")
        print("| Direct c.c. | Indrt. c.c. |")
        print("| {:<11} | {:<11} |".format(self.database.getDirectCycle(), self.database.getIndirectCycle()))
        print("+-------------+-------------+")

if __name__ == '__main__':
    # test case 0
    IOclass = MenuFileIO("studentsdemo.csv", "unitsdemo.csv", "networkdemo.csv")
    IOclass._loadSer()
    IOclass._plash()
    print(IOclass._getChoice())
    IOclass.readSerialized()
    IOclass.readCSV()
    dataClass = IOclass.accessDatabase()
    stu = dataClass.getStudent(14856654)
    stu = dataClass.getStudent(14530101)
    stu = dataClass.getStudent(14260173)
    stu = dataClass.getStudent(14530101)
    print()
    stu = dataClass.getStudentByName("Bonny Kurkowski")
    stu = dataClass.getStudent(14856654)
    stu = dataClass.getStudentByName("Jamaal Miecznikowski")
    IOclass._studentDetail(stu)
    print(IOclass.database.getCycle())
    print(dataClass.getUnit("COMP3002").name)
    uniObj= dataClass.getUnit("JPNS8001")
    uniObj= dataClass.getUnit("ISYS3012")
    IOclass._unitDetail(uniObj)
    IOclass._tutorshipDetail(stu)
    IOclass._tutorshipDetail(stu)
    IOclass._enrolledDetail(uniObj)
    IOclass._unitDetail(uniObj)
    IOclass._statistics()
    IOclass._showOptions()
    IOclass.database
    # test case2
    IOclass = MenuFileIO("studentsdemo.csv", "unitsdemo.csv", "networkdemo.csv")
    IOclass.readCSV()
    dataClass = IOclass.accessDatabase()
    stu = dataClass.getStudent(14185965)
    print()
    IOclass._tutorshipDetail(stu)
    stu = dataClass.getStudent(14245206)
    IOclass._tutorshipDetail(stu)
    print()
    stu = dataClass.getStudent(14368487)
    IOclass._tutorshipDetail(stu)
    print()
    stu = dataClass.getStudent(14612197)
    IOclass._tutorshipDetail(stu)
    print()
    stu = dataClass.getStudent(14806272)
    IOclass._tutorshipDetail(stu)
    print()
    stu = dataClass.getStudent(14856654)
    IOclass._tutorshipDetail(stu)
    print()
    stu = dataClass.getStudent(14857171)
    IOclass._tutorshipDetail(stu)


    


    




















