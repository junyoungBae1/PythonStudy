# 수들의합(1789) https://www.acmicpc.net/problem/1789

S = int(input())
cnt = 0
sum = 0
while 1:
    cnt += 1
    sum += cnt
    if S < sum:
        cnt -= 1
        break

print(cnt)