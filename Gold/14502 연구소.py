# 14502 연구소 https://www.acmicpc.net/problem/14502
from collections import  deque
import copy

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lab = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 3
result = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    lab.append(tmp)

def bfs():
    queue = deque()
    tmp = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                queue.append((i,j))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx,ny))
    global result
    cnt = 0
    for i in range(n):
        cnt += tmp[i].count(0)
    result = max(result,cnt)

def makeWall(cnt):
    if cnt == 0:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(cnt-1)
                lab[i][j] = 0

makeWall(cnt)
print(result)
