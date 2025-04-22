import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros da animação
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'o', markersize=1, alpha=0.5)

# Configurações iniciais do gráfico
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Transição ao Caos: Equação Logística")
ax.set_xlabel("Iterações")
ax.set_ylabel("Valor de x")

# Função logística
def logistic_map(r, x):
    return r * x * (1 - x)

# Gerador de frames
def update(frame):
    r = frame
    x = 0.5
    x_vals = []

    # Queima inicial (para estabilizar)
    for _ in range(100):
        x = logistic_map(r, x)

    # Coleta de dados para plotar
    for _ in range(100):
        x = logistic_map(r, x)
        x_vals.append(x)

    xdata = [r] * len(x_vals)
    ydata = x_vals
    ln.set_data(xdata, ydata)
    ax.set_title(f"r = {r:.3f}")
    return ln,

# Geração da animação
ani = FuncAnimation(
    fig, update, frames=np.linspace(2.5, 4.0, 300), blit=True, interval=30
)

# Salvar como vídeo
ani.save("logistic_chaos.mp4", fps=30, dpi=300)

plt.show()
