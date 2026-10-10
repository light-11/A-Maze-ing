class Maze:
    """Store generated maze data."""

    def __init__(
        self,
        width: int,
        height: int,
        grid: list[list[int]],
        entry: tuple[int, int],
        exit: tuple[int, int],
        solution: list[str] | None = None,
    ) -> None:
        self.width = width
        self.height = height
        self.grid = grid
        self.entry = entry
        self.exit = exit
        self.solution = solution
