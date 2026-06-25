while True:

    print("\nSimple Calculator")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result =", a + b)

    elif choice == 2:
        print("Result =", a - b)

    elif choice == 3:
        print("Result =", a * b)

    elif choice == 4:
        print("Result =", a / b)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
