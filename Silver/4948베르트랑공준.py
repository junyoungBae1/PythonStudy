# 4948 베르트랑 공준

import sys

input = sys.stdin.readline

flag = 1


def is_prime_num(n):
    arr = [True] * (2 * n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, 2 * n + 1):
        if arr[i]:
            j = 2
            while (i * j) <= 2 * n:
                arr[i * j] = False
                j += 1
    return arr


while flag == 1:
    n = int(input())
    if n == 0:
        flag = 0
        break

    arr = is_prime_num(n)
    cnt = 0
    for i in range(n+1,2*n+1):
        if arr[i]:
            cnt += 1
    print(cnt)

