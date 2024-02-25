# 1654 랜선 자르기 https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)
mid = (start + end) // 2

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // mid # 분할된 랜선수

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
