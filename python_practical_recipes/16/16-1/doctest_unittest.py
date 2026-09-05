import unittest
import doctest
import sample_doctest

"""このコードは、doctest を unittest の枠組みに合流させる書き方"""

def load_tests(loader, tests, ignore):
  tests.addTests(doctest.DocTestSuite(sample_doctest))
  return tests

if __name__ == "__main__":
    unittest.main()

"""
このコードは、doctest を unittest の枠組みに合流させる書き方
"""

"""
テキストファイルでのdoctestの場合

def load_tests(loader, tests, ignore):
  tests.addTests(doctest.DocFileSuite("sample_doctest.txt"))
  return tests

if __name__ == "__main__":
    unittest.main()
"""