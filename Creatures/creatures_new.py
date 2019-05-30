class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        if self.health > 0:
            return self.health


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name= "goblin",
                         health=10,
                         damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="ogre",
                         health=30,
                         damage=5)