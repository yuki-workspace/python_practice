# 3.5.3

"""
Pythonには、map()やfilter()といった組み込み関数がある
内包表記を使うことで、それらの組み込み関数と同様かつ、より可読性が高いコードを書ける

map()   ：リストなどの各要素に何らかの関数を適用し、別のオブジェクトを作成する関数
filter()：リストなどの各要素に何らかの関数を適用し、関数の戻り値がTrueとなる要素だけからなるオブジェクトを作成する関数
"""

# map() → 内包表記へ置き換えた例
arr = [1.4, 2.0, 3.5, 2.25, 1.98]
arr2 = list(map(round, arr))
print(arr2)

# 内包表記だと以下
arr2 = [round(n) for n in arr]
print(arr2)

# filter() → 内包表記へ置き換えた例
arr3 = list(map(round, filter(lambda n:n > 2, arr)))
print(arr3)

# 内包表記だと以下
arr2 = [round(n) for n in arr if n > 2]
print(arr2)