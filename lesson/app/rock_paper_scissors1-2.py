def play_rock_paper_scissors():
    choices = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    winner = None
    
    while winner is None:
        player1 = input("プレイヤー1, あなたの手は何ですか？（rock, paper, scissors）: ").lower()
        player2 = input("プレイヤー2, あなたの手は何ですか？（rock, paper, scissors）: ").lower()

        if player1 not in choices or player2 not in choices:
            print("無効な選択です。再試行してください。")
        elif player1 == player2:
            print("引き分け！再試行してください。")
        elif choices[player1] == player2:
            winner = "プレイヤー2"
        else:
            winner = "プレイヤー1"
    
    print(winner + "が勝ち！")

play_rock_paper_scissors()
