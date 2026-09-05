import unittest
from example import add

class AddTest(unittest.TestCase):
  def test_assert_equal(self):
    """assertEqual()使用例"""
    actual = add(1,2)
    expected = 3
    self.assertEqual(actual, expected)

  def test_assert_is_not_none(self):
    """assertIsNotNone使用例"""
    actual = add(1,2)
    self.assertIsNotNone(actual)

  def test_assert_is_instance(self):
    """assertIsInstance使用例"""
    actual = add(1,2)
    self.assertIsInstance(actual, int)

  def test_assert_is_raises(self):
      """assertRaises使用例"""
      with self.assertRaises(TypeError):
        add(None, 2)

if __name__ == '__main__':
  unittest.main()
