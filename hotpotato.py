class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def queuesize(self):
        return len(self.items)
    

def hotPtato(namelist,num):
    sumqueue = Queue()
    for name in  namelist:
        sumqueue.enqueue(name)

    while sumqueue.queuesize() > 1:
        for i in range(num):
            sumqueue.enqueue(sumqueue.dequeue())
        sumqueue.dequeue()

    return sumqueue.dequeue()

namelist = ["Bill","David","Susan","Jane","Kent","Brad"]
num = 3
print(hotPtato(namelist,num))


