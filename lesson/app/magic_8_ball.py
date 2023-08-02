import random

def magic_eight_ball():
    responses = [
        "確かにそうだ",
        "間違いなくそうだ",
        "はい、間違いない",
        "見通しは良好",
        "おそらくそうだ",
        "もう一度聞いてみて",
        "あとで再度質問して",
        "それについては教えてくれない",
        "今すぐ言うことはできない",
        "予測できない",
        "集中して再度質問して",
        "信じられない",
        "私の答えはノー",
        "見通しはあまり良くない",
        "とても疑わしい"
    ]

    print("マジックエイトボールに質問をしてください:")
    question = input()
    print("あなたの質問は: ", question)
    print("マジックエイトボールの答えは: ", random.choice(responses))

magic_eight_ball()

