import tkinter as tk
from random import choice

# マジックエイトボールの回答リスト
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

def ask_magic_eight_ball():
    question = entry.get()
    response = choice(responses)
    response_label.config(text=f"質問: {question}\n回答: {response}")

root = tk.Tk()
root.title("Magic 8 Ball")

label = tk.Label(root, text="マジックエイトボールに質問をしてください:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="質問する", command=ask_magic_eight_ball)
button.pack()

response_label = tk.Label(root, text="")
response_label.pack()

root.mainloop()

