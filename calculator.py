import Divide
import Multiply

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice : ")

    if choice not in ['1', '2','3','4','5']:
        print("Invalid choice. Please enter 1 , 2 , 3, or 4")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = Multiply.multiply_numbers(num1, num2)
        print(f"{num1} x {num2} = {result}")
    elif choice == '4':
        result = Divide.divide_numbers(num1, num2)
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
