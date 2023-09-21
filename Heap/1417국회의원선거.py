# 1417 국회의원선거 #https://www.acmicpc.net/problem/1417

#

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
me = 0
if n == 1:
    print(0)
    exit(0)

for i in range(n):

    x = int(input())
    if i == 0:
        me = x
    else:
        heapq.heappush(heap, -x)

x = 101
cnt = 0
for i in range(101):
    x = -heapq.heappop(heap)
    if me <= x:
        x -= 1
        me += 1
        cnt += 1
        heapq.heappush(heap, -x)
    elif me > x:
        break

print(cnt)

