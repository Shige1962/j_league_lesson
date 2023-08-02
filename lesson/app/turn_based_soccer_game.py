class Game:
    def __init__(self):
        self.scores = {"Player 1": 0, "Player 2": 0}
        self.position = 0
        self.current_player = "Player 1"

    def switch_player(self):
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"

    def take_turn(self, offense, defense):
        if offense == "パス":
            if defense == "インターセプト":
                self.position = 0
            else:
                self.position += 1
        elif offense == "ドリブル":
            if defense == "タックル":
                self.position = 0
            else:
                self.position += 1
        elif offense == "シュート":
            if defense == "カバー" or self.position < 2:
                self.position = 0
            else:
                self.scores[self.current_player] += 1
                self.position = 0
        else:
            print("不正なアクションです。")

    def print_status(self):
        print("スコア: ", self.scores)
        print("ポジション: ", self.position)

offensive_actions = ["パス", "ドリブル", "シュート"]
defensive_actions = ["カバー", "タックル", "インターセプト"]

game = Game()

for _ in range(10):
    print(game.current_player + "の攻撃ターンです。")
    offensive_choice = input("攻撃のアクションを選んでください（パス/ドリブル/シュート）: ")
    defensive_choice = input("守備のアクションを選んでください（カバー/タックル/インターセプト）: ")

    game.take_turn(offensive_choice, defensive_choice)
    game.print_status()
    game.switch_player()

print("ゲーム終了！最終スコアは", game.scores, "です。")


# このゲームでは、攻撃側と守備側がそれぞれアクションを選び、それに基づいてボールの位置とスコアが更新されます。
# 攻撃側が「パス」または「ドリブル」を選んだ場合、守備側が適切なアクション（「インターセプト」または「タックル」）を選ばなければボールは前進します。
# 攻撃側が「シュート」を選んだ場合、守備側が「カバー」を選んだり、攻撃側が十分な位置からシュートを打っていなければ、ゴールが決まります。
# ゲームは10ターン行われ、それぞれのターンで攻撃側と守備側の選択、そしてその結果が表示されます。