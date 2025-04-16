n = int(input())
numbers=list(map(int,input().split()))
lt = 0
rt = n-1
last = 0
str=''
tmp = []
while lt<=rt:
    if(numbers[lt]>last):
        tmp.append((numbers[lt],'L'))
    if(numbers[rt]>last):
        tmp.append((numbers[rt],'R'))
    tmp.sort()
    if(len(tmp)==0):
        break
    else:
        last = tmp[0][0]
        str = str+tmp[0][1]
        if(tmp[0][1]=='L'):
            lt += 1
        else :
            rt -= 1
    tmp.clear()

print(len(str))
print(str)