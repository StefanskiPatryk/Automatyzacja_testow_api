# test_app.py
import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 10), 12)
        self.assertEqual(add(-10, 4), -6)
        self.assertEqual(add(1, 0), 1)

if __name__ == "__main__":
    unittest.main()
