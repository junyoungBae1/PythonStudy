# 1541 잃어버린 괄호 https://www.acmicpc.net/problem/1541

n = input()

p = n.split("-")

for i, d in enumerate(p):
    if "+" in d:
        temp = d.split("+")
        p[i] = 0
        for x in temp:
            p[i] += int(x)
    else:
        p[i] = int(d)

result = 0
for i, d in enumerate(p):
    if i == 0:
        result += d
    else:
        result -= d

print(result)
