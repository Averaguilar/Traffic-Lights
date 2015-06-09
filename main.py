#!/usr/bin/python
"""This module contains the entry function for the traffic simulator.

Reads argument information and executes a simulation depending on the given
arguments.

"""

import argparse
import learner
import time
import road
import state
import traffic_light
import viewer
import distributions

def main():
    """Entry function for the traffic simulator."""
    args = parse_args()
    view = viewer.Viewer()
    learning_algorithm = learner.Learner()
    road1 = road.Road(traffic_light.TrafficLight.RED, distributions.Probability.STANDARD)
    road2 = road.Road(traffic_light.TrafficLight.GREEN, distributions.Probability.STANDARD)

    time_steps = 0
    switch_time = 0

    while 1:
        # Snapshot the state of the roads
        view.update_roads(road1, road2)
        if time_steps % 1000 == 0 and time_steps != 0:
            print road1.get_amount_queued() + road2.get_amount_queued()
            road1.reset_queueing()
            road2.reset_queueing()
        old_state = state.State([road1, road2], switch_time)

        # Update the state of the roads
        if switch_time != 0:
            switch_time -= 1
        action = learning_algorithm.get_action(old_state)
        if action:
            road1.flip_color()
            road2.flip_color()
            switch_time = 3
        road1.update()
        road2.update()
        new_state = state.State([road1, road2], switch_time)
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
