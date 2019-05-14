from pythonds.basic.stack import Stack
def checkBalance(symbolstring):
    a = Stack()
    balance = True   
    index = 0
    while index < len(symbolstring) and balance:
        if symbolstring[index] == '(':
            a.push(symbolstring[index])
        elif symbolstring[index] == ')':
            if a.isEmpty():
                balance = False
            else:
                a.pop()
        else:
            balance = False
        index = index + 1 
        
    if balance and a.isEmpty():
        return True
    else :
        return False 

print(checkBalance('((()))'))
print(checkBalance('(()'))
        




