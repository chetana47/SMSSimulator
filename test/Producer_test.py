import unittest
import queue
from Producer import Producer

class TestProducer(unittest.TestCase):
    def setUp(self):
        self.message_queue = queue.Queue()
        self.msg_count = 10
        self.producer = Producer(self.message_queue, self.msg_count)

    def test_message_generation(self):
        # Test if Producer creates the correct number of messages
        self.assertEqual(self.message_queue.qsize(), self.msg_count)

    def test_phone_number_generation(self):
        # Test if phone numbers generated are of correct length
        phone_no = self.producer.generate_phn_no()
        self.assertEqual(len(phone_no), 10)

    def test_message_content_generation(self):
        # Test if messages generated are of correct length
        msg = self.producer.generate_msg()
        self.assertTrue(1 <= len(msg) <= 100)

if __name__ == '__main__':
    unittest.main()
