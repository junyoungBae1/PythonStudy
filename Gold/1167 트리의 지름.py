# 1167 트리의 지름 https://www.acmicpc.net/problem/1167

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(x,y):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = y+b
            dfs(a,y+b)


n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for j in range(1, (len(info))+1, 2):
        if info[j] == -1:
            break
        graph[info[0]].append((info[j], info[j + 1]))


visited = [-1] * (n+1)
visited[1] = 0
dfs(1,0)

start = visited.index(max(visited))

visited = [-1] * (n+1)
visited[start] = 0
dfs(start,0)

print(max(visited))
