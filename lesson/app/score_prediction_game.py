import random

# ユーザーにスコアを予想させます。
team1_prediction = int(input("チーム1のゴール数を予想してください: "))
team2_prediction = int(input("チーム2のゴール数を予想してください: "))

# ランダムにスコアを生成します。0から5までのゴール数を想定します。
team1_actual = random.randint(0, 5)
team2_actual = random.randint(0, 5)

# ユーザーの予想と実際のスコアを表示します。
print("あなたの予想: チーム1 " + str(team1_prediction) + " - " + str(team2_prediction) + " チーム2")
print("実際のスコア: チーム1 " + str(team1_actual) + " - " + str(team2_actual) + " チーム2")

# ユーザーの予想が当たったかどうかを判断します。
if team1_prediction == team1_actual and team2_prediction == team2_actual:
    print("素晴らしい！あなたの予想は完全に当たりました！")
elif team1_prediction == team1_actual or team2_prediction == team2_actual:
    print("良い試みです！一部の予想が当たりました！")
else:
    print("残念ながら、あなたの予想は外れました。また挑戦してみてください！")

# このゲームでは、ユーザーが2つのチームのスコアを予想します。
# その後、Pythonがランダムにスコアを生成し、ユーザーの予想が当たったかどうかを判断します。