# 14502 연구소
import copy
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

lab = []
answer = 0

for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque()
    copylab = copy.deepcopy(lab)

    for i in range(n):
        for j in range(m):
            if copylab[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copylab[nx][ny] == 0:
                    copylab[nx][ny] = 2
                    q.append([nx, ny])

    global answer
    cnt = 0
    for i in range(n):
        cnt += copylab[i].count(0)
    answer = max(answer,cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(cnt + 1)
                lab[i][j] = 0

makeWall(0)
print(answer)
