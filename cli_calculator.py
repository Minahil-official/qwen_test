import sys
from calculator import Calculator

def main():
    calc = Calculator()
    
    if len(sys.argv) != 4:
        print("Usage: python cli_calculator.py <number1> <operator> <number2>")
        print("Operators: +, -, *, /")
        return
    
    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])
        
        if operator == '+':
            result = calc.add(num1, num2)
        elif operator == '-':
            result = calc.subtract(num1, num2)
        elif operator == '*':
            result = calc.multiply(num1, num2)
        elif operator == '/':
            result = calc.divide(num1, num2)
        else:
            print("Invalid operator. Use: +, -, *, /")
            return
        
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()