## RUBIKS.py
## CONSIDERS THE CUBE TO BE 6 3x3 MATRICES, ROTATIONS ARE SWAPPING ARRAY VALUES, NO MATRIX OPS

from rubik_types import Colour as c
import numpy as np


# Cube: main cube class
# TODO: Maybe add dim parameter to __init__ as to allow for non-3x3x3 cubes?
# NOTE: np.matrix is apparently not recommended anymore
class Cube:
    # lookup table for which order to consider shuffles when face (index) is rotated
    # i.e., index 0 = white face... r in white face moves red face into green, which
    # itself is moved into orange, which itself is moved into blue, which is moved back
    # into red
    __effect_lookup = [[1, 4, 3, 2], [0, 2, 5, 4], [0, 1, 5, 3], [0, 4, 5, 2],
                       [0, 3, 5, 1], [1, 2, 3, 4]]

    def __init__(self):
        self.__faces = []

        # create "solved" cube
        # NOTE: visualisations will always be white facing you and red "up" -> clockwise
        self.__faces.append(self.__make_face(self, c.WHITE))
        self.__faces.append(self.__make_face(self, c.RED))
        self.__faces.append(self.__make_face(self, c.GREEN))
        self.__faces.append(self.__make_face(self, c.ORANGE))
        self.__faces.append(self.__make_face(self, c.BLUE))
        self.__faces.append(self.__make_face(self, c.YELLOW))

    @staticmethod
    def __make_face(self, col):
        # val = int(col)
        return np.array([[col, col, col], [col, col, col], [col, col, col]],
                        np.int)

    # ROTATIONS
    # NOTE: all rotations are handled by __internal_rot. All rotations are pretty much
    # the same but differ by which face they are "looking at".
    # DEBUGGING: SHOULD BE PRIVATE!
    def internal_rot(self, face):
        self.__faces[face] = np.rot90(self.__faces[face])

    # PUBLIC ROTATIONS
    # NOTE: all of these are considering you looking at the white face. Letter prefixes
    # correspond to David Singmaster's Cube Notation: https://ruwix.com/the-rubiks-cube/notation/
    def f_rot(self):
        pass

    def r_rot(self):
        pass

    def u_rot(self):
        pass

    def l_rot(self):
        pass

    def d_rot(self):
        pass
