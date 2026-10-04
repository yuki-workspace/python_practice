import traceback

def foo():
  raise IOError('foo')

def bar():
  try:
    foo()
  except IOError:
    raise RuntimeError('bar') from None

try:
  bar()
except RuntimeError:
  traceback.print_exc(chain=True)
