# #Inheritance
class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print('eating')



class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog created")
    def bark(self):
        print("woof")

myd = Dog()
myd.whoAmI()
myd.eat()
myd.bark()


#Special Methods-to form special operations, called by specific syntax not called directly
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:{}, Author:{}, Pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("the book is no more")

b= Book("python", "zeel", 200)
del b
