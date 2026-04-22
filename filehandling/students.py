import csv

students = []

with open('names.csv', 'r') as file:
  # read a csv file with lobrary instead of manual method
  reader = csv.DictReader(file)
  for name, home in reader:
    students.append({'name' : name, 'home' : home})


# lambda functions are anonymous functions
# used where we only have to call them once
for student in sorted(students, key=lambda student: student['name'], reverse=True):
  print(f"{student['name']} is in {student['house']}")