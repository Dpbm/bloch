import matplotlib.pyplot as plt
import qutip
import numpy as np

zero_state = np.array([[1], [0]])

RY = lambda theta: np.array([[np.cos(theta/2), -np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]])
RX = lambda theta: np.array([[np.cos(theta/2), -1j*np.sin(theta/2)], [-1j*np.sin(theta/2), np.cos(theta/2)]])
RZ = lambda theta: np.array([[np.exp(-1j*(theta/2)), 0], [0, np.exp(1j*(theta/2))]])

angles = [0, np.pi/4, np.pi/2, (3*np.pi)/4, np.pi, -np.pi/4, -np.pi/2, -(3*np.pi)/4]

def plot(bloch, state):
    bloch.add_states(qutip.Qobj(list(state)))

fig = plt.figure(constrained_layout=True)
ax1 = fig.add_subplot(1, 3, 1, projection="3d")
ax2 = fig.add_subplot(1, 3, 2, projection="3d")
ax3 = fig.add_subplot(1, 3, 3, projection="3d")

ry_rotations = qutip.Bloch(fig=fig,axes=ax1)
for angle in angles:
    plot(ry_rotations, np.dot(RY(angle), zero_state))
ry_rotations.render()
ax1.set_title("RY Rotations", y=1.3)

rx_rotations = qutip.Bloch(fig=fig,axes=ax2)
for angle in angles:
    plot(rx_rotations, np.dot(RX(angle), zero_state))
rx_rotations.render()
ax2.set_title("RX Rotations", y=1.3)


half_state = (1/np.sqrt(2)) * np.array([[1], [1]])
rz_rotations = qutip.Bloch(fig=fig,axes=ax3)
for angle in angles:
    plot(rz_rotations, np.dot(RZ(angle), half_state))
rz_rotations.render()
ax3.set_title("RZ Rotations", y=1.3)

plt.savefig('rotations.png')
plt.show()
input()
