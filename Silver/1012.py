# 1012 유기농 배추 https://www.acmicpc.net/problem/1012
# BFS(stack 사용) ,DFS(재귀 사용)

from collections import deque
import sys

sys.setrecursionlimit(10000)  # 재귀함수를 사용할 때 깊이 제한

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 넓이 우선 탐색
def bfs(field, y, x):
    queue = deque()
    queue.append((y, x))
    field[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if field[ny][nx] == 1:
                field[ny][nx] = -1
                queue.append((ny, nx))
    return


# 깊이 우선 탐색
def dfs(field, y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(field, ny, nx)


input = sys.stdin.readline
T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        A, B = map(int, input().split())
        field[B][A] = 1
    earthworm = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                earthworm += 1
                dfs(field, y, x)

    print(earthworm)
