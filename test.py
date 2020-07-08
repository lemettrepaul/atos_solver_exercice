import solver as so
import solver_brut as sob
import numpy as np


def generate_symmetric_matrix(N):
    m = np.random.uniform(-20, 20, size=(N, N))
    m_symm = (m + m.transpose()) / 2
    return m_symm


# Test
print("Test 1 :")
# generate a symmetric matrix and print result of simulated annealing and brut force
Q = generate_symmetric_matrix(3)
print("Q :\n", Q)
s = so.Solver()
sb = sob.SolverBrut()
x0 = s.x_init(Q)

print("annealing min : ", s.annealing_min(Q, x0, 100, 2000, 0.90))
print("annealing max : ", s.annealing_max(Q, x0, 100, 2000, 0.90))

brut = sb.brut_force(Q)

print("brut min : ", brut[0])
print("brut max : ", brut[1])
print("brut min value : ", brut[2])
print("brut max value : ", brut[3])

print("-----------------------------------------------------")
print("Test 2 : ")
# test with a define matrix
Q = np.array([[1, -1, 2, 1],
              [-1, -3, 5, 8],
              [2, 5, 2, -1],
              [1, 8, -1, -2]])

x0 = s.x_init(Q)
print("x0 : ", x0)

print("annealing min : ", s.annealing_min(Q, x0, 100, 2000, 0.95))
print("annealing max : ", s.annealing_max(Q, x0, 100, 2000, 0.95))

brut = sb.brut_force(Q)
print("brut min : ", brut[0])
print("brut max : ", brut[1])
print("brut min value : ", brut[2])
print("brut max value : ", brut[3])

print("-----------------------------------------------------")
print("Test 3")
# Test n_iter times and print the number of good guess
good_max = 0
good_min = 0
n_iter = 200
for i in range(n_iter):
    Q = generate_symmetric_matrix(3)
    x0 = s.x_init(Q)
    r_min = s.annealing_min(Q, x0, 100, 2000, 0.90)
    r_max = s.annealing_max(Q, x0, 100, 2000, 0.95)
    brut = sb.brut_force(Q)

    if (brut[0] == r_min).all():
        good_min += 1
    if (brut[1] == r_max).all():
        good_max += 1
print("good max : ", good_max)
print("success en %: ", (good_max / n_iter) * 100)
print("good min : ", good_min)
print("success en %: ", (good_min / n_iter) * 100)

print("-----------------------------------------------------")
print("generic test")
# Parameters
size = 6
Q = generate_symmetric_matrix(size)
print(Q)
x0 = s.x_init(Q)
nb_iter = 300
t_init = 4000  # initial temperature
cool = 0.99  # temperature cooldown coefficient

# Try
r_min = s.annealing_min(Q, x0, nb_iter, t_init, cool)
r_max = s.annealing_max(Q, x0, nb_iter, t_init, cool)
brut = sb.brut_force(Q)

print("annealing min : ", r_min)
print("brut min : ", brut[0])
print("annealing max : ", r_max)
print("brut max : ", brut[1])
