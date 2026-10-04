from maze import Maze
from maze_utils import get_next_cell
from maze_utils import is_inside
from maze_utils import get_wall_position


def solve_maze(maze: Maze) -> None:
    """Solve the maze."""

    queue: list[tuple[int, int]]
    visited: set[tuple[int, int]]
    parent: dict[
        tuple[int, int],
        tuple[tuple[int, int], str],
    ]
    solution: list[str]

    queue = [maze.entry]
    que_index = 0
    visited = {maze.entry}
    parent = {}

    while que_index < len(queue):
        current = queue[que_index]
        que_index += 1
        x, y = current

        if current == maze.exit:
            break

        for direction in ("N", "E", "S", "W"):
            next_x, next_y = get_next_cell(x, y, direction)

            if not is_inside(next_x, next_y, maze.width, maze.height):
                continue

            wall_x, wall_y = get_wall_position(x, y, direction)
            if maze.grid[wall_x][wall_y] == 1:
                continue

            next_cell = (next_x, next_y)
            if next_cell in visited:
                continue

            visited.add(next_cell)
            parent[next_cell] = (current, direction)
            queue.append(next_cell)

    if maze.exit not in visited:
        raise ValueError("No path to exit")

    solution = []
    current = maze.exit

    while True:
        current, direction = parent[current]
        solution.append(direction)
        if current == maze.entry:
            break

    solution.reverse()
    maze.solution = solution

    return
