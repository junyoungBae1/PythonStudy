# 17144 미세먼지 안녕! https://www.acmicpc.net/problem/17144

from collections import deque
import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

house = []
for i in range(r):
    tmp = list(map(int, input().split()))
    house.append(tmp)
up = 0
down = 0
# 공기청정기 위치 찾기
for i in range(r):
    if house[i][0] == -1:
        up = i
        down = i + 1
        break


# 미세먼지 확산시키기
def spread():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if house[i][j] != 0 and house[i][j] != -1:
                temp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and house[nx][ny] != -1:
                        tmp_arr[nx][ny] += house[i][j] // 5
                        temp += house[i][j] // 5
                house[i][j] -= temp
    for i in range(r):
        for j in range(c):
            house[i][j] += tmp_arr[i][j]

# 공기청정기 위쪽으로 이동
def air_clear_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = up, 1
    direct = 0
    before = 0
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        house[x][y], before = before, house[x][y]
        x = nx
        y = ny


# 공기청정기 아래쪽으로 이동
def air_clear_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = down, 1
    direct = 0
    before = 0
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        house[x][y], before = before, house[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_clear_up()
    air_clear_down()
result = 0
for i in range(r):
    for j in range(c):
        if house[i][j] > 0:
            result += house[i][j]
print(result)
