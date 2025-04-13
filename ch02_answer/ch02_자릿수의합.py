def input_int():
    a=list(map(int,input().split()))
    return a

def digit_sum(x,arr):
    sum = 0
    count = len(str(x))
    for i in range(count):
        sum += x%10
        x = x//10
    arr.append(sum)

def max_digit(arr):
    max_num=0
    max_index=0
    for i in range(len(arr)):
        if(arr[i]>max_num):
            max_num = arr[i]
            max_index=i
    return max_index

n = int(input())
#자연수 입력받기
a=input_int()
#자릿수 별 합 계산 및 리스트 작성
sum_list=[]
for i in range(n):
    digit_sum(a[i],sum_list)
#가장 큰 자릿수의 합을 가진 인덱스 추출
what_is_biggest=max_digit(sum_list)
print(a[what_is_biggest])
