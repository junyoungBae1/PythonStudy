# 1927 최소힙 https://www.acmicpc.net/problem/1927
# 자료구조, 우선순위 큐  힙구현하기
# heapq 쓰기

import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    t = int(input())
    if t != 0:
        heapq.heappush(heap, t)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)




""" 파이썬으로 힙 구현 삽입O(n) 삭제O(log2 N)

import sys

input = sys.stdin.readline

n = int(input())
heap = [0]


def push():
    i = len(heap)-1
    parent = i // 2
    leftchild = parent * 2
    rightchild = parent * 2 + 1

    while parent > 0:
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]  # swap
        i = i // 2
        parent = parent // 2


def arrange(r):
    parent = r
    leftchild = r * 2
    rightchild = (r * 2) + 1

    if leftchild <= len(heap)-1 and heap[leftchild] < heap[parent]:
        parent = leftchild
    if rightchild <= len(heap)-1 and heap[rightchild] < heap[parent]:
        parent = rightchild
    if parent != r:
        heap[r],  heap[parent] = heap[parent], heap[r]
        arrange(parent)



for _ in range(n):
    t = int(input())
    if len(heap) == 1:
        if t == 0:
            print(heap[0])
        else:
            heap.append(t)
    else:
        if t == 0:
            i = len(heap) - 1
            heap[1], heap[i] = heap[i], heap[1]
            print(heap.pop())
            arrange(1)
        else:
            heap.append(t)
            push()
"""

"""
# 시간복잡도 삭제 O(N)
n = int(input())
arr = list()
for _ in range(n):
    t = int(input())
    if t == 0:
        if len(arr) == 0:
            print("0")
        else:
            arr.sort(reverse = True)
            print(arr.pop())
    elif t > 0:
        arr.append(t)
"""
