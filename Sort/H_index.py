# programmers H-index

citations = [0,0,1]


def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    h = citations[len(citations) // 2]
    # 0 1 3 5 6
    # print(citations)

    flag = 0
    while 0 <= h < citations[0]:
        less = 0
        more = 0
        for i in range(len(citations)):

            if h >= citations[i]:
                less += 1
            if h <= citations[i]:
                more += 1
        if more >= h >= less:
            answer = max(answer, h)
            h += 1
            flag = 1
        elif more < h or h < less:
            h -= 1
            if flag == 1:
                return answer
        else:
            h += 1
    return answer

print(solution(citations))
