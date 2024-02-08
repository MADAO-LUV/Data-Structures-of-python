"""
1.stack(栈)----属于我自定义的类,不过符合数据结构中的栈结构
2.这里涉及到后缀表达式的计算,后缀表达式的计算是利用栈的特性来实现的

对于--return operandStack.pop()--这句话的理解:
就是遍历完所有的操作符后,栈中只会剩下一个操作数---计算结果
所以此处,直接返回栈中的最后一个元素
"""


class StacK:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    

def postfixEval(postfixExpr):
    operandSatck = StacK()

    tokenlist = postfixExpr.split()

    for token in tokenlist:
        if token in "for j in range(10)":
            operandSatck.push(int(token))
        else:
            operand2 = operandSatck.pop()
            operand1 = operandSatck.pop()
            reuslt = domath(token,operand1,operand2)
            operandSatck.push(reuslt)

    return operandSatck.pop()

def domath(op,op1,op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    elif op == "-":
        return op1-op2
    