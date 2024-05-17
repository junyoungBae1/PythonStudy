import heapq
import sys

input_str = input()
list_part, num_part = input_str.split("],")

scoville = list(map(int, list_part.strip("[").split(",")))
K = int(num_part)

heapq.heapify(scoville)


def solution(scoville, K):
    answer = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            new_s = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
            heapq.heappush(scoville,new_s)
            answer += 1
        elif scoville:
            return -1
    return answer
#
# import heapq
#
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)
#
#     while True:
#         minimum = heapq.heappop(scoville)
#         if minimum >= K:
#             break
#         if len(scoville) < 1:
#             return -1
#         secminimum = heapq.heappop(scoville)
#         heapq.heappush(scoville, minimum + (secminimum * 2))
#         answer += 1
#
#     return answer
print(solution(scoville, K))
