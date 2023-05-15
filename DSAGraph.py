from DSALinkedList import DSALinkedList
from DSALinkedList import SortedLinkedList
from DSALinkedList import UniqueLinkedList

class DSAVertex:
    def __init__(self, label):
        self.label = label
        self.outgoingEdges = SortedLinkedList()
        self.incomingEdges = SortedLinkedList()

    def linkTo(self, edge):
        self.outgoingEdges.insertSorted(f"{edge.end.label}{edge.label}", edge)

    def linkFrom(self, edge):
        self.incomingEdges.insertSorted(f"{edge.start.label}{edge.label}", edge)

class DSAEdge:
    def __init__(self, start, end, label):
        self.start = start
        self.end = end
        self.label = label
        start.linkTo(self)
        end.linkFrom(self)

class DSAGraph:
    def __init__(self):
        self.count = 0
        self.cycle = None
        self.vertices = SortedLinkedList()  

    def addVertex(self, vertex):
        self.vertices.insertSorted(str(vertex.label), vertex)
        self.count += 1

    def addEdge(self, inStart, inEnd, label):
        start = self.getVertex(inStart)
        end = self.getVertex(inEnd)
        if start is None:
            start = DSAVertex(inStart)
            self.addVertex(start)
        if end is None:
            end = DSAVertex(inEnd)
            self.addVertex(end)
        DSAEdge(start, end, label)


    def getVertex(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                return vertex
        return None
    
    def _dfsCountCycles(self, current, visited, path, start, cycleCount, visitedEdges):
        visited.add(current)
        path.insertLast(current)
        for edge in current.outgoingEdges:
            next = edge.end 
            if  not visitedEdges.hasKey(edge):
                visitedEdges.add(edge)
                if  path.hasKey(next) and next == start:
                    cycleLength = len(path) - path.index(next)
                    cycleCount += 1 / cycleLength
                if next not in visited:
                    cycleCount += self._dfsCountCycles(next, visited, path, start, 0, visitedEdges)
                visitedEdges.remove(edge)
        path.removeLast()
        visited.remove(current)
        return cycleCount

    def countCycles(self):
        cycleCount = 0
        for vertex in self.vertices:
            visited = UniqueLinkedList()
            path = DSALinkedList()
            visitedEdges = UniqueLinkedList()
            cycleCount += self._dfsCountCycles(vertex, visited, path, vertex, 0, visitedEdges)
        return round(cycleCount)
    
# if __name__ == "__main__":
    # from debug_readcsv import readCSV
    # file_path = 'datademo.csv'
    # file_path = 'networkdemo.csv'
    # graph1 = DSAGraph()
    # extracted_data = readCSV(file_path)
    # for row in extracted_data:
    #     graph1.addEdge(row[0], row[2], row[1])
    # print(graph1.countCycles())