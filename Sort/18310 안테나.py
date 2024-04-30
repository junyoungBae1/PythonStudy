# 18310 안테나

import sys

input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))
house.sort()

if len(house) % 2 == 1:
    print(house[n//2])
else:
    print(min(house[(n-2) // 2],house[n//2]))
