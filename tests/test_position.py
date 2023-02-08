import numpy as np

from fixture import ROOM_SIZE
from utils.position import calc_distance_for_position_in_room, random_position_in_room


class TestStringMethods(unittest.TestCase):
    def test_calc_distance_for_position_in_room(self):
        array = np.array((1, 0, 0))  # |array| = 1

        assert calc_distance_for_position_in_room(array) == 1.0

        array = np.array((3, 0, 0))  # |array| = 3
        assert calc_distance_for_position_in_room(array) == 3

    def test_random_position_in_room(self):
        res = random_position_in_room()
        assert len(res) == 3
        assert np.all(ROOM_SIZE[0] <= res)
        assert np.all(ROOM_SIZE[1] > res)
