# 1931 회의실 배정 https://www.acmicpc.net/problem/1931
#sort

import sys

input = sys.stdin.readline

n = int(input())

time_arr = []
for _ in range(n):
    a,b = map(int,input().split())
    time_arr.append([a,b])

time_arr.sort(key=lambda x:(x[1],x[0]))

cnt = 0
start = -1
end = -1
for i in range(n):
    if end <= time_arr[i][0]:
        start = time_arr
        end = time_arr[i][1]
        cnt += 1

print(cnt)
