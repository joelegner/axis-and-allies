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

    for i in range(0, 100):
        a = Forces()
        d = Forces()

        while not len(d):
            d.I = random.randint(0, 9)
            d.A = random.randint(0, 6)
            d.F = random.randint(0, 4)
            d.B = random.randint(0, 2)
    
        arange = (max(int(0.8*len(d)), 1), int(2.0*len(d)))

        while len(a) < arange[0] or len(a) > arange[1]:
            a.I = random.randint(0, 9)
            a.A = random.randint(0, 6)
            a.B = random.randint(0, 2)
            a.F = random.randint(0, 4)

        battle_results = BattleResults(a, d)
        battle(a, d, results=battle_results)

        ratio = battle_results.len_ratio()
        prob = battle_results.attack_prob()

        xs.append(battle_results.len_ratio())
        ys.append(prob)

        if battle_results.attack_prob() >= 0.8:
            print(100*"-")
            print(f"{a} beat {d}")
            print(f"{len(a)}/{len(d)}= {ratio:.2f} => {prob:.2f}")
        elif ratio > 1.0 and prob < 0.50:
            print(100*"*")
            print(f"{a} beat {d}")
            print(f"{len(a)}/{len(d)}= {ratio:.2f} => {prob:.2f}")

    plt.scatter(xs, ys)
    plt.savefig("experiement.png")
