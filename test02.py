import random

# 乱数のシードを設定する。これにより、コードの実行結果を再現可能にする。
random.seed(42)  # 任意のシード値を設定

# 0から100までのランダムな整数を生成
random_number = random.randint(0, 100)

# 生成したランダムな数を出力
print(f"生成されたランダムな数: {random_number}")