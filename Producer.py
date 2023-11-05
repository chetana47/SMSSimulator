import threading
import random
import string

class Producer(threading.Thread):
    def __init__(self, message_queue, msg_count=1000):
        super(Producer, self).__init__()
        self.msg_count = msg_count
        self.message_queue = message_queue
        self.add_to_queue()

    def add_to_queue(self):
        # Generate and add messages to the queue
        for _ in range(self.msg_count):
            phone_no = self.generate_phn_no()
            msg = self.generate_msg()
            self.message_queue.put((phone_no, msg))

    def generate_phn_no(self):
        # Generate a random 10-digit phone number
        return ''.join(random.choice(string.digits) for _ in range(10))

    def generate_msg(self):
        # Generate a random message of up to 100 characters
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 100)))
