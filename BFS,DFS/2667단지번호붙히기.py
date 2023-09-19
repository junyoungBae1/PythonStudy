# 2667 단지번호 붙이기 https://www.acmicpc.net/problem/2667

import sys
from collections import deque

dp = [[1, 0], [-1, 0], [0, 1], [0, -1]]

input = sys.stdin.readline

N = int(input())
visited = [[0 for x in range(N)] for _ in range(N)]
maps = []
result = []
for i in range(N):
    arr = list(map(int,input().strip()))
    maps.append(arr)


def bfs(value):

    q = deque()
    q.append(value)

    visited[value[0]][value[1]] = 1
    cnt = 1
    while q:
        y, x = q.popleft()

        for i in dp:
            a = x + i[1]
            b = y + i[0]

            if 0 <= a < N and 0 <= b < N and maps[b][a] == 1 and visited[b][a] == 0:

                    q.append([b, a])
                    cnt += 1
                    visited[b][a] = 1

    return cnt


for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:
            k = bfs([i, j])
            if k != 0:
                result.append(k)

print(len(result))
for res in sorted(result):
    print(res)
