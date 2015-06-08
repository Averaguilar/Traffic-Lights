import collections
import constants
import road

class Learner(object):
    def __init__(self):
        self._q_estimate = collections.defaultdict(lambda: [0, 0])
        self._num_visits = collections.defaultdict(lambda: [0, 0])

    def learn(self, last_state, current_state, switch_lights):
        max_q = -99999
        alpha = 1 / float(1 + self._num_visits[last_state][switch_lights])

        for action in (True, False):
            if max_q < self._q_estimate[current_state][action]:
                max_q = self._q_estimate[current_state][action]

        self._q_estimate[last_state][switch_lights] = ((1 - alpha) *
            self._q_estimate[last_state][switch_lights] + alpha *
            (reward(last_state, switch_lights) + max_q))
        self._num_visits[last_state][switch_lights] += 1

    def get_action(self, state):
        if self._q_estimate[state][True] > self._q_estimate[state][False]:
            return True
        else:
            return False

def reward(state, switch_lights):
    if switch_lights:
        road = state.green_road()
    else:
        road = state.red_road()

    if state.closest_car(road) == 1:
        return -1
    else:
        return 0
