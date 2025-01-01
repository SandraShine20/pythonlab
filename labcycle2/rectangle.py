class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
         return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
r1=rectangle(5,9)
r2=rectangle(6,10)
print("area of rectangle1:",r1.area())    
print("perimeter of rectangle1:",r1.perimeter())
print("area of rectangle2:",r2.area())
print("perimeter of rectangle2:",r2.perimeter())

if r1.area()>r2.area():
  print("rectangle1 is larger than rectangle2")
elif r1.area()==r2.area():
    print("rectangle1 and rectangle2 are equal")
else:
  print("rectangle2 is larger than rectangle1")