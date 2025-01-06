from graphics import circle
from graphics import rectangle
from graphics.dgraphics.sphere import area as sp_area
from graphics.dgraphics.sphere import volume as sp_vol  
from graphics.dgraphics import cuboid



print("area of circle :",circle.area(2))
print("perimeter of circle :",circle.permiter(2))
print("area of rectangle :",rectangle.area(2,4))
print("perimeter of rectangle :",rectangle.perimeter(2,4))
print("area of sphere :",sp_area(4))
print("volume of sphere :",sp_vol(4))

print("area of cuboid :",cuboid.area(2,3,4))
print("perimeter of cuboid :",cuboid.perimeter(2,3,4))



