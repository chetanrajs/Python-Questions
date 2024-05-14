class Animal:
    def sound(self):
        print("Animal is making a sound")
        
class Dog(Animal):
    def bark(self):
        print("Dog Barks")
        
class Cat(Animal):
    def meow(self):
        print("Cat Meow")
        
dog = Dog()
cat = Cat()

dog.sound()
dog.bark()
cat.sound()
cat.bark()
