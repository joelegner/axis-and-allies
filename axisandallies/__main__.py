import matplotlib.pyplot as plt
import random
import numpy as np
from units import unit_data
import copy

# Order in which casualties are selected for attacking
attack_casualty_prefs = ["I", "A", "F", "B"]

# Order in which casualties are selected for defence
defend_casualty_prefs = ["I", "A", "B", "F"]


class Forces:

    def __init__(self, I=0, A=0, F=0, B=0, attacking=True):
        self.I = I
        self.A = A
        self.B = B
        self.F = F
        self.attacking = attacking

    def land_forces_count(self):
        return self.I + self.A

    def __len__(self):
        return self.I + self.A

    def kill(self, key):
        self.__dict__[key] = self.__dict__[key] - 1

    def _choose_casuality(self):
        print("Choose a casualty")
        global attack_casualty_prefs
        global defend_casualty_prefs
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
        while num:
            if self._choose_casuality():
                num = num - 1
            else:
                return False
        return True


def battle(attackers, defenders, runs=10000):
    assert(type(attackers) == Forces)
    assert(type(defenders) == Forces)

    attacker_wins = 0
    defender_wins = 0

    at = copy.copy(attackers)
    de = copy.copy(defenders)

    rounds = 0
    for r in range(0, runs):
        attackers = copy.copy(at)
        defenders = copy.copy(de)
        while len(attackers) and len(defenders):
            rounds += 1
            print("Attacker rolls:")
            for k in unit_data.keys():
                n = attackers.__dict__[k]
                unit_type = unit_data[k]["name"]
                hit_score = unit_data[k]["attack"]
                if n:
                    print(f"Attacker has {n} {unit_type}")
                    ahits = roll_dice(n, hit_score)
            print("Defender rolls:")
            for k in unit_data.keys():
                n = defenders.__dict__[k]
                unit_type = unit_data[k]["name"]
                hit_score = unit_data[k]["defend"]
                if n:
                    print(f"Defender has {n} {unit_type}")
                    dhits = roll_dice(n, hit_score)
            print(f"Attacker hits {ahits} times")
            defenders.choose_casualties(ahits)
            print(f"Defender hits {dhits} times")
            attackers.choose_casualties(dhits)

        if attackers.land_forces_count():
            attacker_wins += 1
        else:
            defender_wins += 1

    avg_rounds = float(rounds)/runs

    prob_attacker_wins = float(attacker_wins) / \
        float(attacker_wins + defender_wins)
    print(f"in {runs} battles the attackers won {attacker_wins} times and the defenders won {defender_wins} times in an average of {avg_rounds:.2f} rounds. Attacker probability {prob_attacker_wins:.3f}")


def roll_dice(num, hit_score=1):
    hits = 0
    for i in range(0, num):
        if random.randint(1, 6) <= hit_score:
            hits += 1
    return hits


attacking_army = Forces(I=4, A=1, F=0, B=0, attacking=True)
defending_army = Forces(I=1, A=0, F=0, B=0, attacking=False)
battle(attacking_army, defending_army)
