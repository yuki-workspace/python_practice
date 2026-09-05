import unittest
from example import add

# テスト2
class AddTest(unittest.TestCase):
  def test_get_the_sum_of_two_integers(self):
    """add()関数のテストコード"""
    actual = add(1,3)
    expected = 4
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()