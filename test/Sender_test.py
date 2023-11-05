import queue
import unittest
from unittest.mock import patch
from Sender import Sender

class TestSender(unittest.TestCase):
    def setUp(self):
        self.message_queue = queue.Queue()
        self.msg_store = {'sent': 0, 'failed': 0, 'total_time': 0}
        self.processing_time = 0.01
        self.failure_rate = 0

    @patch('random.random')
    @patch('time.sleep', return_value=None)  # Mock sleep to speed up tests
    def test_message_sending(self, mock_sleep, mock_random):
        self.failure_rate = 0
        self.sender = Sender(self.message_queue, self.msg_store, self.processing_time, self.failure_rate)
        mock_random.return_value = 1  # Ensure failure rate condition is never met
        for _ in range(10):
            self.message_queue.put(('8573958437', 'Test Message'))
        while not self.message_queue.empty():
            self.sender.run()
        self.assertEqual(self.msg_store['sent'], 10)
        self.assertEqual(self.msg_store['failed'], 0)

    @patch('random.random')
    @patch('time.sleep', return_value=None)  # Mock sleep to speed up tests
    def test_message_sending_fail(self, mock_sleep, mock_random):
        self.failure_rate = 1
        self.sender = Sender(self.message_queue, self.msg_store, self.processing_time, self.failure_rate)
        mock_random.return_value = 9  # Ensure failure rate condition is always met
        for _ in range(10):
            self.message_queue.put(('8573958437', 'Test Message'))
        while not self.message_queue.empty():
            self.sender.run()
        self.assertEqual(self.msg_store['sent'], 0)
        self.assertEqual(self.msg_store['failed'],10)

if __name__ == '__main__':
    unittest.main()
