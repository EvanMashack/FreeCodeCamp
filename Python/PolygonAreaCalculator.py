# Assignment: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
# Test Case is at the bottom of PolygonAreaCalculator.py

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return str(type(self).__name__) + f"(width={self.width}, height={self.height})"
    
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
     return round(((self.width ** 2 + self.height ** 2) ** .5), 2)

  # Returns our shape drawn in asterisks
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    shape = ""
    for i in range(self.height):
      shape += ("*" * self.width) + "\n"
    return shape

  # Returns how many times shape can fit into self without rotating
  def get_amount_inside(self, shape):
    amount = 0
    for i in range(int(self.height / shape.height)): 
      amount += int(self.width / shape.width)
    return amount

# Child class of Rectangle where width and height must be the same  
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return str(type(self).__name__) + f"(side={self.width})"

  def set_side(self, side):
    self.width = side
    self.height = side
    
  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side



# Test Case
"""
shape1 = Rectangle(4, 5)
shape2 = Square(2)
print(shape1)
print(shape2) 
print("\n")
print(shape1.get_picture())
print(shape2.get_picture())
print("\n")
print(shape1.get_amount_inside(shape2))
print(shape1.get_diagonal())
"""
 
