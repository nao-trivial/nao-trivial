import sqlite3

# Conecta ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('posts_instagram.db')
cursor = conn.cursor()

# Função para inserir um novo post
def inserir_post(topico, subtopico, nome_post, link_canva, legenda):
    cursor.execute('''
        INSERT INTO posts (topico, subtopico, nome_post, link_canva, legenda)
        VALUES (?, ?, ?, ?, ?)
    ''', (topico, subtopico, nome_post, link_canva, legenda))
    conn.commit()

# Função para visualizar posts
def visualizar_posts():
    cursor.execute("SELECT id, topico, subtopico, nome_post FROM posts")
    posts = cursor.fetchall()
    
    if not posts:
        print("\nNenhum post encontrado.")
        return
    
    print("\n--- Posts Cadastrados ---")
    for post in posts:
        print(f"ID: {post[0]} | Tópico: {post[1]} | Subtópico: {post[2]} | Nome do Post: {post[3]}")
    
    try:
        post_id = int(input("\nDigite o ID do post que deseja visualizar ou 0 para voltar: "))
        if post_id == 0:
            return
        
        # Opção de exibição de link ou legenda
        escolha_visualizacao = input("Digite '1' para visualizar o link ou '2' para visualizar a legenda: ")
        
        if escolha_visualizacao == '1':
            cursor.execute("SELECT link_canva FROM posts WHERE id = ?", (post_id,))
            link = cursor.fetchone()
            if link:
                print(f"\nLink do Canva: {link[0]}")
            else:
                print("Post não encontrado.")
        
        elif escolha_visualizacao == '2':
            cursor.execute("SELECT legenda FROM posts WHERE id = ?", (post_id,))
            legenda = cursor.fetchone()
            if legenda:
                print(f"\nLegenda do Post:\n{legenda[0]}")
            else:
                print("Post não encontrado.")
        
        else:
            print("Opção inválida.")
    
    except ValueError:
        print("ID inválido.")

# Função para exibir o menu e inserir posts
def menu_insercao():
    while True:
        print("\n--- Menu de Inserção de Posts ---")
        print("1. Inserir novo post")
        print("2. Visualizar post")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # Coleta dados do usuário
            topico = input("Digite o Tópico: ")
            subtopico = input("Digite o Subtópico: ")
            nome_post = input("Digite o Nome do Post: ")
            link_canva = input("Digite o Link do Post no Canva: ")
            print("Digite a Legenda do Post (finalize com uma linha vazia): ")
            
            # Coleta a legenda com múltiplas linhas
            legenda = ""
            while True:
                linha = input()
                if linha == "":
                    break
                legenda += linha + "\n"
            
            # Insere o post no banco de dados
            inserir_post(topico, subtopico, nome_post, link_canva, legenda)
            print("\nPost inserido com sucesso!")
        
        elif escolha == '2':
            visualizar_posts()
        
        elif escolha == '3':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu de inserção
menu_insercao()

# Fecha a conexão com o banco de dados ao final do programa
conn.close()
