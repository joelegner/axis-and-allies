import matplotlib.pyplot as plt
import random
import numpy as np
from units import unit_data
import copy
import datetime

# Order in which casualties are selected for attacking
attack_casualty_prefs = ["I", "A", "S", "F", "B", "BB", "AC"]

# Order in which casualties are selected for defence
defend_casualty_prefs = ["I", "A", "S", "B", "F", "AC", "BB"]

RUNS = 1000

print(datetime.datetime.now())


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

    def __len__(self):
        return self.I + self.A + self.B + self.F + self.BB + self.S + self.AC

    def kill(self, key):
        print(f"Killed 1 {unit_data[key]['name']}", end = ' ')
        self.__dict__[key] = self.__dict__[key] - 1

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


def battle(attackers, defenders, runs=RUNS):
    assert type(attackers) == Forces
    assert type(defenders) == Forces

    attacker_wins = 0
    defender_wins = 0

    attacker_units_left = 0
    defender_units_left = 0

    at = copy.copy(attackers)
    de = copy.copy(defenders)

    rounds = 0
    for r in range(0, runs):

        print(f"************Start run #{r+1} of {runs}")


        attackers = copy.copy(at)
        defenders = copy.copy(de)

        while len(attackers) and len(defenders):
            rounds += 1
            print(f"=========== Round {rounds}")
            print("Attackers: %s" % attackers)
            print("Defenders: %s" % defenders)
            ahits = 0
            dhits = 0
            # print("Attacker rolls:")
            for j in unit_data.keys():
                n = attackers.__dict__[j]
                unit_type = unit_data[j]["name"]
                hit_score = unit_data[j]["attack"]
                if n:
                    ahits += roll_dice(n, hit_score)
            # print("Defender rolls:")
            for k in unit_data.keys():
                n = defenders.__dict__[k]
                unit_type = unit_data[k]["name"]
                hit_score = unit_data[k]["defend"]
                if n:
                    dhits += roll_dice(n, hit_score)
            print(f"Attacker hits {ahits} times with {len(attackers)} units")
            print(f"Defender hits {dhits} times with {len(defenders)} units")
            print("Attacker...", end=' ')
            if ahits:
                defenders.choose_casualties(ahits)
                print("")
            else:
                print("Misses.")
            print("\nDefender...", end=' ')
            if dhits:
                attackers.choose_casualties(dhits)
                print("")
            else:
                print("Misses.")

        defender_won = True
        if not len(defenders) and attackers.land_forces_count():
            defender_won = False

        if defender_won:
            defender_wins += 1
            defender_units_left += len(defenders)
            print("Defender wins************")
        else:
            attacker_wins += 1
            attacker_units_left += len(attackers)
            print("Attacker wins************")

    avg_rounds = float(rounds) / runs

    prob_attacker_wins = float(attacker_wins) / float(attacker_wins + defender_wins)
    prob_defender_wins = 1.0 - prob_attacker_wins

    avg_attacker_units_left = float(attacker_units_left) / runs
    avg_defender_units_left = float(defender_units_left) / runs

    print(
        f"in {runs} battles the attackers won {attacker_wins} times and the defenders won {defender_wins} times in an average of {avg_rounds:.2f} rounds.\nAttacker probability {prob_attacker_wins:.3f} with average of {avg_attacker_units_left:.2f} units left, defender {prob_defender_wins:.3f} with average of {avg_defender_units_left:.2f} units left."
    )


def roll_dice(num, hit_score=1):
    hits = 0
    for i in range(0, num):
        if random.randint(1, 6) <= hit_score:
            hits += 1
    return hits


attacking_army = Forces(I=2, A=2, F=0, B=0, attacking=True)
defending_army = Forces(I=4, A=0, F=0, B=0, attacking=False)
battle(attacking_army, defending_army)
