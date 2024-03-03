# 11052 카드구매하기


import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
dp = list(0 for _ in range(n + 1))
dp[1] = p[1]
if n > 1:
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + p[i - j])

print(dp[n])
