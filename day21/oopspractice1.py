class Square:
  def __init__(self,side):
    self.side=side

  def area(self):
    return self.side * self.side

  def perimeter(self):
    return 4*self.side

num=int(input())
square=Square(num)
print(square.area())
print(square.perimeter())