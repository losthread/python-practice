# *args take a tuple, **kwargs take a dictionary
def studetnInfo(*args, **kwargs):
  print(args)
  print(kwargs)

studetnInfo('Math', 'Art', name='John', age=22)
