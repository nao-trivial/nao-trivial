import numpy as np
import matplotlib.pyplot as plt

def cobweb_plot(a, b, x0, n_iterations=20):
    """
    Gera um gráfico de teia de aranha para o mapeamento afim x_{n+1} = a*x_n + b.
    
    Parâmetros:
        a (float): Coeficiente angular.
        b (float): Termo constante.
        x0 (float): Condição inicial.
        n_iterations (int): Número de iterações.
    """
    # Define a função do mapeamento
    def f(x):
        return a * x + b
    
    # Cria pontos para plotar a função e a diagonal
    x_values = np.linspace(min(x0 - 5, -5), max(x0 + 5, 5), 400)
    y_values = f(x_values)
    
    # Configura o gráfico
    plt.figure(figsize=(8, 8))
    plt.plot(x_values, y_values, 'b-', label=f'$x_{{n+1}} = {a}x_n + {b}$')
    plt.plot(x_values, x_values, 'k--', label='$y = x$')
    
    # Simula as iterações e plota a teia de aranha
    x = x0
    for _ in range(n_iterations):
        y = f(x)
        plt.plot([x, x], [x, y], 'r-', alpha=0.5, linewidth=1)  # Linha vertical
        plt.plot([x, y], [y, y], 'r-', alpha=0.5, linewidth=1)  # Linha horizontal
        x = y
    
    plt.scatter([x0], [f(x0)], color='g', s=50, label='$x_0$')
    
    # Destaca o ponto fixo (se existir e for único)
    if a != 1:
        x_fixed = b / (1 - a)
        plt.scatter([x_fixed], [x_fixed], color='purple', s=100, label='Ponto fixo')
    
    plt.title(f'Método da Teia de Aranha\n$x_{{n+1}} = {a}x_n + {b}$, $x_0 = {x0}$')
    plt.xlabel('$x_n$')
    plt.ylabel('$x_{n+1}$')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso:
a = 0.5  # |a| < 1 (atrator)
b = 2
x0 = 0
cobweb_plot(a, b, x0)

# Outros exemplos para testar:
# a = -1 (ciclo de período 2)
# a = 1.5 (repulsor)
# a = 1, b = 0 (infinitos pontos fixos)