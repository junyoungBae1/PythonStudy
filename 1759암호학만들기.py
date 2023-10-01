# 1759암호학만들기  https://www.acmicpc.net/problem/1759
#

import sys
from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']

input = sys.stdin.readline

l, c = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()
com = list(combinations(arr, l))

result = []

for i in com:
    cnt_c = 0
    cnt_v = 0
    for j in i:
        if j in vowels:
            cnt_v += 1
        else:
            cnt_c += 1
    if cnt_v >= 1 and cnt_c >= 2:
        for k in sorted(i):
            print(k, end="")
        print()
