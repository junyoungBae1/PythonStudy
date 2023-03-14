# 15650 N과 M(2) https://www.acmicpc.net/problem/15650

import sys

n,m = map(int, input().split())
s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()


dfs(1)
