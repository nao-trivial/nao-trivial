import os

# Define o caminho para o arquivo `legenda.txt`
caminho_arquivo = os.path.join('Fisica', 'Relatividade Geral', 'Tensor de Riemann', 'legenda.txt')

try:
    # Abre o arquivo em modo de leitura e exibe o conteúdo
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo de legenda.txt:\n")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo legenda.txt não foi encontrado. Verifique se o caminho e o arquivo estão corretos.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar acessar o arquivo: {e}")
