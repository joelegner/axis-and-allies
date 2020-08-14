from .units import unit_data # type: ignore
from typing import Sized

# Order in which casualties are selected for attacking
attack_casualty_prefs = ["I", "A", "S", "F", "B", "BB", "AC"]

# Order in which casualties are selected for defence
defend_casualty_prefs = ["I", "A", "S", "B", "F", "AC", "BB"]

class Forces:
    def __init__(self, I=0, A=0, F=0, B=0, S=0, BB=0, AC=0, attacking=True):
        self.I = I  # Infantry
        self.A = A  # Armor
        self.B = B  # Bombers
        self.F = F  # Fighters
        self.S = S  # Submarines
        self.BB = BB  # Battleships
        self.AC = AC  # Aircraft Carriers
        self.attacking = attacking

    def __str__(self):
        retval = ""
        for k in unit_data.keys():
            num = self.__dict__[k]
            if num:
                retval = retval + f"{num} {unit_data[k]['name']} "
        return retval.strip()

    def land_forces_count(self):
        return self.I + self.A

    def __len__(self) -> int:
        return self.I + self.A + self.B + self.F + self.BB + self.S + self.AC

    def kill(self, key):
        self.__dict__[key] = self.__dict__[key] - 1
        return f"Killed 1 {unit_data[key]['name']}"

    def _choose_casuality(self):
        global attack_casualty_prefs
        global defend_casualty_prefs
        assert(len(self))
        if self.attacking:
            prefs = attack_casualty_prefs
        else:
            prefs = defend_casualty_prefs
        for k in prefs:
            if self.__dict__[k] > 0:
                self.kill(k)
                return True
        return False

    def choose_casualties(self, num):
        "Remove least preferred unit first"
        while len(self) and num:
            if self._choose_casuality():
                num = num - 1

    def total_strength(self):
        total_dice = 0
        if self.attacking:
            verb = "attack"
        else:
            verb = "defend"
        for k in unit_data.keys():
            total_dice = total_dice + self.__dict__[k]*unit_data[k][verb]
        return total_dice