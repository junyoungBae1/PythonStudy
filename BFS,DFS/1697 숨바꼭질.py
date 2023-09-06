# 숨바꼭질(1697) https://www.acmicpc.net/problem/1697
# BFS

import sys
from collections import deque

input = sys.stdin.readline

M = 10 ** 5
dist = [0] * (M + 1)
N, K = map(int, input().split())


def bfs(N):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            return dist[x]
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= M:
                if dist[i] == 0:
                    dist[i] = dist[x] + 1
                    q.append(i)


print(bfs(N))
