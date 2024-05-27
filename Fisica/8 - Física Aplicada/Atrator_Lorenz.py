import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definindo as equações do Atrator de Lorenz
def lorenz(state, t):
    x, y, z = state  # Desempacotando o estado
    sigma = 10
    rho = 28
    beta = 8/3
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# Estado inicial (posição no espaço 3D)
state0 = [1.0, 1.0, 1.0]

# Tempo
t = np.arange(0.0, 40.0, 0.01)

# Resolvendo o sistema de equações diferenciais
states = odeint(lorenz, state0, t)

# Plotando
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(states[:,0], states[:,1], states[:,2])
plt.show()
