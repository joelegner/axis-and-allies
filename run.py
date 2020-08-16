from axisandallies.util import battle_from_yaml # type: ignore
from axisandallies.util import wprint
import datetime
import os
import random
import sys
import typing


def usage(self):
    print("Usage: python run.py [yaml filename]")
   

def run_file(filenames: typing.List[str]) -> None:
    report = battle_from_yaml(filename)
    wprint(report[-1])

    # Output to a text file
    outfile = os.path.splitext(filename)[0] + ".txt"

    with open(outfile, "w") as f:
        wprint("%s" % __file__, file=f)
        wprint("Results", file=f)
        wprint(report[-1] + "\n", file=f)
        wprint("%s" % datetime.datetime.now(), file=f)
        for line in report:
            f.write(line + "\n")

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        usage()
        sys.exit(1)
    else:
        filenames = sys.argv[1:]
        for filename in filenames:
            if os.path.exists(filename):
                run_file(filename)
            else:
                print("File {filename} does not exist")
