# 1316 그룹단어체커


n = int(input())
cnt = 0
for i in range(n):
    word = input()
    temp = []
    cnt += 1
    for j in range(len(word)):
        if word[j] not in temp:
            temp.append(word[j])
        elif word[j] in temp:
            if word[j] == word[j - 1]:
                temp.append(word[j])
            else:
                cnt -= 1
                break

print(cnt)
