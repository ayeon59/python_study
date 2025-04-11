import sys
#sys.stdin=open("input.txt","rt")

def in_number():
    a=list(map(int,input().split()))
    return a

def avg(arr):
    num = 0
    for x in arr:
        num += x
    num/=len(arr)
    num = round(num)
    return num

def who_is_closer(arr,score):
    gap=100
    who = 0
    for i in range(len(arr)):
        if(abs(score-arr[i])<gap):
            gap=abs(arr[i]-score)
            who = i 
            print("*%d \n"%gap)
        elif(abs(score-arr[i])==gap):
            if(score-arr[i]<score-arr[who]):
                who = i
    return who
#학생수 입력
he = 0
student = int(input())
#학생별 점수 입력
#배열 인덱스+1 = 학생 번호
math=in_number()
#평균점수 저장
avg_score = avg(math)
he = who_is_closer(math,avg_score)
print("%d %d" %(avg_score,he+1))



