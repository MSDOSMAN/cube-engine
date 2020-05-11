## RUBIKS3.py
## CONSIDERS THE CUBE TO BE 3X3X3 (-1) CONTAINER OF "Blocks", USES MATRIX OPS - probably slower than r2, but more
## elegant for sure

import numpy as np
import rubik_types as t


class Block:
    def __init__(self, position, norms, colours):
        self.__position = position
        self.__norms = norms
        self.__colours = colours

    def transform(self, axis):
        # TODO: add in normal rotation and TEST PLEASE
        # TODO: comment this class after those two tasks have been completed and implement a cube
        # NOTE: DECIDE WHICH ONE OF THE RUBIK'S IMPLEMENTATIONS GET PUT INTO ARCHIVE, MY VOTE IS NOT r3
        if np.all(axis == t.WHITE_NORMAL) | np.all(axis == t.YELLOW_NORMAL):
            self.__position = np.matmul(t.Z_ROT, self.__position)
        elif np.all(axis == t.GREEN_NORMAL) | np.all(axis == t.BLUE_NORMAL):
            self.__position = np.matmul(t.X_ROT, self.__position)
        elif np.all(axis == t.RED_NORMAL) | np.all(axis == t.ORANGE_NORMAL):
            self.__position = np.matmul(t.Y_ROT, self.__position)
        else:
            raise ValueError(
                "axis argument invalid or internal position is corrupted, are you using 'rubik_types' axis constants?")


