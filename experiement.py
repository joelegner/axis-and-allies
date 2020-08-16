from axisandallies.util import battle # type: ignore
from axisandallies.util import wprint
import datetime
import os
import random
import sys
import typing
from axisandallies.forces import Forces
from axisandallies.util import BattleResults

if __name__ == "__main__":
    from matplotlib import pyplot as plt

    xs = [ ]
    ys = [ ]

    threshold = 0.8
    min_len_ratio = 999.0
    ratios = [ ] 

    for i in range(0, 100):
        a = Forces()
        d = Forces()

        while not len(a):
            a.I = random.randint(0, 10)
            a.A = random.randint(0, 10)
            a.B = random.randint(0, 4)
            a.F = random.randint(0, 4)
        while not len(d):
            d.I = random.randint(0, 10)
            d.A = random.randint(0, 10)
            d.F = random.randint(0, 4)
            d.B = random.randint(0, 4)

        battle_results = BattleResults(a, d)
        battle(a, d, results=battle_results)

        ratio = battle_results.len_ratio()
        if ratio > 0.85 and ratio <= 2.0:
            xs.append(battle_results.len_ratio())
            ys.append(battle_results.attack_prob())
            ratios.append(ratio)
        if battle_results.attack_prob() is not None and battle_results.attack_prob() > threshold:


    plt.scatter(xs, ys)
    plt.savefig("experiement.png")
    print(ratios)


