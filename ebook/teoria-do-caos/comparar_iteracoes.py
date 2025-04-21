import numpy as np
import matplotlib.pyplot as plt

def compara_sequencias(a_list, b_list, x0_list, n_iteracoes=15):
    """Compara múltiplas sequências em subplots."""
    fig, axs = plt.subplots(len(a_list), 1, figsize=(10, 3*len(a_list)), sharex=True)
    for i, (a, b, x0) in enumerate(zip(a_list, b_list, x0_list)):
        sequencia = [x0]
        for _ in range(n_iteracoes):
            sequencia.append(a * sequencia[-1] + b)
        axs[i].plot(sequencia, 'ro-', markersize=4)
        axs[i].set_title(f'$a = {a}$, $b = {b}$, $x_0 = {x0}$')
        axs[i].grid(True)
    plt.xlabel('Iteração (n)')
    fig.tight_layout()
    plt.show()

# Exemplo:
compara_sequencias(
    a_list=[0.5, -1.0, 1.5], 
    b_list=[2.0, 3.0, -1.0], 
    x0_list=[0.0, 0.0, 0.9]
)