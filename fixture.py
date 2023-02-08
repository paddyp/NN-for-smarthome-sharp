import numpy as np
import utils.interfaces as interfaces

# the possibe position in the Room alon 4m lenght, 6m width. 
# The minimum height from the floor is 50cm and Maximum 1.8 m height 
# The human in a casual way does not use a smartphone out this high range  
ROOM_SIZE = ((0,0,0.5),(4.0,6.0,1.8))

# Defines the maximum slots shown at the smartphone
MAX_INTERFACE_SLOTS = 3

INTERFACES  = [
    interfaces.SwitchInterface, 
    interfaces.SliderInterface, 
    interfaces.ColorchooserInterface, 
    interfaces.StateInterface
]

SMART_DEVICES = {
    "H1": {
        "name": "Heizkoerper 1",
        "position": np.array([0,75,50]), 
        "noise": 50, 
        "values": (14.0, 36.0, 0.5),
        "additional": [], 
        "scenarios": {
            1: [
                interfaces.SliderInterface(relevance='high', current_value=14.0, min_value=14.0, max_value=36.0, step_value=1),
                interfaces.SwitchInterface(relevance='high', current_value=14.0, on_value=36.0, off_value=14.0), 
            ]
        },
    }, 
    "H2": {
        "name": "Heizkoerper 2", 
        "position": np.array([0,275,50]), 
        "noise": 50,
        "values": (14.0, 36.0, 0.5),
        "additional": [],
         "scenarios": {
            1: [
                interfaces.SwitchInterface(relevance='high', current_value=14.0, on_value=36.0, off_value=14.0),
                interfaces.SliderInterface(relevance='high', current_value=14.0, min_value=14.0, max_value=36.0, step_value=1),
                 
            ]
        },
    }, 
    "F1": {
        "name": "Fenster 1", 
        "position": np.array([0,75,150]), 
        "noise": 50, 
        "values": (0,100,10),
        "additional": [],
         "scenarios": {
            1: [
                interfaces.SwitchInterface(relevance='high', current_value=14.0, on_value=36.0, off_value=14.0),
                interfaces.SliderInterface(relevance='high', current_value=14.0, min_value=14.0, max_value=36.0, step_value=1),
                 
            ]
        },
    },
    "F2": {
        "name": "Fenster 2", 
        "position": np.array([0,275,150]), 
        "noise": 50, 
        "values": (0,100,10),
        "additional": [],
         "scenarios": {
            1: [
                interfaces.SwitchInterface(relevance='high', current_value=14.0, on_value=36.0, off_value=14.0),
                interfaces.SliderInterface(relevance='high', current_value=14.0, min_value=14.0, max_value=36.0, step_value=1),
                 
            ]
        },
    },
    "L1": {
        "name": "Lampe 1", 
        "position": np.array([300,75,250]),  
        "noise": 10, 
        "values": (0,100,10), 
        "additional": ["RGB",],
         "scenarios": {
            1: [
                interfaces.SwitchInterface(relevance='high', current_value=14.0, on_value=36.0, off_value=14.0),
                interfaces.SliderInterface(relevance='high', current_value=14.0, min_value=14.0, max_value=36.0, step_value=1),
                 
            ]
        },
    },
    "L2": {
        "name": "Lampe 2", 
         "position": np.array([300,275,250]), 
        "noise": 10,
        "values": (0,100,10),
        "additional": ["RGB",],
         "scenarios": {
            1: [
                interfaces.SwitchInterface(relevance='high', current_value=14.0, on_value=36.0, off_value=14.0),
                interfaces.SliderInterface(relevance='high', current_value=14.0, min_value=14.0, max_value=36.0, step_value=1),
                 
            ]
        },
    },
}

TIME_RANGES = {
    "MORNING": ((6,0), (12,0)),
    "NOON": ((12,0), (17,0)), 
    "EVENING": ((17,0), (22,0)), 
    "NIGHT": ((22,0), (6,0)), 
    "AFTERWORK": ((17,0), (24,0)),
    "WORK": ((8,0), (17,0))
}

