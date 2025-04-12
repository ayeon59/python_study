def input_int():
    a=list(map(int,input().split()))
    return a

def reverse(x):
    reverse_num=0
    while x>0:
        if(x%10==0):
            x = x//10
            continue
        reverse_num *= 10
        reverse_num += x%10
        x = x//10
    return (reverse_num)

def count_prime(n):
    for i in range(2,n):
        if(n%i==0):
            break
    else :            
        print(n, end=' ')


n = int(input())
a = input_int()
reverse_arr=[]
for x in a:
    reverse_arr.append(reverse(x))
for x in reverse_arr:
    count_prime(x)