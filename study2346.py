# 2346 풍선터뜨리기 https://www.acmicpc.net/problem/2346
N = int(input())

note = [int(x) for x in input().split(" ")]
move = 0
balloon = list(range(1, N + 1))
result = list()

temp = note.pop(move)
result.append(balloon.pop(move))

while note:
    if temp < 0:
        move = (move + temp) % len(note)
    else:
        move = (move + temp - 1) % len(note)
    temp = note.pop(move)
    result.append(balloon.pop(move))
for i in result:
    print(i, end=' ')
