from Creatures.creatures_new import Enemy, Goblin, Ogre
from Items.items import Knife
import World.places, Interactions.interactions_new, World.world



class MapPlace:

    def __init__(self,x, y):
        self.x = x
        self.y = y

    def intro_message(self):
        raise NotImplementedError() #warn if  accidentally create a MapPlace directly

    def modify_player(self, player):
        raise NotImplementedError() #warn if  accidentally create a MapPlace directly


class StartingRoom(MapPlace):

    def intro_message(self):
        return """You find yourself if a cave. You can make out four paths."""

    def modify_player(self, player):
        """This room has no action on a player"""
        pass


class LootRoom(MapPlace):

    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class FindKnifeRoom(LootRoom):

    def __init__(self, x, y):
        super().__init__(x, y, Knife)

    def intro_message(self):
        return """  Your notice something shiny in the corner. It's a knife! You pick it up. """

#added

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapPlace):

    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.heath = the_player.heath - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, the_player.heath))


class GoblinCave(EnemyRoom):

    def __init__(self, x, y):
        super().__init__(x, y, Goblin)

    def intro_message(self):
        if self.enemy.is_alive():
            return """A small goblin stands in front of you"""
        else:
            return """A head of dead goblin is on the ground"""


class EmptyCave(MapPlace):

    def intro_message(self):
        return """ Another unremarkable part of the cave. You must go ahead."""

    def modify_player(self, player):
        """Room has no action on player"""
        pass





