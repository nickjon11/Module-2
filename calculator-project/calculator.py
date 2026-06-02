"""
Jonathan Lachman
Calculator Project with User Input
6/2/2026
"""

# Calculator Function

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Main Program

def main():
    print("Simple Calculator Program Test function")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Choose 1-4): ")
    num1 = float(input("Enter first number "))
    num2 = float(input("Enter second number "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        try:
            print("Result:", divide(num1, num2))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()