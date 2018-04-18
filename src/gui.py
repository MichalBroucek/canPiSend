import curses
import time
from multiprocessing import Queue
from src import read_db
from src import send_std_can


STEP = 0.2        # Step for updating GUI

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
    curses.nocbreak()
    my_window.keypad(False)
    my_window.nodelay(False)
    curses.echo()
    curses.curs_set(0)
    my_window.getkey()
    curses.endwin()


def run_app(my_window):
    init_ncurses_setup(my_window)

    msg_groups = read_db.read_all_can_db_groups()

    # TODO: initialize Sending/Receiving Threads here ?
    # TODO: make sending_thread class member (-> run_app simple function, create class for GUI control)
    sending_thread = send_std_can.SendingCanThread(msg_groups[0])
    sending_thread.start_sending()

    actualize_gui(my_window, msg_groups)            # TODO: replace msg_groups to msg_exchange_queue


    # TODO: finish Sending/Receiving Threads here ?

    deinit_ncurses_setup(my_window)

    return


def actualize_gui(my_window, msg_groups):
    """
    Actualize GUI with latest informations
    :param my_window:
    """
    sending_message_tests = False       # Just for testing ...
    i = 0
    while True:
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
            my_window.addstr(line, 2, "{0}    {1}".format(msg_to_send.get_msg_str(), msg_to_send.progress_character))

        i += 1
        # todo: Add receiving messages here ...
        line += 1
        my_window.addstr(line, 2, "____________________________________________________________")
        line += 1
        my_window.addstr(line, 2, "   Receiving messages:")
        line += 1
        my_window.addstr(line, 2, "--> r e c e i v e d   m e s s a g e s")

        my_window.refresh()

        if my_window.getch() == ord('1'):
            # Sending CAN messages from 1st MsgGroup
            sending_message_tests = True

        if my_window.getch() == ord('s'):
            # Stop sending CAN messages
            sending_message_tests = False

        if sending_message_tests:
            for msg_to_send in msg_groups[0].messages:
                msg_to_send.get_progress()

        if my_window.getch() == ord('q'):
            # Finnish and exit
            # deinit_ncurses_setup(my_window)
            # curses.endwin()
            # return
            break

        time.sleep(STEP)  # Frame for updating VIEW

    deinit_ncurses_setup(my_window)
    curses.endwin()
    return
