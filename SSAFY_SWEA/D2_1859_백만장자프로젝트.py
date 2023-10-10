import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    money = 0
    cnt = 0
    dp = [0] * N

    buy = list(map(int, input().split()))
    sell = max(buy)
    for i in range(N):
        if sell > buy[i]:
            cnt += 1
            money -= buy[i]
        elif sell == buy[i]:
            money = money + cnt * buy[i]
            cnt = 0
            if i != N - 1:
                sell = max(buy[k] for k in range(i + 1, N))
    if money < 0:
        money = 0
    print("#{} {}".format(test_case, money))
