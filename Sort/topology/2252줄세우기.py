# 2252 줄세우기 https://www.acmicpc.net/problem/2252
# 위상정렬 topology sort
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
inDegree[0] = -1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

arr = []
q = deque()
for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)


while q:
    student = q.popleft()
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            q.append(j)
    print(student, end=" ")


# 시간초과... O(N**2)
# n, m = map(int, input().split())
# graph = []
# for i in range(m):
#     a, b = map(int, input().split())
#     graph.append([a,b])
#
# arr = [i for i in range(1,n+1)]
#
# for i in graph:
#     a = arr.index(i[0])
#     b = arr.index(i[1])
#     if i[0] < i[1] and a < b:
#         continue
#     elif i[0] < i[1] and a > b:
#         arr.insert(a,i[0])
#         del arr[a]
#         #값넣고 삭제
#     elif i[1] < i[0] and a < b:
#         continue
#     elif i[1] < i[0] and a > b:
#         del arr[b]
#         arr.insert(a,i[1])
#
# print(arr)
