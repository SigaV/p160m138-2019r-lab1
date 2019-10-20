import sys


def greet(greeted_name: str): 
    return f"Hello, {greeted_name}!"
    
    
if __name__== "__main__":
    print(greet(sys.argv[1]))
