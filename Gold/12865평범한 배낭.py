# 12865 평범한 배낭 https://www.acmicpc.net/problem/12865
# 냅색 알고리즘
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
thing = [[0, 0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    thing.append([w, v])

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)


print(d[n][k])
