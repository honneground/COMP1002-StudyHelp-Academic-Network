import sys
from menuFileIO import MenuFileIO

class StudyHelp(MenuFileIO):
    def __init__(self, studentFile = None, unitFile = None, netFile = None, database = None, advanced = False):
        super().__init__(studentFile, unitFile, netFile, database)
        self.advanced = advanced
        self.usage = """
StudyHelp Usage:
- No command line arguments: Display usage information
- -i: Activate interactive testing environment
- -r <student_file> <unit_file> <network_file>: Activate report mode

Usage Examples:
- To display the usage information:
    StudyHelp.py

- To enter the interactive testing environment:
    StudyHelp.py -i

- To run the report mode with specific file names:
    StudyHelp.py -r students.csv units.csv network.csv
"""

    def printUsage(self):
        self._plash()
        print(self.usage)

    def interactiveMode(self):
        self._plash()
        print("\n# Interactive testing environment activated.")
        input("\nPress \"Enter\" to proceed to the main menu...")
        self.menu()

    def developerMode(self):
        print("\n# Developer testing environment activated.")
        self.readSerialized()
        self.menu()

    def loadMode(self, student, unit, network):
        print("\n# Quick load mode activated.\n")
        print(f"Student file: {student}")
        print(f"Unit file: {unit}")
        print(f"Network file: {network}\n")
        self._loadCsv(student, unit, network)
        input("\nPress \"Enter\" to proceed to the main menu...")
        self.menu()

    def reportMode(self, student, unit, network):
        print("\n# Report mode activated.\n")
        print(f"Student file: {student}")
        print(f"Unit file: {unit}")
        print(f"Network file: {network}\n")
        self._loadCsv(student, unit, network)
        print("\ngenerating report...\n")
        self._statistics()
        print("\nReport generated, please verify.\n")

    def run(self):
        if len(sys.argv) == 1:
            self.printUsage()
        elif sys.argv[1] == "-i":
            self.interactiveMode()

        elif sys.argv[1] == "-r":
            if len(sys.argv) != 5:
                print("Invalid number of arguments. Usage: StudyHelp.py -r <student_file> <unit_file> <network_file>")
            else:
                self.reportMode(sys.argv[2], sys.argv[3], sys.argv[4])

        elif self.advanced:
            if sys.argv[1] == "-d":
                self.developerMode()

            elif sys.argv[1] == "-l":
                if len(sys.argv) != 5:
                    print("Invalid number of arguments. Usage: StudyHelp.py -l <student_file> <unit_file> <network_file>")
                else:
                    self.loadMode(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("Invalid command line argument.")
            print("To obtain hints, run the StudyHelp.py program without any command line arguments.")

if __name__ == "__main__":
    StudyHelp().run()