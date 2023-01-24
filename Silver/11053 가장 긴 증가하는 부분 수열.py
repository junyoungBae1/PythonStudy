#11053 가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053
#dp

n = int(input())

P = list(map(int,input().split()))

cnt = 0
increase = [1] * n
for i in range(n):
    for j in range(i):
        if P[i] > P[j] and increase[i] < increase[j]+1:
            increase[i] = increase[j]+1

print(max(increase))
