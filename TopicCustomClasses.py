#Topic Custom Classes in Python
class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _iter_(self):
        # Yields the dictionary with length and width in the specified format.
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)
for attribute in rect:
    print(attribute)
