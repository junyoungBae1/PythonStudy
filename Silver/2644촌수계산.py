# 촌수계산(2644) https://www.acmicpc.net/problem/2644
# DFS, BFS

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
visited = [0] * (n + 1)
a = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(1, m + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [-1] * (n+1)
flag = 0
result[a[1]] = 0

def dfs(p):
    global flag
    visited[p] = 1
    for i in graph[p]:
        if visited[i] == 0:
            result[i] = result[p] + 1
            if i == a[0]:
                flag = 1
                return
            dfs(i)


dfs(a[1])
print(result[a[0]])
