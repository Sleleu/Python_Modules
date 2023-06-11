import sys

def operations():

    try:
        assert len(sys.argv) > 1, "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
        assert len(sys.argv) == 3, "AssertionError: too many arguments"
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except AssertionError as Error:
        print(Error)
        return
    except ValueError:
        print("AssertionError: only integers")
        return
    
    print(f'Sum:        {a + b}')
    print(f'Difference: {a - b}')
    print(f'Product:    {a * b}')
    try:
        print(f'Quotient:   {a / b}')
        print(f'Remainder:  {a % b}')
    except ZeroDivisionError:
        print("Quotient:   ERROR (division by zero)")
        print("Remainder:  ERROR (modulo by zero)")


if __name__ == "__main__":
    operations()
