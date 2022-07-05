# 바이러스(2606) https://www.acmicpc.net/problem/2606
# BFS, DFS

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v):
    queue = deque()
    visited[v] = 2
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)



dfs(1)
result = 0
for i in visited:
    if i == 1:
        result += 1

print(result-1)
