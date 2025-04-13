def re_order(arr,first,last):
    num = (last - first + 1)//2
    for i in range(num):
        swap = arr[first+i] 
        arr[first+i] = arr[last-i]
        arr[last-i] = swap



a=list()
for i in range(1,21):
    a.append(i)

for i in range(10):
    start,last = map(int,input().split())
    re_order(a,start-1,last-1)

print(' '.join(map(str, a)))