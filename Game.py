class Printed:
    def get_input():
        command = input(":").split()
        verb_word = command[0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            print("Unknown verb {}".format(verb_word))
            return
        
        if len(command) >=2:
            noun_word = command[1]
            print (verb(noun_word))
        else:
            print(verb("nothing"))


class Creature:
    class_name = ""
    descryption = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        Creature.objects[self.class_name] = self
    
    def get_descryption(self):
        return self.class_name + "\n" + self.descryption


class Goblin (Creature):
    class_name = "goblin"
    descryption = "A big, green creature"


def examine(noun):
    if noun in Creature.objects:
        return Creature.objects[noun].get_descryption()
    else:
        return "There is no {} here".format(noun)

def say(noun):
    return "You said {}".format(noun)

verb_dict = {
    "say" : say,
    "examine" : examine
}


goblin = Goblin("Gooby")


while True:
    Printed.get_input()

