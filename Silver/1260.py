# 1260 DFS와 BFS https://www.acmicpc.net/problem/1260

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)

for i in range(len(graph)):
    graph[i].sort()


def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            visited[i] = 1


dfs(v)
print()

visited = [0] * (n + 1)


def bfs(v):
    queue = deque()
    visited[v] = 1
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


bfs(v)

"""import sys
from collections import deque

sys.setrecursionlimit(10000)  # 재귀함수를 사용할 때 깊이 제한

n, m, v = map(int, input().split())

#for문에 변수를 remove해서 오류..
def dfs(a):
    result.append(a)
    for i in M1[:]:
        if a in i:
            if a != i[0]:
                temp = i[0]
                try:
                    M1.remove(i)
                except:
                    nothing = i
                dfs(temp)
            else:
                temp = i[1]
                try:
                    M1.remove(i)
                except:
                    nothing = i
                dfs(temp)


def bfs(a):
    result.append(a)
    queue = deque()
    queue.append(a)
    temp = a
    while queue:
        for i in M2[:]:
            if temp in i:
                if temp != i[0]:
                    queue.append(i[0])
                    result.append(i[0])
                    M2.remove(i)
                else:
                    queue.append(i[1])
                    result.append(i[1])
                    M2.remove(i)
        temp = queue.popleft()


M = list()
for _ in range(m):
    M.append(list(map(int, input().split())))
M.sort()
M1 = list(M)
M2 = list(M)

#dfs
result = list()
dfs(v)
answer = ""
for i in result:
    if str(i) not in answer:
        answer += str(i) + " "
print(answer.strip())

#bfs
result = list()
bfs(v)
answer = ""
for i in result:
    if str(i) not in answer:
        answer += str(i) + " "
print(answer.strip())
"""
