import numpy as np
import matplotlib.pyplot as plt

# Tamanho da imagem
width, height = 500, 500

# Cria uma imagem de exemplo (grid)
def create_grid_image(width, height):
    image = np.zeros((height, width))
    
    # Linhas verticais (a cada 20 pixels)
    for x in range(0, width, 20):
        image[:, x] = 1.0
    
    # Linhas horizontais (a cada 20 pixels)
    for y in range(0, height, 20):
        image[y, :] = 1.0
    
    # Adiciona um ponto central
    image[height//2, width//2] = 1.0
    return image

# Transformação de inversão (w = 1/z)
def inversion_transform(x, y):
    """Aplica a transformação de inversão em coordenadas (x, y)"""
    r_squared = x**2 + y**2
    # Evita divisão por zero
    if r_squared < 1e-10:
        return 0, 0
    u = x / r_squared
    v = -y / r_squared
    return u, v

# Cria a imagem original
original_image = create_grid_image(width, height)

# Prepara a imagem transformada
transformed_image = np.zeros((height, width))

# Define o intervalo das coordenadas (plano complexo)
scale = 2.0
for i in range(height):
    for j in range(width):
        # Converte pixel para coordenadas do plano complexo
        x = scale * (j - width/2) / (width/2)
        y = scale * (height/2 - i) / (height/2)  # Inverte o eixo y
        
        # Aplica a transformação
        u, v = inversion_transform(x, y)
        
        # Converte de volta para coordenadas de pixel
        j_new = int((u/scale) * (width/2) + width/2)
        i_new = int(height/2 - (v/scale) * (height/2))
        
        # Se estiver dentro dos limites, copia o valor
        if 0 <= i_new < height and 0 <= j_new < width:
            transformed_image[i_new, j_new] = original_image[i, j]

# Plot
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(original_image, cmap='gray', extent=[-scale, scale, -scale, scale])
plt.title('Imagem Original')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(122)
plt.imshow(transformed_image, cmap='gray', extent=[-scale, scale, -scale, scale])
plt.title('Imagem Transformada (Inversão w=1/z)')
plt.xlabel('u')
plt.ylabel('v')

plt.tight_layout()
plt.show()