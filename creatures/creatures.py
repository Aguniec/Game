class Creature:
    class_name = ""
    description = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        Creature.objects[self.class_name] = self
    
    def get_description(self):
        return self.class_name + "\n" + self.description


class Goblin (Creature):
    def __init__(self, name):
        self.class_name = "goblin"
        self._description = "A big, green creature"
        self.health = 3
        super().__init__(name)
    
    @property
    def description(self):
        if self.health >= 3:
            return self._description
        elif self.health == 2:
            health_status = "It's arm has been cut off"
        elif self.health == 1:
            health_status = "It lost its leg"
        elif self.health <= 0:
            health_status = "It's dead"
        return self._description + "\n" + health_status
    
    @description.setter
    def description(self, value):
        self._description = value


class Human(Creature):
    def __init__(self, name):
        self.class_name = "human"
        self._description = "Regular human"
        self.health = 10
        super().__init__(name)

    @property
    def description(self):
        if self.health >= 10:
            return self._description
        elif self.health == 6:
            health_status = "It's arm has been cut off"
        elif self.health == 4:
            health_status = "It lost its leg"
        elif self.health == 2:
            health_status = "It los its both legs"
        elif self.health <= 0:
            health_status = "It's dead"
        return self._description + "\n" + health_status

    @description.setter
    def description(self, value):
        self._description = value
