def is_it_num (x,arr):
    if x.isdigit():
        arr.append(x)

def count_divisor(x):
    count = 0
    for i in range(1,x+1):
        if(x%i==0):
            count += 1

    return count

n = input()
num_n = list()
len_n = len(n)

for i in range(len_n):
    is_it_num(n[i],num_n)

answer_num=int(''.join(num_n))

print(answer_num)
print(count_divisor(answer_num))
