# 1715 카드정렬 https://www.acmicpc.net/problem/1715
# heap

import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x = int(input())
    heapq.heappush(heap, x)

result = 0
temp = 0
while heap:
    if temp == 0:
        temp = heapq.heappop(heap)
        if len(heap) == 1:
            x = heapq.heappop(heap)
            result = result + temp + x
    elif temp != 0:
        temp2 = heapq.heappop(heap)
        x = temp + temp2
        result += x
        heapq.heappush(heap, x)
        temp = 0

print(result)
