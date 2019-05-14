from creatures.creatures import Creature, Goblin, Human

class Printed:
    def get_name():
        print("Hello! What's your name?")
        name = input("")
        print("OK {},let's play a game".format(name))
        
    def get_input():
        command = input(":").split()
        verb_word = command[0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            print("Unknown command {}".format(verb_word))
            return
        
        if len(command) >=2:
            noun_word = command[1]
            print (verb(noun_word))
        else:
            print(verb("nothing"))

class Interactions: 
    def hit(noun):
        if noun in Creature.objects:
            thing = Creature.objects[noun]
            if type(thing) == Goblin or Human:
                thing.health = thing.health - 1
                if thing.health <=0:
                    msg = "You killed the {}".format(thing.class_name)
                else:
                    msg = "You hit the {}".format(thing.class_name)
            else:
                msg = "There is no {} here".format(noun)
        return msg

    def examine(noun):
        if noun in Creature.objects:
            return Creature.objects[noun].get_descryption()
        else:
            return "There is no {} here".format(noun)

    def say(noun):
        return "You said {}".format(noun)

    def ask_name(noun):
        if noun in Creature.objects:
            asked_creature = Creature.objects[noun]
            if asked_creature.health > 0:
                print("{}: What's your name?".format(Printed.get_name)) #Doesn't work properly
                msg = "My name is " + asked_creature.name
            else :
                msg = "Why are you try to interact the dead creature?"
        else : 
            msg = "There is no {} here".format(noun)
        return msg


verb_dict = {
    "say" : Interactions.say,
    "examine" : Interactions.examine,
    "hit" : Interactions.hit,
    "ask_name" : Interactions.ask_name
}


goblin = Goblin("Gooby")
human = Human("Steve")


Printed.get_name()

while True:
    Printed.get_input()
