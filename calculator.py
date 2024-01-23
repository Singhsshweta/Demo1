def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

if __name__ == "__main__":
    calculator()
