def divide_numbers(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(result)