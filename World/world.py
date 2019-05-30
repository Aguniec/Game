
_world = {} #maps a coordinate pair to a place
starting_position = (0, 0)


def load_places():
    """Parses a file that describes the world space into the _world object"""
    with open("resources/map.txt", "r") as file:
        rows = file.readlines()
        x_max = len(rows[0].splt("\t")) # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].splt("\t")
            for x in range(x_max):
                place_name = cols[x].replace("\n","")
                if place_name == "StartingRoom":
                    global starting_position
                    starting_position = (x, y)
                if place_name == "":
                    _world[(x, y)] = None  #create a key to a dict, doesn't if cell is empty
                else:
                    getattr(__import__("places"), place_name)(x, y)
                    """reflect into places module, find class whose name matches place_name and
                    passes the coordinates (x, y) to the constructor of the places"""

        """alternative : tile_map = [[FindGoldRoom(),GoblinRoom(),None,None,None],
            [None,StartingRoom(),EmptyCave(),EmptyCave(),None]] """

def place_exist(x, y):
    return _world.get((x, y))