userName = input("User Name : ")
passWord = input("Password : ")
if userName == "admin" and passWord == "1234":
    print("Welcome to ABC Shop")
    print("Product List")
    print("1. Apple", "  -----10----- THB")
    print("2. Banana", " -----15----- THB")
    print("3. Orange", " -----10----- THB")
    print("You can choose more than one product.")
    print("Example 12 or 123 etc.")
    customerChoose = input("What number of products do you want? : ")
    if customerChoose == "1":
        numberOfApple = int(input("How many Apples do you want? : "))
        price = numberOfApple*10
        print("Total price (THB) : ", price)

    elif customerChoose == "2":
        numberOfBanana = int(input("How many Bananas do you want? : "))
        price = numberOfBanana * 15
        print("Total price (THB) : ", price)

    elif customerChoose == "3":
        numberOfOrange = int(input("How many Oranges do you want? : "))
        price = numberOfOrange * 10
        print("Total price (THB) : ", price)

    elif customerChoose == "12":
        numberOfApple = int(input("How many Apples do you want? : "))
        numberOfBanana = int(input("How many Bananas do you want? : "))
        price = numberOfApple*10 + numberOfBanana*15
        print("Total price (THB) : ", price)

    elif customerChoose == "13":
        numberOfApple = int(input("How many Apples do you want? : "))
        numberOfOrange = int(input("How many Oranges do you want? : "))
        price = numberOfApple*10 + numberOfOrange*10
        print("Total price (THB) : ", price)

    elif customerChoose == "123":
        numberOfApple = int(input("How many Apples do you want? : "))
        numberOfBanana = int(input("How many Bananas do you want? : "))
        numberOfOrange = int(input("How many Oranges do you want? : "))
        price = numberOfApple * 10 + numberOfBanana * 15 + numberOfOrange * 10
        print("Total price (THB) : ", price)

    else:
        print("Error !")
        print("Please try again")
else:
    print("Error !")





