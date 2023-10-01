# 16953 https://www.acmicpc.net/problem/16953
#

import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())


def bfs(k, depth):
    q = deque()
    q.append((k, depth))
    while q:
        x, d = q.popleft()
        if x == b:
            return d
        elif x < b:
            if 10 * x + 1 <= b or 2 * x <= b:
                q.append((10 * x + 1,d+1))
                q.append((2 * x,d+1))
    return -1


print(bfs(a, 1))
