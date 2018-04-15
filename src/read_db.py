import can
import os

from src import config
from src import msgGroup

"""
Helper methods to work with file(s)
"""

def read_messages_from_file(file_name):
    """
    Read messages specified in text file and return list of list Messages with delays
    :param file_name: text file where all messages are specified
    :return: list of MsgGroup
    """
    file_lines = None
    with open(file_name) as f:
        file_lines = f.readlines()

    msg_group = msgGroup.MsgGroup()

    if file_lines is not None:
        for line in file_lines:
            if is_msg_line(line):
                msg_group.messages.append(get_msg_from_line(line))

    for msg in msg_group.messages:
        print("MESSAGES: ", msg)

    return msg_group


def is_msg_line(line):
    """Check if string is message line"""
    if not line.strip().startswith('#'):
        return True
    else:
        return False


def is_comment_line(line):
    """Check if line is comments"""
    if line.strip().startswith('#'):
        return True
    else:
        return False


def get_msg_from_line(line):
    """
    Get message from message string
    :param line: which contains message definition
    :return: can.Message
    """

    cycle_time = 0

    msg_items = line.strip().split(" ", 10)

    try:
        msgid_int = int(msg_items[0], 16)
        data_list_int = [int(x, 16) for x in msg_items[1:9]]
    except ValueError:
        print('Error: Cannot parse message from file!')
        print('Line: ', line)
        print('Cannot cast to int!')

    try:
        time_milis_str = msg_items[9].split("=", 1)[1]
        cycle_time = int(time_milis_str)
    except:
        print('Error: Cannot parse cycle time!')
        print('Line', line)

    msg = msgGroup.Msg(can.Message(extended_id=True, arbitration_id=msgid_int, data=data_list_int), cycle_time)

    return msg


def get_delay_from_line(line):
    """
    Get delay from delay string
    :param line: which contains delay value in ms
    :return: delay
    """
    delay_str = line.split("delay", 1)[1]

    try:
        return int(delay_str.strip())
    except ValueError:
        print('Error: When parsing *.txt file delay line!')
        return 0


def read_all_can_db_groups():
    """
    Read all CAN db groups
    :return:
    """
    msg_groups = []

    can_db_files = [db_file_name for db_file_name in os.listdir(config.CAN_DB_FOLDER_NAME) if
                    os.path.isfile(os.path.join(config.CAN_DB_FOLDER_NAME, db_file_name))]

    for file_name in can_db_files:
        file_path = os.path.join(config.CAN_DB_FOLDER_NAME, file_name)
        can_msg_group = read_messages_from_file(file_path)
        msg_groups.append(can_msg_group)

    return msg_groups
