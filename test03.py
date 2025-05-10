import random
import json
import os

class Omikuji:
    def __init__(self, data_file="omikuji.json"):
        self.omikuji = {}
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, data_file)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.omikuji = json.load(f)
        except FileNotFoundError:
            print(f"エラー: おみくじデータファイル '{file_path}' が見つかりません。")
        except json.JSONDecodeError as e:
            print(f"エラー: おみくじデータファイル '{file_path}' の読み込みに失敗しました。: {e}")
        except Exception as e:
            print(f"エラー: おみくじデータファイル '{file_path}' の処理中に予期せぬエラーが発生しました。: {e}")


    def draw(self):
        if not self.omikuji:
            return "おみくじデータがありません。データファイルを確認してください。"
        result = random.choice(list(self.omikuji.keys()))
        message = self.omikuji[result]
        if result == "超凶":
            message += "\n超凶が出た場合は、すぐに神社にお参りに行きましょう！"
        return f"あなたの運勢は…{result}！\n{message}"

omikuji = Omikuji()
print(omikuji.draw())
