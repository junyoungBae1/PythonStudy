# 연속합(1912) https://www.acmicpc.net/problem/1912
# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [arr[0], arr[0]]

for i in range(1,n-1):
    if arr[i] >= 0:
        d[0] += arr[i]
        d[1] += arr[i]
    else:
        if d[1] > d[0]:
            d[0] = d[1]
        else:
            d[0] += arr[i]
        if d[i] < 0:
            continue
        else:
            d[i] = 0
print(d[0])
