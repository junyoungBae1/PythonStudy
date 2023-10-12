# 1208
from collections import deque

T = 10

for tc in range(1, T + 1):
    answer = -1
    dump = int(input())
    data = list(map(int,input().split()))
    n = len(data)
    data = sorted(data)
    for i in range(dump):
        if data[0] > data[n-1]:
            answer = 1
            break
        elif data[0] == data[n-1]:
            answer = 0
            break
        else:
            data[0] += 1
            data[n-1] -= 1
            data = sorted(data)
            answer = data[n-1] - data[0]
    print("#{} {}".format(tc, answer))
