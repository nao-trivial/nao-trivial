import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('posts_instagram.db')
cursor = conn.cursor()

# Cria a tabela de posts se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topico TEXT,
        subtopico TEXT,
        nome_post TEXT,
        link_canva TEXT,
        legenda TEXT
    )
''')

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
    return cursor.fetchall()

def visualizar_link_ou_legenda(post_id, escolha):
    if escolha == '1':
        cursor.execute("SELECT link_canva FROM posts WHERE id = ?", (post_id,))
    elif escolha == '2':
        cursor.execute("SELECT legenda FROM posts WHERE id = ?", (post_id,))
    return cursor.fetchone()

# Função para listar subtópicos ou nomes de posts
def listar_subtopicos_ou_posts(escolha, termo):
    if escolha == '1':
        cursor.execute("SELECT DISTINCT subtopico FROM posts WHERE topico = ?", (termo,))
        return cursor.fetchall()
    elif escolha == '2':
        cursor.execute("SELECT nome_post FROM posts WHERE subtopico = ?", (termo,))
        return cursor.fetchall()

# Função para fechar a conexão com o banco de dados
def fechar_conexao():
    conn.close()
