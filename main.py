from room import Room
from item import Item
from character import Enemy
from character import Friend
from rpginfo import RPGInfo

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
conservatory = Room("Conservatory")

print ("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("An echoing, dusty space adorned with faded curtains")
dining_hall.set_description("A dark-panelled room lit by a crackling log fire")
conservatory.set_description("A misty and mildewed place, overgrown with creepers.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(conservatory, "south")
conservatory.link_room(ballroom, "north")

dave = Enemy("Dave","A smelly zombie!")
dave.set_conversation("Eurghrrh...flesshh")
dave.set_weakness("cheese")

brad = Enemy("Brad","A bloodthirsty vampire!")
brad.set_conversation("Listen to them, the children of the night. What sweet music they make!")
brad.set_weakness("garlic")

mildred = Friend("Mildred","A lazy ghost!")
mildred.set_conversation("Woooo...oh I can't be bothered - hello friend!")
mildred.set_tip("Dave is terrified of cheese!")

frank = Friend("Frank","A chatty crow!")
frank.set_conversation("Caw! Caw!")
frank.set_tip("Caw! Brad hates garlic")

key = Item("key")
key.description = "A small ornate brass key"
key.size = 1

cheese = Item("cheese")
cheese.description = "A very smelly brie"
cheese.size = 2

garlic = Item("garlic")
garlic.description = "A plait of fat garlic bulbs"
garlic.size = 3

dining_hall.set_character(dave)
ballroom.set_character(brad)
kitchen.set_character(mildred)
conservatory.set_character(frank)

dining_hall.set_item(key)
kitchen.set_item(garlic)
conservatory.set_item(cheese)

mystery_manor = RPGInfo("The Mystery Manor")
mystery_manor.welcome()

current_room = kitchen
backpack = []
backpack_capacity = 10
backpack_contents = 0
enemies_defeated = 0
dead = False

#main game loop
while dead == False:
    #print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    roomitem = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if roomitem is not None:
        roomitem.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("there is no-one here to talk to")

    #add an item to backback
    elif command == "take":
        if roomitem is not None:
            if backpack_contents + roomitem.size <= backpack_capacity:
                backpack.append(roomitem.name)
                backpack_contents = backpack_contents + roomitem.size
                current_room.set_item(None)
                print("You have added the " + roomitem.name + " to your backpack")
            else:
                print("There isn't enough room in your backpack")
        else:
            print("there is nothing here to take")

    #remove an item from backback
    #elif command == "leave":
        #item_to_leave = input(">")
        #if item_to_leave in backpack:
            #if roomitem is None:
                #current_room.set_item(item_to_leave)
            #else:
                #print("You can't leave that here")
        #else:
            #print("You dont have that in your backpack")

    elif command == "help":
        if inhabitant is not None:
            inhabitant.ask_help()
        else:
            print("there is no-one here to ask help from")

    #fight an enemy
    elif command == "fight":
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                result = inhabitant.fight(fight_with)
                #print("the result is " + str(result))
                if result == True:
                    enemies_defeated += 1
                    if enemies_defeated >= Enemy.number_of_enemies:
                        print("You have won!")
                        dead = True
                else:
                    print("Game Over!")
                    dead = True
            else:
                print("You dont have any " + fight_with + "!")
        else:
            print("There is no-one here to fight")

RPGInfo.author = "Simon"
RPGInfo.credits()