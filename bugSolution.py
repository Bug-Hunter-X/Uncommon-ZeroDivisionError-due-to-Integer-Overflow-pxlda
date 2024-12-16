import sys

def function_with_uncommon_error(a, b):
    if a == 0:
        return 0
    try:
        result = b / a
        return result
    except OverflowError:
        print("OverflowError occurred. Using arbitrary-precision arithmetic.")
        from decimal import Decimal, getcontext
        getcontext().prec = 100  # Adjust precision as needed
        return Decimal(b) / Decimal(a)
    except ZeroDivisionError:
        return float('inf')  # or raise the exception as appropriate

# Example usage:

a = 1
b = sys.maxsize # Use the maximum integer size for demonstration
result = function_with_uncommon_error(a, b)
print(f"Result with a={a}, b={b}: {result}")

a = 0
b = 10
result = function_with_uncommon_error(a,b)
print(f"Result with a={a}, b={b}: {result}")

a = 10
b = 0
result = function_with_uncommon_error(a,b)
print(f"Result with a={a}, b={b}: {result}") 