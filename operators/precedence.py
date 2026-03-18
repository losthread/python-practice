print(2 + 3 * 4)        # 14  - * before +
print((2 + 3) * 4)      # 20  - () first
print(2 ** 3 ** 2)      # 512 - ** right to left (3**2=9, 2**9=512)
print(10 / 2 + 3)       # 8.0 - / before +
print(10 + 2 > 8 - 1)   # True - arithmetic before comparison
print(True or False and False)  # True - and before or
print(not True or True)         # True - not before or