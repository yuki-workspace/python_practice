from datetime import datetime
import unittest

import freezegun

class ExampleTest(unittest.TestCase):
  @freezegun.freeze_time('2021-01-01 00:00:00')
  def test_example1(self):
    self.assertEqual(datetime.utcnow(), datetime(2021, 1,1,0,0,0))

  def test_example2(self):
    with freezegun.freeze_time('2021-01-01 00:00:00'):
      self.assertEqual(datetime.utcnow(), datetime(2021, 1,1,0,0,0))

if __name__ == '__main__':
  unittest.main()
