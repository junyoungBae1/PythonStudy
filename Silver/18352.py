# 18352 특정 거리의 도시 찾기 https://www.acmicpc.net/problem/18352

import sys
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    graph[x] = 1
    distance[x] = 0
    while queue:
        q = queue.popleft()
        for i in arr[q]:
            if graph[i] == 0:
                graph[i] = 1
                queue.append(i)
                distance[i] = distance[q] + 1



input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
arr = [[] for _ in range(n+1)]

for _ in range(m):
    X, Y = map(int, input().split())
    arr[X].append(Y)

bfs(x)
if k not in distance:
    print(-1)
else:
    for i, dis in enumerate(distance):
        if dis == k:
            print(i)
dic2 ={}
dic2[1] = []
print(dic2)
