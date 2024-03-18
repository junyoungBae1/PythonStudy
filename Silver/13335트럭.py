# 13335 트럭


import sys

input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w  # 다리의 길이만큼 0으로 초기화된 리스트
time = 0
current_weight = 0  # 현재 다리 위의 총 무게

while trucks or current_weight > 0:  # 대기 중인 트럭이 있거나 다리 위에 트럭이 있는 동안
    time += 1
    out = bridge.pop(0)  # 다리를 건너는 트럭을 하나씩 이동
    current_weight -= out  # 다리를 떠난 트럭의 무게를 빼줌

    if trucks:  # 대기 중인 트럭이 있는 경우
        if current_weight + trucks[0] <= L:  # 새 트럭이 다리에 올라갈 수 있는 경우
            truck = trucks.pop(0)
            bridge.append(truck)  # 다리에 트럭 추가
            current_weight += truck
        else:
            bridge.append(0)  # 트럭이 다리에 진입할 수 없는 경우, 0을 추가하여 시간 경과 표시

print(time)

# n, w, L = map(int, input().split())  # 트럭의 수, 다리의 길이, 다리의 하중
#
# truck = list(map(int, input().split()))
# bridge = list()
#
# time = 0
# weight = 0
#
# x = truck.pop(0)
# bridge.append(x)
# weight += x
# time += 1
# while len(truck) != 0:
#     if weight + truck[0] > L:
#         time += w
#         temp = bridge.pop(0)
#         weight -= temp
#         y = truck.pop(0)
#         bridge.append(y)
#         weight += y
#
#     elif weight + truck[0] <= L:
#         y = truck.pop(0)
#         bridge.append(y)
#         weight += y
#         time += 1
#
# time += w
# print(time)