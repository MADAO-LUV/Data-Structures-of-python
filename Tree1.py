
#嵌套法实现树结构

def BinaryTree(r):
    return [r,[],[]]

def insertleftTree(root,newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])

def insertrightTree(root,newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])

def getRootVal(root):
    return root[0]

def serRootVal(root,newval):
    root[0] = newval

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


a = BinaryTree('A')
print(a)
insertleftTree(a,'B')

print(a)

insertleftTree(a,'C')

print(a)
insertrightTree(a,'D')


print(a)