import heapq

op = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

def solution(operations):
    answer = []
    heap = []
    for i in operations:
        command,num = i.split(" ")
        if command == "I":
            heapq.heappush(heap,int(num))
        elif command == "D":
            if int(num) == -1:
                if heap:
                    heapq.heappop(heap)
                else:
                    continue
            elif int(num) == 1:
                if heap:
                    heap.remove(max(heap))
                    heapq.heapify(heap)
                else:
                    continue
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer



print(solution(op))