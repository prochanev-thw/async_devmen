import time
import curses


def draw(canvas):
    curses.curs_set(False)
    row, column = (curses.LINES // 2, curses.COLS // 2)
    canvas.addstr(row, column, 'Hello world!')
    canvas.refresh()
    time.sleep(10)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
