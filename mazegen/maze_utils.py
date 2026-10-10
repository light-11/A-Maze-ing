def cell_to_grid(x: int, y: int) -> tuple[int, int]:
    """Convert logical cell coordinates to expanded-grid coordinates."""
    return 2 * x + 1, 2 * y + 1


def is_inside(
    x: int,
    y: int,
    width: int,
    height: int,
) -> bool:
    """Return whether a logical cell is inside the maze."""
    return 0 <= x < width and 0 <= y < height


def get_next_cell(
    x: int,
    y: int,
    direction: str,
) -> tuple[int, int]:
    """Return the adjacent logical cell in the given direction."""
    if direction == "N":
        return x, y - 1
    if direction == "E":
        return x + 1, y
    if direction == "S":
        return x, y + 1
    if direction == "W":
        return x - 1, y

    raise ValueError("Invalid direction")


def get_next_position(
    x: int,
    y: int,
    direction: str,
) -> tuple[int, int]:
    """Return the expanded-grid position of the adjacent cell."""
    next_x, next_y = get_next_cell(x, y, direction)
    return cell_to_grid(next_x, next_y)


def get_wall_position(
    x: int,
    y: int,
    direction: str,
) -> tuple[int, int]:
    """Return the expanded-grid position of the wall in a direction."""
    if direction == "N":
        return 2 * x + 1, 2 * y
    if direction == "E":
        return 2 * x + 2, 2 * y + 1
    if direction == "S":
        return 2 * x + 1, 2 * y + 2
    if direction == "W":
        return 2 * x, 2 * y + 1

    raise ValueError("Invalid direction")
