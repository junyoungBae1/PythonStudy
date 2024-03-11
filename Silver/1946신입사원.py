# 1946 신입사원


import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    result = 0
    test = [list(map(int, input().split())) for j in range(n)]
    test.sort()
    result += 1
    man = test[0][1]
    for j in range(1, n):
        if man > test[j][1]:
            result += 1
            man = test[j][1]

    print(result)
