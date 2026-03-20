# its just a hashmap

student = {"name" : "John",
           "age" : 25,
           "courses": ["Math", "CS"]}

student["name"] = "Jane"
student.update({"name" : "Rabbit", "age" : 12})

print(student["name"])
print(student.get("lname"))
student["lname"] = "Kaisen"

# deleting
del student["age"]
student.pop("courses")
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# iteration
for key, value in student.items():
  print(key, value)