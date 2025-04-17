n = input()
stack = []
answer = []
top = -1
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

for x in n:
    if x.isdigit():
        answer.append(x)
    elif x == '(':
        stack.append(x)
        top += 1
    elif x == ')':
        while stack[top] != '(':
            answer.append(stack.pop())
            top -= 1
        stack.pop()  # '(' 제거
        top -= 1
    else:  # 연산자 (+, -, *, /)
        while top > -1 and precedence[stack[top]] >= precedence[x]:
            answer.append(stack.pop())
            top -= 1
        stack.append(x)
        top += 1

# 남은 연산자 모두 출력
while top > -1:
    answer.append(stack.pop())
    top -= 1

print("".join(answer))
