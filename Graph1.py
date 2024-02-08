#实现邻接表
"""
1.为图对象的所有顶点保存一个主列表,同时为每一个顶点对象都维护一个列表,其中记录了与它相连的顶点
2.在Vertex类的实现中,我们使用字典（而不是列表）,字典的键是顶点(Node),而值是权重(Weight)

"""
#创建一个顶点类
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
#初始化id, 字典connectedTo

    def addNeighbor(self,nbr,Weight=0):
        self.connectedTo[nbr] = Weight
#加入顶点对象的key

    def __str__(self):
        return str(self.id) + 'connectedTo:' \
            + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
#返回所有与顶点相连的顶点

    def getId(self):
        return self.id
#返回该顶点的键值
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
#返回权重    

#创建一个图的类
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
#初始化一个节点列表

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key) # 创建一个节点实例
        self.vertList[key] = newVertex
        return newVertex
#加入一个新顶点

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
#通过key来查找顶点

    def __contains__(self,n):
        return n in self.vertList
#key in Graph操作

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)
#添加边（edge）操作，记住先是添加节点

    def getVertices(self):
        return self.vertList.keys()
 #获取主列表中所有键值

    def __iter__(self):
        return iter(self.vertList.values())
#迭代函数