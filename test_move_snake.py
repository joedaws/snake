from lib.terminal_display import TerminalDisplay
from lib.snake_object import SnakeObject
from lib.display_border import Border
from lib.snake_object import Direction


if __name__ == "__main__":
    td = TerminalDisplay()
    border = Border(td)
    snake = SnakeObject(td)

    td.add_object(border)
    td.add_object(snake)

    print(f"snake in starting position.")
    print(f"{snake.directions[0]}")
    print(f"{snake.head_position}")
    print(td)

    snake = td.remove_object(snake.name)

    print(f"after remove snake")
    print(td)

    snake.move(Direction.UP)
    td.add_object(snake)

    print(f"snake after moving 1.")
    print(f"{snake.directions[0]}")
    print(f"{snake.head_position}")
    print(td)

    snake = td.remove_object(snake.name)
    snake.move(Direction.UP)
    td.add_object(snake)

    print(f"snake after moving UP 1.")
    print(f"{snake.directions[0]}")
    print(f"{snake.head_position}")
    print(td)

    snake = td.remove_object(snake.name)
    snake.move(Direction.UP)
    td.add_object(snake)

    print(f"snake after moving UP 1.")
    print(f"{snake.directions[0]}")
    print(f"{snake.head_position}")
    print(td)
