# Audrey Young and Norah Redgate 
# 1/11/2024
# To-Do List

# Function
grocerylist = []
# Adds item to the list
def additem():
    addeditem = input("What item do you want to add? ")
    grocerylist.append(addeditem)
    print(grocerylist)
# Prints the current items in the list
def viewlist():
    print(grocerylist)
# Marks an item as purchased
def completedtask():
    finishedtask = input("Which item did you purchase? ")
    position = int(input("What position is this item in? "))
    finishedtask = "X " + finishedtask
    grocerylist.pop(position)
    grocerylist.insert(position, finishedtask)
    print(grocerylist)
# Removes an item from the list
def removetask():
    position2 = int(input("Which position is the item you want to remove in? "))
    grocerylist.pop(position2)
    print(grocerylist)
# Removes all items from the list
def removeall():
    grocerylist.clear()
# Sorts the list alphabetically 
def sortalpha():
    grocerylist.sort()
    print(grocerylist)
# Prints the number of items in the list 
def numberofitems():
    print(len(grocerylist))
# Combines all of the functions to create a custom grocery list
def finallist():
    print("Welcome to your Grocery List: Pick and option 1-5")
    print("1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list \n5. Exit the program \n6. Remove all items \n7. Sort the items alphabetically \n8. Print the number of items on the list")
    option = int(input("Option: ")) 
    if (option == 1):
        additem()
    if (option == 2):
        viewlist()
    if (option == 3):
        completedtask()
    if (option == 4):
        removetask()
    if (option == 5):
        quit()
    if (option == 6):
        removeall()
    if (option == 7):
        sortalpha()
    if (option == 8):
        numberofitems()
    else:
        print("Can't be completed")
    again = input("Would you like to keep editing? ")
    if (again == "yes"):
        finallist()
    else:
        quit()
    
# Main
finallist()