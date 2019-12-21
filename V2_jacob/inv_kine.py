import numpy as np
from calculations_dh import *
from Robotic_arm import *


def inv_kine(r, p, treshold=0.01, max_iter=1000):
    q = r.qc
    T = f_kine(r, q)
    x = np.array([[T[3, 0, 3]], [T[3, 1, 3]], [T[3, 2, 3]]])
    jacob = jac(r, q)
    # print(jacob)
    # print("b")
    # print(q)
    # print("b")
    current_iter = 1

    while True:
        current_iter = current_iter + 1
        # problem is in delta pos in a word in x variable
        inv_jacob = np.linalg.pinv(jacob)
        delta_pos = np.subtract(p, x)

        delta_angle = np.dot(inv_jacob, delta_pos)

        for i in range(6):
            q[i] = q[i] + delta_angle[i][0]
        for i in range(6):
            if (q[i] < r.lb[i]):
                q[i] = r.lb[i]
            if (q[i] > r.ub[i]):
                q[i] = r.ub[i]

        y, x = f_kine_ee(r, q)
        delta_pos = np.subtract(p, x)
        jacob = jac(r, q)

        err = np.linalg.norm(delta_pos)
        if err < treshold or current_iter > max_iter:
            break

    return q, current_iter, err
