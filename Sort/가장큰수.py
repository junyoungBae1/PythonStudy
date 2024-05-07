#programmers 가장큰수



numbers = [12,121]
def solution(numbers):
    str_number = list(map(str,numbers))
    str_number.sort(key=lambda x: x*3,reverse=True)

    # for i in range(len(str_number)):
    #     if len(str_number[i]) == 1:
    #         for j in range(len(str_number)):
    #             if str_number[i][0] == str_number[j][0]:
    #                 for k in range(1,len(str_number[j])):
    #                     if str_number[i][0] < str_number[j][k]:
    #                         break
    #                     elif str_number[i][0] < str_number[j][k]:
    #                         continue
    #                     elif str_number[i][0] > str_number[j][k]:
    #                         temp = str_number[i]
    #                         str_number[i] = str_number[j]
    #                         str_number[j] = temp
    #                         break

    answer = ''.join(str_number)
    return '0' if answer[0] == '0' else answer


print(solution(numbers))