# 1120 문자열 https://www.acmicpc.net/problem/1120

A, B = input().split(" ")
result = 51
gap = len(B) - len(A)
for i in range(gap+1):
    min = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            min += 1

    if result > min:
        result = min
print(result)
