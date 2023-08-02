def todo_app():
    todo_list = []

    while True:
        print("\n1. ToDoを追加")
        print("2. ToDoを完了")
        print("3. ToDoリストを表示")
        print("4. 終了")

        choice = input("選択してください(1, 2, 3, 4): ")
        
        if choice == '1':
            description = input("追加するToDo: ")
            task = {"description": description, "completed": False}
            todo_list.append(task)
        elif choice == '2':
            description = input("完了するToDo: ")
            for task in todo_list:
                if task["description"] == description:
                    task["completed"] = True
                    break
            else:
                print("そのToDoは存在しません。")
        elif choice == '3':
            if not todo_list:
                print("ToDoリストは空です。")
            else:
                for task in todo_list:
                    status = "完了" if task["completed"] else "未完了"
                    print(f'{task["description"]} - {status}')
        elif choice == '4':
            break
        else:
            print("無効な選択です。再試行してください。")

todo_app()


# このアプリケーションでは、ユーザーはToDoタスクをリストに追加し、完了ステータスを更新し、リスト全体を表示することができます。
# また、ユーザーが指定したToDoタスクがリスト内に存在しない場合は、エラーメッセージが表示されます。
# データはプログラミングが終了すると破棄されるのでデータベースを使用する事で解決されます。