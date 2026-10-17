from .maze import Maze
from .maze_utils import cell_to_grid
from .maze_utils import get_next_cell
from .maze_utils import is_inside
from .maze_utils import get_wall_position
from .logo42 import is_logo_size_valid
from .logo42 import is_logo_position_valid
from .logo42 import create_logo_cells
from .solver import solve_maze

import random


class MazeGenerator:
    """Generate and manage a maze."""

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        perfect: bool,
        seed: int | None = None,
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.validate()

    def validate(self) -> None:
        """Validate maze generator parameters."""

        # Validate width and height
        try:
            self.width = int(self.width)
            self.height = int(self.height)
        except (ValueError, TypeError):
            raise ValueError("Width and height must be integers")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers")

        # Validate entry and exit points
        try:
            entry_list = [int(value) for value in self.entry]
            exit_list = [int(value) for value in self.exit]
        except (ValueError, TypeError):
            raise ValueError("Entry and exit must be integers")
        if len(entry_list) != 2 or len(exit_list) != 2:
            raise ValueError("Entry and exit must contain two coordinates")
        self.entry = (entry_list[0], entry_list[1])
        self.exit = (exit_list[0], exit_list[1])
        if not (
            0 <= self.entry[0] < self.width
            and 0 <= self.entry[1] < self.height
        ):
            raise ValueError("Entry point must be within maze bounds")

        if not (
            0 <= self.exit[0] < self.width
            and 0 <= self.exit[1] < self.height
        ):
            raise ValueError("Exit point must be within maze bounds")

        if self.entry == self.exit:
            raise ValueError("Entry and exit points must be different")

        # Validate perfect flag
        if not isinstance(self.perfect, bool):
            raise ValueError("PERFECT must be True or False")

        # Validate seed
        if self.seed is not None:
            try:
                self.seed = int(self.seed)
            except (ValueError, TypeError):
                raise ValueError("SEED must be an integer")

    def generate(self) -> Maze:
        maze = self.make_perfect(
            self.width,
            self.height,
            self.entry,
            self.exit,
            self.seed,
        )
        if not self.perfect:
            self.make_non_perfect(maze, self.seed)
        solve_maze(maze)
        return maze

    def make_non_perfect(
        self,
        maze: Maze,
        seed: int | None = None,
    ) -> None:
        """Modify a perfect maze into a non-perfect maze."""

        wid = maze.width
        hei = maze.height
        rng = random.Random(seed)
        dirs = ["N", "E", "S", "W"]
        for y in range(hei):
            for x in range(wid):
                if (x, y) in maze.logo_cells:
                    continue
                wall_count = 0
                wall_dirs = []
                for dir in dirs:
                    wall_x, wall_y = get_wall_position(x, y, dir)
                    if maze.grid[wall_x][wall_y] == 1:
                        wall_count += 1
                        next_x, next_y = get_next_cell(x, y, dir)
                        if is_inside(next_x, next_y, wid, hei):
                            if (next_x, next_y) not in maze.logo_cells:
                                wall_dirs.append(dir)
                if wall_count == 3 and wall_dirs:
                    dir = rng.choice(wall_dirs)
                    wall_x, wall_y = get_wall_position(x, y, dir)
                    maze.grid[wall_x][wall_y] = 0

    def make_perfect(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        seed: int | None = None,
    ) -> Maze:
        """Generate a perfect maze."""

        rng = random.Random(seed)
        wid = width
        hei = height
        grid_tup = cell_to_grid(wid, hei)

        if not is_logo_size_valid(width, height):
            print("Error: Maze is too small for the 42 logo.")
            logo_cells = set()
        else:
            logo_cells = create_logo_cells(wid, hei)

        if not is_logo_position_valid(logo_cells, entry, exit):
            raise ValueError("Entry or exit overlaps the 42 logo.")

        # 全セルが1のgridを生成
        grid = [[1 for i in range(grid_tup[1])] for i in range(grid_tup[0])]

        # 論理セルを0に変換
        for y in range(hei):
            for x in range(wid):
                if (x, y) in logo_cells:
                    continue
                grid_x, grid_y = cell_to_grid(x, y)
                grid[grid_x][grid_y] = 0

        visited = set()
        stack = []
        stack.append(entry)
        visited.add((entry))

        while stack:
            current = stack[-1]
            next_option = []
            dirs = ["N", "E", "S", "W"]
            for dir in dirs:
                next_x, next_y = get_next_cell(current[0], current[1], dir)
                if is_inside(next_x, next_y, wid, hei):
                    if (
                        (next_x, next_y) not in visited
                        and (next_x, next_y) not in logo_cells
                    ):
                        next_option.append((next_x, next_y, dir))

            if next_option:
                next_x, next_y, dir = rng.choice(next_option)
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
            entry=entry,
            exit=exit,
            solution=None,
            logo_cells=logo_cells,
        )


def generate_maze(
    width: int,
    height: int,
    entry: tuple[int, int],
    exit: tuple[int, int],
    perfect: bool,
    seed: int | None = None,
) -> Maze:
    """Generate the maze."""

    return MazeGenerator(
        width,
        height,
        entry,
        exit,
        perfect,
        seed,
    ).generate()
