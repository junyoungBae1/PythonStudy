# IOIOI 5525 https://www.acmicpc.net/problem/5525

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

answer, i, count = 0, 0, 0

while (m - 1) > i:
    if s[i:i + 3] == "IOI":
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
