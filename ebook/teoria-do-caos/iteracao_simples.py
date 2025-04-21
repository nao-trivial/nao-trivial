x = 1000  # Valor inicial (ex: dinheiro, população)
historico = [x] + [x := 0.7 * x + 50 for _ in range(20)]  # Dinâmica: x_{n+1} = 0.7x_n + 50
print(f"EVOLUÇÃO: {historico}")  # Trajetória do sistema


