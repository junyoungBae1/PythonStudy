# 1546 평균 https://www.acmicpc.net/problem/1546

import sys

input = sys.stdin.readline
N = int(input())
Nlist = list(map(int,input().split()))
Mscore = max(Nlist)

Mlist = []
for i in range(N):
    Mlist.append(Nlist[i]/Mscore * 100)

avg = sum(Mlist)/N
print(avg)
