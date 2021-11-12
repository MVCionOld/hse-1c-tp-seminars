import unittest


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


if __name__ == '__main__':
    unittest.main()
