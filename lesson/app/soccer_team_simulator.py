import random

class Player:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

# プレイヤーリストを作成
players = [
    Player("選手1", random.randint(1, 10)),
    Player("選手2", random.randint(1, 10)),
    Player("選手3", random.randint(1, 10)),
    Player("選手4", random.randint(1, 10)),
    Player("選手5", random.randint(1, 10)),
]

# チームのスキルレベルを計算
team_skill = sum(player.skill for player in players)

# 相手チームのスキルレベルをランダムに決定
opponent_skill = random.randint(5, 50)

print("あなたのチームのスキルレベル: ", team_skill)
print("相手チームのスキルレベル: ", opponent_skill)

# 試合結果を決定
if team_skill > opponent_skill:
    print("おめでとうございます！あなたのチームの勝ちです！")
elif team_skill < opponent_skill:
    print("残念、あなたのチームは敗れました…")
else:
    print("試合は引き分けました。")


# このコードでは、各プレイヤーの「スキル」をランダムに決定し、チーム全体のスキルレベルを計算します。
# 次に、相手チームのスキルレベルもランダムに決定します。
# 最後に、自分のチームと相手チームのスキルレベルを比較して、試合の勝敗を決定します。
