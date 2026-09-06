import unittest

class SetUpAndSetUpClassTest(unittest.TestCase):
  def setUp(self):
    print('setUp実行')

  @classmethod
  def setUpClass(cls):
    print('setUpClass実行')

  def test_example1(self):
    print('test_example1実行')

  def test_example2(self):
      print('test_example2実行')

if __name__ == '__main__':
  unittest.main()

"""
setUp()       ：テストフィクスチャの準備のためのメソッド。テストメソッドを実行する直前に呼び出される
                →各テストごとに、テスト環境をまっさらにしたいときに使う

setUpClass()  ：クラス内に定義されたテストが実行される前に1回だけ呼び出されるクラスメソッド。
                クラスを唯一の引数として取り、classmethod()でデコレートされている必要がある。
                →重い準備を1回だけやるために使う
"""