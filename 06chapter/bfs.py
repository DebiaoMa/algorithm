from collections import deque


def bfs(graph, begin):
    search_queue = deque()
    search_queue += graph[begin]
    searched = []

    while search_queue:
        point = search_queue.popleft()

        if not point in searched:
            if point == 4:
                print('4 has been reached!')
            else:
                search_queue += graph[point]
                searched.append(point)


if __name__ == '__main__':
    graph = {}
    graph[1] = [2, 3]
    graph[2] = [4]
    graph[3] = [4]

    bfs(graph, 1)

