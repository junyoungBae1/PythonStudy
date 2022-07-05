# 좌표압축(18870) https://www.acmicpc.net/problem/18870
# sort, 값 / 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr2 = sorted(set(arr))

dic = dict()
for i in range(len(arr2)):
    dic[arr2[i]] = i

for i in arr:
    print(dic[i], end=" ")

""" 
시간초과 O(N^2)
for _ in range(n):
    m = arr1[cnt]
    for i in range(n):
        if arr[i] > m:
            result[i] += 1
    cnt += 1
"""
