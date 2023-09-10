# 도영이가만든맛있는음식(2961) https://www.acmicpc.net/problem/2961
# 브루트포스(brute force), 비트 마스킹(bit masking)
# itertools combinations

import sys, itertools
from itertools import combinations

input = sys.stdin.readline

n = int(input())
sin = []
dal = []
for _ in range(n):
    a, b = map(int, input().split())
    sin.append(a)
    dal.append(b)
result = []
result2 = []
food = float('inf')
for i in range(1,n+1):
    Combi = combinations(sin, i)
    Combi2 = combinations(dal, i)
    combi = list(Combi)
    combi2 = list(Combi2)
    for j in combi:
        temp = 1
        for k in j:
            temp *= k
        result.append(temp)
    for x in combi2:
        temp = 0
        for y in x:
            temp += y
        result2.append(temp)
a = result
b = result2

for i in range(len(a)):
    food = min(food, abs(a[i] - b[i]))
print(food)
