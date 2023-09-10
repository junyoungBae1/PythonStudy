# 11053 가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053
# dp


n = int(input())
seq = list(map(int, input().split()))

cnt = 0
inc = [1] * n
for i in range(n):
    for j in range(n):
        if seq[i] > seq[j] and inc[i] < inc[j]+1:
            inc[i] = inc[j]+1

print(max(inc))
