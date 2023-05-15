from DSALinkedList import SortedLinkedList
from DSALinkedList import UniqueSortedLinkedList
from DSATree import DSANode
from DSATree import DSATree
from DSATree import DSAVertexNode


class Unit(DSANode):
    def __init__(self, code, name, stage, link):
        super().__init__(code)
        self.code = code
        self.name = name
        self.stage = stage
        self.link = link
        self.tutorships = SortedLinkedList()

class Student(DSAVertexNode):
    def __init__(self, ID, name):
        super().__init__(ID)
        self.ID = ID
        self.name = name
        self.enroll = UniqueSortedLinkedList()
        self.tutoring = self.outgoingEdges
        self.tutored = self.incomingEdges
    def enrolling(self, unit):
        self.enroll.add(str(unit.name), unit)
    def linkTo(self, edge):
        self.outgoingEdges.insertSorted(f"{edge.end.key}{edge.label.code}", edge)
    def linkFrom(self, edge):
        self.incomingEdges.insertSorted(f"{edge.start.key}{edge.label.code}", edge)
        
class UnitTree(DSATree):
    def insert(self, code = 0, name = "Undefined", stage = "Undefined", link = "Undefined"):
        self._insert(Unit(code, name, stage, link))

class StudentTree(DSATree):
    def insert(self, ID, name = "Undefined"):
        self._insert(Student(ID, name))


if __name__ == "__main__":

    ####Test Case 0
    # bst1 = DSATree()
    # import random
    # data = list(range(1, 99))
    # random.shuffle(data)
    # for key in data:
    #     bst1.insert(key)
    # print(bst1.find(50).key)

    ####Test Case 1
    # import random
    # dsatree0 = StudentTree()
    # data = list(range(1, 13))
    # random.seed(42)
    # random.shuffle(data)
    # for key in data:
    #     dsatree0.insert(key, key)
    # print(dsatree0.count)
    # print(dsatree0.find(8).name)
    # dsatree0.insert(1, "A")
    # dsatree0.insert(2, "B")
    # dsatree0.insert(3, "C")
    # dsatree0.insert(4, "D")
    # dsatree0.insert(5, "E")
    # dsatree0.insert(6, "F")
    # print(dsatree0.find(1).name)
    # dsatree0.insert(1, "X")
    # dsatree0.insert(2, "V")
    # dsatree0.insert(3, "K")
    # print(data)
    # print(len(data))
    # print(dsatree0.count)
    # print(dsatree0.find(1).name)
    # print(dsatree0.find(2).name)
    # print(dsatree0.find(3).name)

    ### test case 4
    filename = "units.csv"
    units = UnitTree()
    count = 0
    with open(filename, "r") as file:
        for line in file:
            splitLine = line.strip().split(",")
            count += 1
            units.insert(splitLine[0],splitLine[1],splitLine[2],splitLine[3])
    print(units.getCount())
    print(count)
    print(units.getHeight())
    print()

    ### test case 3
    Students = StudentTree()
    filename = "students.csv"
    # filename = "data2.csv"
    count = 0
    with open(filename, "r") as file:
        for line in file:
            splitLine = line.strip().split(",")
            count += 1
            Students.insert(splitLine[0],splitLine[1])
    print(Students.getCount())
    print(count)
    print(Students.getHeight())
    for stu in Students:
        print(stu.key, stu.name)
   
    print(Students.find(14472268).name)
    print(Students.getCount())