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
    
import random
#创建打印机类
class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() \
                                    * 60/self.pagerate
        


#创建任务类
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
#生成时间戳和随机打印页数

    def getStamp(self):
        return self.timestamp
#返回时间戳    


    def getPages(self):
        return self.pages
#返回打印页数
    
    def waitTime(self,currenttime):
        return currenttime - self.timestamp
#计算等待时间

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
    


def simulation(numSeconds,pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    Waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
#如果有新任务，加入队列

        if (not labprinter.busy()) and \
                    (not printQueue.isEmpty()):
            
            nexttask = printQueue.dequeue()
            Waitingtimes.append(\
                    nexttask.waitingTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
#如果打印机空闲且队列不为空，开始下一个任务

