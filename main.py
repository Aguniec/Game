from Interactions.interactions import MainInteractions
from Creatures.creatures import Goblin, Human

class UserInterface:

    def get_name():
        print("Hello! What's your name?")
        name = input("")
        print("OK {},let's play a game".format(name))
        
    def get_interaction():
        command = input("Select interaction:")
        return command

    def get_creature():
        selected_creature = input("Select creature:")
        return selected_creature

    def select_interaction():
        command = UserInterface.get_interaction()
        selected_creature = UserInterface.get_creature()
        if command in verb_dict:
            selected_interaction = verb_dict[command]
            print(selected_interaction(selected_creature))
        else:
            print("Unknown command {}".format(command))
        return selected_interaction


verb_dict = {
    "say" : MainInteractions.say,
    "examine" : MainInteractions.examine,
    "hit" : MainInteractions.hit
}


goblin = Goblin("Gooby")
human = Human("Steve")


UserInterface.get_name()

while True:

    UserInterface.select_interaction()