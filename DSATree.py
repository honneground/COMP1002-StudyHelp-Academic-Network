from DSALinkedList import SortedLinkedList


class DSANode():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.colour = "Red"
    def __str__(self):
        return str(self.key)

class DSAVertexNode(DSANode):
    def __init__(self, key):
        super().__init__(key)
        self.outgoingEdges = SortedLinkedList()
        self.incomingEdges = SortedLinkedList()
    def linkTo(self, edge):
        self.outgoingEdges.insertSorted(f"{edge.end.key}{edge.label}", edge)
    def linkFrom(self, edge):
        self.incomingEdges.insertSorted(f"{edge.start.key}{edge.label}", edge)

class DSATree():
    def __init__(self):
        self.NIL = DSANode(0)
        self.NIL.left = None
        self.NIL.right = None
        self.NIL.colour = "Black" 
        self.root = self.NIL
        self.count = 0

    def __iter__(self):
        return self._inorderTraversal(self.root)

    def _inorderTraversal(self, current):
        if current is not None and current != self.NIL:
            yield from self._inorderTraversal(current.left)
            yield current
            yield from self._inorderTraversal(current.right)

    def insert(self, key):
        self._insert(DSANode(key))
    
    def _insert(self, new):
        duplicate = self.find(new.key)
        if duplicate is not None:
            new.colour = duplicate.colour
            new.left = duplicate.left
            new.right = duplicate.right
            new.parent = duplicate.parent
            duplicate.left.parent = new
            duplicate.right.parent = new
            if duplicate.parent is not None:
                if duplicate.parent.left == duplicate:
                    duplicate.parent.left = new
                else:
                    duplicate.parent.right = new
            else:
                self.root = new
        else:
            self.count +=1
            new.parent = None
            new.left = self.NIL
            new.right = self.NIL
            new.colour = "Red"
            parentNode = None
            current = self.root
            while current != self.NIL:
                parentNode = current
                if new.key < current.key:
                    current = current.left
                else:
                    current = current.right
            new.parent = parentNode
            if parentNode is None:
                self.root = new
            elif new.key < parentNode.key:
                parentNode.left = new
            else:
                parentNode.right = new
            if new.parent is None:
                new.colour = "Black"
                return
            if new.parent.parent is None:
                return
            self._rebalance(new)

    def _rebalance(self, current):
        while current.parent.colour == "Red":
            if current.parent == current.parent.parent.right:
                uncle = current.parent.parent.left
                if uncle.colour == "Red":
                    uncle.colour = "Black"
                    current.parent.colour = "Black"
                    current.parent.parent.colour = "Red"
                    current = current.parent.parent
                else:
                    if current == current.parent.left:
                        current = current.parent
                        self._rightLeft(current)
                    current.parent.colour = "Black"
                    current.parent.parent.colour = "Red"
                    self._leftRight(current.parent.parent)
            else:
                uncle = current.parent.parent.right
                if uncle.colour == "Red":
                    uncle.colour = "Black"
                    current.parent.colour = "Black"
                    current.parent.parent.colour = "Red"
                    current = current.parent.parent
                else:
                    if current == current.parent.right:
                        current = current.parent
                        self._leftRight(current)
                    current.parent.colour = "Black"
                    current.parent.parent.colour = "Red"
                    self._rightLeft(current.parent.parent)
            if current == self.root:
                break
        self.root.colour = "Black"

    def _leftRight (self ,current):
        rightChild = current.right
        current.right = rightChild.left
        if rightChild.left != self.NIL:
            rightChild.left.parent = current

        rightChild.parent = current.parent
        if current.parent is None:
            self.root = rightChild
        elif current == current.parent.left:
            current.parent.left = rightChild
        else:
            current.parent.right = rightChild
        rightChild.left = current
        current.parent = rightChild 

    def _rightLeft (self , current):
        leftChild = current.left
        current.left = leftChild.right
        if leftChild.right != self.NIL:
            leftChild.right.parent = current

        leftChild.parent = current.parent
        if current.parent is None:
            self.root = leftChild
        elif current == current.parent.right:
            current.parent.right = leftChild
        else:
            current.parent.left = leftChild
        leftChild.right = current
        current.parent = leftChild

    def find(self ,key):
        key = str(key)
        target = self.NIL
        current = self.root
        while current != self.NIL:
            if current.key == key:
                return current
            if current.key <= key:
                current = current.right
            else:
                current = current.left
        if target == self.NIL:
            return None
    
    def getCount(self):
        return self.count

    def getHeight(self):
        count = self.count
        height = -1
        if self.count > 0:
            while count > 0:
                count >>= 1
                height += 1
        return height