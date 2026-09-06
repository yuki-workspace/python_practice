import unittest
from example import add

class AddTest(unittest.TestCase):
  def test_get_the_sum_of_two_integers(self):
    """2つの整数の合計値を取得できる"""
    self.assertEqual(add(1,2), 3)
    self.assertEqual(add(1,2), 4)
    self.assertEqual(add(3,3), 6)

if __name__ == '__main__':
  unittest.main()

"""
1つのテストメソッドの中では1つのアサーションメソッドを行う方がいい
2つめ以降は正常に実行できない可能性がある
→複数のアサーションメソッドを呼ぶ時は、subtest()メソッドを使用することですべて実行できる
"""