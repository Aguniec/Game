from Interactions.interactions import MainInteractions
from Creatures.creatures import Goblin, Human


class UserInterface:


    verb_dict = {
        "say": MainInteractions.say,
        "examine": MainInteractions.examine,
        "hit": MainInteractions.hit
    }

    @staticmethod
    def get_name():
        print("Hello! What's your name?")
        name = input("")
        print("OK {},let's play a game".format(name))

    @staticmethod
    def select_interaction():

        command = input("Select interaction:")
        selected_creature = input("Select creature:")

        if command in UserInterface.verb_dict:
            selected_interaction = UserInterface.verb_dict[command]
            print(selected_interaction(selected_creature))
        else:
            print("Unknown command {}".format(command))
        return selected_interaction



goblin = Goblin("Gooby")
human = Human("Steve")


#UserInterface.get_name()

while True:

    UserInterface.select_interaction()