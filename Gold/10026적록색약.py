# 적록색약(10026) https://www.acmicpc.net/problem/10026
# DFS,BFS

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

CB, NCB = 0, 0

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(input().rstrip()))

visited = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x,y):
    visited[x][y] = 1
    curr = arr[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0:
                if arr[nx][ny] == curr:
                    dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            NCB += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

# visited 초기화
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            CB += 1

print(NCB, CB)
