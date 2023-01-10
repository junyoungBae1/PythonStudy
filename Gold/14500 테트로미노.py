# 14500 테트로미노 https://www.acmicpc.net/problem/14500

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0


def dfs(x, y, dsum, cnt):
    global result

    if cnt == 4:
        result = max(result, dsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, dsum + paper[nx][ny], cnt + 1)
            visited[nx][ny] = 0
#ㅗ,ㅜ,ㅏ,ㅓ
def exce(x,y):
    global result
    for i in range(4):
        tmp = paper[x][y]
        for j in range(3):
            k = (i+j) % 4
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx <n and 0 <=ny<m:
                tmp += paper[nx][ny]
            else:
                tmp = 0
                break
        result = max(result,tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = 0

        exce(i, j)

print(result)
