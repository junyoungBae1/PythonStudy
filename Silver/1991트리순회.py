# # 1991 트리순회
#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
#
# graph = []
# for i in range(n):
#     temp = list(map(str, input().split()))
#     graph.append(temp)
# result = []
#
# def preorder(r):
#     for i in range(len(graph)):
#         if graph[i][0] == r:
#             result.append(r)
#             if graph[i][1] != '.':
#                 preorder(graph[i][1])
#             if graph[i][2] != '.':
#                 preorder(graph[i][2])
#     return
#
#
# def inorder(r):
#     for i in range(len(graph)):
#         if graph[i][0] == r:
#             if graph[i][1] != '.':
#                 inorder(graph[i][1])
#                 result.append(r)
#             if graph[i][2] != '.':
#                 if not r in result:
#                     result.append(r)
#                 inorder(graph[i][2])
#
#             if graph[i][1] == '.' and graph[i][2] == '.':
#                 result.append(r)
#     return
#
#
# def postorder(r):
#     for i in range(len(graph)):
#         if graph[i][0] == r:
#             if graph[i][1] == '.' and graph[i][2] == '.':
#                 result.append(r)
#
#             if graph[i][1] != '.' and graph[i][2] != '.':
#                 postorder(graph[i][1])
#                 postorder(graph[i][2])
#                 result.append(r)
#
#             elif graph[i][1] != '.':
#                 postorder(graph[i][1])
#                 result.append(r)
#
#             elif graph[i][2] != '.':
#                 postorder(graph[i][2])
#                 result.append(r)
#
#
#     return
#
#
# preorder("A")
# for i in result:
#     print(i, end='')
# result = []
# print()
#
# inorder("A")
# for i in result:
#     print(i, end='')
# result = []
# print()
#
# postorder("A")
# for i in result:
#     print(i, end='')
#

def preorder(node):
    if node == '.':
        return ''
    return node + preorder(graph[node][0]) + preorder(graph[node][1])

def inorder(node):
    if node == '.':
        return ''
    return inorder(graph[node][0]) + node + inorder(graph[node][1])

def postorder(node):
    if node == '.':
        return ''
    return postorder(graph[node][0]) + postorder(graph[node][1]) + node

n = int(input())
graph = {}
for _ in range(n):
    node, left, right = input().split()
    graph[node] = (left, right)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))

