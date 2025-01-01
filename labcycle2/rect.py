class rectangle: 
    def __init__(self,__width,__height):
        self.__width = __width
        self.__height = __height

    def area(self):
        return self.__width * self.__height
    
    def __lt__(self,other):
        if self.area()<other.area():
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.area()>other.area():
            return True
        else:
            return False


obj1=rectangle(5,7)
obj2=rectangle(2,3)
print(obj1.area())
print(obj2.area())
print(obj1<obj2)
print(obj1>obj2)
