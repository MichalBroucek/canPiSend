from multiprocessing import Process
import time
import queue


STEP_MS = 1000


def sending_msg(data_queue):

    keep_sending = True

    commands_read = None

    while keep_sending:
        # Keep sending data ...
        # Keep receiving data ...
        print('Sending CAN msg ...')

        # Keep reading commands
        try:
            commands_read = data_queue.get(False)
            print('commands read: {}'.format(commands_read))
        except queue.Empty:
            pass

        time.sleep(STEP_MS / 1000.0)


class CanMsgExchange:
    def __init__(self, data_queue):
        self.local_process = Process(target=sending_msg, args=(data_queue,))

    def start_exchange(self):
        self.local_process.start()

    def join_process(self):
        self.local_process.join()
