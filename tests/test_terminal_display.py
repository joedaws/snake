from lib.terminal_display import TerminalDisplay
from lib.display_border import Border
from lib.snake_object import SnakeObject


def main():
    td = TerminalDisplay(blank_char="gray_square")
    border = Border(td)

    print("I should be empty")
    print(td)

    td.add_object(border)

    print("I should have a boarder")
    print(td)

    snake = SnakeObject(td)
    td.add_object(snake)

    print("now there is a snake")
    print(td)


if __name__ == "__main__":
    main()
