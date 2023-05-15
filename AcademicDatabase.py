from DSAGraph import DSAGraph
from DSAGraph import DSAEdge
from AcademicTree import StudentTree
from AcademicTree import UnitTree
from DSALinkedList import UniqueLinkedList
from DSALinkedList import CycleCounter
from DSALinkedList import DSAPath
from DSALinkedList import UniqueSortedLinkedList


class Tutorship(DSAEdge):
    def __init__(self, tutor, tutee, unit):
        super().__init__(tutor, tutee, unit)
        unit.tutorships.insertSorted(f"{self.end.ID}{self.start.ID}", self)
        self.tutor = self.start
        self.tutee = self.end
        self.unit = self.label
        
class AcademicDatabase(DSAGraph):
    def __init__(self):
        super().__init__()
        self.students = StudentTree()
        self.units = UnitTree()
        self.tutors = UniqueSortedLinkedList()
        self.tutees = UniqueSortedLinkedList()
        self.enabledUnit = UniqueSortedLinkedList()
        self.advanced = False

    def debugMode(self):
        self.advanced = not self.advanced
        prompt = "ON" if self.advanced is True else "OFF"
        print(f"Debug mode is now {prompt}")

    def addTutorship(self, tutorID, tuteeID, unitCode):
        self.count += 1
        tutor = self.getStudent(tutorID)
        tutee = self.getStudent(tuteeID)
        unit = self.getUnit(unitCode)
        if tutor is None:
            self.students.insert(tutorID)
            tutor = self.getStudent(tutorID)
        if tutee is None:
            self.students.insert(tuteeID)
            tutee = self.getStudent(tuteeID)
        if unit is None:
            self.units.insert(unitCode)
            unit = self.getUnit(unitCode)
        Tutorship(tutor, tutee, unit)
        tutor.enrolling(unit)
        tutee.enrolling(unit)
        self.tutors.add(tutorID, tutor)
        self.tutees.add(tuteeID, tutee)
        self.enabledUnit.add(unitCode, unit)

    def _divisionHandler(self, number1, number2):
        try:
            result = number1 / number2
        except:
            result = 0
        return result

    def getTutor2Unit(self):
        return self._divisionHandler(self.tutors.getCount(), self.units.getCount())
    
    def getTutor2Tutee(self):
        return self._divisionHandler(self.tutors.getCount(), self.tutees.getCount())
    
    def getTutor2Eunit(self):
        return self._divisionHandler(self.tutors.getCount(), self.enabledUnit.getCount())
        
    def getCount(self):
        return self.count

    def getUnit(self, code):
        return self.units.find(code)

    def getStudent(self, ID):
        return self.students.find(ID)

    def getStudentByName(self, name):
        for std in self.students:
            if std.name == name:
                return std
        return None

    def _dfsCountCycle(self, currentVertex, visited, path, startVertex, visitedEdges):
        visited.add(currentVertex)
        path.insertLast(currentVertex)
        for edge in currentVertex.outgoingEdges:
            nextVertex = edge.end
            if not visitedEdges.hasKey(edge):
                visitedEdges.add(edge)
                if  path.hasKey(nextVertex) and nextVertex == startVertex:
                    cycleLength = len(path) - path.index(nextVertex)
                    self.cycle.add(1 / cycleLength)
                    if self.advanced == True:
                        print(f"Cycle path {path} found, which weights {1 / cycleLength} (inverse of the cycle length) to the total count.")
                if nextVertex not in visited:
                    self._dfsCountCycle(nextVertex, visited, path, startVertex, visitedEdges)
                visitedEdges.remove(edge)
        path.removeLast()
        visited.remove(currentVertex)

    def _countCycle(self):
        self.cycle = CycleCounter()
        for vertex in self.students:
            # print(f"This is :{vertex.ID}")
            visited = UniqueLinkedList()
            path = DSAPath()
            visitedEdges = UniqueLinkedList()
            self._dfsCountCycle(vertex, visited, path, vertex, visitedEdges)
        return self.cycle.getCount()
    
    def getDirectCycle(self):
        if self.cycle is None:
            self._countCycle()
        return self.cycle.GetDirectCycle()
    
    def getIndirectCycle(self):
        if self.cycle is None:
            self._countCycle()
        return self.cycle.GetIndirectCycle()

    def getCycle(self):
        if self.cycle is None:
            self._countCycle()
        return self.cycle.getCount()
    
    def clearCycleDate(self):
        self.cycle = None
    
if __name__ == "__main__":

    database = AcademicDatabase()

    with open("studentsdemo.csv", "r") as file:
        count = 0
        for line in file:
            splitLine = line.strip().split(",")
            count += 1
            database.students.insert(splitLine[0],splitLine[1])
        readCount = database.students.getCount()
        print(f"Successfully read and stored {readCount} student data entries with {count-readCount} occurrences of overwrite to duplicate data.")

    with open("unitsdemo.csv", "r") as file:
        count = 0
        for line in file:
            splitLine = line.strip().split(",")
            count += 1
            database.units.insert(splitLine[0],splitLine[1],splitLine[2],splitLine[3])
        readCount = database.units.getCount()
        print(f"Successfully read and stored {readCount} unit data entries with {count-readCount} occurrences of overwrite to duplicate data.")

    with open('networkdemo.csv', "r") as file:
        count = 0
        for line in file:
            splitLine = line.strip().split(",")
            count += 1
            database.addTutorship(splitLine[0],splitLine[2],splitLine[1])
        readCount = database.getCount()
        print(f"Successfully read and stored {readCount} unit data entries with {count-readCount} occurrences of overwrite to duplicate data.")


    # print(database.getDirectCycle())
    # print(database.getIndirectCycle())
    # print(database.cycle)
    # print(database.count)
    # stu0 = database.getStudent(14857171)
    # for ship in stu0.tutoring:
    #     print(ship.start.ID,ship.start.name,end=",")
    # print()
    # stu0 = database.getStudent(14857171)
    # for ship in stu0.tutored:
    #     print(ship.end.ID,ship.end.name,end=",")
    # print()
    # print("t/t")
    # print(database.getTutor2Unit())
    # print("t/u")
    # print(database.getTutor2Tutee())
    # print("OR count")
    # print(database.tutors.getCount())
    # print("EE count")
    # print(database.tutees.getCount())
    # print("UN count")
    # print(database.units.getCount())
    # print("STU count")
    # print(database.students.getCount())
    # print("NTW count")
    database.debugMode()
    print(database.getCycle())
    print(database.getCount())
    
    print(database.getStudent(14590536).name)

    