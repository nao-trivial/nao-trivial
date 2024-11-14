from coleta_dados_peticao import BancoDadosPeticao

# Função para inserir uma nova entrevista
def inserir_entrevista(banco_dados):
    nome = input("Nome do entrevistado: ")
    idade = int(input("Idade: "))
    bairro = input("Bairro de residência: ")
    renda_media_familiar = float(input("Renda média familiar: "))
    raca = input("Raça que se considera: ")
    genero = input("Gênero: ")
    conhece_parque = input("Conhece o parque (Sim/Não): ").strip().lower() == "sim"
    importancia_ecologica = input("Qual a importância ecológica do parque? ")
    concorda_peticao = input("Concorda com a petição para impedir o desmatamento? (Sim/Não): ").strip().lower() == "sim"
    comentario = input("Comentário adicional: ")

    banco_dados.inserir_entrevista(
        nome, idade, bairro, renda_media_familiar, raca, genero, conhece_parque, 
        importancia_ecologica, concorda_peticao, comentario
    )

# Função para visualizar todas as entrevistas
def visualizar_entrevistas(banco_dados):
    entrevistas = banco_dados.visualizar_entrevistas()
    for entrevista in entrevistas:
        print(f"ID: {entrevista[0]}, Nome: {entrevista[1]}, Idade: {entrevista[2]}, Bairro: {entrevista[3]}, Conhece o parque: {entrevista[4]}, Concorda com a petição: {entrevista[5]}")
    
    # Permite visualizar detalhes de uma entrevista específica
    escolha = input("\nDeseja ver os detalhes de alguma entrevista? (S/N): ").strip().lower()
    if escolha == "s":
        entrevista_id = int(input("Digite o ID da entrevista: "))
        detalhes = banco_dados.visualizar_detalhes_entrevista(entrevista_id)
        if detalhes:
            print(f"Nome: {detalhes[0]}\nIdade: {detalhes[1]}\nBairro: {detalhes[2]}\nRenda média familiar: {detalhes[3]}\nRaça: {detalhes[4]}\nGênero: {detalhes[5]}\nImportância ecológica: {detalhes[6]}\nComentário: {detalhes[7]}")
        else:
            print("Entrevista não encontrada.")

# Função principal que exibe o menu
def menu():
    banco_dados = BancoDadosPeticao()
    
    while True:
        print("\nMenu Principal:")
        print("1. Inserir nova entrevista")
        print("2. Visualizar entrevistas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            inserir_entrevista(banco_dados)
        elif opcao == "2":
            visualizar_entrevistas(banco_dados)
        elif opcao == "3":
            banco_dados.fechar_conexao()
            print("Conexão com o banco de dados encerrada.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
if __name__ == "__main__":
    menu()
