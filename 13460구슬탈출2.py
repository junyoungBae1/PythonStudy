# 13460 구슬 탈출2 https://www.acmicpc.net/problem/13460

import sys
from collections import deque

input = sys.stdin.readline

R, B, O = [], [], []
n, m = map(int, input().split())
visited = []
arr = []
for i in range(n):
    arr.append(input().strip('\n'))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            R = [i, j]
        if arr[i][j] == 'B':
            B = [i, j]
        if arr[i][j] == 'O':
            O = [i, j]

cnt = 0


def bfs(R, B):
    q = deque()
    q.append([R,B])

    while q:
        x, y = q.popleft()
        # 왼쪽
        while 1:
            #blue ball
            if arr[[x[0]][(x[1]-1)]] == ("#" or "R"):
                break
            elif arr[[x[0]][(x[1]-1)]] == ".":
                x[1] -= 1



        print(x,y)
        # 오른쪽
        # 위
        # 아래
# R가 먼저있으면 레드부터,
# B가 먼저 있으면 먼저 움직임.
# vi

bfs(R, B)

print(R, B, O)
