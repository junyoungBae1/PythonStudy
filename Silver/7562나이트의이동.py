# 7562 나이트의 이동

import sys
from collections import deque

input = sys.stdin.readline

move = [[1, 2], [-1, 2], [-1, -2], [1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]


def bfs(x, y):
    n = len(visited)
    q = deque()
    q.append([x, y])
    while q:
        dx, dy = q.popleft()
        for i in move:
            nx = dx + i[0]
            ny = dy + i[1]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    return visited[dx][dy]
                elif visited[nx][ny] == 1:
                    continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = visited[dx][dy] + 1
                    q.append([nx, ny])


T = int(input())
for i in range(T):
    n = int(input())

    visited = list([0 for _ in range(n)] for _ in range(n))

    x, y = map(int, input().split())  # 시작
    a, b = map(int, input().split())  # 끝

    visited[x][y] = 1
    visited[a][b] = -1
    if x == a and y == b:
        print(0)
    else:
        print(bfs(x, y))
