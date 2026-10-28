from typing import Any

def f(x: Any):
    """A function with a positional parameter.
    
    Notice that positional parameters are almost always required."""
    print(x)

def g(y: Any = "Dr. J"):
    """A function with a keyword parameter.
    
    Keyword parameters are always optional."""
    print(y)

def h(x: Any, y: Any, z: Any = "Henry"):
    """A function with both positional and keyword parameters.
    
    In the declaration, *all* the positional parameters must come before *any*
    of the keyword parameters."""
    print(x, y, z)

def i(x:Any , y: Any, /, z: Any="Alisa"):
    """The / character forces x & y to be only provided positionally."""
    print(x, y, z)

def j(x: Any, y: Any, *, z: Any="Tracie"):
    """The * character forces z to be provided only as a keyword argument."""
    print(x, y, z)

def k(*peeps: Any):
    """Then peeps is a tuple, you input as many positional args as you want."""
    print(type(peeps), peeps)

def l(*peeps:Any, **keyword_peeps: Any):
    """**keyword_peeps forms a dictionary of key-value pairs.
    
    Most often: (*args, **kwargs)"""
    print(peeps)
    print(keyword_peeps)

if __name__ == "__main__":
    # Optional parameters must have a default value in order to be optional
    # f() ## This will crash the program
    # Positional Parameter provided as a positional argument
    f("Tracie")
    # Positional Parameter provided as a keyword argument (kwarg)
    f(x = "Luming")
    # Keyword argument omitted because it is optional, uses default value
    g()
    # Keyword parameter provided as a positional argument
    g("Michelle")
    # Keyword parameter provided as a keyword argument
    g(y = "Sherry")
    # Provide all three positionally
    h("Travis", "Ronik", "Adrian")
    # Can skip the optional one
    h("Krishna", "Jaiden")
    # Can mix them up as keyword arguments
    h(z="Emma", y="Jasmine", x="Jas")
    # If you use both positional and keyword arguments, gotta do positional 1st
    h("Jas", z="Emma", y="Jasmine")
    # This will crash because x & y have to be provided positionally.
    # i(x="Aaron", y="Santa Claus")
    i("Aaron", "Santa Claus")
    # Number of positional arguments is as long as you want.
    k("Tracie", "Sherry")
    k("Alisa", "Aaron", "Jasmine", "Jas", "Emma", "Luming", "Henry", "Travis")
    # Number of positional and keyword args is as long as you want.
    l("Adrian", "Ronik", krishna="Ramaswamy", jaiden="Chen", dr="J", 
            satan="Lucifer")