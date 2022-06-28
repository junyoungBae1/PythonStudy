# 11728 배열 합치기 https://www.acmicpc.net/problem/11728

N, M = map(int, input().split())

A = list([int(x) for x in input().split()])
B = list([int(x) for x in input().split()])


C = sorted(A+B)
result = ""
for i in C:
    result += str(i) + " "

print(result.strip())