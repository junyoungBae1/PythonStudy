# 1967 트리의 지름 https://www.acmicpc.net/problem/1967

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x,y):
    for a, b in tree[x]:
        if visited[a] == -1:
            visited[a] = y+b
            dfs(a,y+b)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])
visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (n+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))

