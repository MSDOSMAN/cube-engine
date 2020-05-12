# RUBIKS3.py
# CONSIDERS THE CUBE TO BE 3X3X3 (-1) CONTAINER OF "Blocks", USES MATRIX OPS - probably slower than r2, but more
# elegant for sure
# NOTE: the type hints are *a little* misleading, we are not asking for a CubeNormal instance, per se, but at least
# it gets you looking in the right direction (we want caller to use CubeNormal public attribute...)

import numpy as np
from rubik_types import CubeNormals
from rubik_types import CubeRots
from rubik_types import Colour
import logging as log
from typing import List


class Block:
    """
    A class that represents the smallest constituent of a larger cube structure.

    ...

    Attributes
    ----------
    None public

    Methods
    -------
    transform : CubeRots
        apply 90 degree clockwise rotation corresponding to face_matrix, regardless of whether Block is on that face
        (uses matrix operations)
    proj_transform : CubeNormals
        apply 90 degree clockwise rotation around a colour's normal, regardless of whether Block is on that face (uses
        projection)
    weak_transform : CubeNormals
        apply 90 degree clockwise rotation around a colour's normal, will not apply any transform if Block is not on
        that face (calls transform)
    get_position : None
        Block position getter
    get_norms : None
        Block normals getter
    get_colours : None
        Block colour getter
    validate : None
        Checks status of Block to ensure that its state is possible, returns True if yes, False otherwise
    """

    def __init__(self, position: np.ndarray, norms: np.ndarray, colours: List[Colour]) -> None:
        """
        :param position: spawn position of Block
        :param norms: spawn normals of Block's colours (direction of its colours)
        :param colours: colours that are on the block
        """
        self.__position = position  # internal position of this block. 3D, coords are ints from -1 to 1
        self.__norms = norms  # internal normals that represent the directions in which coloured faces are pointing
        self.__colours = colours  # colours of the block

    def transform(self, face_matrix: CubeRots) -> None:
        """
        :param face_matrix: CubeRots class attribute corresponding to desired face's rotation matrix
        """
        self.__position = np.matmul(face_matrix, self.__position)
        for i in range(0, len(self.__norms)):
            self.__norms[i] = np.matmul(face_matrix, self.__norms[i])

    def proj_transform(self, axis: CubeNormals) -> None:
        """
        :param axis: CubeNormals class attribute corresponding to normal of the desired rotational face
        """
        orthogonal_projection = np.cross(self.__position, axis)
        self.__position = np.add(axis, orthogonal_projection)

        # TODO: Come up with projection way of finding normal transforms
        for i in range(0, len(self.__norms)):
            orthogonal_projection = np.cross(self.__norms[i], axis)
            self.__norms[i] = np.add(axis, orthogonal_projection)

    def weak_transform(self, axis: CubeNormals) -> None:
        """
        :param axis: CubeNormals class attribute corresponding to normal of the desired rotational face
        """

        if np.all(axis == CubeNormals.GREEN_NORMAL) and self.__position[0] == 1:
            self.transform(CubeRots.GREEN_ROT)
        elif np.all(axis == CubeNormals.BLUE_NORMAL) and self.__position[0] == -1:
            self.transform(CubeRots.BLUE_ROT)
        elif np.all(axis == CubeNormals.RED_NORMAL) and self.__position[1] == 1:
            self.transform(CubeRots.RED_ROT)
        elif np.all(axis == CubeNormals.ORANGE_NORMAL) and self.__position[1] == -1:
            self.transform(CubeRots.ORANGE_ROT)
        elif np.all(axis == CubeNormals.WHITE_NORMAL) and self.__position[2] == 1:
            self.transform(CubeRots.WHITE_ROT)
        elif np.all(axis == CubeNormals.YELLOW_NORMAL) and self.__position[2] == -1:
            self.transform(CubeRots.YELLOW_ROT)
        else:
            log.warning("weak_transform: failed to transform block")

    def get_position(self):
        """
        :return: Block's position
        """
        return self.__position

    def get_norms(self):
        """
        :return: Block's normals
        """
        return self.__norms

    def get_colours(self):
        """
        :return: Block's colours
        """
        return self.__colours

    def validate(self) -> bool:
        # TODO: Validate should perform range checks and type checks on Block attributes, return True is everything is
        # TODO: OK, False otherwise
        raise NotImplementedError("Coming soon")
