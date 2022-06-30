# 9613 GCD 합 https://www.acmicpc.net/problem/9613
# 브루트포스 알고리즘, 유클리드 호제법
import sys

T = int(input())


def GCD(x, y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y:
        temp = x % y
        x = y
        y = temp
    return x


for i in range(T):
    sum = 0
    arr = list(map(int, sys.stdin.readline().split()))

    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            sum += GCD(arr[j], arr[k])
    print(sum)
