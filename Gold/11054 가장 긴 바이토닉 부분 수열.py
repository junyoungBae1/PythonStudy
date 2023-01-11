# 11054 가장 긴 바이토닉 부분 수열 https://www.acmicpc.net/problem/11054

import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int,input().split()))

increase = [1] * n
decrease = [1] * n

for i in range(n):
    for j in range(i):
        if P[i] > P[j] and increase[i] < increase[j]+1:
            increase[i] = increase[j]+1

P.reverse()
for i in range(n):
    for j in range(i):
        if P[i] > P[j] and decrease[i] < decrease[j]+1:
            decrease[i] = decrease[j]+1
decrease.reverse()

result =0
for i in range(n):
    result = max(result,increase[i]+decrease[i]-1)

print(result)