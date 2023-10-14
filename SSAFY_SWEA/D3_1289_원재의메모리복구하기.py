# 1289

T = int(input())

for tc in range(1, T + 1):
    result = 0

    memory = str(input())
    flag = 0
    for i in range(len(memory)):
        if int(memory[i]) != flag:
            if flag == 0:
                flag = 1
            elif flag == 1:
                flag = 0
            result += 1

    print("#{} {}".format(tc, result))
