# Local, Enclosing, Global, Built-in(for built in functions)

# global scope
x = 'global x'

def test():
  # local scope
  y = 'local y'
  print(y)
  print(x)

test()

# enclosing scope
def outer():
  x = 'outer x'
  
  def inner():
    x = 'inner x'
    print(x)

  inner()
  print(x)

outer()