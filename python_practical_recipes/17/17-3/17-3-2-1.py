# import traceback
import logging

logging.basicConfig(filename='example.log',format='%(asctime)s %(levelname)s %(message)s')

try:
  tuple()[0]
except IndexError:
  logging.exception("インデックスエラー発生")  # traceback は自動で付く
  raise
