# 15486 퇴사2 https://www.acmicpc.net/problem/15486

# dp

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())
dp = [0 for _ in range(n + 1)]

max_value = 0 #최대 수익 저장
for i in range(1,n+1):
    dp[i] = max(dp[i], dp[i - 1])
    fin_date = i+t[i]-1
    if fin_date <= n:
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 값이 아닌 i-1일까지
        # 얻을 수 있는 최댓값
        dp[fin_date] = max(dp[fin_date], dp[i-1] + p[i])
print(max(dp))



from sys import stdin

N = int(stdin.readline())
dp = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, stdin.readline().split())
    dp[i] = max(dp[i-1], dp[i])
    if i+t<=N+1:
        dp[i+t-1] = max(dp[i-1]+p, dp[i+t-1])

print(dp[-1])
# if 조건이 필요,
# if s[1][1] <= n:
#     dp[1] = s[1][1]
# if n >= 2:
#     if s[1][0] == 1 and s[2][0] <= n:
#         dp[2] = dp[1] + s[2][1]
#     elif s[2][0] <= n:
#         dp[2] = s[2][1]
#
# if n == 1:
#     print(dp[0])
#     exit(0)
# elif n == 2:
#     print(dp[1])
#     exit(0)
# for i in range(2, n):
#     for j in range(i-1,-1,-1):
#         print("i:",i,"j:",j)
#         if i-j == s[j][0]:
#             print(i,j,i-j)
#             dp[i] = dp[j] + s[i][1]
#             continue
#         else:
#             print("else")
#             dp[i] = s[i][1]
#     print(dp)
