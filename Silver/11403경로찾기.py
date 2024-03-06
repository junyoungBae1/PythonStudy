# 11403 경로 찾기

# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# input = sys.stdin.readline
#
# cnt = 0
#
#
# def dfs(a, b, depth, cnt):
#     global n
#     if cnt == 1:
#         return cnt
#     elif graph[a]:
#         for i in graph[a]:
#             if i == b:
#                 return 1
#             else:
#                 if depth == n:
#                     return 0
#                 return dfs(i, b, depth + 1, cnt)
#     else:
#         return 0
#
#
# n = int(input())
#
# visited = [[0 for i in range(n)] for _ in range(n)]
# matrix = list(list(map(int, input().split())) for _ in range(n))
# graph = list([] for _ in range(n))
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             graph[i].append(j)  # i에서 j로 가는 간선
#
# for i in range(n):
#     for j in range(n):
#         cnt = 0
#         if dfs(i, j, 0, cnt):
#             visited[i][j] = 1
#
# for i in range(n):
#     for j in range(n):
#         print(visited[i][j], end=' ')
#     print()


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                print(i,j,k)
for row in graph:
    print(*row)
