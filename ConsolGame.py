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
    def __init__(self, name):
        self.class_name = "goblin"
        self._descryption = "A big, green creature"
        self.health = 3
        super().__init__(name)
    
    @property
    def descryption(self):
        if self.health >=3:
            return self._descryption
        elif self.health == 2:
            healh_status = "It's arm has been cut off"
        elif self.health == 1:
            healh_status = "It lost its leg"
        elif self.health <= 0:
            healh_status = "It's dead"
        return self._descryption + "\n" + healh_status
    
    @descryption.setter
    def descryption (self, value):
        self._descryption = value


class Human(Creature):
    def __init__(self, name):
        self.class_name = "human"
        self._descryption = "Regular human"
        self.health = 10
        super().__init__(name)

    @property
    def descryption (self):
        if self.health >=10:
            return self._descryption
        elif self.health == 6:
            healh_status = "It's arm has been cut off"
        elif self.health == 4:
            healh_status = "It lost its leg"
        elif self.heath == 2:
            healh_status = "It los its both legs"
        elif self.health <= 0:
            healh_status = "It's dead"
        return self._descryption + "\n" + healh_status

    @descryption.setter
    def descryption (self, value):
        self._descryption = value


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

    def question(noun):
        if noun in Creature.objects:
            asked_creature = Creature.objects[noun]
            if asked_creature.health > 0:
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
    "question" : Interactions.question
}


goblin = Goblin("Gooby")
human = Human("Steve")

while True:
    Printed.get_input()
