import random 

cards = ['jack', 'queen', 'king'];
random.shuffle(cards)
for i in range(0, len(cards)):
  print(cards[i])