# 좌표압축(18870) https://www.acmicpc.net/problem/18870
# sort, 값 / 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
arr = [x for x in map(int, input().split())]


dic = dict()
s_arr = sorted(arr)

cnt = 0
for i,k in enumerate(s_arr):
    if dic.get(k) == None:
        dic[k] = cnt
        cnt += 1

for i in arr:
    print(dic[i], end=" ")

