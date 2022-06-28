# 9375 패션왕 신해빈 https://www.acmicpc.net/problem/9375

T = int(input())

for i in range(T):
    dic = dict()
    flag = 0
    result = 0
    N = int(input())
    for j in range(N):
        name, purpose = input().split()
        if purpose not in dic:
            dic[purpose] = 1
        else:
            dic[purpose] += 1
    for key in dic:
        if result == 0:
            result = 1

        result *= (dic[key]+1)

    if N == 0:
        print(0)
    else:
        print(result-1)
