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

    min_cost_ratio_95pct = 0.0
    min_cost_ratio_80pct = 0.0
    min_cost_ratio_50pct = 0.0

    for i in range(0, 500):
        a = Forces()
        d = Forces()

        while not len(d):
            d.I = random.randint(0, 9)
            d.A = random.randint(0, 6)
            d.F = random.randint(0, 4)
            d.B = random.randint(0, 2)
    
        arange = (max(int(0.8*len(d)), 1), int(4.0*len(d)))

        while len(a) < arange[0] or len(a) > arange[1] or a.total_cost() > d.total_cost()*3.0:
            a.I = random.randint(0, 9)
            a.A = random.randint(0, 6)
            a.B = random.randint(0, 2)
            a.F = random.randint(0, 4)

        battle_results = BattleResults(a, d)
        battle(a, d, results=battle_results)

        cost_ratio = a.total_cost()/d.total_cost()
        prob = battle_results.attack_prob()

        if cost_ratio > 1.5 and prob < 0.5:
            print(f"{a} versus {d} only won {prob:.2f}")

        if prob < 0.95:
            min_cost_ratio_95pct = max(min_cost_ratio_95pct, cost_ratio)
        if prob < 0.80:
            min_cost_ratio_80pct = max(min_cost_ratio_80pct, cost_ratio)
        if prob < 0.50:
            min_cost_ratio_50pct = max(min_cost_ratio_50pct, cost_ratio)

        xs.append(cost_ratio)
        ys.append(prob)

    # Now get the cost ratio that was next above the highest failure
    min_cost_ratio_95pct = min([cr for cr in xs if cr > min_cost_ratio_95pct])
    min_cost_ratio_80pct = min([cr for cr in xs if cr > min_cost_ratio_80pct])
    min_cost_ratio_50pct = min([cr for cr in xs if cr > min_cost_ratio_50pct])

    # Draw some horizontal lines to indicate threshold values
    plt.axhline(y=0.95, color="green")
    plt.axhline(y=0.80, color="orange")
    plt.axhline(y=0.50, color="red")
    plt.axvline(x=min_cost_ratio_80pct, color="orange")
    plt.axvline(x=min_cost_ratio_95pct, color="green")
    plt.axvline(x=min_cost_ratio_50pct, color="red")

    # Label the 50% and 80% values
    FONTSIZE = 8
    plt.text(min_cost_ratio_80pct, 0.2, f"{min_cost_ratio_80pct:.2f}", fontsize=FONTSIZE, va='center', ha='left', backgroundcolor='w', rotation="vertical")
    plt.text(min_cost_ratio_50pct, 0.3, f"{min_cost_ratio_50pct:.2f}", fontsize=FONTSIZE, va='center', ha='left', backgroundcolor='w', rotation="vertical")
    plt.text(min_cost_ratio_95pct, 0.4, f"{min_cost_ratio_95pct:.2f}", fontsize=FONTSIZE, va='center', ha='left', backgroundcolor='w', rotation="vertical")



    plt.scatter(xs, ys)
    plt.savefig("ex_cost.png")

    print(f"Lowest cost_ratio for perfect wins = {min_cost_ratio_95pct:.2f}")
    print(f"Lowest cost_ratio for 80% wins     = {min_cost_ratio_80pct:.2f}")
    print(f"Lowest cost_ratio for 50% wins     = {min_cost_ratio_50pct:.2f}")
