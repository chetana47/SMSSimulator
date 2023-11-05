import queue
import random
import time
import threading

class Sender(threading.Thread):
    def __init__(self, message_queue, msg_store, avg_time, failure_rate):
        super(Sender, self).__init__()
        self.message_queue = message_queue
        self.msg_store = msg_store
        self.avg_time = avg_time
        self.failure_rate = failure_rate

    def generate_processing_time(self):
        # Generate a normally distributed processing time around the average processing time
        variance = self.avg_time * 0.1
        return max(0, round(random.gauss(self.avg_time, variance), 2))

    def run(self):
        # Simulate sending messages
        while True:
            try:
                phone_no, msg = self.message_queue.get(timeout=2)
                processing_time = self.generate_processing_time()

                if 10 - (self.failure_rate * 10) < random.randint(1,10):
                    self.msg_store['failed'] += 1
                else:
                    time.sleep(processing_time)
                    self.msg_store['sent'] += 1

                self.msg_store['total_time'] += processing_time
                self.message_queue.task_done()

            except queue.Empty:
                break



