import curses
import time
from multiprocessing import Queue
from src import read_db


STEP = 0.2      # Step for updating GUI

msg_exchange_queue = Queue()  # TODO: Queue for communication between processes. How to deal with it ?


def init_ncurses_setup(my_window):
    """
    Setup ncurses cmd GUI configuration
    :param my_window: active window
    """
    my_window.clear()  # Clear screen
    curses.noecho()
    curses.curs_set(0)
    my_window.keypad(True)
    curses.cbreak()
    my_window.nodelay(True)


def deinit_ncurses_setup(my_window):
    # GUI finnished - clean cmd gui configuration
    my_window.refresh()

    curses.nocbreak()
    my_window.keypad(False)
    my_window.nodelay(False)
    curses.echo()

    my_window.getkey()
    curses.endwin()


def run_app(my_window):
    init_ncurses_setup(my_window)

    msg_groups = read_db.read_all_can_db_groups()

    actualize_gui(my_window, msg_groups)

    # TODO: initialize Sending/Receiving Threads here ?

    # TODO: finish Sending/Receiving Threads here ?

    deinit_ncurses_setup(my_window)

    return


def actualize_gui(my_window, msg_groups):
    """
    Actualize GUI with latest informations
    :param my_window:
    """
    i = 0
    while i < 255:
        my_window.addstr(0, 2, "CAN message simulation")
        my_window.addstr(1, 2, "\n")
        my_window.addstr(2, 2, "Number of messages groups: {0};  Number msgs in 1st group: {1}".format(len(msg_groups),
                                                                                        len(msg_groups[0].messages)))
        my_window.addstr(3, 5,
                         "[I/i] Idle   [T/t] Torque   [X] not defined   [X] not defined   [X] not defined   [q] Quit")
        my_window.addstr(4, 2, "\n")
        my_window.addstr(5, 2, "   Sending messages:")
        line = 5
        for msg_to_send in msg_groups[0].messages:
            line += 1
            my_window.addstr(line, 2, "{0}    {1}".format(msg_to_send.get_msg_str(), msg_to_send.get_progress()))

        time.sleep(STEP)  # Frame for updating VIEW

        i += 1

        # todo: Add receiving messages here ...
        line += 1
        my_window.addstr(line, 2, "____________________________________________________________")
        line += 1
        my_window.addstr(line, 2, "   Receiving messages:")
        line += 1
        my_window.addstr(line, 2, "--> r e c e i v e d   m e s s a g e s")

        if my_window.getch() == ord('q'):
            # Finnish and exit
            curses.nocbreak()
            my_window.keypad(False)
            my_window.nodelay(False)
            curses.curs_set(1)
            curses.echo()
            curses.endwin()
            return

        my_window.refresh()
