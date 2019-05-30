class Item:

    def __init__(self, name, description, resistance):
        self.name = name
        self.description = description
        self.value = resistance

    def __str__(self):
        return self.name + self.description + self.value


class Gold(Item):

    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold",
                         description="A round coin with {} on it".format(str(self.amount)),
                         resistance=self.amount)


class Weapon(Item):

    def __init__(self, name, description, resistance, damage):
        self.damage = damage
        super().__init__(name, description, resistance)


class Rock(Weapon):

    def __init__(self):
        super().__init__(name="Rock",
                         description="An ordinary pile of debris",
                         resistance=0,
                         damage=5)


class Knife(Weapon):

    def __init__(self):
        super().__init__(name="Knife",
                         description="A knife from steel",
                         resistance=10,
                         damage=10)