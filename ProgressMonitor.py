import threading
import time

class ProgressMonitor(threading.Thread):
    def __init__(self, senders, msg_store, interval):
        super().__init__()
        self.senders = senders
        self.msg_store = msg_store
        self.interval = interval
        self.is_active = True

    def run(self):
        # Display status at regular intervals
        while self.is_active:
            self.show_status()
            time.sleep(self.interval)

    def show_status(self):
        # Display the current status
        total_msgs_sent = self.msg_store['sent']
        total_msgs_failed = self.msg_store['failed']
        total_messages = total_msgs_sent + total_msgs_failed
        total_time = self.msg_store['total_time']

        if total_messages:
            avg_processing_time = total_time / total_messages
            print(f"Messages sent successfully: {total_msgs_sent}")
            print(f"Messages failed to send: {total_msgs_failed}")
            print(f"Average time per message: {avg_processing_time:.2f} seconds\n")
        else:
            print("No messages processed yet.")

    def terminate(self):
        # Terminate the progress monitor
        self.is_active = False
