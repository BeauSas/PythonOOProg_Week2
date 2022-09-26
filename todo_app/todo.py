todolist = []
endAction = 'n'
loopAction = None
loopCount = 0
removeInput = None

def MakeTodoList():
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

def EraseItem(): #NOG TOEVOEGEN IN MAIN VIA MENU
    print(todolist)
    removeInput = input("What item should be removed? (give ID number): ")
    todolist.pop(removeInput)