# 1929 소수 구하기
# 소수


import sys

input = sys.stdin.readline

m, n = map(int, input().split())


def is_prime_num(k):
    arr = [True] * (k + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, k + 1):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:
                arr[i * j] = False
                j += 1
    return arr


arr = is_prime_num(n)

for i in range(m, len(arr)):
    if arr[i]:
        print(i)
