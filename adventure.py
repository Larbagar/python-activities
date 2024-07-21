location = "entrance"
key = False

invalidMessage = "You can't do that. (press enter to continue)"

print("You fall into a pit!")
input()

while location != "exit":
  if location == "entrance":
    print("You see the bright light of the outside world above you, just barely out of reach.")
    print("In front of you, you see a door, and a passage going into a dark room.")
    decision = input("What do you do? (door/passage) ")
    if decision == "door":
      if key:
        print("You unlock the door and walk through.")
        location = "exit"
      else:
        print("The door is locked!")
    elif decision == "passage":
      print("You walk into the dark room.")
      location = "dark room"
    else:
      print(invalidMessage)
  elif location == "dark room":
    print("There's not much light here, but you can barely make out something reflecting the light from the other room")
    print("Behind you is the room that you fell into")
    decision = input("What do you do? (investigate/back) ")
    if decision == "investigate":
      print("You find a key!")
      key = True
    elif decision == "back":
      print("You return to the enterance")
      location = "entrance"
    else:
      print(invalidMessage)
  else:
    print("Not sure how it happened, but you just walked out of bounds...")
    print("I guess I'll just send you back to the enterance?")
    print("Try not to return.")
    location = "entrance"

  input()

print("You feel the blinding light from outside wash over you!")
print("You have escaped!")