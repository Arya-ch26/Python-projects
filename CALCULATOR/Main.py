try:
    a=int( input("Enter first number: "))
    b=int( input("Enter second number: "))
    print("What kind of operation do you want to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation=input("Enter the operation you want to perform: ")

    match operation:
        case "1":
            print(f"Addition is {a + b}")
        case "2":
            print(f"Subtraction is {a - b}")
        case "3":
            print(f"Multiplication is { a * b}")
        case "4":
            print(f"Division is {a / b}")
        case default:
            print("Invalid operation")

except Exception as e:
    print("Enter correct value of a and b:", e)
    