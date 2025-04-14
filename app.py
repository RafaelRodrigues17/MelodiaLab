from flask import Flask, render_template, request, url_for, redirect, flash, session
import database

database.criar_tabelas()

app = Flask(__name__)
app.secret_key = "chave_muito_segura"

# Cria um dicionário e usuários e senha, SERÁ MIGRADO PARA O BANCO DE DADOS
@app.route('/') #rota para a página inicial
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

# VERFIFICAR O LOGIN
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form  # Coletando os dados do formulário de login
        # Chamando a função 'login' do arquivo database para verificar a senha
        if database.login(form) == True:
            session['usuario'] = form['email'] # Armazena o email do usuário na sessão
            return redirect(url_for('home'))
        else:
            return "Ocorreu um erro ao fazer o login do usuário"  # Caso contrário, exibe mensagem de erro
    else:
        return render_template('login.html')  # Se for GET, renderiza o formulário de login

# Rota de cadastro ('/cadastro') que também pode ser acessada por GET ou POST
@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        form = request.form  # Coletando os dados do formulário de cadastro
        # Chamando a função 'criar_usuario' do arquivo database para cadastrar o usuário
        if database.criar_usuario(form) == True:
            return render_template('login.html')  # Se cadastro for bem-sucedido, redireciona para o login
        else:
            return "Ocorreu um erro ao cadastrar usuário"  # Caso contrário, exibe mensagem de erro
    else:
        return render_template('cadastro.html')  # Se for GET, renderiza o formulário de cadastro
 
@app.route('/excluir_usuario')
def excluir_usuario():
    email = session['usuario']
    
    if database.excluir_usuario(email):
        return redirect(url_for('login'))
    else:
        return "Ocorreu um erro ao excluir o usuário"
    
@app.route('/nova_musica', methods=["GET", "POST"])
def nova_musica():
    if request.method == "POST":
        form = request.form
        if database.nova_musica(form):
            return redirect(url_for('home'))  # redireciona para a função `home`
        else:
            return "Ocorreu um erro ao criar a música"
    else:
        return render_template('nova_musica.html')

    
# parte principal do programa
if __name__ == '__main__':
    app.run(debug=True) 