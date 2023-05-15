class DSAListNode():
    def __init__(self, key=None):
        self.key = key
        self.prev = None
        self.next = None

class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.key
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.key
            current = current.prev

    def __next__(self):
        if self.current is None:
            raise StopIteration
        key = self.current.key
        self.current = self.current.next
        return key
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        keys = DSALinkedList()
        current = self.head
        while current:
            keys.insertLast(str(current.key))
            current = current.next
        return "[" + ", ".join(keys) + "]"

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0:
                if index >= self.size:
                    raise IndexError("Index out of range")
                current = self.head
                for _ in range(index):
                    current = current.next
                value = current.key
            else:
                index = abs(index)
                if index > self.size:
                    raise IndexError("Index out of range")
                current = self.tail
                for _ in range(index - 1):
                    current = current.prev
                value = current.key
                
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            if step is None:
                step = 1
            if step == 0:
                raise ValueError("Step cannot be zero")
            if start is None:
                start = 0
            elif start < 0:
                start += self.size
            if stop is None:
                stop = self.size+1            
            elif stop < 0:
                stop += self.size
            sliced_list = DSALinkedList()
            if step > 0:
                current = self.head
                count = 0
                while current and count < stop:
                    if count >= start and (count - start) % step == 0:
                        sliced_list.insertLast(current.key)
                    current = current.next
                    count += 1
            else:
                if start == 0:
                    start = self.size -1
                current = self.tail
                if stop == self.size+1:
                    stop = -1 
                count = self.size - 1
                while current and count > stop:
                    if count <= start and (start - count) % (-step) == 0:
                        sliced_list.insertLast(current.key)
                    current = current.prev
                    count -= 1
            value = sliced_list
        else:
            raise TypeError("Invalid index type")
        return value
    
    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index >= 0:
                if index >= self.size:
                    raise IndexError("Index out of range")
                current = self.head
                for _ in range(index):
                    current = current.next
                current.key = value
            else:
                index = abs(index)
                if index > self.size:
                    raise IndexError("Index out of range")
                current = self.tail
                for _ in range(index - 1):
                    current = current.prev
                current.key = value
        else:
            raise TypeError("Invalid index type")
        
    def __contains__(self, key):
        return self.hasKey(key)
    
    def getCount(self):
        return self.size

    def hasKey(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def isEmpty(self):
        return self.size == 0
    
    def isNotEmpty(self):
        return self.size > 0
    
    def insertFirst(self, key):
        node = DSAListNode(key)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insertLast(self, key):
        node = DSAListNode(key)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def peekFirst(self):
        if self.isEmpty():
            return None
        else:
            return self.head.key

    def peekLast(self):
        if self.isEmpty():
            return None
        else:
            return self.tail.key

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            key = self.head.key
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return key

    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            key = self.tail.key
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return key

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, key):
        self.insertLast(key)

    def pop(self):
        self.removeLast()
    
    def index(self, key):
        current = self.head
        index = 0

        while current:
            if current.key == key:
                return index
            current = current.next
            index += 1

    def LastIndex(self, key):
        current = self.head
        index = 0
        while current:
            if current.key == key:
                last = index
            current = current.next
            index += 1
        if index == 0:
            raise ValueError("Key not found in the linked list")
        return last

    def remove(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next
        raise ValueError("Key not found in the linked list")
    
class UniqueLinkedList(DSALinkedList):
    def add(self, key):
        if self.hasKey(key):
            return False
        self.insertLast(key)
        return True

    def __str__(self):
        keys = DSALinkedList()
        current = self.head
        while current:
            keys.insertLast(str(current.key))
            current = current.next
        return "{" + ", ".join(keys) + "}"
    
class CycleCounter(DSALinkedList):
    def add(self, key):
        if 1 > key > 0:
            self.insertLast(key)

    def getCount(self):
        current = self.head
        total_sum = 0
        while current:
            total_sum += current.key
            current = current.next
        return round(total_sum)

    def GetDirectCycle(self):
        current = self.head
        total_sum = 0
        while current:
            if current.key == 0.5:
                total_sum += current.key
            current = current.next
        return round(total_sum)

    def GetIndirectCycle(self):
        current = self.head
        total_sum = 0
        while current:
            if current.key != 0.5:
                total_sum += current.key
            current = current.next
        return round(total_sum)
    
class ListObjectNode():
    def __init__(self, val = None, key = None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class SortedLinkedList(DSALinkedList):
    def insertSorted(self, val, key):
        node = ListObjectNode(val, key)
        if self.isEmpty():
            self.head = node
            self.tail = node 
        elif val <= self.head.val:
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif val >= self.tail.val:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            current = self.head.next
            while current:
                if val <= current.val:
                    node.prev = current.prev
                    node.next = current
                    current.prev.next = node
                    current.prev = node
                    break
                current = current.next
        self.size += 1

class UniqueSortedLinkedList(SortedLinkedList):
    def add(self, val, key):
        if self.hasKey(key):
            return False
        self.insertSorted(val, key)
        return True

class DSAPath(DSALinkedList):
    def __str__(self):
        keys = DSALinkedList()
        current = self.head
        while current:
            keys.insertLast(str(current.key))
            current = current.next
        return "\"" + "->".join(keys) + f"-><Start>\""


if __name__ == "__main__":
    def testList(lst, index):
        myList0 = DSALinkedList()
        for i in lst:
            myList0.insertLast(i)

        if isinstance(index, int):
            print("DLL: ",myList0[index])
            print("RFN: ",lst[index])
        elif isinstance(index, slice):
            print("DLL: ",myList0[index])
            print("RFN: ",lst[index])
        else:
            raise TypeError("Invalid index type")
    myList1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 14, 15, 16, 17, 18, 19, 20]
    testList(myList1, slice(10, 0, -2))
    testList(myList1, slice(None, 0, -2))
    testList(myList1, slice(0, None, 2))
    testList(myList1, slice(5, 10))
    testList(myList1, slice(None, 5))
    testList(myList1, slice(10, None))
    testList(myList1, slice(-1, None, -3))
    testList(myList1, slice(None, 0, -4))
    testList(myList1, slice(0, None, 5))
    testList(myList1, slice(10, 15))
    testList(myList1, slice(None, 5))
    testList(myList1, slice(10, None))
    testList(myList1, slice(-1, None, -3))
    testList(myList1, slice(None, 0, -4))
    testList(myList1, slice(0, None, 5))

    myLinkList = UniqueSortedLinkedList()
    for i in myList1:
        myLinkList.add(i, i)
    print(myLinkList)

    myLinkList.add(9,9)
    myLinkList.add(14.6,14.6)
    myLinkList.add(999,999)
    myLinkList.remove(7)

    print(myLinkList)
    print(myLinkList.getCount())
    myLinkList.remove(14)
    myLinkList.remove(15)
    myLinkList.add(2.3,2.3)
    myLinkList.add(13.6,13.6)
    myLinkList.add(7.6,7.6)
    print(myLinkList)