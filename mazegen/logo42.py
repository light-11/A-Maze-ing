LOGO_WIDTH = 7
LOGO_HEIGHT = 5

LOGO_PATTERN = {
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (2, 3),
    (2, 4),

    (4, 0),
    (5, 0),
    (6, 0),
    (6, 1),
    (4, 2),
    (5, 2),
    (6, 2),
    (4, 3),
    (4, 4),
    (5, 4),
    (6, 4),
}


def create_logo_cells(width: int, height: int) -> set[tuple[int, int]]:
    """Return the logical cells forming the 42 logo."""
    logo = set()
    origin_x = (width - LOGO_WIDTH) // 2
    origin_y = (height - LOGO_HEIGHT) // 2
    for x, y in LOGO_PATTERN:
        logo.add((x + origin_x, y + origin_y))

    return logo


def is_logo_size_valid(width: int, height: int) -> bool:
    """Check whether the maze can contain the 42 logo."""
    return width >= LOGO_WIDTH + 2 and height >= LOGO_HEIGHT + 2


def is_logo_position_valid(
    logo_cells: set[tuple[int, int]],
    entry: tuple[int, int],
    exit: tuple[int, int],
) -> bool:
    """Check whether entry and exit avoid the 42 logo."""
    return entry not in logo_cells and exit not in logo_cells
