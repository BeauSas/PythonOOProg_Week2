todolist = []
endAction = 'n'
removeInput = None

def MakeTodoList():
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
    print()

def EraseItem():
    print()
    print(todolist)
    removeInput = int(input("What item should be removed? (give ID number): "))
    todolist.pop(removeInput-1)
    print()
    print(todolist)
    print()