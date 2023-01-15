# 별 찍기 -11  https://www.acmicpc.net/problem/2448

import sys
input = sys.stdin.readline

N = int(input())

str1 = "  *  "
str2 = " * * "
str3 = "*****"
printStar = [str1,str2,str3]
def recursion(n,before):
    after = [[" "]*(2*2*N-1) for _ in range(2*n)]
    for i in range(n):
        after[i][n:n + 2 * n - 1] = before[i]

    k = 0
    for i in range(n, 2 * n):
        after[i][:2 * n] = before[k]
        after[i][2 * n:2 * n + len(before[k])] = before[k]
        k += 1

    if 2 * n == N:
        return after

    return recursion(2 * n, after)


if N == 3:
    result = printStar
else:
    result = recursion(3, printStar)

for i in result:
    print("".join(i))


# 별 찍기 -11  https://www.acmicpc.net/problem/2448

n = int(input())
graph = [[' '] * 2 * n for _ in range(n)]


def recursive(x, y, N):
    if N == 3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else:
        nextN = N // 2
        recursive(x, y, nextN)
        recursive(x + nextN, y - nextN, nextN)
        recursive(x + nextN, y + nextN, nextN)


recursive(0, n - 1, n)
for i in graph:
    print("".join(i))