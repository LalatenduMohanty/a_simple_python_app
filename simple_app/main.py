"""
Main module containing the core functionality.
"""

def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name (str): Name of the person to greet
        
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}! Welcome to SimpleApp!"

def main():
    """Main entry point for the application."""
    name = input("Please enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main() 