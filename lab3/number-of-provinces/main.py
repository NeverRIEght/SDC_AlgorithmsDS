from collections import deque


# def bfs(first_elem):
#     q = deque()
#     q.append(first_elem)
#
#     while q:
#         current_poll = q.popleft()
#         print(current_poll)
#         for item in current_poll:
#             q.append(item)

# def dfs(first_elem):
#     q = deque()
#     q.append(first_elem)
#
#     while q:
#         current_poll = q.pop()
#         print(current_poll)
#         for item in current_poll:
#             q.append(item)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        circles_count = len(isConnected)
        visited = set()

        connected_components = 0

        for i in range(circles_count):
            q = deque()
            if i not in visited:
                visited.add(i)
                q.append(i)
                connected_components += 1
            while q:
                current_node = q.popleft()
                for neighbour in range(circles_count):
                    if neighbour not in visited and neighbour != current_node:
                        if isConnected[current_node][neighbour] == 1:
                            visited.add(neighbour)
                            q.append(neighbour)

        return connected_components