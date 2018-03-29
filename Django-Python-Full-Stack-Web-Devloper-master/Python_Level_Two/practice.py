class Dog():
    #class object Attributes
    species = "mammal"

    def __init__(self, breed, name):    #initialization
        self.breed = breed
        self.name = name
mydog = Dog(breed= "labrador", name= "Sammy")
#hisdog = Dog(breed = "Huskie")
print(mydog.breed)
#print(hisdog.breed)
print(mydog.name)
print(mydog.species)

#other example
class Circle():

    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myC = Circle(3)
myC.radius =100
myC.set_radius(999)
print(myC.area())
