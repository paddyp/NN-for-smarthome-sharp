from utils.interfaces import get_random_relevance, RELEVANCE
from fixture import SMART_DEVICES, MAX_INTERFACE_SLOTS, INTERFACES
from utils.position import (
    random_smart_device, 
    random_position_in_room, 
    calc_direction_vector, 
    calc_angle_between_position_and_device,
    calc_distance_for_position_in_room
)

from utils.time import TimeFaker
import random 


def _randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

def szenario_1_data(loop=1): 
    # show random on devices and want this view
    out = []
    res = []
    for _ in range(loop): 
        temp_out = []
        smart_device = random_smart_device()
        rand_pos = random_position_in_room()
        direction_vector = calc_direction_vector(smart_device, rand_pos)
        temp_out.extend(direction_vector)
        angles = []
        distances = []
        rand_values = []
        for s_key, s_value in SMART_DEVICES.items(): 
            temp_direction_vector = calc_direction_vector((s_key,s_value),rand_pos,add_noise=False)
            temp_angle = calc_angle_between_position_and_device(direction_vector, s_value['position'], rand_pos)
            temp_distance = calc_distance_for_position_in_room(temp_direction_vector)
            angles.append(temp_angle)
            distances.append(temp_distance)
            rand_values.append(_randrange_float(*s_value["values"]))
        temp_out.extend(angles)
        temp_out.extend(distances)
        temp_out.append(TimeFaker().random_datetime.isoformat())
        temp_out.extend(rand_values)
        out.append(temp_out)
        device_relevance = [get_random_relevance(RELEVANCE['irrelevant']) for _ in range(len(SMART_DEVICES.keys()))]
        device_relevance[list(SMART_DEVICES.keys()).index(smart_device[0])] = get_random_relevance(RELEVANCE['high'])
        res.extend(device_relevance)
        
        interfaces = []
        for i in range(MAX_INTERFACE_SLOTS): 
            for interface in INTERFACES: 
                # check if interface has to be relevante 
                _, smart_device_values = smart_device
                if len(smart_device_values["scenarios"][1]) > i: 
                    if type(smart_device_values["scenarios"][1][i]) == type(interface):
                        interfaces.extend(smart_device_values["scenarios"][1][i].vector())
                    else: 
                        interfaces.extend(interface().vector())
                else: 
                    interfaces.extend(interface().vector())
        res.append(interfaces)
    return (out, res)
