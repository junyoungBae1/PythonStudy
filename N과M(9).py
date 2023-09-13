# 15663 N과M(9) https://www.acmicpc.net/problem/15663

import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
per = list(set((permutations(arr, M))))
per.sort()

for i in per:
    for j in i:
        print(j, end=" ")
    print()
