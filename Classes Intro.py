mylist = [1,2,3]

myset = set()

type(mylist)

class Dog(): 
    
    def __init__(self,breed,name,spots): #INIT (a method) is the constructor for a class and be called automatically, #SELF represents the instance of the object itself
                                 #SELF represents the instance of the object itself or the class
        # Attributes
        # We take in the arguement
        # We assign it using self.attribute_name in this case self.breed
        self.breed = breed
        self.name = name
        
        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed='lab',name='Sammie',spots=False)

type(my_dog)
#__main__.Dog

my_dog.name
# 'Sammie'

my_dog.spots
# False

