# 동전0(11047) https://www.acmicpc.net/problem/11047
# 그리디 알고리즘

import sys
input = sys.stdin.readline

n, price = map(int, input().split())
coin_lst = list()
for _ in range(n):
    coin_lst.append(int(input()))
cnt = 0  #동전 갯수
#for i in range(n-1, 0, -1):
for i in reversed(range(n)):
    cnt += price//coin_lst[i]
    price %= coin_lst[i]

print(cnt)

