"""
A simple menu system using python for the Terminal

Reference: https://gist.github.com/abishur/2482046
"""
import curses
import os
import sys

from _npmanager.constants import PY3

screen = None

def _select(data):
    global screen
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    h = curses.color_pair(1)
    n = curses.A_NORMAL

    optioncount = len(data['options'])

    pos = 0
    oldpos = None
    x = None

    while x != ord('\n'):
        if pos != oldpos:
            oldpos = pos
            screen.border(0)
            screen.addstr(2, 3, '{}{}'.format(data['title'], ' ' * 10), curses.A_STANDOUT)
            screen.addstr(4, 3, data['subtitle'], curses.A_BOLD)

            # display all menu items
            for index in range(optioncount):
                textstyle = n
                if pos == index:
                    textstyle = h
                screen.addstr(5 + index, 4, '{} - {}'.format(
                    index + 1, data['options'][index]['title']), textstyle)
            textstyle = n
            if pos == optioncount:
                textstyle = h
            screen.addstr(5 + optioncount, 4, '{} - {}'.format(
                optioncount + 1, 'Cancel'), textstyle)
            screen.refresh()

        x = screen.getch()
        _x1 = ord('1') if PY3 else unichr(1)
        _x2 = ord(str(optioncount + 1)) if PY3 else unichr(int(optioncount + 1))
        _x3 = ord('0') if PY3 else unichr(0)
        if x >= _x1 and x <= _x2:
            pos = x - _x3 - 1 # convert keypress back to a number, then subtract 1 to get index
        elif x == 258: # down arrow
            if pos < optioncount:
                pos += 1
            else: pos = 0
        elif x == 259: # up arrow
            if pos > 0:
                pos += -1
            else: pos = optioncount

    curses.endwin()
    os.system('clear')
    return pos

def select(data):
    global screen
    # initializes a new window for capturing key presses
    screen = curses.initscr()
    # disables automatic echoing of key presses
    curses.noecho()
    # disables line buffering
    curses.cbreak()
    # lets you use colors when highlighting selected option
    curses.start_color()
    # capture input from keypad
    screen.keypad(1)

    pos = None
    try:
        pos = _select(data)
    except KeyboardInterrupt:
        curses.endwin()
        sys.exit(0)

    return pos
