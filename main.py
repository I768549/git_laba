# basic_calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def main():
    print("Simple Calculator")
    print("Available operations: add, subtract, multiply")
    
    op = input("Enter operation: ").strip().lower()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Numbers only.")
        return

    if op == "add":
        result = add(num1, num2)
    elif op == "subtract":
        result = subtract(num1, num2)
    elif op == "multiply":
        result = multiply(num1, num2)

    print("Result:", result)

if __name__ == "__main__":
    main()
