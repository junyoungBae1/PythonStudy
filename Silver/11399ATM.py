# ATM(11399) https://www.acmicpc.net/problem/11399
# GA(그리디)

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
sum = 0
for i in arr:
    sum = sum + i
    result += sum
print(result)
