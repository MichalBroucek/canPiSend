import os.path

from src import read_db
from multiprocessing import Queue
from src import can_msg_exchange


def sending_std_msgs():
    msg_exchange_queue = Queue()

    msg_groups = read_db.read_all_can_db_groups()

    # OK
    # for msg_group in msg_groups:
    #     for msg in msg_group.messages:
    #         msg.print_msg()
    #
    #     print("--------------------------------------")

    # TODO: start sending in separate thread here + GUI activation
    # 1) Start GUI ... in the gui listen for commands ?

    # 2) Start thread for sending messages
    msg_exchange = can_msg_exchange.CanMsgExchange(msg_exchange_queue)
    msg_exchange.start_exchange()

