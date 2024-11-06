# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import qutip
import numpy as np

state = np.array([[1], [0]])

RY = lambda theta: np.array([[np.cos(theta/2), -np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]])
RX = lambda theta: np.array([[np.cos(theta/2), -1j*np.sin(theta/2)], [-1j*np.sin(theta/2), np.cos(theta/2)]])
RZ = lambda theta: np.array([[np.exp(-1j*(theta/2)), 0], [0, np.exp(1j*(theta/2))]])

angles = [0, np.pi/4, np.pi/2, (3*np.pi)/4, np.pi, -np.pi/4, -np.pi/2, -(3*np.pi)/4]


def plot(bloch, state):
    bloch.add_states(qutip.Qobj(list(state)))


# RY
ry_rotations = qutip.Bloch()
for angle in angles:
    plot(ry_rotations, np.dot(RY(angle), state))
ry_rotations.save("ry-rotations.png")
ry_rotations.show()

#RX
rx_rotations = qutip.Bloch()
for angle in angles:
    plot(rx_rotations, np.dot(RX(angle), state))
rx_rotations.save("rx-rotations.png")
rx_rotations.show()


#RZ
for angle in angles:
    print(f"angle: {angle}")
    print(f"state: {np.dot(RZ(angle), state)}", end="\n\n")