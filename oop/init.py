class Dog:
  # constructor
  def __init__(this, name, age):
    this.name = name    # self = this in C++
    this.age = age
  
  # method
  def bark(this):
    print(f"{this.name} says woof!")
  
  # string representation
  # defines what prints when we print(object)
  def __str__(this):
    return f"Dog: {this.name}, {this.age}"

# inheritance
class Puppy(Dog):
  def __init__(this, name, age, toy):
    super().__init__(name, age) 
    this.toy = toy

d = Dog("Rex", 3)
d.bark()
print(d)