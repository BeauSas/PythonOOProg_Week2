def MakeTodoList():
    todolist = []
    endAction = 'n'
    loopAction = None
    loopCount = 0

    while loopAction != endAction:
        loopCount += 1
        item_name = input("Describe your item: ")
        item_deadline = input("What is the deadline date?: ")

        listItems = {
            "Item_ID": loopCount,
            "Item_Name": item_name,
            "Item_Deadline": item_deadline
        }
        todolist.append(listItems)
        print()
        loopAction = input("Add another item? (y/n): ")

    print(todolist)