
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    

def divideby2(decnumber):
    remstack = Stack()
     
    while decnumber>0:
        rem = decnumber % 2
        remstack.push(rem)
        decnumber = decnumber // 2
    
    binstring = ""
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())

    return binstring

s = divideby2(233)
print(s)
    


