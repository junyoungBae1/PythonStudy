# 6064 카잉 달력
# https://www.acmicpc.net/problem/6064
#브루트포스 알고리즘
import sys
import math

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    m, n, x, y = map(int, input().split())

    lcm = m * n // math.gcd(m,n)
    while x <= lcm:
        if (x-y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)




    # while True:
    #     if i == x and j == y:
    #         print(cnt)
    #         break
    #     elif i > m or j > n:
    #         print(-1)
    #         break
    #     elif i == m and j != n:
    #         i = 0
    #     elif i != m and j == n:
    #         j = 0
    #
    #     i += 1
    #     j += 1
    #     cnt += 1