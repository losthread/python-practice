print('Imported modules')

test = 'Test String'

def find_index(to_search, target):
  for i in range(len(to_search)):
    if to_search[i] == target:     
      return i
  
  return -1