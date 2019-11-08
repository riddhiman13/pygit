class Rectangle:

    def __init__(self, length, breadth, unit_cost):
        self.breadth = breadth
        self.length = length
        self.unit_cost = unit_cost

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        return self.get_area() * self.unit_cost


rect1 = Rectangle(10, 20, 3)
rect2 = Rectangle(45, 2, 5)
rect3 = Rectangle(30, 67, 8)

print("The area of rectangle 1 is", rect1.get_area())
print("The perimeter of rectangle 2 is", rect2.get_perimeter())

