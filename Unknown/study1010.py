# 1010 다리놓기 https://www.acmicpc.net/problem/1010

T = int(input())


l = []
r = []
for i in range(T):
    temp = input().split(" ")
    l.append(int(temp[0]))
    r.append(int(temp[1]))

for i in range(T):
    m = 1
    n = 1
    k = 1
    if r[i] == 1 or r[i] == l[i]:
        print(1)
    else:
        for j in range(1, r[i] + 1):
            m *= j
        for j in range(1, r[i] - l[i] + 1):
            n *= j
        for j in range(1, l[i] + 1):
            k *= j
        print(int(m / (n * k)))
