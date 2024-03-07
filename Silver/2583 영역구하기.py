# 2583 영역 구하기

import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for l in range(y1, y2):
            if graph[l][j] == 0:
                graph[l][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, area):
    q = deque()
    q.append([y, x])
    graph[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if 0 <= cx < n and 0 <= cy < m:
                if graph[cy][cx] == 0:
                    q.append([cy, cx])
                    graph[cy][cx] = 1
                    area += 1
    return area


cnt = 0
result = list()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt += 1
            area = 1
            area = bfs(j, i, area)  # x,y
            result.append(area)

result = sorted(result)
print(cnt)
for i in result:
    print(i,end=' ')