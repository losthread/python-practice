# sys module imports the system 
import sys

if len(sys.argv) < 2:
  print('Too few arguments')
elif len(sys.argv) > 2:
  print('Too many arguments')

print('Hello', sys.argv[1])