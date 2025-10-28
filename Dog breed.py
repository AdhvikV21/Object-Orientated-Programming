#create class
class Dog:
    
    # class attribute
    animal = "dog"

    # instance attributes 
    def __init__(self, dog_breed, dog_colour):
        self.breed = dog_breed
        self.colour = dog_colour

    def display_details(self):
        print(f"  Type: {Dog.animal}")
        print(f"  Breed: {self.breed}")
        print(f"  Colour: {self.colour}")

dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepard", "Brown")

print("Dog 1")
dog1.display_details()
print("Dog 2")
dog2.display_details()