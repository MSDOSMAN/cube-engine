## RUBIKS2.py
## CONSIDERS THE CUBE TO BE 3X3X3 (-1) CONTAINER OF "Blocks", ALLOWS FOR MATRIX OPS

import numpy as np
from rubik_types import Colour as c


class Block:
    def __init__(self, position, norms, colours):
        self.__position = position
        self.__norms = norms
        self.__colours = colours

    def __negate_and_swap(self, l_idx, r_idx): # will negate the left index and swap it with right
      self.__position[l_idx] *= -1
      self.__position[l_idx] = self.__position[l_idx] - self.__position[r_idx]
      self.__position[r_idx] = self.__position[l_idx] + self.__position[r_idx]
      self.__position[l_idx] = self.__position[r_idx] - self.__position[l_idx]
      
    def transform(self, axis):
        if axis[0] == 1 and self.__position[0] == 1: # x = 1, Green face
          self.__negate_and_swap(1, 2) ## FINISH ME!
          # ADD NORMAL CHANGE HERE!
        elif axis[0] == -1 and self.__position[0] == -1: # x = -1, Blue face
          pass
        elif axis[1] == 1 and self.__position[1] == 1: # y = 1, Red face
          pass
        elif axis[1] == -1 and self.__position[1] == -1: # y = -1, Orange face
          pass
        elif axis[2] == 1 and self.__position[2] == 1: # z = 1, White face
          pass
        elif axis[2] == -1 and self.__position[2] == -1: # z = -1, Yellow face
          pass
        else:
          raise ValueError("axis argument invalid or internal position is corrupted, are you using 'rubik_types' axis constants?")
      


# Cube: main cube class
# TODO: Maybe add dim parameter to __init__ as to allow for non-3x3x3 cubes?
class Cube:
    def __init__(self):
        pass