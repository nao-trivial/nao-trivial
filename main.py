from engine import inserir_post, visualizar_posts, visualizar_link_ou_legenda, listar_subtopicos_ou_posts, fechar_conexao

def menu_insercao():
    while True:
        print("\n--- Menu de Inserção de Posts ---")
        print("1. Inserir novo post")
        print("2. Visualizar post")
        print("3. Listar subtópicos ou nomes de posts")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            topico = input("Digite o Tópico: ")
            subtopico = input("Digite o Subtópico: ")
            nome_post = input("Digite o Nome do Post: ")
            link_canva = input("Digite o Link do Post no Canva: ")
            print("Digite a Legenda do Post (finalize com uma linha vazia): ")
            
            legenda = ""
            while True:
                linha = input()
                if linha == "":
                    break
                legenda += linha + "\n"
            
            inserir_post(topico, subtopico, nome_post, link_canva, legenda)
            print("\nPost inserido com sucesso!")
        
        elif escolha == '2':
            posts = visualizar_posts()
            if not posts:
                print("\nNenhum post encontrado.")
                continue
            
            print("\n--- Posts Cadastrados ---")
            for post in posts:
                print(f"ID: {post[0]} | Tópico: {post[1]} | Subtópico: {post[2]} | Nome do Post: {post[3]}")
            
            try:
                post_id = int(input("\nDigite o ID do post que deseja visualizar ou 0 para voltar: "))
                if post_id == 0:
                    continue
                
                escolha_visualizacao = input("Digite '1' para visualizar o link ou '2' para visualizar a legenda: ")
                resultado = visualizar_link_ou_legenda(post_id, escolha_visualizacao)
                
                if resultado:
                    print(f"\n{('Link do Canva' if escolha_visualizacao == '1' else 'Legenda do Post')}: {resultado[0]}")
                else:
                    print("Post não encontrado.")
            
            except ValueError:
                print("ID inválido.")
        
        elif escolha == '3':
            print("\n--- Listar Subtópicos ou Nomes de Posts ---")
            print("1. Listar todos os subtópicos dentro de um tópico")
            print("2. Listar todos os nomes de posts dentro de um subtópico")
            
            opcao_listagem = input("Escolha uma opção: ")
            termo = input("Digite o Tópico ou Subtópico: ")
            resultados = listar_subtopicos_ou_posts(opcao_listagem, termo)
            
            if resultados:
                print(f"\nResultados para '{termo}':")
                for resultado in resultados:
                    print(f"- {resultado[0]}")
            else:
                print(f"Nenhum resultado encontrado para '{termo}'.")
        
        elif escolha == '4':
            print("Saindo do programa.")
            fechar_conexao()
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu de inserção
menu_insercao()
