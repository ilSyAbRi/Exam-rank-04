def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = []
    for r in range(dim):
        row_dot = []
        for i in range(dim):
            row_dot.append(".")
        grid.append(row_dot)

    for row_cord in stars:
        x, y = row_cord
        if 0 <= x < dim and 0 <= y < dim:
            grid[x][y] = "*"
    result = ["".join(row) for row in grid]
    return result