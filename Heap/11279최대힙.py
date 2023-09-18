# 11279 최대힙 https://www.acmicpc.net/problem/11279

import sys
import heapq

input = sys.stdin.readline

heap = []
result = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            result.append(0)
        else:
            result.append(heapq.heappop(heap)[1])
    heapq.heappush(heap, (-x,x))

for res in result:
    print(res)
