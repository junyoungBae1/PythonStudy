# 1926

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

grim = [list(map(int, input().split())) for _ in range(n)]
visited = list([0 for _ in range(m)] for _ in range(n))


width = 0
def bfs(y, x):
    q = deque()
    q.append([y, x])
    size = 1
    while q:
        a, b = q.popleft()
        for i in move:
            da = a + i[0]
            db = b + i[1]
            if 0 <= da < n and 0 <= db < m:
                if visited[da][db] == 0 and grim[da][db] == 1:
                    visited[da][db] = 1
                    q.append([da,db])
                    size += 1
    return size

cnt = 0
for i in range(n):
    for j in range(m):
        if grim[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            width = max(width,bfs(i, j))

print(cnt)
print(width)
