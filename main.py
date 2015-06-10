#!/usr/bin/python
"""This module contains the entry function for the traffic simulator.

Reads argument information and executes a simulation depending on the given
arguments.

"""

import argparse
import intersection
import learner
import random
import time
import viewer

def main():
    """Entry function for the traffic simulator."""
    learning_algorithm = learner.Learner()
    view = viewer.Viewer()
    intersec = intersection.Intersection()
    time_steps = 0

    while 1:
        # Snapshot the state of the roads
        view.update_roads(intersec.get_roads()[0], intersec.get_roads()[1])
        if time_steps % 1000 == 0 and time_steps != 0:
            print intersec.get_performance()
        old_state = intersec.get_state()

        # Update the state of the roads
        action = learning_algorithm.get_action(old_state)
        # action = time_steps % 10 == 0
        intersec.update_state(action)
        new_state = intersec.get_state()
        learning_algorithm.learn(old_state, new_state, action)
        time_steps += 1
        time.sleep(1)

if __name__ == "__main__":
    main()
