# 1932 정수 삼각형 https://www.acmicpc.net/problem/1932

import sys

input = sys.stdin.readline

n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

if n > 1:
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                tri[i][j] = tri[i][j] + tri[i - 1][j]
            elif j == len(tri[i]) - 1:
                tri[i][j] = tri[i][j] + tri[i - 1][j - 1]
            else:
                tri[i][j] = max(tri[i - 1][j - 1], tri[i - 1][j]) + tri[i][j]

print(max(tri[n - 1]))
