class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"{self.name} makes a sound")

class Dog(Animal):
  def speak(self):
    print(f"{self.name} barks")

class Cat(Animal):
  def speak(self):
    print(f"{self.name} meows")

class Cow(Animal):
  def speak(self):
    print(f"{self.name} moos")

# polymorphism — same method, different behaviour
animals = [Dog("Rex"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
  animal.speak()

# Rex barks
# Whiskers meows
# Bessie moos