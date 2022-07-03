# 색종이만들기(2630) https://www.acmicpc.net/problem/2630
# DC(분할정복), recursion

import sys

input = sys.stdin.readline
n = int(input())
blue = 0
white = 0
confetti = list()
for _ in range(n):
    confetti.append(list(map(int, input().split())))


def check(row, col, n):
    global blue, white

    curr = confetti[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if curr != confetti[i][j]:
                next_n = n // 2
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                return
    if curr == 0:
        white += 1
    else:
        blue += 1
    return


check(0, 0, n)
print(white)
print(blue)
