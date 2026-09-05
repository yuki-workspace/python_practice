"""
与えられた引数について、a/bを行う関数です

>>> div(5,2)
2.5
"""

def div(a,b):
  """
  答えは小数で返ってきます

  >>> [div(n,2) for n in range(5)]
  [0.0, 0.5, 1.0, 1.5, 2.0]

  第2引数がゼロだったときは、ゼロ除算エラーが発生します

  >>> div(1,0)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in div
  ZeroDivisionError: division by zero
  """

  return a/b

if __name__ == "__main__":
  import doctest
  doctest.testmod()

# python3 -m doctest -v sample_doctest.py
# 上記コマンドで、doctest.testmod()を書いてなくても、doctestをコマンドラインで実行できる