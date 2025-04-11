import sys
#sys.stdin=open("input.txt","rt")

def find_case(N,M):
    a = list()
    num_sum=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            a.append(i+j)
    return a

def count_case(arr):
    count_case=0
    max_count=0
    for x in arr:
        count_case=arr.count(x)
        if(count_case>max_count):
            max_count=count_case
    return max_count

def print_answer(arr,n):
    a=[]
    for x in arr:
        if(arr.count(x)==n):
            a.append(x)
            arr.remove(x)
    for x in a:
        print(x, end=' ')    

#N과 M입력
N,M=map(int,input().split())
#가능한 합 전부 계산
case_num=find_case(N,M)

#오름차순 정리
case_num.sort()
#가장 많은 확률 갖는 횟수 계산
max_count=count_case(case_num)

print_answer(case_num,max_count)



