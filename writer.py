from maze import Maze


def grid_to_hex(grid: list[list[int]], x: int, y: int) -> str:
    """Convert one logical maze cell to a hexadecimal wall value."""

    num = (
        grid[2 * y][2 * x + 1] * 1 +
        grid[2 * y + 1][2 * x + 2] * 2 +
        grid[2 * y + 2][2 * x + 1] * 4 +
        grid[2 * y + 1][2 * x] * 8
    )
    return format(num, 'X')


def write_maze(maze: Maze, filename: str) -> None:
    """Write the maze to an output file."""

    output_str = ""
    for y in range(maze.height):
        for x in range(maze.width):
            output_str += grid_to_hex(
                maze.grid,
                x,
                y
            )
        output_str += "\n"
    output_str += "\n"
    output_str += f"{maze.entry[0]},{maze.entry[1]}\n"
    output_str += f"{maze.exit[0]},{maze.exit[1]}\n"
    if maze.solution is not None:
        output_str += "".join(maze.solution) + "\n"

    print(output_str, end="")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_str)

    return
