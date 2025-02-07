class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive = True

    def eat (self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("WOOF!"*3)

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Rat(Animal):
    def speak(self):
        print("SQUEEK!")


dog = Dog("Scooby")
cat =Cat("Garfeild")
mouse =Rat("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()