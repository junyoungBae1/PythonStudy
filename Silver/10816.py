# 10816 숫자 카드 2  https://www.acmicpc.net/problem/10816
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

import sys

N = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))
dic = dict()
for key in arr1:
    if key not in dic:
        dic[key] = 1
    else:
        dic[key] += 1

result = list()
for i, key in enumerate(arr2):
    if key in dic:
        result.append(dic[key])
    else:
        result.append(0)
answer = ""
for i in result:
    answer += str(i) + " "
print(answer.rstrip())
