#!/usr/bin/python
"""This module contains the entry function for the traffic simulator.

Reads argument information and executes a simulation depending on the given
arguments.

"""

import argparse
import time
import road
import traffic_light
import viewer

def main():
    """Entry function for the traffic simulator."""
    args = parse_args()
    view = viewer.Viewer()
    road1 = road.Road(traffic_light.TrafficLight.RED)
    road2 = road.Road(traffic_light.TrafficLight.GREEN)

    perf = 0

    time_steps = 0
    while 1:
        if time_steps % 1000 == 0:
            perf = road1.get_amount_queued() + road2.get_amount_queued()
            road1.reset_queueing()
            road2.reset_queueing()
            print "Performance: " + str(perf)
        road1.update()
        road2.update()
        view.update_roads(road1, road2)
        time_steps += 1
        time.sleep(0.01)

def parse_args():
    """Read in commandline arguments and return them in an argument object."""
    parser = argparse.ArgumentParser(description="A traffic intersection "
                                     "simulator with various learning "
                                     "algorithms.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
