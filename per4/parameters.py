"""
Tricks with Parameters in Python
Dr. J
Fall 2026
"""
from typing import Any

def f(x: Any, y: Any):
    """Here, x & y are positional parameters. They are assigned in order.
    
    The are required parameters. f() can only be called with 2 arguments."""
    print(x, y)

def g(x: Any = None):
    """Here, x is a keyword parameter.
    
    The default value makes the parameter optional."""
    print(x)

def h(x: Any, /):
    """If / is a parameter, then everything before *has* to be positional"""
    print(x)

def i(*, x: Any = None):
    """If * is a parameter, then everything after *has* to be keyword."""
    print(x)

# These two are maybe a little silly
def j(x: Any = None, /):
    """x is an optional keyword parameter you must provide positionally."""
    print(x)

def k(*, x: Any):
    """x is a required parameter that you must provide as kwarg."""
    print(x)

# More useful
def l(*args: Any):
    """The * unary operator says take many things and put them in a tuple
    
    It will take all positional arguments, as many as you want."""
    print(f"{len(args)=}, {type(args)=}")
    for arg in args:
        print(arg, end=", ")
    print()

def m(**kwargs: Any):
    """The ** unary operator takes many key-value pairs into a dictionary"""
    print(kwargs)

if __name__ == "__main__":
    # Here, we have positonal arguments.
    f("Madi", "Sophia")
    # Here, we provide the positional parameters as keyword arguments
    f(y="Sophia", x="Madi")
    # Leave out the optional keyword argument.
    g()
    # Providing the keyword argument positionally.
    g("Saanvi")
    # Here, we are giving a key-value pair as a keyword argument (kwarg).
    g(x = "Eric")
    # Provide the argument positionally
    h("Tomas")
    # Try to provide it as a kwarg
    try:
        h(x="Ethan")
    except TypeError:
        print("You can't provide x as a kwarg in this one.")
    # Provide the argument as kwarg
    i(x = "JT")
    # Try to provide it positionally
    try:
        i("JT")
    except TypeError:
        print("You can't provide x positionally in this one.")
    # Skip the optional argument
    j()
    # Provide it positionally 
    j("David")
    # Try to provide as kwarg
    try:
        j(x="Greg")
    except TypeError:
        print("You can't provide x as a kwarg in this one.")
    # Provide the argument as kwarg
    k(x = "Kayley")
    # Try to provide it positionally
    try:
        k("Kristen")
    except TypeError:
        print("You can't provide x positionally in this one.")
    l("Madi", "Sophia", "Saanvi", "Eric", "Tomas", "Ethan", "JT", "David")
    m(a = "Greg", b = "Kayley", c = "Kristen")