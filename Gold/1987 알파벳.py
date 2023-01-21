# 1987 알파벳 https://www.acmicpc.net/problem/1987

import sys

input = sys.stdin.readline


def bfs():
    global cnt
    queue = set([(0, 0, board[0][0])])

    while queue:
        x, y, z = queue.pop()

        cnt = max(cnt, len(z))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in z:
                queue.add((nx, ny, board[nx][ny] + z))

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1

bfs()
print(cnt)
