import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import qutip
from constants import *


fig = plt.figure(constrained_layout=True)
ax1 = fig.add_subplot(1, 3, 1, projection="3d")
ax2 = fig.add_subplot(1, 3, 2, projection="3d")
ax3 = fig.add_subplot(1, 3, 3, projection="3d")

ry_bloch = qutip.Bloch(fig=fig, axes=ax1)
rx_bloch = qutip.Bloch(fig=fig, axes=ax2)
rz_bloch = qutip.Bloch(fig=fig, axes=ax3)

def animate(step):
    ry_state = np.dot(RY(angles[step]), zero_state)
    rx_state = np.dot(RX(angles[step]), zero_state)
    rz_state = np.dot(RZ(angles[step]), half_state)

    ry_bloch.clear()
    rx_bloch.clear()
    rz_bloch.clear()
    
    ry_bloch.add_states(qutip.Qobj(list(ry_state)))
    rx_bloch.add_states(qutip.Qobj(list(rx_state)))
    rz_bloch.add_states(qutip.Qobj(list(rz_state)))

    ry_bloch.render()
    rx_bloch.render()
    rz_bloch.render()

    ax1.set_title("RY Rotations", y=1.3)
    ax2.set_title("RX Rotations", y=1.3)
    ax3.set_title("RZ Rotations", y=1.3)

    return []

bloch_animation = animation.FuncAnimation(fig, animate, np.arange(8))
bloch_animation.save('rotations.mp4', fps=1)
