# 종이의개수(1780) https://www.acmicpc.net/problem/1780
# DC, recursion
import sys

input = sys.stdin.readline
n = int(input())
paper = list()
minus = 0
zero = 0
one = 0
for _ in range(n):
    paper.append(list(map(int, input().split())))


def check(row, col, n):
    global minus, zero, one
    curr = paper[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if curr != paper[i][j]:
                next_n = n // 3
                next__n = (2 * n) // 3
                check(row, col, next_n)
                check(row + next_n, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col + next_n, next_n)
                check(row + next__n, col, next_n)
                check(row, col + next__n, next_n)
                check(row + next__n, col + next_n, next_n)
                check(row + next_n, col + next__n, next_n)
                check(row + next__n, col + next__n, next_n)
                return
    if curr == -1:
        minus += 1
    elif curr == 0:
        zero += 1
    else:
        one += 1
    return


check(0, 0, n)
print(minus)
print(zero)
print(one)
