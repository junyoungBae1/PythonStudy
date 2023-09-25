# 11000강의실배정 https://www.acmicpc.net/problem/11000
# heap

import sys
import heapq

n = int(input())
heap = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(heap, (y, x))

start = 0
end = 0
cnt = 0
while heap:
    temp = heapq.heappop(heap)
    x = temp[1]
    y = temp[0]
    if x >= end:
        start = x
        end = y
        cnt += 1


print(cnt)
