# 1992 쿼드트리

import sys

input = sys.stdin.readline

N = int(input())
qt = list()
for i in range(N):
    str1 = str(input()).rstrip()
    qt.append(list(str1))

result = list()


def Division(arr):
    n = len(arr)
    if '1' not in (s_num for row in arr for s_num in row):
        result.append(0)
        return 0
    elif '0' not in (s_num for row in arr for s_num in row):
        result.append(1)
        return 0
    elif len(qt) == 1:
        result.append(int(arr[0]))
        return 0
    else:
        result.append("(")
        qt1 = [row[0:n//2] for row in arr[0:n//2]]
        qt2 = [row[n // 2:n] for row in arr[0:n // 2]]
        qt3 = [row[0:(n // 2)] for row in arr[n // 2:n]]
        qt4 = [row[n // 2:n] for row in arr[n // 2:n]]
        Division(qt1)
        Division(qt2)
        Division(qt3)
        Division(qt4)
        result.append(")")
        return 0


Division(qt)

for i in range(len(result)):
    print(result[i], end="")
