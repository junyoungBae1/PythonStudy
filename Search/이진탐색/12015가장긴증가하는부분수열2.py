# 12015 가장 긴 증가하는 부분 수열2 https://www.acmicpc.net/problem/12015
# 이진탐색

import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

LIS = list()
LIS.append(seq[0])


def add(LIS, value):
    LIS.append(value)


def confrontation(LIS, value):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == value:
            return mid
        elif LIS[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    LIS[start] = value


for i in range(1, n):
    x = LIS[-1]  # max
    if seq[i] > x:
        LIS.append(seq[i])
    else:
        confrontation(LIS, seq[i])

print(len(LIS))
