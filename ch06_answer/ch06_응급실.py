from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))

a = deque([(i, x) for i, x in enumerate(nums)])
cnt = 0

while True:
    cur = a.popleft()

    # ✅ 큐가 비었으면 → 마지막 문서임 → 무조건 처리
    if not a:
        cnt += 1
        print(cnt)
        break

    if cur[1] >= max(a, key=lambda x: x[1])[1]:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
    else:
        a.append(cur)
