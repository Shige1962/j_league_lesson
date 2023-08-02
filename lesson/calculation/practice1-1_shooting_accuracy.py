player_a_number = 10
player_a_name = "田中"

print("選手の名前: " + player_a_name + ", 背番号: " + str(player_a_number))

# 選手Aのゴール数とショット数を設定
player_a_goals = 8
player_a_shots = 10

# 選手Aのゴール成功率を計算
player_a_goal_rate = player_a_goals / player_a_shots * 100  # パーセント表示にするために100を掛けます。

print(player_a_name + "選手のゴール成功率は、" + str(player_a_goal_rate) + "%です。")



# このコードでは、選手Aが10ショット中8ゴールを決めた場合のゴール成功率を計算しています。
# ゴール成功率は、「決めたゴールの数」を「ショットの総数」で割り、その結果に100を掛けることで得られます。


# ステップアップ（round関数を入れて数値を見やすくしよう）

# print(player_a_name + "選手のゴール成功率は、" + str(round(player_a_goal_rate, 2)) + "%です。")

