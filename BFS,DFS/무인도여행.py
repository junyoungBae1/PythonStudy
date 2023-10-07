#프로그래머스 무인도여행

from collections import deque

n = 4
maps = list()

for i in range(n):
    maps.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def bfs(n, m, maps, visited, i, j):
    q = deque()
    cnt = int(maps[i][j])
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if maps[nx][ny] == 'X':
                        cnt += 0
                    else:
                        cnt += int(maps[nx][ny])
                        q.append((nx, ny))
    return cnt


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = list()
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and maps[i][j] != 'X':
                answer.append(bfs(n, m, maps, visited, i, j))

    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return sorted(answer)


print(solution(maps))
