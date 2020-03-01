import unittest
import task
import datetime


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

    def list_test1(self):
        list_obj = ['a', 'b', 'c']
        expected = ('a', 'c')
        self.assertEqual(expected, task.list(list_obj))
        list_obj = []
        expected = (None, None)
        self.assertEqual(expected, task.list(list_obj))

    def date_test1(self):
        d1 = datetime.datetime(2020, 1, 10)
        d2 = datetime.datetime(1800, 2, 5)
        diff = abs(d2 - d1)
        expected = diff.days
        self.assertEqual(expected, task.date(d1, d2))


if __name__ == '__main__':
    unittest.main()
