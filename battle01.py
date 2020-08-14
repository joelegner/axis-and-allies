import random
import datetime
from axisandallies.forces import Forces # type: ignore
from axisandallies.util import battle # type: ignore
import os
import typing
from axisandallies.util import wprint

random.seed(a=None, version=2)

RUNS = 1000

attacking_army = Forces(I=2, A=0, F=2, B=0, attacking=True)
defending_army = Forces(I=2, A=0, F=2, B=0, attacking=False)

# Get a report of the battle
report = battle(attacking_army, defending_army, RUNS)
wprint(report[-1])

# Output to a text file
outfile = os.path.splitext(__file__)[0] + ".txt"

with open(outfile, "w") as f:
    wprint("%s" % __file__, file=f)
    wprint("Two infantry and a fighter from India attack the two infantry and fighter in French Indo-China Burma.\n", file=f)
    wprint("Results", file=f)
    wprint(report[-1] + "\n", file=f)
    wprint("%s" % datetime.datetime.now(), file=f)
    for line in report:
        f.write(line + "\n")
