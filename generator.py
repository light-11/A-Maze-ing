from config import MazeConfig
from maze import Maze
from maze_utils import cell_to_grid
from maze_utils import get_next_cell
from maze_utils import is_inside
from maze_utils import get_wall_position
import random


def generate_maze(config: MazeConfig) -> Maze:
    """Generate the maze."""

    wid = config.width
    hei = config.height
    grid_tup = cell_to_grid(wid, hei)

    # 全セルが1のgridを生成
    grid = [[1 for i in range(grid_tup[1])] for i in range(grid_tup[0])]

    # 論理セルを0に変換
    for y in range(hei):
        for x in range(wid):
            grid_x, grid_y = cell_to_grid(x, y)
            grid[grid_x][grid_y] = 0

    visited = set()
    stack = []
    stack.append(config.entry)
    visited.add((config.entry))

    while stack:
        current = stack[-1]
        next_option = []
        dirs = ["N", "E", "S", "W"]
        for dir in dirs:
            next_x, next_y = get_next_cell(current[0], current[1], dir)
            if is_inside(next_x, next_y, wid, hei):
                if (next_x, next_y) not in visited:
                    next_option.append((next_x, next_y, dir))

        if next_option:
            next_x, next_y, dir = random.choice(next_option)
            wall_x, wall_y = get_wall_position(current[0], current[1], dir)
            grid[wall_x][wall_y] = 0
            stack.append((next_x, next_y))
            visited.add((next_x, next_y))

        else:
            stack.pop()

    return Maze(
        width=wid,
        height=hei,
        grid=grid,
        entry=config.entry,
        exit=config.exit,
        solution=None,
    )
