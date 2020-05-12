import rubiks as r
import rubiks2 as r2
import rubiks3 as r3
import numpy as np
import rubik_types as t


def main():
    block = r3.Block(
        np.array([1, 1, 1]), np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
        np.array([t.Colour.WHITE, t.Colour.RED, t.Colour.GREEN])
    )

    block.transform(t.WHITE_ROT)
    block.transform(t.WHITE_ROT)
    block.transform(t.WHITE_ROT)
    block.transform(t.WHITE_ROT)



if __name__ == "__main__":
    main()
