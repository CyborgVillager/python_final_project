import csv


class item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class store:
    def __init__(self):
        self.itemList = {}

    def __init__(self, itemList):
        self.itemList = itemList

    def listItems(self):
        print("Name    --     Price")
        for key, value in self.itemList.items():
            print(key + "    --     " + value[0])

    def updateItemQuantity(self, name, amount, operation):
        if (operation == 'd'):
            self.itemList[name][1] = (str(int(self.itemList[name][1]) - 1))
        elif (operation == 'i'):
            self.itemList[name][1] = (str(int(self.itemList[name][1]) + 1))

    def addItem(self, item):
        result = False
        if (item.name in self.itemList):
            self.itemList[item.name][1] = (str(int(self.itemList[item.name][1]) + int(item.quantity)))
            result = True
        else:
            self.itemList[item.name] = [item.price, item.quantity]
            result = True

        return result

    def removeItem(self, item):
        result = False
        if (item.name in self.itemList):

            if (int(self.itemList[item.name][1]) > int(item.quantity)):
                self.itemList[item.name][1] = (str(int(self.itemList[item.name][1]) - int(item.quantity)))
                result = True
            elif (int(self.itemList[item.name][1]) == int(item.quantity)):
                self.itemList.pop(item.name)
                result = True

        return result

    def updateStoreAfterCheckout(self, itemList):
        for key, value in itemList.items():
            tempItem = item(key, value[0], value[1])
            self.removeItem(tempItem)


class cart:
    def __init__(self):
        self.itemList = {}

    def __init__(self, itemList):
        self.itemList = itemList

    def listItems(self):
        print("Name    --     Price    --     Quantity")
        for key, value in self.itemList.items():
            print(key + "    --     " + value[0] + "    --     " + value[1])

    def addItem(self, itemList, item):
        result = False
        reason = 0
        if (item.name in itemList):
            if (int(itemList[item.name][1]) >= int(item.quantity)):
                if (item.name in self.itemList):
                    if (int(self.itemList[item.name][1]) + int(item.quantity) <= int(itemList[item.name][1])):
                        self.itemList[item.name][1] = (str(int(self.itemList[item.name][1]) + int(item.quantity)))
                        result = True
                    else:
                        reason = 2
                else:
                    self.itemList[item.name] = [itemList[item.name][0], item.quantity]
                    result = True

            else:
                reason = 2
        else:
            reason = 1
        return result, reason

    def removeItem(self, item):
        result = False
        reason = 0
        if (item.name in self.itemList):

            if (int(self.itemList[item.name][1]) > int(item.quantity)):
                self.itemList[item.name][1] = (str(int(self.itemList[item.name][1]) - int(item.quantity)))
                result = True
            elif (int(self.itemList[item.name][1]) == int(item.quantity)):
                self.itemList.pop(item.name)
                result = True
            else:
                reason = 2

        else:
            reason = 1
        return result, reason

    def checkout(self):
        subTotal = 0.0
        for key, value in self.itemList.items():
            subTotal = subTotal + (float(value[0]) * float(value[1]))

        return subTotal


reader = csv.reader(open('products.csv', 'r'))
storeDict = {}
for row in reader:
    product_csv_info, version0, version1 = row
    storeDict[product_csv_info] = [version0, version1]

myStore = store(storeDict)
cartDict = {}
myCart = cart(cartDict)

print("=====================================================================")
print("Welcome to Jonathan\'s Almawi DVD Shop\n")
print("=====================================================================")
run = True
while (run == True):
    print("=====================================================================\n")
    print("--Press 1 for List\n")
    print("--Press 2 for Add\n")
    print("--Press 3 for Cart\n")
    print("--Press 4 for Remove\n")
    print("--Press 5 for Checkout\n")
    print("--Press 6 for Exit\n")

    if (userinput == "6"):
    print("=====================================================================")
    userinput = input("Enter your choice: ")
        run = False
        filename = "products.csv"
        with open(filename, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in myStore.itemList.items():
                writer.writerow([key, value[0], value[1]])
    elif (userinput == "1"):
        print("-------------------------------------------------------------------")
        myStore.listItems()
    elif (userinput == "2"):
        print("-------------------------------------------------------------------")
        nameinput = input("Enter the name of item: ")
        quantityinput = input("Enter the quantity of item: ")
        print("-------------------------------------------------------------------")
        result = myCart.addItem(myStore.itemList, item(nameinput, '', quantityinput))
        if (result[0] == False):
            if (result[1] == 1):
                print("Invalid Item Selected")
            if (result[1] == 2):
                print("Not enough stock available")

        else:
            print("Item Added succesfully")
        print("-------------------------------------------------------------------")
    elif (userinput == "3"):
        print("-------------------------------------------------------------------")
        myCart.listItems()
    elif (userinput == "4"):
        print("-------------------------------------------------------------------")
        nameinput = input("Enter the name of item: ")
        quantityinput = input("Enter the quantity of item: ")
        print("-------------------------------------------------------------------")
        result = myCart.removeItem(item(nameinput, '', quantityinput))
        if (result[0] == False):
            if (result[1] == 1):
                print("Invalid Item Selected")
            if (result[1] == 2):
                print("Not enough items in cart")

        else:
            print("Item Removed succesfully")
        print("-------------------------------------------------------------------")

    elif (userinput == "5"):
        print("-------------------------------------------------------------------")
        subTotal = myCart.checkout()
        tax = subTotal * 0.7

        print("Your subTotal is: " + str(subTotal))
        print("Your tax amount is: " + str(tax))
        total = subTotal + tax
        print("Total Amount is: " + str(total))
        myStore.updateStoreAfterCheckout(myCart.itemList)

    else:
        print("***************")
        print("\n**Wrong Input**\n")
        print("***************")

















