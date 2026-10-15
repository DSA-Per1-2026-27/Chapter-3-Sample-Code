class MyInt:
    def __init__(self, x: int):
        self.x = x

    def __str__(self) -> str:
        return str(f"Myint: {self.x}")

    def __add__(self, y: int) -> int:
        return self.x + y
    
    # Try commenting out __radd__
    def __radd__(self, y: int) -> int:
        return self.x + y

x = MyInt(5)
print(x + 3) # Call __add__ from MyInt
print(3 + x) # Call __radd__ from MyInt