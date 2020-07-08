import numpy as np
from itertools import product


def all_x(n):
    l_tmp = list(product([0, 1], repeat=n))
    return [np.array(x) for x in l_tmp]


class SolverBrut:

    def brut_force(self, Q):
        n = len(Q)
        min_x = np.zeros(n, dtype=int)
        result_min = np.dot(np.dot(min_x.transpose(), Q), min_x)
        max_x = np.zeros(n, dtype=int)
        result_max = np.dot(np.dot(max_x.transpose(), Q), max_x)
        for x in all_x(n):
            result = np.dot(np.dot(x.transpose(), Q), x)
            if result > result_max:
                max_x = x
                result_max = result
            if result < result_min:
                min_x = x
                result_min = result
        return min_x, max_x, result_min, result_max


if __name__ == "__main__":
    s = SolverBrut()
    # Test 1
    print("Test 1")
    Q1 = np.array([[-2, 1], [1, -1]])
    print(s.brut_force(Q1))

    # Test 2
    print("Test 2")
    Q2 = np.array([[1, -1, 2, 1],
                   [-1, -3, 5, 8],
                   [2, 5, 2, -1],
                   [1, 8, -1, -2]])
    print(s.brut_force(Q2))
