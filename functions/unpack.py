def studetnInfo(*args, **kwargs):
  print(args)
  print(kwargs)

courses = ['Math', 'Art']
info = {'name' : 'John',
        'age' : 22}

# * will unpack these collections
studetnInfo(*courses, **info)