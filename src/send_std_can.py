
from multiprocessing import Queue
from multiprocessing import Process
import time
from src import read_db
from src import can_msg_exchange


MAX_MSG_DEBUG = 50         # Maximum nmb of sent messages


def write_file_debug(str_to_write):
    """
    Debug write function into the file to test progress of separate thread
    :return:
    """
    with open("send_thread_output", "a") as fout:
        fout.write(str_to_write)


def sending_msg(msg_group):

    msg_sent_nmb_debug = 0

    while True:
        write_file_debug('Sending CAN msg ... {} ...\n'.format(msg_sent_nmb_debug))

        msg_sent_nmb_debug += 1
        if msg_sent_nmb_debug >= MAX_MSG_DEBUG:
            break

        time.sleep(1)

    write_file_debug("Sending loop finished\n")


class SendingCanThread:
    """
    Class to be sending CAN messages onto CAN HW interface in separate thread and report status of messages
    """

    def __init__(self, msg_group):
        self.msg_can_group = msg_group
        self.sending_process = Process(target=sending_msg, args=(msg_group,))

    def start_sending(self):
        """Start sending thread"""
        self.sending_process.start()

    def join_process(self):
        self.sending_process.join()
