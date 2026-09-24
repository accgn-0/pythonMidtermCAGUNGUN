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

if chooseOpt == opt1:
    def itemName:

    def quantSold:

    def price:

    quantSold = int((input('Quantity Sold: ')))
    price = float(input('Price Per Unit: '))

    if itemName == 0:
        print("Item Name must not be a number")
        exit()
    if itemName == -1:
        print("Item Name must not be in negative")
        exit()
    else:
        print(str(itemName))



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


totalAmount = quantSold * price
print(totalAmount)


# open('sales_log.txt', 'r')
'''