from lib.terminal_display import TerminalDisplay
from lib.display_border import Border

def main():
    td = TerminalDisplay(blank_char="gray_square")
    border = Border(td)

    print(td)

    td.add_object(border)

    print(td)


if __name__ == "__main__":
    main()
