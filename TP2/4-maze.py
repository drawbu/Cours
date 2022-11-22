from pprint import pprint

Grid = list[list[int]]
Point = tuple[int, int]

solutions = []


def maze(grid: Grid, n: int, start: Point = None, moves: list = None):
    global solutions
    if moves is None:
        moves = []
    if start is None:
        start = (0, 0)
        solutions = []

    if start == (n - 1, n - 1):
        solutions.append(moves)
        return solutions

    if start[0] + 1 < n:
        next_point: Point = (start[0] + 1, start[1])
        if grid[next_point[0]][next_point[1]] == 1:
            maze(grid, n, next_point, moves + [next_point])

    if start[1] + 1 < n:
        next_point: Point = (start[0], start[1] + 1)
        if grid[next_point[0]][next_point[1]] == 1:
            maze(grid, n, next_point, moves + [next_point])
    return solutions


def tests():
    maze_grid: Grid = [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
    ]
    assert maze(maze_grid, 4) == [
        [(0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3)],
        [(0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)],
        [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 3)],
        [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)],
    ]


if __name__ == "__main__":
    tests()
