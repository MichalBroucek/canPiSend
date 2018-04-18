

class MsgGroup:
    """
    Class to hold group of messages with theirs delays
    """

    def __init__(self):
        self.messages = []

    def clean(self):
        """
        Reset object into the default state
        """
        self.messages = []


class Msg:
    """
    Class to hold one message with message cycle time
    """

    def __init__(self, can_message, clc_time):
        self.message = can_message              # CAN Message
        self.cycle_time = clc_time              # CAN Message cycle time
        self.type = 's'                         # CAN Message type: r=receive, s=send
        self.progress_character = "/"           # Character signalized message activity
        self.activity_since_lasttime = True
        self.progress_list = ['/', '-', '\\', '|']
        self.progress_id = 0

    def get_progress(self):
        """
        Return sign for progress if message is received (only if particular message is updated/sent) - this may be tricky
        :return: next character from progress list if msg was updated
        """
        if self.activity_since_lasttime:
            temp_id = self.progress_id
            self.progress_id += 1
            if self.progress_id > 3:
                self.progress_id = 0
            self.progress_character = self.progress_list[temp_id]
        else:
            self.progress_character = self.progress_list[self.progress_id]
        return self.progress_character

    def print_msg(self):
        data_str = "{0:x}".format(self.message.data[0]) + " {0:x}".format(self.message.data[1]) + \
                   " {0:x}".format(self.message.data[2]) + " {0:x}".format(self.message.data[3]) + \
                   " {0:x}".format(self.message.data[4]) + " {0:x}".format(self.message.data[5]) + \
                   " {0:x}".format(self.message.data[6]) + " {0:x}".format(self.message.data[7])
        message_description = "<--  {0:x}".format(self.message.arbitration_id) + "   " + data_str + \
                              "   cycle time = {}".format(self.cycle_time)
        print(message_description)

    def get_msg_str(self):
        data_str = "{0:x}".format(self.message.data[0]) + " {0:x}".format(self.message.data[1]) + \
                   " {0:x}".format(self.message.data[2]) + " {0:x}".format(self.message.data[3]) + \
                   " {0:x}".format(self.message.data[4]) + " {0:x}".format(self.message.data[5]) + \
                   " {0:x}".format(self.message.data[6]) + " {0:x}".format(self.message.data[7])
        message_description = "<--  {0:x}   {1}".format(self.message.arbitration_id, data_str)
        return message_description