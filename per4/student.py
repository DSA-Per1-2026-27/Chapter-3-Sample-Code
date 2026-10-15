class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other: "Student") -> bool:
        """Implement == as True if first & last names are same."""
        if not isinstance(other, Student):
            return NotImplemented
        return (self.first_name == other.first_name and 
                self.last_name == other.last_name)