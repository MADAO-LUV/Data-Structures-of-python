

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
 
    def insert(self,pos,item):
        temp = Node(item)
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            current = self.head
            count = 0
            while count < pos-1 and current.getNext() != None:
                current = current.getNext()
                count += 1
            temp.setNext(current.getNext())
            current.setNext(temp)    

    def index(self,item):
        current = self.head
        if self.head.getData() == item:
            return 0
        else:
            count = 0
            while current.getNext() != None:
                if current.getData() == item:
                    return count
                else:
                    current = current.getNext()
                    count += 1

    def pop(self):
        current = self.head
        if self.head.getNext() == None:
            self.head.setData(None)
            return current.getData()
        else:
            end = False
            previous = None
            while  not end:
                if current.getNext() == None:
                    previous.setNext(None)
                    end = True 
                    return current.getData()
                else:
                    previous = current
                    current = current.getNext()

    def pop(self,pos):
        current = self.head
        if pos == 0:
            self.head = current.getNext()
            return current.getData()
        else:
            count = 0
            previous = None
            while current.getNext() != None:
                if count == pos:
                    previous.setNext(current.getNext())
                    return current.getData()
                else:
                    previous = current
                    current = current.getNext()
                    count += 1
            

class Stack:
    def __init__(self):
        self.items = Unorderedlist()

    def isEmpty(self):
        return self.items.isEmpty()
    
    def push(self,item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)
    
    def peak(self):
        return self.items.insert(-1)
    
    def size(self):
        return self.items.size()
    
s = Stack()
print(s)


