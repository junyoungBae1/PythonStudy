# 구간 합 구하기 5 https://www.acmicpc.net/problem/11660

import sys
#표의 크기 n
#합을 구해야 하는 횟수 m
n,m = map(int,input().split())

graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i-1][j-1]

for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())

    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)

