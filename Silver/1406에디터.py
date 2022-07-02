# 에디터(1406) https://www.acmicpc.net/problem/1406
# 자료구조
# insert와 remove는 O(n)만큼 시간을 소요
# st2의 st2.reverse()를 할 경우 아무것도 없을때 Type error가 뜬다.

import sys
input = sys.stdin.readline

st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
    command = list(input().split())

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))



# 내 풀이는 시간 초과가 떴다.
import sys

input = sys.stdin.readline
from collections import deque


def move(string, cursor):
    while queue:
        t = queue.popleft()  # t = list형식
        if len(t) == 1:
            t = t[0]
            if t == 'L':
                cursor -= 1
            elif t == 'D':
                cursor += 1
            elif t == 'B':
                if 1 <= cursor <= len(string):
                    string[cursor-1] = 0
                    string.remove(0)
                    cursor -= 1
            if cursor < 0:
                cursor = 0
            elif cursor > len(string):
                cursor = len(string)
        else:
            string.append(" ")
            string.insert(cursor, t[1])
            cursor += 1
    print("".join(string))


string = list(input().strip())
n = int(input())
queue = deque()
for _ in range(n):
    queue.append(input().split())
cursor = len(string)
move(string, cursor)
