import unittest
from src.models.event import Event

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event = Event(1, "event1", "description1")

    def test_id(self):
        self.assertEqual(self.event.id, 1)

    def test_name(self):
        self.assertEqual(self.event.name, "event1")

    def test_description(self):
        self.assertEqual(self.event.description, "description1")

if __name__ == '__main__':
    unittest.main()
