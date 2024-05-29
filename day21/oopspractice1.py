class square:
  def __init__(self,side):
    self.side=side

  def square_area(self):
    return self.side * self.side

  def square_perimeter(self):
    return 4*self.side

num=int(input())
length=square(num)
print(length.square_area())
print(length.square_perimeter())