# 백준 2851번 https://www.acmicpc.net/problem/2851 슈퍼마리오
mushroom = []
mario = 0
for i in range(10):
    mushroom.append(int(input()))

for i, d in enumerate(mushroom):
    if mario + d >= 100:
        if 100 - mario < mario + d - 100:
            print(mario)
            break
        else:
            print(mario + d)
            break
    else:
        mario += d
    if i == 9:
        print(mario)


