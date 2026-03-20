set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 
# same result
set3 = set1 | set2
print(set3) 

# union allows any collection to be put in a set

# inserts set 2 items into set 1
set1.update(set2)
print(set1) 

# returns a new set
set3 = set1.intersection(set2)
print(set3)
# same result 
set3 = set1 & set2
print(set3)

# updates the original set not a new one
set1.intersection_update(set2)

# returns a new set
set3 = set1.difference(set2)
# same result
set3 = set1 - set2
print(set3)

# changes the original set
set1.difference_update(set2)

# elements not in both sets returns a new set
set3 = set1.symmetric_difference(set2)
# same result
set3 = set1 ^ set2
set1.symmetric_difference_update()