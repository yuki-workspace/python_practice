import traceback
import logging

logging.basicConfig(filename='example2.log',format='%(asctime)s %(levelname)s %(message)s')

try:
  tuple()[0]
except IndexError as e:
  # t = list(traceback.TracebackException.from_exception(e).format())
  t = "".join(traceback.TracebackException.from_exception(e).format())
  logging.error(t)
  raise
