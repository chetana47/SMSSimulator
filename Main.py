import queue
from Producer import Producer
from Sender import Sender
from ProgressMonitor import ProgressMonitor

def alert_service():
    # Initialize message store
    msg_store = {'sent': 0, 'failed': 0, 'total_time': 0}

    # Collect user inputs
    message_count = int(input("Input the number of messages to generate: "))
    senders_count = int(input("Input the number of senders: "))
    avg_time = float(input("Input the mean processing time for senders: "))
    refresh_interval = int(input("Input the tracker update interval in seconds: "))
    failure_rate = float(input("Input the failure rate for senders (0 - 1): "))

    # Validate inputs
    if message_count <= 0 or senders_count <= 0 or not 0 <= failure_rate <= 1 or avg_time <= 0 or refresh_interval <= 0:
        raise ValueError("Invalid input")

    # Initialize message queue and producer
    message_queue = queue.Queue()
    producer = Producer(message_queue, message_count)

    # Initialize senders
    senders = [Sender(message_queue, msg_store, avg_time , failure_rate) for i in range(senders_count)]

    # Initialize and start progress monitor
    progress_monitor = ProgressMonitor(senders, msg_store, refresh_interval)

    for sender in senders:
        sender.start()
    progress_monitor.start()

    # Wait for senders to finish
    for sender in senders:
        sender.join()

    # Display final status and terminate progress monitor
    progress_monitor.show_status()
    progress_monitor.terminate()

alert_service()
