# PASSED
def foo(triangle, depth, idx):
    global visited

    if (depth, idx) in visited:
        return triangle[depth][idx]

    if depth == len(triangle) - 1:
        return triangle[depth][idx]

    visited.add((depth, idx))
    triangle[depth][idx] += max(foo(triangle, depth+1, idx), foo(triangle, depth+1, idx+1))
    return triangle[depth][idx]


def solution(triangle):
    global visited
    visited = set()
    return foo(triangle, 0, 0)