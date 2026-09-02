# 3.5.1
# 例1-1 内包表記する前
number_list=[]

for i in range(10):
  number_list.append(i**2)

print(f"通常の表記：{number_list}")
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 例1-2 内包表記した後
number_list = [i**2 for i in range(10)]
print(f"内包表記：{number_list}")

# 例2　if文で偶数だけリストに追加
number_list = [i**2 for i in range(10) if i % 2 == 0]
print(f"内包表記：{number_list}")

# 例3-1 ネストしたリストの内包表記
drinks = ['coffee', 'tea', 'Espresso']
sizes = ['S', 'M', 'L']
menu = [(drink, size) for drink in drinks for size in sizes]
print(menu)

# 例3-2 for文で書いた場合
menu=[]
for drink in drinks:
  for size in sizes:
    menu.append((drink, size))

print(menu)
