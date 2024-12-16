def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # Correct behavior for a=0
    else:
        return b / a  # Potential ZeroDivisionError if b is very large