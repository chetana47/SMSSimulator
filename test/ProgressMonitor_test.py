import queue
import time
import unittest
from unittest.mock import patch
from ProgressMonitor import ProgressMonitor
from Sender import Sender

class TestProgressMonitor(unittest.TestCase):

    def setUp(self):
        self.msg_store = {'sent': 0, 'failed': 0, 'total_time': 0}
        self.senders = [Sender(queue.Queue(), self.msg_store, 1, 0) for _ in range(2)]
        self.updateInterval = 3  # Set the refresh interval to 3 seconds for the test
        self.monitor = ProgressMonitor(self.senders, self.msg_store, self.updateInterval)

    def test_monitor_stopping(self):
        self.monitor.start()
        self.monitor.terminate()
        self.monitor.join()
        self.assertFalse(self.monitor.is_active)

    @patch('time.sleep', side_effect=lambda x: None)
    def test_monitor_display_called_once(self, mock_sleep):
        with patch.object(self.monitor, 'show_status', wraps=self.monitor.show_status) as mock_display:
            self.monitor.start()
            time.sleep(3)
            self.monitor.terminate()
            self.monitor.join()

        # Display is called once.
        mock_display.assert_called_once()

        # Identify sleep is called with the update interval.
        mock_sleep.assert_called_with(self.updateInterval)

    @patch('time.sleep', side_effect=lambda x: None)
    def test_monitor_update_interval(self, mock_sleep):
        with patch.object(self.monitor, 'show_status', wraps=self.monitor.show_status) as mock_display:
            self.monitor.start()
            time.sleep(3)
            self.monitor.terminate()
            self.monitor.join()

        # Display is called.
        self.assertTrue(mock_display.called)

        # Identify sleep is called with update interval.
        mock_sleep.assert_called_with(self.updateInterval)

if __name__ == '__main__':
    unittest.main()
