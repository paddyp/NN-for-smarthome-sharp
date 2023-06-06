import random

from fixture import INTERFACES, MAX_INTERFACE_SLOTS, SMART_DEVICES
from utils.interfaces import RELEVANCE, get_random_relevance
from utils.position import (
    calc_angle_between_position_and_device,
    calc_direction_vector,
    calc_distance_for_position_in_room,
    random_position_in_room,
    random_smart_device,
)
from utils.time import TimeFaker


def _randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start


# scenario 1
def szenario_1_data(loop=1):
    # show random on devices and want the right interface
    # except special scenario inputs
    out = []
    res = []
    interfaces = []
    for _ in range(loop):
        temp_out = []

        # get a random smart device
        smart_device = random_smart_device()
        # get a random position in the room
        rand_pos = random_position_in_room()
        # calculate direction_vector from random position to smart device
        direction_vector = calc_direction_vector(smart_device, rand_pos)
        # temp_out.extend(direction_vector)
        angles = []  # list of angles of each device
        distances = []  # list of distances from random postion to each device

        # calculate angle and distance for each smart device
        for s_key, s_value in SMART_DEVICES.items():
            temp_direction_vector = calc_direction_vector(
                (s_key, s_value), rand_pos, add_noise=False
            )
            temp_angle = calc_angle_between_position_and_device(
                direction_vector, s_value["position"], rand_pos
            )
            temp_distance = calc_distance_for_position_in_room(temp_direction_vector)
            angles.append(temp_angle)
            distances.append(temp_distance)

        angles /= max(angles)  # normalize angles
        temp_out.extend(angles)  # append angels
        distances /= max(distances)  # normilize distances
        temp_out.extend(distances)  ## append angles

        # add time to data
        # TODO: prevent scenario 2 and 3 time in random datetime
        temp_out.extend(TimeFaker().get_random_datetime_as_list())
        out.append(temp_out)
        temp_res = []
        temp_res_device = [0] * len(list(SMART_DEVICES.keys()))
        temp_res_device[smart_device[1]["id"]] = 1

        temp_res.extend(temp_res_device)

        temp_res_interface = [0] * len(INTERFACES)
        # set relevant interface to 1
        for interface in smart_device[1]["scenarios"][1]:
            temp_res_interface[INTERFACES.index(interface)] = 1

        temp_res.extend(temp_res_interface)
        res.append(temp_res)

    return (out, res)
