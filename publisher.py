class publisher:
    def __init__(self,name):
        self.name=name


class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author

class python(book):
    def __init__(self,name,title,author,price,npages):
        super().__init__(name,title,author)
        self.price=price
        self.npages=npages

    def display(self):
        print(f"Name of publisher: {self.name}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"No of pages: {self.npages}")

obj=python("abcpublishers","101","gefauthor","500","1000")
obj.display()

    
