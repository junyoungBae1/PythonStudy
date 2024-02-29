# 10773제로

#

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    if temp != 0:
        arr.append(temp)
    else:
        arr.pop(len(arr)-1)
result = 0
for i in arr:
    result += i

print(result)

