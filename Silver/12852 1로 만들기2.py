# 12852 1로 2만들기

import sys

input = sys.stdin.readline

n = int(input())
dp = list(10 ** 6 for _ in range(n + 1))
dp[0] = 0
dp[1] = 0
prev = [-1 for _ in range(n+1)]

for i in range(1, n):
    if 3 * i <= n and dp[3 * i] > dp[i] + 1:
        dp[3 * i] = dp[i] + 1
        prev[3 * i] = i
    if 2 * i <= n and dp[2 * i] > dp[i] + 1:
        dp[2 * i] = dp[i] + 1
        prev[2 * i] = i
    if i + 1 <= n and dp[i + 1] > dp[i] + 1:
        dp[i + 1] = dp[i] + 1
        prev[i + 1] = i

print(dp[n])
x = n
result = []
while x != -1:
    result.append(x)
    x = prev[x]

for i in result:
    print(i, end=" ")