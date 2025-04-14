import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco():
    conexao = sqlite3.connect("musicas.db")
    return conexao
# Função para criar as tabelas do banco de dados, caso não existam
def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Criando a tabela de usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                   (email TEXT PRIMARY KEY, nome TEXT, senha TEXT)''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos_musicais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_musica TEXT,
            artista TEXT,
            status TEXT,
            letra TEXT,
            caminho_capa TEXT,
            email_usuario TEXT,
            FOREIGN KEY(email_usuario) REFERENCES usuarios(email))
    ''')
    conexao.commit()
    
def criar_usuario(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Verificando se o e-mail já está cadastrado
    cursor.execute('''SELECT COUNT(email) FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    # Se o e-mail já existir, retorna False
    if quantidade_de_emails[0] > 0:
        print("E-mail já cadastrado! Tente novamente")
        return False
    
    # Criptografando a senha do usuário
    senha_criptografada = generate_password_hash(formulario['senha'])
    
    # Inserindo os dados do novo usuário no banco
    cursor.execute('''INSERT INTO usuarios(email, nome, senha) 
                   VALUES (?, ?, ?)''', (formulario['email'], formulario['usuario'], senha_criptografada))
    
    conexao.commit()
    return True

def login(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Verificando se o e-mail existe no banco de dados
    cursor.execute('''SELECT COUNT(email) FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    # Se o e-mail não estiver cadastrado, retorna False
    if quantidade_de_emails[0] == 0:
        print("E-mail não cadastrado! Tente novamente")
        return False
    
    # Obtendo a senha criptografada do usuário no banco
    cursor.execute('''SELECT senha FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    senha_criptografada = cursor.fetchone()
    
    # Verificando se a senha fornecida corresponde à senha armazenada
    return check_password_hash(senha_criptografada[0], formulario['senha'])

def excluir_usuario(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''DELETE FROM projetos_musicais WHERE email_usuario=?''', (email,))
    cursor.execute('''DELETE FROM usuarios WHERE email=?''', (email,))
    conexao.commit()
    return True

def nova_musica(formulario):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        nome_musica = formulario.get('nome_musica')
        artista = formulario.get('artista')
        status = formulario.get('status')
        letra = formulario.get('letra')
        email_usuario = formulario.get('email_usuario')  # ou pegue do session depois

        cursor.execute('''
            INSERT INTO projetos_musicais (nome_musica, artista, status, letra, caminho_capa, email_usuario)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome_musica, artista, status, letra, '', email_usuario))

        conexao.commit()
        print("Nova música salva!")
        return True
    except Exception as e:
        print("Erro ao salvar música:", e)
        return False

# PARTE PRINCIPAL DO PROGRAMA
if __name__ == '__main__':
   criar_tabelas()