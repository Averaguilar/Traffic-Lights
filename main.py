#!/usr/bin/python
"""This module contains the entry function for the traffic simulator.

Reads argument information and executes a simulation depending on the given
arguments.

"""

import argparse
import intersection
import learner
import time
import viewer

def main():
    """Entry function for the traffic simulator."""
    args = parse_args()
    view = viewer.Viewer()
    learning_algorithm = learner.Learner()
    intersec = intersection.Intersection()
    time_steps = 0

    while 1:
        # Snapshot the state of the roads
        # TODO: fix this it's a hack
        view.update_roads(intersec.get_roads()[0], intersec.get_roads()[1])
        if time_steps % 1000 == 0 and time_steps != 0:
            print intersec.get_performance()
        old_state = intersec.get_state()

        # Update the state of the roads
        action = learning_algorithm.get_action(old_state)
        intersec.update_state(action)
        new_state = intersec.get_state()
        learning_algorithm.learn(old_state, new_state, action)
        time_steps += 1
        time.sleep(0.5)

def parse_args():
    """Read in commandline arguments and return them in an argument object."""
    parser = argparse.ArgumentParser(description="A traffic intersection "
                                     "simulator with various learning "
                                     "algorithms.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
