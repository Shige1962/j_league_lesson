todo_list = []

while True:
    print("\nToDoリスト: ", todo_list)
    print("1. ToDoを追加")
    print("2. ToDoを削除")
    print("3. 終了")

    choice = input("選択してください(1, 2, 3): ")
    
    if choice == '1':
        item = input("追加するToDo: ")
        todo_list.append(item)
    elif choice == '2':
        item = input("削除するToDo: ")
        if item in todo_list:
            todo_list.remove(item)
        else:
            print("そのToDoは存在しません。")
    elif choice == '3':
        break
    else:
        print("無効な選択です。再試行してください。")
