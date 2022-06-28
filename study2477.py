# 2477 참외밭 https://www.acmicpc.net/problem/2477
# hint : 가장 큰 변의 인덱스(가로)에서 양쪽 i-1 i+1의 값을 뺴면 작은 사각형의 세로값 도출이 가능하다.
K = int(input())

d = [list(map(int, input().split(" "))) for _ in range(6)]
# 큰사각형 넓이 구하기
w, h = 0, 0
for i in d:
    if i[0] == 1 or i[0] == 2:  # 가로
        if w < abs(i[1]):
            w = abs(i[1])
    elif i[0] == 3 or i[0] == 4:
        if h < abs(i[1]):
            h = abs(i[1])
bigR = w * h
# 작은사각형 넓이 구하기
x, y = 0, 0
for i in range(6):
    if w == d[i][1]:
        if i == 0:
            y = abs(d[5][1] - d[i+1][1])
        elif i == 5:
            y = abs(d[i - 1][1] - d[0][1])
        else:
            y = abs(d[i-1][1] - d[i+1][1])
    if h == d[i][1]:
        if i == 0:
            x = abs(d[5][1] - d[i + 1][1])
        elif i == 5:
            x = abs(d[i - 1][1] - d[0][1])
        else:
            x = abs(d[i - 1][1] - d[i + 1][1])

smallR = x * y
print((bigR - smallR) * K)
