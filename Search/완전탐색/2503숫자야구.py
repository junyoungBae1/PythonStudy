# 2503 숫자야구


import sys

input = sys.stdin.readline

n = int(input())


all_list = []

for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            all_list.append(str(i) + str(j) + str(k))

for i in range(n):
    question_number, strike, ball = map(int, input().split())
    question_number = list(str(question_number))
    for j in all_list[:]:
        s = 0
        b = 0
        for k in range(3):
            if question_number[k] == j[k]:
                s += 1
            elif question_number[k] in j:
                b += 1
        if s != strike or b != ball:
            all_list.remove(j)

print(len(all_list))
