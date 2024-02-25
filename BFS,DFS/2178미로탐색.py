# 2178미로탐색 https://www.acmicpc.net/problem/2178

# dfs?

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dp = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs():
    q = deque()
    q.append((0, 0))
    cnt = 0
    while q:
        cnt += 1
        x, y = q.popleft()
        for i in dp:
            dx = x + i[0]
            dy = y + i[1]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 1:
                q.append((dx,dy))
                graph[dx][dy] = graph[x][y] + 1

    return graph[n-1][m-1]

print(bfs())
