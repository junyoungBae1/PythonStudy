# 백준 1526번  https://www.acmicpc.net/problem/1526 가장 큰 금민수
N = int(input())
while True:
    flag = 0
    for i in str(N):
        if i != "4" and i != "7":
            N -= 1
            flag = 1

    if flag == 0:
        print(N)
        break
