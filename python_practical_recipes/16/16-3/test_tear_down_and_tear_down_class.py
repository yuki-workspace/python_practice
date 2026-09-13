import unittest

class TearDownAndTearDownClassTest(unittest.TestCase):
  def tearDown(self):
    print('teatDown実行')

  @classmethod
  def tearDownClass(cls):
      print('teatDownClass実行')

  def test_example1(self):
      print('teat_example1実行')

  def test_example2(self):
        print('teat_example2実行')

if __name__ == '__main__':
  unittest.main()


"""
tearDown()    : テストメソッドが実行されたあとに呼び出される。
                このメソッドは、テストの結果にかかわらずsetUp()が成功した場合にのみ呼ばれる。

tearDown()    : クラス内に定義されたテストが実行されたあとに1回だけ呼び出されるクラスメソッド。
                クラスを唯一の引数としてとり、classmethod()でデコレートされている必要がある。
"""