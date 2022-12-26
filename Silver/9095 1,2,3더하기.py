# 9095 1,2,3 더하기  https://www.acmicpc.net/problem/9095

import sys

input = sys.stdin.readline

T = int(input())


def ans(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return ans(n - 1) + ans(n - 2) + ans(n - 3)


for i in range(T):
    n = int(input())
    print(ans(n))
