import numpy as np

import utils.interfaces as interfaces

# the possibe position in the Room alon 4m lenght, 6m width.
# The minimum height from the floor is 50cm and Maximum 1.8 m height
# The human in a casual way does not use a smartphone out this high range
ROOM_SIZE = ((0, 0, 0.5), (4.0, 6.0, 1.8))

# Defines the maximum slots shown at the smartphone
MAX_INTERFACE_SLOTS = 1

INTERFACES = [
    interfaces.SwitchInterface,
    interfaces.SliderInterface,
    interfaces.ColorchooserInterface,
    interfaces.StateInterface,
]

SMART_DEVICES = {
    "H1": {
        "id": 0,
        "name": "Heizkoerper 1",
        "position": np.array([0, 0.75, 0.50]),
        "noise": 0.05,
        "values": (14.0, 36.0, 0.5),
        "additional": [],
        "scenarios": {1: [interfaces.SliderInterface]},
    },
    "H2": {
        "id": 1,
        "name": "Heizkoerper 2",
        "position": np.array([0, 2.75, 0.50]),
        "noise": 0.05,
        "values": (14.0, 36.0, 0.5),
        "additional": [],
        "scenarios": {1: [interfaces.SliderInterface]},
    },
    "F1": {
        "id": 2,
        "name": "Fenster 1",
        "position": np.array([0, 0.75, 1.50]),
        "noise": 0.05,
        "values": (0, 100, 10),
        "additional": [],
        "scenarios": {1: [interfaces.SwitchInterface]},
    },
    "F2": {
        "id": 3,
        "name": "Fenster 2",
        "position": np.array([0, 2.75, 1.50]),
        "noise": 0.05,
        "values": (0, 100, 10),
        "additional": [],
        "scenarios": {1: [interfaces.SwitchInterface]},
    },
    "L1": {
        "id": 4,
        "name": "Lampe 1",
        "position": np.array([3.00, 0.75, 2.50]),
        "noise": 0.10,
        "values": (0, 100, 10),
        "additional": [
            "RGB",
        ],
        "scenarios": {1: [interfaces.SwitchInterface]},
    },
    "L2": {
        "id": 5,
        "name": "Lampe 2",
        "position": np.array([3.00, 2.75, 2.50]),
        "noise": 0.10,
        "values": (0, 100, 10),
        "additional": [
            "RGB",
        ],
        "scenarios": {1: [interfaces.SwitchInterface]},
    },
}

TIME_RANGES = {
    "MORNING": ((6, 0), (12, 0)),
    "NOON": ((12, 0), (17, 0)),
    "EVENING": ((17, 0), (22, 0)),
    "NIGHT": ((22, 0), (6, 0)),
    "AFTERWORK": ((17, 0), (24, 0)),
    "WORK": ((8, 0), (17, 0)),
}
