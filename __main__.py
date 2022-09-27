from todo_app import todo

def main():

    print("1. Add item to list.")
    print("2. Remove item from list.")
    print("3. Quit.")
    print()
    menuChoice = int(input("Your choice: "))
    if menuChoice == 1:
        todo.MakeTodoList()
        main()
    elif menuChoice == 2:
        todo.EraseItem()
        print("Check_2")
        main()
    elif menuChoice == 3:
        None
    else:
        main()

if __name__ == "__main__":
    main()