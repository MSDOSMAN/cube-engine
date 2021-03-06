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


# normal constants, each one corresponds to the absolute orientation of the "solved" side for a given colour
class CubeNormals:
    WHITE_NORMAL = np.array([0, 0, 1])
    RED_NORMAL = np.array([0, 1, 0])
    GREEN_NORMAL = np.array([1, 0, 0])
    ORANGE_NORMAL = np.array([0, -1, 0])
    BLUE_NORMAL = np.array([-1, 0, 0])
    YELLOW_NORMAL = np.array([0, 0, -1])


# constant rotational matrices, each one corresponds to a 90 degrees clockwise rotation "looking" at that face
class CubeRots:
    WHITE_ROT = np.array([[0, 1, 0],
                          [-1, 0, 0],
                          [0, 0, 1]])
    YELLOW_ROT = np.array([[0, -1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])

    GREEN_ROT = np.array([[1, 0, 0],
                          [0, 0, 1],
                          [0, -1, 0]])
    BLUE_ROT = np.array([[1, 0, 0],
                         [0, 0, -1],
                         [0, 1, 0]])

    RED_ROT = np.array([[0, 0, -1],
                        [0, 1, 0],
                        [1, 0, 0]])
    ORANGE_ROT = np.array([[0, 0, 1],
                           [0, 1, 0],
                           [-1, 0, 0]])

