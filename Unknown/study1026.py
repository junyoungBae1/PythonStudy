# 1026 보물 https://www.acmicpc.net/problem/1026

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

A.sort(reverse=True)
B.sort()

sum = 0
for i in range(N):
    sum += int(A[i])*int(B[i])

print(sum)