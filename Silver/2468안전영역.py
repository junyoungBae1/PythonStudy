# 2468 안전영역


import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
rain = max(map(max, arr))
temp = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

result = 0
cnt = 0


def bfs(rain):
    global cnt
    q = deque()
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 1 and visited[i][j] == 0:
                cnt += 1

                q.append([i, j])
                visited[i][j] = 1
                while q:
                    a,b = q.popleft()
                    for k in range(4):
                        da = a + dx[k]
                        db = b + dy[k]
                        if 0 <= da < n and 0 <= db < n:
                            if temp[da][db] == 0 and visited[da][db] == 0:
                                visited[da][db] = 1
                            elif temp[da][db] == 1 and visited[da][db] == 0:
                                q.append([da, db])
                                visited[da][db] = 1

            elif temp[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1


for x in range(rain - 1, -1, -1):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > x:
                temp[i][j] = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    bfs(x)

    result = max(result, cnt)

print(result)