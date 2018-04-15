#!/usr/bin/env python3

import argparse
from curses import wrapper

from multiprocessing import Queue
from src import gui


# TODO:
# 1) needs to do heavy refactoring - new project!
# 2) do proper argparse module x or cmd GUI ?
# 3) add interface for ZF - generate messages (you'll need 2 buffers - to keep sending messages and update them latter)
# 4) control it via cmd + clever output on cmd (not just simple print out!)
# 5) Add simple GUI (on rpi directly)
# 6) Add Android App to control Rpi via mobile phone
# 7) Have fun ...

can_interface = 'vcan0'
#can_interface = 'can0'

CAN_DB_FOLDER_NAME = 'can_db'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate CAN-bus and UDS messages")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--send_can", action="store_true", help="Send standard CAN messages")
    group.add_argument("-u", "--send_uds", action="store_true", help="Send diagnostic CAN messages")
    group.add_argument("-r", "--receive", action="store_true", help="Receive any CAN messages")
    parser.add_argument("t", type=int, help="Max timeout [ms]")
    args = parser.parse_args()

    if args.receive:
        print("Receiving messages ...")
    elif args.send_can:
        print("Sending standard can messages")
    elif args.send_uds:
        print("Sending UDS messages")
    else:
        print("Some other option ...")

    # 2. Start GUI
    # a. initialize GUI
    # b. start GUI

    ###############################
    # START GUI                   #
    ###############################
    wrapper(gui.run_app)

    print("- Done -")
