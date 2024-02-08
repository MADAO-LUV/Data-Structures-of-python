

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Unorderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None :
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        temp = Node(item)
        current = self.head
        found = False
        while not found:
            if current.getNext() == None:
                found = True
            else:
                current = current.getNext()
        current.setNext(temp)
        temp.setNext(None)
        return temp.getData()

list1 = Unorderedlist()
list1.add(1)
list1.add(2)
list1.add(3)
list1.add(4)
list1.add(5)
print(list1.size())
print(list1.append(6))
print(list1.size())
print(list1.search(6))
        
