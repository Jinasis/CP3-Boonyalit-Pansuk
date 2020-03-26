menuList = []
priceList = []

while True:
    menuName = input("Pleas Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    totalPrice = 0
    print("My Food".center(21,"-"))
    for number in range(len(menuList)):
        totalPrice = totalPrice + int(priceList[number])
        print(menuList[number], priceList[number])
    print("Total Price =", totalPrice)

showBill()
