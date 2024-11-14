import sqlite3

class BancoDadosPeticao:
    def __init__(self, nome_banco='peticao_parque_gunnar.db'):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        # Cria a tabela de entrevistas se não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS entrevistas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                bairro TEXT,
                renda_media_familiar REAL,
                raca TEXT,
                genero TEXT,
                conhece_parque BOOLEAN,
                importancia_ecologica TEXT,
                concorda_peticao BOOLEAN,
                comentario TEXT
            )
        ''')
        self.conn.commit()

    def inserir_entrevista(self, nome, idade, bairro, renda_media_familiar, raca, genero, conhece_parque, importancia_ecologica, concorda_peticao, comentario):
        self.cursor.execute('''
            INSERT INTO entrevistas (
                nome, idade, bairro, renda_media_familiar, raca, genero, 
                conhece_parque, importancia_ecologica, concorda_peticao, comentario
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, idade, bairro, renda_media_familiar, raca, genero, conhece_parque, importancia_ecologica, concorda_peticao, comentario))
        self.conn.commit()
        print("Entrevista cadastrada com sucesso!")

    def visualizar_entrevistas(self):
        self.cursor.execute("SELECT id, nome, idade, bairro, conhece_parque, concorda_peticao FROM entrevistas")
        return self.cursor.fetchall()

    def visualizar_detalhes_entrevista(self, entrevista_id):
        self.cursor.execute("SELECT nome, idade, bairro, renda_media_familiar, raca, genero, importancia_ecologica, comentario FROM entrevistas WHERE id = ?", (entrevista_id,))
        return self.cursor.fetchone()

    def fechar_conexao(self):
        self.conn.close()
