# 결혼식(5567) https://github.com/junyoungBae1/PythonStudy/edit/main/README.md
# BFS

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(k):
    count = len(graph[k]) + 1
    visited[k] = 1
    q = deque()
    q.append(k)
    while q:
        count -= 1
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
        if count == 0:
            return


bfs(1)
invite = -1
for i in visited:
    if i == 1:
        invite += 1
print(invite)
