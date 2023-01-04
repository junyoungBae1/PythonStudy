# 11727 2xn 타일링 2 https://www.acmicpc.net/problem/11727

n = int(input())

s = [0,1,3]
if n < 3:
    print(s[n])
else:
    for i in range(3,n+1):
        s.append(s[i-2]*2 + s[i-1])
    print(s[n] % 10007)



