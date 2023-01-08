# N-Queen  https://www.acmicpc.net/problem/9663
# 백트래킹 promising
import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
row = [0] * n


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)


dfs(0)
print(cnt)
