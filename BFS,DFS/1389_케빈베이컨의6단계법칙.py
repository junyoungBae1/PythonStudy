# # 1389 케빈 베이컨의 6단계 법칙 https://www.acmicpc.net/problem/1389
# bfs

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = list([] for i in range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

    return sum(distance)


result = []
for i in range(1, n + 1):
    result.append(bfs(i))

print(result.index(min(result)) + 1)  # index is zero-based


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = list([] for i in range(n + 1))
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# result = [500001]
# def bfs(val):
#     cntarr = []
#
#     for i in range(1, n+1):
#         cnt = 0
#         q = deque()
#         if val != i:
#             q.append(val)
#             while q:
#                 cnt += 1
#                 x = q.popleft()
#                 for j in graph[x]:
#                     if j == i:
#                         cntarr.append(cnt)
#                         q.clear()
#                         break
#                     else:
#                         q.append(j)
#     sum = 0
#     while cntarr:
#         sum += cntarr.pop()
#     return sum
#
# for k in range(1,n+1):
#     result.append(bfs(k))
#
# print(result.index(min(result)))
#
#
#
