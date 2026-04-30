# Simple Python Program
def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def main():
    """Main function to demonstrate the code"""
    # Greet the user
    greeting = greet("Developer")
    print(greeting)
    
    # Perform addition
    result = add_numbers(10, 20)
    print(f"10 + 20 = {result}")
    
    # Print a simple message
    print("Python is awesome!")

if __name__ == "__main__":
    main()