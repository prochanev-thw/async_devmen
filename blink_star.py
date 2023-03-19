import time
import curses
import itertools
import random


def star():
    frames = (
        (('*', curses.A_DIM), lambda: time.sleep(2)),
        (('*', ), lambda: time.sleep(0.3)),
        (('*', curses.A_BOLD), lambda: time.sleep(0.5)),
        (('*', ), lambda: time.sleep(0.3))
    )
    for frame_definition, pause_after in itertools.cycle(frames):
        yield frame_definition, pause_after


def draw(canvas):
    curses.curs_set(False)
    row, column = (curses.LINES // 2, curses.COLS // 2)
    for frame, pause in star():
        canvas.addstr(row, column, *frame)
        canvas.refresh()
        pause()


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
