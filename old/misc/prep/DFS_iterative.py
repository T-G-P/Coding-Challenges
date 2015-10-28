graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}


def dfs(graph, start):
    # create set of all visited verticies starting with start
    visited = set()
    # use stack to add all connected nodes at each iteration
    stack = [start]
    while stack:
        # Get vertex from stack which will be used to visit connected verticies
        vertex = stack.pop()
        # If vertex hasn't been seen, add it to visited set
        # Add all adjacent vertices besides the recently visited one to the stack
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

visited = dfs(graph, 'A')
print(visited)

"""
stack: 'A'
visitied: {}

stack: 'B', 'C'
visited: {A}

stack: 'B, 'F'
visited: {A, C}

stack: 'B, 'E'
visited: {A, C, F}

stack: 'B, 'B'
visited: {A, C, E, F}

stack: 'B'
visited: {A, B, C, E, F}

stack: ''
visited: {A, B, C, D, E, F}

def dfs(graph, start):
    visited = {}
    stack = [start]
    while stack:
        v = stack.pop()
        visited.add(v)
        stack.extend(graph[v] - visited)
    return visited
"""
