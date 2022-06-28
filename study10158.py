# 10158 개미 https://www.acmicpc.net/problem/10158

import sys


def f(w, x):
    return w - abs(w - x)


w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())

t = int(input())

x = (p + t) % (2 * w) #
x = f(w, x)
y = (q + t) % (2 * h) #
y = f(h, y)

print(x, y)

""" 
시간초과

x, y = 1, 1
for _ in range(T):
    if (p == w and x > 0) or (p == 0 and x < 0):
        x = -x
    if (q == h and y > 0) or (q == 0 and y < 0):
        y = -y
    p += x
    q += y

print(p, q)
"""
