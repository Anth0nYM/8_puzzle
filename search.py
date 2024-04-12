import collections
import state
import numpy as np


def bfs(initial_state, goal_state):
    queue = collections.deque([(initial_state, [])])
    visited = set()
    visited.add(state.to_tuple(initial_state))

    while queue:
        node, path = queue.popleft()
        if np.array_equal(node, goal_state):
            return path + [node]
        for child in state.generate_children(node):
            child_tuple = state.to_tuple(child)
            if child_tuple not in visited:
                queue.append((child, path + [node]))
                visited.add(child_tuple)

    return None


def dfs(initial_state, goal_state):
    stack = collections.deque([(initial_state, [])])
    visited = set()
    visited.add(state.to_tuple(initial_state))

    while stack:
        node, path = stack.pop()
        if np.array_equal(node, goal_state):
            return path + [node]
        for child in state.generate_children(node):
            child_tuple = state.to_tuple(child)
            if child_tuple not in visited:
                stack.append((child, path + [node]))
                visited.add(child_tuple)

    return None


initial_state = state.generate_mock_state(1)
goal_state = state.generate_solved_state(2)
print(initial_state)
#state.display(initial_state)
path_bfs = bfs(initial_state, goal_state)
#path_dfs = dfs(initial_state, goal_state)
# print(len(path_bfs))
for st in path_bfs:
    state.display(st)
