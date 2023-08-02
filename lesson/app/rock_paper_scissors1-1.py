def play_rock_paper_scissors():
    choices = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    
    player1 = input("プレイヤー1, あなたの手は何ですか？（rock, paper, scissors）: ")
    player2 = input("プレイヤー2, あなたの手は何ですか？（rock, paper, scissors）: ")

    if player1 not in choices or player2 not in choices:
        print("無効な選択です。再試行してください。")
    elif player1 == player2:
        print("引き分け！")
    elif choices[player1] == player2:
        print("プレイヤー2が勝ち！")
    else:
        print("プレイヤー1が勝ち！")

play_rock_paper_scissors()