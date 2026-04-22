name = input("Enter your name: ")

# safely opens and closes
# if close is forgotten when manually doing it
# then the file may get corrupted
with open("names.txt", "a") as file:
  file.write(f'{name}\n')

names = []

# 'r' gives reading privileges
with open("names.txt", "r") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):
  print(f'hello, {name}')