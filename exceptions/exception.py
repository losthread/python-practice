try:
  x = int(input("Enter a value for x: "))
  print(f"x is {x}")
except ValueError:
  print("Please enter an integer only")