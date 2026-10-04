import logging
import contextvars
import threading
import time
import random

# ── 1. 文脈変数：スレッドごとに別々の request_id を保持 ──
request_id_var = contextvars.ContextVar("request_id", default="-")

# ── 2. 注入フィルター：全ログに今の文脈の request_id を差し込む ──
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get()
        return True

# ── 3. ロガー設定（1回だけ）──
logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(request_id)s] %(message)s", datefmt="%H:%M:%S"))
handler.addFilter(ContextFilter())
logger.addHandler(handler)
logger.propagate = False

# ── 4. 登録処理（各所は本文だけ書く。req_id は一切書かない）──
def register_user(name):
    logger.info(f"登録開始: {name}")
    time.sleep(random.uniform(0.01, 0.05))   # DB待ちを模擬（この隙に他リクエストのログが割り込む）
    logger.info("DBにINSERT")
    time.sleep(random.uniform(0.01, 0.05))
    logger.info(f"登録完了: {name}")

# ── 5. 1リクエスト = 1スレッド。入口で request_id をセット ──
def handle_request(req_id, name):
    request_id_var.set(req_id)               # ← このリクエストの ID を文脈にセット
    register_user(name)

print("=== 3リクエストを同時に処理（ログは時系列で入り混じる）===\n")
threads = [
    threading.Thread(target=handle_request, args=("req-A", "suzuki")),
    threading.Thread(target=handle_request, args=("req-B", "tanaka")),
    threading.Thread(target=handle_request, args=("req-C", "sato")),
]
for t in threads: t.start()
for t in threads: t.join()

print("\n=== req-B だけ抜き出すとこうなる（後からの追跡）===\n")
# 実運用では grep req-B app.log に相当