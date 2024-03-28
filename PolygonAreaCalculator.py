class Rectangle:
    def __init__(self, width, height):
        # Initiate base class
        self.width = width
        self.height = height

    def __repr__(self):
        # Change how the object is printed
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        # Update width
        self.width = width

    def set_height(self, height):
        # Update height
        self.height = height

    def get_area(self):
        # Return the area of the shape
        return self.width * self.height

    def get_perimeter(self):
        # Return the perimeter of the shape
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Return the diagonal of the shape
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Get how the shape should be printed
        if (self.width > 50) or (self.height > 50):
            # Condition for printing: no side is greater than 50
            return "Too big for picture."
        else:
            picture = ""
            for row in range(self.height):
                picture += '*' * self.width
                picture += '\n'

            return picture

    def get_amount_inside(self, shape):
        # Obtain how many {shape} instances could be fitted into the current object
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        # Initiate child class 
        self.side = side
        super().__init__(side, side)

    def __repr__(self):
        # Determine how the child class object is printed
        return f"Square(side={self.side})"

    ### Update the dimensions accordingly
    def set_side(self, side):
        self.side = side
        self.set_width(side)
        self.set_height(side)

    def set_width(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))