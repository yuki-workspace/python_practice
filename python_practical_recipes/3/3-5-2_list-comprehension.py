# 3.5.2

"""
内包表記は、集合・辞書・ジェネレーター式でも使用できる

集合内包表記：set型の値を生成する
辞書内包表記：dict型の値を生成する
ジェネレーター式：ジェネレーターオブジェクトを生成する
"""

# 集合内包表記：set型の値を生成する
val = [i**2%10 for i in range(10)]
print(val)

# {}に変えると、set型（重複なし）の値を生成する
val = {i**2%10 for i in range(10)}
print(val)

# 辞書内包表記：dict型の値を生成する
# キーとバリューのペア（:でつなぐ）を、{}で囲む
val = {i: i**2 for i in range(5)}
print(val)

# ジェネレーター式：ジェネレーターオブジェクトを生成する
"""
あとで実施する
g = (i**2 for i in range(5))
type(g)
<class 'generator'>
"""

