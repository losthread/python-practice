class Person:
  def __init__(this, name, age):
    this.name = name
    # private property
    this.__age = age

  # getter
  def get_age(this):
    return this.__age

  # setter
  def set_age(this, age):
    this.__age = age
  
p1 = Person("John", 25)
p1.set_age(21)
print(p1.name)
print(p1.get_age())

# it is not strict in python
print(p1._Person__age) # still works