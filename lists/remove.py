fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

print(fruits)

fruits.remove("banana")
print(fruits)

# removes at specified index
fruits.pop(1)

# removes last item
fruits.pop()

del fruits[0]
print(fruits)

fruits.clear() #clears the list
del fruits #deletes the list