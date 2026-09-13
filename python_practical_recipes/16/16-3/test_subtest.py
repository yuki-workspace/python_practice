import unittest
from example import add

class AddTest(unittest.TestCase):
  def test_get_the_sum_of_two_integers(self):
    """2つの整数の合計値を取得できる"""

    examples=[
      [1,2,3],
      [1,3,4],
      [3,3,6]
    ]

    for idx, example in enumerate(examples):
      a, b, expected = example
      with self.subTest(f'{a}+{b}={expected}', idx=idx):
        self.assertEqual(add(a,b), expected)

  def test_sample(self):
      """2つの整数の合計値を取得できる"""
      with self.subTest():
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(1,2), 4)
        self.assertEqual(add(3,3), 6)

if __name__ == '__main__':
  unittest.main()

"""
subTest(msg=None, **params)
msg     :テスト失敗時に表示させるメッセージを文字列で指定する
**params:テスト失敗時に表示させるパラメータを指定する。for文のループカウンター、テストデータの内容など、エラーの原因調査がしやすくなる値を指定する

通常のfor文だけでアサーションメソッドを使うと、1つのめのテストで失敗したときに、2つ目以降が検証できない
→subTest()を使うことで、各テストが「独立した小テスト」となり、途中で失敗しても全てテストを検証できる
"""