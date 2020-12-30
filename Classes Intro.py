mylist = [1,2,3]
myset = set()
type(mylist)
list
class Dog(): 
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal' 
    
    def __init__(self,breed,name): #INIT (a method) is the constructor for a class and be called automatically, #SELF represents the instance of the object itself
                                 #SELF represents the instance of the object itself or the class
        # Attributes
        # We take in the arguement
        # We assign it using self.attribute_name in this case self.breed
        self.breed = breed
        self.name = name

        
    # OPERATIONS/Actions ---> Methods
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))
my_dog = Dog('Lab','Frankie')
type(my_dog)
__main__.Dog
my_dog.species
'mammal'
my_dog.name
'Frankie'
my_dog.bark(10)
WOOF! My name is Frankie and the number is10
 
 
 
 
class Circle():
    
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14
     
    def __init__(self,radius=1): # <--- Can have a default value of 1 and then override below 
        
        self.radius = radius
        self.area = radius*radius*Circle.pi #<-- Can reference this in this manner because it is a class object attribute
        
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2
my_circle = Circle(30)  #<--- Overriding value of 30
my_circle.pi
3.14
my_circle.radius
30
my_circle.area
2826.0
my_circle.get_circumference()
188.4
