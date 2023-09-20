# 1655 가운데로 말해요 https://www.acmicpc.net/problem/1655
# heap

import heapq
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
min_heap = []
max_heap = []

for _ in range(n):
    x = int(input())
#값 넣을 떄 비교
    if len(max_heap) == 0 or x <= -max_heap[0]:
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    # Balance the heaps
    if len(max_heap) < len(min_heap):
        t = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -t)
    elif len(max_heap) > len(min_heap) + 1:
        t = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, t)
    print(-max_heap[0])
