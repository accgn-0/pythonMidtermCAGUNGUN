# Interactive Menu System
dividerTop = '========================================'
print(dividerTop)
title = '       Sales Record Management System       '
print(title)
dividerMid = '========================================'
print(dividerMid)
opt1 = '1. Add Sale Record'
print(opt1)
opt2 = '2. View All Records & Summary Statistics'
print(opt2)
opt3 = '3. Clear All Sales Data'
print(opt3)
opt4 = '4. Exit System'
print(opt4)
dividerBot = '========================================'
print(dividerBot)

chooseOpt = int(input('Choose a number from the option: '))

# Option 1
if chooseOpt == opt1:
    def itemName():
        userInputItem = str(input("Enter Item Name:"))
            if userInputItem == 0:
                print("Item Name must not be a number")
                exit()
            elif userInputItem == -1:
                print("Item Name must not be in negative")
                exit()
            else:
                print(str(userInputItem))

    def quantSold():
        userInputSold = int(input("Enter Quantity Sold:"))
            if userInputSold == 0:
                print("quantity sold is 0")
            elif userInputSold <= -1:
                print("quantity sold cannot be in negative")
            elif userInputSold > 1:
                print(f"Quantity Sold is {quantSold}")

    def price():
        userInputPrice = float(input("Enter Price Per Unit:"))
            if userInputPrice <= -1:
                print("Price per unit cannot be in negative.")
                exit()

# calculation
totalAmount = quantSold * price
print(totalAmount)

# Opening file
file = open('sales_log.txt', 'r')



'''

if itemName == 0:
    print("Item Name must not be a number")
    exit()
if itemName == -1:
    print("Item Name must not be in negative")
    exit()
else:
    print(str(itemName))



except
    print()
'''