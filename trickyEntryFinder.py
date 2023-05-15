from FileIO import FileIO
from DSALinkedList import SortedLinkedList
from DSALinkedList import UniqueLinkedList

FileSystem = FileIO("studentsdemo.csv", "unitsdemo.csv", "networkdemo.csv")

FileSystem.readCSV()
Database = FileSystem.accessDatabase()

students = Database.students
complexCases = SortedLinkedList()

def getPeerCount(student):
    peerCount = UniqueLinkedList()
    for ship in student.tutoring:
        peerCount.add(ship)
    # for ship in student.tutored:
    #     peerCount.add(ship)
    return peerCount.getCount()

def getStuCount(student):
    peerCount = UniqueLinkedList()
    for ship in student.tutorships:
        peerCount.add(ship.tutor)
        peerCount.add(ship.tutee)
    return peerCount.getCount()

for student in students:
    peer = getPeerCount(student)
    if peer > 3: 
        complexCases.append(student)

index = 1
for student in complexCases:
    print(f"Student {index}: {getPeerCount(student)}")
    index += 1
    print(student.ID)

complexCases = SortedLinkedList()
for unit in Database.units:
    peerCount = UniqueLinkedList()
    for ship in unit.tutorships:
        peerCount.add(ship.tutor)
        peerCount.add(ship.tutee)
    if  peerCount.getCount() > 10:
        complexCases.append(unit)

index = 1
for unit in complexCases:
    print(f"Unit {index}: {getStuCount(unit)}")
    index += 1
    print(unit.code)







