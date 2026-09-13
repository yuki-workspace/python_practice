import os
import pytest

@pytest.fixture
def is_ci():
  """
  CIサーバ上でテストを実行していればTrueを返す
  環境変数CIに'true'が設定されていればCIサーバ上で実行しているとみなす
  """

  ci = os.environ.get('CI', 'false')
  return ci == 'true'
  