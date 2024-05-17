# 10819 차이를 최대로
import itertools
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
nPa = permutations(a,n)

max_result = 0
for i in nPa:
    result = 0
    for j in range(n-1):
        result += abs(i[j] - i[j+1])

    max_result = max(result,max_result)

print(max_result)
