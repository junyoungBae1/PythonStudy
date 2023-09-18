#1927 최소 힙 https://www.acmicpc.net/problem/1927

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
result = []
for i in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)

for res in result:
    print(res)
