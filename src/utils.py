def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Invalid inputs for add"


def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Invalid inputs for subtract"


def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return "Invalid inputs for multiply"


def divide(a, b):
    try:
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    except TypeError:
        return "Invalid inputs for divide"