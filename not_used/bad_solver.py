import random as random
import numpy as np
from not_used import utils as u


def left_neighbour(x):
    comparison = x == np.zeros(len(x))
    equal_arr = comparison.all()
    if equal_arr:
        return np.full(len(x), 1, dtype=int)
    x_int = u.array_to_int(x)
    x_int_n = x_int - 1
    x_n = u.int_to_array(x_int_n, len(x))
    return x_n


def right_neighbour(x):
    comparison = x == np.full((1, len(x)), 1, dtype=int)
    equal_arr = comparison.all()
    if equal_arr:
        return np.zeros(len(x), dtype=int)
    x_int = u.array_to_int(x)
    x_int_n = x_int + 1
    x_n = u.int_to_array(x_int_n, len(x))
    return x_n


def neighbour(x):
    p = random.random()
    if p < 1 / 2:
        return left_neighbour(x)
    else:
        return right_neighbour(x)


class Solver:
    def E(self, x, Q):
        return np.dot(x.transpose(), np.dot(Q, x))

    def recuit_max(self, Q, x0, nb_iter, t_init, cool):
        x = x0
        t = t_init
        for i in range(nb_iter):
            ex = self.E(x, Q)
            n = neighbour(x)
            en = self.E(n, Q)
            de = en - ex
            if de > 0:
                x = n
            elif np.exp(-de / t) < random.random():
                x = n
            t = t * cool
        return x

    def recuit_min(self, Q, x0, nb_iter, t_init, cool):
        x = x0
        t = t_init
        for i in range(nb_iter):
            ex = self.E(x, Q)
            n = neighbour(x)
            en = self.E(n, Q)
            de = en - ex
            if de < 0:
                x = n
            elif np.exp(-de / t) > random.random():
                x = n
            t = t * cool
        return x

    def x_init(self, Q):
        n = len(Q)
        return np.random.randint(2, size=n)


if __name__ == "__main__":
    s = Solver()
    Q = np.array([[1, -1, 2, 1],
                  [-1, -3, 5, 8],
                  [2, 5, 2, -1],
                  [1, 8, -1, -2]])

    print("Test annealing")
    x0 = s.x_init(Q)
    print("x0 : ", x0)

    print("max : ", s.recuit_max(Q, x0, 100, 2000, 0.99))
    print("min : ", s.recuit_min(Q, x0, 100, 2000, 0.99))
