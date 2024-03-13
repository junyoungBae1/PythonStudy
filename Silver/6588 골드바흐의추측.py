# 6588 골드바흐의 추측

import sys

input = sys.stdin.readline


def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):  # i의 배수들을 False로 설정
                arr[j] = False
    return arr


arr = is_prime(1000001)
prime = list()
for i in range(3, 100001):
    if arr[i]:
        prime.append(i)

while 1:
    n = int(input())
    if n == 0:
        break

    flag = 0
    for p in prime:
        if arr[n - p]:
            print(f"{n} = {p} + {n - p}")
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong")
