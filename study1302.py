# 1302 베스트셀러 https://www.acmicpc.net/problem/1302

N = int(input())
dic = {}
for i in range(N):
    a = input()
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

max = 0
answer = []
for i in dic:
    if max < dic[i]:
        max = dic[i]
for i in dic:
    if max == dic[i]:
        answer.append(i)
answer.sort()
print(answer[0])


