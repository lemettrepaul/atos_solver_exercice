import decimal
import random as random
import numpy as np


# return a random neighbour of x (can be x)
def neighbour(x):
    return np.array([random.randint(0, 1) for i in range(len(x))])


class Solver:
    # the f function
    def E(self, x, Q):
        return np.dot(x.transpose(), np.dot(Q, x))

    # method which search the maximum of E with simulated annealing
    def annealing_max(self, Q, x0, nb_iter, t_init, cool):
        x = x0
        t = t_init
        for i in range(nb_iter):
            ex = self.E(x, Q)
            n = neighbour(x)
            en = self.E(n, Q)
            de = en - ex
            if de > 0:
                x = n
            elif np.exp(decimal.Decimal(-de / t)) < random.random():
                x = n
            t = t * cool
        return x

    # method which search the minimum of E with simulated annealing
    def annealing_min(self, Q, x0, nb_iter, t_init, cool):
        x = x0
        t = t_init
        for i in range(nb_iter):
            ex = self.E(x, Q)
            n = neighbour(x)
            en = self.E(n, Q)
            de = en - ex
            if de < 0:
                x = n
            elif np.exp(decimal.Decimal(-de / t)) > random.random():
                x = n
            t = t * cool
        return x

    # create an initial x0
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

    print("max : ", s.annealing_max(Q, x0, 100, 2000, 0.99))
    print("min : ", s.annealing_min(Q, x0, 100, 2000, 0.99))
