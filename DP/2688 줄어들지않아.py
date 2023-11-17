# 2688 줄어들지 않아 https://www.acmicpc.net/problem/2688
# dp


t = int(input())

for q in range(t):
    n = int(input())
    dp = [[0] * (11) for _ in range(n + 1)]
    dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
    # dp[2] = [10,9,8,7,6,5,4,3,2,1,55]
    # dp[3] = [55,45,
    if n == 1:
        print('10')
        continue
    for i in range(2, n + 1):
        for j in range(11):
            if j == 0:
                dp[i][j] = dp[i - 1][10]
            elif j == 10:
                total = 0
                for k in range(10):
                    total += dp[i][k]
                dp[i][j] = total
            else:
                dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
    print(dp[n][10])
