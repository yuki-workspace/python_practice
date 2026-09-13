import logging
import sys
import warnings
from pathlib import Path

def test_capsys(capsys):
  print('hello')                    # 標準出力に'hello\n'が出力される
  print('error', file=sys.stderr)   # 標準エラー出力に'error\n'が出力される

  captured = capsys.readouterr()    # キャプチャされた標準出力、標準エラー出力を取得
  assert captured.out == 'hello\n'  # キャプチャされた標準出力の内容を確認
  assert captured.err == 'error\n'  # キャプチャされた標準エラー出力の内容を確認

def test_caplog(caplog):
  caplog.set_level(logging.ERROR)   # キャプチャするログレベルをERRORに変更
  logging.error('error')            # ERRORレベルのログを出力
  assert 'error' in caplog.messages # ERRORレベルのログメッセージがキャプチャされている

  # caplog.messagesにキャプチャされたログメッセージがリストで格納されている
  caplog.set_level(logging.INFO)    # キャプチャするログレベルをINFOに変更
  logging.info('info')              # INFOレベルのログを出力
  assert 'info' in caplog.messages  # INFOレベルのログメッセージがキャプチャされている

def depricated_func():
  warnings.warn(DeprecationWarning('this is deprecated'))
  # 非推奨の関数である旨の警告メッセージを出力

def test_recwarn(recwarn):
  depricated_func()                                   # テスト対象の関数を実行

  assert len(recwarn) == 1                            # リストのように出力された警告の数をlen関数で確認できる
  w = recwarn.pop(DeprecationWarning)                 # DeprecationWarningを指定した警告メッセージがある場合、popメソッドで取り出せる
  assert issubclass(w.category, DeprecationWarning)
  assert str(w.message) == 'this is deprecated'       # 出力された警告メッセージを確認できる

def test_tmp_path(tmp_path):
  assert isinstance(tmp_path, Path) # tmp_pathはpathlib.Pathオブジェクト

  # pathlib.Pathを使って、ディレクトリ、ファイルの操作ができる
  p = tmp_path / "test"
  p.mkdir()
  p = p / 'test.txt'
  p.write_text('hello')
  # テスト関数の実行が終わると、tmp_pathで作られたディレクトリは削除される