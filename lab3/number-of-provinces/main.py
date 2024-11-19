from collections import deque


def bfs(first_elem):
    q = deque()
    q.append(first_elem)

    while q:
        current_poll = q.popleft()
        print(current_poll)
        for item in current_poll:
            q.append(item)
        else:
            pass

def dfs(first_elem):
    q = deque()
    q.append(first_elem)

    while q:
        current_poll = q.pop()
        print(current_poll)
        for item in current_poll:
            q.append(item)
        else:
            pass


def main():
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    n = len(is_connected)
    visited = set()

    connected_components = 0

    for i in range(n):
        q = deque()
        if i not in visited:
            visited.add(i)
            q.append(i)
            connected_components += 1
        while q:
            current_node = q.popleft()
            for adj in range(n):
                if adj not in visited:
                    if adj != current_node:
                        if is_connected[current_node][adj] == 1:
                            visited.add(adj)
                            q.append(adj)

    print(connected_components)

main()