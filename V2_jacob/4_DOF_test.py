from Robotic_arm import *
from calculations_dh import *
from inv_kine import *
import numpy as np
from math import pi

qc = np.array([0., 0., 0., 0.])
T = np.array([0.0, 0.0, 0.0, 0.0])
ub = np.array([pi / 2, pi / 2, pi / 2, pi / 2])
lb = np.array([-pi / 2, -pi / 2, -pi / 2, -pi / 2])
theta = np.array([0.0, 0.0, 0.0, 0.0])
alpha = np.array([0.0, 0.0, 0.0, 0.0])
offset = np.array([0.0, 0.0, 0.0, 0.0])
d = np.array([0.0, 0.0, 0.0, 0.0])
a = np.array([0.5, 0.5, 0.5, 0.5])
typee = np.array(['r', 'r', 'r', 'r'])
base = np.array([[0.0], [0.0], [0.0], [0.0]])

arm = Robotic_arm(base, theta, d, a, alpha, offset, qc, typee, jac, T, ub, lb)

for j in np.arange(0.5, 1.7, 0.1):
    q, k, err = inv_kine(arm, np.array([[j], [0.0], [0.0]]))
    selfUpdate(arm, q)
    print(np.degrees(q))
    v, t = f_kine_ee(arm, q)
