# enhance to prevent duplicates
# display contents of list
# loop to remove items in list or "" to exit

shoppingList = ["Milk","Eggs","Chicken"]

dadCart = ["Milk","Soda","Cookies","Cake","ColdCuts","Beer","Chips"]

while True:
    item = input("Enter the item to add to the shopping list (leave blank and press Enter to finish): ")
    #break loop
    if item == "":
        break
    elif item not in shoppingList:
            shoppingList.append(item) #add item to the end
            # shoppingList.insert(2, item) #add item at index location


while True:
    item = input("Enter the item to remove from the shopping list (leave blank and press Enter to finish): ")
    #break loop
    if item == "":
        break
    elif item in shoppingList:
            shoppingList.remove(item) #remove item to the end


print(shoppingList)

print("For Each Listing")
for item in shoppingList:
    print(item)

