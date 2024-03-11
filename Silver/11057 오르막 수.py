# 11057 오르막 수

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# dp = [1 for _ in range(10)]
#
# for i in range(n - 1):
#     for j in range(1, 10):
#         dp[j] += dp[j - 1]
#         print(dp)
#
# print(sum(dp) % 10007)
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
mod = 10007

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= mod

print(sum(dp[n]) % mod)