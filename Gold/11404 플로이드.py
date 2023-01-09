# 11404 플로이드 https://www.acmicpc.net/problem/11404
# 플로이드–워셜
import sys

input = sys.stdin.readline
INF = int(1e9)
# 도시 개수
n = int(input())
# 버스 개수
m = int(input())

bus = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(c, bus[a][b])
# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                bus[i][j] == 0
            else:
                bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in bus[1:]:
    for j in i[1:]:
        if j == INF:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()
