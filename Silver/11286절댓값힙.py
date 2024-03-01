# # 11286 절대값힙
#
# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n = int(input())
# negative = []
# positive = []
#
# for i in range(n):
#     x = int(input())
#
#     if x > 0:
#         heapq.heappush(positive, x)
#     elif x < 0:
#         heapq.heappush(negative, (-x, x))
#
#     elif x == 0:
#         if len(positive) == 0 and len(negative) == 0:
#             print(0)
#         elif len(positive) == 0 and len(negative) != 0:
#             print(heapq.heappop(negative)[1])
#         elif len(positive) != 0 and len(negative) == 0:
#             print(heapq.heappop(positive))
#         elif len(positive) != 0 and len(negative) != 0:
#             a = heapq.heappop(negative)[1]
#             b = heapq.heappop(positive)
#             if abs(a) > b:
#                 heapq.heappush(negative, (-a, a))
#                 print(b)
#             elif abs(a) <= b:
#                 heapq.heappush(positive, b)
#                 print(a)
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)