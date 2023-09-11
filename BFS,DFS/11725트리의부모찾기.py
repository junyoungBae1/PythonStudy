# 11725 트리의 부모 찾기 https://www.acmicpc.net/problem/11725
# bfs,dfs 그래프


import sys
from collections import deque
limit_number = 10**9
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline

n = int(input())

graph = list([] for _ in range(n + 1))
result = [0] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()


def dfs(X):
    parent = X
    q.append(graph[X])
    while q:
        x = q.popleft()
        for k in x:
            if result[k] == 0:
                result[k] = X
                dfs(k)


dfs(1)
for i in range(2,n+1):
    print(result[i])
