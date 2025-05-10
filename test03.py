import random

class Omikuji:
    def __init__(self):
        self.omikuji = {
            "大吉": "運命の女神が微笑む！黄金の未来があなたを待っています！",
            "中吉": "幸運の波に乗れ！願望成就のチャンス到来です！",
            "小吉": "順風満帆、着実に前進を！小さな成功が大きな喜びに繋がります。",
            "吉": "現状維持は成功への道！新たな挑戦も視野に入れ、着実に歩みましょう。",
            "凶": "試練の時、冷静さを保て！困難を乗り越えれば、大きな成長が待っています！"
        }

    def draw(self):
        result = random.choice(list(self.omikuji.keys()))
        return f"あなたの運勢は…{result}！\n{self.omikuji[result]}"

omikuji = Omikuji()
print(omikuji.draw())
