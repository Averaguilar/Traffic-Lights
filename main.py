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

    while 1:
        road1.update()
        road2.update()
        view.update_roads(road1, road2)
        time.sleep(1)

def parse_args():
    """Read in commandline arguments and return them in an argument object."""
    parser = argparse.ArgumentParser(description="A traffic intersection "
                                     "simulator with various learning "
                                     "algorithms.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
