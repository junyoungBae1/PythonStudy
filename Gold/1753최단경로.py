# 1753 최단경로 https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]


for i in range(1, e + 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def Dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


Dijkstra(k)

for i in range(1, v + 1):
    print("INF" if distance[i] == INF else distance[i])
