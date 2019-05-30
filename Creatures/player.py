from Items.items import Gold, Rock, Weapon
import World.world as world


class Player:

    def __init__(self):
        self.inventory = [Gold(25), Rock()]
        self.health = 100
        self.location_x, self.location_y = world.starting_position #soon make world map

    def is_alive(self):
        if self.health > 0:
            return self.health
#self.health &amp;gt; 0

    def print_inventory(self):
        for item in self.inventory:
            print(item)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.place_exist(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory: #looking for a best weapon
            if i in Weapon:
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        print("You use {} against{}".format(best_weapon.name, enemy.name))
        enemy.health -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}".format(enemy.name))
        else:
            print("{} HP is {}".format(enemy.name, enemy.health))