# 1225

from collections import deque

T = 10
for tc in range(1, T + 1):
    q = deque()
    n = str(input())
    answer = "#" + n + " "
    arr = list(map(int, input().split()))
    cycle = 5
    for i in arr:
        q.append(i)
    flag = 1
    while flag:
        for i in range(1, cycle + 1):
            x = q.popleft()
            if x - i <= 0:
                x = 0
                q.append(x)
                flag = 0
                break
            else:
                x = x - i
                q.append(x)
    for i in q:
        answer += str(i) + " "

    print(answer)
