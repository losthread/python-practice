# in python we can extract values from a tuple into variables

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
# *red will store the last remaining elements as a list

print(green)
print(yellow)
print(red)