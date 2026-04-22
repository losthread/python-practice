import csv

name = input('What is your name? ')
home = input('Where is your home? ')

with open('names.csv', 'a') as file:
  # fieldname is used to give the order of the columns
  writer = csv.DictWriter(file, fieldnames=['name', 'home'])
  writer.writerow({'name': name, 'home': home})

