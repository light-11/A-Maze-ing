from maze import Maze


def render_ascii(
        maze: Maze,
        show_solution: bool,
        wall_color: bool
        ) -> None:
    """Print the maze as ASCII art."""

    if wall_color:
        set_color = "\033[34m"
        reset_color = "\033[0m"
    else:
        set_color = ""
        reset_color = ""

    print_grid = [column.copy() for column in maze.grid]

    entry_x = 2 * maze.entry[0] + 1
    entry_y = 2 * maze.entry[1] + 1
    exit_x = 2 * maze.exit[0] + 1
    exit_y = 2 * maze.exit[1] + 1

    if show_solution and maze.solution is not None:
        current_x = entry_x
        current_y = entry_y
        for move in maze.solution:
            if move == "N":
                print_grid[current_x][current_y - 1] = 4
                current_y -= 2
            elif move == "E":
                print_grid[current_x + 1][current_y] = 4
                current_x += 2
            elif move == "S":
                print_grid[current_x][current_y + 1] = 4
                current_y += 2
            elif move == "W":
                print_grid[current_x - 1][current_y] = 4
                current_x -= 2
            print_grid[current_x][current_y] = 4

    print_grid[entry_x][entry_y] = 2
    print_grid[exit_x][exit_y] = 3

    for y in range(maze.height * 2 + 1):
        line = ""
        for x in range(maze.width * 2 + 1):
            if print_grid[x][y] == 0:
                line += ("  ")
            elif print_grid[x][y] == 1:
                line += f"{set_color}##{reset_color}"
            elif print_grid[x][y] == 2:
                line += "S "
            elif print_grid[x][y] == 3:
                line += "G "
            elif print_grid[x][y] == 4:
                line += ".."
        print(line)
    return


def print_menu() -> None:
    """Print visualizer menu."""
    print()
    print("[1] Regenerate maze")
    print("[2] Show / hide solution")
    print("[3] Change wall color")
    print("[4] Quit")
    return


def read_menu() -> str:
    """Read a valid menu selection."""
    # 下に１行空白を確保してから、１行上に戻る
    print()
    print("\033[1A", end="")

    # 正しい選択肢が入力されるまでループ
    while True:
        selected = input("> ")

        if selected in ("1", "2", "3", "4"):
            return selected

        # 誤入力は１行戻して消去
        print("\033[1A\033[J", end="")


def enter_visualizer() -> None:
    """Enter the alternate terminal screen."""
    print("\033[?1049h", end="", flush=True)


def leave_visualizer() -> None:
    """Leave the alternate terminal screen."""
    print("\033[?1049l", end="", flush=True)


def clear_visualizer() -> None:
    """Clear the visualizer screen and move cursor home."""
    print("\033[H\033[J", end="", flush=True)


def visualize_maze(maze: Maze) -> str:
    """Run the terminal visualizer."""
    show_solution = False
    wall_color = False

    enter_visualizer()

    try:
        while True:
            clear_visualizer()
            render_ascii(maze, show_solution, wall_color)
            print_menu()

            selected = read_menu()

            if selected == "1":
                return selected
            elif selected == "2":
                show_solution = not show_solution
            elif selected == "3":
                wall_color = not wall_color
            elif selected == "4":
                return selected
    finally:
        leave_visualizer()
