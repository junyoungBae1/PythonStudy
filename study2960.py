# 2960 에라토스테네스의 체 https://www.acmicpc.net/problem/2960

temp = [int(i) for i in input().split()]
N = temp[0]
K = temp[1]
P = list(range(2, N + 1))
count = 0
for i in range(2, N + 1):
    for j, d in enumerate(P):
        if d % i == 0:
            count += 1
            t = P.pop(j)
            if count == K:
                print(t)
                break
