class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width
    return width

  def set_height(self, height):
    self.height = height
    return height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    
    result = ''
    for i in range(self.height):
      result += self.width * '*'
      result += '\n'
    return result

  def get_amount_inside(self, obj):
    return (self.width // obj.width) * (self.height // obj.height)
  
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
class Square (Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  
  def set_height(self, height):
    self.width = height
    self.height = height
    return height

  def set_width(self, width):
    self.width = width
    self.height = width
    return width

  def set_side(self, side):
    self.width = side
    self.height = side
    return side
    
  def __str__(self):
    return f'Square(side={self.height})'