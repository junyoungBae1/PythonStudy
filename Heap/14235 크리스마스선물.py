# 14235 https://www.acmicpc.net/problem/14235

import sys
import heapq

input = sys.stdin.readline

n = int(input())
gift = []
for i in range(n):
    a = list(map(int,input().split()))
    if a[0] == 0:
        if gift:
            print(-(heapq.heappop(gift)))
        else:
            print(-1)
    else:
        for enum,j in enumerate(a):
            if enum == 0:
                continue
            else:
                heapq.heappush(gift,-j)
