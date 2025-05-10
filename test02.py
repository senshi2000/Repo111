import random

class RandomNumberGenerator:
    def __init__(self, seed=None):
        self.seed = seed
        if self.seed:
            random.seed(self.seed)

    def generate(self):
        return random.randint(1, 10)

    def generate_multiple(self, num):
        return [self.generate() for _ in range(num)]

# 例としてシード値を設定し、乱数を生成して出力します。
generator = RandomNumberGenerator(seed=42)
print(f"生成された乱数: {generator.generate()}")
print(f"生成された乱数(複数): {generator.generate_multiple(5)}")
