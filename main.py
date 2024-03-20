print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You come across a fork in the road.\nTo the left is the entrance to a dark cave system, and to the right is the start of a treacherous mountain pass.\nWhich direction do you go? (Left or Right)\n\n").lower()

if choice1 == "left":
  print("\nYou succesfuly make it into the cave system.\n")
  choice2 = input("Inside of the cave, there is a huge underground lake.\nYou may either take the raft across the water, or swim to the other side.\n\nWhat do you do? (Swim or Raft)\n\n").lower()
  if choice2 == "swim":
    print("\nYou swim across the lake, only to be sucked underwater by a large whirlpool. You pop back up outside the cave.\n")
    choice3 = input("You come across a castle with three large doors. A red door, a yellow door, and a blue door.\nWhich door do you go through? (Red, Yellow, or Blue)\n\n").lower()
    if choice3 == "red":
      print("\nYou open the red door and are immediately engulfed in flames. You burn to death.\n\nGame Over.")
    elif choice3 == "yellow":
      print("You open the yellow door and are immediately engulfed in a bright light. After the light fades, you find the treasure in front of you.\n\nYou Win!")
    else:
      print("The door you open explodes. Oops! You die.\n\nGame Over")
  else:
    print("\nThe raft pops halfway through the water and you hit your head on a rock. You drown and die.\n\nGame Over")
else:
  print("\nYou didn't check the weather before climbing the mountain pass. A storm rolls in and strikes you with lightning. You instantly die.\n\nGame Over")