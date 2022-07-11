# 연결요소의개수(11724) https://www.acmicpc.net/problem/11724
# BFS, DFS

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# N = 정점의 개수, M = 간선의 개수
N, M = map(int, input().split())
visited = [1] + [0] * N
graph = [[] for _ in range(N + 1)]
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(i):
    visited[i] = 1
    for i in graph[i]:
        if visited[i] == 0:
            dfs(i)


for i in range(N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)

