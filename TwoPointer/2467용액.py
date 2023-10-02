# 2467 https://www.acmicpc.net/problem/2467

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = arr[0] + arr[1]
left_idx = 0
right_idx = n - 1
x = 0
y = 1

while left_idx < right_idx:
    temp = arr[left_idx] + arr[right_idx]
    if abs(result) > abs(temp):
        result = temp
        x = left_idx
        y = right_idx
        if result == 0:
            break

    if temp < 0:
        left_idx = left_idx + 1
    elif temp > 0:
        right_idx = right_idx - 1

print(arr[x], arr[y])
