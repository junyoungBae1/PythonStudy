# 백준 2999번 비밀이메일 https://www.acmicpc.net/problem/2999

email = input()

length = len(email)
string = ""
R = 0
C = 0
for i in range(1, length + 1):
    for j in range(1, length + 1):
        if i * j == length and i <= j:
            R = i
            C = j
            break

elist = [[0] * C for i in range(R)]
cnt = 0
for i in range(C):
    for j in range(R):
        elist[j][i] = email[cnt]
        cnt += 1

for i in elist:
    string += "".join(i)

print(string)
