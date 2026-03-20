fruits = set(("apple", "banana", "cherry"))
fruits.add("orange")

fruits2 = set(("pineapple", "orange"))
# update method can take any iterable
# be it tuples, lists, dictionaries
fruits.update(fruits2)
print(fruits)