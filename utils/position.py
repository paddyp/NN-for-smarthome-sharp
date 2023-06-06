# This util is only for position calculation
import numpy as np

from fixture import ROOM_SIZE, SMART_DEVICES


def random_smart_device():
    # choose random smart device
    random_smart_device_key = np.random.choice(list(SMART_DEVICES.keys()))
    return (random_smart_device_key, SMART_DEVICES[random_smart_device_key])


def random_position_in_room():
    # get random x,y,z position of smarphone
    return np.random.uniform(ROOM_SIZE[0], ROOM_SIZE[1])


def calc_direction_vector(
    smart_device: tuple, position_point: np.array, add_noise=True
):
    _, smart_device_value = smart_device
    smart_device_point = smart_device_value["position"]
    # add noise to smart_device_point
    if add_noise:
        noise = np.random.normal(
            0, smart_device_value["noise"] / 2, smart_device_point.shape
        )
        smart_device_point = smart_device_point + noise
    # calc direction vector
    direction_vector = smart_device_point - position_point
    return direction_vector


def calc_distance_for_position_in_room(direction_vector: np.array):
    # calc distance for given direction_vector
    return np.linalg.norm(direction_vector)


def unit_vector(vector: np.array):
    """Returns the unit vector of the vector."""
    return vector / np.linalg.norm(vector)


def calc_angle_between_position_and_device(
    direction_vector: np.array, device_position: np.array, position_in_room: np.array
):
    direct_direction_vector = device_position - position_in_room
    return np.arccos(
        np.clip(
            np.dot(unit_vector(direct_direction_vector), unit_vector(direction_vector)),
            -1.0,
            1.0,
        )
    )
