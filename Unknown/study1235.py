# 1235 학생 번호 https://www.acmicpc.net/problem/1235

N = int(input())
num = []
for i in range(N):
    num.append(input())

numlen = len(num[0])
temp = []
result = 1

for i in range(numlen - 1, -1, -1):
    cnt = 0
    for j in range(N):
        temp.append(int(num[j][i:numlen]))

    for j in range(N):
        if cnt < temp.count(temp[j]):
            cnt = temp.count(temp[j])

    if cnt == 1:
        print(result)
        break
    else:
        result += 1
    temp.clear()
