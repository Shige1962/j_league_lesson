import random

def draw_lottery():
    results = ["大吉", "中吉", "吉", "凶", "大凶"]
    return random.choice(results)

print("おみくじを引きます...")
result = draw_lottery()
print("あなたの運勢は... {} です！".format(result))
