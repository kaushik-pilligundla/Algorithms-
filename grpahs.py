graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

res = []


# iterative depth first search

def dfs(graphs, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        for neighbour in graphs[current]:
            stack.append(neighbour)

# recursive depth first search of the graph


def dfs(graphs, source):
    print(source)
    for neighbour in graphs[source]:
        dfs(graphs, neighbour)


print(dfs(graph, 'a'))
