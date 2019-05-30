from Items.items import Gold, Rock


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