def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234":
        return showMenu()
    else:
        return False

def showMenu():
    print("---Hello----")
    print("Choose 1 = Calculate Vat")
    print("Choose 2 = Calculate Price")
    return menuSelect()

def menuSelect():
    choose = int(input(">> "))
    if choose == 1:
        return vatCalculate(int(input("Price: ")))
    elif choose == 2:
        return priceCalculate()

def vatCalculate(totalPrice):
    vat = 7 / 100
    result = totalPrice + (totalPrice * vat)
    print("Total Price")
    return result

def priceCalculate():
    price1 = int(input("First Product : "))
    price2 = int(input("Second Product : "))
    print("Total Price")
    return vatCalculate(price1 + price2)

print(login())