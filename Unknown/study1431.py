# 1431 시리얼 번호 https://www.acmicpc.net/problem/1431
# sort()함수 lambda에 대해서 배움

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
    return result

n = int(input())

arr = []
for i in range(n):
    arr.append(input())
arr.sort(key=lambda x: (len(x), sum_num(x), x))

for i in arr:
    print(i)


"""
맞게 한거 같은데 오류뜸..
N = int(input())

lst = list(input() for _ in range(N))
lst.sort() #사전식으로 분류

for i in range(N): # 길이별로 분류
    for j in range(i+1, N):
        if len(lst[i]) > len(lst[j]):
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp

for i in range(N): #같은 길이에서 숫자의 합으로 분류
    for j in range(i+1, N):
        if len(lst[i]) == len(lst[j]):
            temp = 0
            temp2 = 0
            for k in lst[i]:
                try:
                    temp += int(k)
                except:
                    temp += 0
            for k in lst[j]:
                try:
                    temp2 += int(k)
                except:
                    temp2 += 0
            if temp2 < temp:
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp

for i in lst:
    print(i)
"""
