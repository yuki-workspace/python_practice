import unittest
from example import add

# テスト1
class AddTest(unittest.TestCase):
  def test_get_the_sum_of_two_integers(self):
    """add()関数のテストコード"""
    actual = add(1,2)
    expected = 3
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()