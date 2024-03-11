# 1890 점프

import sys

input = sys.stdin.readline

n = int(input())

game = [list(map(int, input().split())) for _ in range(n)]

dp = [list(0 for _ in range(n)) for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if game[i][j] == 0:
            continue
        jump = game[i][j]
        #오른쪽으로 점프
        if j + game[i][j] < n:
            dp[i][j+jump] += dp[i][j]
        if i + game[i][j] < n:
            dp[i+jump][j] += dp[i][j]
print(dp[n-1][n-1])
#
# cnt = 0
#
#
# def dfs(a, b):
#     global cnt
#     if a == n-1 and b == n-1:
#         cnt += 1
#         return
#     if game[a][b] == 0:
#         return
#     else:
#         if b + game[a][b] < n:
#             dfs(a, b + game[a][b])
#         if a + game[a][b] < n:
#             dfs(a + game[a][b], b)
#
#         return
#
# dfs(0, 0)
# print(cnt)
