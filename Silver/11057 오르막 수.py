# 11057 오르막 수

import sys

input = sys.stdin.readline

n = int(input())

dp = [1 for _ in range(10)]

for i in range(n - 1):
    for j in range(1, 10):
        dp[j] += dp[j - 1]
        print(dp)

print(sum(dp) % 10007)
