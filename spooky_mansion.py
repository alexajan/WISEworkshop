# Topics:
# types: numbers and strings
# if-else statements

# Story:
# Enter mansion
# choose your door

# Create your character
name = # enter name here: "Sonja Lindberg"
age = # enter age as an integer here: 20
favorite_color = # enter color here: "green"

# Characteristics
# Put a number in each field so that the three values sum to 10
strength =
intellect =
speed =

# Story
# Intro
print("It was a dark and stormy night. Rain was pouring down and an eerie mist had spread over Manhattan. "
      "The trick-or-treaters were tucked safely away in bed, but the ghosts and ghouls were only just coming out to "
      "play. But wait - one trick-or-treater was still out and about!")

print( name + " had gotten lost in the woods of Central Park and was desperately searching for shelter from the downpour"
              " when she came upon a spoooooky mansion. Relieved to find somewhere dry to stay,"
              " she ignored the mysterious red substance dripping from the awning and cheerily proceeded inside. ")

# Variables that we'll use later
door_1 = "- a black door, with smoke pouring out"
door_2 = "- a green door, with a riddle"

door_3 = "- a really heavy steel door"
door_4 = "- a straw door"

door_5 = "- a open doorway with saw blades swinging. It would probably take a really fast person to get through this hall..."
door_6 = "- a just a normal door. Any old schmuck could open it."

end_1 = "A monster jumps out and eats you :("
end_2 = "You are ejected out of the house and land in a nearby tree. Luckily, your house is right around the corner."
end_3 = "You find a box of Gtown cupcakes and a GIANT bag of Halloween candy. Score!"
end_4 = "You end up at the entrance to the mansion, but you can't seem to remember the last 30 minutes. You figure you" \
        "might as well go inside since it's raining pretty hard. #recursion"

current_room = 0

# Entering the mansion - the first decision dun dun dun
print("You enter the mansion and see two doors: ")
print(door_1)
print(door_2)

if intellect > 6:
    print("You solve the riddle easily and enter door 2.")
    current_room = 2

elif intellect > 4:
    print("You take a minute to solve the riddle and go through door 2.")
    speed = speed - 1
    current_room = 2

else:
    print("You're stumped by the riddle and make your way through the smoke through door 1. You cough, "
          "feeling yourself weaken.")
    strength = strength - 1
    current_room = 1

# 2nd floor of the house
print("You find yourself facing another set of doors: ")
if current_room == 1:
    print(door_3)
    print(door_4)

    if strength > 6:
        print("You smile to yourself, flex those biceps, and pull open that steel door easily.")
        current_room = 3

    elif strength > 4:
        print(
            "You wrench open the door with some effort, coughing from the smoke you just inhaled, and enter door 1. You "
            "feel a little light-headed. Oxygen flow to your brain decreases. (Don't smoke, kids.)")
        current_room = 3
        intellect = intellect - 1

    else:
        print("You fall through the straw door.")
        current_room = 4

elif current_room == 2:
    print(door_5)
    print(door_6)

    if speed >
        # fill this out here

    elif
        # fill in the blank

    else:
        # what happens here?

# Ending(s)
if current_room == 3:
    print(end_1)

elif current_room == 4:
    print(end_2)

elif current_room == 5:
    print(end_3)

else:  # in room 6
    print(end_4)

# Ex 01: Draw out the paths you can take through the haunted house.

# Ex 02: Fill in name, age, color, and characteristics.

# Ex 03: Finish room 2 if-else statements, following syntax above.

# Ex 04: Add another door and another ending.

# Ex 05: Create another level of doors that depend on favorite color.

# Talk to Alexa and Sonja if you have any questions or want more to do!