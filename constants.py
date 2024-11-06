import numpy as np

zero_state = np.array([[1], [0]])
half_state = (1/np.sqrt(2)) * np.array([[1], [1]])

RY = lambda theta: np.array([[np.cos(theta/2), -np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]])
RX = lambda theta: np.array([[np.cos(theta/2), -1j*np.sin(theta/2)], [-1j*np.sin(theta/2), np.cos(theta/2)]])
RZ = lambda theta: np.array([[np.exp(-1j*(theta/2)), 0], [0, np.exp(1j*(theta/2))]])

angles = [0, np.pi/4, np.pi/2, (3*np.pi)/4, np.pi, -(3*np.pi)/4, -np.pi/2, -np.pi/4]
