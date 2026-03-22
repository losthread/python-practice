class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

del p1

p2 = MyClass()
p3 = MyClass()
print(p2.x, p3.x)