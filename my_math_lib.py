def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b
    
def mul(a,b):
    return a*b
    
def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factoral(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
    
