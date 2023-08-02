import random

# シュートの方向をリストで定義します。
directions = ["左", "中央", "右"]

# ユーザーにシュートの方向を予想させます。
keeper_guess = input("シューターがシュートする方向を予想してください（左、中央、右）: ")

# ランダムにシュートの方向を選びます。
shooter_direction = random.choice(directions)

# ユーザーの予想と実際のシュートの方向を表示します。
print("あなたの予想: " + keeper_guess)
print("シューターのシュート方向: " + shooter_direction)

# ユーザーの予想が当たったかどうかを判断します。
if keeper_guess == shooter_direction:
    print("素晴らしい！あなたの予想は正確でした！セーブに成功しました！")
else:
    print("残念ながら、あなたの予想は外れました。ゴールを許してしまいました…")
