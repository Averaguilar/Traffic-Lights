#!/usr/bin/python
"""This module contains the entry function for the traffic simulator.

Reads argument information and executes a simulation depending on the given
arguments.

"""

import argparse
import viewer

def main():
    """Entry function for the traffic simulator."""
    args = parse_args()
    print args

def parse_args():
    """Read in commandline arguments and return them in an argument object."""
    parser = argparse.ArgumentParser(description="A traffic intersection "
                                     "simulator with various learning "
                                     "algorithms.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
