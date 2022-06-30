# 9020 골드바흐의 추측 https://www.acmicpc.net/problem/9020


import sys
import math
input = sys.stdin.readline

T = int(input())


def isPrime(a):
    flag = True
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            flag = False

    return flag


for _ in range(T):

    x = 0
    y = 0
    n = int(input())

    x = n // 2
    y = n // 2
    flag = True
    while flag:
        if isPrime(x) and isPrime(y) and x+y == n:
            print(y, x)
            flag = False
        else:
            x += 1
            y -= 1
print(int(1e4))



"""
시간초과
    temp = [0, 0] + [1] * (n - 1)
    primes = list()
    for i in range(2, n + 1):
        if temp[i] == 1:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                temp[j] = 0
    for i in range(len(primes) // 2,0,-1):
        for j in range(len(primes) // 2, len(primes)):
            if n == (primes[i] + primes[j]):
                if min > abs(primes[i] - primes[j]):
                    min = abs(primes[i] - primes[j])
                    x = primes[i]
                    y = primes[j]
                    break
"""