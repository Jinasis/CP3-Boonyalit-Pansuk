def plus(x,y):
    print(x+y)
def minus(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)

inputFirstNumber = int(input("First number : "))
inputSecondNumber = int(input("Second number : "))
x = inputFirstNumber
y = inputSecondNumber

print("Plus")
plus(x,y)
print("Minus")
minus(x,y)
print("Multiply")
multiply(x,y)
print("Divide")
divide(x,y)