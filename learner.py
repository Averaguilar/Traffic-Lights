"""This module contains a class implementing the Q-learning algorithm"""

import collections
import constants

class Learner(object):
    """A class implementing Q-learning on roads."""
    def __init__(self):
        """Initialize the class with all estimates set to 0."""
        self._q_estimate = collections.defaultdict(lambda: [0, 0])
        self._num_visits = collections.defaultdict(lambda: [0, 0])

    def learn(self, last_state, current_state, switch_lights):
        """Update the estimates of last state given the state it changed to."""
        max_q = -99999
        alpha = 1 / float(1 + self._num_visits[last_state][switch_lights])

        for action in (True, False):
            if max_q < self._q_estimate[current_state][action]:
                max_q = self._q_estimate[current_state][action]

        self._q_estimate[last_state][switch_lights] = ((1 - alpha) *
            self._q_estimate[last_state][switch_lights] + alpha *
            (reward2(last_state, switch_lights) + constants.DISCOUNT * max_q))
        self._num_visits[last_state][switch_lights] += 1

    def get_action(self, state):
        """Get the estimated best action to make in the given state."""
        if state.wait_time() > 0:
            return False

        if self._q_estimate[state][True] > self._q_estimate[state][False]:
            return True
        else:
            return False

def reward(state, switch_lights):
    """Given a state and an action, returns a reward based on the result"""
    if switch_lights:
        stopped_road = state.green_road()
    else:
        stopped_road = state.red_road()
    if stopped_road == -1:
        if state.closest_car(0) == 1 or state.closest_car(1) == 1:
            return -1
        else: 
            return 0

    if state.closest_car(stopped_road) == 1:
        return -1
    else:
        return 0

def reward2(state, switch_lights):
    return state.closest_car(0) + state.closest_car(1) - 18
