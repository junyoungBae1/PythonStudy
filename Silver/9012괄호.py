# 9012 https://www.acmicpc.net/problem/9012
#

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    cnt = 0
    vps = input()
    if vps[0] != '(' and vps[len(vps)-1] != ')':
        print("NO")
        continue
    for j in vps:
        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            continue

    if cnt == 0:
        print('YES')
    elif cnt != 0:
        print('NO')
