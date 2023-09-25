# 11657 타임머신 https://www.acmicpc.net/problem/11657
# 벨만포든 bellman-ford

import sys

max_int = float("INF")

input = sys.stdin.readline
n, m = map(int, input().split())
edges = []  # 도시간 거리 정보 저장할 리스트
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((x, y, z))

dist = [max_int] * (n + 1)
dist[1] = 0

for i in range(n):
    for x, y, cost in edges:
        if dist[x] != max_int and dist[y] > dist[x] + cost:
            if i == n - 1:  # n번째 순회에서도 값이 바뀐다면 음수 사이클 존재
                print(-1)
                exit(0)
            dist[y] = dist[x] + cost

for i in range(2, n + 1):
    if dist[i] == max_int:
        print(-1)
    else:
        print(dist[i])
