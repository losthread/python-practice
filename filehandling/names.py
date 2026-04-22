name = input("What is your name? ")

# opens the file and 'w' gives write privileges
# 'a' gives append privileges
file = open("names.txt", "a")
# adds
file.write(f'{name}\n')
# close
file.close()