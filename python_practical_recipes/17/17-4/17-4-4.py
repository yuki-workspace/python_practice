import logging

# ── 1. Logger（入口・司令塔）───────────────────────────
# 名前付きロガーを取得。レベルは広めに DEBUG まで開けておく。
logger = logging.getLogger("myapp.register")
logger.setLevel(logging.DEBUG)

# ── 4. Filter（選別＋文脈の注入）──────────────────────
# 全ログに request_id という属性を差し込むフィルター。
# filter() が True を返せば通過、False なら捨てる。
class RequestIdFilter(logging.Filter):
    def __init__(self, request_id):
        super().__init__()
        self.request_id = request_id

    def filter(self, record):
        record.request_id = self.request_id   # LogRecord に属性を追加
        return True                            # 常に通す（今回は注入が目的）

# ── 2. Handler（出口）× 2つ ───────────────────────────
# (a) コンソール: INFO 以上だけ、簡潔フォーマット
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# (b) ファイル: DEBUG 以上を全部、詳細フォーマット
filehandler = logging.FileHandler("app.log", mode="w", encoding="utf-8")
filehandler.setLevel(logging.DEBUG)

# ── 3. Formatter（整形）── Handler ごとに変える ────────
console.setFormatter(
    logging.Formatter("[%(levelname)s] %(message)s")
)
filehandler.setFormatter(
    logging.Formatter(
        "%(asctime)s [%(levelname)-7s] %(name)s "
        "(req=%(request_id)s) %(message)s"    # ← Filter が注入した属性を使う
    )
)

# ── 組み立て ──────────────────────────────────────────
logger.addFilter(RequestIdFilter("req-0001"))
logger.addHandler(console)
logger.addHandler(filehandler)

# ── 実際にログを出す ──────────────────────────────────
logger.debug("DBコネクション取得")          # コンソールには出ない(INFO未満) / ファイルには出る
logger.info("ユーザー tanaka の登録開始")
logger.warning("既存ユーザーと名前が近い")
try:
    1 / 0
except ZeroDivisionError:
    logger.error("登録処理でエラー", exc_info=True)  # トレースバックも記録