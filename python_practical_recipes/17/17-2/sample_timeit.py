import timeit

# ── 測定対象の3つの実装 ──
def use_loop():
    result = []
    for n in range(1000):
        result.append(n * 2)
    return result

def use_comprehension():
    return [n * 2 for n in range(1000)]

def use_map():
    return list(map(lambda n: n * 2, range(1000)))

# ── 各方法を測定(number回まとめて実行 × repeat回繰り返す) ──
methods = ["use_loop", "use_comprehension", "use_map"]

for name in methods:
    times = timeit.repeat(
        f"{name}()",
        setup=f"from __main__ import {name}",
        repeat=5,
        number=10000
    )
    print(f"{name:20s}: {min(times):.4f} 秒 (10000回×5セットの最小値)")