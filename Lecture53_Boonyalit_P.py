def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

print("Vat Calculate")
inputPrice = int(input("Price : "))
print("Total price =", vatCalculate(inputPrice))