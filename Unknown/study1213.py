# 1213 팰린드롬 만들기 https://www.acmicpc.net/problem/1213
# hint : 홀수개인 알파벳이 1개 이하여야 함

name = list(input())
name.sort()
dic = dict()
for i in name:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
result = list(range(len(name)))
nlen = len(name)
odd = 0
even = 0
for d in dic:
    if dic[d] % 2 == 0:
        even += 1
    else:
        odd += 1
cnt = 0
if odd > 1 or (nlen == 2 and len(dic) > 1):
    print("I'm Sorry Hansoo")
else:
    for i in dic:
        while dic[i] != 0:
            if dic[i] % 2 == 1:
                result[int(nlen / 2)] = i
                dic[i] -= 1
                cnt -= 1
            else:
                result[cnt] = i
                result[nlen - cnt - 1] = i
                dic[i] -= 2
            cnt += 1
    print(''.join(result))
