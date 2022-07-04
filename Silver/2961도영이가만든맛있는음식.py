# 도영이가만든맛있는음식(2961) https://www.acmicpc.net/problem/2961
# 브루트포스(brute force), 비트 마스킹(bit masking)
# itertools combinations

import sys

input = sys.stdin.readline
n = int(input())

s = list()
b = list()

for _ in range(n):
    x, y = map(int, input().split())
    s.append(x)
    b.append(y)
if n == 1:
    print(abs(s[0]-b[0]))
else:
    diff = list()
    n = 2 ** n
    for i in range(1, n):
        bit = str(bin(i))
        S = 1
        B = 0
        for index, j in enumerate(bit[:1:-1]):
            if j == "1":
                S *= s[index]
                B += b[index]
        diff.append(abs(S-B))

    print(min(diff))

# combinations을 이용할 수 있다. (모든 경우의 수를 구해주는 라이브러리)

import sys, itertools
from itertools import combinations
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = float('inf')

for i in range(1, n+1): # 재료를 i개 뽑을 때
    idxs = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트

    for food in idxs: # 경우 하나씩 탐색
        s = 1
        b = 0

        for j in range(i): # 맛 계산
            s *= sour[food[j]]
            b += bitter[food[j]]
        if abs(s - b) < diff:
            diff = abs(s - b)

print(diff)