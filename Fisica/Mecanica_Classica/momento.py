import numpy as np

# Função para calcular o momento na forma integral
def momento_integral(inicio, fim, funcao, num_intervalos):
    intervalo = (fim - inicio) / num_intervalos
    xi = np.linspace(inicio, fim, num_intervalos)
    soma = np.sum(xi * funcao(xi) * intervalo)
    return soma

# Função para calcular o momento na forma diferencial
def momento_diferencial(funcao, x):
    return x * funcao(x)

# Função exemplo
def funcao_exemplo(x):
    return np.sin(x)  # Qualquer função pode ser utilizada aqui

# Parâmetros
inicio = 0.0  # Início do intervalo
fim = np.pi  # Fim do intervalo (pi)
num_intervalos = 1000  # Número de intervalos para o cálculo integral
ponto = 1.0  # Ponto onde calcular o momento diferencial

# Cálculo do momento na forma integral
momento_integral_resultado = momento_integral(inicio, fim, funcao_exemplo, num_intervalos)
print("Momento na forma integral:", momento_integral_resultado)

# Cálculo do momento na forma diferencial
momento_diferencial_resultado = momento_diferencial(funcao_exemplo, ponto)
print("Momento na forma diferencial em x =", ponto, ":", momento_diferencial_resultado)
