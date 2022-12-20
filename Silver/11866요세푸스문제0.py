# 11866 요세푸스 문제 0 https://www.acmicpc.net/problem/11866

import sys

input = sys.stdin.readline
N, K = map(int, input().split())

A = [i+1 for i in range(N)]
removed = []
now = K-1
while A:
    removed.append(A.pop(now))
    if A:
        now = ((now-1) + K) % len(A)
print(f'<{", ".join(map(str,removed))}>')
