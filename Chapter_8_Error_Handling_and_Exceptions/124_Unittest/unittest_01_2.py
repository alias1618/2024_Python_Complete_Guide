import unittest
import unittest_01_1

class MyTest(unittest.TestCase):
    def test_one(self):
        text = "sample"
        result = unittest_01_1.cap_text(text)
        self.assertEqual(result, "Sample")

    def test_two(self):
        text = "just testing"
        result = unittest_01_1.cap_text(text)
        self.assertEqual(result, "Just Testing")

if __name__ == '__main__':
    unittest.main()