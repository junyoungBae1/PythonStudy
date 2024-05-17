import heapq

jobs = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    jobs = sorted(jobs)

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))


print(solution(jobs))
