import time
from lib.terminal_display import TerminalDisplay
from lib.snake_object import SnakeObject
from lib.display_border import Border
from lib.snake_object import Direction


if __name__ == "__main__":
    td = TerminalDisplay()
    print(len(td.chars))
    border = Border(td)
    snake = SnakeObject(td)

    td.add_object(border)
    td.add_object(snake)

    nlines = td.rows + 1

    print(len(td.chars))

    # scroll up to make room for output
    print(f"\033[{nlines}S", end="")

    # move cursor back up
    print(f"\033[{nlines}A", end="")

    # save current cursor position
    print("\033[s", end="")

    directions = [Direction.UP]*2 +\
                 [Direction.RIGHT]*2 +\
                 [Direction.DOWN]*2 +\
                 [Direction.LEFT]*2
    num_dir = len(directions)

    for i in range(25):
        # restore saved cursor position
        print("\033[u", end="")

        # get next direction
        new_dir = directions[i % num_dir]

        snake = td.remove_object(snake.name)
        snake.move(new_dir)
        td.add_object(snake)
        print(td)
        time.sleep(0.17)
