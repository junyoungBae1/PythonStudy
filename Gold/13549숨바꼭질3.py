# 숨바꼭질3(13549) https://www.acmicpc.net/problem/13549
# BFS, 다익스트라



import sys
from collections import deque
input = sys.stdin.readline

M = 10 ** 5
dist = [-1] * (M + 1)
A, B = map(int, input().split())

def dijkstra():
    queue = deque()
    dist[A] = 0
    queue.append(A)
    while queue:
        x = queue.popleft()
        if x == B:
            return dist[x]
        for i in (x*2, x - 1, x + 1):
            if 0 <= i <= M:
                if dist[i] == -1:
                    if x * 2 == i:
                        dist[i] = dist[x]
                    else:
                        dist[i] = dist[x] + 1
                    queue.append(i)


print(dijkstra())
