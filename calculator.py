class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

def main():
    calc = Calculator()
    print("Basic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    if choice == '1':
        result = calc.add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = calc.subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = calc.multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        try:
            result = calc.divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()