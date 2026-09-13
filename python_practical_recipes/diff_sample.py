import difflib
import logging
from pathlib import Path

# テキストファイルの作成（A）
old_file = Path('old_file.txt')
old_file.write_text("first_write", encoding="utf-8")
old_text = old_file.read_text()

# テキストファイルの更新（B）
# shutil.copy(old_file, "new_file.txt")
new_file = Path("new_file.txt")
new_file.write_text("second_write", encoding="utf-8")
new_text = new_file.read_text()

# AとBの差分のログ化
def log_authz_diff(old_text:str, new_text:str):
  logging.basicConfig(level=logging.INFO)
  diff = difflib.ndiff(old_text.splitlines(), new_text.splitlines())

  # diff_lines = list(diff)
  Path("log.txt").write_text('\n'.join(diff), encoding="utf-8")

  """
  if not diff_lines:
    logging.info('authz更新:差分なし')
  else:
    logging.info('authz更新:差分あり\n' + '\n'.join(diff_lines))
  """

log_authz_diff(old_text, new_text)