# # def is_queue_full() -> bool:
# #     global SIZE, rear
# #     if rear == SIZE-1:
# #         return True
# #     else:
# #         return False
#
#
# def is_queue_full() -> bool:
#     global SIZE, rear, front
#     if rear != SIZE-1:
#         return False
#     elif rear == SIZE-1 and front == -1:
#         return True
#     else:
#         for i in range(front+1, SIZE):
#             queue[i-1] = queue[i]
#             queue[i] = None
#         front = front - 1
#         rear = rear - 1
#         return False
#
#
# def is_queue_empty() -> bool:
#     global SIZE, front, rear
#     if front == rear:
#         return True
#     else:
#         return False
#
#
# def en_queue(data):
#     global rear
#     if is_queue_full():
#         print("큐가 꽉 찼습니다")
#         return None
#     rear = rear + 1
#     queue[rear] = data
#
#
# def de_queue():
#     global front
#     if is_queue_empty():
#         print("큐가 비어있습니다")
#         return None
#     front += 1
#     data = queue[front]
#     queue[front] = None
#     return data
#
#
# def peek():
#     global front
#     if is_queue_empty():
#         print("큐가 비어있습니다")
#         return None
#     return queue[front+1]
#
#
# SIZE = int(input("큐 사이즈 입력 : "))
# queue = [None for _ in range(SIZE)]
# front = -1
# rear = -1
#
# if __name__ == "__main__":
#     while True:
#         menu = input("삽입(i), 추출(e), 확인(v), 종료(x) : ")
#         if menu == 'x' or menu == 'X':
#             print("프로그램을 종료합니다")
#             break
#         elif menu == 'i' or menu == 'I':
#             en_queue(input("입력할 데이터 : "))
#             print(queue)
#         elif menu == 'e' or menu == 'E':
#             print(f"추출된 데이터 {de_queue()}")
#             print(queue)
#         elif menu == 'v' or menu == 'V':
#             print(f"확인된 데이터 {peek()}")
#             print(queue)
#         else:
#             print(f"{menu} 메뉴는 존재하지 않습니다. 메뉴의 기능을 이용해 주세요")
#
# class Graph:
#     def __init__(self, size):
#         self.SIZE = size
#         self.graph = [[0 for _ in range(size)] for _ in range(size)]
#
#     def print_graph(self, n):
#         for r in range(n):
#             for c in range(n):
#                 print(self.graph[r][c], end=' ')
#             print()
#
#
# G1 = Graph(4)
# G3 = Graph(4)
# G_self = Graph(4)
#
# # 0 == A, 1 == B, 2 == C, 3 == D
# G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
# G1.graph[1][0] = 1; G1.graph[1][2] = 1
# G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
# G1.graph[3][0] = 1; G1.graph[3][2] = 1
#
# print("G1 무방향 그래프")
#
# G1.print_graph(G1.SIZE)
#
#
# # 0 == A, 1 == B, 2 == C, 3 == D
# G3.graph[0][1] = 1; G3.graph[0][2] = 1
# G3.graph[3][0] = 1; G3.graph[3][2] = 1
#
# print("G3 방향 그래프")
#
# G3.print_graph(G3.SIZE)
#
# # 0 == A, 1 == B, 2 == C, 3 == D
# G_self.graph[0][3] = 1
# G_self.graph[1][2] = 1; G_self.graph[1][3] = 1
# G_self.graph[2][1] = 1
# G_self.graph[3][0] = 1; G_self.graph[3][1] = 1
#
# print("G_self 무방향 그래프")
# for r in range(G_self.SIZE):
#     for c in range(G_self.SIZE):
#         print(G_self.graph[r][c], end=' ')
#     print()


graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A') + i), end = ' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, i, visited):
    pass
# 크루스칼 알고리즘

visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 7, visited_dfs)
print()
bfs(graph, 4, visited_bfs)








