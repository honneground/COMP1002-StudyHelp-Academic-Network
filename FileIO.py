from AcademicDatabase import AcademicDatabase
import pickle
import sys
# Set the recursion depth limit to the maximum value for 32-bit (2147483647)
sys.setrecursionlimit(2147483647)

class FileIO:
    def __init__(self, studentFile = None, unitFile = None, netFile = None, database = None):
        self.studentFile = studentFile 
        self.unitFile = unitFile
        self.netFile = netFile
        self.database = database
    
    def getData(self):
        return self.database 

    def readCSV(self):
        errorFlag = False
        warningFlag = False
        self.database = AcademicDatabase()
        print(f"Reading the data from the csv file of \"{self.studentFile}\", \"{self.unitFile}\" and \"{self.netFile}\"...\n")
        try:
            with open(self.studentFile, "r") as fileobj:
                try:
                    count = 0
                    for line in fileobj:
                        splitLine = line.strip().split(",")
                        count += 1
                        self.database.students.insert(splitLine[0],splitLine[1])
                    readCount = self.database.students.getCount()
                    print(f"Successfully read and stored {readCount} student data entries with {count-readCount} occurrences of overwrite to duplicate data.")
                except:
                    print("The studentFile file format incorrect!!!")
                    errorFlag = True
        except:
            print("404 studentFile File not found!!!")
            warningFlag = True
        try:
            with open(self.unitFile, "r") as fileobj:
                try:
                    count = 0
                    for line in fileobj:
                        splitLine = line.strip().split(",")
                        count += 1
                        self.database.units.insert(splitLine[0],splitLine[1],splitLine[2],splitLine[3])
                    readCount = self.database.units.getCount()
                    print(f"Successfully read and stored {readCount} unit data entries with {count-readCount} occurrences of overwrite to duplicate data.")
                except:
                    print("The unitFile file format incorrect!!!")
                    errorFlag = True
        except:
            print("404 unitFile File not found!!!")
            warningFlag = True

        try:
            with open(self.netFile, "r") as fileobj:
                try:
                    count = 0
                    for line in fileobj:
                        splitLine = line.strip().split(",")
                        count += 1
                        self.database.addTutorship(splitLine[0],splitLine[2],splitLine[1])
                    readCount = self.database.getCount()
                    print(f"Successfully read and stored {readCount} network data entries with {count-readCount} occurrences of overwrite to duplicate data.")
                except:
                    print("The netFile file format incorrect!!!")
                    errorFlag = True
        except:
            print("404 netFile File not found!!!")
            warningFlag = True
        if errorFlag:
            print("Due to the loading file format error, the data was not loaded.")
        elif warningFlag:
            print("Data was only partly loaded. Strongly suggest loading again.")
        return self.database
    
    def writeSerialized(self, filePath="studeyHelpData.pickle"):
        self.database.clearCycleDate()
        print(f"Serializing data to \"{filePath}\"...")
        try:
            with open(filePath,"wb") as fileobj:
                try:
                    pickle.dump(self.database, fileobj)
                    print(f"Successfully writed study help data to the serialized file \"{filePath}\".")
                except:
                    print("The date size is too large, resulting in a failure to write to the serialized file. To resolve this, adjust the maximum recursion depth in the system to accommodate the serialization process.")
        except:
            print("Permission error, cannot access the object!!!")

    def readSerialized(self, filePath="studeyHelpData.pickle"):
        print(f"Loading data from the Serialized \"{filePath}\"...")
        try:
            with open(filePath,"rb") as fileobj:
                try:
                    self.database = pickle.load(fileobj)
                    print(f"Successfully loaded from serialized file \"{filePath}\".")
                except:
                    print("Error: Incorrect file format!!!")
                    self.database = None
        except:
            print("Error: File does not exist!!!")
        return self.database
    
    def accessDatabase(self):
            return self.database
    
    def clearData(self):
        self.database = None

if __name__ == "__main__":
    a="studentsdemo.csv"
    b="unitsdemo.csv"
    c="networkdemo.csv"
    database0 = FileIO(a,b,c)
    database0.readCSV()
    print(database0.database.getStudent(14472268).name)
    print(database0.database.getStudentByName("Jonathan Reynoso").name)

    print(database0.database.getCycle())
    print(database0.database.getDirectCycle())
    print(database0.database.getIndirectCycle())
    print("t/t")
    print(database0.database.getTutor2Tutee())
    print("t/u")
    print(database0.database.getTutor2Unit())
    print("tutor count")
    print(database0.database.tutors.getCount())
    print("tutee count")
    print(database0.database.tutees.getCount())
    print("unit count")
    print(database0.database.units.getCount())
    print("unit with TR count")
    print(database0.database.enabledUnit.getCount())
    database0.writeSerialized()

    