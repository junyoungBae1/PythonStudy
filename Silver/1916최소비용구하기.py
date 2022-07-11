# 최소비용구하기(1916) https://www.acmicpc.net/problem/1916
# Dijkstra Algorithm
# 벨만 포드 알고리즘 -> 매 단계마다 모든 간선을 확인 --> 시간복잡도 O(VE)
# 다익스트라 알고리즘 -> 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택 (OElogV)

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
dist = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, c = map(int, input().split())
    graph[start].append([end, c])

x, y = map(int, input().split())


def dijkstra():
    dist[x] = 0
    queue = [(x, 0)]
    while queue:
        curr, w = heapq.heappop(queue)

        if dist[curr] < w:  #이미 처리되었다면 무시
            continue

        for i in graph[curr]:
            cost = dist[curr] + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))


dijkstra()
print(dist[y])
