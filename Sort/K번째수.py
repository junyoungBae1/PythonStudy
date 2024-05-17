#programmers K번째수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        a,b,c = commands[i]
        q = array[a-1:b]
        q.sort()
        print(q)
        answer.append(q[c-1])

    return answer

print(solution(array,commands))