# 2847 게임을 만드는 동준이 https://www.acmicpc.net/problem/2847

N = int(input())
point = []
for i in range(N):
    point.append(int(input()))
rpoint = list(reversed(point))
result = 0
for i in range(N - 1):
    while True:
        if rpoint[i] <= rpoint[i + 1]:
            rpoint[i + 1] -= 1
            result += 1
        else:
            break

result = 0
