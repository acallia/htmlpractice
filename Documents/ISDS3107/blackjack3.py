import random

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
sum = 0
turn = "hit"
while turn == "hit":
  sum += random.choice(card_values)
  print("You currently have: " + str(sum))
  turn = input("What do you want to do? ")

if sum >= 21:
  print("You went over 21!")
else:
  print("You stopped at: " + str(sum))
