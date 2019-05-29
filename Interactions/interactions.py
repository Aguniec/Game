from Creatures.creatures import Creature, Goblin, Human



class MainInteractions:
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

"""
    def ask_name(noun):
        if noun in Creature.objects:
            asked_creature = Creature.objects[noun]
            if asked_creature.health > 0:
                print("{}: What's your name?".format(UserInterface.get_name)) #Doesn't work properly
                msg = "My name is " + asked_creature.name
            else :
                msg = "Why are you try to interact the dead creature?"
        else :
            msg = "There is no {} here".format(noun)
        return msg
"""