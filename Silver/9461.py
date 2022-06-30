# 9461 파도반 수열 https://www.acmicpc.net/problem/9461

import sys

T = int(sys.stdin.readline())
N = list()
for i in range(T):
    N.append(int(sys.stdin.readline()))

M = max(N)
d = [1 for x in range(M+1)]

for i in range(4, M+1):
    d[i] = d[i-3] + d[i-2]

for i in N:
    print(d[i])
