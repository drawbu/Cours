Grid = list[list[int]]
Point = tuple[int, int]


def maze(
        grid: Grid,
        n: int,
        start: Point = None,
        path: list[Point] = None,
        paths: list[list[Point]] = None
):
    if path is None:
        path = []
    if paths is None:
        paths = []
    if start is None:
        start = (0, 0)

    if start == (n - 1, n - 1):
        paths.append(path)
        return paths

    if start[0] + 1 < n:
        next_point: Point = (start[0] + 1, start[1])
        if grid[next_point[0]][next_point[1]] == 1:
            maze(grid, n, next_point, path + [next_point], paths)

    if start[1] + 1 < n:
        next_point: Point = (start[0], start[1] + 1)
        if grid[next_point[0]][next_point[1]] == 1:
            maze(grid, n, next_point, path + [next_point], paths)
    return paths


def test_maze():
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
