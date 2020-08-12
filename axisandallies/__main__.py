import random
import datetime
from forces import Forces # type: ignore
from util import battle # type: ignore

random.seed(a=None, version=2)

RUNS = 1000

print(datetime.datetime.now())
attacking_army = Forces(I=2, A=3, F=0, B=0, attacking=True)
defending_army = Forces(I=4, A=0, F=0, B=0, attacking=False)
battle(attacking_army, defending_army, RUNS)
