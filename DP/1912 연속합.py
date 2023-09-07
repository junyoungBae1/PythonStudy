# 연속합(1912) https://www.acmicpc.net/problem/1912
# DP
import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))
d = [0] * n
d[0] = seq[0]
for i in range(1, n):
    d[i] = max(seq[i], (d[i - 1] + seq[i]))

print(max(d))
