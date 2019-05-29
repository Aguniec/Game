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
