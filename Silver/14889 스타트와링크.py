# 14889 스타트와 링크

import sys
from itertools import combinations

combi = combinations
input = sys.stdin.readline

# 백트래킹
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [False for _ in range(n)]
result = 10e9


def dfs(depth, idx):
    global result
    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start += arr[i][j]
                elif not visit[i] and not visit[j]:
                    link += arr[i][j]
        result = min(result, abs(start - link))
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            dfs(depth+1, i + 1)
            visit[i] = False


dfs(0, 0)
print(result)

# 완전 탐색 알고리즘
#
#
# result = 10e9
# n = int(input())
#
# start = list(i for i in range(n))
#
# arr = []
# for i in range(n):
#     team = list(map(int, input().split()))
#     arr.append(team)
#
# S1 = list(combi(start, int(n / 2)))
#
# for i in S1:
#     TF = [True] * n
#     for j in i:
#         TF[j] = False
#     S2 = list(combi(i, 2))
#     start_team = 0
#     for a, b in S2:
#         start_team += arr[a][b] + arr[b][a]
#
#     link = []
#     for j in range(n):
#         if TF[j]:
#             link.append(j)
#     S3 = list(combi(link,2))
#     link_team = 0
#     for a,b in S3:
#         link_team += arr[a][b] + arr[b][a]
#
#     result = min(result, abs(start_team-link_team))
#
# print(result)
