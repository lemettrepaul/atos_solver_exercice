import numpy as np


def array_to_int(x):
    x_str = ''.join(str(d) for d in x)
    return int(x_str, 2)


def int_to_array(n, width):
    x_str = bin(n)
    return np.array([int(e) for e in x_str[2:].zfill(width)])


if __name__ == "__main__":
    print(array_to_int(np.array([0, 0, 1, 0, 1, 1])))
    print(int_to_array(11, 6))
