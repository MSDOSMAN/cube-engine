import rubiks as r
import rubiks2 as r2
import numpy as np
import rubik_types as t


def main():
    # cube = r.Cube()
    # cube.internal_rot(0)
    # print("STOP")
    block = r2.Block(
        np.array([1, 1, 1]), np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
        np.array([t.Colour.WHITE, t.Colour.GREEN, t.Colour.ORANGE]))


if __name__ == "__main__":
    main()