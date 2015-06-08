import road
import traffic_light

class State(object):
    def __init__(self, roads):
        self._closest = []
        for road in roads:
            start = road.light_location() + 1
            for i in xrange(0, 9):
                 if road.has_car(start - i):
                     break
            self._closest.append(i)
        for i in xrange(0, len(roads)):
            if roads[i].light_color() == traffic_light.TrafficLight.GREEN:
                self._green_road = i
    def __eq__(self, other):
        for i in xrange(len(self._closest)):
            if self._closest[i] != other._closest[i]:
                return False
        return self._green_road == other._green_road

    def __hash__(self):
        hash_list = list(self._closest)
        hash_list.append(self._green_road)
        return hash(tuple(hash_list))

    def green_road(self):
        return self._green_road

    def red_road(self):
        return (self._green_road + 1) % 2

    def closest_car(self, road_num):
        return self._closest[road_num]
