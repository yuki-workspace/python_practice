class MyValidateError(Exception):
  title=None
  detail=None

  def __str__(self):
    return str(self.title)

class MyTypeError(MyValidateError):
  title='Type error'
  detail='数値で入力してください'

class MyMaxError(MyValidateError):
  title='Max error'
  detail='Max 100までの値を入力してください'

def validate_number(num):
  try:
    num=int(num)
  except ValueError:
    raise MyTypeError
  if num > 100:
    raise MyMaxError

try:
  input_number=input('検証する数字を入力してください')
  validate_number(input_number)
except MyValidateError as e:
  print(f'{e}の例外が発生しました')
  print(f'detail={e.detail}')
