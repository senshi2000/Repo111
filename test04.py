def add(x, y):
  """足し算を行う関数"""
  return x + y

def subtract(x, y):
  """引き算を行う関数"""
  return x - y

while True:
  print("1. 足し算")
  print("2. 引き算")
  print("3. 終了")

  choice = input("選択してください(1/2/3): ")

  if choice == '3':
    break

  try:
    num1 = float(input("最初の数字を入力してください: "))
    num2 = float(input("2番目の数字を入力してください: "))
    if choice == '2' and num2 == 0:
      print("ゼロ除算エラーです。")
      continue
  except ValueError:
    print("無効な入力です。数字を入力してください。")
    continue
  except Exception as e:
    print(f"エラーが発生しました: {e}")
    continue

  if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
  elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
  else:
    print("無効な選択です。")
