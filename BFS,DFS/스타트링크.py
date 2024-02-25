# 5014 스타트링크 https://www.acmicpc.net/problem/5014
# dfs

import sys
from collections import deque

input = sys.stdin.readline
# f:끝층,s:현재위치,g:스타트링크,u:위층.d:아래층
f, s, g, u, d = map(int, input().split())
cnt = list(1000001 for _ in range(f + 1))
cnt[s] = 0

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        # up
        a = x + u

        if a < f+1:
            if cnt[a] == 1000001:
                q.append(a)
            cnt[a] = min(cnt[a], cnt[x] + 1)
            if a == g:
                return
        # down
        b = x - d
        if b > 0:
            if cnt[b] == 1000001:
                q.append(b)
            cnt[b] = min(cnt[b], cnt[x] + 1)
            if b == g:
                return


bfs(s)

if cnt[g] == 1000001:
    print("use the stairs")
else:
    print(cnt[g])
