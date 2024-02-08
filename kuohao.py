
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
    operandStack = StacK()
    tokenlist = postfixExpr.split()
    #此处是将接受到的字符串以空格为分隔符分割成列表

    for token in tokenlist:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = domath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def domath(op,op1,op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else:
        return op1-op2
    
s = postfixEval(("7 8 + 3 2 + /"))
print(s)

