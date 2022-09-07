import collections

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


# iterative depth first search for graph

def dfs(graphs, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)

        for neighbour in graphs[current]:
            stack.append(neighbour)


# Recursive deph first search for graphs


def dfs(graphs, source):
    print(source)
    for neighbour in graphs[source]:
        dfs(graphs, neighbour)


# Breadth first approach for graphs

q = collections.deque()


def bfs(graphs, source):
    q.append(source)
    while q:
        current = q.popleft()
        print(current)
        for neighbour in graphs[current]:
            q.appendleft(neighbour)


print(bfs(graph, 'a'))
