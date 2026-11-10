def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def main():
    history = []

    while True:
        print("\nENTERPRISE MODULAR UTILITY CALCULATOR")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. View Calculation History")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == '8':
            print("Exiting program.")
            break

        if choice == '7':
            if not history:
                print("\nHistory is empty.")
            else:
                print("\n--- History ---")
                for item in history:
                    print(item)
                print("---------------")
            continue

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("\nError: Invalid selection. Choose between 1 and 8.")
            continue

        try:
            if choice == '6':
                base = float(input("Enter the base number: "))
                exp_input = input("Enter the exponent (press Enter for default 2): ")
                
                if exp_input == "":
                    res = power(base)
                    record = f"{base} ** 2 = {res}"
                else:
                    exp = float(exp_input)
                    res = power(base, exp)
                    record = f"{base} ** {exp} = {res}"
            else:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if choice == '1':
                    res = add(a, b)
                    record = f"{a} + {b} = {res}"
                elif choice == '2':
                    res = subtract(a, b)
                    record = f"{a} - {b} = {res}"
                elif choice == '3':
                    res = multiply(a, b)
                    record = f"{a} * {b} = {res}"
                elif choice == '4':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero is not allowed.")
                    res = divide(a, b)
                    record = f"{a} / {b} = {res}"
                elif choice == '5':
                    if b == 0:
                        raise ZeroDivisionError("Modulus by zero is not allowed.")
                    res = modulus(a, b)
                    record = f"{a} % {b} = {res}"

            print(f"Result: {res}")
            history.append(record)

        except ValueError:
            print("\nError: Invalid numeric input.")
        except ZeroDivisionError as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()