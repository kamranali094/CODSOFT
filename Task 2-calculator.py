def main():

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
         return x / y
        else:
            return "Cannot divide by zero"
    print("Welcome to Calculator")
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operate = input(":")

    if operate == '1':
        print(add(num1,num2))
    elif operate == '2':
        print(subtract(num1,num2))
    elif operate == '3':
        print(multiply(num1,num2))
    elif operate == '4':
        print(divide(num1,num2))
    else:
        print("Invalid input. Please enter a valid choice.")
    print("you have any other calculation")
    print("y. Yes")
    print("n. No")
    rep=input(":")
    if rep=="y":
        main()
main()

