from enum import Enum

class Realm(Enum):
    LAND = 1
    SEA = 2
    AIR = 3

unit_data = {
    "I": {"name": "Infantry", "attack": 1, "defend": 2},
    "A": {"name": "Armor", "attack": 3, "defend": 2},
    "F": {"name": "Fighter", "attack": 3, "defend": 4},
    "B": {"name": "Bomber", "attack": 4, "defend": 1},
    "S": {"name": "Submarine", "attack": 2, "defend": 2},
    "T": {"name": "Transport", "attack": 0, "defend": 1},
    "BB": {"name": "Battleship", "attack": 4, "defend": 4},
    "AC": {"name": "Aircraft Carrier", "attack": 0, "defend": 1},
}

can_hit_air = ["I", "A", "F", "B", "BB", "T", "AC"]
can_hit_land = ["I", "A", "F", "B", "BB"]
can_hit_sea = ["I", "A", "F", "B", "BB", "T", "AC"]