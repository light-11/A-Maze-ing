from maze import Maze


def render_ascii(maze: Maze) -> None:
    """Print the maze as ASCII art."""
    print_grid = [row.copy() for row in maze.grid]

    entry_x = 2 * maze.entry[0] + 1
    entry_y = 2 * maze.entry[1] + 1
    exit_x = 2 * maze.exit[0] + 1
    exit_y = 2 * maze.exit[1] + 1

    print_grid[entry_y][entry_x] = 2
    print_grid[exit_y][exit_x] = 3

    for row in print_grid:
        line = ""
        for cell in row:
            if cell == 0:
                line += ("  ")
            elif cell == 1:
                line += "##"
            elif cell == 2:
                line += "S "
            elif cell == 3:
                line += "G "
        print(line)
    return


def visualize_maze(maze: Maze) -> None:
    """Run the terminal visualizer."""
    render_ascii(maze)
