from .forces import attack_casualty_prefs # type: ignore
from .forces import defend_casualty_prefs # type: ignore
from .forces import Forces # type: ignore
from .units import unit_data # type: ignore
import copy
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import random
import textwrap
import typing
import yaml

WIDTH = 100

def battle(attackers: Forces, defenders: Forces, is_sea_battle=False, runs:int=1000):
    # Create a new report as a list of strings
    rpt = []

    attacker_wins = 0
    defender_wins = 0

    attacker_units_left = 0
    defender_units_left = 0

    at = copy.copy(attackers)
    de = copy.copy(defenders)

    if is_sea_battle:
        rpt.append("Type of Battle: Sea Battle")
    else:
        rpt.append("Type of Battle: Land Battle")

    rounds = 0
    for r in range(0, runs):
        rpt.append(f"************Start run #{r+1} of {runs}")
        attackers = copy.copy(at)
        defenders = copy.copy(de)

        while len(attackers) and len(defenders):
            rounds += 1
            rpt.append(f"=========== Round {rounds}")
            rpt.append("Attackers: %s" % attackers)
            rpt.append("Defenders: %s" % defenders)
            ahits = 0
            dhits = 0
            # rpt.append("Attacker rolls:")
            for j in unit_data.keys():
                n = attackers.__dict__[j]
                unit_type = unit_data[j]["name"]
                hit_score = unit_data[j]["attack"]
                if n:
                    ahits += roll_dice(n, hit_score)
            # rpt.append("Defender rolls:")
            for k in unit_data.keys():
                n = defenders.__dict__[k]
                unit_type = unit_data[k]["name"]
                hit_score = unit_data[k]["defend"]
                if n:
                    dhits += roll_dice(n, hit_score)
            if ahits > 1:
                rpt.append(f"Attacker hits {ahits} time")
            else:
                rpt.append(f"Attacker hits {ahits} times")
            rpt.append(f"Defender hits {dhits} times")
            rpt.append("Attacker:")
            if ahits:
                defenders.choose_casualties(ahits)
            else:
                rpt.append("Misses.")
            rpt.append("\nDefender:")
            if dhits:
                attackers.choose_casualties(dhits)
            else:
                rpt.append("Misses.")

        defender_won = True
        if not len(defenders) and len(attackers):
            defender_won = False

        if defender_won:
            defender_wins += 1
            defender_units_left += len(defenders)
            rpt.append("Defender wins************")
        else:
            attacker_wins += 1
            attacker_units_left += len(attackers)
            rpt.append("Attacker wins************")

    avg_rounds = float(rounds) / runs

    prob_attacker_wins = float(attacker_wins) / float(attacker_wins + defender_wins)
    prob_defender_wins = 1.0 - prob_attacker_wins

    avg_attacker_units_left = float(attacker_units_left) / runs
    avg_defender_units_left = float(defender_units_left) / runs

    rpt.append(
        f"In {runs} of battles with {at} attacking {de} the attackers won {attacker_wins} times and the defenders won {defender_wins} times in an average of {avg_rounds:.2f} rounds. Attacker probability {prob_attacker_wins:.3f} with average of {avg_attacker_units_left:.2f} units left, defender {prob_defender_wins:.3f} with average of {avg_defender_units_left:.2f} units left."
    )

    # Return the report
    return rpt

def battle_from_yaml(filename: str) -> typing.List[str]:
    rpt = [f"{filename} could not be opened."]
    with open(filename) as yaml_file:
        yaml_dict = yaml.load(yaml_file, Loader=yaml.SafeLoader)
        if "sea battle" in yaml_dict.keys():
            is_sea_battle = yaml_dict["sea battle"]  # Can still be false
        else:
            is_sea_battle = False
        attacking_army = Forces(attacking = True)
        defending_army = Forces(attacking = False)
        attacker_dict = yaml_dict["attacker"]
        defender_dict = yaml_dict["defender"]
        for k in attacker_dict.keys():
            attacking_army.__dict__[k] = attacker_dict[k]
        for k in defender_dict.keys():
            defending_army.__dict__[k] = defender_dict[k]
        rpt = battle(attacking_army, defending_army, is_sea_battle=is_sea_battle)
    return rpt
    

def roll_dice(num, hit_score=1):
    hits = 0
    for i in range(0, num):
        if random.randint(1, 6) <= hit_score:
            hits += 1
    return hits

def wprint(txt: str, file: typing.TextIO=None) -> None:
    "Print a string wrapped to a file"
    for wrapped_line in  textwrap.wrap(txt, width=WIDTH):
        if file is not None:
            print(wrapped_line, file=file)
        else:
            print(wrapped_line)
