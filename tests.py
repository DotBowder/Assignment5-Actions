import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def area_test1(self):
        r = 1
        expected = 3.14 * r * r
        self.assertEqual(expected, task.area(r))
        r = 2
        expected = 3.14 * r * r
        self.assertEqual(expected, task.area(r))


if __name__ == '__main__':
    unittest.main()
