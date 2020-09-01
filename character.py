class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here! " + self.description )

    def get_conversation(self):
        return self.conversation

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    # Ask character for a tip
    def ask_help(self):
        print(self.name + " doesn't want to help you")
#Enemy subclass
class Enemy(Character):
    number_of_enemies = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.number_of_enemies += 1

    def get_weakness(self):
        return self.weakness

    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness

    #fight this enemy character
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

#Friend subclass
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.tip = None

    def get_tip(self):
        return self.tip

    #set what gift the friend has to give
    def set_tip(self, tip):
        self.tip = tip

    #ask the friend for a helpful tip
    def ask_help(self):
        if self.tip is not None:
            print("[" + self.name + " says]:" + self.tip)
        else:
            print("[" + self.name + " says]: I dont have anything to give, but good luck!")