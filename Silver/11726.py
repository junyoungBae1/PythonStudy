# 11726 2xn 타일링 https://www.acmicpc.net/problem/11726

N = int(input())

d = [1 for x in range(1, N+2)]
for i in range(2, N+1):
    d[i] = d[i-1]+d[i-2]

result = d[N] % 10007
print(result)
