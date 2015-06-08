class Car(object):
    def __init__(self):
        self._wait_time = 0

    def move(self):
        self._wait_time = 0

    def wait(self):
        self._wait_time += 1

    def get_wait(self):
        return self._wait_time
