# basic_calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def hotfix():
    print("SWEAR TO GOD I FIXED SOMETHING")
    #source: just trust me, bro

def main():
    for i in range(100):
        hotfix()
    print("Simple Calculator")
    print("Available operations: add, subtract")
    
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

    print("Result:", result)

if __name__ == "__main__":
    main()
