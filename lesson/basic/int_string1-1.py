# このコードでは、 player_a_number は int 型なので、それを string 型に変換する必要があります（str(player_a_number)）。
# これは、Pythonでは文字列と整数を直接結合することができないからです。したがって、整数を文字列に変換することで、それらを結合して出力できます。

player_a_number = 10
player_a_name = "田中"

print("選手の名前: " + player_a_name + ", 背番号: " + str(player_a_number))
