# 14940 쉬운최단거래

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

visited = [list(0 for _ in range(m)) for _ in range(n)]

cheeze = [list(map(int, input().split())) for _ in range(n)]

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(b, a):
    q = deque()
    q.append([b, a])
    visited[b][a] = 0
    while q:
        y, x = q.popleft()
        for i in move:
            dy = y + i[0]
            dx = x + i[1]
            if 0 <= dy < n and 0 <= dx < m:
                if visited[dy][dx] == 0 and cheeze[dy][dx] == 1:
                    visited[dy][dx] = visited[y][x] + 1
                    q.append([dy, dx])


for i in range(n):
    for j in range(m):
        if cheeze[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if cheeze[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
        print(visited[i][j], end=" ")
    print()

