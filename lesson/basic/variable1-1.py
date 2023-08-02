
#以下は変数を使用しないコード

print("選手Aのゴール数：5")
print("選手Bのゴール数：3")

# 以下のケースでは、各選手のゴール数は変数に格納されます。
# なぜこれが便利かと言うと、もし後で選手Aと選手Bのゴール数を更新したい場合、変数の値を更新するだけで済むからです。

player_a_goals = 5
player_b_goals = 3

print("選手Aのゴール数：" + str(player_a_goals))
print("選手Bのゴール数：" + str(player_b_goals))


# 例えば、選手Aがさらにゴールを決めた場合、以下のようにコードを更新できます。

player_a_goals = player_a_goals + 1

print("選手Aのゴール数：" + str(player_a_goals))
print("選手Bのゴール数：" + str(player_b_goals))
