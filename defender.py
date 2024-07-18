
print("Defender game")
print()

print("This game helps with learning about arrays, specifically appending and removing items")
print("It will also help by practising while loops")
print("This example uses no for loops")


import random


structures = ["mine", "mine", "mine"]
monsters = []
money = 0
survivalTime = 0


while len(structures) > 0:
  
  # Print out all the structures
  print("Your structures:")
  i = 0
  while i < len(structures):
    print(structures[i])
    i += 1
  print()

  # Print out all the enemies
  print("Monsters:")
  i = 0
  while i < len(monsters):
    print(monsters[i])
    i += 1

  print()
  print()

  # Let the player build structures
  print("You have $" + str(money))
  print("What would you like to do? (help for help)")
  command = input()
  while command != "":
    print()
    if command == "help":
      print("Type nothing to let time pass")
      print("Type \"check\" to see the state of the game")
      print("Type \"mercinary\" to hire a mercinary to kill one monster, costs $2")
      print("Type \"mine\" to build a mine, costs $4")
      print("Type \"tower\" to build a tower, costs $6")
    elif command == "check":
      # Print out all the structures
      print("Your structures:")
      i = 0
      while i < len(structures):
        print(structures[i])
        i += 1
      print()

      # Print out all the enemies
      print("Monsters:")
      i = 0
      while i < len(monsters):
        print(monsters[i])
        i += 1
    elif command == "mercinary":
      if money >= 2:
        if(len(monsters) > 0):
          target = random.randrange(0, len(monsters))
          print("The mercinary killed a " + monsters[target] + "!")
          monsters.pop(target)
          money -= 2
        else:
          print("There are no monsters to kill!")
      else:
        print("You don't have enough money!")
    elif command == "mine":
      if money >= 4:
        structures.append("mine")
        money -= 4
        print("You built a mine!")
      else:
        print("You don't have enough money!")
    elif command == "tower":
      if money >= 6:
        structures.append("tower")
        money -= 6
        print("You built a tower!")
      else:
        print("You don't have enough money!")
    else:
      print("Invalid command")

    print()
    
    print("You have $" + str(money))
    print("What would you like to do? (help for help)")
    command = input()

  # Run the players' structures
  print("Your turn:")
  i = 0
  while i < len(structures):
    structure = structures[i]
    if(structure == "mine"):
      print("You mined!")
      money += 1
    elif structure == "tower":
      if(len(monsters) > 0):
        target = random.randrange(0, len(monsters))
        print("Your tower killed a " + monsters[target] + "!")
        monsters.pop(target)
    i+=1
  print()
  print("Press enter to continue")
  input()

  # Run the monsters
  print("Monsters turn:")
  i = 0
  while i < len(monsters) and len(structures) > 0:
    monster = monsters[i]
    if monster == "zombie":
      target = random.randrange(0, len(structures))
      print("A zombie destroyed your " + structures[target] + "!")
      structures.pop(target)
    i += 1

  print()
  print("Press enter to continue")
  input()

  # Summon monsters
  zombies = 0
  if survivalTime < 5:
    zombies = random.randrange(0, 2)
  elif survivalTime < 11:
    zombies = random.randrange(0, 5)
  elif survivalTime < 21:
    zombies = random.randrange(0, 17)

  print(str(zombies) + " zombies appeared!")
  i = 0
  while i < zombies:
    monsters.append("zombie")
    i += 1

  survivalTime += 1

  print()
  print("Press enter to continue")
  input()



print("You have no structures remaining!")
print("Game over.")

input()

print("Other ideas:")
print("Add more waves")
print("Add more enemy types, such as ones that can deal more damage, deal no damage (but still block hits), summon other monsters, summon monsters on death, steal money, have a chance of dodging attacks, target specific structures, disable structures, are immune to certain towers, or buff other monsters.")
print("Add more tower types, such as ones that can attack multiple monsters, attack only certain types of monsters, attract monsters, block monster hits, or buff other towers.")
print("Possibly get monsters to drop things.")