fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

# by index
for i in range(len(fruits)):
  print(fruits[i])

i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1

[print(x) for x in fruits] 

# copy elements
newList = fruits.copy()
newList2 = list(fruits)
newList3 = fruits[:]