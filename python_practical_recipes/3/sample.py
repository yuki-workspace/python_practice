import csv

try:
  input_file_name=input('Enter file_name')
  with open(input_file_name, mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
      population_density=float(row[1] / float(row[2]))
      print(f'{row[0]}の人口密度は{population_density}ですぞ！')
except:
  print('例外が発生しました')