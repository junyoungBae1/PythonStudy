# 1743 음식물피하기

import sys
from collections import deque

input = sys.stdin.readline

move = [[0, 1], [1, 0], [-1, 0], [0, -1]]

n, m, k = map(int, input().split())
hotel = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0
for i in range(k):
    y, x = map(int, input().split())
    hotel[y - 1][x - 1] = 1


def bfs(y, x):
    q = deque()
    q.append([y, x])
    cnt = 0

    while q:
        cnt += 1
        a, b = q.popleft()
        for i in move:
            da = a + i[0]
            db = b + i[1]
            if 0 <= da < n and 0 <= db < m:
                if visited[da][db] == 0 and hotel[da][db] == 1:
                    q.append([da,db])
                    visited[da][db] = 1

    return cnt


for i in range(n):
    for j in range(m):
        if hotel[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            result = max(result, bfs(i, j))


print(result)
