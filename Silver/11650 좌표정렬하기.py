# 11650 좌표 정렬하기  https://www.acmicpc.net/problem/11650

import sys

input = sys.stdin.readline

n = int(input())
xy_list = []

for i in range(n):
    xy_list.append(list(map(int, input().split())))
xy_list.sort(key=lambda x: (x[0],x[1]))
for i in xy_list:
    print(i[0],i[1])
