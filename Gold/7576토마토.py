# 토마토(7576) https://www.acmicpc.net/problem/7576
# BFS
import sys
import copy

input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())

visited = list()
for _ in range(b):
    visited.append(list(map(int, input().split())))


def bfs():
    global a, b
    day = -1
    queue = deque()
    for i, Y in enumerate(visited):
        for j, X in enumerate(Y):
            if X == 1:
                queue.append([j, i])

    while queue:
        cnt = 0
        copyqueue = copy.copy(queue)
        for x, y in copyqueue:
            cnt += 1
            if x + 1 < a:
                if visited[y][x + 1] == 0:
                    visited[y][x + 1] = 1
                    queue.append([x + 1, y])
            if x > 0:
                if visited[y][x - 1] == 0:
                    visited[y][x - 1] = 1
                    queue.append([x - 1, y])
            if y + 1 < b:
                if visited[y + 1][x] == 0:
                    visited[y + 1][x] = 1
                    queue.append([x, y + 1])
            if y > 0:
                if visited[y - 1][x] == 0:
                    visited[y - 1][x] = 1
                    queue.append([x, y - 1])

        for _ in range(cnt):
            queue.popleft()
        day += 1
    return day


d = bfs()
for i in visited:
    if 0 in i:
        d = -1
        break
print(d)
