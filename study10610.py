# 백준 10610 30 https://www.acmicpc.net/problem/10610

N = list(input())
sum = 0
if '0' not in N:
    print(-1)
else:
    for i in N:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        N.sort(reverse=True)
        print(''.join(N))

