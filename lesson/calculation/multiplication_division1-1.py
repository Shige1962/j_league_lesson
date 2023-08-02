# チケットの値段と販売数
ticket_price = 2000  # 単位: 円
tickets_sold = 5000

# 掛け算: 総収入を計算する
total_income = ticket_price * tickets_sold

# チケットの値段を更新
new_ticket_price = 2500

# 割り算: 新しいチケットの値段で何枚売れば以前と同じ収入を得られるか計算する
tickets_needed = total_income / new_ticket_price

# 結果を表示する
print("総収入：" + str(total_income) + " 円")
print("新しいチケット価格で同じ収入を得るために必要なチケット数：" + str(tickets_needed))


# この例では、チケットの価格と売り上げから総収入を掛け算で計算し、新しいチケット価格で同じ収入を得るために必要なチケット数を割り算で計算しています。


