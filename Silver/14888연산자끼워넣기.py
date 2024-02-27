# 14888 연산자 끼워넣기
# +-*%
import itertools
import sys
from itertools import product

per = product

input = sys.stdin.readline
result = []
n = int(input())
number = list(map(int, input().split()))
op1 = ["+", "-", "*", "%"]
op2 = list(map(int, input().split()))
op = []
for i in range(len(op2)):
    if op2[i] == 0:
        continue
    else:
        for j in range(op2[i]):
            op.append(op1[i])
perop = list(itertools.permutations(op, n - 1))
for i in range(len(perop)):
    total = number[0]
    for j in range(n - 1):
        if perop[i][j] == "+":
            total = total + number[j + 1]
        elif perop[i][j] == "-":
            total = total - number[j + 1]
        elif perop[i][j] == "*":
            total = total * number[j + 1]
        elif perop[i][j] == "%":
            if total >= 0:
                total = total // number[j + 1]
            elif total < 0:
                total = -(-total // number[j + 1])
    result.append(total)

print(max(result))
print(min(result))
