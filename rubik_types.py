from enum import IntEnum
import numpy as np


# Enumeration of rubik's colours
# NOTE: WHITE is always "up"
class Colour(IntEnum):
    NULL = 0
    WHITE = 1
    RED = 2
    BLUE = 3
    ORANGE = 4
    GREEN = 5
    YELLOW = 6


# constants DO NOT TOUCH!
WHITE_AXIS = np.array([0, 0, 1])
RED_AXIS = np.array([0, 1, 0])
GREEN_AXIS = np.array([1, 0, 0])
ORANGE_AXIS = np.array([0, -1, 0])
BLUE_AXIS = np.array([-1, 0, 0])
YELLOW_AXIS = np.array([0, 0, -1])
