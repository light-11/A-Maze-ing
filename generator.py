from config import MazeConfig
from maze import Maze


def generate_maze(config: MazeConfig) -> Maze:
    """Generate the maze."""

    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]

    return Maze(
        width=2,
        height=2,
        grid=grid,
        entry=(0, 0),
        exit=(1, 1),
        solution=None,
    )
