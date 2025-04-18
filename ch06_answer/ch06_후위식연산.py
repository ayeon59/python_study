n = input()
stack = []

lt = 0
rt = 0
for x in n :
    if (x.isdigit()):
        stack.append(x)
    else:
        rt=int(stack.pop())
        lt=int(stack.pop())
        if(x=='*'):
            stack.append(lt*rt)
        elif(x=='/'):
            stack.append(lt//rt)
        elif(x=='+'):
            stack.append(lt+rt)
        else:
            stack.append(lt-rt)

print(stack.pop())