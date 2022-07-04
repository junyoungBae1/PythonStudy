# 결혼식(5567) https://github.com/junyoungBae1/PythonStudy/edit/main/README.md
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)


def bfs(x):
    queue = deque()
    visited[x] = 1
    count = len(graph[x]) + 1
    queue.append(x)
    while queue:
        count -= 1
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
        if count == 0:
            return

bfs(1)
invite = -1
for i in visited:
    if i == 1:
        invite += 1
print(invite)
