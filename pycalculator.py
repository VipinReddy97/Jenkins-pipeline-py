# Simple calculator application that supports addition, subtraction and product of two positive integers

# This function adds two numbers
def add(x, y):
    if x <= 0 or y <= 0:
        print("Only positive integers allowed in this calculator:")
        return
    else:
        return x + y


# This function subtracts two numbers
def subtract(x, y):
    if x <= 0 or y <= 0:
        print("Only positive integers allowed in this calculator:")
        return
    else:
        return x - y


# This function multiplies two numbers
def multiply(x, y):
    if x <= 0 or y <= 0:
        print("Only positive integers allowed in this calculator:")
        return
    else:
        return x * y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")


while True:

    choice = input("Enter choice(1/2/3): ")
# Check if choice is one of the four options
    if choice in ('1', '2', '3'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            break
    else:
        print("Invalid Input")
