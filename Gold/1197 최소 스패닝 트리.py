#1197 최소 스패닝 트리https://www.acmicpc.net/problem/1197

import sys

input = sys.stdin.readline

v,e = map(int,input().split())

parent = [ x for x in range(v+1)]
edges = []

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

def union(a,b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

answer = 0
edges.sort(key=lambda x:x[2])

for edge in edges:
    x,y,cost = edge[0],edge[1],edge[2]
    #사이클을 만들면 무시
    if find_parent(x) == find_parent(y):
        continue

    union(x,y)
    answer += cost

print(answer)